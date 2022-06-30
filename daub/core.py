"""Top-level package for daub"""

import asyncio
import base64
import itertools
import logging
import os
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdown2 import markdown_path
from pyppeteer import launch

logging.basicConfig()


CHROME_GUESSES_MACOS = (
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)

CHROME_GUESSES_WINDOWS = (
    os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Users\UserName\AppDataLocal\Google\Chrome",
    r"C:\Documents and Settings\UserName\Local Settings\Application Data\Google\Chrome",
)

CHROME_GUESSES_LINUX = [
    "/".join((path, executable))
    for path, executable in itertools.product(
        (
            "/usr/local/sbin",
            "/usr/local/bin",
            "/usr/sbin",
            "/usr/bin",
            "/sbin",
            "/bin",
            "/opt/google/chrome",
        ),
        ("google-chrome", "chrome", "chromium", "chromium-browser"),
    )
]


HTML_TEMPLATE = Path(__file__).parent / "html" / "template.html"
BASE_CSS = Path(__file__).parent / "css" / "base.css"


def _guess_chrome_path() -> str:  # pragma: no cover
    """
    try to locate a chrome executable

    Returns:
        str: the path to the chrome executable, or None if nothing is found.
    """

    if sys.platform == "darwin":
        guesses = CHROME_GUESSES_MACOS
    elif sys.platform == "win32":
        guesses = CHROME_GUESSES_WINDOWS
    else:
        guesses = CHROME_GUESSES_LINUX
    for guess in guesses:
        if os.path.exists(guess):
            return guess
    return ""


def md2pdf(md_file_path: str, pdf_file_path: str = None, css_file_path: str = None):
    """
    converts a markdown file to a pdf file

    Args:
        md_file_path (str): the markdown file to convert
        pdf_file_path (str, optional): the output pdf file. Defaults to None.
        css_file_path (str, optional): a css file to use for styling. Defaults to None.
    """

    pdf_file_path = (
        str(Path(pdf_file_path).resolve())
        if pdf_file_path
        else str(Path(md_file_path).with_suffix(".pdf").resolve())
    )
    source_html = markdown_path(md_file_path, extras=["cuddled-lists", "tables"])

    template_soup = BeautifulSoup(
        HTML_TEMPLATE.read_text(encoding="utf-8"), "html.parser"
    )
    source_soup = BeautifulSoup(source_html, "html.parser")

    new_div = template_soup.new_tag("style")

    css_string = (
        Path(css_file_path).read_text(encoding="utf-8")
        if css_file_path
        else BASE_CSS.read_text(encoding="utf-8")
    )

    new_div.string = css_string

    template_soup.html.head.append(new_div)

    for element in source_soup:
        template_soup.body.append(element)

    source_html = str(template_soup)
    asyncio.get_event_loop().run_until_complete(write_pdf(source_html, pdf_file_path))


async def write_pdf(html: str, output_file: str, chrome: str = "") -> None:
    """
    render an html file to pdf using chrome or chromium

    Args:
        html (str): the html string
        output_file (str): the output pdf file
        chrome (str, optional): absolute path to a chrome executable. Defaults to "".
    """

    html64 = base64.b64encode(html.encode("utf-8"))
    browser = await launch(executablePath=chrome or _guess_chrome_path())
    page = await browser.newPage()

    await page.goto(
        f"data:text/html;base64,{html64.decode('utf-8')}", waitUntil="networkidle2"
    )
    await page.emulateMedia("screen")
    await page.pdf(
        {
            "path": output_file,
            "margin": {"top": "1cm", "right": "1cm", "bottom": "1cm", "left": "1cm"},
            "printBackground": True,
        }
    )
    await browser.close()
