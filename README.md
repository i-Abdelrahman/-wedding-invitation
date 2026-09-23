# Wedding Invitation — عبدالرحمن وأمنية

Static Arabic wedding invitation for **Thursday, 8 October 2026**.

## Current approved experience

- One public invitation link.
- Full-screen opening cover.
- Preserved original hero artwork.
- One continuous long-form invitation story using the hero sky / cloud / mountain / floral palette.
- Live Arabic copy, countdown, Google Maps button, day schedule, closing section, and background audio control.
- Mobile-first responsive layout capped to an invitation-style canvas on larger screens.

## Approved content

- نتشرف بدعوتكم لحضور حفل زفافنا
- فرحتنا تكتمل بوجودكم ❤️
- الخميس، 8 أكتوبر 2026
- مدينة السادات، المنطقة 28 أ، قطعة 123
- الغداء — 4:00 عصرًا
- الاستقبال — 6:00 مساءً
- بدء الحفل — 8:00 مساءً
- تشرفنا بوجودكم

## Verification

Run from the local project workspace:

```bash
python tests/test_final_invitation.py
python tests/test_hero_palette_design.py
python qa_final.py
python qa_responsive.py
```

Verified viewports: `320×700`, `390×844`, `768×1024`, `1440×900`.

The production artifact is a self-contained `dist/index.html` with images and audio embedded as data URIs. The repository keeps a lightweight source template with explicit asset placeholders because the connected GitHub write interface does not support directly syncing the ~2 MB generated single-file artifact from the runtime.

See `VERIFICATION.json` for the verified artifact checksum and deployment metadata.
