"""Console script for daub."""

import typer

from daub import md2pdf

app = typer.Typer()


@app.command()
def main(
    markdown_file: str,
    output_file: str = typer.Argument(None),
    css: str = typer.Option(
        None, "--css", "-c", help="Path to a css file to use for styling."
    ),
):
    """Opinionated pdf renderer"""
    md2pdf(markdown_file, output_file, css)
