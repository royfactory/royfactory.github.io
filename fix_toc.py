#!/usr/bin/env python3
import os
import re
import glob

def fix_toc_in_file(file_path):
    """파일에서 TOC 섹션을 Kramdown 형식으로 변경"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # TOC 섹션 패턴 찾기
        # ## Table of Contents 다음에 오는 리스트를 찾아서 Kramdown TOC로 교체
        toc_pattern = r'## Table of Contents\n(?:(?:\d+\..*\n)+|(?:\*.*\n)+|(?:-.*\n)+)'
        
        if re.search(toc_pattern, content):
            # TOC 섹션을 Kramdown 형식으로 교체
            new_toc = "## Table of Contents\n\n* TOC\n{:toc}\n"
            content = re.sub(toc_pattern, new_toc, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {file_path}")
            return True
        else:
            # TOC 섹션이 없는 파일에는 "* TOC\n{:toc}" 패턴만 확인
            simple_toc_pattern = r'\* TOC\n\{:toc\}'
            if not re.search(simple_toc_pattern, content) and 'toc: true' in content:
                print(f"⚠️  No TOC section found but toc: true exists: {file_path}")
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
        if fix_toc_in_file(file_path):
            fixed_count += 1
    
    print(f"\n📊 Summary: Fixed {fixed_count} files out of {len(post_files)} total files")

if __name__ == "__main__":
    main()
