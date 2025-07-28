#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

# Jekyll 포스트를 Hugo 포스트로 변환하는 스크립트

def convert_jekyll_frontmatter_to_hugo(content):
    """Jekyll frontmatter를 Hugo frontmatter로 변환"""
    lines = content.split('\n')
    if not (lines[0].strip() == '---'):
        return content
    
    frontmatter_end = -1
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            frontmatter_end = i
            break
    
    if frontmatter_end == -1:
        return content
    
    frontmatter_lines = lines[1:frontmatter_end]
    content_lines = lines[frontmatter_end + 1:]
    
    # Hugo frontmatter 변환
    hugo_frontmatter = ['---']
    processed_keys = set()
    
    for line in frontmatter_lines:
        if line.strip() == '':
            continue
            
        # Jekyll 특정 필드들을 Hugo로 변환
        if line.startswith('layout:'):
            # layout은 제거
            continue
        elif line.startswith('categories:'):
            if 'categories' not in processed_keys:
                # categories를 tags로 변환
                value = line.split(':', 1)[1].strip()
                hugo_frontmatter.append(f'categories: ["{value}"]')
                processed_keys.add('categories')
        elif line.startswith('cover:') or line.startswith('image:'):
            if 'cover' not in processed_keys:
                # cover/image 필드 처리
                value = line.split(':', 1)[1].strip()
                hugo_frontmatter.append(f'cover:')
                hugo_frontmatter.append(f'  image: {value}')
                processed_keys.add('cover')
        elif line.startswith('tags:'):
            if 'tags' not in processed_keys:
                # tags를 배열 형식으로 변환
                value = line.split(':', 1)[1].strip()
                # 공백으로 구분된 태그들을 배열로 변환 (쉼표나 공백으로 구분)
                if ',' in value:
                    tags = [f'"{tag.strip()}"' for tag in value.split(',') if tag.strip()]
                else:
                    tags = [f'"{tag.strip()}"' for tag in value.split() if tag.strip()]
                hugo_frontmatter.append(f'tags: [{", ".join(tags)}]')
                processed_keys.add('tags')
        elif line.startswith('toc:'):
            # TOC 설정
            if 'toc' not in processed_keys:
                hugo_frontmatter.append('ShowToc: true')
                processed_keys.add('toc')
        elif line.startswith('organiser:'):
            # organiser는 author로 변환
            if 'author' not in processed_keys:
                value = line.split(':', 1)[1].strip()
                hugo_frontmatter.append(f'author: {value}')
                processed_keys.add('author')
        else:
            # 키 추출
            key = line.split(':', 1)[0].strip()
            if key not in processed_keys:
                # 나머지 필드들은 그대로 유지
                hugo_frontmatter.append(line)
                processed_keys.add(key)
    
    # draft: false 추가
    if 'draft' not in processed_keys:
        hugo_frontmatter.append('draft: false')
    
    hugo_frontmatter.append('---')
    
    # Jekyll TOC 제거 및 Hugo 형식으로 변환
    processed_content = []
    skip_toc = False
    
    for line in content_lines:
        # Jekyll TOC 제거
        if '* ToC' in line or '{:toc}' in line:
            skip_toc = True
            continue
        if skip_toc and line.strip() == '':
            continue
        if skip_toc and line.startswith('#'):
            skip_toc = False
        
        if not skip_toc:
            processed_content.append(line)
    
    return '\n'.join(hugo_frontmatter + processed_content)

def convert_posts():
    """Jekyll 포스트들을 Hugo 포스트로 변환"""
    jekyll_posts_dir = Path('/Users/royzero/royfactory.github.io/_posts')
    hugo_posts_dir = Path('/Users/royzero/royfactory.github.io/content/posts')
    
    for category_dir in jekyll_posts_dir.iterdir():
        if not category_dir.is_dir():
            continue
            
        hugo_category_dir = hugo_posts_dir / category_dir.name
        hugo_category_dir.mkdir(exist_ok=True)
        
        for post_file in category_dir.glob('*.md'):
            print(f"Converting {post_file.name}...")
            
            # 파일 내용 읽기
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Jekyll frontmatter를 Hugo frontmatter로 변환
            converted_content = convert_jekyll_frontmatter_to_hugo(content)
            
            # Hugo 포스트 파일로 저장
            hugo_post_file = hugo_category_dir / post_file.name
            with open(hugo_post_file, 'w', encoding='utf-8') as f:
                f.write(converted_content)
            
            print(f"Converted: {hugo_post_file}")

if __name__ == "__main__":
    convert_posts()
    print("Jekyll to Hugo conversion completed!")
