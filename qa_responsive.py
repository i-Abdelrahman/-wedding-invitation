from pathlib import Path
from playwright.sync_api import sync_playwright
html=Path('/mnt/data/wedding-invitation/dist/index.html').read_text(encoding='utf-8')
viewports=[(320,700),(390,844),(768,1024),(1440,900)]
out=Path('/mnt/data/wedding-invitation/final_previews'); out.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox','--disable-dev-shm-usage','--autoplay-policy=no-user-gesture-required'])
    for w,h in viewports:
        page=browser.new_page(viewport={'width':w,'height':h}, device_scale_factor=1)
        page.set_content(html, wait_until='load')
        before=page.evaluate('''() => ({scrollWidth:document.documentElement.scrollWidth,innerWidth,coverH:document.querySelector('#cover').getBoundingClientRect().height})''')
        page.click('#open-invitation'); page.wait_for_timeout(1000)
        after=page.evaluate('''() => ({scrollWidth:document.documentElement.scrollWidth,innerWidth,siteW:document.querySelector('.site').getBoundingClientRect().width,storyH:document.querySelector('.continuous-story').getBoundingClientRect().height,closing:document.querySelector('#closing').innerText.includes('تشرفنا')})''')
        assert before['scrollWidth'] <= w, (w,'overflow before',before)
        assert after['scrollWidth'] <= w, (w,'overflow after',after)
        assert after['closing'], (w,'closing missing')
        assert after['siteW'] <= 480.5, (w,'site too wide',after)
        print(w,h,before,after)
        if w in (320,1440): page.screenshot(path=str(out/f'responsive-{w}x{h}.png'))
        page.close()
    browser.close()
