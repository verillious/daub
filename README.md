daub
======

opinionated pdf renderer

install
-------


```console
pip install --user daub
```

Or, to install from source:

```console
git clone git@github.com:verillious/daub.git
pip install --user -e daub/
```

usage
-----
from the command line:

```console
daub [OPTIONS] MARKDOWN_FILE [OUTPUT_FILE]

  Opinionated pdf renderer

Arguments:
  MARKDOWN_FILE  [required]
  [OUTPUT_FILE]

Options:
  -c, --css TEXT                  Path to a css file to use for styling.
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## features
* converts a markdown file to a pdf file
* optionally takes in a custom css file for styling
* by default tries to emulate the [minimal-github-theme](https://pages-themes.github.io/minimal/)

## alternatives
* requires [Weasyprint](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html) which [only supports Windows 11](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows):
  * [md2pdf](https://github.com/jmaupetit/md2pdf)
  * [markdown2pdf](https://github.com/kxxoling/markdown2pdf)
  * [markdown-to-pdf](https://github.com/ljpengelen/markdown-to-pdf)
* [resume.md](https://github.com/mikepqr/resume.md) (requires [Chrome](https://www.google.com/intl/en_uk/chrome/) or [Chromium](https://www.chromium.org/Home/))
* [rinohtype](https://github.com/brechtm/rinohtype) (doesn't support css)
* [amd2pdf](https://github.com/tenuki/amd2pdf) (requires [wkhtmltopdf](https://wkhtmltopdf.org/))

## credits
this package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [verillious/cookiecutter-python](https://github.com/verillious/cookiecutter-python) project template.
