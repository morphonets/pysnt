
``FillConverter`` Class Documentation
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


**Package:** ``sc.fiji.snt``

Map filled nodes from a Collection of FillerThreads to and between RandomAccessibles.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getFillerStack()

   Merges the input FillerThreads into a single SearchImageStack. When a filled voxel position is present in multiple filler instances, the node with the lowest g-score is chosen for inclusion in the merged stack.


Other Methods
~~~~~~~~~~~~~


.. py:method:: convert(RandomAccessible, RandomAccessible)

   Map values between the input and output at fill voxel positions.


.. py:method:: convertBinary(RandomAccessible)

   Set 1 at fill voxel positions.


.. py:method:: convertDistance(RandomAccessible)

   Map the node distance measure to fill voxel positions. This corresponds to the g-score of a node assigned during the Dijkstra search. This value is stored as Double.


.. py:method:: convertLabels(RandomAccessible)

   Map the fill component label to fill voxel positions. The concrete IntegerType should be chosen based on the cardinality of the given Collection of FillerThreads. For example, if there are less than 256 FillerThreads, choose UnsignedByteType. If there are more than 255 but less than 65536, choose UnsignedShortType, etc. Fill components are assigned labels based on their order in the collection. If you want to ensure labels are assigned based on insertion order, make sure to use an ordered collection such as List or LinkedHashSet. The first component will have label == 1, the second label == 2, and so on. The label 0 is not assigned to any voxel positions. 0-valued voxels may already exist in the output image.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.FillConverter>`_
* `FillConverter JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/FillConverter.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
