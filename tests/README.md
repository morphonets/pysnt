# PySNT Test Suite

This directory contains the test suite for PySNT

## Test Files

- `test_inspect.py`: Tests for the `pysnt.inspect()` function and related functionality
  Does not require SNT/Java initialization, but needs to be run after `scrips/deploy.py`.
  - `test_inspect_function_exists()` - Verifies inspect function is available
  - `test_inspect_without_jvm()` - Tests behavior when JVM is not started
  - `test_inspect_function_signature()` - Verifies function signature
  - `test_inspect_parameter_defaults()` - Tests default parameter values
  - `test_inspect_helper_functions()` - Tests helper functions like `_matches_keyword`
  - `test_inspect_module_import()` - Tests import from `pysnt.java_utils`
  - `test_inspect_in_all()` - Verifies function is in `__all__`


- `test_java_autocompletion.py`: Tests for Java class accessibility and method availability for IDE auto-completion.
  Tests that require Java methods are skipped when SNT initialization fails.
  Does not require SNT/Java initialization, but needs to be run after `scrips/deploy.py`.
  - `test_tree_class_import()` - Tests Tree class import
  - `test_tree_methods_accessible()` - Tests Tree methods accessibility
  - `test_analysis_class_import()` - Tests analysis class import 
  - `test_analysis_methods_accessible()` - Tests analysis methods
  - `test_path_class_methods()` - Tests Path class methods
  - `test_snt_utils_methods()` - Tests SNTUtils methods

    
- `test_type_stubs.py`: Tests that verify type stub functionality and auto-completion support.
  Does not require SNT/Java initialization, but needs to be run after `scrips/deploy.py`.
  - `test_type_stub_accessibility()` - Verifies all functions are accessible via `hasattr()`
  - `test_type_hints()` - Verifies type annotations work correctly
  - `test_all_functions_in_all_list()` - Verifies functions are properly exported in `__all__`

- `test_reflection.py`Tests for Java reflection capabilities and method extraction.
  - `test_reflection()` - Tests Java reflection on SNT classes
  - `test_inspect_function()` - Tests `pysnt.inspect()` with initialized SNT


## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test files
python -m pytest tests/test_type_stubs.py -v
python -m pytest tests/test_inspect.py -v

#  Test files can also be run directly:
python tests/test_inspect.py
python tests/test_java_autocompletion.py
python tests/test_reflection.py
```

## Adding New Tests

When adding new tests, follow these guidelines:

1. **Use proper pytest format** - Functions should start with `test_`
2. **Handle SNT initialization gracefully** - Use `pytest.skip()` for Java-dependent testsxw