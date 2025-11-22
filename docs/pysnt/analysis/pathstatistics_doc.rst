
``PathStatistics`` Class Documentation
===================================


.. toctree::
   :maxdepth: 3
   :caption: Complete API Reference
   :hidden:

   ../api_auto/index
   ../api_auto/pysnt
   ../api_auto/pysnt.analysis
   ../api_auto/pysnt.analysis.graph
   ../api_auto/pysnt.analysis.growth
   ../api_auto/pysnt.analysis.sholl
   ../api_auto/pysnt.analysis.sholl.gui
   ../api_auto/pysnt.analysis.sholl.math
   ../api_auto/pysnt.analysis.sholl.parsers
   ../api_auto/pysnt.annotation
   ../api_auto/pysnt.converters
   ../api_auto/pysnt.converters.chart_converters
   ../api_auto/pysnt.converters.core
   ../api_auto/pysnt.converters.enhancement
   ../api_auto/pysnt.converters.extractors
   ../api_auto/pysnt.converters.graph_converters
   ../api_auto/pysnt.converters.structured_data_converters
   ../api_auto/pysnt.core
   ../api_auto/pysnt.display
   ../api_auto/pysnt.display.core
   ../api_auto/pysnt.display.data_display
   ../api_auto/pysnt.display.utils
   ../api_auto/pysnt.display.visual_display
   ../api_auto/pysnt.gui
   ../api_auto/pysnt.gui.cmds
   ../api_auto/pysnt.io
   ../api_auto/pysnt.tracing
   ../api_auto/pysnt.tracing.artist
   ../api_auto/pysnt.tracing.cost
   ../api_auto/pysnt.tracing.heuristic
   ../api_auto/pysnt.tracing.image
   ../api_auto/pysnt.util
   ../api_auto/pysnt.viewer
   ../api_auto/pysnt.common_module
   ../api_auto/pysnt.config
   ../api_auto/pysnt.gui_utils
   ../api_auto/pysnt.java_utils
   ../api_auto/pysnt.setup_utils
   ../api_auto/method_index
   ../api_auto/class_index
   ../api_auto/constants_index


**Package:** ``sc.fiji.snt.analysis``

A specialized version of TreeStatistics for analyzing individual paths without considering their connectivity relationships.

PathStatistics provides morphometric analysis of neuronal paths while treating each path as an independent entity, rather than as part of a connected tree structure.

Key differences from TreeStatistics:

No graph conversion - paths are analyzed independently Branch-related metrics are redefined to work with individual paths Supports path-specific measurements like Path ID and number of children Provides individual path measurement capabilities

Example usage: 
```
// Analyze a single path
PathStatistics stats = new PathStatistics(path);
double length = stats.getMetric("Path length").doubleValue();

// Analyze multiple paths independently
Collection<Path> paths = getPaths();
PathStatistics multiStats = new PathStatistics(paths, "My Analysis");
multiStats.measureIndividualPaths(Arrays.asList("Path length", "N. nodes"), true);
```


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getAllMetrics()

   Gets the terminal branches from the analyzed paths.

Returns paths that have children, representing non-terminal segments. Note: This implementation differs from typical terminal branch definition as it returns paths with children rather than leaf paths.


.. py:method:: getAnnotatedLength(int, String, boolean)

   


.. py:method:: getAnnotatedLengthHistogram(int, String)

   


.. py:method:: getAnnotatedLengthsByHemisphere(int)

   


.. py:method:: getAnnotations(int)

   


.. py:method:: getAvgBranchLength()

   Gets the total length of terminal branches.

Calculates the sum of lengths of all terminal branches as defined by `getTerminalBranches()`.


.. py:method:: getAvgContraction()

   


.. py:method:: getAvgFractalDimension()

   


.. py:method:: getAvgFragmentation()

   


.. py:method:: getAvgPartitionAsymmetry()

   


.. py:method:: getAvgRemoteBifAngle()

   


.. py:method:: getBranchPoints(BrainAnnotation, boolean)

   


.. py:method:: getBranches()

   Gets all the paths being analyzed as branches.

In PathStatistics, all paths are considered as branches since each path represents a distinct structural element.


.. py:method:: getCableLength()

   


.. py:method:: getCableLengthNorm(BrainAnnotation)

   


.. py:method:: getCancelReason()

   


.. py:method:: getContext()

   


.. py:method:: getConvexAnalyzer()

   


.. py:method:: getConvexHullMetric(String)

   


.. py:method:: getDepth()

   


.. py:method:: getDescriptiveStats(String)

   


.. py:method:: getFlowPlot(String, Collection, String, double, boolean)

   


.. py:method:: getFractalDimension()

   


.. py:method:: getHeight()

   


.. py:method:: getHighestPathOrder()

   Gets the number of branches (paths) being analyzed.

Returns the total count of paths in this PathStatistics instance.


.. py:method:: getHistogram(String)

   


.. py:method:: getInnerBranches()

   Gets the inner branches from the analyzed paths.

In PathStatistics, inner branches are equivalent to primary branches.


.. py:method:: getInnerLength()

   Gets the total length of inner branches.

In PathStatistics, this returns the same value as getPrimaryLength().


.. py:method:: getMetric(String, Path)

   Gets a specific metric value for an individual path.

This method provides direct access to morphometric properties of individual paths, including geometric measurements, connectivity information, and structural characteristics. It supports all standard path metrics plus PathStatistics-specific measurements.

Supported metrics include:

Geometric: length, volume, surface area, mean radius Structural: number of nodes, branch points, children Angular: extension angles in XY, XZ, ZY planes Morphological: contraction, fractal dimension, spine density Metadata: path ID, channel, frame, order


.. py:method:: static getMetrics()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: cancel(String)

   Measures specified metrics for each individual path and creates a detailed table.

This method generates a comprehensive measurement table where each row represents an individual path and columns contain the requested morphometric measurements. This is particularly useful for comparative analysis of path properties or for exporting detailed morphometric data.

The generated table includes:

Path identification information (name, SWC type) All requested morphometric measurements Optional summary statistics (if summarize is true)


.. py:method:: context()

   


.. py:method:: dispose()

   


.. py:method:: static fromCollection(Collection, String)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.PathStatistics>`_
* `PathStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/PathStatistics.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
