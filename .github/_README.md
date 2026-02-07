# Auto-Update README Table of Contents

This repository uses a GitHub Action to automatically update the README's table of contents whenever Python solution files are added or modified.

## How It Works

### Workflow Trigger
The action is triggered when:
- Changes are pushed to the `main` branch
- The changes include `.py` files or `README.md`

### What It Does
1. **Scans** all Python files in the repository
2. **Categorizes** them by platform:
   - **LeetCode Problems**: Files matching patterns like `0056-merge-intervals.py` or `9. Palindrome Number.py`
   - **Codeforces Problems**: Files matching pattern `X_Problem_Name.py` where X is a division letter (A-F)
   - **Other Problems**: Any other Python files
3. **Generates** a formatted table of contents with:
   - Sorted problem lists
   - Working file links
   - Problem counts
   - Labels for duplicate problems
4. **Updates** the README.md automatically
5. **Commits** and pushes the changes (if any)

## Files

- **`.github/workflows/update-toc.yml`**: The GitHub Action workflow definition
- **`.github/scripts/update_toc.py`**: Python script that generates the TOC

## Running Locally

You can test the TOC generation script locally:

```bash
python .github/scripts/update_toc.py
```

This will update the README.md file based on the current Python files in the repository.

## Adding New Problems

Simply add your Python solution file to the repository and push to main. The TOC will be automatically updated within seconds!

### Naming Conventions

For proper categorization:
- **LeetCode**: `XXXX-problem-name.py` or `XXXX. Problem Name.py`
- **Codeforces**: `X_Problem_Name.py` (where X is division A-F)
- **Other**: Any descriptive name ending in `.py`
