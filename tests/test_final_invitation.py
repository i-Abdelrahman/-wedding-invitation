from pathlib import Path
import re

html = Path('/mnt/data/wedding-invitation/dist/index.html').read_text(encoding='utf-8')

# Single-file deployment contract
assert 'data:image/jpeg;base64,' in html or 'data:image/png;base64,' in html, 'images must be embedded'
assert 'data:audio/mpeg;base64,' in html, 'audio must be embedded'
assert 'assets/' not in html, 'no external asset paths allowed'

# Continuous-story contract: no raster panel-stack implementation
assert 'continuous-story' in html, 'continuous story wrapper missing'
assert 'story-background' in html, 'single continuous background missing'
assert 'reference-panel' not in html, 'old separate panel implementation still present'
assert 'panel-section' not in html, 'old section-card implementation still present'

# Exact approved Arabic copy
required = [
    'نتشرف بدعوتكم لحضور حفل زفافنا',
    'فرحتنا تكتمل بوجودكم',
    'موعد زفافنا',
    'الخميس، 8 أكتوبر 2026',
    'مدينة السادات، المنطقة 28 أ، قطعة 123',
    'الغداء', '4:00 عصرًا',
    'الاستقبال', '6:00 مساءً',
    'بدء الحفل', '8:00 مساءً',
    'تشرفنا بوجودكم',
]
for text in required:
    assert text in html, f'missing approved text: {text}'

# Closing section is real, not only alt/sr-only text
assert re.search(r'<section[^>]+id="closing"[\s\S]*?تشرفنا بوجودكم[\s\S]*?</section>', html), 'closing section missing'

# Cover should fill viewport and have one interaction layer only
assert 'min-height:100svh' in html.replace(' ', ''), 'cover must fill viewport'
assert html.count('id="open-invitation"') == 1, 'duplicate open invitation controls'

# Functional pieces
assert '2026-10-08T20:00:00+03:00' in html, 'countdown target incorrect/missing'
assert 'https://maps.app.goo.gl/FK2sCrA2D5gTKwkY6?g_st=iw' in html, 'maps URL missing'
assert 'id="audio-toggle"' in html, 'audio control missing'

print('FINAL_CONTRACT_OK')
