
``SNTChart`` Class Documentation
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


**Package:** ``sc.fiji.snt.analysis``

Extension of ChartPanel modified for scientific publications and convenience methods for plot annotations.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: checkImage(Image, ImageObserver)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: action(Event, Object)

   


.. py:method:: actionPerformed(ActionEvent)

   Shows a bivariate histogram (two-dimensional histogram) from two DescriptiveStatistics objects. The number of bins is automatically determined using the Freedman-Diaconis rule.


.. py:method:: add(String, Component)

   


.. py:method:: addAncestorListener(AncestorListener)

   


.. py:method:: addChartMouseListener(ChartMouseListener)

   


.. py:method:: addColorBarLegend(String, ColorTable, double, double, int)

   Adds a color bar legend (LUT ramp).


.. py:method:: addComponentListener(ComponentListener)

   


.. py:method:: addContainerListener(ContainerListener)

   


.. py:method:: addFocusListener(FocusListener)

   


.. py:method:: addHierarchyBoundsListener(HierarchyBoundsListener)

   


.. py:method:: addHierarchyListener(HierarchyListener)

   


.. py:method:: addInputMethodListener(InputMethodListener)

   


.. py:method:: addKeyListener(KeyListener)

   


.. py:method:: addMouseListener(MouseListener)

   


.. py:method:: addMouseMotionListener(MouseMotionListener)

   


.. py:method:: addMouseWheelListener(MouseWheelListener)

   


.. py:method:: addNotify()

   


.. py:method:: addOverlay(Overlay)

   


.. py:method:: addPolygon(Polygon2D, String, String)

   


.. py:method:: addPropertyChangeListener(String, PropertyChangeListener)

   


.. py:method:: addVetoableChangeListener(VetoableChangeListener)

   


.. py:method:: annotate(String)

   Adds a subtitle to the chart.


.. py:method:: annotateCategory(String, String, String)

   Annotates the specified category (Category plots only).


.. py:method:: annotatePoint([D, String, String)

   Highlights a point in a histogram/XY plot by drawing a labeled arrow at the specified location.


.. py:method:: annotateXline(double, String, String)

   Annotates the specified X-value (XY plots and histograms).


.. py:method:: annotateYline(double, String)

   Annotates the specified Y-value (XY plots and histograms).


.. py:method:: applyComponentOrientation(ComponentOrientation)

   


.. py:method:: applyStyle(SNTChart)

   


.. py:method:: areFocusTraversalKeysSet(int)

   Saves this chart.


.. py:method:: bounds()

   


.. py:method:: chartChanged(ChartChangeEvent)

   


.. py:method:: chartProgress(ChartProgressEvent)

   


.. py:method:: static closeAll()

   Closes all open charts


.. py:method:: static combine(Collection, int, int, boolean)

   Combines a collection of charts into a multipanel montage.


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.SNTChart>`_
* `SNTChart JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SNTChart.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
