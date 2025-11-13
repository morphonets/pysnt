
``TreeStatistics`` Class Documentation
===================================


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

Enhanced documentation for TreeStatistics class.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getAllMetrics())

   Gets the list of supported metrics.


.. py:method:: getAnnotatedLength(int))

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron.


.. py:method:: getAnnotatedLengthHistogram(int, String))

   Retrieves the histogram of cable length frequencies across brain areas of the specified ontology level across the specified hemisphere.


.. py:method:: getAnnotatedLengthsByHemisphere(int))

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron in the two brain hemispheres. Lengths are absolute and not normalized to the cells' cable length.


.. py:method:: getAnnotations(int))

   Retrieves the brain compartments (neuropil labels) associated with the Tree being measured innervated by the analyzed neuron.


.. py:method:: getAvgBranchLength())

   Gets average length for all the branches of the analyzed tree.


.. py:method:: getAvgContraction())

   Gets average contraction for all the branches of the analyzed tree.


.. py:method:: getAvgFractalDimension())

   Gets the average fractal dimension of the analyzed tree. Note that branches with less than 5 points are ignored during the computation.


.. py:method:: getAvgFragmentation())

   Gets the average no. of nodes (fragmentation) for all the branches of the analyzed tree.


.. py:method:: getAvgPartitionAsymmetry())

   Gets the average partition asymmetry of the analyzed tree. Note that branch points with more than 2 children are ignored during the computation.


.. py:method:: getAvgRemoteBifAngle())

   Gets the average remote bifurcation angle of the analyzed tree. Note that branch points with more than 2 children are ignored during the computation.


.. py:method:: getBranchPoints())

   Gets the position of all the branch points in the analyzed tree associated with the specified annotation.


.. py:method:: getBranches())

   Gets all the branches in the analyzed tree. A branch is defined as the Path composed of all the nodes between two branching points or between one branching point and a termination point.


.. py:method:: getCableLength(BrainAnnotation))

   Gets the cable length associated with the specified compartment (neuropil label).


.. py:method:: getCableLengthNorm(BrainAnnotation))

   Gets the cable length associated with the specified compartment (neuropil label) as a ratio of total length.


.. py:method:: getCancelReason())

   


.. py:method:: getContext())

   


.. py:method:: getConvexAnalyzer())

   Gets the ConvexHullAnalyzer instance associated with this TreeStatistics instance.


.. py:method:: getConvexHullMetric(String))

   Convenience method to obtain a single-value metric from ConvexHullAnalyzer


.. py:method:: getDepth())

   Returns the depth of the BoundingBox box of the tree being measured


.. py:method:: getDescriptiveStats(String))

   Computes the `DescriptiveStatistics` for the specified measurement.


.. py:method:: getFlowPlot(String, Collection, boolean))

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.


.. py:method:: getFractalDimension())

   Gets the fractal dimension of each branch in the analyzed tree. Note that branches with less than 5 points are ignored.


.. py:method:: getHeight())

   Returns the height of the BoundingBox box of the tree being measured


.. py:method:: getHighestPathOrder())

   Gets the highest path order of the analyzed tree


.. py:method:: getHistogram(String))

   Retrieves the histogram of relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.


.. py:method:: getInnerBranches())

   Retrieves the branches of highest Strahler order in the Tree. This typically correspond to the most 'internal' branches of the Tree in direct sequence from the root.


.. py:method:: getInnerLength())

   Gets the cable length of inner branches


.. py:method:: getMetric(String))

   Computes the specified metric.


.. py:method:: static getMetrics())

   Gets the list of most commonly used metrics.


.. py:method:: getNBranchPoints(BrainAnnotation))

   Gets the number of branch points in the analyzed tree associated with the specified annotation.


Other Methods
~~~~~~~~~~~~~


.. py:method:: cancel(String))

   Sets the table for this TreeStatistics instance.


.. py:method:: context())

   


.. py:method:: dispose())

   Clears internal caches and mappings to free memory.


.. py:method:: static fromCollection(Collection, String))

   Creates a TreeStatistics instance from a group of Trees and a specific metric for convenient retrieval of histograms


See Also
--------

* `Package API <../../api_auto/pysnt.analysis.html#pysnt.analysis.TreeStatistics>`_
* `Main API Documentation <../../api_auto/pysnt.analysis#TreeStatistics>`_
* `TreeStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/TreeStatistics.html>`_
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Class Index </api_auto/class_index>`

