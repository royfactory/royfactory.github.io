#!/usr/bin/env python3
import os
import glob
import yaml
import re

def fix_yaml_frontmatter(filepath):
    """Fix YAML frontmatter issues in markdown files"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with frontmatter
        if not content.startswith('---'):
            return False
        
        # Find the end of frontmatter
        end_pos = content.find('\n---\n', 4)
        if end_pos == -1:
            end_pos = content.find('\n---\r\n', 4)
        if end_pos == -1:
            # Try to fix by finding the second ---
            lines = content.split('\n')
            end_line = -1
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    end_line = i
                    break
            
            if end_line == -1:
                print(f"❌ Cannot find end of frontmatter in {filepath}")
                return False
            
            end_pos = sum(len(line) + 1 for line in lines[:end_line])
        
        frontmatter_raw = content[4:end_pos].strip()
        body = content[end_pos + 4:].strip()
        
        # Try to parse YAML
        try:
            frontmatter_data = yaml.safe_load(frontmatter_raw)
            if frontmatter_data is None:
                frontmatter_data = {}
        except yaml.YAMLError as e:
            print(f"❌ YAML error in {filepath}: {e}")
            return False
        
        # Ensure required fields
        if 'ShowToc' not in frontmatter_data:
            frontmatter_data['ShowToc'] = True
        if 'draft' not in frontmatter_data:
            frontmatter_data['draft'] = False
        
        # Remove any content that accidentally got into the YAML
        for key in list(frontmatter_data.keys()):
            if isinstance(frontmatter_data[key], str) and ('##' in frontmatter_data[key] or 'draft: false' in frontmatter_data[key]):
                # This field contains markdown content, clean it
                clean_value = frontmatter_data[key].split('draft: false')[0].split('##')[0].strip()
                if clean_value:
                    frontmatter_data[key] = clean_value
                else:
                    del frontmatter_data[key]
        
        # Clean body - remove any stray frontmatter fields
        body_lines = body.split('\n')
        cleaned_body_lines = []
        
        for line in body_lines:
            # Skip lines that look like frontmatter fields in the body
            if re.match(r'^(draft|ShowToc|categories|tags|title|date|description|keywords|image):\s*', line):
                continue
            if line.strip() == 'draft: false':
                continue
            cleaned_body_lines.append(line)
        
        # Rebuild the file
        new_frontmatter = yaml.dump(frontmatter_data, default_flow_style=False, allow_unicode=True).strip()
        new_content = f"---\n{new_frontmatter}\n---\n\n{chr(10).join(cleaned_body_lines)}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

# Process all files
success_count = 0
error_count = 0

for filepath in glob.glob('content/posts/**/*.md', recursive=True):
    try:
        if fix_yaml_frontmatter(filepath):
            print(f"✅ Fixed: {filepath}")
            success_count += 1
        else:
            print(f"⚠️  Issues with: {filepath}")
            error_count += 1
    except Exception as e:
        print(f"❌ Failed: {filepath} - {e}")
        error_count += 1

print(f"\n🎉 Summary: {success_count} files fixed, {error_count} files had issues")
