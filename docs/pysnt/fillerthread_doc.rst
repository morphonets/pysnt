
``FillerThread`` Class Documentation
=================================


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


**Package:** ``sc.fiji.snt.tracing``

Seeded-volume segmentation via single-source shortest paths. Path nodes are used as seed points in an open-ended variant of Dijkstra's algorithm. The threshold sets the maximum allowable distance for a node to be included in the Fill. This distance is represented in the g-score of a node, which is the length of the shortest path from a seed point to that node. The magnitudes of these distances are heavily dependent on the supplied cost function Cost, so the threshold should be set with a particular cost function in mind. It often helps to adjust the threshold interactively.


Fields
------


**imgDepth** : ``int``
    No description available.


**imgHeight** : ``int``
    No description available.


**imgWidth** : ``int``
    No description available.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getDistanceAtPoint(double, double, double)

   


.. py:method:: getExitReason()

   


.. py:method:: getFill()

   


.. py:method:: getNodesAsImage()

   


.. py:method:: getNodesAsImageFromGoal()

   


.. py:method:: getNodesAsImageFromStart()

   


.. py:method:: getResult()

   


.. py:method:: getThreshold()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setSourcePaths(Collection)

   


.. py:method:: setStopAtThreshold(boolean)

   Whether to terminate the fill operation once all nodes less than or equal to the distance threshold have been explored. If false, the search will run until it has explored the entire image. The default is false.


.. py:method:: setStoreExtraNodes(boolean)

   Whether to store above-threshold nodes in the Fill object. The default is true.


.. py:method:: setThreshold(double)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addNode(DefaultSearchNode, boolean)

   


.. py:method:: addProgressListener(SearchProgressCallback)

   


.. py:method:: createNewNode(int, int, int, double, double, DefaultSearchNode, byte)

   


.. py:method:: static fromFill(ImagePlus, ImageStatistics, Fill)

   


.. py:method:: pointsConsideredInSearch()

   


.. py:method:: printStatus()

   


.. py:method:: reportFinished(boolean)

   


.. py:method:: run()

   


See Also
--------

* `Package API <../api_auto/pysnt.tracing.html#pysnt.tracing.FillerThread>`_
* `FillerThread JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/FillerThread.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
