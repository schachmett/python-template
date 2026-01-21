# Python Copier Template

This repository is a Copier template for bootstrapping new Python projects.

## Usage

```bash
python -m pip install --user copier
copier copy . /tmp/newproj
cd /tmp/newproj
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
- `license` (MIT, Apache-2.0, Proprietary)
- `python_version` (3.12, 3.13)
- `include_precommit` (bool)
- `include_github_actions` (bool)

## Derived from `example/`

The template files were derived from the reference layout under `example/`:
- `pyproject.toml` → `template/pyproject.toml.jinja`
- `AGENTS.md` → `template/AGENTS.md.jinja`
- `LICENSE` → `template/LICENSE.jinja`
- `.gitignore` → `template/.gitignore`
- `.pre-commit-config.yaml` → `template/.pre-commit-config.yaml.jinja`
- `src/` layout → `template/src/{{ package_name }}/__init__.py`
- `tests/` layout → `template/tests/test_smoke.py`

Files under `example/.vscode` were intentionally not templated.
