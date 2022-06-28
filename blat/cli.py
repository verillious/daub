"""Console script for blat."""

import typer

from blat import md2pdf

app = typer.Typer()


@app.command()
def main(
    markdown_file: str,
    output: str = typer.Argument(None),
):
    """Opinionated pdf renderer"""
    md2pdf(markdown_file, output)
