# API Reference

```{note}
The API documentation is automatically generated from the code docstrings using Sphinx's autodoc extension. 
```

```{toctree}
:maxdepth: 3
:caption: API Modules

api_auto/pysnt
api_auto/pysnt.core
api_auto/pysnt.analysis
api_auto/pysnt.util
api_auto/pysnt.viewer
api_auto/pysnt.tracing
api_auto/pysnt.java_utils
api_auto/pysnt.setup_utils
```

## Quick Reference

### Core Functions
- {func}`pysnt.initialize_snt` - Initialize the SNT environment
- {func}`pysnt.version` - Get version information  
- {func}`pysnt.info` - Show detailed system information

### Root Classes (Direct Import)
```python
from pysnt import SNTService, SNTUtils, Tree, Path
```

### Analysis Classes
```python
from pysnt.analysis import TreeStatistics, MultiTreeStatistics, ConvexHull
```

### Utility Classes
```python
from pysnt.util import PointInImage, SWCPoint
```

## Usage Patterns

### Basic Usage
```python
import pysnt

# Initialize
pysnt.initialize_snt()

# Import classes
from pysnt import Tree, SNTUtils
from pysnt.analysis import TreeStatistics
```

### Advanced Usage
```python
# Extended class access
import pysnt.analysis as analysis
NodeStats = analysis.get_class("NodeStatistics")

# Discovery
analysis.list_classes()
```

## Core Modules

### Main Package
The {doc}`api_auto/pysnt` module contains the main package interface with root classes and core functionality.

### Initialization
The {doc}`api_auto/pysnt.core` module handles initialization and setup functions.

## Analysis and Data

### Analysis Tools
The {doc}`api_auto/pysnt.analysis` module provides neuronal morphology analysis tools and statistics.

### Utility Classes
The {doc}`api_auto/pysnt.util` module contains utility classes and helper functions.

## Visualization and Tracing

### Visualization
The {doc}`api_auto/pysnt.viewer` module provides 2D and 3D visualization utilities.

### Tracing
The {doc}`api_auto/pysnt.tracing` module contains automated and manual neurite tracing tools.

## Setup and Configuration

### Java Management
The {doc}`api_auto/pysnt.java_utils` module handles Java environment management utilities.

### Setup Utilities
The {doc}`api_auto/pysnt.setup_utils` module provides setup and configuration helpers.