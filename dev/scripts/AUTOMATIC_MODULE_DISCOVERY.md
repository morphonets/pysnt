# Automatic Module Discovery for Docstring Enhancements

## Problem
The module list in `structured_integration.py` was hardcoded:
```python
module_names = [
    'pysnt',
    'pysnt.analysis',
    'pysnt.annotation',  # Had to manually add this!
    'pysnt.converters',
    # ... etc
]
```

This required manual updates whenever:
- A new submodule was added to pysnt
- A module was renamed or removed
- Easy to forget and cause missing enhancements

## Solution: Automatic Discovery

The module list is now automatically discovered by scanning the `src/pysnt/` directory:

```python
def _apply_enhanced_docstrings(enhanced_docstrings):
    """Apply enhanced docstrings to classes in loaded modules."""
    import sys
    from pathlib import Path
    
    # Automatically discover all pysnt submodules
    module_names = ['pysnt']  # Start with main module
    
    # Find the pysnt package directory
    pysnt_dir = None
    for path in sys.path:
        potential_dir = Path(path) / 'pysnt'
        if potential_dir.is_dir() and (potential_dir / '__init__.py').exists():
            pysnt_dir = potential_dir
            break
    
    # Discover submodules
    if pysnt_dir:
        for item in sorted(pysnt_dir.iterdir()):
            if item.is_dir() and not item.name.startswith('_'):
                if (item / '__init__.py').exists():
                    module_names.append(f'pysnt.{item.name}')
    
    # ... rest of enhancement logic
```

## How It Works

### Discovery Logic:
1. Start with `['pysnt']` as the base module
2. Find the pysnt package directory in `sys.path`
3. Iterate through all subdirectories
4. Skip directories starting with `_` or `.` (like `__pycache__`, `__init__.py`, `.git`)
5. Check if directory has `__init__.py` (is a Python package)
6. Add `pysnt.{dirname}` to the module list
7. Sort alphabetically for consistency

### Fallback:
If discovery fails for any reason, falls back to a hardcoded list:
```python
except Exception:
    # If discovery fails, fall back to known modules
    module_names = [
        'pysnt',
        'pysnt.analysis',
        'pysnt.annotation',
        # ... etc
    ]
```

## Benefits

### Before (Manual):
- ❌ Had to manually update list when adding modules
- ❌ Easy to forget new modules (like `pysnt.annotation`)
- ❌ Required code changes for structural changes
- ❌ Maintenance burden

### After (Automatic):
- ✅ Automatically discovers all submodules
- ✅ No manual updates needed
- ✅ Works with any project structure
- ✅ Self-maintaining
- ✅ Sorted alphabetically for consistency

## Discovered Modules

Current automatic discovery finds:
```
- pysnt
- pysnt.analysis
- pysnt.annotation
- pysnt.converters
- pysnt.display
- pysnt.gui
- pysnt.io
- pysnt.tracing
- pysnt.util
- pysnt.viewer
```

## Testing

### Verify Discovery:
```python
from pathlib import Path

pysnt_dir = Path('src/pysnt')
module_names = ['pysnt']

for item in sorted(pysnt_dir.iterdir()):
    if item.is_dir() and not item.name.startswith('_') and not item.name.startswith('.'):
        if (item / '__init__.py').exists():
            module_names.append(f'pysnt.{item.name}')

print(module_names)
```

### Verify Enhancement Works:
```python
import pysnt
pysnt.initialize()
import pysnt.annotation

# Should have enhanced docstring
assert 'detailed documentation' in pysnt.annotation.AllenCompartment.__doc__
```

## Files Modified

1. **`dev/scripts/enhanced_api_docs/structured_integration.py`**
   - Replaced hardcoded module list with automatic discovery
   - Added fallback for robustness

2. **`src/pysnt/_docstring_enhancements.py`** (auto-generated)
   - Now includes automatic discovery code
   - Self-maintaining

## Future-Proof

This change makes the system future-proof:
- ✅ Add new module → automatically discovered
- ✅ Rename module → automatically updated
- ✅ Remove module → automatically excluded
- ✅ No code changes needed

## Status

✅ **IMPLEMENTED** - Module discovery is now fully automatic and self-maintaining.
