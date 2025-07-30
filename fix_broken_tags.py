#!/usr/bin/env python3
import re
import glob

def fix_yaml_tags(filepath):
    """Fix broken YAML tags format"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match broken tags like: tags: [ai machine-learning]python
        pattern = r'(tags: \[[^\]]+\])(\w+)'
        
        def replacement(match):
            tags_part = match.group(1)
            extra_word = match.group(2)
            # Add the extra word to the tags list
            tags_part = tags_part[:-1] + f', {extra_word}]'
            return tags_part
        
        # Apply the fix
        fixed_content = re.sub(pattern, replacement, content)
        
        if fixed_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

# Process problematic files
files_to_fix = [
    'content/posts/ai/2025-07-11-q-learning-cartpole-tutorial.md',
    'content/posts/ai/2025-06-29-what-is-automl.md',
    'content/posts/ai/2025-06-30-what-is-langchain.md',
    'content/posts/ai/2025-07-10-dqn-cartpole-deep-rl-start.md',
    'content/posts/ai/2025-07-01-automl-h2o-intro.md',
    'content/posts/cloud/2025-07-28-kubernetes-service-types.md',
    'content/posts/cloud/2025-07-15-why-use-kubernetes.md',
    'content/posts/cloud/2025-07-29-kubernetes-service-types-summary.md'
]

fixed_count = 0
for filepath in files_to_fix:
    if fix_yaml_tags(filepath):
        print(f"✅ Fixed: {filepath}")
        fixed_count += 1

print(f"\n🎉 Fixed {fixed_count} files!")
