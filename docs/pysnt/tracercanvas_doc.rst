
``TracerCanvas`` Class Documentation
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


**Package:** ``sc.fiji.snt``

Provides rendering capabilities for visualizing paths, overlays, and additional interactive elements in an ImageJ canvas.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnnotationsColor()

   


.. py:method:: getCanvasLabel()

   


.. py:method:: getCursorPos()

   


.. py:method:: getEitherSide()

   


.. py:method:: getGraphics2D(Graphics)

   


.. py:method:: getLabelForegroundColor()

   


.. py:method:: getPlane()

   Returns the MultiDThreePanes plane associated with this canvas.


.. py:method:: getViewPort()

   


.. py:method:: isEventsDisabled()

   


.. py:method:: isJustNearSlices()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAnnotationsColor(Color)

   


.. py:method:: setCanvasLabel(String)

   


.. py:method:: setCrosshairs(double, double, double, boolean)

   


.. py:method:: setCursorText(String)

   


.. py:method:: setDrawCrosshairs(boolean)

   


.. py:method:: setLabelForegroundColor(Color)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: disableEvents(boolean)

   Sets the baseline for rendering diameter of path nodes


.. py:method:: mouseDragged(MouseEvent)

   


.. py:method:: myOffScreenX(int)

   


.. py:method:: myOffScreenXD(int)

   


.. py:method:: myOffScreenY(int)

   


.. py:method:: myOffScreenYD(int)

   


.. py:method:: myScreenX(int)

   


.. py:method:: myScreenXD(double)

   


.. py:method:: myScreenXDprecise(double)

   


.. py:method:: myScreenY(int)

   


.. py:method:: myScreenYD(double)

   


.. py:method:: myScreenYDprecise(double)

   


.. py:method:: paint(Graphics)

   


.. py:method:: restoreDefaultCursor()

   


.. py:method:: scrollTo(int, int)

   


.. py:method:: updateCursor(double, double, double)

   


.. py:method:: updatePosition(double, double, double)

   


.. py:method:: zoomIn(int, int)

   


.. py:method:: zoomOut(int, int)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.TracerCanvas>`_
* `TracerCanvas JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/TracerCanvas.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
