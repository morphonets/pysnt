# PySNT Tests

This directory contains tests for PySNT functionality.

## Running Individual Tests
```bash
python tests/test_java_autocompletion.py

# Run with pytest
python -m pytest tests/test_java_autocompletion.py -v
```

## All Tests
```bash
# Run all tests with pytest
python -m pytest tests/ -v
```

## Requirements
Some tests may require SNT/Fiji to be configured:

```python
import pysnt.setup_utils as setup

# Configuration management
setup.show_config_status()
setup.set_fiji_path("/Applications/Fiji.app")
setup.auto_detect_and_configure()

# Detailed status
status = setup.get_fiji_status()
if not status['valid']:
    print(f"Issues: {status['issues']}")

# Troubleshooting
setup.reset_fiji_path()  # Clears config + env var
```
