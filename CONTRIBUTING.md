# Contributing

Thank you for your interest in contributing. This project follows standard
open-source practices aligned with GovTech security requirements.

## Getting Started

1. Fork the repository and clone locally.
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Install dev dependencies: `pip install -e ".[dev]"`
4. Run tests: `pytest`
5. Run linters: `ruff check . && mypy src/`

## Pull Request Process

1. Ensure all tests pass and linting is clean.
2. Update documentation if your change affects public APIs.
3. Reference any related issues in the PR description.
4. PRs require at least one approving review before merge.

## Code Style

- Follow PEP 8 via **ruff** and **black**.
- All public functions must have type hints and docstrings.
- Keep commits atomic with [Conventional Commits](https://www.conventionalcommits.org/).

## Security

If you discover a security vulnerability, **do not** open a public issue.
See [SECURITY.md](SECURITY.md) for responsible disclosure instructions.
