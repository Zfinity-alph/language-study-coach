"""Dependency-free structural checks; not a behavioral or general YAML validator."""

import re
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    skill = root / 'skills' / 'language-study-coach'
    problems = []
    main_file = skill / 'SKILL.md'
    text = main_file.read_text(encoding='utf-8')
    manifest = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n', text)
    if not manifest or manifest.group(1) != skill.name:
        problems.append('Unexpected two-field manifest or folder/name mismatch')
    elif len(manifest.group(2)) > 1024:
        problems.append('Description exceeds 1024 characters')
    files = [root / 'README.md']
    for folder in ('skills', 'examples', 'tests'):
        files.extend((root / folder).rglob('*.md'))
    for file in files:
        content = file.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'https?://', target) or target.startswith('#'):
                continue
            dest = (file.parent / target.split('#', 1)[0]).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                problems.append(f'Invalid local link in {file.relative_to(root)}: {target}')
        if re.search(r'(?i)[CD]:[\\/]|BaiduNetdiskDownload|Tencent Files|CET-6.{0,10}566', content):
            problems.append(f'Private data candidate: {file.relative_to(root)}')
        if re.search(r'\[TODO:[^\n]*\]', content):
            problems.append(f'Unfinished scaffold: {file.relative_to(root)}')
    for problem in problems:
        print(problem)
    print(f'Checked {len(files)} Markdown files; {len(problems)} findings.')
    print('Checks do not establish behavioral quality, linguistic correctness, or exhaustive privacy review.')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
