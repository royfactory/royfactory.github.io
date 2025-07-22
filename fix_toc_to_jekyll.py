#!/usr/bin/env python3
import os
import re
import glob

def fix_toc_to_jekyll_toc(file_path):
    """파일에서 Kramdown TOC를 Jekyll TOC 태그로 변경"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # toc: true가 있는지 확인
        if 'toc: true' not in content:
            return False
        
        # Kramdown TOC 패턴을 Jekyll TOC 태그로 교체
        kramdown_toc_pattern = r'## Table of Contents\n\n\* TOC\n\{:toc\}'
        
        if re.search(kramdown_toc_pattern, content):
            # Kramdown TOC를 Jekyll TOC 태그로 교체
            new_toc = "## Table of Contents\n\n{% toc %}"
            content = re.sub(kramdown_toc_pattern, new_toc, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed TOC: {file_path}")
            return True
        else:
            print(f"⚠️  No Kramdown TOC found: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    # _posts 디렉토리에서 모든 .md 파일 찾기
    post_files = glob.glob('/Users/royzero/royfactory.github.io/_posts/**/*.md', recursive=True)
    
    print(f"Found {len(post_files)} markdown files")
    
    fixed_count = 0
    for file_path in post_files:
        if fix_toc_to_jekyll_toc(file_path):
            fixed_count += 1
    
    print(f"\n📊 Summary: Fixed {fixed_count} files out of {len(post_files)} total files")

if __name__ == "__main__":
    main()
