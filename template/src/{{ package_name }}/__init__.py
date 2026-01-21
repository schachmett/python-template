from __future__ import annotations


def hello() -> str:
    """Return a short greeting for smoke tests."""
    return "Hello from {{ project_name }}"


__all__ = ["hello"]
