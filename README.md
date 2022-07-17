# 🖌️ daub
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pulse](https://img.shields.io/github/commit-activity/m/verillious/daub)
![Checks](https://github.com/verillious/daub/actions/workflows/check.yml/badge.svg)
![Publish](https://github.com/verillious/daub/actions/workflows/publish.yml/badge.svg)
> Opinionated pdf renderer

<br>

# ⚙️ Install
```shell
pip install --user daub
```

Or, to install from source:

```shell
git clone git@github.com:verillious/daub.git
pip install --user -e daub/
```

# 🖊️ Usage
From the command line:

```shell
Usage: daub [OPTIONS] MARKDOWN_FILE

  Opinionated pdf renderer

Options:
  -o, --output PATH  Override the output pdf file path.
  --css PATH         Override the default stylesheet.
  --version          Show the version and exit.
  --help             Show this message and exit.
```

## 💪 Features
* Converts a markdown file to a pdf file
* Optionally takes in a custom css file for styling
* By default tries to emulate the [minimal-github-theme](https://pages-themes.github.io/minimal/)

## 🔍 Alternatives
* Requires [Weasyprint](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html) which [only supports Windows 11](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows):
  * [md2pdf](https://github.com/jmaupetit/md2pdf)
  * [markdown2pdf](https://github.com/kxxoling/markdown2pdf)
  * [markdown-to-pdf](https://github.com/ljpengelen/markdown-to-pdf)
* [resume.md](https://github.com/mikepqr/resume.md) (Requires [Chrome](https://www.google.com/intl/en_uk/chrome/) or [Chromium](https://www.chromium.org/Home/))
* [rinohtype](https://github.com/brechtm/rinohtype) (Doesn't support css)
* [amd2pdf](https://github.com/tenuki/amd2pdf) (Requires [wkhtmltopdf](https://wkhtmltopdf.org/))

## 🙏 Credits
🍪 This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [verillious/cookiecutter-python](https://github.com/verillious/cookiecutter-python) project template.
