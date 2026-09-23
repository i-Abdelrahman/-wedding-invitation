from pathlib import Path
from playwright.sync_api import sync_playwright

html=Path('/mnt/data/wedding-invitation/dist/index.html').read_text(encoding='utf-8')
out=Path('/mnt/data/wedding-invitation/final_previews'); out.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox','--disable-dev-shm-usage','--autoplay-policy=no-user-gesture-required'])
    page=browser.new_page(viewport={'width':390,'height':844}, device_scale_factor=1)
    page.set_content(html, wait_until='load')
    page.screenshot(path=str(out/'01-cover.png'))
    page.click('#open-invitation')
    page.wait_for_timeout(1100)
    page.screenshot(path=str(out/'02-hero.png'))
    for idx, sec in enumerate(['welcome','countdown','location','schedule','closing'], start=3):
        page.locator('#'+sec).scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        page.screenshot(path=str(out/f'{idx:02d}-{sec}.png'))
    page.screenshot(path=str(out/'full-page.png'), full_page=True)
    metrics=page.evaluate('''() => ({
      bodyWidth: document.body.scrollWidth,
      innerWidth: innerWidth,
      storyTop: document.querySelector('.continuous-story').getBoundingClientRect().top + scrollY,
      storyHeight: document.querySelector('.continuous-story').getBoundingClientRect().height,
      closingText: document.querySelector('#closing').innerText.trim(),
      mainHidden: document.querySelector('#main').hidden,
      audioEmbedded: document.querySelector('#wedding-audio').src.startsWith('data:audio/mpeg;base64,'),
      imageEmbedded: document.querySelector('.story-background').src.startsWith('data:image/jpeg;base64,')
    })''')
    print(metrics)
    browser.close()
