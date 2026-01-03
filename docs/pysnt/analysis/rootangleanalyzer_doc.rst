
``RootAngleAnalyzer`` Class Documentation
======================================


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

Class to perform Root angle analysis on a Tree according to Bird and Cuntz 2019, PMID 31167149.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnalysis()

   


.. py:method:: getAngles()

   


.. py:method:: getCramerVonMisesStatistic()

   Computes the Cramér-von Mises statistic between computed root angles and fitted von Mises distribution. A value of 0 indicates a perfect fit between the empirical distribution and the theoretical distribution, and larger values indicate a greater discrepancy between the two distributions.


.. py:method:: getDensityPlot()

   


.. py:method:: static getDensityPlot(List)

   


.. py:method:: getDescriptiveStatistics()

   


.. py:method:: static getHistogram(List, boolean)

   


.. py:method:: getHistogram(boolean)

   


.. py:method:: getTaggedGraph()

   


.. py:method:: getTaggedTree(ColorTable, double, double)

   Returns a recolored copy of the analyzed tree with the root angles assigned to its node values.


Other Methods
~~~~~~~~~~~~~


.. py:method:: balancingFactor()

   Returns the balancing factor, computed from centripetalBias().


.. py:method:: centripetalBias()

   Returns the strength of the centripetal bias, also known as κ. κ is defined as the concentration of the von Mises fit of the root angle distribution. κ= 0 indicate no bias (root angles are distributed uniformly). K->∞ indicate that all neurites point directly toward the root of the tree


.. py:method:: static main(String;)

   


.. py:method:: max()

   


.. py:method:: mean()

   


.. py:method:: meanDirection()

   Returns the mean direction of the fitted von Mises distribution.


.. py:method:: min()

   


.. py:method:: static supportedMetrics()

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.RootAngleAnalyzer>`_
* `RootAngleAnalyzer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/RootAngleAnalyzer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
