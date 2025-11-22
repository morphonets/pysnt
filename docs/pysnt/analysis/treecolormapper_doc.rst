
``TreeColorMapper`` Class Documentation
====================================


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

Class for color coding Trees.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAvailableLuts()

   Gets the available LUTs.


.. py:method:: getColor(double)

   


.. py:method:: getColorRGB(double)

   


.. py:method:: getColorTable(String)

   


.. py:method:: static getMetrics()

   Gets the list of supported mapping metrics.


.. py:method:: getMinMax()

   


.. py:method:: getMultiViewer()

   Assembles a Multi-pane viewer using all the Trees mapped so far.


.. py:method:: getNaNColor()

   


.. py:method:: isIntegerScale()

   


.. py:method:: isNodeMapping()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setMinMax(double, double)

   


.. py:method:: setNaNColor(Color)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: static main(String;)

   


.. py:method:: map(Tree, LinearProfileStats, ColorTable)

   Colorizes a tree after the specified measurement. Mapping bounds are automatically determined.


.. py:method:: mapTrees(List, String)

   Colorizes a list of trees, with each tree being assigned a LUT index.


.. py:method:: static unMap(Tree)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.TreeColorMapper>`_
* `TreeColorMapper JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/TreeColorMapper.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
