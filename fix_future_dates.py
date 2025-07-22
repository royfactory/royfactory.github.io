#!/usr/bin/env python3
import os
import re
import glob
from datetime import datetime, date

def fix_future_dates(file_path):
    """미래 날짜를 현재 날짜 이전으로 수정"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 현재 날짜
        today = date.today()
        current_date_str = today.strftime('%Y-%m-%d')
        
        # front matter에서 date 찾기
        date_pattern = r'date: (\d{4}-\d{2}-\d{2})'
        date_match = re.search(date_pattern, content)
        
        if date_match:
            post_date_str = date_match.group(1)
            post_date = datetime.strptime(post_date_str, '%Y-%m-%d').date()
            
            # 미래 날짜인 경우
            if post_date > today:
                # 파일명에서 날짜 추출
                filename = os.path.basename(file_path)
                filename_date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
                
                if filename_date_match:
                    filename_date = filename_date_match.group(1)
                    filename_date_obj = datetime.strptime(filename_date, '%Y-%m-%d').date()
                    
                    # 적절한 과거 날짜 계산 (오늘로부터 역순으로)
                    if filename_date_obj > today:
                        # 파일명 날짜도 미래인 경우, 순차적으로 과거 날짜 할당
                        # 예: 2025-07-23 -> 2025-07-16, 2025-07-24 -> 2025-07-15 등
                        days_diff = (filename_date_obj - today).days
                        new_date = date(2025, 7, 22 - days_diff)
                        if new_date < date(2025, 7, 1):
                            new_date = date(2025, 7, 1)
                    else:
                        new_date = filename_date_obj
                else:
                    new_date = today
                
                new_date_str = new_date.strftime('%Y-%m-%d')
                
                # 날짜 교체
                new_content = re.sub(date_pattern, f'date: {new_date_str}', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ Fixed date: {file_path}")
                print(f"   {post_date_str} → {new_date_str}")
                return True
        
        return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    # _posts 디렉토리에서 모든 .md 파일 찾기
    post_files = glob.glob('/Users/royzero/royfactory.github.io/_posts/**/*.md', recursive=True)
    
    print(f"Found {len(post_files)} markdown files")
    print(f"Current date: {date.today()}")
    print("Checking for future dates...\n")
    
    fixed_count = 0
    for file_path in post_files:
        if fix_future_dates(file_path):
            fixed_count += 1
    
    print(f"\n📊 Summary: Fixed {fixed_count} files with future dates")

if __name__ == "__main__":
    main()
