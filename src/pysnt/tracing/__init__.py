"""
This module provides convenient access to
`SNT's tracing classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "BiSearch",
    "BiSearchNode",
    "DefaultSearchNode",
    "FillerThread",
    "PathResult",
    "SearchNode",
    "SearchThread",
    "TracerThread",
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "AbstractSearch",
    "ManualTracerThread",
    "SearchInterface",
    "TubularGeodesicsTracer",
]


# Placeholder classes for IDE support - will be replaced with Java classes
class BiSearch:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    **JavaDoc Description**:
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.

    **Usage Examples**:

    .. code-block:: python

        bisearch = BiSearch()
        result = bisearch.addProgressListener()

    See `tracing_BiSearch_javadoc`_.
    
    .. _tracing_BiSearch_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/BiSearch.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class BiSearchNode:
    """
    A SearchNode which can maintain both a from-start and from-goal search state.
    
    **All Methods and Attributes:** See `BiSearchNode detailed documentation <../pysnt/tracing/bisearchnode_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.

The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </bisearch_doc.html>`_.
    """
    """
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute. The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Attributes:** See `BiSearch detailed documentation </pysnt/tracing/bisearch_doc.html>`_ for comprehensive information.
    """
    """
    Curated SNT class with enhanced JavaDoc integration.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    **JavaDoc Description:**
    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute. The search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.
    
    **All Methods and Fields:**
    See :doc:`pysnt.tracing.bisearch_doc` for comprehensive documentation with all methods, fields, and usage examples.
    
    See `BiSearch JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/BiSearch.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class DefaultSearchNode:
    """
    A SearchNode which can maintain both a from-start and from-goal search state.
    
    **All Methods and Attributes:** See `DefaultSearchNode detailed documentation <../pysnt/tracing/defaultsearchnode_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class FillerThread:
    """
    Seeded-volume segmentation via single-source shortest paths. Path nodes are used as seed points in an open-ended variant of Dijkstra's algorithm. The threshold sets the maximum allowable distance for a node to be included in the Fill. This distance is represented in the g-score of a node, which is the length of the shortest path from a seed point to that node. The magnitudes of these distances are heavily dependent on the supplied cost function Cost, so the threshold should be set with a particular cost function in mind. It often helps to adjust the threshold interactively.
    
    **All Methods and Attributes:** See `FillerThread detailed documentation <../pysnt/tracing/fillerthread_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathResult:
    """
    SNT class with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    **All Methods and Attributes:** See `PathResult detailed documentation <../pysnt/tracing/pathresult_doc.html>`_.
    
    See `PathResult JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/PathResult.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SearchNode:
    """
    SNT class with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    **All Methods and Attributes:** See `SearchNode detailed documentation <../pysnt/tracing/searchnode_doc.html>`_.
    
    See `SearchNode JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/SearchNode.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SearchThread:
    """
    Implements a common thread that explores the image using a variety of strategies, e.g., to trace tubular structures or surfaces.
    
    **All Methods and Attributes:** See `SearchThread detailed documentation <../pysnt/tracing/searchthread_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class TracerThread:
    """
    SNT's default tracer thread: explores between two points in an image, doing an A* search with a choice of distance measures.
    
    **All Methods and Attributes:** See `TracerThread detailed documentation <../pysnt/tracing/tracerthread_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.tracing",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    include_interfaces=True  # Include interfaces for tracing
)

# Import functions into module namespace
get_available_classes = _module_funcs["get_available_classes"]
get_class = _module_funcs["get_class"]
list_classes = _module_funcs["list_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt.tracing", submodules=["artist", "cost", "heuristic", "image"])
__dir__ = _module_funcs["create_dir"]()


# Static __all__ with curated classes always available
# This ensures IDEs know these symbols are available for import
__all__ = [
    # Functions
    "get_available_classes",
    "get_class",
    "list_classes",
    "get_curated_classes",
    "get_extended_classes",
    # Constants
    "CURATED_CLASSES",
    "EXTENDED_CLASSES",
    # Curated classes (always available for direct import)
    "SearchThread",
    "TracerThread",
    # Submodules
    "artist",
    "cost", 
    "heuristic",
    "image",
]

# Submodule imports
from . import artist, cost, heuristic, image
