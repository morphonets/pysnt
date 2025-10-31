# Contributing to PySNT

Thank you for your interest in contributing to PySNT! This document provides guidelines and information for contributors.

## Development Setup

Please see the [Getting Started for Developers](README.md#getting-started-for-developers) section in the README for detailed setup instructions.

## Code Style

### Python Code Style
- **Formatting**: We use [Black](https://black.readthedocs.io/) with 88-character line length
- **Import sorting**: [isort](https://pycqa.github.io/isort/) with Black-compatible profile
- **Linting**: [flake8](https://flake8.pycqa.org/) with project-specific configuration
- **Type hints**: Use type hints where appropriate, checked with [mypy](https://mypy.readthedocs.io/)

### Documentation Style
- **Docstrings**: Write clear, concise docstrings
- **Comments**: Add comments for complex logic
- **Docs**: Update documentation when adding new features


## Development Scripts
See [DEV (README)](./dev/README.md).


## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_specific.py

# Run with verbose output
pytest -v
```

### Writing Tests
- Place tests in the `tests/` directory
- Use descriptive test names: `test_should_do_something_when_condition()`
- Mock external dependencies when appropriate


## Pull Request Process
1. **Fork and Clone**: Fork the repository and clone your fork
2. **Branch**: Create a feature branch (`git checkout -b feature/new-feature`)
3. **Develop**: Make your changes following the code style guidelines
4. **Test**: Ensure all tests pass and add new tests for your changes
5. **Document**: Update documentation and docstrings as needed
6. **Commit**: Use clear, descriptive commit messages
7. **Push**: Push to your fork (`git push origin feature/new-feature`)
8. **PR**: Open a pull request with a clear description of your changes

### Pull Request Guidelines
- **Title**: Use a clear, descriptive title
- **Description**: Explain what your PR does and why
- **Tests**: If possible include tests for new functionality
- **Documentation**: Update docs if you're changing user-facing behavior

## Issue Reporting

### Bug Reports
When reporting bugs, please include:
- **Environment**: Python version, OS, PySNT version
- **Steps to reproduce**: Clear, minimal steps to reproduce the issue
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Error messages**: Full error messages and stack traces

### Feature Requests
For feature requests, please include:
- **Use case**: Why is this feature needed?
- **Proposed solution**: How should it work?
- **Alternatives**: What alternatives have you considered?


## Getting Help
- **Documentation**: [pysnt.readthedocs.io](https://pysnt.readthedocs.io)
- **Forum**: [forum.image.sc/tag/snt](https://forum.image.sc/tag/snt) - Tag posts with `snt`
- **Issues**: [GitHub Issues](https://github.com/morphonets/pysnt/issues)

Thank you for contributing to PySNT! 🎉