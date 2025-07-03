#!/usr/bin/env python3
"""
SEO 개선을 위한 Jekyll 포스트 Front Matter 업데이트 스크립트
"""

import os
import re
import yaml
from pathlib import Path

# 포스트 디렉토리 설정
POSTS_DIR = Path("/Users/royzero/royfactory.github.io/_posts")

# SEO 키워드 매핑 (카테고리별)
SEO_KEYWORDS = {
    'ai': [
        'artificial intelligence', 'machine learning', 'deep learning', 'python',
        'data science', 'neural networks', 'AI tutorial', 'ML algorithms'
    ],
    'linux': [
        'linux', 'unix', 'bash', 'shell scripting', 'system administration',
        'command line', 'terminal', 'server management'
    ],
    'programming': [
        'programming', 'coding', 'software development', 'web development',
        'javascript', 'python', 'tutorial', 'best practices'
    ]
}

def extract_front_matter(content):
    """Front Matter 추출"""
    if content.startswith('---\n'):
        end_idx = content.find('\n---\n', 4)
        if end_idx != -1:
            front_matter_str = content[4:end_idx]
            body = content[end_idx + 5:]
            try:
                front_matter = yaml.safe_load(front_matter_str)
                return front_matter, body
            except yaml.YAMLError:
                return None, content
    return None, content

def generate_description(title, body, max_length=160):
    """제목과 본문을 기반으로 설명 생성"""
    # 본문에서 첫 번째 문단 추출 (마크다운 헤더 제외)
    lines = body.split('\n')
    content_lines = []
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('```'):
            content_lines.append(line)
            if len(' '.join(content_lines)) > max_length:
                break
    
    description = ' '.join(content_lines)
    if len(description) > max_length:
        description = description[:max_length-3] + '...'
    
    return description

def generate_keywords(title, tags, category):
    """제목, 태그, 카테고리를 기반으로 키워드 생성"""
    keywords = set()
    
    # 태그에서 키워드 추출
    if tags:
        if isinstance(tags, str):
            keywords.update(tags.split())
        elif isinstance(tags, list):
            keywords.update(tags)
    
    # 카테고리별 SEO 키워드 추가
    if category in SEO_KEYWORDS:
        keywords.update(SEO_KEYWORDS[category])
    
    # 제목에서 키워드 추출
    title_words = re.findall(r'\b\w+\b', title.lower())
    keywords.update(title_words)
    
    return ', '.join(sorted(list(keywords)))

def update_post_seo(file_path):
    """개별 포스트의 SEO 메타데이터 업데이트"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        front_matter, body = extract_front_matter(content)
        if not front_matter:
            print(f"⚠️  Front Matter를 찾을 수 없습니다: {file_path}")
            return False
        
        # 현재 값들
        title = front_matter.get('title', '')
        tags = front_matter.get('tags', [])
        category = front_matter.get('categories', '')
        cover = front_matter.get('cover', '/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg')
        
        # SEO 메타데이터 생성/업데이트
        if 'description' not in front_matter or not front_matter['description']:
            front_matter['description'] = generate_description(title, body)
        
        if 'keywords' not in front_matter or not front_matter['keywords']:
            front_matter['keywords'] = generate_keywords(title, tags, category)
        
        if 'image' not in front_matter:
            front_matter['image'] = cover
        
        # Front Matter 재구성
        new_front_matter = "---\n"
        new_front_matter += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
        new_front_matter += "---\n"
        
        # 파일 업데이트
        new_content = new_front_matter + body
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 업데이트 완료: {file_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ 오류 발생 {file_path}: {e}")
        return False

def main():
    """메인 실행 함수"""
    print("🚀 Jekyll 포스트 SEO 메타데이터 업데이트 시작...")
    
    # AI 포스트 파일들 찾기
    ai_posts = list(POSTS_DIR.glob("ai/*.md"))
    linux_posts = list(POSTS_DIR.glob("linux/*.md"))
    
    all_posts = ai_posts + linux_posts
    
    print(f"📁 총 {len(all_posts)}개 포스트 발견")
    
    success_count = 0
    for post_file in all_posts:
        if update_post_seo(post_file):
            success_count += 1
    
    print(f"\n🎉 완료! {success_count}/{len(all_posts)}개 포스트 업데이트됨")

if __name__ == "__main__":
    main()
