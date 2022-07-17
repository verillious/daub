"""Console script for daub."""

import click

from daub import md2pdf


@click.command()
@click.argument("markdown_file", type=click.Path(exists=True))
@click.option(
    "-o",
    "--output",
    type=click.Path(),
    default=None,
    help="Override the output pdf file path.",
)
@click.option(
    "--css",
    type=click.Path(exists=True),
    default=None,
    help="Override the default stylesheet.",
)
@click.version_option()
def main(
    markdown_file: str,
    output: str = None,
    css: str = None,
):
    """Opinionated pdf renderer"""
    md2pdf(markdown_file, output, css)
