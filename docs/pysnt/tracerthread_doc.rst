
``TracerThread`` Class Documentation
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

SNT's default tracer thread: explores between two points in an image, doing an A* search with a choice of distance measures.


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


.. py:method:: getExitReason()

   


.. py:method:: getNodesAsImageFromGoal()

   


.. py:method:: getNodesAsImageFromStart()

   


.. py:method:: getResult()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addNode(DefaultSearchNode, boolean)

   


.. py:method:: addProgressListener(SearchProgressCallback)

   


.. py:method:: createNewNode(int, int, int, double, double, DefaultSearchNode, byte)

   


.. py:method:: pointsConsideredInSearch()

   


.. py:method:: printStatus()

   


.. py:method:: reportFinished(boolean)

   


.. py:method:: run()

   


See Also
--------

* `Package API <../api_auto/pysnt.tracing.html#pysnt.tracing.TracerThread>`_
* `TracerThread JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/TracerThread.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
