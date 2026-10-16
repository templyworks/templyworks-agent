import { chromium } from 'playwright';
const id = process.argv[2];
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY }, args: ['--ignore-certificate-errors'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 1100 }, colorScheme: 'dark' });
const p = await ctx.newPage();
await p.goto(`https://cute-herring-2b2.notion.site/${id}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
await p.waitForTimeout(6000); const sc=await p.$('.notion-frame .notion-scroller'); for(let k=0;k<8;k++){ if(sc) await sc.evaluate(e=>e.scrollBy(0,900)); await p.waitForTimeout(1500);} 
const t=await p.innerText('body'); const i=t.indexOf(process.argv[3]||''); console.log(t.slice(i, i+700));
await browser.close();
