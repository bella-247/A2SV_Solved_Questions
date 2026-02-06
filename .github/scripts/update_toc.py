#!/usr/bin/env python3
"""
Script to automatically generate and update the Table of Contents in README.md
based on Python solution files in the repository.
"""

import os
import re
from pathlib import Path
from urllib.parse import quote
from typing import Dict, List, Tuple


def extract_problem_info(filename: str) -> Tuple[str, str, str]:
    """
    Extract problem category, number, and title from filename.
    
    Returns: (category, number, title)
    - category: 'leetcode', 'codeforces_A', 'codeforces_B', etc., or 'other'
    - number: problem number if available
    - title: human-readable title
    """
    # LeetCode patterns
    # Pattern 1: 0056-merge-intervals.py
    leetcode_pattern1 = re.match(r'^(\d+)-(.+)\.py$', filename)
    # Pattern 2: 9. Palindrome Number.py
    leetcode_pattern2 = re.match(r'^(\d+)\.\s+(.+)\.py$', filename)
    
    if leetcode_pattern1:
        num = str(int(leetcode_pattern1.group(1)))  # Remove leading zeros
        title = leetcode_pattern1.group(2).replace('-', ' ').title()
        return 'leetcode', num, f"{num}. {title}"
    
    if leetcode_pattern2:
        num = leetcode_pattern2.group(1)
        title = leetcode_pattern2.group(2)
        return 'leetcode', num, f"{num}. {title}"
    
    # Codeforces patterns: A_Array_and_Peaks.py
    codeforces_pattern = re.match(r'^([A-Z])_(.+)\.py$', filename)
    if codeforces_pattern:
        division = codeforces_pattern.group(1)
        title = codeforces_pattern.group(2).replace('_', ' ')
        return f'codeforces_{division}', '', f"{division}. {title}"
    
    # Other problems
    title = filename.replace('.py', '').replace('_', ' ')
    return 'other', '', title


def generate_toc(repo_path: str) -> str:
    """Generate the Table of Contents section."""
    
    # Get all Python files
    py_files = [f for f in os.listdir(repo_path) if f.endswith('.py')]
    
    # Categorize files
    problems: Dict[str, List[Tuple[str, str, str]]] = {
        'leetcode': [],
        'codeforces_A': [],
        'codeforces_B': [],
        'codeforces_C': [],
        'codeforces_D': [],
        'codeforces_E': [],
        'codeforces_F': [],
        'other': []
    }
    
    for filename in py_files:
        category, number, title = extract_problem_info(filename)
        problems[category].append((number, title, filename))
    
    # Sort each category
    # LeetCode: by problem number
    problems['leetcode'].sort(key=lambda x: int(x[0]) if x[0] else 0)
    # Codeforces: alphabetically by title
    for key in ['codeforces_A', 'codeforces_B', 'codeforces_C', 'codeforces_D', 'codeforces_E', 'codeforces_F']:
        problems[key].sort(key=lambda x: x[1])
    # Other: alphabetically
    problems['other'].sort(key=lambda x: x[1])
    
    # Generate TOC
    toc_lines = ["## Table of Contents\n"]
    
    # LeetCode section
    if problems['leetcode']:
        toc_lines.append("### LeetCode Problems\n")
        for num, title, filename in problems['leetcode']:
            encoded_filename = quote(filename)
            toc_lines.append(f"- [{title}]({encoded_filename})\n")
        toc_lines.append("\n")
    
    # Codeforces section
    codeforces_divisions = ['A', 'B', 'C', 'D', 'E', 'F']
    has_codeforces = any(problems[f'codeforces_{div}'] for div in codeforces_divisions)
    
    if has_codeforces:
        toc_lines.append("### Codeforces Problems\n")
        for div in codeforces_divisions:
            key = f'codeforces_{div}'
            if problems[key]:
                toc_lines.append(f"\n#### Division {div}\n")
                for _, title, filename in problems[key]:
                    encoded_filename = quote(filename)
                    toc_lines.append(f"- [{title}]({encoded_filename})\n")
        toc_lines.append("\n")
    
    # Other section
    if problems['other']:
        toc_lines.append("### Other Problems\n")
        for _, title, filename in problems['other']:
            encoded_filename = quote(filename)
            toc_lines.append(f"- [{title}]({encoded_filename})\n")
        toc_lines.append("\n")
    
    # Total count
    total = sum(len(v) for v in problems.values())
    toc_lines.append("---\n")
    toc_lines.append(f"\n**Total Problems Solved: {total}**\n")
    
    return ''.join(toc_lines)


def update_readme(repo_path: str):
    """Update the README.md file with the new TOC."""
    readme_path = os.path.join(repo_path, 'README.md')
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new TOC
    new_toc = generate_toc(repo_path)
    
    # Find the TOC section and replace it
    # Pattern: from "## Table of Contents" to either the next "##" heading or "---" separator
    # This handles the TOC ending with the "---" line before "**Total Problems Solved:**"
    toc_pattern = r'## Table of Contents\n.*?\*\*Total Problems Solved: \d+\*\*\n'
    
    if re.search(toc_pattern, content, re.DOTALL):
        # Replace existing TOC
        new_content = re.sub(toc_pattern, new_toc, content, flags=re.DOTALL)
    else:
        # Try alternate pattern without the total line
        toc_pattern_alt = r'## Table of Contents\n.*?(?=\n##|\Z)'
        if re.search(toc_pattern_alt, content, re.DOTALL):
            new_content = re.sub(toc_pattern_alt, new_toc.rstrip(), content, flags=re.DOTALL)
        else:
            # Add TOC after the first heading and description
            lines = content.split('\n')
            # Find where to insert (after title and description)
            insert_idx = 2  # After title and description line
            if len(lines) > insert_idx:
                lines.insert(insert_idx, '\n' + new_toc)
                new_content = '\n'.join(lines)
            else:
                new_content = content + '\n\n' + new_toc
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ README.md updated successfully!")
    print(f"📊 Total problems: {len([f for f in os.listdir(repo_path) if f.endswith('.py')])}")


if __name__ == '__main__':
    repo_path = os.environ.get('GITHUB_WORKSPACE', '.')
    update_readme(repo_path)
