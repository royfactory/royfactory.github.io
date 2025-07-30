#!/usr/bin/env python3
import os
import re
import glob
import yaml

def clean_markdown_file(filepath):
    """Clean and standardize markdown file format for Hugo"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split front matter and content
    if not content.startswith('---'):
        return
    
    # Find the end of front matter
    end_marker = content.find('---', 3)
    if end_marker == -1:
        return
    
    front_matter_raw = content[3:end_marker].strip()
    body = content[end_marker + 3:].strip()
    
    # Parse and clean front matter
    try:
        fm_data = yaml.safe_load(front_matter_raw)
        if not fm_data:
            fm_data = {}
    except:
        # If YAML parsing fails, return original
        return
    
    # Remove Jekyll/unwanted fields
    unwanted_fields = ['layout', 'organiser', 'toc', 'cover']
    for field in unwanted_fields:
        fm_data.pop(field, None)
    
    # Standardize image field (remove duplicate if exists)
    if 'image' not in fm_data and 'cover' in unwanted_fields:
        # Keep the first image field we find
        pass
    
    # Add Hugo standard fields
    fm_data['ShowToc'] = True
    fm_data['draft'] = False
    
    # Convert categories to list format if string
    if 'categories' in fm_data and isinstance(fm_data['categories'], str):
        fm_data['categories'] = [fm_data['categories']]
    
    # Clean body content
    body_lines = body.split('\n')
    cleaned_body_lines = []
    
    skip_next = False
    for i, line in enumerate(body_lines):
        if skip_next:
            skip_next = False
            continue
            
        # Skip Jekyll ToC syntax and unwanted separators
        stripped = line.strip()
        if stripped in ['* ToC', '{:toc}', '--']:
            continue
        
        # Skip empty lines after removed content
        if stripped == '' and i > 0 and body_lines[i-1].strip() in ['* ToC', '{:toc}', '--']:
            continue
            
        cleaned_body_lines.append(line)
    
    # Rebuild front matter as YAML
    new_front_matter = yaml.dump(fm_data, default_flow_style=False, allow_unicode=True).strip()
    
    # Rebuild content
    new_content = f"---\n{new_front_matter}\n---\n\n{chr(10).join(cleaned_body_lines)}"
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Process all markdown files in content/posts
for filepath in glob.glob('content/posts/**/*.md', recursive=True):
    try:
        clean_markdown_file(filepath)
        print(f"✓ Cleaned: {filepath}")
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")

print("✅ All files processed!")
