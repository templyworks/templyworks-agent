import { chromium } from 'playwright';
const [slug, id, scheme] = process.argv.slice(2);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY }, args: ['--ignore-certificate-errors'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 1100 }, deviceScaleFactor: 2, colorScheme: scheme || 'dark' });
const p = await ctx.newPage();
await p.goto(`https://cute-herring-2b2.notion.site/${id}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
await p.waitForTimeout(9000);
const sc = await p.$('.notion-frame .notion-scroller');
for (let i = 0; i < 7; i++) {
  await p.screenshot({ path: `shots/${slug}-${scheme}-${i}.png` });
  if (!sc) break;
  await sc.evaluate((el) => el.scrollBy(0, 950));
  await p.waitForTimeout(2500);
}
await browser.close();
