
``GroupedTreeStatistics`` Class Documentation
==========================================


.. toctree::
   :maxdepth: 3
   :caption: Complete API Reference
   :hidden:

   ../../api_auto/index
   ../../api_auto/pysnt
   ../../api_auto/pysnt.analysis
   ../../api_auto/pysnt.analysis.graph
   ../../api_auto/pysnt.analysis.growth
   ../../api_auto/pysnt.analysis.sholl
   ../../api_auto/pysnt.analysis.sholl.gui
   ../../api_auto/pysnt.analysis.sholl.math
   ../../api_auto/pysnt.analysis.sholl.parsers
   ../../api_auto/pysnt.annotation
   ../../api_auto/pysnt.converters
   ../../api_auto/pysnt.converters.chart_converters
   ../../api_auto/pysnt.converters.core
   ../../api_auto/pysnt.converters.enhancement
   ../../api_auto/pysnt.converters.extractors
   ../../api_auto/pysnt.converters.graph_converters
   ../../api_auto/pysnt.converters.structured_data_converters
   ../../api_auto/pysnt.core
   ../../api_auto/pysnt.display
   ../../api_auto/pysnt.display.core
   ../../api_auto/pysnt.display.data_display
   ../../api_auto/pysnt.display.utils
   ../../api_auto/pysnt.display.visual_display
   ../../api_auto/pysnt.gui
   ../../api_auto/pysnt.gui.cmds
   ../../api_auto/pysnt.io
   ../../api_auto/pysnt.tracing
   ../../api_auto/pysnt.tracing.artist
   ../../api_auto/pysnt.tracing.cost
   ../../api_auto/pysnt.tracing.heuristic
   ../../api_auto/pysnt.tracing.image
   ../../api_auto/pysnt.util
   ../../api_auto/pysnt.viewer
   ../../api_auto/pysnt.common_module
   ../../api_auto/pysnt.config
   ../../api_auto/pysnt.gui_utils
   ../../api_auto/pysnt.java_utils
   ../../api_auto/pysnt.setup_utils
   ../../api_auto/method_index


**Package:** ``sc.fiji.snt.analysis``

Enhanced documentation for GroupedTreeStatistics class.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBoxPlot(String, int, double, boolean))

   Assembles a Box and Whisker Plot for the specified feature.


.. py:method:: getFlowPlot(String, Collection, boolean))

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.


.. py:method:: getGroupStats(String))

   Gets the group statistics.


.. py:method:: getGroups())

   Gets the group identifiers currently queued for analysis.


.. py:method:: getHistogram(String))

   Gets the relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.


.. py:method:: getN(String))

   Gets the number of Trees in a specified group.


.. py:method:: getPolarHistogram(String))

   Gets the relative frequencies histogram for a univariate measurement as a polar (rose) plot assuming a data range between [0-360]. The number of bins is determined using the Freedman-Diaconis rule.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setMinNBins(int))

   Sets the minimum number of bins when assembling histograms.


Other Methods
~~~~~~~~~~~~~


.. py:method:: addGroup(Collection, String))

   Adds a comparison group to the analysis queue.


.. py:method:: anovaPValue(String))

   Computes the one-way ANOVA P-value for all the groups being analyzed. It is assumed that data fulfills basic assumptions on normality, variance homogeneity, sample size, etc.


.. py:method:: static main(String;))

   


.. py:method:: tTest(String, String, String))

   Computes a two-sample, two-tailed t-test P-value for two of groups being analyzed. It is assumed that data fulfills basic assumptions on normality, variance homogeneity, etc.


See Also
--------

* `Package API <../../api_auto/pysnt.analysis.html#pysnt.analysis.GroupedTreeStatistics>`_
* `Main API Documentation <../../api_auto/pysnt.analysis#GroupedTreeStatistics>`_
* `GroupedTreeStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/GroupedTreeStatistics.html>`_
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Class Index </api_auto/class_index>`

