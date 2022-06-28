#!/usr/bin/env python
"""Tests for `blat` package."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from blat.cli import app


@pytest.fixture(autouse=True)
def run_around_tests():
    """Make sure we get rid of generated files"""
    yield
    file = Path("tests/out.pdf")
    if file.exists():
        file.unlink()


def test_command_line_interface():
    """test the CLI launches"""
    runner = CliRunner()
    help_result = runner.invoke(app, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output
