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
    # LeetCode patterns
    leetcode_pattern1 = re.match(r'^(+)-(.+)$', filename)
    leetcode_pattern2 = re.match(r'^(+)+(.+)$', filename)
    if leetcode_pattern1:
        num = str(int(leetcode_pattern1.group(1)))  # Remove leading zeros
        title = leetcode_pattern1.group(2).replace('-', ' ').title()
        return 'leetcode', num, f"{num}. {title}"
    if leetcode_pattern2:
        num = leetcode_pattern2.group(1)
        title = leetcode_pattern2.group(2)
        return 'leetcode', num, f"{num}. {title}"

    # Codeforces division: A_Array_and_Peaks.py
    codeforces_pattern = re.match(r'^([A-Z])_(.+)\.py$', filename)
    if codeforces_pattern:
        division = codeforces_pattern.group(1)
        title = codeforces_pattern.group(2).replace('_', ' ')
        return f'codeforces_{division}', '', f"{division}. {title}"

    # Codeforces CF123A forms (e.g., CF123A_Array_and_Peaks.py or CF123A-Array_and_Peaks.py)
    codeforces_cf_pattern = re.match(r'^(CF\d+[A-Z])[_-](.+)\.py$', filename)
    if codeforces_cf_pattern:
        cfid = codeforces_cf_pattern.group(1)
        title = codeforces_cf_pattern.group(2).replace('_', ' ')
        return 'codeforces_misc', '', f"{cfid}. {title}"

    # Other problems
    title = filename.replace('.py', '').replace('_', ' ')
    return 'other', '', title

def generate_toc(repo_path: str) -> str:
    # Get all Python files
    py_files = [f for f in os.listdir(repo_path) if f.endswith('.py')]
    problems: Dict[str, List[Tuple[str, str, str]]] = {
        'leetcode': [],
        'codeforces_A': [],
        'codeforces_B': [],
        'codeforces_C': [],
        'codeforces_D': [],
        'codeforces_E': [],
        'codeforces_F': [],
        'codeforces_misc': [], # For CF123A type Codeforces
        'other': []
    }
    for filename in py_files:
        category, number, title = extract_problem_info(filename)
        if category not in problems:
            category = 'other'
        problems[category].append((number, title, filename))
    # LeetCode: by problem number
    problems['leetcode'].sort(key=lambda x: int(x[0]) if x[0] else 0)
    for key in ['codeforces_A', 'codeforces_B', 'codeforces_C', 'codeforces_D', 'codeforces_E', 'codeforces_F', 'codeforces_misc']:
        problems[key].sort(key=lambda x: x[1])
    problems['other'].sort(key=lambda x: x[1])
    toc_lines = ["## Table of Contents\n"]
    if problems['leetcode']:
        toc_lines.append("### LeetCode Problems\n")
        seen_numbers = {}
        for num, title, filename in problems['leetcode']:
            encoded_filename = quote(filename)
            if num in seen_numbers:
                toc_lines.append(f"- [{title}]({encoded_filename}) (alternative version)\n")
            else:
                toc_lines.append(f"- [{title}]({encoded_filename})\n")
                seen_numbers[num] = True
        toc_lines.append("\n")
    # Codeforces section
    codeforces_divisions = ['A', 'B', 'C', 'D', 'E', 'F', 'misc']
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
    if problems['other']:
        toc_lines.append("### Other Problems\n")
        for _, title, filename in problems['other']:
            encoded_filename = quote(filename)
            toc_lines.append(f"- [{title}]({encoded_filename})\n")
        toc_lines.append("\n")
    total = sum(len(v) for v in problems.values())
    toc_lines.append("---\n")
    toc_lines.append(f"\n**Total Problems Solved: {total}**\n")
    return ''.join(toc_lines)

def update_readme(repo_path: str):
    readme_path = os.path.join(repo_path, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_toc = generate_toc(repo_path)
    toc_start = content.find('## Table of Contents')
    if toc_start != -1:
        total_pattern = r'\*\*Total Problems Solved: \d+\*\*'
        match = re.search(total_pattern, content[toc_start:])
        if match:
            toc_end = toc_start + match.end()
            new_content = content[:toc_start] + new_toc + content[toc_end:]
        else:
            next_heading = re.search(r'\n##[^#]', content[toc_start + 20:])
            if next_heading:
                toc_end = toc_start + 20 + next_heading.start()
                new_content = content[:toc_start] + new_toc.rstrip() + '\n' + content[toc_end:]
            else:
                new_content = content[:toc_start] + new_toc
    else:
        lines = content.split('\n')
        insert_idx = 2
        if len(lines) > insert_idx:
            lines.insert(insert_idx, '\n' + new_toc)
            new_content = '\n'.join(lines)
        else:
            new_content = content + '\n\n' + new_toc
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ README.md updated successfully!")
    print(f"📊 Total problems: {len([f for f in os.listdir(repo_path) if f.endswith('.py')])}")

if __name__ == '__main__':
    repo_path = os.environ.get('GITHUB_WORKSPACE', '.')
    update_readme(repo_path)