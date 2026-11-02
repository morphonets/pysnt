
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

The PathAndFillManager is responsible for importing, handling and managing of Paths and Fills. Typically, a PathAndFillManager is accessed from a ``SNT`` instance, but accessing a PathAndFillManager directly is useful for batch/headless operations.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clear()

   Deletes all paths and fills.


.. py:method:: resetListeners(Path)

   


.. py:method:: validateImageDimensions()

   Publicly triggers the same "does the loaded image accommodate these nodes" check that ``load(java.io.InputStream)`` and ``addTrees(java.util.Collection<sc.fiji.snt.Tree>, java.lang.String)`` perform automatically. Useful for callers (e.g. stream-mode importers) that add `Tree`s one at a time via ``addTree(Tree, String)``, which intentionally skips this check since it assumes a currently-traced image is large enough to contain the tree


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBoundingBox(boolean)

   Returns the BoundingBox enclosing all nodes of all existing Paths.


.. py:method:: getCorrespondences(PathAndFillManager, double)

   For each point in this PathAndFillManager, find the corresponding point on the other one. If there's no corresponding one, include a null instead. *


.. py:method:: getLoadedFills()

   


.. py:method:: getOrphanedFittedPaths()

   Returns the "orphaned" fitted paths currently registered with this manager: fitted-version paths (``Path.isFittedVersionOfAnotherPath()``) whose un-fitted original was never registered here (see ``isDeFactoPath(Path)``). Their pre-fit geometry no longer exists in this session, and saving them (see ``writeXML(java.lang.String, boolean)``) writes a ``fittedversionof`` reference to a path ID that is not present in the saved file.


.. py:method:: getPath(int)

   Returns the Path at the specified position in the PathAndFillManager list.


.. py:method:: getPathFromID(int)

   Returns the Path with the specified id.


.. py:method:: getPathFromName(String, boolean)

   Returns the Path with the specified name.


.. py:method:: getPaths()

   Returns the "main" paths managed by this PathAndFillManager. This is a convenience method that excludes:

   - Null entries (defensive filtering)

   - Fitted paths (i.e., paths that are refined versions of other paths, created by path-fitting algorithms). These are typically displayed alongside their parent path rather than as standalone entries.

   The returned list is a snapshot safe for iteration even if paths are concurrently added or removed.


.. py:method:: getPathsFiltered()

   Returns the 'de facto' Paths (excluding null or fitted versions). he returned list is a snapshot safe for iteration even if paths are concurrently added or removed.

   A fitted-version path is only excluded when its un-fitted counterpart is also registered with this manager, i.e., when that counterpart is available to represent it instead. See ``isDeFactoPath(Path)`` for why that check -- rather than an unconditional exclusion -- is necessary.


.. py:method:: getPathsInROI(Roi)

   


.. py:method:: getPathsStructured()

   


.. py:method:: getPhantomFittedPaths()

   Returns "phantom" fitted paths: registered paths that look like ordinary, standalone paths but are actually the fitted flavor of an original that no longer exists in any form -- neither registered here nor resolvable from a ``fittedversionof`` reference. This happens when a traces file is loaded whose ``fittedversionof`` attribute points to a path ID absent from the file itself (e.g. the raw/unfitted original was deleted before saving), which leaves ``Path.fittedVersionOf`` ``null`` rather than merely unregistered. Such paths pass loading validation silently and are indistinguishable from a normal path except for their negative ID (see ``Path.setFitted(Path)``).


.. py:method:: getPlugin()

   Gets the SNT instance.


.. py:method:: getSWCFor(Collection)

   Converts a collection of connected Path objects into SWC points for export.

   SWC is the standardized format used for neuromorphological data exchange. The conversion process:

   - Validates that paths form a proper tree structure with exactly one primary path (tree's root)

   - Uses breadth-first traversal to ensure correct parent-child relationships

   - Assigns sequential SWC IDs starting from 1

   - Establishes proper parent references based on path connectivity

   - Preserves path properties including SWC type, color, annotations, and custom tags

   **Path Requirements:**

   - Must contain exactly **one primary path** (root of the tree)

   - All non-primary paths must have valid parent relationships

   - Paths must form a connected tree structure (no disconnected components)

   - Empty paths (size == 0) are automatically skipped


.. py:method:: getSelectedPaths()

   Gets all paths selected in the GUI


.. py:method:: getTree(String)

   Returns the specified Tree.


.. py:method:: getTrees()

   Returns all the paths associated with this PathAndFillManager instance, grouped by Tree.


.. py:method:: getVersionInUse(Path)

   Returns the version of a path that is in use, i.e., the one that is displayed and analyzed: its fitted flavor if ``Path.getUseFitted()``, otherwise the path itself. Same rule as ``Tree(Collection)``, which uses the collection itself as registry. A fitted copy whose original is registered with this manager is first resolved to that original (see ``isDeFactoPath(Path)``), so that both flavors of a path always resolve to the same version.


.. py:method:: isDeFactoPath(Path)

   Single source of truth (manager-bound convenience over ``Path.isDeFactoPath(Collection)``) for whether ``p`` should be treated as a normal, standalone/"de facto" path rather than one redundant with an un-fitted counterpart already registered here.

   Deliberately checks object identity against ``allPaths`` rather than looking up ``p.getUnfitted().getID()`` via ``getPathFromID(int)``: registration (e.g. ``addTree(Tree, String)`` with ``forceNewId=true``) reassigns every path a new ID, discarding whatever ID it had in its source file. An un-fitted counterpart that was never registered still carries its *original* file ID, which can -- and in practice does -- collide with the freshly assigned ID of some unrelated, actually-registered path, making an ID-based lookup a false positive.


.. py:method:: isSelected(Path)

   Checks if a Path is currently selected in the GUI.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setHeadless(boolean)

   Sets whether this PathAndFillManager instance should run headless.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: createFromFile(String, int[])

   Creates a PathAndFillManager instance from imported data


.. py:method:: exportAllPathsAsSWC(String)

   


.. py:method:: exportFillsAsCSV(File)

   Export fills as CSV.


.. py:method:: exportToCSV(File)

   Output some potentially useful information about all the Paths managed by this instance as a CSV (comma separated values) file.


.. py:method:: exportTree(int, File)

   


.. py:method:: importNeurons(Map, ColorRGB, String)

   Import neuron(s) as a collection of reconstruction nodes (SWC points)


.. py:method:: importSWC(String, String)

   Imports an SWC file using advanced options.


.. py:method:: importSWCs(Map, ColorRGB)

   Imports a group of SWC files (Remote URLs supported).


.. py:method:: load(String, int[])

   Imports a reconstruction file (any supported extension).


.. py:method:: loadGuessingType(String)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addPath(Path)

   


.. py:method:: addPathAndFillListener(PathAndFillListener)

   Adds a PathAndFillListener. This is used by the interface to have changes in the path manager reported so that they can be reflected in the UI.


.. py:method:: addTree(Tree)

   Adds a ``Tree``. If an image is currently being traced, it is assumed it is large enough to contain the tree.


.. py:method:: addTrees(Collection)

   Adds a collection of `Tree`s.


.. py:method:: allPointsIterator()

   


.. py:method:: anySelected()

   Checks whether at least one Path is currently selected in the UI.


.. py:method:: assignSpatialSettings(ImagePlus)

   


.. py:method:: canvasResized()

   


.. py:method:: contentAdded(Content)

   


.. py:method:: contentChanged(Content)

   


.. py:method:: contentRemoved(Content)

   


.. py:method:: contentSelected(Content)

   


.. py:method:: createFromGraph(DirectedWeightedGraph, boolean)

   Create a new PathAndFillManager instance from the graph.


.. py:method:: createFromNodes(Collection)

   Creates a PathAndFillManager instance from a collection of reconstruction nodes.


.. py:method:: deletePath(Path)

   Deletes a path.


.. py:method:: deletePaths(Collection)

   Delete paths by position.


.. py:method:: dispose()

   


.. py:method:: downsampleAll(double)

   Downsamples alls path using Ramer-Douglas-Peucker simplification. Downsampling occurs only between branch points and terminal points.


.. py:method:: endElement(String, String, String)

   


.. py:method:: nearestNodeInUse(Collection, double, double, double)

   As ``nearestNodeOnPaths(Collection, double, double, double)``, but searching the version in use of each path (see ``getVersionInUse(Path)``). The returned ``PathAndFillManager.NodeRef.path()`` is that version.


.. py:method:: nearestNodeOnPaths(Collection, double, double, double)

   Finds the node nearest to a position, across the given paths as they are (no fitted/unfitted resolution: see ``nearestNodeInUse(Collection, double, double, double)``).


.. py:method:: nearestPointOnAnyPath(Collection, PointInCanvas, double)

   


.. py:method:: pathChanged(PathChangeEvent)

   


.. py:method:: repairPhantomFittedPaths()

   Repairs the paths returned by ``getPhantomFittedPaths()`` into ordinary, standalone paths: assigns each a fresh, valid (positive, collision-free) ID and a default name, since the fit-time name/ID are meaningless once the original they were fitted from is gone.


.. py:method:: size()

   Returns the number of Paths in the PathAndFillManager list.


.. py:method:: startElement(String, String, String, Attributes)

   


.. py:method:: transformPaths(PathTransformer, ImagePlus, ImagePlus)

   


.. py:method:: transformationFinished(View)

   


.. py:method:: transformationStarted(View)

   


.. py:method:: transformationUpdated(View)

   


.. py:method:: universeClosed()

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.PathAndFillManager>`_
* `PathAndFillManager JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathAndFillManager.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
