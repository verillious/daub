#!/usr/bin/env python
"""Tests for `blat` package."""

from os import stat
from pathlib import Path

import pytest
from typer.testing import CliRunner

from blat.cli import app


@pytest.fixture(autouse=True)
def run_around_tests():
    """Make sure we get rid of generated files"""
    file = Path("tests/test.pdf")
    if file.exists():
        file.unlink()
    yield
    file = Path("tests/test.pdf")
    if file.exists():
        file.unlink()


def test_command_line_interface():
    """test the CLI launches"""
    runner = CliRunner()
    help_result = runner.invoke(app, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output


def test_generate_pdf():
    """test rendering a markdown document to a pdf file"""
    runner = CliRunner()
    help_result = runner.invoke(app, ["tests/test.md"])
    assert help_result.exit_code == 0
    pdf = Path("tests/test.pdf")
    assert pdf.exists()
    pdf_result = stat(str(pdf.resolve()))

    assert pdf_result.st_mode == 33206
    assert pdf_result.st_dev == 1723108590
    assert pdf_result.st_nlink == 1
    assert pdf_result.st_uid == 0
    assert pdf_result.st_gid == 0
    assert pdf_result.st_size == 63095


def test_generate_pdf_with_css():
    """test rendering a markdown document to a pdf file using a custom css file"""
    runner = CliRunner()
    help_result = runner.invoke(app, ["tests/test.md", "--css", "tests/test.css"])
    assert help_result.exit_code == 0
    pdf = Path("tests/test.pdf")
    assert pdf.exists()
    pdf_result = stat(str(pdf.resolve()))

    assert pdf_result.st_mode == 33206
    assert pdf_result.st_dev == 1723108590
    assert pdf_result.st_nlink == 1
    assert pdf_result.st_uid == 0
    assert pdf_result.st_gid == 0
    assert pdf_result.st_size == 71114
