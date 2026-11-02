
``MultiTreeStatistics`` Class Documentation
========================================


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

Computes summary and descriptive statistics from univariate properties of ``Tree`` groups. For analysis of individual Trees use ``TreeStatistics``.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: resetRestrictions()

   Description copied from class: ``TreeStatistics``


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAllMetrics()

   


.. py:method:: getAnnotatedLength(int)

   Description copied from class: ``TreeStatistics``


.. py:method:: getAnnotatedLengthHistogram()

   


.. py:method:: getAnnotatedLengthsByHemisphere(int)

   Description copied from class: ``TreeStatistics``


.. py:method:: getAnnotations()

   Description copied from class: ``TreeStatistics``


.. py:method:: getAvgBranchLength()

   


.. py:method:: getAvgContraction()

   


.. py:method:: getAvgFractalDimension()

   


.. py:method:: getAvgFragmentation()

   


.. py:method:: getAvgPartitionAsymmetry()

   


.. py:method:: getAvgRemoteBifAngle()

   


.. py:method:: getBoxPlot(String)

   Assembles a Box and Whisker Plot for the specified measurement (cell morphometry).


.. py:method:: getBranchPoints()

   Description copied from class: ``TreeStatistics``


.. py:method:: getBranches()

   Description copied from class: ``TreeStatistics``


.. py:method:: getCableLength()

   Description copied from class: ``TreeStatistics``


.. py:method:: getCableLengthNorm(BrainAnnotation)

   


.. py:method:: getConvexAnalyzer()

   


.. py:method:: getConvexHullMetric(String)

   


.. py:method:: getDepth()

   


.. py:method:: getDescriptiveStats(String)

   Description copied from class: ``TreeStatistics``


.. py:method:: getFlowPlot(String, Collection)

   Description copied from class: ``TreeStatistics``


.. py:method:: getFractalDimension()

   


.. py:method:: getGroup()

   Gets the collection of Trees being analyzed.


.. py:method:: getHeight()

   


.. py:method:: getHighestPathOrder()

   


.. py:method:: getHistogram(String)

   Description copied from class: ``TreeStatistics``


.. py:method:: getInnerBranches()

   Description copied from class: ``TreeStatistics``


.. py:method:: getInnerLength()

   


.. py:method:: getMetric(String)

   


.. py:method:: getMetrics()

   Gets the list of metrics supported by MultiTreeStatistics.

   Returns all the metrics that can be computed for groups of trees, including aggregate measures and group-specific statistics.


.. py:method:: getNBranchPoints(BrainAnnotation)

   


.. py:method:: getNBranchPointsNorm(BrainAnnotation)

   


.. py:method:: getNBranches()

   


.. py:method:: getNNodes()

   


.. py:method:: getNPaths()

   


.. py:method:: getNTips(BrainAnnotation)

   


.. py:method:: getNTipsNorm(BrainAnnotation)

   


.. py:method:: getNoSpinesOrVaricosities()

   


.. py:method:: getNodeStatistics()

   


.. py:method:: getParsedTree()

   


.. py:method:: getPartitionAsymmetry()

   


.. py:method:: getPolarHistogram(String)

   Description copied from class: ``TreeStatistics``


.. py:method:: getPrimaryBranches()

   Description copied from class: ``TreeStatistics``


.. py:method:: getPrimaryLength()

   


.. py:method:: getPrimaryPaths()

   


.. py:method:: getRawValues(String)

   


.. py:method:: getRemoteBifAngles()

   


.. py:method:: getRootAngleAnalyzer()

   


.. py:method:: getRootAngleMetric(String)

   


.. py:method:: getShollAnalyzer()

   Description copied from class: ``TreeStatistics``


.. py:method:: getSpineOrVaricosityDensity()

   


.. py:method:: getStrahlerAnalyzer()

   Description copied from class: ``TreeStatistics``


.. py:method:: getStrahlerBifurcationRatio()

   


.. py:method:: getStrahlerNumber()

   


.. py:method:: getSummaryStats(String)

   Description copied from class: ``TreeStatistics``


.. py:method:: getTable()

   


.. py:method:: getTerminalBranches()

   Description copied from class: ``TreeStatistics``


.. py:method:: getTerminalLength()

   


.. py:method:: getTips()

   Description copied from class: ``TreeStatistics``


.. py:method:: getUnit(String)

   


.. py:method:: getWidth()

   


.. py:method:: isExactMetricMatch()

   The group is 3D if any of its (non-empty) trees is


.. py:method:: isValid()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setExactMetricMatch(boolean)

   Main method for testing and demonstration purposes.

   Creates a MultiTreeStatistics instance using demo data and displays various analysis plots including histograms and flow plots. This method is primarily used for development and debugging.


.. py:method:: setLabel(String)

   Sets an identifying label for the group of Trees being analyzed.


.. py:method:: setTable(GenericTable)

   


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: measure(Collection, boolean)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: updateAndDisplayTable()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: dispose()

   


.. py:method:: fromCollection(Collection, String)

   


.. py:method:: restrictToSWCType(int[])

   Description copied from class: ``TreeStatistics``


.. py:method:: run()

   


.. py:method:: summarize(boolean)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.MultiTreeStatistics>`_
* `MultiTreeStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/MultiTreeStatistics.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
