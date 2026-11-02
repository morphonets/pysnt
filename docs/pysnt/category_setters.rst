Setters Methods
===============

Methods that modify values or properties of objects.

Total methods in this category: **696**

.. contents:: Classes in this Category
   :local:

Annotation3D
------------

.. method:: setBoundingBoxColor(boundingBoxColor)

   Determines whether the mesh bounding box should be displayed.

   **Signature:** ``setBoundingBoxColor(ColorRGB) -> void``

   **Parameters:**

   * **boundingBoxColor** (``Any``): - the color of the mesh bounding box. If null, no bounding box is displayed

   **Returns:** ``None``

.. method:: setColor(color)

   Script friendly method to assign a color to the annotation.

   **Signature:** ``setColor(String) -> void``

   **Parameters:**

   * **color** (``str``): - the color to render the imported file, either a 1) HTML color codes starting with hash (

   **Returns:** ``None``

.. method:: setTransparency(transparencyPercent)

   Script friendly method to assign a transparency to the annotation.

   **Signature:** ``setTransparency(double) -> void``

   **Parameters:**

   * **transparencyPercent** (``float``): - the color transparency (in percentage)

   **Returns:** ``None``

.. method:: setWireframeColor(color)

   Assigns a wireframe color to the annotation.

   **Signature:** ``setWireframeColor(ColorRGB) -> void``

   **Parameters:**

   * **color** (``Any``): - the wireframe color. Ignored if the annotation has no wireframe.

   **Returns:** ``None``


AnnotationGraph
---------------

.. method:: removeOrphans()

   **Signature:** ``removeOrphans() -> Set``

   **Returns:** ``Set[Any]``

.. method:: setEdgeColor(edge, color)

   **Signature:** ``setEdgeColor(DefaultWeightedEdge, ColorRGB) -> void``

   **Parameters:**

   * **edge** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setVertexColor(vertex, color)

   **Signature:** ``setVertexColor(Object, ColorRGB) -> void``

   **Parameters:**

   * **vertex** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setVertexValue(vertex, value)

   **Signature:** ``setVertexValue(Object, double) -> void``

   **Parameters:**

   * **vertex** (``Any``)
   * **value** (``float``)

   **Returns:** ``None``


ArraySearchImage
----------------

.. method:: setValue(x, y, node)

   **Signature:** ``setValue(int, int, Object) -> void``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **node** (``Any``)

   **Returns:** ``None``


ArrayStorageBackend
-------------------

.. method:: setConnectivityType(type)

   **Signature:** ``setConnectivityType(int) -> void``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``None``

.. method:: setDistance(index, distance)

   **Signature:** ``setDistance(long, double) -> void``

   **Parameters:**

   * **index** (``int``)
   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setGWDT(index, value)

   **Signature:** ``setGWDT(long, double) -> void``

   **Parameters:**

   * **index** (``int``)
   * **value** (``float``)

   **Returns:** ``None``

.. method:: setParent(index, parentIndex)

   **Signature:** ``setParent(long, long) -> void``

   **Parameters:**

   * **index** (``int``)
   * **parentIndex** (``int``)

   **Returns:** ``None``

.. method:: setState(index, stateValue)

   **Signature:** ``setState(long, byte) -> void``

   **Parameters:**

   * **index** (``int``)
   * **stateValue** (``int``)

   **Returns:** ``None``

.. method:: setTrackAliveIndices(track)

   **Signature:** ``setTrackAliveIndices(boolean) -> void``

   **Parameters:**

   * **track** (``bool``)

   **Returns:** ``None``


AutoTraceConfig
---------------

.. method:: addWarning(warning)

   **Signature:** ``addWarning(String) -> void``

   **Parameters:**

   * **warning** (``str``)

   **Returns:** ``None``


AutoTracer
----------

.. method:: setRoots(seeds)

   **Signature:** ``setRoots(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setTips(seeds)

   **Signature:** ``setTips(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setWaypoints(seeds)

   **Signature:** ``setWaypoints(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``


Bdv
---

.. method:: addMouseListenerToDisplay(ml)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``addMouseListenerToDisplay(MouseListener) -> void``

   **Parameters:**

   * **ml** (``Any``): - the listener to add

   **Returns:** ``None``

.. method:: addTree(tree)

   **Signature:** ``addTree(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``)

   **Returns:** ``None``

.. method:: clearAllTrees()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``clearAllTrees() -> void``

   **Returns:** ``None``

.. method:: enableTracing(manual)

   **Signature:** ``enableTracing(boolean) -> void``

   **Parameters:**

   * **manual** (``bool``)

   **Returns:** ``None``

.. method:: removeTree(treeLabel)

   **Signature:** ``removeTree(String) -> boolean``

   **Parameters:**

   * **treeLabel** (``str``)

   **Returns:** ``bool``

.. method:: setCalibration(spacing, unit)

   **Signature:** ``setCalibration(double[], String) -> void``

   **Parameters:**

   * **spacing** (``List[float]``)
   * **unit** (``str``)

   **Returns:** ``None``

.. method:: setCurrentTimepoint(timepoint)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``setCurrentTimepoint(int) -> void``

   **Parameters:**

   * **timepoint** (``int``): - the 1-based timepoint to navigate to; values < 1 are coerced to 1

   **Returns:** ``None``

.. method:: setDisplayRadii(display)

   Switches between frustum (radius-based) and centerline rendering. Invalidates the overlay cache and requests a repaint.

   **Signature:** ``setDisplayRadii(boolean) -> void``

   **Parameters:**

   * **display** (``bool``): -

   **Returns:** ``None``

.. method:: setPathOverlayOffset(offsetX, offsetY, offsetZ)

   Shifts all rendered trees by (offsetX, offsetY, offsetZ) in world coordinates, for rendering purposes only.

   **Signature:** ``setPathOverlayOffset(double, double, double) -> void``

   **Parameters:**

   * **offsetX** (``float``): - x offset in calibrated units
   * **offsetY** (``float``)
   * **offsetZ** (``float``)

   **Returns:** ``None``

.. method:: setRenderSettleTime(millis)

   **Signature:** ``setRenderSettleTime(long) -> void``

   **Parameters:**

   * **millis** (``int``)

   **Returns:** ``None``

.. method:: setTracingLockedByPause(locked)

   **Signature:** ``setTracingLockedByPause(boolean) -> void``

   **Parameters:**

   * **locked** (``bool``)

   **Returns:** ``None``

.. method:: setViewerTransform(target, durationMs)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``setViewerTransform(AffineTransform3D, long) -> void``

   **Parameters:**

   * **target** (``Any``): - the desired world-to-screen transform
   * **durationMs** (``int``)

   **Returns:** ``None``

.. method:: toggleEditMode()

   **Signature:** ``toggleEditMode() -> void``

   **Returns:** ``None``


BiSearch
--------

.. method:: addProgressListener(callback)

   Description copied from class: `AbstractSearch`

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **callback** (``Any``): - the callback to register

   **Returns:** ``None``


BiSearchArtist
--------------

.. method:: setClosedColor(color)

   **Signature:** ``setClosedColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setDrawingThreshold(threshold)

   **Signature:** ``setDrawingThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setOpenColor(color)

   **Signature:** ``setOpenColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``


BiSearchNode
------------

.. method:: setFFromGoal(fFromGoal)

   **Signature:** ``setFFromGoal(double) -> void``

   **Parameters:**

   * **fFromGoal** (``float``)

   **Returns:** ``None``

.. method:: setFFromStart(fFromStart)

   **Signature:** ``setFFromStart(double) -> void``

   **Parameters:**

   * **fFromStart** (``float``)

   **Returns:** ``None``

.. method:: setFrom(g, f, p, fromStart)

   **Signature:** ``setFrom(double, double, BiSearchNode, boolean) -> void``

   **Parameters:**

   * **g** (``float``)
   * **f** (``float``)
   * **p** (``BiSearchNode``)
   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: setFromGoal(gFromGoal, fFromGoal, predecessorFromGoal)

   **Signature:** ``setFromGoal(double, double, BiSearchNode) -> void``

   **Parameters:**

   * **gFromGoal** (``float``)
   * **fFromGoal** (``float``)
   * **predecessorFromGoal** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setFromStart(gFromStart, fFromStart, predecessorFromStart)

   **Signature:** ``setFromStart(double, double, BiSearchNode) -> void``

   **Parameters:**

   * **gFromStart** (``float``)
   * **fFromStart** (``float``)
   * **predecessorFromStart** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setGFromGoal(gFromGoal)

   **Signature:** ``setGFromGoal(double) -> void``

   **Parameters:**

   * **gFromGoal** (``float``)

   **Returns:** ``None``

.. method:: setGFromStart(gFromStart)

   **Signature:** ``setGFromStart(double) -> void``

   **Parameters:**

   * **gFromStart** (``float``)

   **Returns:** ``None``

.. method:: setHeapHandle(handle, fromStart)

   **Signature:** ``setHeapHandle(Handle, boolean) -> void``

   **Parameters:**

   * **handle** (``Any``)
   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: setHeapHandleFromGoal(heapHandleFromGoal)

   **Signature:** ``setHeapHandleFromGoal(Handle) -> void``

   **Parameters:**

   * **heapHandleFromGoal** (``Any``)

   **Returns:** ``None``

.. method:: setHeapHandleFromStart(heapHandleFromStart)

   **Signature:** ``setHeapHandleFromStart(Handle) -> void``

   **Parameters:**

   * **heapHandleFromStart** (``Any``)

   **Returns:** ``None``

.. method:: setPosition(x, y, z)

   **Signature:** ``setPosition(int, int, int) -> void``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)

   **Returns:** ``None``

.. method:: setPredecessorFromGoal(predecessorFromGoal)

   **Signature:** ``setPredecessorFromGoal(BiSearchNode) -> void``

   **Parameters:**

   * **predecessorFromGoal** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setPredecessorFromStart(predecessorFromStart)

   **Signature:** ``setPredecessorFromStart(BiSearchNode) -> void``

   **Parameters:**

   * **predecessorFromStart** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setState(state, fromStart)

   **Signature:** ``setState(State, boolean) -> void``

   **Parameters:**

   * **state** (``Any``)
   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: setStateFromGoal(stateFromGoal)

   **Signature:** ``setStateFromGoal(State) -> void``

   **Parameters:**

   * **stateFromGoal** (``Any``)

   **Returns:** ``None``

.. method:: setStateFromStart(stateFromStart)

   **Signature:** ``setStateFromStart(State) -> void``

   **Parameters:**

   * **stateFromStart** (``Any``)

   **Returns:** ``None``

.. method:: setX(x)

   **Signature:** ``setX(int) -> void``

   **Parameters:**

   * **x** (``int``)

   **Returns:** ``None``

.. method:: setY(y)

   **Signature:** ``setY(int) -> void``

   **Parameters:**

   * **y** (``int``)

   **Returns:** ``None``

.. method:: setZ(z)

   **Signature:** ``setZ(int) -> void``

   **Parameters:**

   * **z** (``int``)

   **Returns:** ``None``


BinaryTracer
------------

.. method:: setConnectComponents(connectComponents)

   **Signature:** ``setConnectComponents(boolean) -> void``

   **Parameters:**

   * **connectComponents** (``bool``)

   **Returns:** ``None``

.. method:: setLengthThreshold(lengthThreshold)

   **Signature:** ``setLengthThreshold(double) -> void``

   **Parameters:**

   * **lengthThreshold** (``float``)

   **Returns:** ``None``

.. method:: setMaxConnectDist(maxConnectDist)

   **Signature:** ``setMaxConnectDist(double) -> void``

   **Parameters:**

   * **maxConnectDist** (``float``)

   **Returns:** ``None``

.. method:: setOrigIP(origIP)

   **Signature:** ``setOrigIP(ImagePlus) -> void``

   **Parameters:**

   * **origIP** (``Any``)

   **Returns:** ``None``

.. method:: setPruneEnds(pruneEnds)

   **Signature:** ``setPruneEnds(boolean) -> void``

   **Parameters:**

   * **pruneEnds** (``bool``)

   **Returns:** ``None``

.. method:: setPruneMode(pruneMode)

   **Signature:** ``setPruneMode(int) -> void``

   **Parameters:**

   * **pruneMode** (``int``)

   **Returns:** ``None``

.. method:: setRootRoi(roi, strategy)

   **Signature:** ``setRootRoi(Roi, int) -> void``

   **Parameters:**

   * **roi** (``Any``)
   * **strategy** (``int``)

   **Returns:** ``None``

.. method:: setRoots(seeds)

   **Signature:** ``setRoots(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setShortestPath(shortestPath)

   **Signature:** ``setShortestPath(boolean) -> void``

   **Parameters:**

   * **shortestPath** (``bool``)

   **Returns:** ``None``

.. method:: setSilent(silent)

   **Signature:** ``setSilent(boolean) -> void``

   **Parameters:**

   * **silent** (``bool``)

   **Returns:** ``None``

.. method:: setTips(seeds)

   **Signature:** ``setTips(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setVerbose(verbose)

   **Signature:** ``setVerbose(boolean) -> void``

   **Parameters:**

   * **verbose** (``bool``)

   **Returns:** ``None``

.. method:: setWaypoints(seeds)

   **Signature:** ``setWaypoints(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``


BookmarkManager
---------------

.. method:: addViewerToolbarButton(component)

   Adds a component to the viewer toolbar section of this panel. The component is appended after a separator the first time this method is called. Viewer subclasses use this to inject context-specific controls (e.g. a slab-clip toggle).

   **Signature:** ``addViewerToolbarButton(JComponent) -> void``

   **Parameters:**

   * **component** (``Any``): - the component to add; must not be

   **Returns:** ``None``

.. method:: clearSelection()

   Clears the selection of bookmarks in the table. Does nothing if no selection exists.

   **Signature:** ``clearSelection() -> void``

   **Returns:** ``None``

.. method:: setVisible(visible)

   Shows or hides this manager's markers in the big-viewer overlay without touching the model itself (bookmarks are neither added nor removed), leaving every other owner's layer (paths, seed annotations) untouched. Mirrors `SeedOverlay.isVisible()`'s role for `SeedOverlayBigViewerHandler`.

   **Signature:** ``setVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - true to show, false to hide

   **Returns:** ``None``

.. method:: toggleViewerPanel()

   Shows or hides this marker manager's UI: redirects to SNTUI's "Bookmarks" tab whenever when SNTUI is present (e.g., in stream mode, see `insideSNTUI()`), otherwise toggles the floating viewer dialog.

   **Signature:** ``toggleViewerPanel() -> void``

   **Returns:** ``None``


BoundingBox
-----------

.. method:: setDimensions(uncalibratedWidth, uncalibratedHeight, uncalibratedDepth)

   Sets the dimensions of this bounding box using uncalibrated (pixel) lengths.

   **Signature:** ``setDimensions(long, long, long) -> void``

   **Parameters:**

   * **uncalibratedWidth** (``int``): - the uncalibrated width
   * **uncalibratedHeight** (``int``)
   * **uncalibratedDepth** (``int``)

   **Returns:** ``None``

.. method:: setOrigin(origin)

   Sets the origin for this box, i.e., its (xMin, yMin, zMin) vertex.

   **Signature:** ``setOrigin(PointInImage) -> void``

   **Parameters:**

   * **origin** (``PointInImage``): - the new origin

   **Returns:** ``None``

.. method:: setOriginOpposite(originOpposite)

   Sets the origin opposite for this box, i.e., its (xMax, yMax, zMax) vertex.

   **Signature:** ``setOriginOpposite(PointInImage) -> void``

   **Parameters:**

   * **originOpposite** (``PointInImage``): - the new origin opposite.

   **Returns:** ``None``

.. method:: setSpacing(xSpacing, ySpacing, zSpacing, spacingUnit)

   Sets the voxel spacing.

   **Signature:** ``setSpacing(double, double, double, String) -> void``

   **Parameters:**

   * **xSpacing** (``float``): - the 'voxel width' of the bounding box
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)
   * **spacingUnit** (``str``)

   **Returns:** ``None``

.. method:: setUnit(unit)

   Sets the default length unit for voxel spacing (typically um, for SWC reconstructions)

   **Signature:** ``setUnit(String) -> void``

   **Parameters:**

   * **unit** (``str``): - the new unit

   **Returns:** ``None``


Bvv
---

.. method:: addMouseListenerToDisplay(ml)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``addMouseListenerToDisplay(MouseListener) -> void``

   **Parameters:**

   * **ml** (``Any``): - the listener to add

   **Returns:** ``None``

.. method:: addTree(tree)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``addTree(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the transform to be applied

   **Returns:** ``None``

.. method:: clearAllTrees()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``clearAllTrees() -> void``

   **Returns:** ``None``

.. method:: enableTracing(manual)

   **Signature:** ``enableTracing(boolean) -> void``

   **Parameters:**

   * **manual** (``bool``)

   **Returns:** ``None``

.. method:: removeTree(treeLabel)

   **Signature:** ``removeTree(String) -> boolean``

   **Parameters:**

   * **treeLabel** (``str``)

   **Returns:** ``bool``

.. method:: setCalibration(spacing, unit)

   Overrides the voxel calibration (spacing and unit) for all loaded sources. This is useful when the image metadata does not carry the correct spatial calibration (e.g., ND2 files opened via SCIFIO/Bio-Formats where the unit string is lost). The change takes effect immediately: the scale bar, distance measurements, and slab-thickness controls will all use the new values.

   **Signature:** ``setCalibration(double[], String) -> void``

   **Parameters:**

   * **spacing** (``List[float]``): - voxel size in {x, y, z} order
   * **unit** (``str``)

   **Returns:** ``None``

.. method:: setChannelColors(colors)

   Sets per-channel colors across all source groups, assigning colors sequentially by global channel order across all groups. For example, with two 3-channel images and colors [R, G, B, C, M, Y], image 1 gets R/G/B and image 2 gets C/M/Y. With a single multichannel image or a dataset where each setup is its own group (e.g. IMS), colors are assigned one-to-one in load order.

To apply the same color pattern to every group independently, call `setChannelColors(BvvMultiSource, Color...)` per group.

Typical script usage: 
```
def bvv = Bvv.open(img)
   bvv.setChannelColors(Color.RED, Color.GREEN, Color.BLUE)
```


   **Signature:** ``setChannelColors(Color[]) -> void``

   **Parameters:**

   * **colors** (``List[Any]``): - colors assigned sequentially across all channels in all groups

   **Returns:** ``None``

   **Example:**

   .. code-block:: java

      def bvv = Bvv.open(img)
         bvv.setChannelColors(Color.RED, Color.GREEN, Color.BLUE)

.. method:: setCurrentTimepoint(timepoint)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``setCurrentTimepoint(int) -> void``

   **Parameters:**

   * **timepoint** (``int``): - the 1-based timepoint to navigate to; values < 1 are coerced to 1

   **Returns:** ``None``

.. method:: setDisplayRadii(display)

   Sets whether paths are rendered as tapered frusta with per-node radii (`true`) or as anti-aliased lines (`false`). Line rendering is significantly faster for datasets with many paths. Automatically invalidates the overlay cache and repaints.

   **Signature:** ``setDisplayRadii(boolean) -> void``

   **Parameters:**

   * **display** (``bool``): -

   **Returns:** ``None``

.. method:: setDisplayRange(group, min, max)

   Sets the display range (min/max intensity) for all channels of a specific source group.

   **Signature:** ``setDisplayRange(BvvMultiSource, double, double) -> void``

   **Parameters:**

   * **group** (``BvvMultiSource``): - the target source group, obtained from getMultiSources()
   * **min** (``float``)
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setPathOverlayOffset(offsetX, offsetY, offsetZ)

   Offsets all paths being rendered. This allows for 'dislodging' paths from their underlying signal without altering their coordinates.

Rendering-only: stored purely in `renderingOptions.pathOffset` and read directly by `OverlayRenderer#computeScreenData`. Does NOT touch `Path`/`Tree` state

   **Signature:** ``setPathOverlayOffset(double, double, double) -> void``

   **Parameters:**

   * **offsetX** (``float``): - X offset (calibrated distance)
   * **offsetY** (``float``)
   * **offsetZ** (``float``)

   **Returns:** ``None``

.. method:: setRenderSettleTime(millis)

   **Signature:** ``setRenderSettleTime(long) -> void``

   **Parameters:**

   * **millis** (``int``)

   **Returns:** ``None``

.. method:: setTracingLockedByPause(locked)

   **Signature:** ``setTracingLockedByPause(boolean) -> void``

   **Parameters:**

   * **locked** (``bool``)

   **Returns:** ``None``

.. method:: setViewerTransform(target, durationMs)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``setViewerTransform(AffineTransform3D, long) -> void``

   **Parameters:**

   * **target** (``Any``): - the desired world-to-screen transform
   * **durationMs** (``int``)

   **Returns:** ``None``

.. method:: toggleEditMode()

   **Signature:** ``toggleEditMode() -> void``

   **Returns:** ``None``


BvvMultiSource
--------------

.. method:: removeFromBvv()

   Removes all sources in the group from the viewer.

   **Signature:** ``removeFromBvv() -> void``

   **Returns:** ``None``

.. method:: setActive(active)

   Sets the active/visible state for all sources in the group.

   **Signature:** ``setActive(boolean) -> void``

   **Parameters:**

   * **active** (``bool``): -

   **Returns:** ``None``

.. method:: setColor(color)

   Sets the color for all sources in the group.

   **Signature:** ``setColor(ARGBType) -> void``

   **Parameters:**

   * **color** (``Any``): - the ARGB color

   **Returns:** ``None``

.. method:: setDisplayRange(min, max)

   Sets the display range for all sources in the group.

   **Signature:** ``setDisplayRange(double, double) -> void``

   **Parameters:**

   * **min** (``float``): - minimum display value
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setLiveSync(live)

   Sets whether transforms are propagated to followers on every render frame (`true`) or only on explicit `syncTransforms()` calls (`false`).

   **Signature:** ``setLiveSync(boolean) -> void``

   **Parameters:**

   * **live** (``bool``): -

   **Returns:** ``None``


BvvUtils
--------

.. method:: clearCaches()

   Releases the in-memory cell caches of all streamed (N5/Zarr/IMS) sources shown in BVV. Open viewers keep working: tiles are simply reloaded on demand. The GPU tile cache is not affected (it is freed when its window closes)

   **Signature:** ``clearCaches() -> long``

   **Returns:** (``int``) the number of cells that were resident (loaded) and have now been released

.. method:: setCachePrefMB(mb)

   Persists the GPU tile cache preference (MB). 0 means automatic. Applies next time a BVV window is opened

   **Signature:** ``setCachePrefMB(int) -> void``

   **Parameters:**

   * **mb** (``int``)

   **Returns:** ``None``

.. method:: setCachePromptSuppressed(suppress)

   **Signature:** ``setCachePromptSuppressed(boolean) -> void``

   **Parameters:**

   * **suppress** (``bool``)

   **Returns:** ``None``

.. method:: setFetchersPref(n)

   Persists the tile fetcher thread preference. 0 means automatic. Applies when a dataset is next opened

   **Signature:** ``setFetchersPref(int) -> void``

   **Parameters:**

   * **n** (``int``)

   **Returns:** ``None``

.. method:: setRenderQuality(quality)

   **Signature:** ``setRenderQuality(RenderQuality) -> void``

   **Parameters:**

   * **quality** (``Any``)

   **Returns:** ``None``

.. method:: setSessionCacheMB(mb)

   Overrides the preference for the current session only (0 clears the override)

   **Signature:** ``setSessionCacheMB(int) -> void``

   **Parameters:**

   * **mb** (``int``)

   **Returns:** ``None``


ConvexHullAnalyzer
------------------

.. method:: setLabel(analysisLabel)

   Sets the optional description for the analysis

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **analysisLabel** (``str``): - a string describing the analysis

   **Returns:** ``None``


CurationManager
---------------

.. method:: addWarnings(warnings)

   Appends warnings to the table without replacing existing ones. Used by external producers that want to inject items into the warnings log alongside the ones already produced by the live/deep checks. The severity filter is re-applied automatically; entries whose severity is currently hidden are accepted into the underlying list but stay invisible until the user re-enables their severity in the toolbar.

   **Signature:** ``addWarnings(List) -> void``

   **Parameters:**

   * **warnings** (``List[Any]``): - entries to append;

   **Returns:** ``None``


DefaultSearchNode
-----------------

.. method:: setFrom(another)

   **Signature:** ``setFrom(DefaultSearchNode) -> void``

   **Parameters:**

   * **another** (``DefaultSearchNode``)

   **Returns:** ``None``

.. method:: setHandle(handle)

   **Signature:** ``setHandle(Handle) -> void``

   **Parameters:**

   * **handle** (``Any``)

   **Returns:** ``None``

.. method:: setPredecessor(p)

   **Signature:** ``setPredecessor(DefaultSearchNode) -> void``

   **Parameters:**

   * **p** (``DefaultSearchNode``)

   **Returns:** ``None``


DirectedWeightedGraph
---------------------

.. method:: addVertex(x, y, z)

   **Signature:** ``addVertex(double, double, double) -> SWCPoint``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** ``SWCPoint``

.. method:: setEdgeColor(edge, color)

   **Signature:** ``setEdgeColor(DefaultWeightedEdge, ColorRGB) -> void``

   **Parameters:**

   * **edge** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setRoot(newRoot)

   **Signature:** ``setRoot(SWCPoint) -> void``

   **Parameters:**

   * **newRoot** (``SWCPoint``)

   **Returns:** ``None``

.. method:: setVertexColor(vertex, color)

   **Signature:** ``setVertexColor(Object, ColorRGB) -> void``

   **Parameters:**

   * **vertex** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setVertexValue(vertex, value)

   **Signature:** ``setVertexValue(Object, double) -> void``

   **Parameters:**

   * **vertex** (``Any``)
   * **value** (``float``)

   **Returns:** ``None``


DirectedWeightedSubgraph
------------------------

.. method:: setLabel(label)

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **label** (``str``)

   **Returns:** ``None``

.. method:: setRoot(newRoot)

   **Signature:** ``setRoot(SWCPoint) -> void``

   **Parameters:**

   * **newRoot** (``SWCPoint``)

   **Returns:** ``None``


DiskBackedGWDTTracer
--------------------

.. method:: setAllowVoxelGap(allow)

   **Signature:** ``setAllowVoxelGap(boolean) -> void``

   **Parameters:**

   * **allow** (``bool``)

   **Returns:** ``None``

.. method:: setAutoFilter(enabled)

   **Signature:** ``setAutoFilter(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setBackgroundThreshold(threshold)

   **Signature:** ``setBackgroundThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setBranchTuneMaxAngle(maxAngleDeg)

   **Signature:** ``setBranchTuneMaxAngle(double) -> void``

   **Parameters:**

   * **maxAngleDeg** (``float``)

   **Returns:** ``None``

.. method:: setCaliperFraction(fraction)

   **Signature:** ``setCaliperFraction(double) -> void``

   **Parameters:**

   * **fraction** (``float``)

   **Returns:** ``None``

.. method:: setConnectivityType(type)

   **Signature:** ``setConnectivityType(int) -> void``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``None``

.. method:: setJointLeafPruneEnabled(enabled)

   **Signature:** ``setJointLeafPruneEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setLeafPruneOverlap(threshold)

   **Signature:** ``setLeafPruneOverlap(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setMaxGapVoxels(maxVoxels)

   **Signature:** ``setMaxGapVoxels(int) -> void``

   **Parameters:**

   * **maxVoxels** (``int``)

   **Returns:** ``None``

.. method:: setMinSegmentLengthVoxels(lengthInVoxels)

   **Signature:** ``setMinSegmentLengthVoxels(double) -> void``

   **Parameters:**

   * **lengthInVoxels** (``float``)

   **Returns:** ``None``

.. method:: setMinSomaDistance(distance)

   **Signature:** ``setMinSomaDistance(double) -> void``

   **Parameters:**

   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setNSomas(nSomas)

   **Signature:** ``setNSomas(int) -> void``

   **Parameters:**

   * **nSomas** (``int``)

   **Returns:** ``None``

.. method:: setOvershootRemovalEnabled(enabled)

   **Signature:** ``setOvershootRemovalEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setParallelBranchPruneEnabled(enabled)

   **Signature:** ``setParallelBranchPruneEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setPathFittingEnabled(enabled)

   **Signature:** ``setPathFittingEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setResampleStep(step)

   **Signature:** ``setResampleStep(double) -> void``

   **Parameters:**

   * **step** (``float``)

   **Returns:** ``None``

.. method:: setRoots(seeds)

   **Signature:** ``setRoots(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setScoreMap(map)

   **Signature:** ``setScoreMap(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **map** (``Any``)

   **Returns:** ``None``

.. method:: setScoreMapEnabled(enabled)

   **Signature:** ``setScoreMapEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setScoreMapFilterType(type)

   **Signature:** ``setScoreMapFilterType(FilterType) -> void``

   **Parameters:**

   * **type** (``Any``)

   **Returns:** ``None``

.. method:: setScoreMapPruneThreshold(threshold)

   **Signature:** ``setScoreMapPruneThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setScoreMapScales(scales)

   **Signature:** ``setScoreMapScales(double[]) -> void``

   **Parameters:**

   * **scales** (``List[float]``)

   **Returns:** ``None``

.. method:: setSeed(voxelCoords)

   **Signature:** ``setSeed(long[]) -> void``

   **Parameters:**

   * **voxelCoords** (``List[int]``)

   **Returns:** ``None``

.. method:: setSeedPhysical(physicalCoords)

   **Signature:** ``setSeedPhysical(double[]) -> void``

   **Parameters:**

   * **physicalCoords** (``List[float]``)

   **Returns:** ``None``

.. method:: setSomaRoi(roi)

   **Signature:** ``setSomaRoi(Roi) -> void``

   **Parameters:**

   * **roi** (``Any``)

   **Returns:** ``None``

.. method:: setSomaRoiZPosition(z)

   **Signature:** ``setSomaRoiZPosition(int) -> void``

   **Parameters:**

   * **z** (``int``)

   **Returns:** ``None``

.. method:: setSphereOverlapThreshold(threshold)

   **Signature:** ``setSphereOverlapThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setSrRatio(ratio)

   **Signature:** ``setSrRatio(double) -> void``

   **Parameters:**

   * **ratio** (``float``)

   **Returns:** ``None``

.. method:: setStatusListener(listener)

   **Signature:** ``setStatusListener(Consumer) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: setTipExtensionDistance(distance)

   **Signature:** ``setTipExtensionDistance(double) -> void``

   **Parameters:**

   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setTips(seeds)

   **Signature:** ``setTips(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setTracedRegionBuffer(buffer)

   **Signature:** ``setTracedRegionBuffer(int) -> void``

   **Parameters:**

   * **buffer** (``int``)

   **Returns:** ``None``

.. method:: setVerbose(verbose)

   **Signature:** ``setVerbose(boolean) -> void``

   **Parameters:**

   * **verbose** (``bool``)

   **Returns:** ``None``

.. method:: setWaypointBiasFixedFactor(factor)

   **Signature:** ``setWaypointBiasFixedFactor(double) -> void``

   **Parameters:**

   * **factor** (``float``)

   **Returns:** ``None``

.. method:: setWaypointBiasRadiusVoxels(radius)

   **Signature:** ``setWaypointBiasRadiusVoxels(double) -> void``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``None``

.. method:: setWaypointBiasSource(source)

   **Signature:** ``setWaypointBiasSource(WaypointBiasSource) -> void``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``None``

.. method:: setWaypointBiasStrength(strength)

   **Signature:** ``setWaypointBiasStrength(double) -> void``

   **Parameters:**

   * **strength** (``float``)

   **Returns:** ``None``

.. method:: setWaypoints(seeds)

   **Signature:** ``setWaypoints(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setZigzagRemovalEnabled(enabled)

   **Signature:** ``setZigzagRemovalEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``


DiskBackedStorageBackend
------------------------

.. method:: setConnectivityType(type)

   **Signature:** ``setConnectivityType(int) -> void``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``None``

.. method:: setDistance(index, distance)

   **Signature:** ``setDistance(long, double) -> void``

   **Parameters:**

   * **index** (``int``)
   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setGWDT(index, value)

   **Signature:** ``setGWDT(long, double) -> void``

   **Parameters:**

   * **index** (``int``)
   * **value** (``float``)

   **Returns:** ``None``

.. method:: setParent(index, parentIndex)

   **Signature:** ``setParent(long, long) -> void``

   **Parameters:**

   * **index** (``int``)
   * **parentIndex** (``int``)

   **Returns:** ``None``

.. method:: setState(index, stateValue)

   **Signature:** ``setState(long, byte) -> void``

   **Parameters:**

   * **index** (``int``)
   * **stateValue** (``int``)

   **Returns:** ``None``

.. method:: setTrackAliveIndices(track)

   **Signature:** ``setTrackAliveIndices(boolean) -> void``

   **Parameters:**

   * **track** (``bool``)

   **Returns:** ``None``


Fill
----

.. method:: setMetric(cost)

   Sets the cost metric for the filled structure.

   **Signature:** ``setMetric(CostType) -> void``

   **Parameters:**

   * **cost** (``Any``): - the cost type to set

   **Returns:** ``None``

.. method:: setSourcePaths(newSourcePaths)

   Sets the source paths for the filled structure using a set of paths.

   **Signature:** ``setSourcePaths(Path[]) -> void``

   **Parameters:**

   * **newSourcePaths** (``List[Path]``): - the set of new source paths

   **Returns:** ``None``

.. method:: setSpacing(x_spacing, y_spacing, z_spacing, units)

   **Signature:** ``setSpacing(double, double, double, String) -> void``

   **Parameters:**

   * **x_spacing** (``float``)
   * **y_spacing** (``float``)
   * **z_spacing** (``float``)
   * **units** (``str``)

   **Returns:** ``None``

.. method:: setThreshold(threshold)

   Sets the distance threshold for the filled structure.

   **Signature:** ``setThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``): - the threshold value to set

   **Returns:** ``None``


FillManagerUI
-------------

.. method:: setFillList(fillList)

   **Signature:** ``setFillList(List) -> void``

   **Parameters:**

   * **fillList** (``List[Any]``)

   **Returns:** ``None``

.. method:: setFillTransparent(transparent)

   Sets the transparency state of fills.

   **Signature:** ``setFillTransparent(boolean) -> void``

   **Parameters:**

   * **transparent** (``bool``): - true to make fills transparent, false for opaque

   **Returns:** ``None``

.. method:: setPathList(justAdded, expandAll)

   **Signature:** ``setPathList(Path, boolean) -> void``

   **Parameters:**

   * **justAdded** (``Path``)
   * **expandAll** (``bool``)

   **Returns:** ``None``

.. method:: setSelectedPaths(selectedPathSet, source)

   **Signature:** ``setSelectedPaths(Collection, Object) -> void``

   **Parameters:**

   * **selectedPathSet** (``List[Any]``)
   * **source** (``Any``)

   **Returns:** ``None``

.. method:: setSplitFills(split)

   Sets whether each path should be filled independently.

   **Signature:** ``setSplitFills(boolean) -> void``

   **Parameters:**

   * **split** (``bool``): - true to enable "one fill per path", false for bulk filling

   **Returns:** ``None``


FillerThread
------------

.. method:: addNode(n, fromStart)

   **Signature:** ``addNode(DefaultSearchNode, boolean) -> void``

   **Parameters:**

   * **n** (``DefaultSearchNode``)
   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: addProgressListener(callback)

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **callback** (``Any``)

   **Returns:** ``None``

.. method:: setSourcePaths(newSourcePaths)

   **Signature:** ``setSourcePaths(Collection) -> void``

   **Parameters:**

   * **newSourcePaths** (``List[Any]``)

   **Returns:** ``None``

.. method:: setStopAtThreshold(stopAtThreshold)

   Whether to terminate the fill operation once all nodes less than or equal to the distance threshold have been explored. If false, the search will run until it has explored the entire image. The default is false.

   **Signature:** ``setStopAtThreshold(boolean) -> void``

   **Parameters:**

   * **stopAtThreshold** (``bool``): -

   **Returns:** ``None``

.. method:: setStoreExtraNodes(storeExtraNodes)

   Whether to store above-threshold nodes in the `Fill` object. The default is true.

   **Signature:** ``setStoreExtraNodes(boolean) -> void``

   **Parameters:**

   * **storeExtraNodes** (``bool``): -

   **Returns:** ``None``

.. method:: setThreshold(threshold)

   **Signature:** ``setThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``


FillerThreadArtist
------------------

.. method:: setClosedColor(color)

   **Signature:** ``setClosedColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setOpacity(percent)

   **Signature:** ``setOpacity(double) -> void``

   **Parameters:**

   * **percent** (``float``)

   **Returns:** ``None``

.. method:: setOpenColor(color)

   **Signature:** ``setOpenColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``


GWDTTracer
----------

.. method:: setAllowVoxelGap(allow)

   **Signature:** ``setAllowVoxelGap(boolean) -> void``

   **Parameters:**

   * **allow** (``bool``)

   **Returns:** ``None``

.. method:: setAutoFilter(enabled)

   **Signature:** ``setAutoFilter(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setBackgroundThreshold(threshold)

   **Signature:** ``setBackgroundThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setBranchTuneMaxAngle(maxAngleDeg)

   **Signature:** ``setBranchTuneMaxAngle(double) -> void``

   **Parameters:**

   * **maxAngleDeg** (``float``)

   **Returns:** ``None``

.. method:: setCaliperFraction(fraction)

   **Signature:** ``setCaliperFraction(double) -> void``

   **Parameters:**

   * **fraction** (``float``)

   **Returns:** ``None``

.. method:: setConnectivityType(type)

   **Signature:** ``setConnectivityType(int) -> void``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``None``

.. method:: setJointLeafPruneEnabled(enabled)

   **Signature:** ``setJointLeafPruneEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setLeafPruneOverlap(threshold)

   **Signature:** ``setLeafPruneOverlap(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setMaxGapVoxels(maxVoxels)

   **Signature:** ``setMaxGapVoxels(int) -> void``

   **Parameters:**

   * **maxVoxels** (``int``)

   **Returns:** ``None``

.. method:: setMinSegmentLengthVoxels(lengthInVoxels)

   **Signature:** ``setMinSegmentLengthVoxels(double) -> void``

   **Parameters:**

   * **lengthInVoxels** (``float``)

   **Returns:** ``None``

.. method:: setMinSomaDistance(distance)

   **Signature:** ``setMinSomaDistance(double) -> void``

   **Parameters:**

   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setNSomas(nSomas)

   **Signature:** ``setNSomas(int) -> void``

   **Parameters:**

   * **nSomas** (``int``)

   **Returns:** ``None``

.. method:: setOvershootRemovalEnabled(enabled)

   **Signature:** ``setOvershootRemovalEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setParallelBranchPruneEnabled(enabled)

   **Signature:** ``setParallelBranchPruneEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setPathFittingEnabled(enabled)

   **Signature:** ``setPathFittingEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setResampleStep(step)

   **Signature:** ``setResampleStep(double) -> void``

   **Parameters:**

   * **step** (``float``)

   **Returns:** ``None``

.. method:: setRoots(seeds)

   **Signature:** ``setRoots(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setScoreMap(map)

   **Signature:** ``setScoreMap(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **map** (``Any``)

   **Returns:** ``None``

.. method:: setScoreMapEnabled(enabled)

   **Signature:** ``setScoreMapEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setScoreMapFilterType(type)

   **Signature:** ``setScoreMapFilterType(FilterType) -> void``

   **Parameters:**

   * **type** (``Any``)

   **Returns:** ``None``

.. method:: setScoreMapPruneThreshold(threshold)

   **Signature:** ``setScoreMapPruneThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setScoreMapScales(scales)

   **Signature:** ``setScoreMapScales(double[]) -> void``

   **Parameters:**

   * **scales** (``List[float]``)

   **Returns:** ``None``

.. method:: setSeed(voxelCoords)

   **Signature:** ``setSeed(long[]) -> void``

   **Parameters:**

   * **voxelCoords** (``List[int]``)

   **Returns:** ``None``

.. method:: setSeedPhysical(physicalCoords)

   **Signature:** ``setSeedPhysical(double[]) -> void``

   **Parameters:**

   * **physicalCoords** (``List[float]``)

   **Returns:** ``None``

.. method:: setSomaRoi(roi)

   **Signature:** ``setSomaRoi(Roi) -> void``

   **Parameters:**

   * **roi** (``Any``)

   **Returns:** ``None``

.. method:: setSomaRoiZPosition(z)

   **Signature:** ``setSomaRoiZPosition(int) -> void``

   **Parameters:**

   * **z** (``int``)

   **Returns:** ``None``

.. method:: setSphereOverlapThreshold(threshold)

   **Signature:** ``setSphereOverlapThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setSrRatio(ratio)

   **Signature:** ``setSrRatio(double) -> void``

   **Parameters:**

   * **ratio** (``float``)

   **Returns:** ``None``

.. method:: setStatusListener(listener)

   **Signature:** ``setStatusListener(Consumer) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: setTipExtensionDistance(distance)

   **Signature:** ``setTipExtensionDistance(double) -> void``

   **Parameters:**

   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setTips(seeds)

   **Signature:** ``setTips(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setTracedRegionBuffer(buffer)

   **Signature:** ``setTracedRegionBuffer(int) -> void``

   **Parameters:**

   * **buffer** (``int``)

   **Returns:** ``None``

.. method:: setVerbose(verbose)

   **Signature:** ``setVerbose(boolean) -> void``

   **Parameters:**

   * **verbose** (``bool``)

   **Returns:** ``None``

.. method:: setWaypointBiasFixedFactor(factor)

   **Signature:** ``setWaypointBiasFixedFactor(double) -> void``

   **Parameters:**

   * **factor** (``float``)

   **Returns:** ``None``

.. method:: setWaypointBiasRadiusVoxels(radius)

   **Signature:** ``setWaypointBiasRadiusVoxels(double) -> void``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``None``

.. method:: setWaypointBiasSource(source)

   **Signature:** ``setWaypointBiasSource(WaypointBiasSource) -> void``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``None``

.. method:: setWaypointBiasStrength(strength)

   **Signature:** ``setWaypointBiasStrength(double) -> void``

   **Parameters:**

   * **strength** (``float``)

   **Returns:** ``None``

.. method:: setWaypoints(seeds)

   **Signature:** ``setWaypoints(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setZigzagRemovalEnabled(enabled)

   **Signature:** ``setZigzagRemovalEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``


GroupedTreeStatistics
---------------------

.. method:: addGroup(group, groupLabel)

   Adds a comparison group to the analysis queue.

   **Signature:** ``addGroup(Collection, String) -> void``

   **Parameters:**

   * **group** (``List[Any]``): - the collection of Trees to be analyzed
   * **groupLabel** (``str``)

   **Returns:** ``None``

.. method:: setMinNBins(minNoOfBins)

   Sets the minimum number of bins when assembling histograms.

   **Signature:** ``setMinNBins(int) -> void``

   **Parameters:**

   * **minNoOfBins** (``int``): - the minimum number of bins.

   **Returns:** ``None``


GrowthAnalyzer
--------------

.. method:: setMinTimePoints(minTimePoints)

   **Signature:** ``setMinTimePoints(int) -> void``

   **Parameters:**

   * **minTimePoints** (``int``)

   **Returns:** ``None``

.. method:: setPhaseSensitivity(phaseSensitivity)

   **Signature:** ``setPhaseSensitivity(double) -> void``

   **Parameters:**

   * **phaseSensitivity** (``float``)

   **Returns:** ``None``

.. method:: setPlateauThreshold(plateauThresholdFraction)

   **Signature:** ``setPlateauThreshold(double) -> void``

   **Parameters:**

   * **plateauThresholdFraction** (``float``)

   **Returns:** ``None``

.. method:: setRapidThreshold(rapidThresholdMultiple)

   **Signature:** ``setRapidThreshold(double) -> void``

   **Parameters:**

   * **rapidThresholdMultiple** (``float``)

   **Returns:** ``None``

.. method:: setRetractionThreshold(retractionThreshold)

   **Signature:** ``setRetractionThreshold(double) -> void``

   **Parameters:**

   * **retractionThreshold** (``float``)

   **Returns:** ``None``

.. method:: setUseGlobalThresholds(useGlobalThresholds)

   **Signature:** ``setUseGlobalThresholds(boolean) -> void``

   **Parameters:**

   * **useGlobalThresholds** (``bool``)

   **Returns:** ``None``

.. method:: setWindowSizeFraction(windowSizeFraction)

   **Signature:** ``setWindowSizeFraction(double) -> void``

   **Parameters:**

   * **windowSizeFraction** (``float``)

   **Returns:** ``None``


ImageParser2D
-------------

.. method:: setAggressiveSpikeSuppression(enabled)

   **Signature:** ``setAggressiveSpikeSuppression(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setCenter(x, y)

   **Signature:** ``setCenter(double, double) -> void``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)

   **Returns:** ``None``

.. method:: setCenterFromROI()

   **Signature:** ``setCenterFromROI() -> void``

   **Returns:** ``None``

.. method:: setCenterPx(x, y)

   **Signature:** ``setCenterPx(int, int) -> void``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)

   **Returns:** ``None``

.. method:: setHemiShells(flag)

   **Signature:** ``setHemiShells(String) -> void``

   **Parameters:**

   * **flag** (``str``)

   **Returns:** ``None``

.. method:: setPosition(channel, slice, frame)

   **Signature:** ``setPosition(int, int, int) -> void``

   **Parameters:**

   * **channel** (``int``)
   * **slice** (``int``)
   * **frame** (``int``)

   **Returns:** ``None``

.. method:: setRadii(radiiArray)

   **Signature:** ``setRadii(double[]) -> void``

   **Parameters:**

   * **radiiArray** (``List[float]``)

   **Returns:** ``None``

.. method:: setRadiiSpan(nSamples, integrationFlag)

   **Signature:** ``setRadiiSpan(int, int) -> void``

   **Parameters:**

   * **nSamples** (``int``)
   * **integrationFlag** (``int``)

   **Returns:** ``None``

.. method:: setRetrieveIntDensities(retrieveIntDensities)

   **Signature:** ``setRetrieveIntDensities(boolean) -> void``

   **Parameters:**

   * **retrieveIntDensities** (``bool``)

   **Returns:** ``None``

.. method:: setThreshold(lower, upper)

   **Signature:** ``setThreshold(double, double) -> void``

   **Parameters:**

   * **lower** (``float``)
   * **upper** (``float``)

   **Returns:** ``None``


ImageParser3D
-------------

.. method:: setCenter(x, y, z)

   **Signature:** ``setCenter(double, double, double) -> void``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** ``None``

.. method:: setCenterFromROI()

   **Signature:** ``setCenterFromROI() -> void``

   **Returns:** ``None``

.. method:: setCenterPx(x, y, z)

   **Signature:** ``setCenterPx(int, int, int) -> void``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)

   **Returns:** ``None``

.. method:: setHemiShells(flag)

   **Signature:** ``setHemiShells(String) -> void``

   **Parameters:**

   * **flag** (``str``)

   **Returns:** ``None``

.. method:: setPosition(channel, frame)

   **Signature:** ``setPosition(int, int) -> void``

   **Parameters:**

   * **channel** (``int``)
   * **frame** (``int``)

   **Returns:** ``None``

.. method:: setRadii(radiiArray)

   **Signature:** ``setRadii(double[]) -> void``

   **Parameters:**

   * **radiiArray** (``List[float]``)

   **Returns:** ``None``

.. method:: setRetrieveIntDensities(retrieveIntDensities)

   **Signature:** ``setRetrieveIntDensities(boolean) -> void``

   **Parameters:**

   * **retrieveIntDensities** (``bool``)

   **Returns:** ``None``

.. method:: setSkipSingleVoxels(skip)

   **Signature:** ``setSkipSingleVoxels(boolean) -> void``

   **Parameters:**

   * **skip** (``bool``)

   **Returns:** ``None``

.. method:: setThreshold(lower, upper)

   **Signature:** ``setThreshold(double, double) -> void``

   **Parameters:**

   * **lower** (``float``)
   * **upper** (``float``)

   **Returns:** ``None``


ImgUtils
--------

.. method:: setOmeZarrCalibration(path, spacing, unit)

   Sets the spacing and/or unit in the root metadata of a local OME-Zarr (OME-NGFF v0.5) container. Spacing is the level 0 voxel size: the scale and translation of every pyramid level are rescaled by the ratio between the new and the stored spacing, so the pyramid stays consistent. Only the metadata file is rewritten

   **Signature:** ``setOmeZarrCalibration(String, double[], String) -> boolean``

   **Parameters:**

   * **path** (``str``): - the container directory (or its
   * **spacing** (``List[float]``): , see getLocalOmeZarrDir(java.lang.String))
   * **unit** (``str``)

   **Returns:** (``bool``) true if the metadata was updated

.. method:: setOmeZarrUnit(path, unit)

   Sets the unit of the spatial axes in the root metadata of a local OME-Zarr (OME-NGFF v0.5) container. Only the metadata file is rewritten

   **Signature:** ``setOmeZarrUnit(String, String) -> boolean``

   **Parameters:**

   * **path** (``str``): - the container directory (or its
   * **unit** (``str``): , see getLocalOmeZarrDir(java.lang.String))

   **Returns:** (``bool``) true if the metadata was updated


ImpUtils
--------

.. method:: clearAllTags()

   Clears both tag registries entirely. Intended as a session-teardown safety net, not for routine use: individual images are already forgotten via `forgetTags(ImagePlus)` as they close.

   **Signature:** ``clearAllTags() -> void``

   **Returns:** ``None``

.. method:: removeIsolatedPixels(binaryImp)

   **Signature:** ``removeIsolatedPixels(ImagePlus) -> void``

   **Parameters:**

   * **binaryImp** (``Any``)

   **Returns:** ``None``

.. method:: removeSlices(stack, labels)

   **Signature:** ``removeSlices(ImageStack, Collection) -> void``

   **Parameters:**

   * **stack** (``Any``)
   * **labels** (``List[Any]``)

   **Returns:** ``None``

.. method:: setIsDisplayCanvas(imp)

   Used by SNT to tag an image as a Display Canvas (typically a blank placeholder image).

   **Signature:** ``setIsDisplayCanvas(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``): - the image to be tagged

   **Returns:** ``None``

.. method:: setIsMaterializedCrop(imp)

   Used by SNT to tag an eagerly-materialized pixel crop of a streamed volume as such.

   **Signature:** ``setIsMaterializedCrop(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``): - the image to be tagged

   **Returns:** ``None``

.. method:: setLut(imp, lutName)

   **Signature:** ``setLut(ImagePlus, String) -> void``

   **Parameters:**

   * **imp** (``Any``)
   * **lutName** (``str``)

   **Returns:** ``None``

.. method:: setSliceLabels(stack, commonLabel)

   **Signature:** ``setSliceLabels(ImageStack, String) -> void``

   **Parameters:**

   * **stack** (``Any``)
   * **commonLabel** (``str``)

   **Returns:** ``None``


LinearProfileStats
------------------

.. method:: setMaxEvaluations(maxEval)

   **Signature:** ``setMaxEvaluations(int) -> void``

   **Parameters:**

   * **maxEval** (``int``)

   **Returns:** ``None``

.. method:: setPrimaryBranches(nBranches)

   **Signature:** ``setPrimaryBranches(int) -> void``

   **Parameters:**

   * **nBranches** (``int``)

   **Returns:** ``None``


ListSearchImage
---------------

.. method:: setValue(x, y, value)

   **Signature:** ``setValue(int, int, Object) -> void``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **value** (``Any``)

   **Returns:** ``None``


MapSearchImage
--------------

.. method:: setValue(x, y, value)

   **Signature:** ``setValue(int, int, Object) -> void``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **value** (``Any``)

   **Returns:** ``None``


MouseLightQuerier
-----------------

.. method:: setCCFVersion(version)

   Sets the version of the Common Coordinate Framework to be used by the Querier.

   **Signature:** ``setCCFVersion(String) -> void``

   **Parameters:**

   * **version** (``str``): - Either "3" (the default), or "2.5" (MouseLight legacy)

   **Returns:** ``None``


MultiSpectralRefiner
--------------------

.. method:: setAutoTune(autoTune)

   Enables automatic parameter tuning from path and image statistics. When enabled, `call()` will adjust `maxRadius`, `cosSimilarityThreshold`, and intensity thresholds based on the actual data before running the optimization loop.

   **Signature:** ``setAutoTune(boolean) -> void``

   **Parameters:**

   * **autoTune** (``bool``): - true to enable (default false)

   **Returns:** ``None``

.. method:: setBackgroundThreshold(threshold)

   Sets the background fraction threshold. If more than this fraction of voxels in a node's sphere fail the intensity test, the node is considered to be in the background.

   **Signature:** ``setBackgroundThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``): - the threshold (default 0.47)

   **Returns:** ``None``

.. method:: setColorWeight(weight)

   Sets the weight for the color (cosine similarity) penalty term.

   **Signature:** ``setColorWeight(double) -> void``

   **Parameters:**

   * **weight** (``float``): - the weight (default 0.85)

   **Returns:** ``None``

.. method:: setConvergenceThreshold(threshold)

   Sets the convergence threshold for the refinement loop. The loop stops when the relative improvement per iteration falls below this fraction (e.g., 0.001 = stop when improvement is less than 0.1% of total penalty).

   **Signature:** ``setConvergenceThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``): - the relative improvement threshold (default 0.001)

   **Returns:** ``None``

.. method:: setCosSimilarityThreshold(threshold)

   Sets the cosine similarity threshold below which a voxel is considered spectrally dissimilar to the reference color.

   **Signature:** ``setCosSimilarityThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``): - the threshold (default 0.90)

   **Returns:** ``None``

.. method:: setIntensityRange(minIntensity, maxIntensity)

   Sets the intensity range for adaptive percent-C computation.

   **Signature:** ``setIntensityRange(double, double) -> void``

   **Parameters:**

   * **minIntensity** (``float``): - lower bound (total channel sum); default 10000
   * **maxIntensity** (``float``)

   **Returns:** ``None``

.. method:: setIntensityWeight(weight)

   Sets the weight for the intensity background penalty term.

   **Signature:** ``setIntensityWeight(double) -> void``

   **Parameters:**

   * **weight** (``float``): - the weight (default 1.00)

   **Returns:** ``None``

.. method:: setMaxIterations(maxIterations)

   Sets the maximum number of iterations for the refinement loop. The loop also stops early if convergence is reached.

   **Signature:** ``setMaxIterations(int) -> void``

   **Parameters:**

   * **maxIterations** (``int``): - the iteration cap (default 50)

   **Returns:** ``None``

.. method:: setMaxRadius(maxRadius)

   Sets the maximum radius (in pixels) to test during radius optimization.

   **Signature:** ``setMaxRadius(int) -> void``

   **Parameters:**

   * **maxRadius** (``int``): - the max radius (default 12)

   **Returns:** ``None``

.. method:: setPercentCRange(minPercent, maxPercent)

   Sets the percent-C range for adaptive intensity tolerance.

   **Signature:** ``setPercentCRange(double, double) -> void``

   **Parameters:**

   * **minPercent** (``float``): - tolerance at high intensities (default 0.05)
   * **maxPercent** (``float``)

   **Returns:** ``None``

.. method:: setRadiusWeight(weight)

   Sets the weight for the radius expansion penalty term.

   **Signature:** ``setRadiusWeight(double) -> void``

   **Parameters:**

   * **weight** (``float``): - the weight (default 3.75)

   **Returns:** ``None``

.. method:: setReferenceWindowRadius(windowRadius)

   Sets the sliding-window radius for per-node reference color computation. When enabled, each node's reference color is the average of the ±N neighboring nodes along the path, rather than a single global average. This handles color drift along long axons in Brainbow images.

   **Signature:** ``setReferenceWindowRadius(int) -> void``

   **Parameters:**

   * **windowRadius** (``int``): - number of nodes on each side to include. Use -1 (default) for a single global reference, or a positive value (e.g., 10–30) for sliding window.

   **Returns:** ``None``


MultiTreeColorMapper
--------------------

.. method:: setMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinMax(min, max)

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **min** (``float``)
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setMinMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMinMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinPercentileClipped(values, clipPercent)

   **Signature:** ``setMinPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(nanColor)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **nanColor** (``Any``)

   **Returns:** ``None``


MultiTreeStatistics
-------------------

.. method:: setExactMetricMatch(exactMetricMatch)

   Main method for testing and demonstration purposes.

Creates a MultiTreeStatistics instance using demo data and displays various analysis plots including histograms and flow plots. This method is primarily used for development and debugging.

   **Signature:** ``setExactMetricMatch(boolean) -> void``

   **Parameters:**

   * **exactMetricMatch** (``bool``): - command line arguments (not used)

   **Returns:** ``None``

.. method:: setLabel(groupLabel)

   Sets an identifying label for the group of Trees being analyzed.

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **groupLabel** (``str``): - the identifying string for the group.

   **Returns:** ``None``

.. method:: setTable(table)

   **Signature:** ``setTable(GenericTable) -> void``

   **Parameters:**

   * **table** (``Any``)

   **Returns:** ``None``


MultiViewer2D
-------------

.. method:: setAxesVisible(visible)

   **Signature:** ``setAxesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setColorBarLegend(colorMapper)

   **Signature:** ``setColorBarLegend(ColorMapper) -> void``

   **Parameters:**

   * **colorMapper** (``Any``)

   **Returns:** ``None``

.. method:: setGridlinesVisible(visible)

   **Signature:** ``setGridlinesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setLayoutColumns(cols)

   **Signature:** ``setLayoutColumns(int) -> void``

   **Parameters:**

   * **cols** (``int``)

   **Returns:** ``None``

.. method:: setOutlineVisible(visible)

   **Signature:** ``setOutlineVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setTitle(title)

   Sets the title of this Viewer's frame.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``): - the viewer's title.

   **Returns:** ``None``

.. method:: setXrange(xMin, xMax)

   Sets a manual range for the viewers' X-axis. Calling `setXrange(-1, -1)` enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setXrange(double, double) -> void``

   **Parameters:**

   * **xMin** (``float``): - the lower-limit for the X-axis
   * **xMax** (``float``)

   **Returns:** ``None``

.. method:: setYrange(yMin, yMax)

   Sets a manual range for the viewers' Y-axis. Calling `setYrange(-1, -1)` enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setYrange(double, double) -> void``

   **Parameters:**

   * **yMin** (``float``): - the lower-limit for the Y-axis
   * **yMax** (``float``)

   **Returns:** ``None``


MultiViewer3D
-------------

.. method:: addColorBarLegend(colorMapper)

   **Signature:** ``addColorBarLegend(ColorMapper) -> void``

   **Parameters:**

   * **colorMapper** (``Any``)

   **Returns:** ``None``

.. method:: setAnimationEnabled(enabled)

   **Signature:** ``setAnimationEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setGap(gap)

   **Signature:** ``setGap(int) -> void``

   **Parameters:**

   * **gap** (``int``)

   **Returns:** ``None``

.. method:: setLabels(labels)

   **Signature:** ``setLabels(List) -> void``

   **Parameters:**

   * **labels** (``List[Any]``)

   **Returns:** ``None``

.. method:: setLayoutColumns(cols)

   **Signature:** ``setLayoutColumns(int) -> void``

   **Parameters:**

   * **cols** (``int``)

   **Returns:** ``None``

.. method:: setTitle(title)

   Sets the title of the Viewer's frame.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``): - the viewer's title.

   **Returns:** ``None``

.. method:: setViewMode(view)

   **Signature:** ``setViewMode(ViewMode) -> void``

   **Parameters:**

   * **view** (``Any``)

   **Returns:** ``None``


NeuroMorphoLoader
-----------------

.. method:: enableSourceVersion(enable)

   Enables or disables the use of source version URLs.

   **Signature:** ``enableSourceVersion(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - true to enable source version URLs, false otherwise

   **Returns:** ``None``


NodeColorMapper
---------------

.. method:: setMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinMax(min, max)

   Description copied from class: `ColorMapper`

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **min** (``float``): - the mapping lower bound (i.e., the highest measurement value for the LUT scale). It is automatically calculated (the default) when set to Double.NaN
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setMinMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMinMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinPercentileClipped(values, clipPercent)

   **Signature:** ``setMinPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(nanColor)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **nanColor** (``Any``)

   **Returns:** ``None``


NodeProfiler
------------

.. method:: setNodeStep(nodeStep)

   **Signature:** ``setNodeStep(int) -> void``

   **Parameters:**

   * **nodeStep** (``int``): - sets the sampling frequency. I.e., if 10, each 10th node is sampled.

   **Returns:** ``None``

.. method:: setRadius(radius)

   **Signature:** ``setRadius(int) -> void``

   **Parameters:**

   * **radius** (``int``): - the radius (in pixels) of sampling shape

   **Returns:** ``None``

.. method:: setShape(shape)

   Sets the shape of the iterating cursor.

   **Signature:** ``setShape(Shape) -> void``

   **Parameters:**

   * **shape** (``Any``): - A ProfileProcessor.Shape

   **Returns:** ``None``


NodeStatistics
--------------

.. method:: setLabel(label)

   Sets a descriptive label to this statistic analysis to be used in histograms, etc.

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **label** (``str``): - the descriptive label

   **Returns:** ``None``


OBJMesh
-------

.. method:: setBoundingBoxColor(boundingBoxColor)

   Determines whether the mesh bounding box should be displayed.

   **Signature:** ``setBoundingBoxColor(ColorRGB) -> void``

   **Parameters:**

   * **boundingBoxColor** (``Any``): - the color of the mesh bounding box, either a 1) HTML color codes starting with hash (

   **Returns:** ``None``

.. method:: setColor(color, transparencyPercent)

   Assigns a color to the mesh.

   **Signature:** ``setColor(ColorRGB, double) -> void``

   **Parameters:**

   * **color** (``Any``): - the color to render the imported file
   * **transparencyPercent** (``float``)

   **Returns:** ``None``

.. method:: setDisplayedHemisphere(hemiHalf)

   Sets which hemisphere of this mesh is displayed.

   **Signature:** ``setDisplayedHemisphere(String) -> void``

   **Parameters:**

   * **hemiHalf** (``str``): - "left" (or "l", "1"), "right" (or "r", "2"), or anything else for both hemispheres

   **Returns:** ``None``

.. method:: setLabel(label)

   Sets the label for this mesh.

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **label** (``str``): - the label to set

   **Returns:** ``None``

.. method:: setSourceAnnotation(annotation)

   Associates this mesh with the `BrainAnnotation` (atlas compartment) it was retrieved from.

   **Signature:** ``setSourceAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **annotation** (``Any``): - the source annotation

   **Returns:** ``None``

.. method:: setSymmetryAxis(axis)

   Sets the axis defining the symmetry plane of this mesh (e.g., the sagittal plane for most bilateria models), where X=0; Y=1; Z=2;

   **Signature:** ``setSymmetryAxis(int) -> void``

   **Parameters:**

   * **axis** (``int``)

   **Returns:** ``None``

.. method:: setTransparency(transparencyPercent)

   Changes the transparency of this mesh.

   **Signature:** ``setTransparency(double) -> void``

   **Parameters:**

   * **transparencyPercent** (``float``): - the mesh transparency (in percentage).

   **Returns:** ``None``

.. method:: setVolume(volume)

   Sets the volume of this mesh.

   **Signature:** ``setVolume(double) -> void``

   **Parameters:**

   * **volume** (``float``): - the volume to set

   **Returns:** ``None``


OneMinusErf
-----------

.. method:: setZFudge(zFudge)

   **Signature:** ``setZFudge(double) -> void``

   **Parameters:**

   * **zFudge** (``float``)

   **Returns:** ``None``


Path
----

.. method:: addNode(point)

   Appends a node to this Path.

   **Signature:** ``addNode(PointInImage) -> void``

   **Parameters:**

   * **point** (``PointInImage``): - the node to be inserted

   **Returns:** ``None``

.. method:: addPointDouble(x, y, z)

   **Signature:** ``addPointDouble(double, double, double) -> void``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** ``None``

.. method:: removeNode(index)

   Removes the specified node if this path has at least two nodes. Does nothing if this is a single point path.

   **Signature:** ``removeNode(int) -> void``

   **Parameters:**

   * **index** (``int``): - the zero-based index of the node to be removed

   **Returns:** ``None``

.. method:: setBranchFrom(parentPath, branchPoint)

   Establishes this path as a child path originating from the specified parent path.

In detail:

- Sets the parent path that this path branches from

- Records the exact point where branching occurs

- Adds this path to the parent's children collection

- Updates this path's order to be parent order + 1

- Maintains bidirectional references for tree traversal

   **Signature:** ``setBranchFrom(Path, PointInImage) -> void``

   **Parameters:**

   * **parentPath** (``Path``): - the parent path that this path branches from. Must not be null. Some operations may expect it to be an existing path in the same tree structure
   * **branchPoint** (``PointInImage``)

   **Returns:** ``None``

.. method:: setCTposition(channel, frame)

   Sets the hyperstack position of this Path

   **Signature:** ``setCTposition(int, int) -> void``

   **Parameters:**

   * **channel** (``int``): - the channel (one-based index)
   * **frame** (``int``)

   **Returns:** ``None``

.. method:: setCanvasOffset(canvasOffset)

   Specifies a translation offset when rendering this Path in a `TracerCanvas`. Path coordinates remain unaltered.

   **Signature:** ``setCanvasOffset(PointInCanvas) -> void``

   **Parameters:**

   * **canvasOffset** (``Any``): - the x,y,z coordinates (pixel-based) specifying the translation offset

   **Returns:** ``None``

.. method:: setColor(color)

   Sets this path color.

   **Signature:** ``setColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``): - the path color. Set it to null, to have SNT render this Path using default settings. You may need to cast the null reference to

   **Returns:** ``None``

.. method:: setEditableNode(index)

   Tags the specified point position as 'editable'.

   **Signature:** ``setEditableNode(int) -> void``

   **Parameters:**

   * **index** (``int``): - the index of the point to be tagged. Set it to -1 to for no tagging

   **Returns:** ``None``

.. method:: setGuessedTangents(pointsEitherSide)

   **Signature:** ``setGuessedTangents(int) -> void``

   **Parameters:**

   * **pointsEitherSide** (``int``)

   **Returns:** ``None``

.. method:: setName(newName)

   Sets this Path's name. Set it to null or `""`, to reset it to the default.

   **Signature:** ``setName(String) -> void``

   **Parameters:**

   * **newName** (``str``): - the new name.

   **Returns:** ``None``

.. method:: setNodeAnnotation(annotation, pos)

   Assigns an annotation to an existing node.

   **Signature:** ``setNodeAnnotation(BrainAnnotation, int) -> void``

   **Parameters:**

   * **annotation** (``Any``): - the node annotation
   * **pos** (``int``)

   **Returns:** ``None``

.. method:: setNodeColor(color, pos)

   Sets the node color.

   **Signature:** ``setNodeColor(Color, int) -> void``

   **Parameters:**

   * **color** (``Any``): - the node color
   * **pos** (``int``)

   **Returns:** ``None``

.. method:: setNodeColors(colors)

   Sets the node colors.

   **Signature:** ``setNodeColors(Color[]) -> void``

   **Parameters:**

   * **colors** (``List[Any]``): - the colors used to render the nodes of this. If null (the default) all nodes are rendered using the Path color.

   **Returns:** ``None``

.. method:: setNodeHemisphere(hemisphereFlag, pos)

   Assigns a hemisphere to an existing node.

   **Signature:** ``setNodeHemisphere(char, int) -> void``

   **Parameters:**

   * **hemisphereFlag** (``str``): - the node hemisphere flag.
   * **pos** (``int``)

   **Returns:** ``None``

.. method:: setNodeRadius(radius, pos)

   Sets the radius of a specific node.

   **Signature:** ``setNodeRadius(double, int) -> void``

   **Parameters:**

   * **radius** (``float``): - the radius value
   * **pos** (``int``)

   **Returns:** ``None``

.. method:: setNodeTangent(tangent, pos)

   Sets the tangent vector of a specific node.

   **Signature:** ``setNodeTangent(double[], int) -> void``

   **Parameters:**

   * **tangent** (``List[float]``): - the X component of the tangent
   * **pos** (``int``)

   **Returns:** ``None``

.. method:: setNodeValue(value, pos)

   Assigns the "value" property to this node.

   **Signature:** ``setNodeValue(double, int) -> void``

   **Parameters:**

   * **value** (``float``): - the node value
   * **pos** (``int``)

   **Returns:** ``None``

.. method:: setNodeValues(values)

   Sets the path "values", the array containing the numeric property assigned to path nodes, typically voxel intensities.

   **Signature:** ``setNodeValues(double[]) -> void``

   **Parameters:**

   * **values** (``List[float]``): - the new node values

   **Returns:** ``None``

.. method:: setOrder(order)

   **Signature:** ``setOrder(int) -> void``

   **Parameters:**

   * **order** (``int``)

   **Returns:** ``None``

.. method:: setRadii(radii)

   Assigns radii to this Path

   **Signature:** ``setRadii(double[]) -> void``

   **Parameters:**

   * **radii** (``List[float]``): - the radii array. Setting it null removes the radius attribute from the Path

   **Returns:** ``None``

.. method:: setRadius(r)

   Assigns a radius to a specific node of this Path.

Sets the radius for the node at the specified index. If this is the first radius being set for the path and no tangents exist, this method will also compute guessed tangents to support proper 3D rendering.

   **Signature:** ``setRadius(double) -> void``

   **Parameters:**

   * **r** (``float``): - the radius to be assigned to the node. NaN values are ignored.

   **Returns:** ``None``

.. method:: setSWCType(newSWCType)

   **Signature:** ``setSWCType(int) -> void``

   **Parameters:**

   * **newSWCType** (``int``)

   **Returns:** ``None``

.. method:: setSelected(newSelectedStatus)

   **Signature:** ``setSelected(boolean) -> void``

   **Parameters:**

   * **newSelectedStatus** (``bool``)

   **Returns:** ``None``

.. method:: setSpacing(cal)

   **Signature:** ``setSpacing(Calibration) -> void``

   **Parameters:**

   * **cal** (``Any``)

   **Returns:** ``None``

.. method:: setUseFitted(useFitted)

   Sets whether the fitted flavor of this Path should be used.

   **Signature:** ``setUseFitted(boolean) -> void``

   **Parameters:**

   * **useFitted** (``bool``): - the new use fitted

   **Returns:** ``None``


PathAndFillManager
------------------

.. method:: addPath(p)

   **Signature:** ``addPath(Path) -> void``

   **Parameters:**

   * **p** (``Path``)

   **Returns:** ``None``

.. method:: addPathAndFillListener(listener)

   Adds a PathAndFillListener. This is used by the interface to have changes in the path manager reported so that they can be reflected in the UI.

   **Signature:** ``addPathAndFillListener(PathAndFillListener) -> void``

   **Parameters:**

   * **listener** (``Any``): - the listener

   **Returns:** ``None``

.. method:: addTree(tree)

   Adds a `Tree`. If an image is currently being traced, it is assumed it is large enough to contain the tree.

   **Signature:** ``addTree(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the collection of paths to be added

   **Returns:** ``None``

.. method:: addTrees(trees)

   Adds a collection of `Tree`s.

   **Signature:** ``addTrees(Collection) -> void``

   **Parameters:**

   * **trees** (``List[Any]``): - the collection of trees to be added

   **Returns:** ``None``

.. method:: setHeadless(headless)

   Sets whether this PathAndFillManager instance should run headless.

   **Signature:** ``setHeadless(boolean) -> void``

   **Parameters:**

   * **headless** (``bool``): - true to activate headless calls, otherwise false

   **Returns:** ``None``


PathFitter
----------

.. method:: setCrossSectionRadius(crossSectionRadius)

   Sets the radius of cross-sectional planes sampled around each node.

At each node, PathFitter samples a square cross-section perpendicular to the path tangent. This radius controls the physical extent of that sampling.

   **Signature:** ``setCrossSectionRadius(double) -> void``

   **Parameters:**

   * **crossSectionRadius** (``float``): - the physical search radius (in physical units)

   **Returns:** ``None``

.. method:: setImage(img)

   Sets the target image

   **Signature:** ``setImage(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **img** (``Any``): - the Image containing the signal to which the fit will be performed

   **Returns:** ``None``

.. method:: setNodeRadiusFallback(fallback)

   Sets the fallback strategy for node radii at locations where fitting failed.

When cross-section fitting fails at a node (e.g., low SNR, ambiguous geometry), this strategy determines what radius value to assign to that node.

   **Signature:** ``setNodeRadiusFallback(int) -> void``

   **Parameters:**

   * **fallback** (``int``): - the fallback strategy: FALLBACK_MODE, FALLBACK_MIN_SEP, or FALLBACK_NAN

   **Returns:** ``None``

.. method:: setProgressCallback(fitterIndex, progress)

   **Signature:** ``setProgressCallback(int, MultiTaskProgress) -> void``

   **Parameters:**

   * **fitterIndex** (``int``)
   * **progress** (``Any``)

   **Returns:** ``None``

.. method:: setReplaceNodes(replaceNodes)

   Sets whether fitting should occur "in place".

   **Signature:** ``setReplaceNodes(boolean) -> void``

   **Parameters:**

   * **replaceNodes** (``bool``): - If true, the nodes of the input Path will be replaced by those of the fitted result. If false, the fitted result is kept as a separated Path linked to the input as per Path.getFitted(). Note that in the latter case, some topological operations (e.g., forking) performed on the fitted result may not percolate to the non-fitted Path.

   **Returns:** ``None``

.. method:: setScope(scope)

   Sets the fitting scope.

   **Signature:** ``setScope(int) -> void``

   **Parameters:**

   * **scope** (``int``): - Either RADII, MIDPOINTS, or RADII_AND_MIDPOINTS

   **Returns:** ``None``

.. method:: setShowAnnotatedView(showAnnotatedView)

   Sets whether an interactive image of the result should be displayed.

   **Signature:** ``setShowAnnotatedView(boolean) -> void``

   **Parameters:**

   * **showAnnotatedView** (``bool``): - If true, an interactive stack (cross-section view) of the fit is displayed. Note that this is probably only useful if SNT's UI is visible and functional.

   **Returns:** ``None``


PathManagerUI
-------------

.. method:: clearSelection()

   Clears the current path selection.

   **Signature:** ``clearSelection() -> void``

   **Returns:** ``None``

.. method:: removeTags(p)

   **Signature:** ``removeTags(Path) -> String``

   **Parameters:**

   * **p** (``Path``)

   **Returns:** ``str``

.. method:: setCombinedSelectionFilters(enable)

   Sets whether selection filters should be combined. This is equivalent to toggling the 'filter' button in Path Manager's UI

   **Signature:** ``setCombinedSelectionFilters(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - if true, selection filters are combined

   **Returns:** ``None``

.. method:: setFillList(fillList)

   **Signature:** ``setFillList(List) -> void``

   **Parameters:**

   * **fillList** (``List[Any]``)

   **Returns:** ``None``

.. method:: setPathList(justAdded, expandAll)

   **Signature:** ``setPathList(Path, boolean) -> void``

   **Parameters:**

   * **justAdded** (``Path``)
   * **expandAll** (``bool``)

   **Returns:** ``None``

.. method:: setSelectedPaths(selectedPaths, source)

   **Signature:** ``setSelectedPaths(Collection, Object) -> void``

   **Parameters:**

   * **selectedPaths** (``List[Any]``)
   * **source** (``Any``)

   **Returns:** ``None``


PathProfiler
------------

.. method:: setMetric(metric)

   **Signature:** ``setMetric(Metric) -> void``

   **Parameters:**

   * **metric** (``Any``)

   **Returns:** ``None``

.. method:: setNodeIndicesAsDistances(nodeIndices)

   Sets whether the profile abscissae should be reported in real-word units (the default) or node indices (zero-based). Must be called before calling `getValues(Path)`, `getPlot()` or `getXYPlot()`.

   **Signature:** ``setNodeIndicesAsDistances(boolean) -> void``

   **Parameters:**

   * **nodeIndices** (``bool``): - If true, distances will be reported as indices.

   **Returns:** ``None``

.. method:: setRadius(radius)

   **Signature:** ``setRadius(int) -> void``

   **Parameters:**

   * **radius** (``int``)

   **Returns:** ``None``

.. method:: setShape(shape)

   **Signature:** ``setShape(Shape) -> void``

   **Parameters:**

   * **shape** (``Any``): - Either ProfileProcessor.Shape

   **Returns:** ``None``


PathStatistics
--------------

.. method:: setExactMetricMatch(exactMetricMatch)

   **Signature:** ``setExactMetricMatch(boolean) -> void``

   **Parameters:**

   * **exactMetricMatch** (``bool``)

   **Returns:** ``None``

.. method:: setTable(table)

   **Signature:** ``setTable(GenericTable) -> void``

   **Parameters:**

   * **table** (``Any``)

   **Returns:** ``None``


PathStraightener
----------------

.. method:: setWidth(width)

   Sets the width of the straightened path image.

   **Signature:** ``setWidth(int) -> void``

   **Parameters:**

   * **width** (``int``): - the width in pixels

   **Returns:** ``None``


PlausibilityCalibrator
----------------------

.. method:: setLowerPercentile(percentile)

   **Signature:** ``setLowerPercentile(double) -> void``

   **Parameters:**

   * **percentile** (``float``)

   **Returns:** ``None``

.. method:: setUpperPercentile(percentile)

   **Signature:** ``setUpperPercentile(double) -> void``

   **Parameters:**

   * **percentile** (``float``)

   **Returns:** ``None``


PlausibilityMonitor
-------------------

.. method:: addWarningListener(listener)

   **Signature:** ``addWarningListener(WarningListener) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: clearForkContext()

   **Signature:** ``clearForkContext() -> void``

   **Returns:** ``None``

.. method:: removeWarningListener(listener)

   **Signature:** ``removeWarningListener(WarningListener) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: setEnabled(enabled)

   **Signature:** ``setEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setImageData(image)

   **Signature:** ``setImageData(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **image** (``Any``)

   **Returns:** ``None``

.. method:: setImageStats(min, max)

   **Signature:** ``setImageStats(double, double) -> void``

   **Parameters:**

   * **min** (``float``)
   * **max** (``float``)

   **Returns:** ``None``


PointInImage
------------

.. method:: setAnnotation(annotation)

   Description copied from interface: `SNTPoint`

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **annotation** (``Any``): - the annotation to be assigned to this point

   **Returns:** ``None``

.. method:: setHemisphere(lr)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **lr** (``str``)

   **Returns:** ``None``

.. method:: setPath(onPath)

   Associates a Path with this node

   **Signature:** ``setPath(Path) -> void``

   **Parameters:**

   * **onPath** (``Path``): - the Path to be associated with this node

   **Returns:** ``None``


PolarProfileStats
-----------------

.. method:: setDataMode(mode)

   **Signature:** ``setDataMode(DataMode) -> void``

   **Parameters:**

   * **mode** (``Any``)

   **Returns:** ``None``


Profile
-------

.. method:: setCenter(center)

   **Signature:** ``setCenter(ShollPoint) -> void``

   **Parameters:**

   * **center** (``Any``)

   **Returns:** ``None``

.. method:: setExtraMeasurement(measurement, unit)

   **Signature:** ``setExtraMeasurement(String, String) -> void``

   **Parameters:**

   * **measurement** (``str``)
   * **unit** (``str``)

   **Returns:** ``None``

.. method:: setIdentifier(identifier)

   **Signature:** ``setIdentifier(String) -> void``

   **Parameters:**

   * **identifier** (``str``)

   **Returns:** ``None``

.. method:: setIsIntDensityProfile(isIntDensityProfile)

   **Signature:** ``setIsIntDensityProfile(boolean) -> void``

   **Parameters:**

   * **isIntDensityProfile** (``bool``)

   **Returns:** ``None``

.. method:: setNDimensions(twoDthreeD)

   **Signature:** ``setNDimensions(int) -> void``

   **Parameters:**

   * **twoDthreeD** (``int``)

   **Returns:** ``None``

.. method:: setProperties(properties)

   **Signature:** ``setProperties(Properties) -> void``

   **Parameters:**

   * **properties** (``Any``)

   **Returns:** ``None``

.. method:: setSpatialCalibration(cal)

   **Signature:** ``setSpatialCalibration(Calibration) -> void``

   **Parameters:**

   * **cal** (``Any``)

   **Returns:** ``None``


ProfileEntry
------------

.. method:: addPoint(point)

   **Signature:** ``addPoint(ShollPoint) -> void``

   **Parameters:**

   * **point** (``Any``)

   **Returns:** ``None``

.. method:: removePoint(point)

   **Signature:** ``removePoint(ShollPoint) -> void``

   **Parameters:**

   * **point** (``Any``)

   **Returns:** ``None``


RootDetector
------------

.. method:: setPercentileClip(percentileClip)

   **Signature:** ``setPercentileClip(double) -> void``

   **Parameters:**

   * **percentileClip** (``float``)

   **Returns:** ``None``

.. method:: setRadius(radius)

   **Signature:** ``setRadius(double) -> void``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``None``

.. method:: setWeightByThickness(weightByThickness)

   **Signature:** ``setWeightByThickness(boolean) -> void``

   **Parameters:**

   * **weightByThickness** (``bool``)

   **Returns:** ``None``


SNT
---

.. method:: addFillerThread(filler)

   **Signature:** ``addFillerThread(FillerThread) -> void``

   **Parameters:**

   * **filler** (``FillerThread``)

   **Returns:** ``None``

.. method:: addListener(listener)

   **Signature:** ``addListener(SNTListener) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: clearIsolatedTreeID()

   Convenience for `setIsolatedTreeID(-1)`: lifts any active tree isolation.

   **Signature:** ``clearIsolatedTreeID() -> void``

   **Returns:** ``None``

.. method:: disableEventsAllPanes(disable)

   Sets default path colors.

   **Signature:** ``disableEventsAllPanes(boolean) -> void``

   **Parameters:**

   * **disable** (``bool``): - new default color for selected paths

   **Returns:** ``None``

.. method:: disableZoomAllPanes(disable)

   **Signature:** ``disableZoomAllPanes(boolean) -> void``

   **Parameters:**

   * **disable** (``bool``)

   **Returns:** ``None``

.. method:: enableAstar(enable)

   Toggles the A* search algorithm (enabled by default)

   **Signature:** ``enableAstar(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - true to enable A* search, false otherwise

   **Returns:** ``None``

.. method:: enableSecondaryLayerTracing(enable)

   **Signature:** ``enableSecondaryLayerTracing(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``)

   **Returns:** ``None``

.. method:: enableSnapCursor(enable)

   Enables SNT's XYZ snap cursor feature. Does nothing if no image data is available or currently loaded image is binary

   **Signature:** ``enableSnapCursor(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - whether cursor snapping should be enabled

   **Returns:** ``None``

.. method:: removeMIPOverlayAllPanes()

   **Signature:** ``removeMIPOverlayAllPanes() -> void``

   **Returns:** ``None``

.. method:: setAnnotationsColorAllPanes(newColor)

   **Signature:** ``setAnnotationsColorAllPanes(Color) -> void``

   **Parameters:**

   * **newColor** (``Any``)

   **Returns:** ``None``

.. method:: setAnnotationsVisible(visible)

   Enables/Disables SNT overlays over tracing views. Note that disabling overlays will also suppress most GUI-related operations.

   **Signature:** ``setAnnotationsVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - whether overlays should be rendered

   **Returns:** ``None``

.. method:: setBatchRetraceChannelFrame(channel, frame)

   Sets or clears the channel/frame lock described in `getBatchRetraceChannelFrame()`.

   **Signature:** ``setBatchRetraceChannelFrame(Integer, Integer) -> void``

   **Parameters:**

   * **channel** (``int``): - 1-based channel, or null to clear the lock
   * **frame** (``int``)

   **Returns:** ``None``

.. method:: setCanvasLabelAllPanes(label)

   **Signature:** ``setCanvasLabelAllPanes(String) -> void``

   **Parameters:**

   * **label** (``str``)

   **Returns:** ``None``

.. method:: setChannelAndFrame(channel, frame)

   Sets the channel/frame (1-based, IJ hyperstack convention) to be associated with subsequently traced paths (via `Path.setCTposition(int, int)`), and, for 
```
manualTrace(sc.fiji.snt.util.SNTPoint, sc.fiji.snt.util.SNTPoint, sc.fiji.snt.util.PointInImage)
```
, with the pixel data A* search reads (see `setImageData(net.imglib2.RandomAccessibleInterval<?>)`).

Useful alongside `setImageData(net.imglib2.RandomAccessibleInterval<?>)`/`setImageMetadata(int, int, int, double, double, double, java.lang.String)` when pixel data comes from a source with no single, already-loaded multichannel/multi-timepoint array to index into (e.g. each channel of a BigDataViewer/SpimData or N5/Zarr source is its own separate object): callers are responsible for keeping the three in sync when the active channel/timepoint changes.

   **Signature:** ``setChannelAndFrame(int, int) -> void``

   **Parameters:**

   * **channel** (``int``): - the channel (1-based index; coerced to 1 if ≤0)
   * **frame** (``int``)

   **Returns:** ``None``

.. method:: setCostType(costType)

   **Signature:** ``setCostType(CostType) -> void``

   **Parameters:**

   * **costType** (``Any``)

   **Returns:** ``None``

.. method:: setCurrentPath(path)

   **Signature:** ``setCurrentPath(Path) -> void``

   **Parameters:**

   * **path** (``Path``)

   **Returns:** ``None``

.. method:: setCursorTextAllPanes(label)

   **Signature:** ``setCursorTextAllPanes(String) -> void``

   **Parameters:**

   * **label** (``str``)

   **Returns:** ``None``

.. method:: setDrawCrosshairsAllPanes(drawCrosshairs)

   **Signature:** ``setDrawCrosshairsAllPanes(boolean) -> void``

   **Parameters:**

   * **drawCrosshairs** (``bool``)

   **Returns:** ``None``

.. method:: setDrawDiameters(draw)

   **Signature:** ``setDrawDiameters(boolean) -> void``

   **Parameters:**

   * **draw** (``bool``)

   **Returns:** ``None``

.. method:: setFillList(fillList)

   **Signature:** ``setFillList(List) -> void``

   **Parameters:**

   * **fillList** (``List[Any]``)

   **Returns:** ``None``

.. method:: setFillThreshold(distance)

   Sets the fill threshold distance. Typically, this value is set before a filling operation as a starting value for the `FillerThread`.

   **Signature:** ``setFillThreshold(double) -> void``

   **Parameters:**

   * **distance** (``float``): - the new threshold distance. Set it to

   **Returns:** ``None``

.. method:: setFillThresholdFrom(world_x, world_y, world_z)

   **Signature:** ``setFillThresholdFrom(double, double, double) -> void``

   **Parameters:**

   * **world_x** (``float``)
   * **world_y** (``float``)
   * **world_z** (``float``)

   **Returns:** ``None``

.. method:: setFilterType(filterType)

   **Signature:** ``setFilterType(FilterType) -> void``

   **Parameters:**

   * **filterType** (``Any``)

   **Returns:** ``None``

.. method:: setHeuristicType(heuristicType)

   **Signature:** ``setHeuristicType(HeuristicType) -> void``

   **Parameters:**

   * **heuristicType** (``Any``)

   **Returns:** ``None``

.. method:: setImageData(data)

   Directly sets the image data backing A* search, without requiring an `ImgPlus` wrapper. Useful when pixel data comes from a source whose `RandomAccessibleInterval` is already resolved elsewhere (e.g., a BigDataViewer/SpimData `ImgLoader`, or a BDV/BVV `Source`), and building/discarding a full `ImgPlus` just to satisfy `SNT(ImgPlus)` would be wasteful, or would not preserve lazy/chunked access the way the original object does.

Callers remain responsible for also calling `setImageMetadata(int, int, int, double, double, double, java.lang.String)` (or equivalent) with matching dimensions/calibration; this method does not attempt to infer them from `data`.

`data`'s pixel type must be a `RealType`; other types (e.g. `ARGBType`) will throw a `ClassCastException` later, e.g., the first time A* search accesses a pixel.

   **Signature:** ``setImageData(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **data** (``Any``): - the (possibly lazily-backed) image data, in the same pixel/voxel grid implied by the dimensions/calibration set via setImageMetadata(int, int, int, double, double, double, java.lang.String)

   **Returns:** ``None``

.. method:: setImageMetadata(width, height, depth, xSpacing, ySpacing, zSpacing, units)

   Sets image dimensions and calibration without providing actual pixel data. Useful when the source image is not directly accessible as random-access data (e.g., a BigDataViewer `AbstractSpimData`/IMS source, or an ambiguous N5/Zarr layout) but its metadata (size, voxel spacing) is still known. This allows features that only need bounds/scale (e.g., manual tracing, bounds/distance checks) to work correctly with the image's real dimensions, even though `accessToValidImageData()` keeps reporting no data is available (this does NOT set `ctSlice3d`, so A* search remains unavailable).

   **Signature:** ``setImageMetadata(int, int, int, double, double, double, String) -> void``

   **Parameters:**

   * **width** (``int``): - width in pixels (ignored if ≤0)
   * **height** (``int``)
   * **depth** (``int``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)
   * **units** (``str``)

   **Returns:** ``None``

.. method:: setIsolatedTreeID(treeID)

   Isolates a single tree (arbor) for display across every tracing viewer, hiding paths belonging to any other tree. Orthogonal to `setShowOnlySelectedPaths(boolean)`: does not touch path selection or rendered colors, it only restricts which trees are candidates for display at all. Pass -1 (or call `clearIsolatedTreeID()`) to lift the restriction.

   **Signature:** ``setIsolatedTreeID(int) -> void``

   **Parameters:**

   * **treeID** (``int``): - the ID of the tree to isolate (see Tree.getTreeID()), or -1 to show all

   **Returns:** ``None``

.. method:: setPathList(justAdded, expandAll)

   **Signature:** ``setPathList(Path, boolean) -> void``

   **Parameters:**

   * **justAdded** (``Path``)
   * **expandAll** (``bool``)

   **Returns:** ``None``

.. method:: setSearchImageType(searchImageType)

   **Signature:** ``setSearchImageType(SearchImageType) -> void``

   **Parameters:**

   * **searchImageType** (``Any``)

   **Returns:** ``None``

.. method:: setSearchType(searchType)

   **Signature:** ``setSearchType(SearchType) -> void``

   **Parameters:**

   * **searchType** (``Any``)

   **Returns:** ``None``

.. method:: setSecondaryImage(file)

   Specifies the 'secondary image' to be used during a tracing session.

   **Signature:** ``setSecondaryImage(File) -> void``

   **Parameters:**

   * **file** (``str``): - The file containing the 'secondary image'

   **Returns:** ``None``

.. method:: setSecondaryImageMinMax(min, max)

   **Signature:** ``setSecondaryImageMinMax(double, double) -> void``

   **Parameters:**

   * **min** (``float``)
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setSelectedPaths(selectedPathsSet, source)

   **Signature:** ``setSelectedPaths(Collection, Object) -> void``

   **Parameters:**

   * **selectedPathsSet** (``List[Any]``)
   * **source** (``Any``)

   **Returns:** ``None``

.. method:: setShowOnlySelectedPaths(showOnlySelectedPaths)

   **Signature:** ``setShowOnlySelectedPaths(boolean) -> void``

   **Parameters:**

   * **showOnlySelectedPaths** (``bool``)

   **Returns:** ``None``

.. method:: setSinglePane(single_pane)

   **Signature:** ``setSinglePane(boolean) -> void``

   **Parameters:**

   * **single_pane** (``bool``)

   **Returns:** ``None``

.. method:: setStopFillAtThreshold(stopFillAtThreshold)

   **Signature:** ``setStopFillAtThreshold(boolean) -> void``

   **Parameters:**

   * **stopFillAtThreshold** (``bool``)

   **Returns:** ``None``

.. method:: setStoreExtraFillNodes(storeExtraFillNodes)

   **Signature:** ``setStoreExtraFillNodes(boolean) -> void``

   **Parameters:**

   * **storeExtraFillNodes** (``bool``)

   **Returns:** ``None``

.. method:: setTemporaryPath(path)

   **Signature:** ``setTemporaryPath(Path) -> void``

   **Parameters:**

   * **path** (``Path``)

   **Returns:** ``None``

.. method:: setUseSubVolumeStats(useSubVolumeStatistics)

   **Signature:** ``setUseSubVolumeStats(boolean) -> void``

   **Parameters:**

   * **useSubVolumeStatistics** (``bool``)

   **Returns:** ``None``

.. method:: setWorldOriginOffset(xOffset, yOffset, zOffset)

   Sets a rigid world-space origin offset (in calibrated units) to be applied on top of the usual `voxelIndex * spacing` coordinate mapping. Not needed for a normally-loaded `ImgPlus` (its calibration/origin is assumed anchored at world (0,0,0)), but required when pixel data was wired in via `setImageData(net.imglib2.RandomAccessibleInterval<?>)`/`setImageMetadata(int, int, int, double, double, double, java.lang.String)` from a source whose own coordinate frame is *not* anchored at (0,0,0) - e.g. a BigDataViewer/N5 `Source` whose `sourceTransform` carries a translation (see `BigDataLoaderCmd#applyFallbackCalibration`).

This offset is not applied automatically to coordinates read elsewhere in this class (e.g. manual tracing, A* search); callers that produce `Tree`/`Path` results from such a source are responsible for applying it themselves, e.g. via `Tree.translate(double, double, double)`.

**Not the same thing as `ij.measure.Calibration#xOrigin/yOrigin/zOrigin`** (nor a drop-in replacement for it), despite the similar name/purpose. The two use different conventions and are not numerically interchangeable:

- This offset is applied in **world** space, after scaling: `world = voxelIndex * spacing + offset` .

- `Calibration` 's origin is applied in **pixel** space, before scaling (see `Calibration#getRawX/Y/Z` , and `ShollPoint#rawZ` for the equivalent hand-written formula): `world = (voxelIndex - origin) * spacing` , i.e. `voxelIndex = world / spacing + origin` .

Converting between the two requires the spacing too (`offset = -origin * spacing`); they are not the same number and must not be assigned to/read from each other directly. `getCalibration()` always returns spacing-only calibration objects with `xOrigin/yOrigin/zOrigin` left at their default of 0, regardless of this offset; callers needing pixel<->world conversions that account for this offset must use `getWorldOriginOffset()` directly (see `BookmarkManager#pixelToWorld`/ `#worldToPixel` for a worked example), not `getCalibration()` alone.

   **Signature:** ``setWorldOriginOffset(double, double, double) -> void``

   **Parameters:**

   * **xOffset** (``float``): - x offset, in calibrated units
   * **yOffset** (``float``)
   * **zOffset** (``float``)

   **Returns:** ``None``

.. method:: setZPositionAllPanes(new_x, new_y, new_z)

   **Signature:** ``setZPositionAllPanes(int, int, int) -> void``

   **Parameters:**

   * **new_x** (``int``)
   * **new_y** (``int``)
   * **new_z** (``int``)

   **Returns:** ``None``


SNTChart
--------

.. method:: addColorBarLegend(title, colorTable, min, max, nDecimalPlaces)

   Adds a color bar legend (LUT ramp).

   **Signature:** ``addColorBarLegend(String, ColorTable, double, double, int) -> void``

   **Parameters:**

   * **title** (``str``): - the color bar label
   * **colorTable** (``Any``)
   * **min** (``float``)
   * **max** (``float``)
   * **nDecimalPlaces** (``int``)

   **Returns:** ``None``

.. method:: addPolygon(poly, lineColor, fillColor)

   **Signature:** ``addPolygon(Polygon2D, ColorRGB, ColorRGB) -> void``

   **Parameters:**

   * **poly** (``Any``)
   * **lineColor** (``Any``)
   * **fillColor** (``Any``)

   **Returns:** ``None``

.. method:: setAxesVisible(visible)

   Sets the visibility of chart axes.

Controls whether the domain (X) and range (Y) axes are visible in the chart. This affects both XY plots and category plots.

   **Signature:** ``setAxesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - true to show axes, false to hide them

   **Returns:** ``None``

.. method:: setChartTitle(title)

   **Signature:** ``setChartTitle(String) -> void``

   **Parameters:**

   * **title** (``str``)

   **Returns:** ``None``

.. method:: setColors(colorTable)

   (Re)colors existing dataset series. Unlike `setColors(String...)`, only the series fill is touched: outline/item-label paint is left alone, since e.g. histogram bars rely on a fixed black/white outline (set independently of series color, see `AnalysisUtils`) for the margin between adjacent bars

   **Signature:** ``setColors(ColorTable) -> void``

   **Parameters:**

   * **colorTable** (``Any``): - the series colors, one per series (extra series, if any, are left unchanged)

   **Returns:** ``None``

.. method:: setDefaultFontScale(scalingFactor)

   **Signature:** ``setDefaultFontScale(double) -> void``

   **Parameters:**

   * **scalingFactor** (``float``)

   **Returns:** ``None``

.. method:: setEqualizeAxes(equalize)

   Sets whether the axes of the underlying XY plot should be equalized (same scale).

When enabled, both X and Y axes will use the same scale to maintain equal aspect ratio. When disabled, each axis maximizes its range.

   **Signature:** ``setEqualizeAxes(boolean) -> void``

   **Parameters:**

   * **equalize** (``bool``): - true to equalize axes, false otherwise

   **Returns:** ``None``

.. method:: setGMMFitVisible(visible)

   Sets whether a GMM distribution curve should be overlaid over histogram frequencies.

   **Signature:** ``setGMMFitVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - whether curve should be displayed. Ignored if current chart is not a histogram

   **Returns:** ``None``

.. method:: setGaussianFitVisible(visible)

   Sets whether a normal distribution curve should be overlaid over histogram frequencies.

   **Signature:** ``setGaussianFitVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - whether curve should be displayed. Ignored if current chart is not a histogram

   **Returns:** ``None``

.. method:: setGridlinesVisible(visible)

   **Signature:** ``setGridlinesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setLegendVisible(visible)

   **Signature:** ``setLegendVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setLineWidth(width)

   Changes the line width of all series in a XY plot

   **Signature:** ``setLineWidth(int) -> void``

   **Parameters:**

   * **width** (``int``): - the stroke width

   **Returns:** ``None``

.. method:: setOutlineVisible(visible)

   Sets the visibility of the plot outline.

Controls whether the border outline around the plot area is visible.

   **Signature:** ``setOutlineVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - true to show outline, false to hide it

   **Returns:** ``None``

.. method:: setQuartilesVisible(visible)

   Sets whether quartile markers (Q1, Median, Q3) should be overlaid over histogram frequencies.

   **Signature:** ``setQuartilesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``): - whether markers should be displayed. Ignored if current chart is not a histogram

   **Returns:** ``None``

.. method:: setTitle(title)

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``)

   **Returns:** ``None``


SNTColor
--------

.. method:: setAWTColor(color)

   Re-assigns an AWT color.

   **Signature:** ``setAWTColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``): - the new color

   **Returns:** ``None``

.. method:: setSWCType(swcType)

   Re-assigns a SWC type integer flag

   **Signature:** ``setSWCType(int) -> void``

   **Parameters:**

   * **swcType** (``int``): - the new SWC type

   **Returns:** ``None``


SNTGraph
--------

.. method:: setEdgeColor(edge, color)

   **Signature:** ``setEdgeColor(DefaultWeightedEdge, ColorRGB) -> void``

   **Parameters:**

   * **edge** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setVertexColor(vertex, color)

   **Signature:** ``setVertexColor(Object, ColorRGB) -> void``

   **Parameters:**

   * **vertex** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setVertexValue(vertex, value)

   **Signature:** ``setVertexValue(Object, double) -> void``

   **Parameters:**

   * **vertex** (``Any``)
   * **value** (``float``)

   **Returns:** ``None``


SNTPoint
--------

.. method:: setAnnotation(annotation)

   Assigns a neuropil annotation (e.g., atlas compartment) to this point.

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **annotation** (``Any``): - the annotation to be assigned to this point

   **Returns:** ``None``

.. method:: setHemisphere(lr)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **lr** (``str``)

   **Returns:** ``None``


SNTPrefs
--------

.. method:: clearAll()

   **Signature:** ``clearAll() -> void``

   **Returns:** ``None``

.. method:: clearBvvPrefs()

   Restores the defaults of all BVV preferences

   **Signature:** ``clearBvvPrefs() -> void``

   **Returns:** ``None``

.. method:: setAutoLoadToolbarButton(autoLoad)

   Sets whether the SNT button should be auto-installed in the IJ toolbar at Fiji startup.

   **Signature:** ``setAutoLoadToolbarButton(boolean) -> void``

   **Parameters:**

   * **autoLoad** (``bool``): - the new preference

   **Returns:** ``None``

.. method:: setAutoSelectionOfFinishedPath(activateFinishedPath)

   **Signature:** ``setAutoSelectionOfFinishedPath(boolean) -> void``

   **Parameters:**

   * **activateFinishedPath** (``bool``)

   **Returns:** ``None``

.. method:: setAutosaveFile(file)

   **Signature:** ``setAutosaveFile(File) -> void``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``None``

.. method:: setBvvCacheMB(mb)

   **Signature:** ``setBvvCacheMB(int) -> void``

   **Parameters:**

   * **mb** (``int``): - the BVV GPU tile cache size (MB) to persist. 0 means automatic

   **Returns:** ``None``

.. method:: setBvvCachePromptSuppressed(suppress)

   **Signature:** ``setBvvCachePromptSuppressed(boolean) -> void``

   **Parameters:**

   * **suppress** (``bool``)

   **Returns:** ``None``

.. method:: setBvvFetchers(n)

   **Signature:** ``setBvvFetchers(int) -> void``

   **Parameters:**

   * **n** (``int``): - the number of BVV tile fetcher threads to persist. 0 means automatic

   **Returns:** ``None``

.. method:: setBvvMaxStep(step)

   **Signature:** ``setBvvMaxStep(double) -> void``

   **Parameters:**

   * **step** (``float``)

   **Returns:** ``None``

.. method:: setBvvRenderQuality(name)

   **Signature:** ``setBvvRenderQuality(String) -> void``

   **Parameters:**

   * **name** (``str``): - the name of the BVV render quality preset to persist, or null to restore the default

   **Returns:** ``None``

.. method:: setCanvasAutoActivation(enable)

   **Signature:** ``setCanvasAutoActivation(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``)

   **Returns:** ``None``

.. method:: setDeselectedPathColor(color)

   **Signature:** ``setDeselectedPathColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setDisplayCustomPathColors(displayCustomPathColors)

   **Signature:** ``setDisplayCustomPathColors(boolean) -> void``

   **Parameters:**

   * **displayCustomPathColors** (``bool``)

   **Returns:** ``None``

.. method:: setFastCropMaterialization(enable)

   **Signature:** ``setFastCropMaterialization(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - see isFastCropMaterializationEnabled()

   **Returns:** ``None``

.. method:: setLastKnownDir(file)

   **Signature:** ``setLastKnownDir(File) -> void``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``None``

.. method:: setLookAndFeel(laf)

   Sets the look and feel preference.

   **Signature:** ``setLookAndFeel(String) -> void``

   **Parameters:**

   * **laf** (``str``): - the look and feel class name

   **Returns:** ``None``

.. method:: setNextImgExtensions(extensions)

   Convenience method for setting filename suffixes from a comma-separated string. Whitespace around entries is trimmed and blank entries are ignored. Delegates to `setNextImgExtensions(List)`.

   **Signature:** ``setNextImgExtensions(List) -> void``

   **Parameters:**

   * **extensions** (``List[Any]``): - a comma-separated string of filename suffixes (e.g.,

   **Returns:** ``None``

.. method:: setRecentDir(file)

   **Signature:** ``setRecentDir(File) -> void``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``None``

.. method:: setRequireShiftToFork(requireShiftToFork)

   **Signature:** ``setRequireShiftToFork(boolean) -> void``

   **Parameters:**

   * **requireShiftToFork** (``bool``)

   **Returns:** ``None``

.. method:: setSaveCompressedTraces(bool)

   Sets whether to save traces in compressed format.

   **Signature:** ``setSaveCompressedTraces(boolean) -> void``

   **Parameters:**

   * **bool** (``bool``): - true to enable compressed traces, false otherwise

   **Returns:** ``None``

.. method:: setSaveWinLocations(value)

   Sets whether window locations should be saved and restored.

   **Signature:** ``setSaveWinLocations(boolean) -> void``

   **Parameters:**

   * **value** (``bool``): - true to save window locations, false otherwise

   **Returns:** ``None``

.. method:: setScrollDiameterEnabled(enable)

   **Signature:** ``setScrollDiameterEnabled(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``)

   **Returns:** ``None``

.. method:: setSelectedPathColor(color)

   **Signature:** ``setSelectedPathColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setSomaDisplayTriangle(bool)

   Sets whether single-node paths tagged as soma should render w/ triangular shape.

   **Signature:** ``setSomaDisplayTriangle(boolean) -> void``

   **Parameters:**

   * **bool** (``bool``): - true to enable triangular shape, false for default representation

   **Returns:** ``None``

.. method:: setTemp(key, value)

   Sets a temporary string preference value that will be cleared at session end.

   **Signature:** ``setTemp(String, String) -> void``

   **Parameters:**

   * **key** (``str``): - the preference key
   * **value** (``str``)

   **Returns:** ``None``

.. method:: setThreads(n)

   Sets the number of threads to use for multi-threaded operations.

   **Signature:** ``setThreads(int) -> void``

   **Parameters:**

   * **n** (``int``): - the number of threads (if less than 1, uses available processors)

   **Returns:** ``None``

.. method:: setUseNativeFileChooser(useNative)

   Sets whether SNT's simple open/save dialogs should use native OS file dialogs.

   **Signature:** ``setUseNativeFileChooser(boolean) -> void``

   **Parameters:**

   * **useNative** (``bool``): - the new preference

   **Returns:** ``None``

.. method:: setWorkspaceDir(dir)

   **Signature:** ``setWorkspaceDir(File) -> void``

   **Parameters:**

   * **dir** (``str``)

   **Returns:** ``None``


SNTTable
--------

.. method:: addColumn(colHeader, array)

   **Signature:** ``addColumn(String, Collection) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **array** (``List[Any]``)

   **Returns:** ``None``

.. method:: addGenericColumn(colHeader, collection)

   **Signature:** ``addGenericColumn(String, Collection) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **collection** (``List[Any]``)

   **Returns:** ``None``

.. method:: removeColumn(header)

   **Signature:** ``removeColumn(String) -> Column``

   **Parameters:**

   * **header** (``str``)

   **Returns:** ``Any``

.. method:: removeSummary()

   Removes summary statistics from the table.

If the table contains summary statistics, this method removes the summary rows to return the table to its raw data state.

   **Signature:** ``removeSummary() -> void``

   **Returns:** ``None``

.. method:: setContext(context)

   Sets a SciJava context to this table.

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **context** (``Any``): - the SciJava application context

   **Returns:** ``None``

.. method:: setTitle(title)

   Sets the title of the table.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``): - the table's title

   **Returns:** ``None``


SNTUI
-----

.. method:: setBdv(bdv)

   Registers (or clears, if `bdv` is null) the `Bdv` instance tethered to this UI.

   **Signature:** ``setBdv(Bdv) -> void``

   **Parameters:**

   * **bdv** (``Bdv``): - the Bdv instance to tether, or null to detach

   **Returns:** ``None``

.. method:: setBvv(bvv)

   Registers (or clears, if `bvv` is null) the `Bvv` instance tethered to this UI.

   **Signature:** ``setBvv(Bvv) -> void``

   **Parameters:**

   * **bvv** (``Bvv``): - the Bvv instance to tether, or null to detach

   **Returns:** ``None``

.. method:: setEnableDebugMode(enable)

   Enables/disables debug mode

   **Signature:** ``setEnableDebugMode(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - true to enable debug mode, otherwise false

   **Returns:** ``None``

.. method:: setLookAndFeel(lookAndFeelName)

   **Signature:** ``setLookAndFeel(String) -> void``

   **Parameters:**

   * **lookAndFeelName** (``str``)

   **Returns:** ``None``

.. method:: setRenderingScale(scale)

   Sets rendering scale of Paths as per respective widget in dialog.

   **Signature:** ``setRenderingScale(double) -> void``

   **Parameters:**

   * **scale** (``float``): - the scale value (-1 for default scale)

   **Returns:** ``None``

.. method:: setSigmaPaletteListener(listener)

   **Signature:** ``setSigmaPaletteListener(SigmaPaletteListener) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: setVisibilityFilter(filter, state)

   Sets filters for visibility of paths, as per respective widget in dialog.

   **Signature:** ``setVisibilityFilter(String, boolean) -> void``

   **Parameters:**

   * **filter** (``str``): - a reference to the visibility filter checkbox. Either the checkbox complete label or relevant keyword, e.g., "selected", "Z-slices", "channel", etc. "all" can also be used to toggle all checkboxes in the widget
   * **state** (``bool``)

   **Returns:** ``None``


SNTUtils
--------

.. method:: addViewer(viewer)

   **Signature:** ``addViewer(Viewer3D) -> void``

   **Parameters:**

   * **viewer** (``Viewer3D``)

   **Returns:** ``None``

.. method:: removeViewer(viewer)

   **Signature:** ``removeViewer(Viewer3D) -> void``

   **Parameters:**

   * **viewer** (``Viewer3D``)

   **Returns:** ``None``

.. method:: setContext(context)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **context** (``Any``)

   **Returns:** ``None``

.. method:: setDebugMode(b)

   Enables/disables debug mode

   **Signature:** ``setDebugMode(boolean) -> void``

   **Parameters:**

   * **b** (``bool``): - verbose flag

   **Returns:** ``None``

.. method:: setIsLoading(isLoading, streamMode)

   Shows or hides the loading splash screen. Calls nest safely: several independent call chains can be "loading" at once, so the splash only actually closes once every `true` has been balanced by a matching `false`, hence calls should be made in a try/finally block.

   **Signature:** ``setIsLoading(boolean, boolean) -> void``

   **Parameters:**

   * **isLoading** (``bool``): - true to show the splash screen (or register one more caller that wants it showing, if already showing); false to release one such registration, closing the splash once no callers still hold it
   * **streamMode** (``bool``)

   **Returns:** ``None``


SWCPoint
--------

.. method:: setAnnotation(annotation)

   Description copied from interface: `SNTPoint`

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **annotation** (``Any``): - the annotation to be assigned to this point

   **Returns:** ``None``

.. method:: setColor(color)

   Sets the color of this point.

   **Signature:** ``setColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``): - the color to set

   **Returns:** ``None``

.. method:: setHemisphere(lr)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **lr** (``str``)

   **Returns:** ``None``

.. method:: setPath(onPath)

   **Signature:** ``setPath(Path) -> void``

   **Parameters:**

   * **onPath** (``Path``)

   **Returns:** ``None``

.. method:: setPrevious(previousNode)

   Sets the preceding node in the reconstruction

   **Signature:** ``setPrevious(SWCPoint) -> void``

   **Parameters:**

   * **previousNode** (``SWCPoint``): - the previous node preceding this one

   **Returns:** ``None``

.. method:: setTags(tags)

   Sets the tags associated with this point.

   **Signature:** ``setTags(String) -> void``

   **Parameters:**

   * **tags** (``str``): - the tags string

   **Returns:** ``None``


SearchThread
------------

.. method:: addNode(n, fromStart)

   **Signature:** ``addNode(DefaultSearchNode, boolean) -> void``

   **Parameters:**

   * **n** (``DefaultSearchNode``)
   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: addProgressListener(callback)

   Description copied from class: `AbstractSearch`

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **callback** (``Any``): - the callback to register

   **Returns:** ``None``


SearchThreadArtist
------------------

.. method:: setClosedColor(color)

   **Signature:** ``setClosedColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setDrawingThreshold(threshold)

   **Signature:** ``setDrawingThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setOpenColor(color)

   **Signature:** ``setOpenColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``


SeedOverlay
-----------

.. method:: addAll(batch)

   **Signature:** ``addAll(Collection) -> void``

   **Parameters:**

   * **batch** (``List[Any]``)

   **Returns:** ``None``

.. method:: addListener(listener)

   **Signature:** ``addListener(SeedOverlayListener) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: clearSelection()

   **Signature:** ``clearSelection() -> void``

   **Returns:** ``None``

.. method:: removeAll(batch)

   **Signature:** ``removeAll(Collection) -> int``

   **Parameters:**

   * **batch** (``List[Any]``)

   **Returns:** ``int``

.. method:: removeAt(index)

   **Signature:** ``removeAt(int) -> SeedPoint``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``SeedPoint``

.. method:: removeListener(listener)

   **Signature:** ``removeListener(SeedOverlayListener) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: removeSelected()

   **Signature:** ``removeSelected() -> int``

   **Returns:** ``int``

.. method:: setColorMode(mode)

   **Signature:** ``setColorMode(ColorMode) -> void``

   **Parameters:**

   * **mode** (``Any``)

   **Returns:** ``None``

.. method:: setColorTable(name)

   **Signature:** ``setColorTable(String) -> void``

   **Parameters:**

   * **name** (``str``)

   **Returns:** ``None``

.. method:: setConfidenceRange(low, high)

   **Signature:** ``setConfidenceRange(double, double) -> void``

   **Parameters:**

   * **low** (``float``)
   * **high** (``float``)

   **Returns:** ``None``

.. method:: setSelectedSeeds(selection)

   **Signature:** ``setSelectedSeeds(Collection) -> void``

   **Parameters:**

   * **selection** (``List[Any]``)

   **Returns:** ``None``

.. method:: setTransparency(t)

   **Signature:** ``setTransparency(double) -> void``

   **Parameters:**

   * **t** (``float``)

   **Returns:** ``None``

.. method:: setUnknownConfidenceColor(color)

   **Signature:** ``setUnknownConfidenceColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setVisible(visible)

   **Signature:** ``setVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``


SeedPoint
---------

.. method:: setAnnotation(annotation)

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **annotation** (``Any``)

   **Returns:** ``None``

.. method:: setHemisphere(lr)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **lr** (``str``)

   **Returns:** ``None``


ShollAnalyzer
-------------

.. method:: setEnableCurveFitting(enable)

   Sets whether curve fitting computations should be performed.

   **Signature:** ``setEnableCurveFitting(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - if

   **Returns:** ``None``

.. method:: setPolynomialFitRange(fromDegree, toDegree)

   Sets the polynomial fit range for linear Sholl statistics.

   **Signature:** ``setPolynomialFitRange(int, int) -> void``

   **Parameters:**

   * **fromDegree** (``int``): - the lowest degree to be considered. Set it to -1 to skip polynomial fit
   * **toDegree** (``int``)

   **Returns:** ``None``


ShollOverlay
------------

.. method:: addCenter()

   **Signature:** ``addCenter() -> void``

   **Returns:** ``None``

.. method:: removePoints()

   **Signature:** ``removePoints() -> void``

   **Returns:** ``None``

.. method:: removeShells()

   **Signature:** ``removeShells() -> void``

   **Returns:** ``None``

.. method:: removeShollROIs(overlay)

   **Signature:** ``removeShollROIs(Overlay) -> void``

   **Parameters:**

   * **overlay** (``Any``)

   **Returns:** ``None``

.. method:: setAlternateShells()

   **Signature:** ``setAlternateShells() -> void``

   **Returns:** ``None``

.. method:: setBaseColor(baseColor)

   **Signature:** ``setBaseColor(Color) -> void``

   **Parameters:**

   * **baseColor** (``Any``)

   **Returns:** ``None``

.. method:: setGradientShells(color1, color2)

   **Signature:** ``setGradientShells(Color, Color) -> void``

   **Parameters:**

   * **color1** (``Any``)
   * **color2** (``Any``)

   **Returns:** ``None``

.. method:: setPointsColor(color)

   **Signature:** ``setPointsColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setPointsLUT(lutName)

   **Signature:** ``setPointsLUT(String) -> void``

   **Parameters:**

   * **lutName** (``str``)

   **Returns:** ``None``

.. method:: setPointsOpacity(percent)

   **Signature:** ``setPointsOpacity(double) -> void``

   **Parameters:**

   * **percent** (``float``)

   **Returns:** ``None``

.. method:: setShellsColor(color)

   **Signature:** ``setShellsColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setShellsLUT(lutName)

   **Signature:** ``setShellsLUT(String) -> void``

   **Parameters:**

   * **lutName** (``str``)

   **Returns:** ``None``

.. method:: setShellsOpacity(percent)

   **Signature:** ``setShellsOpacity(double) -> void``

   **Parameters:**

   * **percent** (``float``)

   **Returns:** ``None``

.. method:: setShellsThickness(strokeWidth)

   **Signature:** ``setShellsThickness(int) -> void``

   **Parameters:**

   * **strokeWidth** (``int``)

   **Returns:** ``None``


ShollPlot
---------

.. method:: addPoints(points, label)

   **Signature:** ``addPoints(List, String) -> void``

   **Parameters:**

   * **points** (``List[Any]``)
   * **label** (``str``)

   **Returns:** ``None``

.. method:: enableLegend(enable)

   **Signature:** ``enableLegend(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``)

   **Returns:** ``None``


ShollStats
----------

.. method:: setDataMode(mode)

   **Signature:** ``setDataMode(DataMode) -> void``

   **Parameters:**

   * **mode** (``Any``)

   **Returns:** ``None``


ShollTable
----------

.. method:: addColumn(colHeader, array)

   **Signature:** ``addColumn(String, Collection) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **array** (``List[Any]``)

   **Returns:** ``None``

.. method:: addGenericColumn(colHeader, collection)

   **Signature:** ``addGenericColumn(String, Collection) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **collection** (``List[Any]``)

   **Returns:** ``None``

.. method:: removeColumn(header)

   **Signature:** ``removeColumn(String) -> Column``

   **Parameters:**

   * **header** (``str``)

   **Returns:** ``Any``

.. method:: removeSummary()

   **Signature:** ``removeSummary() -> void``

   **Returns:** ``None``

.. method:: setContext(context)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **context** (``Any``)

   **Returns:** ``None``

.. method:: setDetailedSummary(detailed)

   **Signature:** ``setDetailedSummary(boolean) -> void``

   **Parameters:**

   * **detailed** (``bool``)

   **Returns:** ``None``

.. method:: setTitle(title)

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``)

   **Returns:** ``None``


SparseGWDTTracer
----------------

.. method:: setAllowVoxelGap(allow)

   **Signature:** ``setAllowVoxelGap(boolean) -> void``

   **Parameters:**

   * **allow** (``bool``)

   **Returns:** ``None``

.. method:: setAutoFilter(enabled)

   **Signature:** ``setAutoFilter(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setBackgroundThreshold(threshold)

   **Signature:** ``setBackgroundThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setBranchTuneMaxAngle(maxAngleDeg)

   **Signature:** ``setBranchTuneMaxAngle(double) -> void``

   **Parameters:**

   * **maxAngleDeg** (``float``)

   **Returns:** ``None``

.. method:: setCaliperFraction(fraction)

   **Signature:** ``setCaliperFraction(double) -> void``

   **Parameters:**

   * **fraction** (``float``)

   **Returns:** ``None``

.. method:: setConnectivityType(type)

   **Signature:** ``setConnectivityType(int) -> void``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``None``

.. method:: setJointLeafPruneEnabled(enabled)

   **Signature:** ``setJointLeafPruneEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setLeafPruneOverlap(threshold)

   **Signature:** ``setLeafPruneOverlap(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setMaxGapVoxels(maxVoxels)

   **Signature:** ``setMaxGapVoxels(int) -> void``

   **Parameters:**

   * **maxVoxels** (``int``)

   **Returns:** ``None``

.. method:: setMinSegmentLengthVoxels(lengthInVoxels)

   **Signature:** ``setMinSegmentLengthVoxels(double) -> void``

   **Parameters:**

   * **lengthInVoxels** (``float``)

   **Returns:** ``None``

.. method:: setMinSomaDistance(distance)

   **Signature:** ``setMinSomaDistance(double) -> void``

   **Parameters:**

   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setNSomas(nSomas)

   **Signature:** ``setNSomas(int) -> void``

   **Parameters:**

   * **nSomas** (``int``)

   **Returns:** ``None``

.. method:: setOvershootRemovalEnabled(enabled)

   **Signature:** ``setOvershootRemovalEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setParallelBranchPruneEnabled(enabled)

   **Signature:** ``setParallelBranchPruneEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setPathFittingEnabled(enabled)

   **Signature:** ``setPathFittingEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setResampleStep(step)

   **Signature:** ``setResampleStep(double) -> void``

   **Parameters:**

   * **step** (``float``)

   **Returns:** ``None``

.. method:: setRoots(seeds)

   **Signature:** ``setRoots(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setScoreMap(map)

   **Signature:** ``setScoreMap(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **map** (``Any``)

   **Returns:** ``None``

.. method:: setScoreMapEnabled(enabled)

   **Signature:** ``setScoreMapEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: setScoreMapFilterType(type)

   **Signature:** ``setScoreMapFilterType(FilterType) -> void``

   **Parameters:**

   * **type** (``Any``)

   **Returns:** ``None``

.. method:: setScoreMapPruneThreshold(threshold)

   **Signature:** ``setScoreMapPruneThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setScoreMapScales(scales)

   **Signature:** ``setScoreMapScales(double[]) -> void``

   **Parameters:**

   * **scales** (``List[float]``)

   **Returns:** ``None``

.. method:: setSeed(voxelCoords)

   **Signature:** ``setSeed(long[]) -> void``

   **Parameters:**

   * **voxelCoords** (``List[int]``)

   **Returns:** ``None``

.. method:: setSeedPhysical(physicalCoords)

   **Signature:** ``setSeedPhysical(double[]) -> void``

   **Parameters:**

   * **physicalCoords** (``List[float]``)

   **Returns:** ``None``

.. method:: setSomaRoi(roi)

   **Signature:** ``setSomaRoi(Roi) -> void``

   **Parameters:**

   * **roi** (``Any``)

   **Returns:** ``None``

.. method:: setSomaRoiZPosition(z)

   **Signature:** ``setSomaRoiZPosition(int) -> void``

   **Parameters:**

   * **z** (``int``)

   **Returns:** ``None``

.. method:: setSphereOverlapThreshold(threshold)

   **Signature:** ``setSphereOverlapThreshold(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setSrRatio(ratio)

   **Signature:** ``setSrRatio(double) -> void``

   **Parameters:**

   * **ratio** (``float``)

   **Returns:** ``None``

.. method:: setStatusListener(listener)

   **Signature:** ``setStatusListener(Consumer) -> void``

   **Parameters:**

   * **listener** (``Any``)

   **Returns:** ``None``

.. method:: setTipExtensionDistance(distance)

   **Signature:** ``setTipExtensionDistance(double) -> void``

   **Parameters:**

   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setTips(seeds)

   **Signature:** ``setTips(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setTracedRegionBuffer(buffer)

   **Signature:** ``setTracedRegionBuffer(int) -> void``

   **Parameters:**

   * **buffer** (``int``)

   **Returns:** ``None``

.. method:: setVerbose(verbose)

   **Signature:** ``setVerbose(boolean) -> void``

   **Parameters:**

   * **verbose** (``bool``)

   **Returns:** ``None``

.. method:: setWaypointBiasFixedFactor(factor)

   **Signature:** ``setWaypointBiasFixedFactor(double) -> void``

   **Parameters:**

   * **factor** (``float``)

   **Returns:** ``None``

.. method:: setWaypointBiasRadiusVoxels(radius)

   **Signature:** ``setWaypointBiasRadiusVoxels(double) -> void``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``None``

.. method:: setWaypointBiasSource(source)

   **Signature:** ``setWaypointBiasSource(WaypointBiasSource) -> void``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``None``

.. method:: setWaypointBiasStrength(strength)

   **Signature:** ``setWaypointBiasStrength(double) -> void``

   **Parameters:**

   * **strength** (``float``)

   **Returns:** ``None``

.. method:: setWaypoints(seeds)

   **Signature:** ``setWaypoints(Collection) -> void``

   **Parameters:**

   * **seeds** (``List[Any]``)

   **Returns:** ``None``

.. method:: setZigzagRemovalEnabled(enabled)

   **Signature:** ``setZigzagRemovalEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``


SparseStorageBackend
--------------------

.. method:: setConnectivityType(type)

   **Signature:** ``setConnectivityType(int) -> void``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``None``

.. method:: setDistance(index, distance)

   **Signature:** ``setDistance(long, double) -> void``

   **Parameters:**

   * **index** (``int``)
   * **distance** (``float``)

   **Returns:** ``None``

.. method:: setGWDT(index, value)

   **Signature:** ``setGWDT(long, double) -> void``

   **Parameters:**

   * **index** (``int``)
   * **value** (``float``)

   **Returns:** ``None``

.. method:: setParent(index, parentIndex)

   **Signature:** ``setParent(long, long) -> void``

   **Parameters:**

   * **index** (``int``)
   * **parentIndex** (``int``)

   **Returns:** ``None``

.. method:: setState(index, stateValue)

   **Signature:** ``setState(long, byte) -> void``

   **Parameters:**

   * **index** (``int``)
   * **stateValue** (``int``)

   **Returns:** ``None``

.. method:: setTrackAliveIndices(track)

   **Signature:** ``setTrackAliveIndices(boolean) -> void``

   **Parameters:**

   * **track** (``bool``)

   **Returns:** ``None``


TracerCanvas
------------

.. method:: disableEvents(disable)

   Sets the baseline for rendering diameter of path nodes

   **Signature:** ``disableEvents(boolean) -> void``

   **Parameters:**

   * **disable** (``bool``): - the diameter to be used when rendering path nodes. Set it to -1 for adopting the default value. Set it to zero to suppress node rendering

   **Returns:** ``None``

.. method:: setAnnotationsColor(color)

   **Signature:** ``setAnnotationsColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setCanvasLabel(label)

   **Signature:** ``setCanvasLabel(String) -> void``

   **Parameters:**

   * **label** (``str``)

   **Returns:** ``None``

.. method:: setCrosshairs(x, y, z, display)

   **Signature:** ``setCrosshairs(double, double, double, boolean) -> void``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)
   * **display** (``bool``)

   **Returns:** ``None``

.. method:: setCursorText(cursorText)

   **Signature:** ``setCursorText(String) -> void``

   **Parameters:**

   * **cursorText** (``str``)

   **Returns:** ``None``

.. method:: setDrawCrosshairs(drawCrosshairs)

   **Signature:** ``setDrawCrosshairs(boolean) -> void``

   **Parameters:**

   * **drawCrosshairs** (``bool``)

   **Returns:** ``None``

.. method:: setLabelForegroundColor(color)

   **Signature:** ``setLabelForegroundColor(Color) -> void``

   **Parameters:**

   * **color** (``Any``)

   **Returns:** ``None``


TracerThread
------------

.. method:: addNode(n, fromStart)

   **Signature:** ``addNode(DefaultSearchNode, boolean) -> void``

   **Parameters:**

   * **n** (``DefaultSearchNode``)
   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: addProgressListener(callback)

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **callback** (``Any``)

   **Returns:** ``None``


Tree
----

.. method:: setBoundingBox(box)

   Associates a bounding box to this tree.

   **Signature:** ``setBoundingBox(BoundingBox) -> void``

   **Parameters:**

   * **box** (``BoundingBox``): - the BoundingBox, typically referring to the image associated with this tree

   **Returns:** ``None``

.. method:: setColor(color)

   Assigns a color to all the paths in this tree. Note that assigning a non-null color will remove node colors from Paths.

   **Signature:** ``setColor(ColorRGB) -> void``

   **Parameters:**

   * **color** (``Any``): - the color to be applied, either a 1) HTML color codes starting with hash (

   **Returns:** ``None``

.. method:: setLabel(label)

   Sets an identifying label for this Tree.

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **label** (``str``): - the identifying string

   **Returns:** ``None``

.. method:: setRadii(r)

   Assigns a fixed radius to all the nodes in this tree.

   **Signature:** ``setRadii(double) -> void``

   **Parameters:**

   * **r** (``float``): - the radius to be assigned. Setting it to 0 or Double.NaN removes the radius attribute from the Tree

   **Returns:** ``None``

.. method:: setSWCType(type)

   Assigns an SWC type label to all the Paths in this Tree.

   **Signature:** ``setSWCType(String) -> void``

   **Parameters:**

   * **type** (``str``): - the SWC type (e.g., "soma", "axon", "(basal) dendrite", "apical dendrite", etc.)

   **Returns:** ``None``

.. method:: setType(type)

   Assigns an SWC type label to all the Paths in this Tree.

   **Signature:** ``setType(int) -> void``

   **Parameters:**

   * **type** (``int``): - the SWC type (e.g., Path.SWC_AXON, Path.SWC_DENDRITE, etc.)

   **Returns:** ``None``


TreeColorMapper
---------------

.. method:: setMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinMax(min, max)

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **min** (``float``)
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setMinMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMinMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinPercentileClipped(values, clipPercent)

   **Signature:** ``setMinPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(nanColor)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **nanColor** (``Any``)

   **Returns:** ``None``


TreeParser
----------

.. method:: setCenter(center)

   **Signature:** ``setCenter(PointInImage) -> void``

   **Parameters:**

   * **center** (``PointInImage``)

   **Returns:** ``None``

.. method:: setIntersectedVolumeAsExtraMeasurement(b)

   **Signature:** ``setIntersectedVolumeAsExtraMeasurement(boolean) -> void``

   **Parameters:**

   * **b** (``bool``)

   **Returns:** ``None``

.. method:: setSkipSomaticSegments(skipSomaticSegments)

   **Signature:** ``setSkipSomaticSegments(boolean) -> void``

   **Parameters:**

   * **skipSomaticSegments** (``bool``)

   **Returns:** ``None``


TreeStatistics
--------------

.. method:: setExactMetricMatch(exactMetricMatch)

   Sets whether loose phrases (e.g., "# bps" or "n junctions") should be matched to the closest supported metric when retrieving metrics. By default, they are. Names that differ from a supported metric only in case, spacing or punctuation are always matched.

   **Signature:** ``setExactMetricMatch(boolean) -> void``

   **Parameters:**

   * **exactMetricMatch** (``bool``): - if true, loose phrases are not matched and an UnknownMetricException is thrown instead

   **Returns:** ``None``

.. method:: setTable(table)

   Sets the table for this TreeStatistics instance.

   **Signature:** ``setTable(GenericTable) -> void``

   **Parameters:**

   * **table** (``Any``): - the table to be used by this TreeStatistics instance

   **Returns:** ``None``


TreeToRaster
------------

.. method:: setAxialRes(axialRes)

   Sets the axial (z) voxel size.

A value of `0` switches the rasterizer to 2D mode: the z coordinates of the tree are ignored (every node is projected onto the `z = 0` plane) and the output image is a single slice. In-plane (x, y) thickness from node radii is preserved.

   **Signature:** ``setAxialRes(double) -> TreeToRaster``

   **Parameters:**

   * **axialRes** (``float``): - voxel size in the tree's spatial units (typically µm), or

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setDefaultRadius(radius)

   Sets the default radius used for nodes/trees that have no radii defined. If not set, defaults to half the lateral voxel size (i.e., a 1-voxel diameter).

   **Signature:** ``setDefaultRadius(double) -> TreeToRaster``

   **Parameters:**

   * **radius** (``float``): - the default radius in the tree's spatial units

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setGaussianBlur(sigma)

   Enables Gaussian blurring of the (optionally noisy) image, simulating spatially correlated noise and optical blur. Note that Gaussian blurring is ignored when using `rasterizePathLabels()`.

   **Signature:** ``setGaussianBlur(double) -> TreeToRaster``

   **Parameters:**

   * **sigma** (``float``): - the Gaussian sigma in the tree's spatial units (typically µm). Must be positive.

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setLateralRes(lateralRes)

   Sets the lateral (x, y) voxel size.

   **Signature:** ``setLateralRes(double) -> TreeToRaster``

   **Parameters:**

   * **lateralRes** (``float``): - voxel size in the tree's spatial units (typically µm)

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setPoissonNoise(snr, background)

   Enables Poisson shot noise on the rasterized image, simulating photon counting noise typical of fluorescence microscopy.

The peak intensity is derived from the SNR and background using the photon-counting model: `SNR = (peak - bg) / sqrt(peak)`. Note that Poisson shot noise is ignored when using `rasterizePathLabels()`

   **Signature:** ``setPoissonNoise(double, double) -> TreeToRaster``

   **Parameters:**

   * **snr** (``float``): - the signal-to-noise ratio (peak-to-noise). Must be positive.
   * **background** (``float``)

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setRadiusScale(scale)

   Sets a uniform multiplier applied to every node radius (and to the default radius for nodes without radii) when rasterizing. Values above 1 dilate the rendered neurites, e.g. to make thin or sparse structures cover more voxels; values below 1 erode them. Because scaling is uniform, the relative thickness order (and thus thickest-wins label priority) is unchanged.

Note that larger radii increase the rasterized extent and the per-voxel supersampling cost.

   **Signature:** ``setRadiusScale(double) -> TreeToRaster``

   **Parameters:**

   * **scale** (``float``): - the radius multiplier (default 1.0). Must be positive.

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setReferenceBounds(imp)

   Sets reference bounds explicitly, so the output image matches the specified dimensions. When set, the rasterized image will have exactly the given width, height, and depth, with the origin at (0, 0, 0) in pixel coordinates.

   **Signature:** ``setReferenceBounds(ImagePlus) -> TreeToRaster``

   **Parameters:**

   * **imp** (``Any``): - the reference width in pixels

   **Returns:** (``TreeToRaster``) this instance for chaining

.. method:: setThicknessModulation(factor)

   Enables intensity modulation based on local neurite thickness. When enabled, thicker neurites are rendered brighter and thinner neurites dimmer, proportional to the local radius.

The modulation factor defines what fraction of the intensity range is used for thickness variation. For example, a factor of 0.2 means the thickest frustum receives full intensity (1.0) while the thinnest receives 80% of the maximum (0.8).

Note: This option incurs additional computation since the local radius must be resolved for every sub-voxel hit during supersampling. Also, a factor of 1.0 maps the thinnest structure to zero intensity, effectively wiping it.

   **Signature:** ``setThicknessModulation(double) -> TreeToRaster``

   **Parameters:**

   * **factor** (``float``): - the modulation depth in [0, 1]. 0 disables modulation (default). Must be non-negative and at most 1.

   **Returns:** (``TreeToRaster``) this instance for chaining


TuftDetector
------------

.. method:: setPenalizeShortBranches(penalizeShortBranches)

   **Signature:** ``setPenalizeShortBranches(boolean) -> void``

   **Parameters:**

   * **penalizeShortBranches** (``bool``)

   **Returns:** ``None``

.. method:: setPercentileClip(percentileClip)

   **Signature:** ``setPercentileClip(double) -> void``

   **Parameters:**

   * **percentileClip** (``float``)

   **Returns:** ``None``

.. method:: setRadius(radius)

   **Signature:** ``setRadius(double) -> void``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``None``

.. method:: setWeightByIntensity(weightByIntensity)

   **Signature:** ``setWeightByIntensity(boolean) -> void``

   **Parameters:**

   * **weightByIntensity** (``bool``)

   **Returns:** ``None``

.. method:: setWeightByThickness(weightByThickness)

   **Signature:** ``setWeightByThickness(boolean) -> void``

   **Parameters:**

   * **weightByThickness** (``bool``)

   **Returns:** ``None``


Viewer2D
--------

.. method:: addColorBarLegend()

   Adds a color bar legend (LUT ramp) to the viewer. Does nothing if no measurement mapping occurred successfully. Note that when performing mapping to different measurements, the legend reflects only the last mapped measurement.

   **Signature:** ``addColorBarLegend() -> void``

   **Returns:** ``None``

.. method:: addNodes(coloredNodes)

   **Signature:** ``addNodes(Map) -> void``

   **Parameters:**

   * **coloredNodes** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: addPolygon(poly, label)

   **Signature:** ``addPolygon(Polygon2D, String) -> void``

   **Parameters:**

   * **poly** (``Any``)
   * **label** (``str``)

   **Returns:** ``None``

.. method:: setAxesVisible(visible)

   **Signature:** ``setAxesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setDefaultColor(color)

   Sets the default (fallback) color for plotting paths.

   **Signature:** ``setDefaultColor(ColorRGB) -> void``

   **Parameters:**

   * **color** (``Any``): - null not allowed

   **Returns:** ``None``

.. method:: setEqualizeAxes(equalizeAxes)

   /** Sets whether the axes should be equalized (same scale).

When enabled, both X and Y axes will use the same scale to maintain equal aspect ratio. When disabled, each axis maximizes its range.

   **Signature:** ``setEqualizeAxes(boolean) -> void``

   **Parameters:**

   * **equalizeAxes** (``bool``): - true to equalize axes, false otherwise

   **Returns:** ``None``

.. method:: setGridlinesVisible(visible)

   **Signature:** ``setGridlinesVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinMax(min, max)

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **min** (``float``)
   * **max** (``float``)

   **Returns:** ``None``

.. method:: setMinMaxPercentileClipped(values, clipPercent)

   **Signature:** ``setMinMaxPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setMinPercentileClipped(values, clipPercent)

   **Signature:** ``setMinPercentileClipped(double[], double) -> void``

   **Parameters:**

   * **values** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(nanColor)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **nanColor** (``Any``)

   **Returns:** ``None``

.. method:: setOutlineVisible(visible)

   **Signature:** ``setOutlineVisible(boolean) -> void``

   **Parameters:**

   * **visible** (``bool``)

   **Returns:** ``None``

.. method:: setTitle(title)

   Sets the plot display title.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``): - the new title

   **Returns:** ``None``

.. method:: setXrange(xMin, xMax)

   Sets a manual range for the viewers' X-axis. Calling `setXrange(-1, -1)` enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setXrange(double, double) -> void``

   **Parameters:**

   * **xMin** (``float``): - the lower-limit for the X-axis
   * **xMax** (``float``)

   **Returns:** ``None``

.. method:: setYrange(yMin, yMax)

   Sets a manual range for the viewers' Y-axis. Calling `setYrange(-1, -1)` enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setYrange(double, double) -> void``

   **Parameters:**

   * **yMin** (``float``): - the lower-limit for the Y-axis
   * **yMax** (``float``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: addColorBarLegend(colorMapper)

   Adds a color bar legend (LUT ramp) with a title.

   **Signature:** ``addColorBarLegend(ColorMapper) -> void``

   **Parameters:**

   * **colorMapper** (``Any``): - the color table

   **Returns:** ``None``

.. method:: addLabel(label)

   Adds an annotation label to the scene.

   **Signature:** ``addLabel(String) -> void``

   **Parameters:**

   * **label** (``str``): - the annotation text

   **Returns:** ``None``

.. method:: addMesh(objMesh)

   Loads a Wavefront .OBJ file. Should be called before_ displaying the scene, otherwise, if the scene is already visible, `validate()` should be called to ensure all meshes are visible.

   **Signature:** ``addMesh(OBJMesh) -> boolean``

   **Parameters:**

   * **objMesh** (``OBJMesh``): - the mesh to be loaded

   **Returns:** (``bool``) true, if successful

.. method:: addTree(tree)

   Adds a tree to this viewer. Note that calling `updateView()` may be required to ensure that the current View's bounding box includes the added Tree.

   **Signature:** ``addTree(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the Tree to be added. The Tree's label will be used as identifier. It is expected to be unique when rendering multiple Trees, if not (or no label exists) a unique label will be generated.

   **Returns:** ``None``

.. method:: removeAllMeshes()

   Removes all loaded OBJ meshes from current viewer

   **Signature:** ``removeAllMeshes() -> void``

   **Returns:** ``None``

.. method:: removeAllTrees()

   Removes all the Trees from current viewer

   **Signature:** ``removeAllTrees() -> void``

   **Returns:** ``None``

.. method:: removeAnnotation(annot)

   Removes the specified annotation from the viewer.

   **Signature:** ``removeAnnotation(Annotation3D) -> boolean``

   **Parameters:**

   * **annot** (``Annotation3D``): - the Annotation3D object to remove

   **Returns:** (``bool``) true if the annotation was successfully removed, false if the annotation was not found in this viewer

.. method:: removeMesh(mesh)

   Removes the specified OBJ mesh.

   **Signature:** ``removeMesh(OBJMesh) -> boolean``

   **Parameters:**

   * **mesh** (``OBJMesh``): - the key defining the OBJ mesh to be removed.

   **Returns:** (``bool``) true, if mesh was successfully removed.

.. method:: removeTree(treeLabel)

   Removes the specified Tree.

   **Signature:** ``removeTree(String) -> boolean``

   **Parameters:**

   * **treeLabel** (``str``): - the key defining the tree to be removed.

   **Returns:** (``bool``) true, if tree was successfully removed.

.. method:: setAnatomicalMapping(template)

   Applies a custom anatomical axis mapping to the scene, setting axis labels and the scene's up vector (dorsal direction). This is useful for custom atlases or coordinate systems not covered by the predefined templates.

   **Signature:** ``setAnatomicalMapping(String) -> void``

   **Parameters:**

   * **template** (``str``): - a 3-element array of axis labels for {X, Y, Z}, e.g., {"Anterior-Posterior", "Dorsal-Ventral", "Left-Right"}. If null, axes are reset to "X", "Y", "Z".

   **Returns:** ``None``

.. method:: setAnimationAxis(axis)

   Sets the rotation axis for the live animation (double-click spin). Calling this method disables automatic axis detection.

   **Signature:** ``setAnimationAxis(RotationAxis) -> void``

   **Parameters:**

   * **axis** (``Any``): - the axis of rotation (X, Y, or Z). null defaults to Z.

   **Returns:** ``None``

.. method:: setAnimationEnabled(enabled)

   Toggles the Viewer's animation.

   **Signature:** ``setAnimationEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - if true animation starts. Stops if false

   **Returns:** ``None``

.. method:: setAnimationMode(mode)

   Sets the animation mode for both live (double-click) and recorded rotations.

   **Signature:** ``setAnimationMode(AnimationMode) -> void``

   **Parameters:**

   * **mode** (``Any``): - the animation mode (Viewer3D.AnimationMode.FULL_ROTATION or Viewer3D.AnimationMode.PING_PONG). null defaults to FULL_ROTATION.

   **Returns:** ``None``

.. method:: setAutoDetectAnimationAxis(auto)

   Enables or disables automatic detection of the best rotation axis based on the current viewpoint. When enabled (the default), double-clicking to start a live animation will infer the most natural axis by picking the world axis most aligned with the camera's viewing direction. Calling `setAnimationAxis(RotationAxis)` disables auto-detection.

   **Signature:** ``setAutoDetectAnimationAxis(boolean) -> void``

   **Parameters:**

   * **auto** (``bool``): - whether to auto-detect the axis before each animation start

   **Returns:** ``None``

.. method:: setAxesLabels(labels)

   Sets custom labels for the 3D coordinate axes.

   **Signature:** ``setAxesLabels(String[]) -> void``

   **Parameters:**

   * **labels** (``List[str]``): - the axis labels in order: X-axis, Y-axis, Z-axis. If null, defaults to "X", "Y", "Z". If fewer than 3 labels are provided, only the available axes are labeled.

   **Returns:** ``None``

.. method:: setBounds(xMin, xMax, yMin, yMax, zMin, zMax)

   Sets a manual bounding box for the scene. The bounding box determines the zoom and framing of the scene. Current view point is logged to the Console when interacting with the Reconstruction Viewer in debug mode.

   **Signature:** ``setBounds(float, float, float, float, float, float) -> void``

   **Parameters:**

   * **xMin** (``float``): - the X coordinate of the box origin
   * **xMax** (``float``)
   * **yMin** (``float``)
   * **yMax** (``float``)
   * **zMin** (``float``)
   * **zMax** (``float``)

   **Returns:** ``None``

.. method:: setDefaultColor(color)

   Sets the default color for rendering `Tree`s.

   **Signature:** ``setDefaultColor(ColorRGB) -> void``

   **Parameters:**

   * **color** (``Any``): - the new color. Note that this value only applies to Paths that have no specified color and no colors assigned to its nodes

   **Returns:** ``None``

.. method:: setDefaultThickness(thickness)

   Sets the line thickness for rendering `Tree`s that have no specified radius. Must be called *before* adding paths to the scene.

   **Signature:** ``setDefaultThickness(float) -> void``

   **Parameters:**

   * **thickness** (``float``): - the new line thickness. Note that this value only applies to Paths that have no specified radius

   **Returns:** ``None``

.. method:: setDepthFog(enabled)

   Enables or disables depth fog for all trees (current and future). The preference is persisted across sessions.

   **Signature:** ``setDepthFog(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - whether to apply depth fog to neurite rendering

   **Returns:** ``None``

.. method:: setEnableAxes(enable)

   Enables/disables the display of X,Y,Z axis grid.

   **Signature:** ``setEnableAxes(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - true to enable axes

   **Returns:** ``None``

.. method:: setEnableDarkMode(enable)

   Enables/disables "Dark Mode" mode

   **Signature:** ``setEnableDarkMode(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - true to enable "Dark Mode", "Light Mode" otherwise

   **Returns:** ``None``

.. method:: setEnableDebugMode(enable)

   Enables/disables debug mode

   **Signature:** ``setEnableDebugMode(boolean) -> void``

   **Parameters:**

   * **enable** (``bool``): - true to enable debug mode, otherwise false

   **Returns:** ``None``

.. method:: setFogIntensity(intensity)

   Sets the fog intensity for all trees and persists the preference.

   **Signature:** ``setFogIntensity(float) -> void``

   **Parameters:**

   * **intensity** (``float``): - 0 (very subtle) to 1 (fully fogged at far depth)

   **Returns:** ``None``

.. method:: setFont(font, angle, color)

   Sets the font for label annotations

   **Signature:** ``setFont(Font, float, ColorRGB) -> void``

   **Parameters:**

   * **font** (``Any``): - the font label, e.g.,
   * **angle** (``float``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: setLabelLocation(x, y)

   Sets the location for annotation labels

   **Signature:** ``setLabelLocation(float, float) -> void``

   **Parameters:**

   * **x** (``float``): - the x position of the label
   * **y** (``float``)

   **Returns:** ``None``

.. method:: setLookAndFeel(lookAndFeelName)

   **Signature:** ``setLookAndFeel(String) -> void``

   **Parameters:**

   * **lookAndFeelName** (``str``)

   **Returns:** ``None``

.. method:: setMeshBackfaceCull(enabled)

   Enables or disables backface culling for all OBJ meshes (current and future). Backface culling skips rendering of back-facing triangles, improving performance for closed meshes. The preference is persisted across sessions.

   **Signature:** ``setMeshBackfaceCull(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - whether to enable backface culling

   **Returns:** ``None``

.. method:: setMeshShadingMode(mode)

   Sets the shading mode for all OBJ meshes (current and future). The preference is persisted across sessions.

   **Signature:** ``setMeshShadingMode(int) -> void``

   **Parameters:**

   * **mode** (``int``): - OBJMesh.SHADING_DEFAULT or OBJMesh.SHADING_SMOOTH

   **Returns:** ``None``

.. method:: setPseudoLighting(enabled)

   Enables or disables pseudo-lighting for all trees (current and future). Mutually exclusive with depth fog. Enabling this disables fog.

   **Signature:** ``setPseudoLighting(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - whether to apply tangent-based pseudo-lighting

   **Returns:** ``None``

.. method:: setRadiusScale(scale)

   Applies a tube radius scale to a subset of rendered trees.

   **Signature:** ``setRadiusScale(float) -> void``

   **Parameters:**

   * **scale** (``float``): - the Collection of keys specifying the subset of trees, or null to apply to all trees

   **Returns:** ``None``

.. method:: setScaleBarDisplayed(displayed)

   Toggles the display of a scale bar in the bottom-left corner of the scene. The scale bar assumes that scene coordinates are in micrometers, unless a different unit has been specified through `setScaleBarUnit(String)`.

   **Signature:** ``setScaleBarDisplayed(boolean) -> void``

   **Parameters:**

   * **displayed** (``bool``): - true to display the scale bar, false to hide it

   **Returns:** ``None``

.. method:: setScaleBarUnit(unit)

   Sets the base unit of the scene coordinates, used to compute the scale bar length. The unit is parsed by `BoundingBox.sanitizedUnit(String)`, so common aliases (e.g., "um", "micron") are accepted.

   **Signature:** ``setScaleBarUnit(String) -> void``

   **Parameters:**

   * **unit** (``str``): - the unit of scene coordinates: "µm", "nm", "mm", "cm", "m" Unrecognized units are ignored.

   **Returns:** ``None``

.. method:: setSceneUpdatesEnabled(enabled)

   Sets whether the scene should update (refresh) every time a new reconstruction (or mesh) is added/removed from the scene.

   **Signature:** ``setSceneUpdatesEnabled(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - Whether scene updates should be enabled. Should be set to

   **Returns:** ``None``

.. method:: setSnapshotDir(path)

   Sets the directory for storing snapshots.

   **Signature:** ``setSnapshotDir(String) -> void``

   **Parameters:**

   * **path** (``str``): - the absolute path to the new snapshot directory.

   **Returns:** ``None``

.. method:: setSomaRadius(radius)

   Applies a constant radius to the somas of a subset of rendered trees.

   **Signature:** ``setSomaRadius(float) -> void``

   **Parameters:**

   * **radius** (``float``): - the Collection of keys specifying the subset of trees.

   **Returns:** ``None``

.. method:: setSomasDisplayed(displayed)

   Toggles the visibility of somas for all trees in the scene.

   **Signature:** ``setSomasDisplayed(boolean) -> void``

   **Parameters:**

   * **displayed** (``bool``): - whether soma should be displayed

   **Returns:** ``None``

.. method:: setSplitDendritesFromAxons(split)

   Sets whether axons and dendrites should be imported as separated objects.

   **Signature:** ``setSplitDendritesFromAxons(boolean) -> void``

   **Parameters:**

   * **split** (``bool``): - true to segregate imported Trees into axonal and dendritic subtrees. This is likely only relevant to allow for subtree customizations using the GUI commands provided by the "RV Controls" dialog. This parameter is ignored if Trees have no annotations.

   **Returns:** ``None``

.. method:: setTitle(title)

   Sets the title of the Viewer's frame.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **title** (``str``): - the viewer's title. Ignored if Viewer's frame does not exist

   **Returns:** ``None``

.. method:: setTreeColor(labels, color, compartment)

   Recolors a subset of rendered trees.

   **Signature:** ``setTreeColor(Collection, ColorRGB, String) -> void``

   **Parameters:**

   * **labels** (``List[Any]``): - the Collection of keys specifying the subset of trees
   * **color** (``Any``)
   * **compartment** (``str``)

   **Returns:** ``None``

.. method:: setTreeThickness(thickness)

   Applies a constant thickness (line width) to all rendered trees.Note that by default, trees are rendered using their nodes' diameter.

   **Signature:** ``setTreeThickness(float) -> void``

   **Parameters:**

   * **thickness** (``float``): - the thickness (line width)

   **Returns:** ``None``

.. method:: setTubeMode(enabled)

   Enables or disables tube rendering for all trees (current and future). The preference is persisted across sessions.

   **Signature:** ``setTubeMode(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - whether to render neurites as 3D tubes

   **Returns:** ``None``

.. method:: setTubeSides(sides)

   Sets the number of sides for tube cross-sections for all trees. Only has a visual effect when tube rendering is active. The preference is persisted across sessions.

   **Signature:** ``setTubeSides(int) -> void``

   **Parameters:**

   * **sides** (``int``): - number of sides (clamped to [3, 16])

   **Returns:** ``None``

.. method:: setTubeWireframe(enabled)

   Enables or disables the wireframe overlay on tube rendering for all trees. The preference is persisted across sessions.

   **Signature:** ``setTubeWireframe(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``): - whether to show wireframe edges on tubes

   **Returns:** ``None``

.. method:: setUpsamplingFactor(factor)

   Sets the Catmull-Rom upsampling factor for all trees and rebuilds them. 1 = no smoothing, higher = smoother paths at vertex joints.

   **Signature:** ``setUpsamplingFactor(int) -> void``

   **Parameters:**

   * **factor** (``int``): - upsampling factor (1-10)

   **Returns:** ``None``

.. method:: setViewMode(viewMode)

   Renders the scene from a specified camera angle (script-friendly).

   **Signature:** ``setViewMode(String) -> void``

   **Parameters:**

   * **viewMode** (``str``): - the view mode (case-insensitive): "xy"; "xz"; "yz"; "perspective" or "overview"; "default" or "".

   **Returns:** ``None``

.. method:: setViewPoint(r, t)

   Renders the scene from a specified camera angle using polar coordinates relative to the center of the scene. Only X and Y dimensions are required, as the distance to center is automatically computed. Current view point is logged to the Console by calling `logSceneControls()`.

   **Signature:** ``setViewPoint(double, double) -> void``

   **Parameters:**

   * **r** (``float``): - the radial coordinate
   * **t** (``float``)

   **Returns:** ``None``

.. method:: setViewPointCC(x, y)

   Calls `setViewPoint(double, double)` using Cartesian coordinates.

   **Signature:** ``setViewPointCC(double, double) -> void``

   **Parameters:**

   * **x** (``float``): - the X coordinate
   * **y** (``float``)

   **Returns:** ``None``

.. method:: setVisible(label, visible)

   Toggles the visibility of a rendered Tree, a loaded OBJ mesh, or an annotation.

   **Signature:** ``setVisible(String, boolean) -> void``

   **Parameters:**

   * **label** (``str``): - the unique identifier of the Tree (as per addTree(Tree)), the filename/identifier of the loaded OBJ loadMesh(String, ColorRGB, double), or annotation label.
   * **visible** (``bool``)

   **Returns:** ``None``


----

*Category index generated on 2026-11-02 08:38:08*