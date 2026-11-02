
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

Extension of ``DefaultGenericTable`` with (minor) scripting conveniences.


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

   Gets the title of the table.

   Returns the table's title, or "SNT Measurements" if no title has been set.


.. py:method:: hasUnsavedData()

   Checks if the table has unsaved data.

   Returns true if the table contains data and has been modified since the last save operation.


.. py:method:: isSummarized()

   Checks if the table contains summary statistics.

   Returns true if the table has been summarized with statistical measures like mean, standard deviation, etc. This is determined by looking for specific row headers in the expected positions.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: set(String, String, Object)

   


.. py:method:: setContext(Context)

   Sets a SciJava context to this table.


.. py:method:: setTitle(String)

   Sets the title of the table.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: createOrUpdateDisplay()

   Creates a new display or updates an existing one.

   If no display exists, creates a new table display window. If a display already exists, updates it with the current table contents.


.. py:method:: show()

   


.. py:method:: updateDisplay()

   Updates the existing table display.

   Refreshes the table display with the current table contents without creating a new display window.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: fromFile(String)

   Script-friendly method for loading tabular data from a file/URL.


.. py:method:: save(File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addColumn(String, Collection)

   


.. py:method:: addGenericColumn(String, Collection)

   


.. py:method:: appendToLastRow(String, Object)

   Appends a value to the last row in the specified column.

   If the table is empty, a new row is created first. The value is then set in the specified column of the last row.


.. py:method:: asDouble(Object)

   Coerces a table cell to a ``double``. Cells may be typed ``Double``, ``Long``, or ``String`` depending on how the table was parsed (e.g. CSV column-type inference); this accepts any of those, with a String parse fallback for a numeric-looking value stored in a non-numeric column


.. py:method:: asInt(Object, int)

   Coerces a table cell to an ``int``. Tolerates a Double-shaped integer string (e.g. ``"1.0"`` -> ``1``)


.. py:method:: asString(Object, String)

   Coerces a table cell to a trimmed ``String``


.. py:method:: fillEmptyCells(Object)

   Fills all empty cells in the table with the specified value.

   Iterates through all cells in the table and replaces null values with the provided replacement value.


.. py:method:: findColumnIndex(String)

   Case-/whitespace-insensitive column lookup.


.. py:method:: fromGenericTable(GenericTable)

   


.. py:method:: geColumnStats(String, int, int)

   


.. py:method:: geRowStats(String, int, int)

   


.. py:method:: insertRow(String)

   


.. py:method:: removeColumn(String)

   


.. py:method:: removeSummary()

   Removes summary statistics from the table.

   If the table contains summary statistics, this method removes the summary rows to return the table to its raw data state.


.. py:method:: replace(String, double, double)

   


.. py:method:: summarize()

   


.. py:method:: toString(GenericTable)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.SNTTable>`_
* `SNTTable JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SNTTable.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
