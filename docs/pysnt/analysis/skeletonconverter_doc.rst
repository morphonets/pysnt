
``SkeletonConverter`` Class Documentation
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

Class for generation of Trees from a skeletonized ImagePlus.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getGraphs()

   Generates a list of `DirectedWeightedGraph`s from the skeleton image. Each graph corresponds to one connected component of the graph returned by `SkeletonResult.getGraph()`.


.. py:method:: getPruneMode()

   Gets the loop pruning strategy.


.. py:method:: getRootRoiStrategy()

   Gets the current root ROI strategy.

Returns the strategy used for handling root ROIs during skeleton conversion. If no root ROI is set, returns ROI_UNSET.


.. py:method:: getSingleGraph()

   Generates a single `DirectedWeightedGraph`s by combining getGraphs()'s list into a single, combined graph. Typically, this method assumes that the skeletonization handles a known single component (e.g., an image of a single cell). If multiple graphs() do exist, this method requires that setRootRoi(Roi, int) has been called using ROI_CENTROID or `ROI_CENTROID_WEIGHTED`.


.. py:method:: getSingleTree()

   Generates a single Tree from getSingleGraph(). If a ROI-based centroid has been set, Root is converted to a single node, root path with radius set to that of a circle with the same area of root-defining soma.


.. py:method:: getTrees()

   Generates a list of Trees from the skeleton image. Each Tree corresponds to one connected component of the graph returned by `SkeletonResult.getGraph()`.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setConnectComponents(boolean)

   Sets whether to connect nearby skeleton components.

Controls whether disconnected skeleton components should be connected if they are within the maximum connection distance.


.. py:method:: setLengthThreshold(double)

   Sets the minimum component length necessary to avoid pruning. This value is only used if pruneByLength is true.

Specifies the minimum length below which skeleton components will be pruned from the result. Negative values are set to 0.


.. py:method:: setMaxConnectDist(double)

   Sets the maximum distance for connecting skeleton components.

Specifies the maximum distance within which disconnected skeleton components will be connected. Values ≤ 0 are set to Double.MIN_VALUE.


.. py:method:: setOrigIP(ImagePlus)

   Sets the original ImagePlus to be used during voxel-based loop pruning. See AnalyzeSkeleton documentation

Specifies the original (non-skeletonized) image to be used during skeleton analysis for additional processing options.


.. py:method:: setPruneByLength(boolean)

   Sets whether to prune components below a threshold length from the result.


.. py:method:: setPruneEnds(boolean)

   Sets whether to prune end branches during skeleton analysis.

Controls whether terminal branches should be pruned during the skeleton analysis process.


.. py:method:: setPruneMode(int)

   Sets the loop pruning strategy. See AnalyzeSkeleton documentation


.. py:method:: setRootRoi(Roi, int)

   Sets the Roi enclosing the nodes to be set as root(s) in the final graphs. Must be called before retrieval of any converted data.


.. py:method:: setShortestPath(boolean)

   Sets whether to calculate the longest shortest-path in the skeleton result.


.. py:method:: setSilent(boolean)

   Sets whether to run skeleton analysis in silent mode.

Setting this to false will display both the tagged skeleton image and the shortest path image (if the shortest path calculation is enabled).


.. py:method:: setVerbose(boolean)

   Sets whether to run skeleton analysis in verbose mode.

Controls whether the skeleton analysis should provide detailed output messages during processing.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static main(String;)

   


.. py:method:: static skeletonize(ImagePlus, double, double, boolean)

   Convenience method to skeletonize a thresholded image using Skeletonize3D_.


.. py:method:: static skeletonizeTimeLapse(ImagePlus, boolean)

   Convenience method to skeletonize a thresholded time-lapse using Skeletonize3D_.


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.SkeletonConverter>`_
* `SkeletonConverter JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SkeletonConverter.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
