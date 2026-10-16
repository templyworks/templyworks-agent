import { chromium } from 'playwright';
const pages = {
  'finance-hq': '15267ba5a550496dac45eb500a6ce131',
  'client-pipeline': '541fd801bced4d35adbdd1e08dfb1ea9',
  'project-tracker': '6c34ce46100d497b89e8962c5d38a998',
  'pitch-kit': 'c96232522fff45dcaa0531880815b547',
  'second-brain': 'b658d2b24061413f8bdfc7f27cb41e9f',
  'client-portal': '5a44a939fb7a42e3bada671908151385',
  'student-os': '3fb6bb63c14f81fca1dffb5272690f0d',
};
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined, args: ['--ignore-certificate-errors'] });
for (const [slug, id] of Object.entries(pages)) {
  for (const scheme of ['light']) {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 4200 }, deviceScaleFactor: 2, colorScheme: scheme });
    const p = await ctx.newPage();
    await p.goto(`https://cute-herring-2b2.notion.site/${id}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await p.waitForTimeout(9000);
    // full page
    await p.screenshot({ path: `shots/${slug}-full.png`, fullPage: false });
    console.log(slug, await p.title());
    await ctx.close();
  }
}
await browser.close();
