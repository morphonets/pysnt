
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

A specialized version of ``TreeStatistics`` for analyzing individual paths without considering their connectivity relationships.

PathStatistics provides morphometric analysis of neuronal paths while treating each path as an independent entity, rather than as part of a connected tree structure.

Key differences from TreeStatistics:

- No graph conversion - paths are analyzed independently

- Branch-related metrics are redefined to work with individual paths

- Supports path-specific measurements like Path ID and number of children

- Provides individual path measurement capabilities

Example usage: 


::

    // Analyze a single path
    PathStatistics stats = new PathStatistics(path);
    double length = stats.getMetric("Path length").doubleValue();

    // Analyze multiple paths independently
    Collection<Path> paths = getPaths();
    PathStatistics multiStats = new PathStatistics(paths, "My Analysis");
    multiStats.measureIndividualPaths(Arrays.asList("Path length", "N. nodes"), true);




Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: resetRestrictions()

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAllMetrics()

   


.. py:method:: getAnnotatedLength(int)

   


.. py:method:: getAnnotatedLengthHistogram()

   


.. py:method:: getAnnotatedLengthsByHemisphere(int)

   


.. py:method:: getAnnotations()

   


.. py:method:: getAvgBranchLength()

   


.. py:method:: getAvgContraction()

   


.. py:method:: getAvgFractalDimension()

   


.. py:method:: getAvgFragmentation()

   


.. py:method:: getAvgPartitionAsymmetry()

   


.. py:method:: getAvgRemoteBifAngle()

   


.. py:method:: getBranchPoints()

   


.. py:method:: getBranches()

   Gets all the paths being analyzed as branches.

   In PathStatistics, all paths are considered as branches since each path represents a distinct structural element.


.. py:method:: getCableLength()

   


.. py:method:: getCableLengthNorm(BrainAnnotation)

   


.. py:method:: getConvexAnalyzer()

   


.. py:method:: getConvexHullMetric(String)

   


.. py:method:: getDepth()

   


.. py:method:: getDescriptiveStats(String)

   


.. py:method:: getFlowPlot(String, Collection)

   


.. py:method:: getFractalDimension()

   


.. py:method:: getHeight()

   


.. py:method:: getHighestPathOrder()

   


.. py:method:: getHistogram(String)

   


.. py:method:: getInnerBranches()

   Gets the inner branches from the analyzed paths.

   In PathStatistics, inner branches are equivalent to primary branches.


.. py:method:: getInnerLength()

   Gets the total length of inner branches.

   In PathStatistics, this returns the same value as ``getPrimaryLength()``.


.. py:method:: getMetric(String)

   Gets a specific metric value for an individual path.

   This method provides direct access to morphometric properties of individual paths, including geometric measurements, connectivity information, and structural characteristics. It supports all standard path metrics plus PathStatistics-specific measurements.

   Supported metrics include:

   - Geometric: length, volume, surface area, mean radius

   - Structural: number of nodes, branch points, children

   - Angular: extension angles in XY, XZ, ZY planes

   - Morphological: contraction, fractal dimension, spine density

   - Metadata: path ID, channel, frame, order


.. py:method:: getMetrics()

   


.. py:method:: getNBranchPoints(BrainAnnotation)

   


.. py:method:: getNBranchPointsNorm(BrainAnnotation)

   


.. py:method:: getNBranches()

   Gets the number of branches (paths) being analyzed.

   Returns the total count of paths in this PathStatistics instance.


.. py:method:: getNNodes()

   


.. py:method:: getNPaths()

   


.. py:method:: getNTips(BrainAnnotation)

   


.. py:method:: getNTipsNorm(BrainAnnotation)

   


.. py:method:: getNoSpinesOrVaricosities()

   


.. py:method:: getNodeStatistics()

   


.. py:method:: getParsedTree()

   


.. py:method:: getPartitionAsymmetry()

   


.. py:method:: getPolarHistogram(String)

   


.. py:method:: getPrimaryBranches()

   Gets the primary branches from the analyzed paths.

   Returns only those paths that are marked as primary branches, typically those that originate directly from the root or soma.


.. py:method:: getPrimaryLength()

   Gets the total length of primary branches.

   Calculates the sum of lengths of all paths marked as primary branches.


.. py:method:: getPrimaryPaths()

   


.. py:method:: getRemoteBifAngles()

   


.. py:method:: getRootAngleAnalyzer()

   


.. py:method:: getRootAngleMetric(String)

   


.. py:method:: getShollAnalyzer()

   


.. py:method:: getSpineOrVaricosityDensity()

   


.. py:method:: getStrahlerAnalyzer()

   


.. py:method:: getStrahlerBifurcationRatio()

   


.. py:method:: getStrahlerNumber()

   


.. py:method:: getSummaryStats(String)

   Description copied from class: ``TreeStatistics``


.. py:method:: getTable()

   


.. py:method:: getTerminalBranches()

   Gets the terminal branches from the analyzed paths.

   Returns paths that have children, representing non-terminal segments. Note: This implementation differs from typical terminal branch definition as it returns paths with children rather than leaf paths.


.. py:method:: getTerminalLength()

   Gets the total length of terminal branches.

   Calculates the sum of lengths of all terminal branches as defined by ``getTerminalBranches()``.


.. py:method:: getTips()

   


.. py:method:: getUnit(String)

   


.. py:method:: getWidth()

   


.. py:method:: isExactMetricMatch()

   


.. py:method:: isValid()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setExactMetricMatch(boolean)

   


.. py:method:: setTable(GenericTable)

   


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: measure(Collection, boolean)

   


.. py:method:: measureIndividualPaths(Collection, boolean)

   Measures specified metrics for each individual path and creates a detailed table.

   This method generates a comprehensive measurement table where each row represents an individual path and columns contain the requested morphometric measurements. This is particularly useful for comparative analysis of path properties or for exporting detailed morphometric data.

   The generated table includes:

   - Path identification information (name, SWC type)

   - All requested morphometric measurements

   - Optional summary statistics (if summarize is true)


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: updateAndDisplayTable()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: dispose()

   


.. py:method:: fromCollection(Collection, String)

   


.. py:method:: restrictToSWCType(int[])

   


.. py:method:: run()

   


.. py:method:: summarize(boolean)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.PathStatistics>`_
* `PathStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/PathStatistics.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
