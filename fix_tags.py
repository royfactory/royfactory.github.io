#!/usr/bin/env python3
import os
import glob
import yaml
import re

def fix_tags_categories(filepath):
    """Fix tags and categories format in YAML frontmatter"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and body
        if not content.startswith('---'):
            return False
            
        end_pos = content.find('\n---\n', 4)
        if end_pos == -1:
            return False
            
        frontmatter_raw = content[4:end_pos]
        body = content[end_pos + 4:]
        
        # Parse YAML
        try:
            data = yaml.safe_load(frontmatter_raw)
        except yaml.YAMLError:
            return False
            
        if not data:
            return False
        
        # Fix tags - convert string to list
        if 'tags' in data:
            if isinstance(data['tags'], str):
                # Split by spaces and clean
                tags = data['tags'].split()
                data['tags'] = tags
            elif isinstance(data['tags'], list):
                # Flatten any nested structure and clean
                flat_tags = []
                for tag in data['tags']:
                    if isinstance(tag, str):
                        flat_tags.extend(tag.split())
                    else:
                        flat_tags.append(str(tag))
                data['tags'] = flat_tags
        
        # Fix categories - convert string to list
        if 'categories' in data:
            if isinstance(data['categories'], str):
                data['categories'] = [data['categories']]
        
        # Rebuild file
        new_frontmatter = yaml.dump(data, default_flow_style=False, allow_unicode=True).strip()
        new_content = f"---\n{new_frontmatter}\n---{body}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

# Process all files
success_count = 0
for filepath in glob.glob('content/posts/**/*.md', recursive=True):
    if fix_tags_categories(filepath):
        print(f"✅ Fixed: {filepath}")
        success_count += 1

print(f"\n🎉 {success_count} files processed successfully!")
