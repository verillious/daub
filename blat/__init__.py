"""Top-level package for blat"""

import base64
import itertools
import logging
import os
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdown2 import markdown_path

logging.basicConfig()


CHROME_GUESSES_MACOS = (
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)

CHROME_GUESSES_WINDOWS = (
    # Windows 10
    os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    # Windows 7
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    # Vista
    r"C:\Users\UserName\AppDataLocal\Google\Chrome",
    # XP
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


def guess_chrome_path() -> str:
    """
    try to locate a chrome executable

    Raises:
        ValueError: raised if no install is found

    Returns:
        str: the path to the chrome executable
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
    raise ValueError("Could not find Chrome. Please set CHROME_PATH.")


def md2pdf(md_file_path: str, pdf_file_path: str = ""):
    """
    converts a markdown file to a pdf file

    Args:
        md_file_path (str): the markdown file to convert
        pdf_file_path (str, optional): the output pdf file. Defaults to "".
    """

    pdf_file_path = (
        pdf_file_path
        if pdf_file_path
        else str(Path.cwd() / Path(md_file_path).with_suffix(".pdf"))
    )
    source_html = markdown_path(md_file_path, extras=["cuddled-lists", "tables"])

    template_soup = BeautifulSoup(
        HTML_TEMPLATE.read_text(encoding="utf-8"), "html.parser"
    )
    source_soup = BeautifulSoup(source_html, "html.parser")

    new_div = template_soup.new_tag("style")
    new_div.string = BASE_CSS.read_text(encoding="utf-8")
    template_soup.html.head.append(new_div)

    for element in source_soup:
        template_soup.body.append(element)

    source_html = str(template_soup)

    write_pdf(source_html, pdf_file_path)


def write_pdf(html: str, output_file: str, chrome: str = "") -> None:
    """
    render an html file to pdf using chromium

    Args:
        html (str): the html string
        output_file (str): the output pdf file
        chrome (str, optional): absolute path to a chrome executable. Defaults to "".
    """
    chrome = chrome or guess_chrome_path()
    html64 = base64.b64encode(html.encode("utf-8"))
    options = [
        "--headless",
        "--print-to-pdf-no-header",
        "--enable-logging=stderr",
        "--log-level=2",
        "--in-process-gpu",
        "--disable-gpu",
    ]

    subprocess.run(
        [
            chrome,
            *options,
            f"--print-to-pdf={output_file}",
            "data:text/html;base64," + html64.decode("utf-8"),
        ],
        check=True,
    )
