from __future__ import annotations

from typer.testing import CliRunner

from {{ package_name }}.cli import app


def test_cli_hello() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["hello", "codex"])
    assert result.exit_code == 0
    assert "Hello codex" in result.stdout
