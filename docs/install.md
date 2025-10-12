# Installation

## Requirements

- Python 3.8 or higher
- Java 8 or higher (for PyImageJ integration)

## Install pySNT

### Via pip (recommended)

```bash
pip install pysnt
```

### Via conda

```bash
conda install -c conda-forge pysnt
```

### Development Installation

For the latest development version:

```bash
git clone https://github.com/morphonets/pysnt.git
cd pysnt
pip install -e .
```

## Verify Installation

Test your installation by running:

```python
import pysnt
print(pysnt.__version__)
```

## Next Steps

- Check out the [Getting Started notebook](notebooks/1_overview.ipynb)
- Browse the [Notebooks Gallery](notebooks/index.md)
- Read the [SNT User Manual](https://imagej.net/plugins/snt/)