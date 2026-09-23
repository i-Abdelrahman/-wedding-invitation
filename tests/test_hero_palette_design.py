from pathlib import Path
import re

html = Path('/mnt/data/wedding-invitation/dist/index.html').read_text(encoding='utf-8')
flat = re.sub(r'\s+', '', html)

# New visual direction: the long story must use the hero's blue/ivory palette,
# not a flat parchment-only field.
for token in ['--sky-1:', '--sky-2:', '--cloud-panel:', '--mountain-blue:']:
    assert token in html, f'missing hero palette token {token}'

assert 'data-theme="hero-palette"' in html, 'continuous story must declare hero palette theme'
assert 'hero-palette-wash' in html, 'hero palette background wash missing'

# The decorative raster stays as one continuous layer, but should blend with
# the blue wash so it no longer reads as separate cream panels.
assert re.search(r'\.story-background\{[^}]*opacity:', html), 'story background must blend with palette wash'

# Text areas should feel like the calm light area under the names: soft,
# translucent and borderless rather than hard cards.
assert 'soft-panel' in html, 'soft content panel class missing'
assert re.search(r'\.soft-panel\{[^}]*backdrop-filter:blur', flat), 'soft panel needs blur/glass effect'
assert re.search(r'\.soft-panel\{[^}]*border-radius:', flat), 'soft panel needs organic rounded shape'

# Primary location CTA should use the same quiet ivory/gold treatment rather
# than a dark filled gold pill.
assert 'map-btn quiet-btn' in html, 'map button must use quiet hero-inspired treatment'
assert re.search(r'\.quiet-btn\{[^}]*background:rgba\(255,', flat), 'quiet button must be light/translucent'

print('HERO_PALETTE_DESIGN_OK')
