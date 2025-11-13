
``SNTUtils`` Class Documentation
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


**Package:** ``sc.fiji.snt``

Static utilities for SNT


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getBackupCopies(File)

   Retrieves a list of time-stamped backup files associated with a TRACES file


.. py:method:: static getContext()

   Convenience method to access the context of the running Fiji instance


.. py:method:: static getDecimalFormat(double, int)

   


.. py:method:: static getElapsedTime(long)

   


.. py:method:: static getInstance()

   


.. py:method:: static getPluginInstance()

   


.. py:method:: static getReadableVersion()

   


.. py:method:: static getReconstructionFiles(File, String)

   Retrieves a list of reconstruction files stored in a common directory matching the specified criteria.


.. py:method:: static getSanitizedUnit(String)

   


.. py:method:: static getTimeStamp()

   


.. py:method:: static getUniquelySuffixedFile(File)

   


.. py:method:: static getUniquelySuffixedTifFile(File)

   


.. py:method:: static isContextSet()

   


.. py:method:: static isDebugMode()

   Assesses if SNT is running in debug mode


.. py:method:: static isReconstructionFile(File)

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: static setContext(Context)

   


.. py:method:: static setDebugMode(boolean)

   Enables/disables debug mode


.. py:method:: static setIsLoading(boolean)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static addViewer(Viewer3D)

   


.. py:method:: static removeViewer(Viewer3D)

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static downloadToTempFile(String)

   Downloads a file from the specified URL to a temporary file


Other Methods
~~~~~~~~~~~~~


.. py:method:: static buildDate()

   Retrieves Sholl Analysis implementation date


.. py:method:: static csvQuoteAndPrint(PrintWriter, Object)

   


.. py:method:: static error(String, Throwable)

   


.. py:method:: static extractReadableTimeStamp(File)

   


.. py:method:: static fileAvailable(File)

   


.. py:method:: static findClosestPair(File, String;)

   


.. py:method:: static formatDouble(double, int)

   


.. py:method:: static log(String)

   


.. py:method:: static randomPaths()

   Generates a list of random paths. Only useful for debugging purposes


.. py:method:: static startApp()

   Convenience method to start up SNT's GUI.


.. py:method:: static stripExtension(String)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNTUtils>`_
* `SNTUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
