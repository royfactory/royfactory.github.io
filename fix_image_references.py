#!/usr/bin/env python3
"""
존재하지 않는 이미지 참조를 제거하여 Mixed Content 오류를 방지하는 스크립트
"""

import os
import re
import glob

def fix_image_references():
    # content/posts 폴더의 모든 마크다운 파일을 찾습니다
    pattern = "/Users/royzero/royfactory.github.io/content/posts/**/*.md"
    markdown_files = glob.glob(pattern, recursive=True)
    
    print(f"Found {len(markdown_files)} markdown files")
    
    for file_path in markdown_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 존재하지 않는 이미지 참조 패턴들을 제거
            # 1. cover.image 제거
            content = re.sub(r'cover:\s*\n\s*image:\s*/img/[^\n]+\n', '', content, flags=re.MULTILINE)
            
            # 2. 단독 image 라인 제거 (존재하지 않는 이미지)
            lines = content.split('\n')
            new_lines = []
            
            for line in lines:
                # image: /img/로 시작하는 라인 체크
                if re.match(r'\s*image:\s*/img/', line):
                    # 이미지 경로 추출
                    img_match = re.search(r'/img/([^"\s]+)', line)
                    if img_match:
                        img_path = img_match.group(1)
                        full_img_path = f"/Users/royzero/royfactory.github.io/img/{img_path}"
                        
                        # 파일이 존재하지 않으면 라인 제거
                        if not os.path.exists(full_img_path):
                            print(f"Removing non-existent image reference: {img_path} from {file_path}")
                            continue
                
                new_lines.append(line)
            
            content = '\n'.join(new_lines)
            
            # 변경사항이 있으면 파일 저장
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed: {file_path}")
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_image_references()
    print("Image reference cleanup completed!")
