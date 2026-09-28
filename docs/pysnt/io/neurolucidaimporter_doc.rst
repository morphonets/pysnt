
``NeurolucidaImporter`` Class Documentation
========================================


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


**Package:** ``sc.fiji.snt.io``

Importer for Neurolucida XML files (Neuromorphological File Specification / NMF format). Parses <tree> elements into SNT Path/Tree objects and <marker> elements into bookmark data (centroid coordinates). Contours and vessels are skipped in this implementation.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCalibration()

   Returns the spatial calibration parsed from the file header.


.. py:method:: getMarkerColors()

   Returns the colors for each parsed marker, in the same order as getMarkerPoints().


.. py:method:: getMarkerLabels()

   Returns the labels for each parsed marker, in the same order as getMarkerPoints().


.. py:method:: getMarkerPoints()

   Returns the marker centroids parsed from <marker> elements. Each entry is a double[3] array of {x, y, z} coordinates in the file's coordinate system (typically micrometers).


.. py:method:: getSpacingUnits()

   Returns the spacing units string (default "um").


.. py:method:: getTrees()

   Returns the parsed trees (one per <tree> element in the file).


.. py:method:: static isNeurolucidaXML(InputStream)

   Checks whether the given input stream starts with Neurolucida XML content. The stream must support `InputStream.mark(int)`.


See Also
--------

* `Package API <../api_auto/pysnt.io.html#pysnt.io.NeurolucidaImporter>`_
* `NeurolucidaImporter JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/NeurolucidaImporter.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
