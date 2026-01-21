from __future__ import annotations

from {{ package_name }} import hello


def test_smoke() -> None:
    assert hello()
