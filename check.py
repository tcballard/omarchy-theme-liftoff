"""Portable fallback checks; not the upstream validator or Rust handoff tool."""
from pathlib import Path
import re
import tomllib
from PIL import Image

root = Path(__file__).resolve().parent
palette = tomllib.loads((root / 'colors.toml').read_text())
assert palette['mode'] == 'dark'
for key, value in palette.items():
    assert key == 'mode' or re.fullmatch(r'#[0-9a-fA-F]{6}', value), key
for key in ('accent', 'background', 'foreground', 'red', 'yellow', 'green', 'cyan', 'blue', 'magenta'):
    assert key in palette

def luminance(value):
    values = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    values = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in values]
    return sum(v * w for v, w in zip(values, (.2126, .7152, .0722)))

for a, b, minimum in [('foreground', 'background', 4.5), ('foreground', 'selection', 4.5), ('accent', 'background', 3), ('muted', 'background', 4.5), ('dark_foreground', 'background', 4.5)]:
    high, low = sorted([luminance(palette[a]), luminance(palette[b])], reverse=True)
    ratio = (high + .05) / (low + .05)
    print(f'{a}/{b}: {ratio:.2f}:1')
    assert ratio >= minimum
for name, expected_size in [('01-liftoff.png', (8192, 4608)), ('02-engine-cluster.png', (8192, 5461)), ('03-liftoff-sunset.png', (8192, 4608))]:
    with Image.open(root / 'backgrounds' / name) as im:
        im.load()
        assert im.format == 'PNG'
        assert im.size == expected_size
        assert not im.getexif(), 'Review EXIF before delivery'
        print(f'{name}: 8K PNG fully decoded: {im.size}; no EXIF metadata')
for p in root.rglob('*'):
    assert not p.is_symlink()
for md in root.glob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', md.read_text()):
        if '://' not in link:
            assert (root / link).is_file(), link
for line in (root / 'media.tsv').read_text().splitlines()[1:]:
    path, kind, caption = line.split('\t')
    assert (root / path).is_file()
    if kind in ('contact-sheet', 'mockup'):
        assert 'not a desktop screenshot' in caption
print('PASS: flat TOML, required colours, contrast targets, media inventory, local links and no symlinks')
print('NOT RUN: live desktop, Git-installed path, Rust helper/handoff, upstream registry validator')
