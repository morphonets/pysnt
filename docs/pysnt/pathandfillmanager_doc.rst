
``PathAndFillManager`` Class Documentation
=======================================


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

The PathAndFillManager is responsible for importing, handling and managing of Paths and Fills. Typically, a PathAndFillManager is accessed from a SNT instance, but accessing a PathAndFillManager directly is useful for batch/headless operations.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clear()

   Deletes all paths and fills.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBoundingBox(boolean)

   Returns the BoundingBox enclosing all nodes of all existing Paths.


.. py:method:: getCorrespondences(PathAndFillManager, double)

   For each point in this PathAndFillManager, find the corresponding point on the other one. If there's no corresponding one, include a null instead. *


.. py:method:: getLoadedFills()

   


.. py:method:: getPath(int)

   Returns the Path at the specified position in the PathAndFillManager list.


.. py:method:: getPathFromID(int)

   Returns the Path with the specified id.


.. py:method:: getPathFromName(String, boolean)

   Returns the Path with the specified name.


.. py:method:: getPaths()

   Returns all the paths.


.. py:method:: getPathsFiltered()

   Returns the 'de facto' Paths.


.. py:method:: getPathsInROI(Roi)

   


.. py:method:: getPathsStructured()

   


.. py:method:: getPlugin()

   Gets the SNT instance.


.. py:method:: getSWCFor(Collection)

   Converts a collection of connected Path objects into SWC points for export.

SWC is the standardized format used for neuromorphological data exchange. The conversion process:

Validates that paths form a proper tree structure with exactly one primary path (tree's root) Uses breadth-first traversal to ensure correct parent-child relationships Assigns sequential SWC IDs starting from 1 Establishes proper parent references based on path connectivity Preserves path properties including SWC type, color, annotations, and custom tags

Path Requirements:

Must contain exactly one primary path (root of the tree) All non-primary paths must have valid parent relationships Paths must form a connected tree structure (no disconnected components) Empty paths (size == 0) are automatically skipped


.. py:method:: getSelectedPaths()

   Gets all paths selected in the GUI


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static createFromFile(String, [I)

   Creates a PathAndFillManager instance from imported data


.. py:method:: exportAllPathsAsSWC(String)

   Exports all as Paths as SWC file(s). Multiple files are created if multiple Trees exist.


.. py:method:: exportFillsAsCSV(File)

   Export fills as CSV.


.. py:method:: exportToCSV(File)

   Output some potentially useful information about all the Paths managed by this instance as a CSV (comma separated values) file.


.. py:method:: exportTree(int, File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addPath(Path, int, int)

   


.. py:method:: addPathAndFillListener(PathAndFillListener)

   Adds a PathAndFillListener. This is used by the interface to have changes in the path manager reported so that they can be reflected in the UI.


.. py:method:: addTree(Tree, String)

   Adds a Tree. If an image is currently being traced, it is assumed it is large enough to contain the tree.


.. py:method:: addTrees(Collection)

   Adds a collection of Trees.


.. py:method:: allPointsIterator()

   


.. py:method:: anySelected()

   Checks whether at least one Path is currently selected in the UI.


.. py:method:: assignSpatialSettings(ImagePlus)

   


.. py:method:: canvasResized()

   


.. py:method:: characters([C, int, int)

   


.. py:method:: contentAdded(Content)

   


.. py:method:: contentChanged(Content)

   


.. py:method:: contentRemoved(Content)

   


.. py:method:: contentSelected(Content)

   


.. py:method:: static createFromGraph(DirectedWeightedGraph, boolean)

   Create a new PathAndFillManager instance from the graph.


.. py:method:: static createFromNodes(Collection)

   Creates a PathAndFillManager instance from a collection of reconstruction nodes.


.. py:method:: declaration(String, String, String)

   


.. py:method:: deletePath(int)

   Deletes a path.


.. py:method:: deletePaths(Collection)

   Delete paths by position.


.. py:method:: dispose()

   


.. py:method:: downsampleAll(double)

   Downsamples alls path using Ramer–Douglas–Peucker simplification. Downsampling occurs only between branch points and terminal points.


.. py:method:: endDocument()

   


.. py:method:: endElement(String, String, String)

   


.. py:method:: endPrefixMapping(String)

   Sets whether this PathAndFillManager instance should run headless.


.. py:method:: error(SAXParseException)

   


.. py:method:: fatalError(SAXParseException)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.PathAndFillManager>`_
* `PathAndFillManager JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathAndFillManager.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
