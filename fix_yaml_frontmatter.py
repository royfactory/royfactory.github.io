#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_yaml_frontmatter(file_path):
    """YAML frontmatter의 줄바꿈 문제 수정"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    if not (lines[0].strip() == '---'):
        return
    
    frontmatter_end = -1
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            frontmatter_end = i
            break
    
    if frontmatter_end == -1:
        return
    
    frontmatter_lines = lines[1:frontmatter_end]
    content_lines = lines[frontmatter_end + 1:]
    
    fixed_frontmatter = ['---']
    i = 0
    while i < len(frontmatter_lines):
        line = frontmatter_lines[i]
        
        # tags 라인 처리
        if line.startswith('tags:'):
            # 다음 줄들이 들여쓰기로 시작하면 합치기
            tags_line = line
            j = i + 1
            while j < len(frontmatter_lines) and frontmatter_lines[j].startswith('  '):
                tags_line += ' ' + frontmatter_lines[j].strip()
                j += 1
            
            # tags 라인을 올바른 형식으로 변환
            if '["' in tags_line:
                # 이미 배열 형식이면 그대로
                fixed_frontmatter.append(tags_line)
            else:
                # 문자열을 배열로 변환
                tags_value = tags_line.split(':', 1)[1].strip()
                tags = [f'"{tag.strip()}"' for tag in tags_value.split() if tag.strip()]
                fixed_frontmatter.append(f'tags: [{", ".join(tags)}]')
            
            i = j
        else:
            fixed_frontmatter.append(line)
            i += 1
    
    fixed_frontmatter.append('---')
    
    fixed_content = '\n'.join(fixed_frontmatter + content_lines)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"Fixed: {file_path}")

def main():
    posts_dir = Path('/Users/royzero/royfactory.github.io/content/posts')
    
    for md_file in posts_dir.glob('**/*.md'):
        fix_yaml_frontmatter(md_file)

if __name__ == "__main__":
    main()
    print("All YAML frontmatter issues fixed!")
