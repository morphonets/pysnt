
``ShollTable`` Class Documentation
===============================


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


**Package:** ``sc.fiji.snt.analysis.sholl.gui``

Enhanced documentation for ShollTable class.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clear()

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getColumnHeaders()

   


.. py:method:: getSummaryRow()

   


.. py:method:: getTitle()

   


.. py:method:: hasContext()

   


.. py:method:: hasUnsavedData()

   


.. py:method:: isSummarized()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: set(String, String, Object)

   


.. py:method:: setContext(Context)

   


.. py:method:: setDetailedSummary(boolean)

   


.. py:method:: setTitle(String)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: createOrUpdateDisplay()

   


.. py:method:: show()

   


.. py:method:: updateDisplay()

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: fromFile(String)

   


.. py:method:: save(File)

   


.. py:method:: saveSilently(File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addColumn(String, Collection)

   


.. py:method:: addGenericColumn(String, Collection)

   


.. py:method:: appendToLastRow(String, Object)

   


.. py:method:: asDouble(Object)

   


.. py:method:: asInt(Object, int)

   


.. py:method:: asString(Object, String)

   


.. py:method:: fillEmptyCells(Object)

   


.. py:method:: findColumnIndex(String)

   


.. py:method:: fromGenericTable(GenericTable)

   


.. py:method:: geColumnStats(String, int, int)

   


.. py:method:: geRowStats(String, int, int)

   


.. py:method:: insertRow(String)

   


.. py:method:: listProfileEntries()

   


.. py:method:: removeColumn(String)

   


.. py:method:: removeSummary()

   


.. py:method:: replace(String, double, double)

   


.. py:method:: summarize()

   


.. py:method:: toString(GenericTable)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.sholl.gui.html#pysnt.analysis.sholl.gui.ShollTable>`_
* `ShollTable JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/gui/ShollTable.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
