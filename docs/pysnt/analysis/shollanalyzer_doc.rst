
``ShollAnalyzer`` Class Documentation
==================================


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

Class to retrieve Sholl metrics from a Tree.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getLinearStats()

   Gets the LinearProfileStats associated with this analyzer. By default, it is set to determine the polynomial of 'best-fit' (2-20 degree range.)


.. py:method:: getMaximaRadii()

   


.. py:method:: static getMetrics()

   


.. py:method:: getNormStats()

   Gets the `NormalizedProfileStats` associated with this analyzer. By default it is set to determine the regression method of 'best-fit' (log-log or semi-log) using shell volume as normalizer (if Tree has a depth component) or shell area if Tree is 2D.


.. py:method:: getSecondaryMaxima()

   


.. py:method:: getSingleValueMetrics()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setEnableCurveFitting(boolean)

   Sets whether curve fitting computations should be performed.


.. py:method:: setPolynomialFitRange(int, int)

   Sets the polynomial fit range for linear Sholl statistics.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.ShollAnalyzer>`_
* `ShollAnalyzer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/ShollAnalyzer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
