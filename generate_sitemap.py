#!/usr/bin/env python3
"""
Static sitemap.xml generator for Jekyll blog
Generates sitemap without Jekyll processing to avoid script tag injection
"""

import os
import re
from datetime import datetime
import glob

def parse_post_frontmatter(filepath):
    """Extract frontmatter from markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        if content.startswith('---'):
            end_pos = content.find('---', 3)
            if end_pos != -1:
                frontmatter = content[3:end_pos]
                
                # Parse date and title
                date_match = re.search(r'^date:\s*(.+)$', frontmatter, re.MULTILINE)
                title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
                
                if date_match:
                    date_str = date_match.group(1).strip()
                    # Parse date (handle various formats)
                    try:
                        if 'T' in date_str:
                            post_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                        else:
                            post_date = datetime.strptime(date_str, '%Y-%m-%d')
                    except:
                        # Extract date from filename as fallback
                        filename = os.path.basename(filepath)
                        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
                        if date_match:
                            post_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
                        else:
                            return None
                    
                    # Only include posts that are not in the future
                    if post_date.date() <= datetime.now().date():
                        return {
                            'date': post_date,
                            'title': title_match.group(1).strip().strip('"') if title_match else 'Untitled',
                            'path': filepath
                        }
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    
    return None

def generate_url_from_path(filepath):
    """Generate URL from file path"""
    # Remove _posts/ prefix and .md suffix
    relative_path = filepath.replace('_posts/', '').replace('.md', '')
    
    # Extract date and title from filename
    filename = os.path.basename(relative_path)
    date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)', filename)
    
    if date_match:
        year, month, day, slug = date_match.groups()
        # Get category from directory structure
        category = os.path.dirname(relative_path)
        if category:
            return f"/{category}/{year}/{month}/{day}/{slug}.html"
        else:
            return f"/{year}/{month}/{day}/{slug}.html"
    
    return None

def main():
    """Generate static sitemap.xml"""
    
    print("Generating static sitemap.xml...")
    
    # Collect all posts
    posts = []
    post_files = glob.glob('_posts/**/*.md', recursive=True)
    
    for filepath in post_files:
        post_info = parse_post_frontmatter(filepath)
        if post_info:
            url = generate_url_from_path(filepath)
            if url:
                post_info['url'] = url
                posts.append(post_info)
    
    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate sitemap XML
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://royfactory.github.io</loc>
    <lastmod>{current_date}</lastmod>
    <priority>1.0</priority>
  </url>
'''.format(current_date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00'))

    # Add posts
    for post in posts:
        sitemap_content += f'''  <url>
    <loc>https://royfactory.github.io{post['url']}</loc>
    <lastmod>{post['date'].strftime('%Y-%m-%dT%H:%M:%S+09:00')}</lastmod>
  </url>
'''

    # Add static pages
    static_pages = [
        '/about/',
        '/archive/',
        '/apps/',
    ]
    
    for page_url in static_pages:
        sitemap_content += f'''  <url>
    <loc>https://royfactory.github.io{page_url}</loc>
  </url>
'''

    sitemap_content += '</urlset>\n'
    
    # Write sitemap.xml
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print(f"Generated sitemap.xml with {len(posts)} posts")
    print("Posts included:")
    for i, post in enumerate(posts[:10]):  # Show first 10
        print(f"  {i+1}. {post['date'].strftime('%Y-%m-%d')} - {post['title']}")
    if len(posts) > 10:
        print(f"  ... and {len(posts) - 10} more posts")

if __name__ == '__main__':
    main()
