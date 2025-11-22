
``MultiViewer2D`` Class Documentation
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


**Package:** ``sc.fiji.snt.viewer``

Class for rendering montages of Trees as 2D plots that can be exported as SVG, PNG or PDF.


Methods
-------


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAxesVisible(boolean)

   


.. py:method:: setColorBarLegend(String, double, double)

   


.. py:method:: setGridlinesVisible(boolean)

   


.. py:method:: setLabel(String)

   


.. py:method:: setLayoutColumns(int)

   


.. py:method:: setOutlineVisible(boolean)

   


.. py:method:: setTitle(String)

   Sets the title of this Viewer's frame.


.. py:method:: setXrange(double, double)

   Sets a manual range for the viewers' X-axis. Calling setXrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.


.. py:method:: setYrange(double, double)

   Sets a manual range for the viewers' Y-axis. Calling setYrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: show()

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: save(String)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.MultiViewer2D>`_
* `MultiViewer2D JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/MultiViewer2D.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
