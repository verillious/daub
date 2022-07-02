#!/usr/bin/env python
"""Tests for `daub` package."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from daub.cli import app


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


def test_generate_pdf_with_css():
    """test rendering a markdown document to a pdf file using a custom css file"""
    runner = CliRunner()
    help_result = runner.invoke(app, ["tests/test.md", "--css", "tests/test.css"])
    assert help_result.exit_code == 0
    pdf = Path("tests/test.pdf")
    assert pdf.exists()
