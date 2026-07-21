from pathlib import Path
import re

pattern = re.compile(r'!\[[^\]]*\]\((/images/5-Workshop/IRMS/[^)]+)\)')
files = [
    Path('content/5-Workshop/5.3-Infrastructure-Configuration/_index.md'),
    Path('content/5-Workshop/5.3-Infrastructure-Configuration/_index.vi.md'),
    Path('content/5-Workshop/5.5-Deployment-and-Testing/_index.md'),
    Path('content/5-Workshop/5.5-Deployment-and-Testing/_index.vi.md'),
]
for path in files:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    new_text = pattern.sub(lambda m: '> Screenshot placeholder: ' + Path(m.group(1)).name, text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f'Updated {path}')
