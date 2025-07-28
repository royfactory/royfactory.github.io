#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def convert_app_privacy_pages():
    """앱의 privacy 페이지들을 Hugo 형식으로 변환"""
    
    # 앱 리스트
    apps = ['bookmark', 'boxingtimer', 'growthliubei', 'myvoca', 'planktime', 'scoreboard', 'tableclock']
    
    base_path = Path('/Users/royzero/royfactory.github.io')
    apps_source = base_path / 'apps'
    content_apps = base_path / 'content' / 'apps'
    
    for app in apps:
        print(f"Processing {app}...")
        
        # 소스 파일 경로
        source_file = apps_source / app / 'privacy.md'
        
        # 대상 디렉토리 생성
        target_dir = content_apps / app
        target_dir.mkdir(exist_ok=True)
        
        # privacy.md 파일이 존재하는지 확인
        if source_file.exists():
            # 파일 내용 읽기
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Jekyll frontmatter를 Hugo frontmatter로 변환
            lines = content.split('\n')
            if lines[0].strip() == '---':
                # frontmatter 끝 찾기
                frontmatter_end = -1
                for i, line in enumerate(lines[1:], 1):
                    if line.strip() == '---':
                        frontmatter_end = i
                        break
                
                if frontmatter_end > 0:
                    # Hugo frontmatter 생성
                    hugo_frontmatter = [
                        '---',
                        'title: "개인정보처리방침"',
                        'date: 2024-01-01',
                        'draft: false',
                        'layout: "single"',
                        f'url: "/apps/{app}/privacy/"',
                        '---'
                    ]
                    
                    # 나머지 콘텐츠
                    content_lines = lines[frontmatter_end + 1:]
                    
                    # 최종 콘텐츠 생성
                    final_content = '\n'.join(hugo_frontmatter + content_lines)
                    
                    # 대상 파일에 쓰기
                    target_file = target_dir / 'privacy.md'
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(final_content)
                    
                    print(f"  ✓ Created: {target_file}")
                else:
                    print(f"  ✗ No valid frontmatter in {source_file}")
            else:
                print(f"  ✗ No frontmatter found in {source_file}")
        else:
            print(f"  ✗ Source file not found: {source_file}")
            
            # 기본 privacy 페이지 생성
            default_content = f"""---
title: "개인정보처리방침"
date: 2024-01-01
draft: false
layout: "single"
url: "/apps/{app}/privacy/"
---

# {app.title()} 개인정보처리방침

이 페이지는 {app.title()} 앱의 개인정보처리방침입니다.

## 개인정보 수집 및 이용

본 앱은 개인정보를 수집하지 않습니다.

## 문의사항

개인정보처리방침에 대한 문의사항이 있으시면 rozyero0717@gmail.com으로 연락주세요.
"""
            target_file = target_dir / 'privacy.md'
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(default_content)
            
            print(f"  ✓ Created default: {target_file}")

if __name__ == "__main__":
    convert_app_privacy_pages()
    print("Apps privacy pages conversion completed!")
