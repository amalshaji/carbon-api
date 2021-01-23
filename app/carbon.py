import os
from typing import Tuple

from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page

DOWNLOAD_FOLDER = os.getcwd()


async def get_carbon_page(url: str) -> Tuple[Browser, Page]:
    browser = await launch(
        # defaultViewPort=None,
        # handleSIGINT=False,
        # handleSIGTERM=False,
        # handleSIGHUP=False,
        # headless=True,
        # args=["--no-sandbox", "--disable-setuid-sandbox"],
    )
    page = await browser.newPage()
    # await page._client.send(
    #     "Page.setDownloadBehaviour",
    #     {
    #         "behaviour": "allow",
    #         "downloadPath": DOWNLOAD_FOLDER,
    #     },
    # )
    await page.goto(url, timeout=100000)
    return browser, page


async def get_image(url: str, path: str) -> str:
    browser, page = await get_carbon_page(url)
    element = await page.querySelector("#export-container  .container-bg")
    _ = await element.screenshot({"path": path})
    await browser.close()
    return path
