
``SNTTable`` Class Documentation
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

Extension of DefaultGenericTable with (minor) scripting conveniences.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clear()

   


.. py:method:: clone()

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: get(int)

   


.. py:method:: getColumnCount()

   


.. py:method:: getColumnHeader(int)

   


.. py:method:: getColumnIndex(String)

   


.. py:method:: getFirst()

   


.. py:method:: getLast()

   


.. py:method:: getRowCount()

   


.. py:method:: getRowHeader(int)

   


.. py:method:: getRowIndex(String)

   


.. py:method:: getSummaryRow()

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: createOrUpdateDisplay()

   Creates a new display or updates an existing one.

If no display exists, creates a new table display window. If a display already exists, updates it with the current table contents.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static fromFile(String, String)

   Script-friendly method for loading tabular data from a file/URL.


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(int, Object)

   


.. py:method:: addAll(Collection)

   


.. py:method:: addColumn(String, [D)

   


.. py:method:: addFirst(Object)

   Sets a SciJava context to this table.


.. py:method:: addGenericColumn(String, Collection)

   


.. py:method:: addLast(Object)

   


.. py:method:: appendColumn()

   


.. py:method:: appendColumns(String;)

   


.. py:method:: appendRow(String)

   


.. py:method:: appendRows(String;)

   


.. py:method:: appendToLastRow(String, Object)

   Appends a value to the last row in the specified column.

If the table is empty, a new row is created first. The value is then set in the specified column of the last row.


.. py:method:: contains(Object)

   


.. py:method:: containsAll(Collection)

   


.. py:method:: ensureCapacity(int)

   


.. py:method:: fillEmptyCells(Object)

   Fills all empty cells in the table with the specified value.

Iterates through all cells in the table and replaces null values with the provided replacement value.


.. py:method:: forEach(Consumer)

   


.. py:method:: geColumnHeaders(String)

   


.. py:method:: geColumnStats(int, int, int)

   


.. py:method:: geRowStats(String, int, int)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.SNTTable>`_
* `SNTTable JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SNTTable.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
