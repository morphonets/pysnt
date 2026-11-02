
``SeedOverlay`` Class Documentation
================================


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


**Package:** ``sc.fiji.snt.seed``

Enhanced documentation for SeedOverlay class.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clear()

   


.. py:method:: clearSelection()

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: get(int)

   


.. py:method:: getColorMode()

   


.. py:method:: getColorTable()

   


.. py:method:: getColorTableName()

   


.. py:method:: getHighConfidence()

   


.. py:method:: getLowConfidence()

   


.. py:method:: getSelectedSeeds()

   


.. py:method:: getTransparency()

   


.. py:method:: getUnknownConfidenceColor()

   


.. py:method:: isEmpty()

   


.. py:method:: isSelected(SeedPoint)

   


.. py:method:: isVisible()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setColorMode(ColorMode)

   


.. py:method:: setColorTable(String)

   


.. py:method:: setConfidenceRange(double, double)

   


.. py:method:: setSelectedSeeds(Collection)

   


.. py:method:: setTransparency(double)

   


.. py:method:: setUnknownConfidenceColor(Color)

   


.. py:method:: setVisible(boolean)

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: loadCsv(File, boolean)

   


.. py:method:: saveAs(File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(SeedPoint)

   


.. py:method:: addAll(Collection)

   


.. py:method:: addListener(SeedOverlayListener)

   


.. py:method:: countOutOfBounds(long[], double[], double[])

   


.. py:method:: filtered()

   


.. py:method:: indexOf(SeedPoint)

   


.. py:method:: list()

   


.. py:method:: nearest(double, double, double, double)

   


.. py:method:: parseCsv(File)

   


.. py:method:: remove(SeedPoint)

   


.. py:method:: removeAll(Collection)

   


.. py:method:: removeAt(int)

   


.. py:method:: removeListener(SeedOverlayListener)

   


.. py:method:: removeSelected()

   


.. py:method:: replaceAll(Collection)

   


.. py:method:: replaceAllAt(Map)

   


.. py:method:: replaceAt(int, SeedPoint)

   


.. py:method:: scaleConfidence(Collection, double)

   


.. py:method:: scaleRadius(Collection, double)

   


.. py:method:: size()

   


.. py:method:: topKByConfidence(int)

   


.. py:method:: visibleSize()

   


See Also
--------

* `Package API <../api_auto/pysnt.seed.html#pysnt.seed.SeedOverlay>`_
* `SeedOverlay JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/seed/SeedOverlay.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
