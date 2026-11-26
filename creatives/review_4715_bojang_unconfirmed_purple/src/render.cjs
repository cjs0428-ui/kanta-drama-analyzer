// RECONSTRUCTED renderer. This is NOT the original scratchpad/render.cjs:
// its source never appears in the server transcript from 2026-10-22 09:12Z to 2026-11-05.
// It was rebuilt from how the transcript calls it and the errors it printed:
//   W=1080 H=1920 [Q=..] [TS=0.5,2,4.2] node render.cjs <siteDir> <stills|frames> <outDir>
//   - the page exposes window.render(t) and window.DURATION
//   - frames mode writes <outDir>/f%05d.jpg at 30 fps (muxed with: ffmpeg -framerate 30 -i fr/f%05d.jpg ...)
//   - stills mode writes <outDir>/t<Number(ts)>.png (e.g. TS=13.0 -> t13.png, as seen in the transcript)
//   - uses Playwright chromium (the session used require('playwright'))
// The original also handled pages whose render(t) is async (awaits img.decode); awaiting it here covers both.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const [site, mode = 'frames', out = 'fr'] = process.argv.slice(2);
  const W = +(process.env.W || 1080), H = +(process.env.H || 1920);
  const Q = +(process.env.Q || 92);
  const FPS = +(process.env.FPS || 30);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(site, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
  const dur = await page.evaluate(() => window.DURATION);
  if (mode === 'stills') {
    const ts = (process.env.TS || '0').split(',').map(Number);
    for (const t of ts) {
      await page.evaluate(async t => { await window.render(t); }, t);
      await page.screenshot({ path: path.join(out, `t${t}.png`) });
    }
  } else {
    const n = Math.ceil(dur * FPS);
    for (let i = 0; i < n; i++) {
      await page.evaluate(async t => { await window.render(t); }, i / FPS);
      await page.screenshot({ path: path.join(out, `f${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: Q });
    }
  }
  await browser.close();
})();
