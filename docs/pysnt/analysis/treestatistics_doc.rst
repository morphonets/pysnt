
``TreeStatistics`` Class Documentation
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

Computes summary and descriptive statistics from properties of Paths and Nodes in a ``Tree``, including convenience methods to plot distributions of such data. For analysis of groups of Trees have a look at ``MultiTreeStatistics`` and ``GroupedTreeStatistics``.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: resetRestrictions()

   Removes any filtering restrictions that may have been set. Once called, subsequent analysis will use all paths initially parsed by the constructor. Does nothing if no paths are currently being excluded from the analysis.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAllMetrics()

   Gets the list of supported metrics.


.. py:method:: getAnnotatedLength(int)

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron.


.. py:method:: getAnnotatedLengthHistogram()

   


.. py:method:: getAnnotatedLengthsByHemisphere(int)

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron in the two brain hemispheres. Lengths are absolute and not normalized to the cells' cable length.


.. py:method:: getAnnotations()

   Retrieves the brain compartments (neuropil labels) associated with the Tree being measured innervated by the analyzed neuron.


.. py:method:: getAvgBranchLength()

   Gets average length for all the branches of the analyzed tree.


.. py:method:: getAvgContraction()

   Gets average ``contraction`` for all the branches of the analyzed tree.


.. py:method:: getAvgFractalDimension()

   Gets the average fractal dimension of the analyzed tree. Note that branches with less than 5 points are ignored during the computation.


.. py:method:: getAvgFragmentation()

   Gets the average no. of nodes (fragmentation) for all the branches of the analyzed tree.


.. py:method:: getAvgPartitionAsymmetry()

   Gets the average partition asymmetry of the analyzed tree. Note that branch points with more than 2 children are ignored during the computation.


.. py:method:: getAvgRemoteBifAngle()

   Gets the average remote bifurcation angle of the analyzed tree. Note that branch points with more than 2 children are ignored during the computation.


.. py:method:: getBranchPoints()

   Gets the position of all the branch points in the analyzed tree associated with the specified annotation.


.. py:method:: getBranches()

   Gets all the branches in the analyzed tree. A branch is defined as the Path composed of all the nodes between two branching points or between one branching point and a termination point.


.. py:method:: getCableLength()

   Gets the cable length associated with the specified compartment (neuropil label).


.. py:method:: getCableLengthNorm(BrainAnnotation)

   Gets the cable length associated with the specified compartment (neuropil label) as a ratio of total length.


.. py:method:: getConvexAnalyzer()

   Gets the ``ConvexHullAnalyzer`` instance associated with this TreeStatistics instance.


.. py:method:: getConvexHullMetric(String)

   Convenience method to obtain a single-value metric from ``ConvexHullAnalyzer``


.. py:method:: getDepth()

   Returns the depth of the ``BoundingBox`` box of the tree being measured


.. py:method:: getDescriptiveStats(String)

   Computes the ``DescriptiveStatistics`` for the specified measurement.


.. py:method:: getFlowPlot(String, Collection)

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.


.. py:method:: getFractalDimension()

   Gets the fractal dimension of each branch in the analyzed tree. Note that branches with less than 5 points are ignored.


.. py:method:: getHeight()

   Returns the height of the ``BoundingBox`` box of the tree being measured


.. py:method:: getHighestPathOrder()

   Gets the highest ``path order`` of the analyzed tree


.. py:method:: getHistogram(String)

   


.. py:method:: getInnerBranches()

   Retrieves the branches of highest ``Strahler order`` in the Tree. This typically correspond to the most 'internal' branches of the Tree in direct sequence from the root.


.. py:method:: getInnerLength()

   Gets the cable length of inner branches


.. py:method:: getMetric(String)

   Computes the specified metric.


.. py:method:: getMetrics()

   Gets the list of most commonly used metrics.


.. py:method:: getNBranchPoints(BrainAnnotation)

   Gets the number of branch points in the analyzed tree associated with the specified annotation.


.. py:method:: getNBranchPointsNorm(BrainAnnotation)

   Gets the percentage of branch points in the analyzed tree associated with the specified annotation


.. py:method:: getNBranches()

   Gets the number of branches in the analyzed tree.


.. py:method:: getNNodes()

   Gets the number of nodes in the analyzed tree.


.. py:method:: getNPaths()

   Gets the no. of parsed paths.


.. py:method:: getNTips(BrainAnnotation)

   Gets the number of end points in the analyzed tree associated with the specified annotation.


.. py:method:: getNTipsNorm(BrainAnnotation)

   Gets the percentage of end points in the analyzed tree associated with the specified annotation


.. py:method:: getNoSpinesOrVaricosities()

   Gets the number of spines/varicosities that have been (manually) assigned to tree being analyzed.


.. py:method:: getNodeStatistics()

   Convenience method to initialize a ``NodeStatistics`` from a subset of the nodes of the Tree being analyzed.


.. py:method:: getParsedTree()

   Returns the set of parsed Paths.


.. py:method:: getPartitionAsymmetry()

   Gets the partition asymmetry at each bifurcation point in the analyzed tree. Note that branch points with more than 2 children are ignored.


.. py:method:: getPolarHistogram(String)

   Assembles a polar histogram for the specified metric (assumed to be an angular measurements (e.g., branch angles, path orientations).


.. py:method:: getPrimaryBranches()

   Retrieves the primary branches of the analyzed Tree. Primary branches (or root-associated) have origin in the Tree's root, extending to the closest branch/end-point. Note that a primary branch can also be terminal.


.. py:method:: getPrimaryLength()

   Gets the cable length of primary branches.


.. py:method:: getPrimaryPaths()

   Retrieves all the Paths in the analyzed Tree tagged as primary.


.. py:method:: getRemoteBifAngles()

   Gets the angle between each bifurcation point and its children in the simplified graph, which comprise either branch points or terminal nodes. Note that branch points with more than 2 children are ignored.


.. py:method:: getRootAngleAnalyzer()

   Gets the ``RootAngleAnalyzer`` instance associated with this TreeStatistics instance.


.. py:method:: getRootAngleMetric(String)

   Convenience method to obtain a single-value metric from ``RootAngleAnalyzer``.


.. py:method:: getShollAnalyzer()

   Gets the ``ShollAnalyzer`` instance associated with this TreeStatistics instance. Note that changes to ``ShollAnalyzer`` must be performed before retrieving Sholl related metrics, i.e., before calling ``measure(Collection, boolean)``, etc.


.. py:method:: getSpineOrVaricosityDensity()

   Gets the overall density of spines/varicosities associated with this tree


.. py:method:: getStrahlerAnalyzer()

   Gets the ``StrahlerAnalyzer`` instance associated with this TreeStatistics instance


.. py:method:: getStrahlerBifurcationRatio()

   Gets the average ``Strahler bifurcation ratio`` of analyzed tree.


.. py:method:: getStrahlerNumber()

   Gets the highest ``Strahler number`` of the analyzed tree.


.. py:method:: getSummaryStats(String)

   Computes the ``SummaryStatistics`` for the specified measurement.


.. py:method:: getTable()

   Gets the table currently being used by this TreeStatistics instance


.. py:method:: getTerminalBranches()

   Retrieves the terminal branches of the analyzed Tree. A terminal branch corresponds to the section of a terminal Path between its last branch-point and its terminal point (tip). A terminal branch can also be primary.


.. py:method:: getTerminalLength()

   Gets the cable length of terminal branches


.. py:method:: getTips()

   Gets the position of all tips in the analyzed tree that are within the specified distance range from the root. This method is useful for analyzing tree morphology within specific distance bands from the soma.


.. py:method:: getUnit(String)

   Returns the physical unit associated with the specified metric. This is the single source of truth for metric units: histograms, tables and color legends all rely on it.


.. py:method:: getWidth()

   Returns the width of the ``BoundingBox`` box of the tree being measured


.. py:method:: isExactMetricMatch()

   Checks if 'fuzzy matching' of metrics is disabled for this instance.


.. py:method:: isValid()

   Checks whether this tree is topologically valid, i.e., contains only one root and no loops.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setExactMetricMatch(boolean)

   Sets whether loose phrases (e.g., "# bps" or "n junctions") should be matched to the closest supported metric when retrieving metrics. By default, they are. Names that differ from a supported metric only in case, spacing or punctuation are always matched.


.. py:method:: setTable(GenericTable)

   Sets the table for this TreeStatistics instance.


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: measure(Collection, boolean)

   Measures this Tree, outputting the result to the measurements table. If a Context has been specified, the table is updated. Otherwise, table contents are printed to Console.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: updateAndDisplayTable()

   Updates and displays the measurements table. If ``Context`` has not been set (running headless!?), table is printed to Console.


Other Methods
~~~~~~~~~~~~~


.. py:method:: dispose()

   Clears internal caches and mappings to free memory.


.. py:method:: fromCollection(Collection, String)

   Creates a TreeStatistics instance from a group of Trees and a specific metric for convenient retrieval of histograms


.. py:method:: main(String[])

   


.. py:method:: restrictToSWCType(int[])

   Restricts analysis to Paths sharing the specified SWC flag(s).


.. py:method:: run()

   Generates detailed summaries in which measurements are grouped by SWC-type flags


.. py:method:: summarize(boolean)

   Outputs a summary of the current analysis to the measurements table.


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.TreeStatistics>`_
* `TreeStatistics JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/TreeStatistics.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
