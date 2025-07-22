#!/usr/bin/env python3
import os
import re
import glob

def add_toc_to_file(file_path):
    """파일에 TOC 섹션 추가 또는 수정"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # front matter가 있는지 확인
        if not content.startswith('---'):
            return False
        
        # toc: true가 있는지 확인
        if 'toc: true' not in content:
            return False
        
        # 이미 Kramdown TOC가 있는지 확인
        if '* TOC\n{:toc}' in content:
            print(f"✅ Already has Kramdown TOC: {file_path}")
            return False
        
        # 기존 TOC 섹션 패턴 찾기 및 교체
        toc_pattern = r'## Table of Contents\n(?:(?:\d+\..*\n)+|(?:\*.*\n)+|(?:-.*\n)+)'
        
        if re.search(toc_pattern, content):
            # 기존 TOC 섹션을 Kramdown 형식으로 교체
            new_toc = "## Table of Contents\n\n* TOC\n{:toc}\n"
            content = re.sub(toc_pattern, new_toc, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed existing TOC: {file_path}")
            return True
        
        # TOC 섹션이 없는 경우, 첫 번째 ## 헤딩 앞에 추가
        # front matter 다음 첫 번째 내용 찾기
        front_matter_end = content.find('---', 3) + 3
        if front_matter_end > 3:
            after_front_matter = content[front_matter_end:].lstrip()
            
            # 첫 번째 ## 헤딩 찾기 (# 헤딩은 제외)
            first_heading_match = re.search(r'\n## ', after_front_matter)
            
            if first_heading_match:
                # 첫 번째 ## 헤딩 앞에 TOC 섹션 추가
                insert_pos = front_matter_end + first_heading_match.start()
                
                toc_section = "\n## Table of Contents\n\n* TOC\n{:toc}\n\n---\n"
                
                new_content = content[:insert_pos] + toc_section + content[insert_pos+1:]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Added new TOC: {file_path}")
                return True
        
        print(f"⚠️  Could not add TOC to: {file_path}")
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
        if add_toc_to_file(file_path):
            fixed_count += 1
    
    print(f"\n📊 Summary: Fixed {fixed_count} files out of {len(post_files)} total files")

if __name__ == "__main__":
    main()
