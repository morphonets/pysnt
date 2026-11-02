
``IOUtils`` Class Documentation
============================


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


**Package:** ``sc.fiji.snt.util``

Static utilities for file I/O, namely the detection of reconstruction file formats.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getReconstructionExtensions()

   Returns the extensions (lower case, without the leading period) of the supported reconstruction formats that can be identified by name alone, i.e., not including Neurolucida .xml files


.. py:method:: isReconstructionFile(File)

   Checks if a file is a reconstruction file. Apart from the extension-only check, XML files are recognized as Neurolucida reconstructions if ``sniffXml`` is true and their header is that of a Neurolucida file. Only the first few KB of XML files are read.


.. py:method:: isSWCFile(File)

   Checks if a file has an SWC extension, i.e., .swc or .eswc (extended SWC, which holds extra columns that are ignored on import). Case-insensitive.


Other Methods
~~~~~~~~~~~~~


.. py:method:: detectFormat(File)

   Guesses the format of a reconstruction file from its first bytes. See ``detectFormat(InputStream, boolean)``


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.IOUtils>`_
* `IOUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/IOUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
