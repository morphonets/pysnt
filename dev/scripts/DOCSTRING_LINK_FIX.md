# Fix: Docstring Links to Detailed Documentation

## Problem
The enhanced docstrings in `_docstring_enhancements.py` had **absolute paths** starting with `/`:
```python
"AllenCompartment": '...**All Methods and Attributes:** See `AllenCompartment detailed documentation </allencompartment_doc.html>`_...'
```

This caused broken links because:
- Absolute paths like `/allencompartment_doc.html` look for files at the web root
- The actual files are at `../pysnt/allencompartment_doc.html` relative to `api_auto/`

## Fix Applied

### Changed in `structured_integration.py`:
```python
# Before (line 850):
return f"/{web_path}"

# After:
return f"../pysnt/{web_path}"
```

### Result:
All enhanced docstrings now have correct relative paths:
```python
"AllenCompartment": '...**All Methods and Attributes:** See `AllenCompartment detailed documentation <../pysnt/allencompartment_doc.html>`_...'
```

## Verification

```bash
# Check the generated file
$ grep -o 'detailed documentation <[^>]*>' src/pysnt/_docstring_enhancements.py | head -5
detailed documentation <../pysnt/mouselightquerier_doc.html>
detailed documentation <../pysnt/interactivetracercanvas_doc.html>
detailed documentation <../pysnt/sntui_doc.html>
detailed documentation <../pysnt/zbatlasutils_doc.html>
detailed documentation <../pysnt/tracercanvas_doc.html>
```

✅ All links now use relative paths `../pysnt/`

## How Links Work Now

### From Notebooks:
```markdown
[AllenCompartment](../api_auto/pysnt.annotation.html#pysnt.annotation.AllenCompartment)
```

### From API Auto Pages:
The enhanced docstrings will show:
```
**All Methods and Attributes:** See AllenCompartment detailed documentation.
```
With a link to `../pysnt/allencompartment_doc.html`

### From Detailed Doc Pages:
Links back to API auto pages:
```rst
See Also
--------
* `Package API <../api_auto/pysnt.annotation.html#pysnt.annotation.AllenCompartment>`_
```

## Path Structure

```
docs/
├── api_auto/
│   ├── pysnt.annotation.html          # Auto-generated API
│   └── pysnt.html
├── pysnt/
│   ├── allencompartment_doc.html      # Detailed docs
│   └── tree_doc.html
└── notebooks/
    └── 03_convex_hull.ipynb
```

### Relative Paths:
- From `api_auto/` to `pysnt/`: `../pysnt/`
- From `pysnt/` to `api_auto/`: `../api_auto/`
- From `notebooks/` to `api_auto/`: `../api_auto/`
- From `notebooks/` to `pysnt/`: `../pysnt/`

## Note on Sphinx Autodoc

The enhanced docstrings are applied at runtime when pysnt is imported. For Sphinx autodoc to pick them up:

1. `pysnt.__init__.py` imports `_docstring_enhancements`
2. `enhance_class_docstrings()` runs automatically
3. Classes get enhanced docstrings
4. Sphinx autodoc reads the enhanced `__doc__` attributes

However, this only works for classes that are loaded when the module is imported. Some classes might not get enhanced if they're lazy-loaded.

## Files Modified

1. **`dev/scripts/enhanced_api_docs/structured_integration.py`**
   - Fixed `_get_detailed_doc_link()` to use relative paths

2. **`src/pysnt/_docstring_enhancements.py`** (auto-generated)
   - Regenerated with correct relative paths

## To Apply This Fix

```bash
# Regenerate documentation with the fix
python dev/scripts/generate_api_docs.py

# Rebuild HTML docs
make -C docs html
```

## Status

✅ **FIXED** - All docstring links now use correct relative paths
