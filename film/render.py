import asyncio,sys,os
from playwright.async_api import async_playwright
FPS=30;DUR=45
async def main():
    os.makedirs('frames',exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///home/ubuntu/bdny/film/film.html');await pg.evaluate('document.fonts.ready');await pg.wait_for_timeout(500)
        if len(sys.argv)>1:
            for t in [float(x) for x in sys.argv[1:]]:
                await pg.evaluate(f'seek({t})');await pg.screenshot(path=f'/tmp/f_{t}.jpg',type='jpeg',quality=85)
        else:
            for i in range(FPS*DUR):
                await pg.evaluate(f'seek({i/FPS})');await pg.screenshot(path=f'frames/{i:05d}.jpg',type='jpeg',quality=92)
                if i%300==0:print(i,flush=True)
        await b.close()
asyncio.run(main())
