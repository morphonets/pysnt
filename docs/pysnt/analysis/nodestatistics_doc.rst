
``NodeStatistics`` Class Documentation
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

Computes summary and descriptive statistics from a Collection of nodes, including convenience methods to plot distributions of such data.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: get(BrainAnnotation)

   Gets the list of nodes associated with the specified compartment (neuropil label).


.. py:method:: getAnnotatedFrequencies(int, String)

   Retrieves the count frequencies across brain compartment.


.. py:method:: getAnnotatedFrequenciesByHemisphere(int, Tree)

   


.. py:method:: getAnnotatedFrequencyHistogram(int, String, Tree)

   Retrieves the histogram of count frequencies across brain areas of the specified ontology level across the specified hemisphere.


.. py:method:: getAnnotatedHistogram()

   Retrieves the histogram of count frequencies across brain areas of the specified ontology level.


.. py:method:: getAnnotatedNodes()

   Splits the nodes being analyzed into groups sharing the same brain annotation.


.. py:method:: getDescriptiveStatistics(String)

   Computes the `DescriptiveStatistics` for the specified measurement.


.. py:method:: getHistogram(String)

   Gets the relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.


.. py:method:: static getMetrics()

   Gets the list of supported metrics.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setLabel(String)

   Sets a descriptive label to this statistic analysis to be used in histograms, etc.


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: static computeNearestNeighborDistances(List)

   Computes nearest neighbor distances. Assigns the computed value to the v value of each point


Other Methods
~~~~~~~~~~~~~


.. py:method:: assignBranches(Tree)

   Associates the nodes being analyzed to the branches of the specified tree


.. py:method:: filter(String, double, double)

   Filters the current pool of nodes matching a measurement-based criterion.


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.NodeStatistics>`_
* `NodeStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/NodeStatistics.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
