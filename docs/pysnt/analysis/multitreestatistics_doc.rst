
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

Computes summary and descriptive statistics from univariate properties of Tree groups. For analysis of individual Trees use TreeStatistics.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getAllMetrics()

   Description copied from class: TreeStatistics


.. py:method:: getAnnotatedLength(int)

   Description copied from class: TreeStatistics


.. py:method:: getAnnotatedLengthHistogram(int)

   


.. py:method:: getAnnotatedLengthsByHemisphere(int)

   Description copied from class: TreeStatistics


.. py:method:: getAnnotations()

   Description copied from class: TreeStatistics


.. py:method:: getAvgBranchLength()

   


.. py:method:: getAvgContraction()

   


.. py:method:: getAvgFractalDimension()

   


.. py:method:: getAvgFragmentation()

   


.. py:method:: getAvgPartitionAsymmetry()

   


.. py:method:: getAvgRemoteBifAngle()

   


.. py:method:: getBoxPlot(String)

   


.. py:method:: getBranchPoints()

   Description copied from class: TreeStatistics


.. py:method:: getBranches()

   Description copied from class: TreeStatistics


.. py:method:: getCableLength()

   Description copied from class: TreeStatistics


.. py:method:: getCableLengthNorm(BrainAnnotation)

   


.. py:method:: getCancelReason()

   


.. py:method:: getContext()

   


.. py:method:: getConvexAnalyzer()

   


.. py:method:: getConvexHullMetric(String)

   


.. py:method:: getDepth()

   


.. py:method:: getDescriptiveStats(String)

   Description copied from class: TreeStatistics


.. py:method:: getFlowPlot(String, Collection, String, double, boolean)

   Description copied from class: TreeStatistics


.. py:method:: getFractalDimension()

   


.. py:method:: getGroup()

   Gets the collection of Trees being analyzed.


.. py:method:: getHeight()

   


.. py:method:: getHighestPathOrder()

   


.. py:method:: getHistogram(String)

   Description copied from class: TreeStatistics


.. py:method:: getInnerBranches()

   Description copied from class: TreeStatistics


.. py:method:: getInnerLength()

   


.. py:method:: getMetric(String)

   


.. py:method:: static getMetrics()

   Gets the list of metrics supported by MultiTreeStatistics.

Returns all the metrics that can be computed for groups of trees, including aggregate measures and group-specific statistics.


Other Methods
~~~~~~~~~~~~~


.. py:method:: cancel(String)

   Main method for testing and demonstration purposes.

Creates a MultiTreeStatistics instance using demo data and displays various analysis plots including histograms and flow plots. This method is primarily used for development and debugging.


.. py:method:: context()

   


.. py:method:: dispose()

   Description copied from class: TreeStatistics


.. py:method:: static fromCollection(Collection, String)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.MultiTreeStatistics>`_
* `MultiTreeStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/MultiTreeStatistics.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
