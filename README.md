# Python Copier Template

This repository is a Copier template for bootstrapping new Python projects.

## Usage

```bash
sudo apt install pipx
pipx ensurepath
pipx install copier
pipx install uv  # recommended
copier copy github.com/schachmett/python-template /path/to/newproj
cd /path/to/newproj
```

Follow the printed next steps to create a virtual environment, install dev deps, and run checks.

## Update an existing project

```bash
copier update
```

## Template inputs

- `project_name` (string, default: `my-project`)
- `package_name` (string, default derived from `project_name`)
- `author_name` (optional)
- `license` (MIT, Apache-2.0, Proprietary; default MIT)
- `python_version` (3.14, 3.13, 3.12; default 3.14)
- `include_precommit` (bool)
- `cli` (bool, adds Typer CLI scaffold)
