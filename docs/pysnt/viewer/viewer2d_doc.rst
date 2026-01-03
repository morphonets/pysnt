
``Viewer2D`` Class Documentation
=============================


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


**Package:** ``sc.fiji.snt.viewer``

Class for rendering Trees as 2D plots that can be exported as SVG, PNG or PDF.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAvailableLuts()

   


.. py:method:: getChart()

   Gets the current viewer as a SNTChart object


.. py:method:: getColor(double)

   


.. py:method:: getColorRGB(double)

   


.. py:method:: getColorTable(String)

   


.. py:method:: getJFreeChart()

   Gets the current viewer as a JFreeChart object


.. py:method:: static getMetrics()

   


.. py:method:: getMinMax()

   


.. py:method:: getMultiViewer()

   


.. py:method:: getNaNColor()

   


.. py:method:: getPlot()

   Gets the current plot as a XYPlot object


.. py:method:: getTitle()

   Gets the plot display title.


.. py:method:: isIntegerScale()

   


.. py:method:: isNodeMapping()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAxesVisible(boolean)

   


.. py:method:: setDefaultColor(ColorRGB)

   Sets the default (fallback) color for plotting paths.


.. py:method:: setEqualizeAxes(boolean)

   /** Sets whether the axes should be equalized (same scale).

When enabled, both X and Y axes will use the same scale to maintain equal aspect ratio. When disabled, each axis maximizes its range.


.. py:method:: setGridlinesVisible(boolean)

   


.. py:method:: setMinMax(double, double)

   


.. py:method:: setNaNColor(Color)

   


.. py:method:: setOutlineVisible(boolean)

   


.. py:method:: setPreferredSize(int, int)

   Sets the preferred size of the plot to a constant value.


.. py:method:: setTitle(String)

   Sets the plot display title.


.. py:method:: setXrange(double, double)

   Sets a manual range for the viewers' X-axis. Calling setXrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.


.. py:method:: setYrange(double, double)

   Sets a manual range for the viewers' Y-axis. Calling setYrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: show()

   Displays the current plot on a dedicated frame *


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(Object)

   Appends a tree to the viewer rendered after the specified measurement.


.. py:method:: addColorBarLegend(ColorTable, double, double)

   Adds a color bar legend (LUT ramp) to the viewer. Does nothing if no measurement mapping occurred successfully. Note that when performing mapping to different measurements, the legend reflects only the last mapped measurement.


.. py:method:: addNodes(Map)

   


.. py:method:: addPolygon(Polygon2D, String)

   


.. py:method:: addTree(Tree)

   Appends a tree to the viewer using default options.


.. py:method:: addTrees(Collection)

   Adds a collection of trees. Each tree will be rendered using a unique color.


.. py:method:: static main(String;)

   


.. py:method:: map(Tree, String, String)

   


.. py:method:: mapTrees(List, String)

   


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.Viewer2D>`_
* `Viewer2D JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Viewer2D.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
