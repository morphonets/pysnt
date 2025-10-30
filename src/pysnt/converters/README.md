# PySNT Converters Module

This directory contains the PySNT converters functionality, organized into modules.

## Module Structure

```
src/pysnt/converters/
├── __init__.py            # Public API exports and backward compatibility
├── core.py                # Base utilities, constants, and factory functions
├── extractors.py          # Graph vertex and edge attribute extraction
├── graph_converters.py    # SNT graph to NetworkX conversion
├── chart_converters.py    # SNT chart to matplotlib conversion
├── structured_data_converters.py    # SNT structured data (tabular-like data) to xarray conversion
├── display.py             # Display handlers and visualization
├── enhancement.py         # Java object enhancement functionality
└── *.pyi                  # Type stubs for each module
```


## Quick Reference

### Adding New Functionality

- **Constants/utilities**: Add to `core.py`
- **Graph extraction**: Add to `extractors.py`
- **Graph conversion**: Add to `graph_converters.py`
- **Chart conversion**: Add to `chart_converters.py`
- **Structured data conversion**: Add to `structured_data_converters.py`
- **Display features**: Add to `display.py`
- **Enhancement features**: Add to `enhancement.py`
- **Public API**: Export from `__init__.py`


### Common Patterns

#### Factory Functions (from core.py)
```python
from .core import _create_snt_object, _create_converter_result, _create_error_result

# Create successful conversion result
result = _create_converter_result(data, source_type="ImagePlus", title="My Image")

# Create error result
error_result = _create_error_result(matplotlib.figure.Figure, error, source_type="SNTChart")
```

#### Extractor Pattern (from extractors.py)
```python
from .extractors import _VERTEX_EXTRACTORS, _detect_vertex_type

# Detect and use appropriate extractor
vertex_type = _detect_vertex_type(graph)
extractor = _VERTEX_EXTRACTORS.get(vertex_type)
if extractor:
    attributes = extractor.extract_attributes(vertex, requested_attrs)
```

#### Converter Pattern
```python
# Each converter module follows this pattern:
def _is_[type](obj: Any) -> bool:
    """Check if object is of this type."""
    pass

def _convert_[type](obj: Any, **kwargs) -> SNTObject:
    """Convert object to Python equivalent."""
    pass
```
