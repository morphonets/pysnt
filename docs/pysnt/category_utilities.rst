Utilities Methods
=================

General utility methods and helper functions.

Total methods in this category: **916**

.. contents:: Classes in this Category
   :local:

AStarRefiner
------------

.. method:: apply()

   Applies the re-traced geometry to the original path via `Path.replaceNodes(Path)`. Must be called sequentially (not thread-safe), typically on the EDT after all parallel `call()` invocations have completed.

   **Signature:** ``apply() -> void``

   **Returns:** ``None``

.. method:: applySettings(ref)

   No-op: kept for consistency with the other `AbstractRefineHelper` workers; there are no per-worker settings to propagate here (see `readPreferences()`).

   **Signature:** ``applySettings(AStarRefiner) -> void``

   **Parameters:**

   * **ref** (``AStarRefiner``): - the reference refiner (unused)

   **Returns:** ``None``

.. method:: call()

   Runs the A* re-trace on this path's current waypoints. Thread-safe: does not modify the original path. Call `apply()` afterward (sequentially) to commit results.

   **Signature:** ``call() -> Path``

   **Returns:** (``Path``) the re-traced path, or null if re-tracing failed

.. method:: succeeded()

   Whether the re-trace succeeded. Only meaningful after `call()`.

   **Signature:** ``succeeded() -> boolean``

   **Returns:** (``bool``) true if a valid re-traced path was produced


AllenCompartment
----------------

.. method:: acronym()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``acronym() -> String``

   **Returns:** ``str``

.. method:: aliases()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``aliases() -> String[]``

   **Returns:** ``List[str]``

.. method:: equals(obj)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **obj** (``Any``)

   **Returns:** ``bool``

.. method:: id()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``id() -> int``

   **Returns:** ``int``

.. method:: includes(other)

   **Signature:** ``includes(BrainAnnotation) -> boolean``

   **Parameters:**

   * **other** (``Any``)

   **Returns:** ``bool``

.. method:: name()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``name() -> String``

   **Returns:** ``str``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``


AllenUtils
----------

.. method:: assignAnnotationsFromNodeValues(tree)

   Assigns brain annotations (interpreted as CCF IDs) to node values for all paths in a Tree.

This method is the inverse operation of `transferAnnotationIdsToNodeValues(Tree)`.

   **Signature:** ``assignAnnotationsFromNodeValues(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the Tree containing paths with node values to be converted to annotations. Must not be null. Paths without node values are skipped. Invalid node values result in null annotations.

   **Returns:** ``None``

.. method:: assignHemisphereTags(graph)

   **Signature:** ``assignHemisphereTags(DirectedWeightedGraph) -> void``

   **Parameters:**

   * **graph** (``DirectedWeightedGraph``)

   **Returns:** ``None``

.. method:: assignToLeftHemisphere(tree)

   Assigns a tree to the left hemisphere by mirroring it if necessary.

   **Signature:** ``assignToLeftHemisphere(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the tree to assign to the left hemisphere

   **Returns:** ``None``

.. method:: assignToRightHemisphere(tree)

   Assigns a tree to the right hemisphere by mirroring it if necessary.

   **Signature:** ``assignToRightHemisphere(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the tree to assign to the right hemisphere

   **Returns:** ``None``

.. method:: brainCenter()

   Returns the spatial centroid of the Allen CCF.

   **Signature:** ``brainCenter() -> SNTPoint``

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of the ARA

.. method:: splitByHemisphere(graph)

   **Signature:** ``splitByHemisphere(DirectedWeightedGraph) -> List``

   **Parameters:**

   * **graph** (``DirectedWeightedGraph``)

   **Returns:** ``List[Any]``

.. method:: transferAnnotationIdsToNodeValues(tree)

   Transfers brain annotation IDs to node values for all paths in a Tree.

This is useful for preserving annotation information when saving data to TRACES files. Note that this method overwrites any existing node values. Nodes without annotations (null) are assigned `BRAIN_ROOT_ID`.

   **Signature:** ``transferAnnotationIdsToNodeValues(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the Tree containing paths with brain annotations to be transferred. Must not be null and must contain valid annotations.

   **Returns:** ``None``


AlongPathDetector
-----------------

.. method:: detect(paths, cfg)

   **Signature:** ``detect(Collection, Config) -> List``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **cfg** (``Any``)

   **Returns:** ``List[Any]``


Annotation3D
------------

.. method:: meshToDrawable(mesh)

   **Signature:** ``meshToDrawable(Mesh) -> Drawable``

   **Parameters:**

   * **mesh** (``Any``)

   **Returns:** ``Any``


AnnotationGraph
---------------

.. method:: applyEdges(operator)

   **Signature:** ``applyEdges(UnaryOperator) -> void``

   **Parameters:**

   * **operator** (``Any``)

   **Returns:** ``None``

.. method:: applyVertices(operator)

   **Signature:** ``applyVertices(UnaryOperator) -> void``

   **Parameters:**

   * **operator** (``Any``)

   **Returns:** ``None``

.. method:: filterEdges(predicate)

   **Signature:** ``filterEdges(Predicate) -> void``

   **Parameters:**

   * **predicate** (``Any``)

   **Returns:** ``None``

.. method:: filterEdgesByWeight(minWeight)

   **Signature:** ``filterEdgesByWeight(int) -> void``

   **Parameters:**

   * **minWeight** (``int``)

   **Returns:** ``None``

.. method:: filterVertices(predicate)

   **Signature:** ``filterVertices(Predicate) -> void``

   **Parameters:**

   * **predicate** (``Any``)

   **Returns:** ``None``

.. method:: sumEdgeWeights()

   **Signature:** ``sumEdgeWeights() -> double``

   **Returns:** ``float``


ArraySearchImage
----------------

.. method:: iterator()

   **Signature:** ``iterator() -> Iterator``

   **Returns:** ``Any``


ArrayStorageBackend
-------------------

.. method:: buildGraph(dims, spacing, threshold)

   **Signature:** ``buildGraph(long[], double[], double) -> DirectedWeightedGraph``

   **Parameters:**

   * **dims** (``List[int]``)
   * **spacing** (``List[float]``)
   * **threshold** (``float``)

   **Returns:** ``DirectedWeightedGraph``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: estimateMemoryUsage()

   **Signature:** ``estimateMemoryUsage() -> long``

   **Returns:** ``int``

.. method:: initializeFastMarching(dims, seedIndex)

   **Signature:** ``initializeFastMarching(long[], long) -> void``

   **Parameters:**

   * **dims** (``List[int]``)
   * **seedIndex** (``int``)

   **Returns:** ``None``

.. method:: iterateNeighborsForFM(pos, neighborPos, nDims, spacing, consumer)

   **Signature:** ``iterateNeighborsForFM(long[], long[], int, double[], DoubleConsumer) -> void``

   **Parameters:**

   * **pos** (``List[int]``)
   * **neighborPos** (``List[int]``)
   * **nDims** (``int``)
   * **spacing** (``List[float]``)
   * **consumer** (``Any``)

   **Returns:** ``None``

.. method:: reinitializeFastMarching(dims, seedIndex, excludedIndices)

   **Signature:** ``reinitializeFastMarching(long[], long, Set) -> void``

   **Parameters:**

   * **dims** (``List[int]``)
   * **seedIndex** (``int``)
   * **excludedIndices** (``Set[Any]``)

   **Returns:** ``None``


AutoTraceConfig
---------------

.. method:: applyTo(tracer)

   **Signature:** ``applyTo(AbstractGWDTTracer) -> void``

   **Parameters:**

   * **tracer** (``Any``)

   **Returns:** ``None``

.. method:: fractionInBounds(paths, source, spacing)

   **Signature:** ``fractionInBounds(List, RandomAccessibleInterval, double[]) -> double``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``float``


AutoTracer
----------

.. method:: honoredSeedRoles()

   **Signature:** ``honoredSeedRoles() -> EnumSet``

   **Returns:** ``Any``

.. method:: trace()

   **Signature:** ``trace() -> Tree``

   **Returns:** ``Tree``

.. method:: traceTrees()

   **Signature:** ``traceTrees() -> List``

   **Returns:** ``List[Any]``


Bdv
---

.. method:: add(reconstructionFiles)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``add(File[]) -> void``

   **Parameters:**

   * **reconstructionFiles** (``List[str]``): - which source(s) to recompute

   **Returns:** ``None``

.. method:: annotations()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``annotations() -> AnnotationOverlay``

   **Returns:** ``Any``

.. method:: captureKeyframe()

   **Signature:** ``captureKeyframe() -> Keyframe``

   **Returns:** ``Any``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: flyTo(box)

   **Signature:** ``flyTo(BoundingBox) -> boolean``

   **Parameters:**

   * **box** (``BoundingBox``)

   **Returns:** ``bool``

.. method:: hideSecondaryData()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``hideSecondaryData() -> void``

   **Returns:** ``None``

.. method:: onSntActiveNodeChanged()

   **Signature:** ``onSntActiveNodeChanged() -> void``

   **Returns:** ``None``

.. method:: onSntEditModeChanged(enabled)

   **Signature:** ``onSntEditModeChanged(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: playback(keyframes)

   **Signature:** ``playback(List) -> void``

   **Parameters:**

   * **keyframes** (``List[Any]``)

   **Returns:** ``None``

.. method:: promptGoTo()

   **Signature:** ``promptGoTo() -> void``

   **Returns:** ``None``

.. method:: registerOmeZarrSource(path)

   **Signature:** ``registerOmeZarrSource(String) -> void``

   **Parameters:**

   * **path** (``str``)

   **Returns:** ``None``

.. method:: repaint()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``repaint() -> void``

   **Returns:** ``None``

.. method:: resyncCalibrationFromActiveSource()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``resyncCalibrationFromActiveSource() -> void``

   **Returns:** ``None``

.. method:: revealContextCommand(cmd)

   **Signature:** ``revealContextCommand(ContextMenuCommand) -> void``

   **Parameters:**

   * **cmd** (``Any``)

   **Returns:** ``None``

.. method:: revealContextItem(canvasItem)

   **Signature:** ``revealContextItem(JMenuItem) -> void``

   **Parameters:**

   * **canvasItem** (``Any``)

   **Returns:** ``None``

.. method:: runContextCommand(cmd)

   **Signature:** ``runContextCommand(ContextMenuCommand) -> String``

   **Parameters:**

   * **cmd** (``Any``)

   **Returns:** ``str``

.. method:: runContextItem(canvasItem)

   **Signature:** ``runContextItem(JMenuItem) -> String``

   **Parameters:**

   * **canvasItem** (``Any``)

   **Returns:** ``str``

.. method:: show(spimData)

   Opens sources loaded from an N5 or OME-Zarr container (see `SpimDataUtils.resolvePathToSource(String)`). Unlike `show(AbstractSpimData)`, there is no BDV-XML descriptor or `AbstractSpimData` involved: sources are built directly from the container's own N5/OME-NGFF metadata via `n5-viewer_fiji`.

   **Signature:** ``show(AbstractSpimData) -> List``

   **Parameters:**

   * **spimData** (``Any``): - the sources to display

   **Returns:** (``List[Any]``) list of BdvStackSources, one per setup

.. method:: stopPlayback()

   **Signature:** ``stopPlayback() -> void``

   **Returns:** ``None``

.. method:: syncOverlays()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``syncOverlays() -> void``

   **Returns:** ``None``

.. method:: updateSecondaryLayerIndicator()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``updateSecondaryLayerIndicator() -> void``

   **Returns:** ``None``

.. method:: updateSelection()

   Lightweight alternative to `AbstractBigViewer.syncPathManagerList()` for pure selection changes: patches color/thickness in place for already-rendered trees. Mirrors `Bvv.updateSelection()`

   **Signature:** ``updateSelection() -> void``

   **Returns:** ``None``

.. method:: updateStatus(message, step, nSteps)

   **Signature:** ``updateStatus(String, int, int) -> void``

   **Parameters:**

   * **message** (``str``)
   * **step** (``int``)
   * **nSteps** (``int``)

   **Returns:** ``None``


BiSearch
--------

.. method:: pointsConsideredInSearch()

   Description copied from class: `AbstractSearch`

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   Description copied from class: `AbstractSearch`

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(success)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **success** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


BiSearchArtist
--------------

.. method:: anyNodeUnderThreshold(x, y, z, threshold)

   **Signature:** ``anyNodeUnderThreshold(int, int, int, double) -> BiSearchNode``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)
   * **threshold** (``float``)

   **Returns:** ``BiSearchNode``


BiSearchNode
------------

.. method:: equals(o)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **o** (``Any``)

   **Returns:** ``bool``

.. method:: heapDecreaseKey(fromStart)

   **Signature:** ``heapDecreaseKey(boolean) -> void``

   **Parameters:**

   * **fromStart** (``bool``)

   **Returns:** ``None``

.. method:: heapInsert(heap, fromStart)

   **Signature:** ``heapInsert(AddressableHeap, boolean) -> void``

   **Parameters:**

   * **heap** (``Any``)
   * **fromStart** (``bool``)

   **Returns:** ``None``


BinaryTracer
------------

.. method:: honoredSeedRoles()

   **Signature:** ``honoredSeedRoles() -> EnumSet``

   **Returns:** ``Any``

.. method:: skeletonize(imp, erodeIsolatedPixels)

   **Signature:** ``skeletonize(ImagePlus, boolean) -> void``

   **Parameters:**

   * **imp** (``Any``)
   * **erodeIsolatedPixels** (``bool``)

   **Returns:** ``None``

.. method:: skeletonizeTimeLapse(imp, erodeIsolatedPixels)

   **Signature:** ``skeletonizeTimeLapse(ImagePlus, boolean) -> void``

   **Parameters:**

   * **imp** (``Any``)
   * **erodeIsolatedPixels** (``bool``)

   **Returns:** ``None``

.. method:: trace()

   **Signature:** ``trace() -> Tree``

   **Returns:** ``Tree``

.. method:: traceTrees()

   **Signature:** ``traceTrees() -> List``

   **Returns:** ``List[Any]``


BookmarkManager
---------------

.. method:: add(map, commonLabel)

   Adds multiple bookmarks from selected path nodes

   **Signature:** ``add(Map, String) -> void``

   **Parameters:**

   * **map** (``Dict[str, Any]``): - the map of [k=Path, v=list of node indices] from which node positions are extracted
   * **commonLabel** (``str``)

   **Returns:** ``None``

.. method:: dispose()

   Should be called when the panel is removed from the UI.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: load(file)

   **Signature:** ``load(File) -> boolean``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``bool``

.. method:: remove(path, nodeIndex)

   **Signature:** ``remove(Path, int) -> void``

   **Parameters:**

   * **path** (``Path``)
   * **nodeIndex** (``int``)

   **Returns:** ``None``

.. method:: reset()

   Clears all bookmarks.

   **Signature:** ``reset() -> void``

   **Returns:** ``None``

.. method:: resyncOverlay()

   Re-pushes all markers onto the viewer's shared `AbstractBigViewer.AnnotationOverlay`. A no-op in SNT-UI mode (`viewer == null`). Meant to be called by `Bvv`/`Bdv` right after (re)creating that overlay, so markers added while `syncViewerOverlay()` was still no-op-ing on a null `AbstractBigViewer.annotations()` (i.e. before the viewer window existed) get rendered instead of silently staying buffered in the model.

   **Signature:** ``resyncOverlay() -> void``

   **Returns:** ``None``

.. method:: save(file)

   **Signature:** ``save(File) -> boolean``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``bool``

.. method:: toOverlay(overlay)

   Adds the bookmark ROIs to the specified overlay. If no bookmarks are selected, all bookmarks are added, otherwise only the selected bookmarks are added.

   **Signature:** ``toOverlay(Overlay) -> void``

   **Parameters:**

   * **overlay** (``Any``): - the overlay to add the bookmarks to. Null not allowed

   **Returns:** ``None``

.. method:: toRoiManager()

   Adds the bookmarks to the ROI Manager. If no bookmarks are selected, all bookmarks are added, otherwise only the selected bookmarks are added.

   **Signature:** ``toRoiManager() -> void``

   **Returns:** ``None``


BoundingBox
-----------

.. method:: append(iterator)

   Computes the bounding box of the specified point cloud and appends it to this bounding box, resizing it as needed.

   **Signature:** ``append(Iterator) -> void``

   **Parameters:**

   * **iterator** (``Any``): - the iterator of the points Collection

   **Returns:** ``None``

.. method:: clone()

   Creates a copy of this BoundingBox.

   **Signature:** ``clone() -> BoundingBox``

   **Returns:** (``BoundingBox``) a new BoundingBox that is a copy of this bounding box

.. method:: combine(other)

   Combines this bounding box with another one. It is assumed both boxes share the same voxel spacing/Calibration.

   **Signature:** ``combine(BoundingBox) -> void``

   **Parameters:**

   * **other** (``BoundingBox``): - the bounding box to be combined.

   **Returns:** ``None``

.. method:: contains(boundingBox)

   **Signature:** ``contains(BoundingBox) -> boolean``

   **Parameters:**

   * **boundingBox** (``BoundingBox``)

   **Returns:** ``bool``

.. method:: contains2D(point)

   **Signature:** ``contains2D(SNTPoint) -> boolean``

   **Parameters:**

   * **point** (``SNTPoint``)

   **Returns:** ``bool``

.. method:: depth()

   **Signature:** ``depth() -> double``

   **Returns:** ``float``

.. method:: equals(obj)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **obj** (``Any``)

   **Returns:** ``bool``

.. method:: expand(xPad, yPad, zPad)

   Grows this box outward on every side by the specified calibrated (world-unit) amounts, keeping its centroid fixed. Unlike a fixed pixel-count margin, this scales sensibly with anisotropic spacing (e.g., a large Z spacing common in light-sheet/expansion data would make a fixed pixel margin either negligible or huge depending on the axis).

   **Signature:** ``expand(double, double, double) -> void``

   **Parameters:**

   * **xPad** (``float``): - the calibrated padding added on both sides of X
   * **yPad** (``float``)
   * **zPad** (``float``)

   **Returns:** ``None``

.. method:: height()

   **Signature:** ``height() -> double``

   **Returns:** ``float``

.. method:: inferSpacing(points)

   Infers the voxel spacing of this box from the inter-node distances of a Collection of `SWCPoint`s.

   **Signature:** ``inferSpacing(Collection) -> void``

   **Parameters:**

   * **points** (``List[Any]``): - the point collection

   **Returns:** ``None``

.. method:: intersection(other)

   Retrieves the intersection cuboid between this bounding with another bounding box. It is assumed both boxes share the same voxel spacing/Calibration.

   **Signature:** ``intersection(BoundingBox) -> BoundingBox``

   **Parameters:**

   * **other** (``BoundingBox``): - the second bounding box.

   **Returns:** (``BoundingBox``) The intersection cuboid.

.. method:: origin()

   Retrieves the origin of this box.

   **Signature:** ``origin() -> PointInImage``

   **Returns:** (``PointInImage``) the origin

.. method:: originOpposite()

   Retrieves the origin opposite of this box.

   **Signature:** ``originOpposite() -> PointInImage``

   **Returns:** (``PointInImage``) the origin

.. method:: sanitizedUnit(unit)

   **Signature:** ``sanitizedUnit(String) -> String``

   **Parameters:**

   * **unit** (``str``)

   **Returns:** ``str``

.. method:: scale(scale)

   **Signature:** ``scale(double[]) -> BoundingBox``

   **Parameters:**

   * **scale** (``List[float]``)

   **Returns:** ``BoundingBox``

.. method:: shift(offset)

   **Signature:** ``shift(double[]) -> BoundingBox``

   **Parameters:**

   * **offset** (``List[float]``)

   **Returns:** ``BoundingBox``

.. method:: toBoundingBox3d()

   **Signature:** ``toBoundingBox3d() -> BoundingBox3d``

   **Returns:** ``Any``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``

.. method:: unscaledOrigin()

   Retrieves the origin of this box in unscaled ("pixel" units)

   **Signature:** ``unscaledOrigin() -> PointInImage``

   **Returns:** (``PointInImage``) the unscaled origin

.. method:: unscaledOriginOpposite()

   Retrieves the origin opposite of this box in unscaled ("pixel" units)

   **Signature:** ``unscaledOriginOpposite() -> PointInImage``

   **Returns:** (``PointInImage``) the unscaled origin opposite

.. method:: width()

   **Signature:** ``width() -> double``

   **Returns:** ``float``


BundleDetector
--------------

.. method:: find(paths, cfg)

   Entry point: detect bundle events for a collection of paths using the given config. Internally constructs a `CrossoverFinder.Config` ith the inverted angle filter (`CrossoverFinder.Config.thetaMaxDeg` set, `CrossoverFinder.Config.thetaMinDeg` disabled) and delegates to 
```
CrossoverFinder.find(java.util.Collection<sc.fiji.snt.Path>, sc.fiji.snt.util.CrossoverFinder.Config)
```
.

   **Signature:** ``find(Collection, Config) -> List``

   **Parameters:**

   * **paths** (``List[Any]``): - the collection of paths
   * **cfg** (``Any``)

   **Returns:** (``List[Any]``) list of detected bundle events (typed as `CrossoverFinder.CrossoverEvent`)


Bvv
---

.. method:: add(reconstructionFiles)

   Loads reconstruction files and adds them to the viewer with live progress feedback. Files are loaded one at a time on a background thread; the viewer scene is updated after each file so the user sees trees appearing incrementally. The progress bar in the SNT Annotations card tracks progress.

   **Signature:** ``add(File[]) -> void``

   **Parameters:**

   * **reconstructionFiles** (``List[str]``): - the reconstruction files (SWC, JSON, etc.) to load

   **Returns:** ``None``

.. method:: annotations()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``annotations() -> AnnotationOverlay``

   **Returns:** ``Any``

.. method:: captureKeyframe()

   **Signature:** ``captureKeyframe() -> Keyframe``

   **Returns:** ``Any``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: findCenterRay()

   Returns the world-space endpoints of the perspective ray through the center of the viewer's display (its optical axis). Unlike `findClickRay()`, this does not depend on the mouse cursor.

   **Signature:** ``findCenterRay() -> double[][]``

   **Returns:** (``List[List[float]]``) a 2x3 array { nearWorld, farWorld } in world coordinates, or null if the viewer state is unavailable

.. method:: findClickRay()

   Returns the world-space endpoints of the perspective ray through the current mouse cursor position: result[0] = near-clip world point, result[1] = far-clip world point. Returns null if the mouse is outside the display or the viewer is not initialized.

The ray correctly accounts for BVV's perspective projection (`pf = dCam/(dCam+viewerZ)`), giving a well-defined 3D ray for every screen pixel regardless of where the volume's focal plane sits. Use this instead of `getGlobalMouseCoordinates(net.imglib2.RealPoint)` when the Z coordinate of the picked point is important (e.g. landmark placement).

   **Signature:** ``findClickRay() -> double[][]``

   **Returns:** ``List[List[float]]``

.. method:: findClickRayMaxima()

   Finds the world-space point of maximum intensity along the perspective ray through the current mouse cursor position.

Casts a ray from the near clip plane to the far clip plane, samples the active source at 0.5-voxel intervals, and refines the peak location to sub-voxel accuracy via a 3-point parabola fit. Use this for landmark placement when the Z coordinate from the focal plane alone is unreliable.

   **Signature:** ``findClickRayMaxima() -> double[]``

   **Returns:** (``List[float]``) world-space [x, y, z] of the intensity maximum, or null if the ray misses the volume, the mouse is outside the display, or no source is loaded

.. method:: findSceneCenterMaxima()

   Finds the world-space point of maximum intensity along the perspective ray through the center of the viewer's display, i.e. whatever is actually visible at the middle of the screen right now, at whatever depth its signal peaks. Same search as `findClickRayMaxima()`, but along the optical axis rather than through the mouse.

   **Signature:** ``findSceneCenterMaxima() -> double[]``

   **Returns:** (``List[float]``) world-space [x, y, z] of the intensity maximum, or null if the ray misses the volume, the viewer is unavailable, or no source is loaded

.. method:: flyTo(box)

   **Signature:** ``flyTo(BoundingBox) -> boolean``

   **Parameters:**

   * **box** (``BoundingBox``)

   **Returns:** ``bool``

.. method:: hideSecondaryData()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``hideSecondaryData() -> void``

   **Returns:** ``None``

.. method:: onSntActiveNodeChanged()

   **Signature:** ``onSntActiveNodeChanged() -> void``

   **Returns:** ``None``

.. method:: onSntEditModeChanged(enabled)

   **Signature:** ``onSntEditModeChanged(boolean) -> void``

   **Parameters:**

   * **enabled** (``bool``)

   **Returns:** ``None``

.. method:: open(spimData)

   Convenience factory: opens one or more file paths into the same BVV viewer window, choosing the most appropriate loading strategy per file:

- **.ims** Imaris HDF5: creates a BDV XML sidecar file next to the `.ims` file (using the same base name, e.g. `dataset.xml` ), then loads it via `XmlIoSpimDataMinimal` . BVV's pyramid-aware GPU cache manager is used, so the full volume is never loaded into RAM. If the directory is not writable, an `IllegalArgumentException` is thrown with instructions to create the XML manually using `Plugins > BigDataViewer > Create XML for Imaris file` .

- **.xml** BDV XML/HDF5: loaded directly via `XmlIoSpimDataMinimal` and displayed using BVV's cache manager. This covers BDV HDF5 and BDV N5 datasets.

- **.n5 / .zarr** directories: opened directly via `n5-viewer_fiji` (no XML sidecar) and displayed using BVV's cache manager. This covers plain N5 multiscale groups and OME-NGFF (OME-Zarr) containers.

- **anything else** delegated to `ImgUtils.open(String)` and displayed via the standard `ImgPlus` path. Very large flat volumes will fail with a descriptive error rather than a GL crash.

Typical Groovy/PySNT usage: `def bvv = Bvv.open("/path/to/reference.xml", "/path/to/moving.ims")`

   **Signature:** ``open(AbstractSpimData) -> Bvv``

   **Parameters:**

   * **spimData** (``Any``): - one or more file paths or URLs to open

   **Returns:** (``Bvv``) the fully initialised `Bvv` instance

   **Example:**

   .. code-block:: java

      def bvv = Bvv.open("/path/to/reference.xml", "/path/to/moving.ims")

.. method:: playback(keyframes)

   **Signature:** ``playback(List) -> void``

   **Parameters:**

   * **keyframes** (``List[Any]``)

   **Returns:** ``None``

.. method:: promptGoTo()

   **Signature:** ``promptGoTo() -> void``

   **Returns:** ``None``

.. method:: registerOmeZarrSource(path)

   **Signature:** ``registerOmeZarrSource(String) -> void``

   **Parameters:**

   * **path** (``str``)

   **Returns:** ``None``

.. method:: repaint()

   Forces a repaint of the viewer, updating volume renderings but not overlays.

   **Signature:** ``repaint() -> void``

   **Returns:** ``None``

.. method:: resyncCalibrationFromActiveSource()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``resyncCalibrationFromActiveSource() -> void``

   **Returns:** ``None``

.. method:: revealContextCommand(cmd)

   **Signature:** ``revealContextCommand(ContextMenuCommand) -> void``

   **Parameters:**

   * **cmd** (``Any``)

   **Returns:** ``None``

.. method:: revealContextItem(canvasItem)

   **Signature:** ``revealContextItem(JMenuItem) -> void``

   **Parameters:**

   * **canvasItem** (``Any``)

   **Returns:** ``None``

.. method:: runContextCommand(cmd)

   **Signature:** ``runContextCommand(ContextMenuCommand) -> String``

   **Parameters:**

   * **cmd** (``Any``)

   **Returns:** ``str``

.. method:: runContextItem(canvasItem)

   **Signature:** ``runContextItem(JMenuItem) -> String``

   **Parameters:**

   * **canvasItem** (``Any``)

   **Returns:** ``str``

.. method:: show(spimData)

   Displays the BVV viewer with the specified image.

   **Signature:** ``show(AbstractSpimData) -> List``

   **Parameters:**

   * **spimData** (``Any``)

   **Returns:** ``List[Any]``

.. method:: snapshot()

   Retrieves the specified scene view as an image. **Must be called from a non-EDT thread** (e.g. a script or SwingWorker), otherwise the render latch will time out.

   **Signature:** ``snapshot() -> ImagePlus``

   **Returns:** ``Any``

.. method:: stopPlayback()

   **Signature:** ``stopPlayback() -> void``

   **Returns:** ``None``

.. method:: syncOverlays()

   Updates the viewer display to reflect changes in rendered trees and paths. This method should be called after modifying the collection of rendered objects to ensure the display is synchronized.

   **Signature:** ``syncOverlays() -> void``

   **Returns:** ``None``

.. method:: updateSecondaryLayerIndicator()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``updateSecondaryLayerIndicator() -> void``

   **Returns:** ``None``

.. method:: updateSelection()

   Lightweight alternative to `AbstractBigViewer.syncPathManagerList()` for pure selection changes. Patches color/thickness in place for already-rendered trees instead of rebuilding the Path Manager's tree grouping and recomputing screen-space geometry for the whole scene. Does nothing if paths haven't been rendered yet (e.g., before the first sync); The next `AbstractBigViewer.syncPathManagerList()` call renders and colors them correctly regardless.

   **Signature:** ``updateSelection() -> void``

   **Returns:** ``None``

.. method:: updateStatus(message, step, nSteps)

   **Signature:** ``updateStatus(String, int, int) -> void``

   **Parameters:**

   * **message** (``str``)
   * **step** (``int``)
   * **nSteps** (``int``)

   **Returns:** ``None``


BvvMultiSource
--------------

.. method:: applyTransform(transform)

   Applies the given transform as the fixed transform to the leader and all followers. This is the primary entry point for loading a saved transform.

   **Signature:** ``applyTransform(AffineTransform3D) -> void``

   **Parameters:**

   * **transform** (``Any``): - the transform to apply

   **Returns:** ``None``

.. method:: channelSetup(i)

   **Signature:** ``channelSetup(int) -> ConverterSetup``

   **Parameters:**

   * **i** (``int``)

   **Returns:** ``Any``

.. method:: channelSource(i)

   **Signature:** ``channelSource(int) -> SourceAndConverter``

   **Parameters:**

   * **i** (``int``)

   **Returns:** ``Any``

.. method:: syncTransforms()

   Forces a repaint. With field-sharing active, followers already hold the same transform objects as the leader: this call just flushes the display. Called internally after transform commits in the fallback path.

   **Signature:** ``syncTransforms() -> void``

   **Returns:** ``None``


BvvUtils
--------

.. method:: buildTiledPyramid(img, nLevels)

   Builds one pyramid-backed `Source` per channel of an in-memory image, such that BVV renders it with its tile-streaming path (`MultiResolutionStack3D`) instead of uploading the whole volume as a single 3D texture, which is capped by `GL_MAX_3D_TEXTURE_SIZE`. Level 0 and every coarser level is copied into its own `CellImg`, because BVV only streams sources backed by cell images. Level 0 is copied in memory (see `ImgUtils.materializeTiled(net.imglib2.RandomAccessibleInterval<T>, int)`), which costs the full volume in heap (see `estimateTiledPyramidBytes(net.imagej.ImgPlus<?>)`). Coarser levels (step 2, 4, 8...) are averaged from the previous level (see `averagedLevel(net.imglib2.RandomAccessibleInterval<T>)`) and computed lazily, on demand

Meant for view-only sessions: the returned sources are independent copies, so an image also held for tracing would be stored twice

   **Signature:** ``buildTiledPyramid(ImgPlus, int) -> N5Sources``

   **Parameters:**

   * **img** (``Any``): - image with X, Y, Z leading, an optional channel axis, and no time axis (see ImgUtils.normalizeToXYZ(net.imagej.ImgPlus<T>))
   * **nLevels** (``int``)

   **Returns:** (``Any``) one source per channel, ready for `Bvv.show(SpimDataUtils.N5Sources)`

.. method:: effectiveCacheMB(nChannels, streaming)

   **Signature:** ``effectiveCacheMB(int, boolean) -> int``

   **Parameters:**

   * **nChannels** (``int``): - number of channels to be displayed
   * **streaming** (``bool``)

   **Returns:** (``int``) the GPU tile cache size (MB) to use: session override, else user preference, else automatic

.. method:: ensureCellBacked(soc)

   As `ensureCellBacked(SourceAndConverter)`, sizing the cells after the chunks of the underlying data

   **Signature:** ``ensureCellBacked(SourceAndConverter) -> SourceAndConverter``

   **Parameters:**

   * **soc** (``Any``): - the source about to be shown in BVV

   **Returns:** (``Any``) `soc` itself if no wrapping is needed (or possible), or an equivalent, cell-backed one

.. method:: estimateLocalCopyBytes(source)

   Estimates the heap needed to copy level 0 of `source` into memory (see `synthesizeMipmapPyramid(bdv.viewer.Source<T>, int, boolean)`)

   **Signature:** ``estimateLocalCopyBytes(Source) -> long``

   **Parameters:**

   * **source** (``Any``): - the source to estimate

   **Returns:** (``int``) the estimated size in bytes

.. method:: estimateTiledPyramidBytes(img)

   Estimates the heap needed by `buildTiledPyramid(net.imagej.ImgPlus<T>, int)`: the full XYZ volume of every channel, plus ~15% for the coarser levels. Doubled if `img` is not lazily loaded, since it stays in memory during the copy

   **Signature:** ``estimateTiledPyramidBytes(ImgPlus) -> long``

   **Parameters:**

   * **img** (``Any``): - an image with X, Y, Z leading, and optionally a channel axis

   **Returns:** (``int``) the estimated size in bytes

.. method:: fetcherThreads(remote)

   **Signature:** ``fetcherThreads(boolean) -> int``

   **Parameters:**

   * **remote** (``bool``): - whether the data is read over the network

   **Returns:** (``int``) the number of tile fetcher threads: the `snt.bvv.fetchers` system property, else the user preference, else 64 for remote data or one less than the number of CPU cores

.. method:: maxCacheMB()

   **Signature:** ``maxCacheMB() -> int``

   **Returns:** (``int``) the largest GPU tile cache (MB) we allow: `MAX_CACHE_SIZE_MB` or 25% of the JVM max heap

.. method:: preferMultiResolutionIfSafe(source, timepoint)

   Forces BVV to render `source` with its pyramid-aware, block-streaming path (`bvv.core.multires.MultiResolutionStack3D`) instead of the naive single-texture path (`bvv.core.multires.SimpleStack3D`), when it is safe to do so.

BVV auto-detects which path to use (`bvv.core.multires.SourceStacks#inferSourceStackType`): it only picks the multi-resolution path when `source`'s pixel type is `TileAccess`-supported AND `source.getSource(timepoint, 0)` is (or wraps, via `VolatileView`) an `AbstractCellImg`. Many BDV/N5 source builders wrap their levels in a plain `Views`-based interval (not an `AbstractCellImg`), which makes BVV fall back to `SimpleStack3D` even for a genuinely multi-resolution, remote source. `SimpleStack3D` uploads the entire full-resolution volume as one texture on first paint, fetching all of it synchronously

This mirrors BVV's own `inferSourceStackType` check before overriding it, so it never forces multi-resolution rendering on a source that would actually fail it (which would throw `UnsupportedOperationException` from `TileAccess.create` on the render thread). If the check fails, this method does nothing and BVV falls back to its own (slower) default

   **Signature:** ``preferMultiResolutionIfSafe(Source, int) -> void``

   **Parameters:**

   * **source** (``Any``): - the source about to be shown in BVV
   * **timepoint** (``int``)

   **Returns:** ``None``

.. method:: prefetchForShow(source, timepoint)

   As `prefetchForShow(Source, int)`, reporting progress as the data is fetched

   **Signature:** ``prefetchForShow(Source, int) -> void``

   **Parameters:**

   * **source** (``Any``): - the source to warm up
   * **timepoint** (``int``)

   **Returns:** ``None``

.. method:: recommendedCacheMB(nChannels)

   **Signature:** ``recommendedCacheMB(int) -> int``

   **Parameters:**

   * **nChannels** (``int``)

   **Returns:** (``int``) the automatic GPU tile cache size (MB) for a streamed pyramid with `nChannels` channels

.. method:: releaseSources(sources)

   Releases the in-memory cell caches of the given sources (those not backed by `BvvUtils.CellBackedSource` are ignored) and forgets them. Meant for when the viewer showing them is disposed. The pinned-heap budget they hold is returned right away. That of levels not owned by a source (synthesized or tiled pyramids) is returned once they are garbage-collected

   **Signature:** ``releaseSources(Collection) -> void``

   **Parameters:**

   * **sources** (``List[Any]``): - the sources to release

   **Returns:** ``None``

.. method:: reportChunking(name, chunkShape)

   Logs how the cells streamed to BVV relate to the source chunks and, if the chunk layout is poorly suited to interactive 3D viewing, queues a notice for the notification center. Does nothing if the chunk shape is unknown

   **Signature:** ``reportChunking(String, int[]) -> void``

   **Parameters:**

   * **name** (``str``): - the display name of the data
   * **chunkShape** (``List[int]``)

   **Returns:** ``None``

.. method:: synthesizeMipmapPyramid(source, nLevels, copyLocally)

   Wraps a single-resolution `Source` in a synthetic mipmap pyramid. BVV's `VolumeRenderer` requires multiple resolution levels to pick a LOD; without one it throws on every repaint. Use this for non-pyramidal N5/Zarr sources that cannot be re-exported with a real pyramid.

Level 0 is either a local, cell-based copy of the source (see `ImgUtils.materializeTiled(net.imglib2.RandomAccessibleInterval<T>, int)`), or, if `copyLocally` is false, the source itself (as a zero-min view: a non-zero min of the source is moved into the returned source's transform, so its position in world space is unchanged). Each extra level doubles the previous step size along X/Y/Z, matching how a real N5/Zarr multiscale pyramid is laid out. Extra levels are averaged (2x2x2) from the previous level (see `averagedLevel(net.imglib2.RandomAccessibleInterval<T>)`) and computed lazily, on demand, so they cost no heap up front

   **Signature:** ``synthesizeMipmapPyramid(Source, int, boolean) -> Source``

   **Parameters:**

   * **source** (``Any``): - the single-level source to wrap
   * **nLevels** (``int``)
   * **copyLocally** (``bool``)

   **Returns:** (``Any``) a multi-resolution `Source` wrapping `source`, or `source` unchanged if it already has more than one level

.. method:: trackQueue(queue)

   Makes `syncQueuesWithViewer(bvv.vistools.BvvHandle)` aware of a fetch queue that feeds BVV

   **Signature:** ``trackQueue(CacheControl) -> void``

   **Parameters:**

   * **queue** (``Any``)

   **Returns:** ``None``

.. method:: warnIfLikelyRemoteImgPlus(img, pathOrUrl)

   Diagnostic-only warning for the plain `ImgPlus` fallback path (see `SpimDataUtils.resolvePathToSource(String)`). Unlike `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`/ `warnIfLikelySimpleStack(bdv.viewer.Source<?>, int)`, an `ImgPlus` always has a single mipmap level, so BVV always renders it via the non-pyramid-aware `SimpleStack3D` path regardless of pixel type or backing storage - there is no "is it structurally eligible for MULTIRESOLUTION" question to ask here the way there is for `AbstractSpimData`/`N5Sources`.

`resolvePathToSource` already knows this at resolution time - a remote `ImgPlus` is only ever produced by its own URL fallback branch (`ImgUtils.open(url)`) - so this simply carries that signal forward rather than trying to re-derive it by introspecting the RAI (which, for a lazily-opened remote image, may not even be a recognizable cache type)

   **Signature:** ``warnIfLikelyRemoteImgPlus(ImgPlus, String) -> void``

   **Parameters:**

   * **img** (``Any``): - the resolved
   * **pathOrUrl** (``str``): about to be shown in BVV

   **Returns:** ``None``

.. method:: warnIfLikelySimpleStack(source, timepoint)

   Read-only counterpart to `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` for `AbstractSpimData` sources (BDV-XML/HDF5, IMS): logs a warning if `source` looks likely to fall back to BVV's non-pyramid-aware `SimpleStack3D` renderer, without attempting to prevent it.

Unlike the `SpimDataUtils.N5Sources` path, 
```
BvvFunctions.show(AbstractSpimData,
 BvvOptions)
```
 builds its own `Source` instances internally (via `BigDataViewer#initSetups`), so there is no hook to call `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` on the actual instance before it first renders. `inferSourceStackType`'s check is a pure function of the source's structural properties (pixel type, whether level 0 is an `AbstractCellImg`), not of instance identity or any per-instance cached state, so running the same check here - on the `Source` SNT already has a handle to after `show()` returns - still gives an accurate answer; it just can't change the outcome

This is diagnostic only: it neither prefetches nor forces a stack type, so it carries none of `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`/`prefetchForShow(bdv.viewer.Source<T>, int)`'s risk of misbehaving on a source shape this hasn't been exercised against - it only makes a slow first paint traceable in the log after the fact, for whichever `AbstractSpimData` backend produced it

   **Signature:** ``warnIfLikelySimpleStack(Source, int) -> void``

   **Parameters:**

   * **source** (``Any``): - the (already-shown) source to inspect
   * **timepoint** (``int``)

   **Returns:** ``None``


ColorMaps
---------

.. method:: applyPlasma(imp)

   Applies the "plasma" colormap to the specified (non-RGB) image

   **Signature:** ``applyPlasma(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``): - A non-RGB image

   **Returns:** ``None``

.. method:: applyViridis(imp)

   Applies the "viridis" colormap to the specified (non-RGB) image

   **Signature:** ``applyViridis(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``): - A non-RGB image

   **Returns:** ``None``

.. method:: get(name)

   Returns a 'core' color table from its title

   **Signature:** ``get(String) -> ColorTable``

   **Parameters:**

   * **name** (``str``): - the color table name (e.g., "fire", "viridis", etc)

   **Returns:** (``Any``) the color table


ConvexHull2D
------------

.. method:: intersection(convexHulls)

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``intersection(AbstractConvexHull[]) -> ConvexHull2D``

   **Parameters:**

   * **convexHulls** (``List[Any]``)

   **Returns:** ``ConvexHull2D``

.. method:: intersectionBox(convexHulls)

   **Signature:** ``intersectionBox(AbstractConvexHull[]) -> BoundingBox``

   **Parameters:**

   * **convexHulls** (``List[Any]``)

   **Returns:** ``BoundingBox``


ConvexHull3D
------------

.. method:: intersection(convexHulls)

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``intersection(AbstractConvexHull[]) -> ConvexHull3D``

   **Parameters:**

   * **convexHulls** (``List[Any]``)

   **Returns:** ``ConvexHull3D``

.. method:: intersectionBox(convexHulls)

   **Signature:** ``intersectionBox(AbstractConvexHull[]) -> BoundingBox``

   **Parameters:**

   * **convexHulls** (``List[Any]``)

   **Returns:** ``BoundingBox``


ConvexHullAnalyzer
------------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: dump(table)

   **Signature:** ``dump(SNTTable) -> void``

   **Parameters:**

   * **table** (``SNTTable``)

   **Returns:** ``None``

.. method:: get(metric)

   Gets the value of a specific convex hull metric.

Retrieves the computed value for the specified metric name. The metric must be one of the supported metrics returned by `supportedMetrics()`.

   **Signature:** ``get(String) -> double``

   **Parameters:**

   * **metric** (``str``): - the name of the metric to retrieve

   **Returns:** (``float``) the computed value for the metric

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


CrossSectionUtils
-----------------

.. method:: applyAnnularMask(fp, innerRadius, outerRadius)

   Applies an annular mask to a cross-section `FloatProcessor`. Pixels outside the annulus (closer than `innerRadius` or farther than `outerRadius` from center) are set to `Float.NaN`.

   **Signature:** ``applyAnnularMask(FloatProcessor, double, double) -> void``

   **Parameters:**

   * **fp** (``Any``): - the cross-section image to mask (modified in place)
   * **innerRadius** (``float``)
   * **outerRadius** (``float``)

   **Returns:** ``None``

.. method:: applyAnnularMask1D(profile, innerRadius, outerRadius)

   Applies an annular mask to a 1D profile. Samples closer than `innerRadius` or farther than `outerRadius` from the center are set to `Float.NaN`.

   **Signature:** ``applyAnnularMask1D(float[], double, double) -> void``

   **Parameters:**

   * **profile** (``List[float]``): - the profile array (modified in place)
   * **innerRadius** (``float``)
   * **outerRadius** (``float``)

   **Returns:** ``None``

.. method:: backProject(gridX, gridY, side, scaleIso, ox, oy, oz, aBasis, bBasis)

   Back-projects a 2D cross-section grid coordinate to 3D world coordinates.

   **Signature:** ``backProject(int, int, int, double, double, double, double, double[], double[]) -> double[]``

   **Parameters:**

   * **gridX** (``int``): - grid X coordinate (pixel in the cross-section)
   * **gridY** (``int``)
   * **side** (``int``)
   * **scaleIso** (``float``)
   * **ox** (``float``)
   * **oy** (``float``)
   * **oz** (``float``)
   * **aBasis** (``List[float]``)
   * **bBasis** (``List[float]``)

   **Returns:** (``List[float]``) `double[3]` world coordinates `{x, y, z}`

.. method:: findMaxima1D(profile, prominence)

   Finds local maxima in a 1D profile using prominence-based filtering. A sample is a local maximum if it is strictly greater than both its neighbors (ignoring NaN) and its prominence exceeds the threshold. Prominence is defined as the peak value minus the highest saddle point connecting the peak to any higher peak (or the profile boundary).

   **Signature:** ``findMaxima1D(float[], double) -> int[]``

   **Parameters:**

   * **profile** (``List[float]``): - the 1D intensity profile (may contain NaN for masked regions)
   * **prominence** (``float``)

   **Returns:** (``List[int]``) array of indices into `profile` where maxima were found

.. method:: findMinima1D(profile, prominence)

   Finds local minima in a 1D profile using prominence-based filtering. Symmetric inversion of `findMaxima1D(float[], double)`: a sample is a local minimum if it is strictly less than both its neighbors (ignoring NaN) and its prominence (the height it would need to climb to escape the basin and reach a deeper minimum, or the profile boundary) exceeds the threshold.

Useful for detecting localized intensity valleys along a path's intensity profile -- the inverse of finding peaks.

   **Signature:** ``findMinima1D(float[], double) -> int[]``

   **Parameters:**

   * **profile** (``List[float]``): - the 1D intensity profile (may contain NaN for masked regions)
   * **prominence** (``float``)

   **Returns:** (``List[int]``) array of indices into `profile` where minima were found

.. method:: sampleCrossSection(side, scaleA, scaleB, ox, oy, oz, aBasis, bBasis, xSpacing, ySpacing, zSpacing, offsetX, offsetY, offsetZ, realAccess)

   Samples a square cross-section of an image on the plane perpendicular to a path tangent at a given node position. The section is centered on the node and oriented according to the precomputed basis vectors.

   **Signature:** ``sampleCrossSection(int, double, double, double, double, double, double[], double[], double, double, double, double, double, double, RealRandomAccess) -> FloatProcessor``

   **Parameters:**

   * **side** (``int``): - grid size in pixels (width = height = side)
   * **scaleA** (``float``)
   * **scaleB** (``float``)
   * **ox** (``float``)
   * **oy** (``float``)
   * **oz** (``float``)
   * **aBasis** (``List[float]``)
   * **bBasis** (``List[float]``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)
   * **offsetX** (``float``)
   * **offsetY** (``float``)
   * **offsetZ** (``float``)
   * **realAccess** (``Any``)

   **Returns:** (``Any``) the sampled cross-section as a `FloatProcessor`


CrossoverFinder
---------------

.. method:: find(paths, cfg)

   Entry point: detect crossover events for a collection of paths using the given config.

   **Signature:** ``find(Collection, Config) -> List``

   **Parameters:**

   * **paths** (``List[Any]``): - the collection of paths
   * **cfg** (``Any``)

   **Returns:** ``List[Any]``


CurationManager
---------------

.. method:: calibrateFromTrees(trees)

   Calibrates thresholds from the given in-memory trees, enables live monitoring, runs a full scan, and switches SNTUI to the Assistant tab. Intended to be called programmatically after autotracing completes.

   **Signature:** ``calibrateFromTrees(List) -> void``

   **Parameters:**

   * **trees** (``List[Any]``): - the freshly traced trees to calibrate from

   **Returns:** ``None``

.. method:: dispose()

   Unregisters this panel from the monitor. Should be called when the panel is removed from the UI to avoid listener leaks.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: refreshFromMonitor()

   Refreshes all UI controls (spinners, checkboxes, toggle) from the monitor's current state. Called after loading a preset or restoring a session.

   **Signature:** ``refreshFromMonitor() -> void``

   **Returns:** ``None``

.. method:: warningsUpdated(warnings)

   Description copied from interface: `PlausibilityMonitor.WarningListener`

   **Signature:** ``warningsUpdated(List) -> void``

   **Parameters:**

   * **warnings** (``List[Any]``): - the current (immutable) list of warnings

   **Returns:** ``None``


DefaultSearchNode
-----------------

.. method:: compareTo(o)

   **Signature:** ``compareTo(DefaultSearchNode) -> int``

   **Parameters:**

   * **o** (``DefaultSearchNode``)

   **Returns:** ``int``

.. method:: equals(o)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **o** (``Any``)

   **Returns:** ``bool``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``


DelineationsManager
-------------------

.. method:: load(delineationROIs)

   Loads delineations from a list of area ROIs. Each ROI is mapped to a delineation entry, and path nodes whose XY coordinates fall within the ROI are assigned to the corresponding delineation. If an ROI has been renamed or colored (stroke or fill), those properties are transferred to the delineation.

   **Signature:** ``load(List) -> int``

   **Parameters:**

   * **delineationROIs** (``List[Any]``): - the area ROIs to import;

   **Returns:** (``int``) the number of ROIs successfully associated with at least one path

.. method:: reset()

   Deletes all delineations.

   **Signature:** ``reset() -> void``

   **Returns:** ``None``


Detection
---------

.. method:: toSNTPoint()

   **Signature:** ``toSNTPoint() -> PointInImage``

   **Returns:** ``PointInImage``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``

.. method:: xyzct()

   **Signature:** ``xyzct() -> double[]``

   **Returns:** ``List[float]``


DetectorUtils
-------------

.. method:: deduplicate(detections, mergingDistance)

   **Signature:** ``deduplicate(List, double) -> List``

   **Parameters:**

   * **detections** (``List[Any]``)
   * **mergingDistance** (``float``)

   **Returns:** ``List[Any]``

.. method:: interpolateRadius(radii, idx, fallback)

   **Signature:** ``interpolateRadius(double[], int, double) -> double``

   **Parameters:**

   * **radii** (``List[float]``)
   * **idx** (``int``)
   * **fallback** (``float``)

   **Returns:** ``float``

.. method:: prepareRadii(path)

   **Signature:** ``prepareRadii(Path) -> double[]``

   **Parameters:**

   * **path** (``Path``)

   **Returns:** ``List[float]``

.. method:: sampleDistances(paths, edt)

   **Signature:** ``sampleDistances(Collection, Img) -> double[]``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **edt** (``Any``)

   **Returns:** ``List[float]``

.. method:: sampleDistancesWithIndices(path, edt)

   **Signature:** ``sampleDistancesWithIndices(Path, Img) -> List``

   **Parameters:**

   * **path** (``Path``)
   * **edt** (``Any``)

   **Returns:** ``List[Any]``


Difference
----------

.. method:: costMovingTo(valueAtNewPoint)

   **Signature:** ``costMovingTo(double) -> double``

   **Parameters:**

   * **valueAtNewPoint** (``float``)

   **Returns:** ``float``

.. method:: minStepCost()

   **Signature:** ``minStepCost() -> double``

   **Returns:** ``float``


DifferenceSq
------------

.. method:: costMovingTo(valueAtNewPoint)

   **Signature:** ``costMovingTo(double) -> double``

   **Parameters:**

   * **valueAtNewPoint** (``float``)

   **Returns:** ``float``

.. method:: minStepCost()

   **Signature:** ``minStepCost() -> double``

   **Returns:** ``float``


Dijkstra
--------

.. method:: estimateCostToGoal(current_x, current_y, current_z, goal_x, goal_y, goal_z)

   **Signature:** ``estimateCostToGoal(int, int, int, int, int, int) -> double``

   **Parameters:**

   * **current_x** (``int``)
   * **current_y** (``int``)
   * **current_z** (``int``)
   * **goal_x** (``int``)
   * **goal_y** (``int``)
   * **goal_z** (``int``)

   **Returns:** ``float``


DirectedWeightedGraph
---------------------

.. method:: applyEdges(operator)

   **Signature:** ``applyEdges(UnaryOperator) -> void``

   **Parameters:**

   * **operator** (``Any``)

   **Returns:** ``None``

.. method:: applyVertices(operator)

   **Signature:** ``applyVertices(UnaryOperator) -> void``

   **Parameters:**

   * **operator** (``Any``)

   **Returns:** ``None``

.. method:: assignEdgeWeightsEuclidean()

   **Signature:** ``assignEdgeWeightsEuclidean() -> void``

   **Returns:** ``None``

.. method:: filterEdges(predicate)

   **Signature:** ``filterEdges(Predicate) -> void``

   **Parameters:**

   * **predicate** (``Any``)

   **Returns:** ``None``

.. method:: filterVertices(predicate)

   **Signature:** ``filterVertices(Predicate) -> void``

   **Parameters:**

   * **predicate** (``Any``)

   **Returns:** ``None``

.. method:: scale(xScale, yScale, zScale, updateEdgeWeightsEuclidean)

   **Signature:** ``scale(double, double, double, boolean) -> void``

   **Parameters:**

   * **xScale** (``float``)
   * **yScale** (``float``)
   * **zScale** (``float``)
   * **updateEdgeWeightsEuclidean** (``bool``)

   **Returns:** ``None``

.. method:: show()

   **Signature:** ``show() -> Window``

   **Returns:** ``Any``

.. method:: sumEdgeWeights()

   **Signature:** ``sumEdgeWeights() -> double``

   **Returns:** ``float``

.. method:: updateVertexProperties()

   **Signature:** ``updateVertexProperties() -> void``

   **Returns:** ``None``

.. method:: vertexSet(lr)

   **Signature:** ``vertexSet(char) -> Set``

   **Parameters:**

   * **lr** (``str``)

   **Returns:** ``Set[Any]``


DirectedWeightedSubgraph
------------------------

.. method:: show()

   **Signature:** ``show() -> Window``

   **Returns:** ``Any``

.. method:: sumEdgeWeights(adjusted)

   **Signature:** ``sumEdgeWeights(boolean) -> double``

   **Parameters:**

   * **adjusted** (``bool``)

   **Returns:** ``float``


DiskBackedGWDTTracer
--------------------

.. method:: create(source)

   **Signature:** ``create(ImagePlus) -> DiskBackedGWDTTracer``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``DiskBackedGWDTTracer``

.. method:: findRoot(source, spacing)

   **Signature:** ``findRoot(RandomAccessibleInterval, double[]) -> long[]``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[int]``

.. method:: findRootPhysical(source, spacing)

   **Signature:** ``findRootPhysical(RandomAccessibleInterval, double[]) -> double[]``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: findThickestPoint(source, threshold, spacing)

   **Signature:** ``findThickestPoint(RandomAccessibleInterval, double, double[]) -> long[]``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[int]``

.. method:: findThickestPointPhysical(source, threshold, spacing)

   **Signature:** ``findThickestPointPhysical(RandomAccessibleInterval, double, double[]) -> double[]``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: honoredSeedRoles()

   **Signature:** ``honoredSeedRoles() -> EnumSet``

   **Returns:** ``Any``

.. method:: iterateNeighbors(delta, dim, nDims, action)

   **Signature:** ``iterateNeighbors(int[], int, int, Runnable) -> void``

   **Parameters:**

   * **delta** (``List[int]``)
   * **dim** (``int``)
   * **nDims** (``int``)
   * **action** (``Any``)

   **Returns:** ``None``

.. method:: posToIndex(pos, dims)

   **Signature:** ``posToIndex(long[], long[]) -> long``

   **Parameters:**

   * **pos** (``List[int]``)
   * **dims** (``List[int]``)

   **Returns:** ``int``

.. method:: trace()

   **Signature:** ``trace() -> Tree``

   **Returns:** ``Tree``

.. method:: traceMultiSoma(somas)

   **Signature:** ``traceMultiSoma(List) -> List``

   **Parameters:**

   * **somas** (``List[Any]``)

   **Returns:** ``List[Any]``

.. method:: traceToGraph()

   **Signature:** ``traceToGraph() -> DirectedWeightedGraph``

   **Returns:** ``DirectedWeightedGraph``

.. method:: traceTrees()

   **Signature:** ``traceTrees() -> List``

   **Returns:** ``List[Any]``


DiskBackedStorageBackend
------------------------

.. method:: buildGraph(dims, spacing, threshold)

   **Signature:** ``buildGraph(long[], double[], double) -> DirectedWeightedGraph``

   **Parameters:**

   * **dims** (``List[int]``)
   * **spacing** (``List[float]``)
   * **threshold** (``float``)

   **Returns:** ``DirectedWeightedGraph``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: estimateMemoryUsage()

   **Signature:** ``estimateMemoryUsage() -> long``

   **Returns:** ``int``

.. method:: initializeFastMarching(dims, seedIndex)

   **Signature:** ``initializeFastMarching(long[], long) -> void``

   **Parameters:**

   * **dims** (``List[int]``)
   * **seedIndex** (``int``)

   **Returns:** ``None``

.. method:: reinitializeFastMarching(dims, seedIndex, excludedIndices)

   **Signature:** ``reinitializeFastMarching(long[], long, Set) -> void``

   **Parameters:**

   * **dims** (``List[int]``)
   * **seedIndex** (``int``)
   * **excludedIndices** (``Set[Any]``)

   **Returns:** ``None``


Euclidean
---------

.. method:: estimateCostToGoal(source_x, source_y, source_z, target_x, target_y, target_z)

   **Signature:** ``estimateCostToGoal(int, int, int, int, int, int) -> double``

   **Parameters:**

   * **source_x** (``int``)
   * **source_y** (``int``)
   * **source_z** (``int``)
   * **target_x** (``int``)
   * **target_y** (``int``)
   * **target_z** (``int``)

   **Returns:** ``float``


Fill
----

.. method:: add(x, y, z, distance, previous, open)

   Adds a node to the filled structure.

   **Signature:** ``add(int, int, int, double, int, boolean) -> void``

   **Parameters:**

   * **x** (``int``): - the x-coordinate of the node
   * **y** (``int``)
   * **z** (``int``)
   * **distance** (``float``)
   * **previous** (``int``)
   * **open** (``bool``)

   **Returns:** ``None``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``


FillConverter
-------------

.. method:: convert(in, out)

   Map values between the input and output at fill voxel positions.

   **Signature:** ``convert(RandomAccessible, RandomAccessible) -> void``

   **Parameters:**

   * **in** (``Any``): - the input rai
   * **out** (``Any``)

   **Returns:** ``None``

.. method:: convertBinary(out)

   Set 1 at fill voxel positions.

   **Signature:** ``convertBinary(RandomAccessible) -> void``

   **Parameters:**

   * **out** (``Any``): - the output rai

   **Returns:** ``None``

.. method:: convertDistance(out)

   Map the node distance measure to fill voxel positions. This corresponds to the g-score of a node assigned during the Dijkstra search. This value is stored as `Double`.

   **Signature:** ``convertDistance(RandomAccessible) -> void``

   **Parameters:**

   * **out** (``Any``): - the output rai

   **Returns:** ``None``

.. method:: convertLabels(out)

   Map the fill component label to fill voxel positions. The concrete `IntegerType` should be chosen based on the cardinality of the given `Collection` of `FillerThread`s. For example, if there are less than 256 `FillerThread`s, choose `UnsignedByteType`. If there are more than 255 but less than 65536, choose `UnsignedShortType`, etc. Fill components are assigned labels based on their order in the collection. If you want to ensure labels are assigned based on insertion order, make sure to use an ordered collection such as `List` or `LinkedHashSet`. The first component will have label == 1, the second label == 2, and so on. The label 0 is not assigned to any voxel positions. 0-valued voxels may already exist in the output image.

   **Signature:** ``convertLabels(RandomAccessible) -> void``

   **Parameters:**

   * **out** (``Any``): - the output rai

   **Returns:** ``None``


FillManagerUI
-------------

.. method:: actionPerformed(ae)

   **Signature:** ``actionPerformed(ActionEvent) -> void``

   **Parameters:**

   * **ae** (``Any``)

   **Returns:** ``None``

.. method:: finished(source, success)

   **Signature:** ``finished(SearchInterface, boolean) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **success** (``bool``)

   **Returns:** ``None``

.. method:: maximumDistanceCompletelyExplored(source, f)

   **Signature:** ``maximumDistanceCompletelyExplored(FillerThread, double) -> void``

   **Parameters:**

   * **source** (``FillerThread``)
   * **f** (``float``)

   **Returns:** ``None``

.. method:: pointsInSearch(source, inOpen, inClosed)

   **Signature:** ``pointsInSearch(SearchInterface, long, long) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **inOpen** (``int``)
   * **inClosed** (``int``)

   **Returns:** ``None``

.. method:: threadStatus(source, currentStatus)

   **Signature:** ``threadStatus(SearchInterface, int) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **currentStatus** (``int``)

   **Returns:** ``None``


FillerThread
------------

.. method:: createNewNode(x, y, z, g, h, predecessor, searchStatus)

   **Signature:** ``createNewNode(int, int, int, double, double, DefaultSearchNode, byte) -> DefaultSearchNode``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)
   * **g** (``float``)
   * **h** (``float``)
   * **predecessor** (``DefaultSearchNode``)
   * **searchStatus** (``int``)

   **Returns:** ``DefaultSearchNode``

.. method:: fromFill(imagePlus, stats, fill)

   **Signature:** ``fromFill(ImagePlus, ImageStatistics, Fill) -> FillerThread``

   **Parameters:**

   * **imagePlus** (``Any``)
   * **stats** (``Any``)
   * **fill** (``Fill``)

   **Returns:** ``FillerThread``

.. method:: pointsConsideredInSearch()

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(success)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **success** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


FillerThreadArtist
------------------

.. method:: anyNodeUnderThreshold(x, y, z, threshold)

   **Signature:** ``anyNodeUnderThreshold(int, int, int, double) -> DefaultSearchNode``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)
   * **threshold** (``float``)

   **Returns:** ``DefaultSearchNode``


Frangi
------

.. method:: accept(output)

   **Signature:** ``accept(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **output** (``Any``)

   **Returns:** ``None``

.. method:: apply(img, scales)

   Apply multiscale Frangi vesselness filter to an ImgPlus.

   **Signature:** ``apply(ImgPlus, double[]) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``): - input image (2D or 3D) with calibrated axes
   * **scales** (``List[float]``)

   **Returns:** (``Any``) filtered ImgPlus with same axes as input

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


GWDTTracer
----------

.. method:: create(source)

   **Signature:** ``create(ImagePlus) -> GWDTTracer``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``GWDTTracer``

.. method:: findRoot(source, spacing)

   **Signature:** ``findRoot(RandomAccessibleInterval, double[]) -> long[]``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[int]``

.. method:: findRootPhysical(source, spacing)

   **Signature:** ``findRootPhysical(RandomAccessibleInterval, double[]) -> double[]``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: findThickestPoint(source, threshold, spacing)

   **Signature:** ``findThickestPoint(RandomAccessibleInterval, double, double[]) -> long[]``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[int]``

.. method:: findThickestPointPhysical(source, threshold, spacing)

   **Signature:** ``findThickestPointPhysical(RandomAccessibleInterval, double, double[]) -> double[]``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: honoredSeedRoles()

   **Signature:** ``honoredSeedRoles() -> EnumSet``

   **Returns:** ``Any``

.. method:: iterateNeighbors(delta, dim, nDims, action)

   **Signature:** ``iterateNeighbors(int[], int, int, Runnable) -> void``

   **Parameters:**

   * **delta** (``List[int]``)
   * **dim** (``int``)
   * **nDims** (``int``)
   * **action** (``Any``)

   **Returns:** ``None``

.. method:: posToIndex(pos, dims)

   **Signature:** ``posToIndex(long[], long[]) -> long``

   **Parameters:**

   * **pos** (``List[int]``)
   * **dims** (``List[int]``)

   **Returns:** ``int``

.. method:: trace()

   **Signature:** ``trace() -> Tree``

   **Returns:** ``Tree``

.. method:: traceMultiSoma(somas)

   **Signature:** ``traceMultiSoma(List) -> List``

   **Parameters:**

   * **somas** (``List[Any]``)

   **Returns:** ``List[Any]``

.. method:: traceToGraph()

   **Signature:** ``traceToGraph() -> DirectedWeightedGraph``

   **Returns:** ``DirectedWeightedGraph``

.. method:: traceTrees()

   **Signature:** ``traceTrees() -> List``

   **Returns:** ``List[Any]``


GWDTTracerFactory
-----------------

.. method:: create(source)

   **Signature:** ``create(ImagePlus) -> AbstractGWDTTracer``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``Any``

.. method:: estimateWorkingMemoryMB(dims)

   **Signature:** ``estimateWorkingMemoryMB(long[]) -> long``

   **Parameters:**

   * **dims** (``List[int]``)

   **Returns:** ``int``

.. method:: forceArray(source, spacing)

   **Signature:** ``forceArray(RandomAccessibleInterval, double[]) -> GWDTTracer``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``GWDTTracer``

.. method:: forceDisk(source, spacing)

   **Signature:** ``forceDisk(RandomAccessibleInterval, double[]) -> DiskBackedGWDTTracer``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``DiskBackedGWDTTracer``

.. method:: forceSparse(source, spacing)

   **Signature:** ``forceSparse(RandomAccessibleInterval, double[]) -> SparseGWDTTracer``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``SparseGWDTTracer``

.. method:: printMemoryStatus()

   **Signature:** ``printMemoryStatus() -> void``

   **Returns:** ``None``

.. method:: recommendBackend(dims)

   **Signature:** ``recommendBackend(long[]) -> String``

   **Parameters:**

   * **dims** (``List[int]``)

   **Returns:** ``str``


GroupedTreeStatistics
---------------------

.. method:: anovaPValue(measurement)

   Computes the one-way ANOVA P-value for all the groups being analyzed. It is assumed that data fulfills basic assumptions on normality, variance homogeneity, sample size, etc.

   **Signature:** ``anovaPValue(String) -> double``

   **Parameters:**

   * **measurement** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``float``) the p-value

.. method:: tTest(measurement, group1Label, group2Label)

   Computes a two-sample, two-tailed t-test P-value for two of groups being analyzed. It is assumed that data fulfills basic assumptions on normality, variance homogeneity, etc.

   **Signature:** ``tTest(String, String, String) -> double``

   **Parameters:**

   * **measurement** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)
   * **group1Label** (``str``)
   * **group2Label** (``str``)

   **Returns:** (``float``) the p-value


Heuristic
---------

.. method:: estimateCostToGoal(current_x, current_y, current_z, goal_x, goal_y, goal_z)

   **Signature:** ``estimateCostToGoal(int, int, int, int, int, int) -> double``

   **Parameters:**

   * **current_x** (``int``)
   * **current_y** (``int``)
   * **current_z** (``int``)
   * **goal_x** (``int``)
   * **goal_y** (``int``)
   * **goal_z** (``int``)

   **Returns:** ``float``


IOUtils
-------

.. method:: detectFormat(file)

   Guesses the format of a reconstruction file from its first bytes. See `detectFormat(InputStream, boolean)`

   **Signature:** ``detectFormat(File) -> ReconstructionFormat``

   **Parameters:**

   * **file** (``str``): - the file to be inspected

   **Returns:** (``Any``) the detected format


ImageParser2D
-------------

.. method:: maxPossibleRadius()

   **Signature:** ``maxPossibleRadius() -> double``

   **Returns:** ``float``

.. method:: parse()

   **Signature:** ``parse() -> void``

   **Returns:** ``None``

.. method:: reset()

   **Signature:** ``reset() -> void``

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: successful()

   **Signature:** ``successful() -> boolean``

   **Returns:** ``bool``

.. method:: terminate()

   **Signature:** ``terminate() -> void``

   **Returns:** ``None``


ImageParser3D
-------------

.. method:: maxPossibleRadius()

   **Signature:** ``maxPossibleRadius() -> double``

   **Returns:** ``float``

.. method:: parse()

   **Signature:** ``parse() -> void``

   **Returns:** ``None``

.. method:: reset()

   **Signature:** ``reset() -> void``

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: successful()

   **Signature:** ``successful() -> boolean``

   **Returns:** ``bool``

.. method:: terminate()

   **Signature:** ``terminate() -> void``

   **Returns:** ``None``


ImgUtils
--------

.. method:: axisReport(img)

   Builds a one-line diagnostic string listing all axes of an `ImgPlus` with their type, size, and scale. Used by `open(String)` to report the axis layout of freshly opened images.

   **Signature:** ``axisReport(ImgPlus) -> String``

   **Parameters:**

   * **img** (``Any``): - the image to describe

   **Returns:** (``str``) a human-readable axis summary, e.g. `"Axes: [X 512 (1.0µm)] [Y 512 (1.0µm)] [Z 60 (2.0µm)] [Channel 3 (1.0)]"`

.. method:: createIntervals(sourceDimensions, blockDimensions)

   Partition the source dimensions into a list of `Interval`s with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have slightly different dimensions.

   **Signature:** ``createIntervals(long[], long[]) -> List``

   **Parameters:**

   * **sourceDimensions** (``List[int]``): - the source dimensions
   * **blockDimensions** (``List[int]``)

   **Returns:** (``List[Any]``) the list of Intervals

.. method:: crop(img, bboxMin, bboxMax, materialize)

   Crop a region from a RandomAccessibleInterval using (x, y, z) pixel coordinates.

For RAIs without axis metadata, assumes ZYX dimension order. Returns a view (no data copy) with the specified bounds, clamped to image bounds.

**Important:** This method assumes ZYX dimension order (dim0=Z, dim1=Y, dim2=X), which is common for OME-ZARR and N5 datasets. For images with different axis orders, wrap as ImgPlus with proper axis metadata and use `crop(ImgPlus, long[], long[], boolean)`.

   **Signature:** ``crop(ImgPlus, long[], long[], boolean) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``)
   * **bboxMin** (``List[int]``)
   * **bboxMax** (``List[int]``)
   * **materialize** (``bool``)

   **Returns:** ``Any``

.. method:: depthCodedProjection(rai, axis, min, max, lut, displayMin, displayMax)

   Computes a depth color-coded slab max-intensity projection (analogous to ImageJ's "Temporal-Color Code" or "Hyperstack Depth Color" tools). Hue is determined by the depth of the maximum within the slab, and brightness by the intensity of the maximum.

   **Signature:** ``depthCodedProjection(RandomAccessibleInterval, int, long, long, ColorTable, double, double) -> ImagePlus``

   **Parameters:**

   * **rai** (``Any``): - the 3D single-channel source
   * **axis** (``int``)
   * **min** (``int``)
   * **max** (``int``)
   * **lut** (``Any``)
   * **displayMin** (``float``)
   * **displayMax** (``float``)

   **Returns:** (``Any``) a 2D RGB image (uncalibrated)

.. method:: downsampleToFit(imgPlus, maxDimSize)

   Same as `downsampleToFit(ImgPlus, int)`, but additionally caps the number of voxels of the spatial (X, Y, Z) volume, e.g., to fit BVV's single-texture capacity. After satisfying `maxDimSize`, the step of the axis with the finest physical voxel size is repeatedly increased until the cap is met, which keeps the resulting voxels as isotropic as possible

   **Signature:** ``downsampleToFit(ImgPlus, int) -> ImgPlus``

   **Parameters:**

   * **imgPlus** (``Any``): - the image to downsample
   * **maxDimSize** (``int``)

   **Returns:** (``Any``) a (possibly lazy) downsampled ImgPlus, or the original if no limit is exceeded

.. method:: dropSingletonDimensions(img)

   Remove singleton dimensions from an ImgPlus, preserving axis metadata.

   **Signature:** ``dropSingletonDimensions(ImgPlus) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``): - the source ImgPlus (e.g., 5D XYZCT with C=1, T=1)

   **Returns:** (``Any``) ImgPlus with singleton dimensions removed

.. method:: exceedsDimension(imgPlus, maxDimSize)

   Checks whether any spatial dimension of an `ImgPlus` exceeds the given limit. Only X, Y, and Z axes are considered.

   **Signature:** ``exceedsDimension(ImgPlus, int) -> boolean``

   **Parameters:**

   * **imgPlus** (``Any``): - the image to check
   * **maxDimSize** (``int``)

   **Returns:** (``bool``) `true` if at least one spatial dimension exceeds the limit

.. method:: findSpatialAxisIndices(img)

   Find dimension indices for X, Y, Z axes in an ImgPlus.

   **Signature:** ``findSpatialAxisIndices(ImgPlus) -> int[]``

   **Parameters:**

   * **img** (``Any``): - the ImgPlus

   **Returns:** (``List[int]``) int array {xIdx, yIdx, zIdx}, with -1 for missing axes

.. method:: findSpatialAxisIndicesWithFallback(img)

   Find dimension indices for X, Y, Z axes, with fallback to assumed ZYX order.

   **Signature:** ``findSpatialAxisIndicesWithFallback(ImgPlus) -> int[]``

   **Parameters:**

   * **img** (``Any``): - the ImgPlus

   **Returns:** (``List[int]``) int array {xIdx, yIdx, zIdx}

.. method:: haveSameSpatialDimensions(imp, rai)

   Checks whether an `ImagePlus` and a `RandomAccessibleInterval` have compatible spatial dimensions (width, height, and optionally depth).

   **Signature:** ``haveSameSpatialDimensions(ImagePlus, RandomAccessibleInterval) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the ImagePlus
   * **rai** (``Any``)

   **Returns:** (``bool``) `true` if spatial dimensions match

.. method:: impToRealRai5d(imp)

   Wrap an `ImagePlus` to a `RandomAccessibleInterval` such that the number of dimensions in the resulting rai is 5 and the axis order is XYCZT. Axes that are not present in the input imp have singleton dimensions in the rai.

For example, given a 2D, multichannel imp, the dimensions of the result rai are [ |X|, |Y|, |C|, 1, 1 ]

   **Signature:** ``impToRealRai5d(ImagePlus) -> RandomAccessibleInterval``

   **Parameters:**

   * **imp** (``Any``): -

   **Returns:** (``Any``) the 5D rai

.. method:: materialize(source)

   Copies a (possibly lazy/remote) view into a local, contiguous `ArrayImgFactory`-backed image. Use before repeated random-access operations on a view backed by something expensive to re-read, e.g. a remote N5/Zarr source.

   **Signature:** ``materialize(RandomAccessibleInterval) -> Img``

   **Parameters:**

   * **source** (``Any``): - the view to copy

   **Returns:** (``Any``) a local, fully-realized copy of `source`

.. method:: materializeTiled(source, cellSize)

   Copies a (possibly lazy/remote) view into a local `CellImg`. Unlike `materialize(net.imglib2.RandomAccessibleInterval<T>)`, the result is an `AbstractCellImg`, which is what BVV requires to stream tiles through its GPU cache instead of uploading the whole volume as a single 3D texture. It also avoids the 2^31 elements limit of `ArrayImg`

   **Signature:** ``materializeTiled(RandomAccessibleInterval, int) -> Img``

   **Parameters:**

   * **source** (``Any``): - the view to copy
   * **cellSize** (``int``)

   **Returns:** (``Any``) a local, zero-min, fully-realized, cell-based copy of `source`

.. method:: maxDimension(dimensions)

   **Signature:** ``maxDimension(long[]) -> int``

   **Parameters:**

   * **dimensions** (``List[int]``): -

   **Returns:** (``int``) the index of the largest dimension

.. method:: maxIntensityProjection(source)

   Computes a type-preserving max-intensity projection along the Z axis of an `ImgPlus`.

The Z axis is located via `Axes.Z` metadata, falling back to dim 2 if no labeled Z axis is found. The input pixel type `T` is preserved in the output, and the non-Z axes' calibration is copied across.

If the source has no Z axis (e.g., a 2D image), the source is returned unchanged. If the Z axis exists but has depth 1, a 2D copy is returned.

   **Signature:** ``maxIntensityProjection(ImgPlus) -> ImgPlus``

   **Parameters:**

   * **source** (``Any``): - the input image

   **Returns:** (``Any``) a 2D max-intensity projection preserving `T`, or the original source if it has no Z axis

.. method:: maxProjectionWithDepth(rai, axis, min, max)

   Computes a slab max-intensity projection of a (possibly lazy, e.g., cell-cached) image along an arbitrary axis, also keeping track of the depth at which each maximum occurs. The source is read plane by plane and only the 2D results are held in memory, so this is suitable for slabs of large datasets (see `maxIntensityProjection(ImgPlus)` for the ImgPlus/Z-only counterpart). To project a multichannel image, slice the channel first, e.g., with `Views.hyperSlice(RandomAccessibleInterval, int, long)`

   **Signature:** ``maxProjectionWithDepth(RandomAccessibleInterval, int, long, long) -> MaxProjection``

   **Parameters:**

   * **rai** (``Any``): - the 3D source
   * **axis** (``int``)
   * **min** (``int``)
   * **max** (``int``)

   **Returns:** (``Any``) the projection and its depth map

.. method:: normalizeToXYZ(img)

   Normalizes the axes of an `ImgPlus` for volume viewers and tracing: singleton axes are dropped and the remaining ones are ordered X, Y, Z, [C], [T], with no pixel copy.

- Unlabeled axes: if exactly 3 axes are present and none is labeled, they are assumed to be XYZ; if X and Y are labeled and a single third axis is unlabeled, it is assumed to be Z. Both cases are logged. Anything else unlabeled is rejected as ambiguous

- Images without a Z axis after singleton removal (2D, or 2D plus C/T) are returned as is: callers are expected to reject them as non-volumetric

- Images with Z but any other non-singleton axis than C or T (e.g., Position, Series) are rejected

Images already in the normalized layout are returned unchanged (same instance).

   **Signature:** ``normalizeToXYZ(ImgPlus) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``): - the source image

   **Returns:** (``Any``) the normalized image, or `img` if no change was needed

.. method:: open(file)

   Opens an image file as an ImgPlus.

   **Signature:** ``open(File) -> ImgPlus``

   **Parameters:**

   * **file** (``str``): - the file to open

   **Returns:** (``Any``) the opened image as ImgPlus, or null if opening fails

.. method:: outOfBounds(pos, min, max)

   Checks if pos is outside the bounds given by min and max

   **Signature:** ``outOfBounds(long[], long[], long[]) -> boolean``

   **Parameters:**

   * **pos** (``List[int]``): - the position to check
   * **min** (``List[int]``)
   * **max** (``List[int]``)

   **Returns:** (``bool``) true if pos is out of bounds, false otherwise

.. method:: permuteToXYZCT(img)

   Reorders the axes of an `ImgPlus` to the canonical XYZCT order expected by BVV and most ImageJ tools, applying swaps as needed. Axes not present in the image are left in place. No pixel data is copied.

This is useful when SCIFIO opens an image with axis order XYCZT (as ImageJ saves it) but BVV expects XYZCT, causing Z and C to be misinterpreted.

   **Signature:** ``permuteToXYZCT(ImgPlus) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``): - the source image; may have any axis order

   **Returns:** (``Any``) a new ImgPlus reordered to XYZCT (axes already in canonical order are returned unchanged)

.. method:: raiToImp(rai, title)

   Convert a `RandomAccessibleInterval` to an `ImagePlus`. If the input has 3 dimensions, the 3rd dimension is treated as depth.

   **Signature:** ``raiToImp(RandomAccessibleInterval, String) -> ImagePlus``

   **Parameters:**

   * **rai** (``Any``): - the source rai
   * **title** (``str``)

   **Returns:** (``Any``) the ImagePlus

.. method:: raiToImpFast(rai, title)

   Faster, single-copy alternative to `raiToImp(rai, title).duplicate()`. That combination routes through a lazy `ImageJVirtualStack` (which performs a full copy of every slice on first/every access) and then `ImagePlus.duplicate()` which performs a SECOND full, single-threaded copy of every stack slice. For large crops this double-copy, single-threaded path may be quite heavy.

This method instead copies `rai` directly into an `ImagePlusImg`-backed destination, in one pass, optionally multithreaded via `LoopBuilder`. `ImagePlusImg`'s own per-plane pixel arrays ARE the `ImagePlus`'s eventual `ImageStack` slice arrays (see `ByteImagePlus` and its siblings), so `ImagePlusImg.getImagePlus()` needs no further copy.

Only pixel types `ImagePlusImg` can back with a real `ImagePlus` are supported: in practice `byte`/`short`/`int`/`float` `NativeType`s, i.e. everything `raiToImp(RandomAccessibleInterval, String)` is normally called with here. Anything else throws `ImgLibException`; callers wanting a guaranteed-to-work fallback should catch it and fall back to `raiToImp(rai, title).duplicate()`.

   **Signature:** ``raiToImpFast(RandomAccessibleInterval, String) -> ImagePlus``

   **Parameters:**

   * **rai** (``Any``): - same contract as raiToImp(RandomAccessibleInterval, String)
   * **title** (``str``)

   **Returns:** (``Any``) an eagerly-populated, real (non-virtual) ImagePlus, built in a single copy pass

.. method:: resolveSpacing(img, explicit)

   Resolves pixel spacing for a `RandomAccessibleInterval`. If explicit spacing is provided and has enough dimensions, it is used directly. Otherwise, axis metadata is extracted from `ImgPlus` if available. Falls back to isotropic spacing of 1.0.

   **Signature:** ``resolveSpacing(RandomAccessibleInterval, double[]) -> double[]``

   **Parameters:**

   * **img** (``Any``): - the image
   * **explicit** (``List[float]``)

   **Returns:** (``List[float]``) pixel spacing array with one entry per image dimension

.. method:: sampledStats(in, maxSamples)

   Computes min, max, mean and (sample) standard deviation in a single pass. If the image holds more than `maxSamples` voxels, only a regular grid of voxels is visited (same stride along all dimensions), so the result is approximate. Exact otherwise.

   **Signature:** ``sampledStats(Iterable, long) -> double[]``

   **Parameters:**

   * **in** (``List[Any]``): - the data
   * **maxSamples** (``int``)

   **Returns:** (``List[float]``) {min, max, mean, stdDev, nSamples}

.. method:: save(img, filePath)

   Saves an image to disk as a TIFF file, converting pixel values to the specified output type before writing. This is the save counterpart of `open(String)`.

The image is materialized into a concrete in-memory `Img` of the requested type, so the caller must ensure sufficient RAM is available. Conversion is done via `ComplexType.setReal(double)`, which clamps values to the target type's range automatically (e.g. 16-bit unsigned values are clamped to [0, 65535]).

Typical usage: 
```
ImgUtils.save(rai, "/path/to/out.tif", new UnsignedShortType());
   ImgUtils.save(rai, "/path/to/out.tif", new UnsignedByteType());
   ImgUtils.save(rai, "/path/to/out.tif", new FloatType());
```


   **Signature:** ``save(RandomAccessibleInterval, String) -> void``

   **Parameters:**

   * **img** (``Any``): - the image to save; may be virtual or transformed
   * **filePath** (``str``)

   **Returns:** ``None``

   **Example:**

   .. code-block:: java

      ImgUtils.save(rai, "/path/to/out.tif", new UnsignedShortType());
         ImgUtils.save(rai, "/path/to/out.tif", new UnsignedByteType());
         ImgUtils.save(rai, "/path/to/out.tif", new FloatType());

.. method:: spatialNgffUnit(img)

   Returns the first recognized spatial unit (as an OME-NGFF name) among the X, Y and Z axes of `img`, or null if none is recognized. Bio-Formats readers do not always set the unit on every axis (or spell it as expected), so all spatial axes are checked, not just the first

   **Signature:** ``spatialNgffUnit(ImgPlus) -> String``

   **Parameters:**

   * **img** (``Any``): - the image

   **Returns:** (``str``) the OME-NGFF unit name (e.g., "micrometer"), or null if uncalibrated/unrecognized

.. method:: splitIntoBlocks(source, blockDimensions)

   Partition the source rai into a list of `IntervalView` with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have truncated dimensions.

   **Signature:** ``splitIntoBlocks(RandomAccessibleInterval, long[]) -> List``

   **Parameters:**

   * **source** (``Any``): - the source rai
   * **blockDimensions** (``List[int]``)

   **Returns:** (``List[Any]``) the list of blocks

.. method:: subInterval(img, p1, p2, padPixels)

   Get an N-D sub-interval of an N-D image, given two corner points and specified padding.

Works in native dimension order (no XYZ remapping). The sub-interval is clamped to image bounds.

   **Signature:** ``subInterval(RandomAccessibleInterval, Localizable, Localizable, long) -> RandomAccessibleInterval``

   **Parameters:**

   * **img** (``Any``): - the source interval
   * **p1** (``Any``)
   * **p2** (``Any``)
   * **padPixels** (``int``)

   **Returns:** (``Any``) the sub-interval

.. method:: subVolume(img, x1, y1, z1, x2, y2, z2, padPixels)

   Get a 3D sub-volume of an image, given two corner points and specified padding.

Coordinates are in XYZ order. If the input is 2D, a singleton dimension is added. The sub-volume is clamped to image bounds.

   **Signature:** ``subVolume(RandomAccessibleInterval, long, long, long, long, long, long, long) -> RandomAccessibleInterval``

   **Parameters:**

   * **img** (``Any``): - the source interval
   * **x1** (``int``)
   * **y1** (``int``)
   * **z1** (``int``)
   * **x2** (``int``)
   * **y2** (``int``)
   * **z2** (``int``)
   * **padPixels** (``int``)

   **Returns:** (``Any``) the sub-volume

.. method:: swapAxes(img, axis1, axis2)

   Returns a new `ImgPlus` with two axes swapped. The underlying data is a lazy permuted view (no pixel data is copied). Axis metadata (type, scale, unit) is reordered to match the new dimension order. Example: swap Z and Channel in an XYZCT image: 
```
ImgPlus<?> xyzct = ImgUtils.open("image.tif");
   ImgPlus<?> xyczT = ImgUtils.swapAxes(xyzct, Axes.Z, Axes.CHANNEL);
```


   **Signature:** ``swapAxes(ImgPlus, AxisType, AxisType) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``): - the source image
   * **axis1** (``Any``)
   * **axis2** (``Any``)

   **Returns:** (``Any``) a new ImgPlus with the two axes permuted

   **Example:**

   .. code-block:: java

      ImgPlus<?> xyzct = ImgUtils.open("image.tif");
         ImgPlus<?> xyczT = ImgUtils.swapAxes(xyzct, Axes.Z, Axes.CHANNEL);

.. method:: toImagePlus(img)

   Convert an ImgPlus to an ImagePlus, cropping to a bounding box. Convenience overload without padding.

   **Signature:** ``toImagePlus(ImgPlus) -> ImagePlus``

   **Parameters:**

   * **img** (``Any``)

   **Returns:** ``Any``

.. method:: toUnsignedShortIfFloat(rai)

   Returns a 16-bit view of the given RAI if its pixel type is `FloatType`, normalizing to the given min/max range.

   **Signature:** ``toUnsignedShortIfFloat(RandomAccessibleInterval) -> RandomAccessibleInterval``

   **Parameters:**

   * **rai** (``Any``): - the source image

   **Returns:** (``Any``) a 16-bit RAI, or the original RAI if not float

.. method:: wrapWithAxes(rai, source, name)

   Wrap a RandomAccessibleInterval with axis metadata from a source ImgPlus.

Useful for wrapping op results with proper calibration.

   **Signature:** ``wrapWithAxes(RandomAccessibleInterval, ImgPlus, String) -> ImgPlus``

   **Parameters:**

   * **rai** (``Any``): - the RAI to wrap
   * **source** (``Any``)
   * **name** (``str``)

   **Returns:** (``Any``) ImgPlus with copied axis metadata

.. method:: wrapWithSpacing(rai, spacing)

   Wraps a RandomAccessibleInterval as an ImgPlus with calibrated axes (no unit).

   **Signature:** ``wrapWithSpacing(RandomAccessibleInterval, double[]) -> ImgPlus``

   **Parameters:**

   * **rai** (``Any``): - the source image
   * **spacing** (``List[float]``)

   **Returns:** (``Any``) an ImgPlus with calibrated spatial axes


ImpUtils
--------

.. method:: ascii(imp, dilate, width, height)

   Converts the specified image into ascii art.

   **Signature:** ``ascii(ImagePlus, boolean, int, int) -> String``

   **Parameters:**

   * **imp** (``Any``): - The image to be converted to ascii art
   * **dilate** (``bool``)
   * **width** (``int``)
   * **height** (``int``)

   **Returns:** (``str``) ascii art

.. method:: binarize(imp, lower, upper)

   Binarize an ImagePlus using lower and upper thresholds. Pixels within [lower, upper] become 255 (white), others become 0 (black).

   **Signature:** ``binarize(ImagePlus, double, double) -> void``

   **Parameters:**

   * **imp** (``Any``): - the image to be binarized
   * **lower** (``float``)
   * **upper** (``float``)

   **Returns:** ``None``

.. method:: calibrationToAxes(cal, numDimensions)

   Creates ImgPlus axes from IJ1 Calibration

   **Signature:** ``calibrationToAxes(Calibration, int) -> CalibratedAxis[]``

   **Parameters:**

   * **cal** (``Any``)
   * **numDimensions** (``int``)

   **Returns:** ``List[Any]``

.. method:: combineSkeletons(trees)

   **Signature:** ``combineSkeletons(Collection) -> ImagePlus``

   **Parameters:**

   * **trees** (``List[Any]``)

   **Returns:** ``Any``

.. method:: convertRGBtoComposite(imp)

   **Signature:** ``convertRGBtoComposite(ImagePlus) -> ImagePlus``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``Any``

.. method:: convertTo16bit(imp)

   **Signature:** ``convertTo16bit(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: convertTo32bit(imp)

   **Signature:** ``convertTo32bit(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: convertTo8bit(imp)

   **Signature:** ``convertTo8bit(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: convertToSimple2D(imp, frame)

   Converts the specified image into an easy displayable form, i.e., a non-composite 2D image If the image is a timelapse, only the first frame is considered; if 3D, a MIP is retrieved; if multichannel, an RGB version is obtained. The image is flattened if its Overlay has ROIs.

   **Signature:** ``convertToSimple2D(ImagePlus, int) -> ImagePlus``

   **Parameters:**

   * **imp** (``Any``): - The image to be converted
   * **frame** (``int``)

   **Returns:** (``Any``) a 2D 'flattened' version of the image

.. method:: create(title, width, height, depth, bitDepth)

   **Signature:** ``create(String, int, int, int, int) -> ImagePlus``

   **Parameters:**

   * **title** (``str``)
   * **width** (``int``)
   * **height** (``int``)
   * **depth** (``int``)
   * **bitDepth** (``int``)

   **Returns:** ``Any``

.. method:: crop(imp, backgroundValue)

   Crops the image around non-background values. Does nothing if the image does not have non-background values.

   **Signature:** ``crop(ImagePlus, Number) -> void``

   **Parameters:**

   * **imp** (``Any``): - The image to be cropped
   * **backgroundValue** (``Union[int, float]``)

   **Returns:** ``None``

.. method:: demo(img)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.

   **Signature:** ``demo(String) -> ImagePlus``

   **Parameters:**

   * **img** (``str``): - a string describing the type of demo image. Options include: 'fractal' for the L-system toy neuron; 'ddaC' for the C4 ddaC drosophila neuron (demo image initially distributed with the Sholl plugin); 'OP1'/'OP_1' for the DIADEM OP_1 dataset; 'cil701', 'cil810', or 'ci41458' for the respective Cell Image Library entries, 'microglia' for a MIP of tiled microglia cells in the mouse retina, and 'binary timelapse' for a small 4-frame sequence of neurite growth

   **Returns:** (``Any``) the demo image, or null if data could not be retrieved

.. method:: forgetTags(imp)

   Removes `imp` from both the materialized-crop and display-canvas tag registries. Call once an image is known to be closed/discarded, for deterministic (rather than GC-timed) cleanup; harmless if `imp` was never tagged.

   **Signature:** ``forgetTags(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``): - the image to forget

   **Returns:** ``None``

.. method:: fromBufferedImage(title, image)

   **Signature:** ``fromBufferedImage(String, BufferedImage) -> ImagePlus``

   **Parameters:**

   * **title** (``str``)
   * **image** (``Any``)

   **Returns:** ``Any``

.. method:: imageTypeToString(type)

   **Signature:** ``imageTypeToString(int) -> String``

   **Parameters:**

   * **type** (``int``)

   **Returns:** ``str``

.. method:: invertLut(imp)

   **Signature:** ``invertLut(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: mergeChannels(imps)

   Script-friendly method for merging separate channels into a multichannel composite image.

   **Signature:** ``mergeChannels(Object[]) -> ImagePlus``

   **Parameters:**

   * **imps** (``List[Any]``): - The channels to be merged (Array, Collection, Iterable, or comma-separated images).

   **Returns:** (``Any``) the composite image, or if `imps` is a single image, that same image.

.. method:: nextZoomLevel(level)

   **Signature:** ``nextZoomLevel(double) -> double``

   **Parameters:**

   * **level** (``float``)

   **Returns:** ``float``

.. method:: open(file)

   **Signature:** ``open(File) -> ImagePlus``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``Any``

.. method:: previousZoomLevel(level)

   **Signature:** ``previousZoomLevel(double) -> double``

   **Parameters:**

   * **level** (``float``)

   **Returns:** ``float``

.. method:: rotate90(imp, direction)

   Rotates an image 90 degrees.

   **Signature:** ``rotate90(ImagePlus, String) -> void``

   **Parameters:**

   * **imp** (``Any``): - the image to be rotated
   * **direction** (``str``)

   **Returns:** ``None``

.. method:: sameCTDimensions(imp1, imp2)

   **Signature:** ``sameCTDimensions(ImagePlus, ImagePlus) -> boolean``

   **Parameters:**

   * **imp1** (``Any``)
   * **imp2** (``Any``)

   **Returns:** ``bool``

.. method:: sameCalibration(imp1, imp2)

   **Signature:** ``sameCalibration(ImagePlus, ImagePlus) -> boolean``

   **Parameters:**

   * **imp1** (``Any``)
   * **imp2** (``Any``)

   **Returns:** ``bool``

.. method:: sameXYZDimensions(imp1, imp2)

   **Signature:** ``sameXYZDimensions(ImagePlus, ImagePlus) -> boolean``

   **Parameters:**

   * **imp1** (``Any``)
   * **imp2** (``Any``)

   **Returns:** ``bool``

.. method:: save(imp, filePath)

   Saves the specified image.

   **Signature:** ``save(ImagePlus, String) -> void``

   **Parameters:**

   * **imp** (``Any``): - The image to be saved
   * **filePath** (``str``)

   **Returns:** ``None``

.. method:: toDataset(imp)

   **Signature:** ``toDataset(ImagePlus) -> Dataset``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``Any``

.. method:: toImgPlus(imp)

   Convert an ImagePlus to an ImgPlus with calibration and origin metadata.

Creates an ImgPlus with proper axis types (X, Y, Z, Channel, Time) and transfers calibration including pixel sizes, units, and origin offsets.

   **Signature:** ``toImgPlus(ImagePlus) -> ImgPlus``

   **Parameters:**

   * **imp** (``Any``): - the source ImagePlus

   **Returns:** (``Any``) ImgPlus with calibrated axes

.. method:: toImgPlus3D(imp, channel, frame)

   Convert an ImagePlus to a 3D (XYZ) ImgPlus, extracting a single channel/frame if needed.

Useful for analysis that expects simple 3D images without channel/time dimensions.

   **Signature:** ``toImgPlus3D(ImagePlus, int, int) -> ImgPlus``

   **Parameters:**

   * **imp** (``Any``): - the source ImagePlus
   * **channel** (``int``)
   * **frame** (``int``)

   **Returns:** (``Any``) 3D ImgPlus with X, Y, Z axes

.. method:: toStack(imps)

   **Signature:** ``toStack(Collection) -> ImagePlus``

   **Parameters:**

   * **imps** (``List[Any]``)

   **Returns:** ``Any``

.. method:: zoomTo(imp, paths)

   Zooms the image canvas to the specified magnification level, centered on the bounding box of the given paths.

   **Signature:** ``zoomTo(ImagePlus, Collection) -> double``

   **Parameters:**

   * **imp** (``Any``)
   * **paths** (``List[Any]``)

   **Returns:** ``float``


InsectBrainCompartment
----------------------

.. method:: acronym()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``acronym() -> String``

   **Returns:** ``str``

.. method:: aliases()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``aliases() -> String[]``

   **Returns:** ``List[str]``

.. method:: equals(o)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **o** (``Any``)

   **Returns:** ``bool``

.. method:: id()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``id() -> int``

   **Returns:** ``int``

.. method:: name()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``name() -> String``

   **Returns:** ``str``


InsectBrainLoader
-----------------

.. method:: idExists()

   Checks whether the neuron to be loaded was found in the database.

   **Signature:** ``idExists() -> boolean``

   **Returns:** (``bool``) true, if the neuron id specified in the constructor was found in the database


LabelProximityDetector
----------------------

.. method:: detect(paths, labelImg, config)

   **Signature:** ``detect(Collection, RandomAccessibleInterval, Config) -> List``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **labelImg** (``Any``)
   * **config** (``Any``)

   **Returns:** ``List[Any]``


LabelsToSeeds
-------------

.. method:: connectedComponents(mask, fullyConnected)

   **Signature:** ``connectedComponents(ImagePlus, boolean) -> ImagePlus``

   **Parameters:**

   * **mask** (``Any``)
   * **fullyConnected** (``bool``)

   **Returns:** ``Any``


LinearProfileStats
------------------

.. method:: findBestFit(fromDegree, toDegree, prefService)

   **Signature:** ``findBestFit(int, int, PrefService) -> int``

   **Parameters:**

   * **fromDegree** (``int``)
   * **toDegree** (``int``)
   * **prefService** (``Any``)

   **Returns:** ``int``

.. method:: fitPolynomial(degree)

   **Signature:** ``fitPolynomial(int) -> void``

   **Parameters:**

   * **degree** (``int``)

   **Returns:** ``None``

.. method:: plot()

   **Signature:** ``plot() -> ShollPlot``

   **Returns:** ``ShollPlot``

.. method:: validFit()

   **Signature:** ``validFit() -> boolean``

   **Returns:** ``bool``


ListSearchImage
---------------

.. method:: iterator()

   **Signature:** ``iterator() -> Iterator``

   **Returns:** ``Any``


MapSearchImage
--------------

.. method:: iterator()

   **Signature:** ``iterator() -> Iterator``

   **Returns:** ``Any``


MouseLightLoader
----------------

.. method:: demoTrees()

   Returns a collection of four demo reconstructions NB: Data is cached locally. No internet connection required.

   **Signature:** ``demoTrees() -> List``

   **Returns:** (``List[Any]``) the list of `Tree`s, corresponding to the dendritic arbors of cells "AA0001", "AA0002", "AA0003", "AA0004"

.. method:: extractNodes(jsonFile, compartment)

   **Signature:** ``extractNodes(File, String) -> Map``

   **Parameters:**

   * **jsonFile** (``str``)
   * **compartment** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: extractTrees(jsonFile, compartment)

   **Signature:** ``extractTrees(File, String) -> Map``

   **Parameters:**

   * **jsonFile** (``str``)
   * **compartment** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: idExists()

   Checks if the neuron ID exists in the database.

   **Signature:** ``idExists() -> boolean``

   **Returns:** (``bool``) true if the ID exists, false otherwise

.. method:: save(file)

   Convenience method to save JSON data.

   **Signature:** ``save(File) -> boolean``

   **Parameters:**

   * **file** (``str``): - the output directory or the output file

   **Returns:** (``bool``) true, if successful


MultiSpectralRefiner
--------------------

.. method:: apply()

   Applies the refinement result to the original path by replacing all its nodes with the refined geometry. This preserves hierarchical relationships (parent, children, connections) via `Path.replaceNodes(Path)`. Must be called sequentially (not thread-safe).

   **Signature:** ``apply() -> void``

   **Returns:** ``None``

.. method:: applySettings(ref)

   Applies all settings from another refiner to this one. Useful for batch operations where a reference refiner holds the user-configured parameters.

   **Signature:** ``applySettings(MultiSpectralRefiner) -> void``

   **Parameters:**

   * **ref** (``MultiSpectralRefiner``): - the reference refiner to copy settings from

   **Returns:** ``None``

.. method:: call()

   Runs the multispectral refinement on this path. Thread-safe: does not modify the original path. Call `apply()` afterward (sequentially) to commit results.

   **Signature:** ``call() -> Path``

   **Returns:** (``Path``) the refined path, or null if refinement failed

.. method:: refineTree(imp, tree)

   Refines all paths in a tree with custom parameters, where the tree's node coordinates and imp's own pixel grid are related by a fixed offset. See `MultiSpectralRefiner(ImagePlus, Path, double, double, double)`.

   **Signature:** ``refineTree(ImagePlus, Tree) -> int``

   **Parameters:**

   * **imp** (``Any``): - the multichannel image
   * **tree** (``Tree``)

   **Returns:** (``int``) the number of paths successfully refined

.. method:: succeeded()

   Whether the refinement succeeded (penalty decreased or path was already optimal).

   **Signature:** ``succeeded() -> boolean``

   **Returns:** ``bool``


MultiTreeColorMapper
--------------------

.. method:: map(measurement, colorTable)

   Description copied from class: `ColorMapper`

   **Signature:** ``map(String, ColorTable) -> void``

   **Parameters:**

   * **measurement** (``str``): - the measurement to be mapped
   * **colorTable** (``Any``)

   **Returns:** ``None``

.. method:: mapRootDistanceToCentroid(compartment, colorTable)

   **Signature:** ``mapRootDistanceToCentroid(AllenCompartment, ColorTable) -> void``

   **Parameters:**

   * **compartment** (``AllenCompartment``)
   * **colorTable** (``Any``)

   **Returns:** ``None``

.. method:: mapTrees(trees, lut)

   **Signature:** ``mapTrees(List, String) -> void``

   **Parameters:**

   * **trees** (``List[Any]``)
   * **lut** (``str``)

   **Returns:** ``None``

.. method:: sortedMappedTrees()

   **Signature:** ``sortedMappedTrees() -> List``

   **Returns:** ``List[Any]``

.. method:: unMap(paths)

   **Signature:** ``unMap(Collection) -> void``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``None``


MultiTreeStatistics
-------------------

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: fromCollection(trees, metric)

   **Signature:** ``fromCollection(Collection, String) -> TreeStatistics``

   **Parameters:**

   * **trees** (``List[Any]``)
   * **metric** (``str``)

   **Returns:** ``TreeStatistics``

.. method:: resetRestrictions()

   Description copied from class: `TreeStatistics`

   **Signature:** ``resetRestrictions() -> void``

   **Returns:** ``None``

.. method:: restrictToSWCType(types)

   Description copied from class: `TreeStatistics`

   **Signature:** ``restrictToSWCType(int[]) -> void``

   **Parameters:**

   * **types** (``List[int]``): - the allowed SWC flags (e.g., Path.SWC_AXON, etc.)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: summarize(groupByType)

   **Signature:** ``summarize(boolean) -> void``

   **Parameters:**

   * **groupByType** (``bool``)

   **Returns:** ``None``

.. method:: updateAndDisplayTable()

   **Signature:** ``updateAndDisplayTable() -> void``

   **Returns:** ``None``


MultiViewer2D
-------------

.. method:: save(filePath)

   **Signature:** ``save(String) -> void``

   **Parameters:**

   * **filePath** (``str``)

   **Returns:** ``None``

.. method:: show()

   **Signature:** ``show() -> JFrame``

   **Returns:** ``Any``


MultiViewer3D
-------------

.. method:: show()

   **Signature:** ``show() -> JFrame``

   **Returns:** ``Any``


NeuroMorphoLoader
-----------------

.. method:: get(cellId)

   Convenience method for retrieving SWC data,

   **Signature:** ``get(String) -> Tree``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved (case-sensitive). It may be the neuron name or its qualified filename. E.g., "cnic_002" or "cnic_002.swc" or "cnic_002.CNG.swc". By default, the standardized (CNG) version is assumed. Examples:

"cnic_002" -> CNG version of neuron cnic_002 is retrieved "cnic_002.CNG.swc" -> CNG version of neuron cnic_002 is retrieved "cnic_002.swc" -> Source version of neuron cnic_002 is retrieved

   **Returns:** (``Tree``) the specified neuron as a `Tree` object, or null if data could not be retrieved


NodeColorMapper
---------------

.. method:: map(measurement, colorTable)

   Maps nodes after the specified measurement. Mapping bounds are automatically determined.

   **Signature:** ``map(String, ColorTable) -> void``

   **Parameters:**

   * **measurement** (``str``): - the measurement (X_COORDINATES, Y_COORDINATES, etc.)
   * **colorTable** (``Any``)

   **Returns:** ``None``

.. method:: unMap(paths)

   **Signature:** ``unMap(Collection) -> void``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``None``


NodeProfiler
------------

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


NodeStatistics
--------------

.. method:: assignBranches(tree)

   Associates the nodes being analyzed to the branches of the specified tree

   **Signature:** ``assignBranches(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the association tree

   **Returns:** ``None``

.. method:: filter(metric, lowerBound, upperBound)

   Filters the current pool of nodes matching a measurement-based criterion.

   **Signature:** ``filter(String, double, double) -> List``

   **Parameters:**

   * **metric** (``str``): - the measurement (X_COORDINATES, Y_COORDINATES, BRANCH_ORDER, etc.)
   * **lowerBound** (``float``)
   * **upperBound** (``float``)

   **Returns:** (``List[Any]``) the filtered list.

.. method:: get(compartment)

   Gets the list of nodes associated with the specified compartment (neuropil label).

   **Signature:** ``get(BrainAnnotation) -> List``

   **Parameters:**

   * **compartment** (``Any``): - the query compartment (null not allowed)

   **Returns:** (``List[Any]``) the list of filtered nodes


NormalizedProfileStats
----------------------

.. method:: is2Dnormalization()

   **Signature:** ``is2Dnormalization() -> boolean``

   **Returns:** ``bool``

.. method:: is3Dnormalization()

   **Signature:** ``is3Dnormalization() -> boolean``

   **Returns:** ``bool``

.. method:: resetRegression()

   **Signature:** ``resetRegression() -> void``

   **Returns:** ``None``

.. method:: restrictRegToPercentile(p1, p2)

   **Signature:** ``restrictRegToPercentile(double, double) -> void``

   **Parameters:**

   * **p1** (``float``)
   * **p2** (``float``)

   **Returns:** ``None``

.. method:: restrictRegToRange(x1, x2)

   **Signature:** ``restrictRegToRange(double, double) -> void``

   **Parameters:**

   * **x1** (``float``)
   * **x2** (``float``)

   **Returns:** ``None``

.. method:: validFit()

   **Signature:** ``validFit() -> boolean``

   **Returns:** ``bool``


OBJMesh
-------

.. method:: duplicate()

   **Signature:** ``duplicate() -> OBJMesh``

   **Returns:** ``OBJMesh``

.. method:: label()

   Gets this mesh label.

   **Signature:** ``label() -> String``

   **Returns:** ``str``

.. method:: toMesh()

   Returns a copy of this mesh as an imglib2-mesh `Mesh` (vertices and triangles only, in the coordinates of this mesh).

   **Signature:** ``toMesh() -> Mesh``

   **Returns:** (``Any``) the mesh (empty if this mesh has no triangles)

.. method:: translate(offset)

   Translates the vertices of this mesh by the specified offset. If mesh is displayed, changes may only occur once scene is rebuilt.

   **Signature:** ``translate(SNTPoint) -> void``

   **Parameters:**

   * **offset** (``SNTPoint``): - the translation offset

   **Returns:** ``None``


OneMinusErf
-----------

.. method:: costMovingTo(valueAtNewPoint)

   **Signature:** ``costMovingTo(double) -> double``

   **Parameters:**

   * **valueAtNewPoint** (``float``)

   **Returns:** ``float``

.. method:: minStepCost()

   **Signature:** ``minStepCost() -> double``

   **Returns:** ``float``


PCAnalyzer
----------

.. method:: orientTowardDirection(axes, referenceDirection)

   Orients principal axes so the primary axis points toward a reference direction, i.e., the primary axis is oriented to minimize the angle with the reference direction. If the primary axis points away from the reference (dot product < 0), it's flipped.\

   **Signature:** ``orientTowardDirection(PrincipalAxis[], double[]) -> PrincipalAxis[]``

   **Parameters:**

   * **axes** (``List[Any]``): - the principal axes to orient
   * **referenceDirection** (``List[float]``)

   **Returns:** (``List[Any]``) oriented principal axes

.. method:: orientTowardTips(axes, tree)

   Convenience method to orient existing principal axes toward a tree's tips centroid. For several topologies, this orients the primary axis is so it aligns with the general growth direction of the arbor.

   **Signature:** ``orientTowardTips(PrincipalAxis[], Tree) -> PrincipalAxis[]``

   **Parameters:**

   * **axes** (``List[Any]``): - the principal axes to orient
   * **tree** (``Tree``)

   **Returns:** (``List[Any]``) oriented principal axes


Path
----

.. method:: add(other)

   **Signature:** ``add(Path) -> void``

   **Parameters:**

   * **other** (``Path``)

   **Returns:** ``None``

.. method:: clone()

   Creates a copy of this Path with optional inclusion of immediate children.

This method creates a clone of this path and optionally includes clones of its immediate child paths. When children are included, they are properly reconnected to the cloned parent path, maintaining the parent-child relationships. Note that only immediate children are cloned - grandchildren and deeper descendants are not included.

**Limitations:** This method only clones the immediate children and does not recursively clone the entire subtree. For complex tree structures, consider using `Tree.clone()` instead.

   **Signature:** ``clone() -> Path``

   **Returns:** ``Path``

.. method:: compareTo(o)

   **Signature:** ``compareTo(Path) -> int``

   **Parameters:**

   * **o** (``Path``)

   **Returns:** ``int``

.. method:: contains(pim)

   Checks if this path contains the specified point within the given tolerance.

   **Signature:** ``contains(PointInImage) -> boolean``

   **Parameters:**

   * **pim** (``PointInImage``): - the point to check

   **Returns:** (``bool``) true if the path contains the point within tolerance

.. method:: detachFromParent()

   Detaches this path from its parent, converting it into an independent primary path.

Removes the parent-child relationship established by `setBranchFrom(Path, PointInImage)` In

- Clears the parent path reference and branch point

- Removes this path from the parent's children collection

- Updates bidirectional references for tree traversal

- Resets the path order to -1 (no hierarchical position)

- Converts this path from a branch to a primary path

   **Signature:** ``detachFromParent() -> void``

   **Returns:** ``None``

.. method:: downsample(internodeSpacing)

   Downsamples this path (in-place) by reducing the number of nodes while preserving its overall shape.

This method reduces the density of nodes in the path by removing redundant points expected to not significantly contribute to the path's shape. The downsampling is performed using the Douglas-Peucker algorithm, which preserves fidelity within the specified tolerance.

The method operates on the segments flanked by anchor points (junctions, start, and end points). Each segment is downsampled independently, and the results are combined to form the final downsampled path. Node radii are averaged appropriately for retained points

**Thread Safety:** This method is synchronized to prevent concurrent modification of the path structure during the downsampling operation.

   **Signature:** ``downsample(double) -> void``

   **Parameters:**

   * **internodeSpacing** (``float``): - the target spacing between nodes after downsampling. This parameter controls the aggressiveness of the downsampling - smaller values preserve more detail, larger values result in more aggressive simplification. Must be greater than zero.

   **Returns:** ``None``

.. method:: findJunctionIndices()

   Returns the indices of nodes which are indicated to be a join, either in this Path object, or any other that starts or ends on it.

   **Signature:** ``findJunctionIndices() -> TreeSet``

   **Returns:** (``Set[Any]``) the indices of junction nodes, naturally sorted

.. method:: findJunctions()

   Returns the nodes which are indicated to be a join (junction/branch point), either in this Path object, or any other that starts or ends on it.

   **Signature:** ``findJunctions() -> List``

   **Returns:** (``List[Any]``) the list of nodes as `PointInImage` objects

.. method:: firstNode()

   Returns the first node of this path.

   **Signature:** ``firstNode() -> PointInImage``

   **Returns:** (``PointInImage``) the root node, or null if path is empty

.. method:: fitRadii(imp)

   Fits radii to this Path by fitting circular cross-sections to the image signal. This is the scripting equivalent of the UI's "Fit Path" action. Node positions are not modified; only radii and tangent vectors are computed.

   **Signature:** ``fitRadii(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the image containing the signal to fit against

   **Returns:** (``bool``) true if the fit succeeded

.. method:: indexNearestTo(x, y, z, within)

   **Signature:** ``indexNearestTo(double, double, double, double) -> int``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)
   * **within** (``float``)

   **Returns:** ``int``

.. method:: indexNearestToUnscaled(x, y, z)

   Returns the index of the node nearest to the specified position in pixel (unscaled) coordinates, searching across all nodes regardless of distance.

   **Signature:** ``indexNearestToUnscaled(double, double, double) -> int``

   **Parameters:**

   * **x** (``float``): - the x-coordinate in pixel units
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** (``int``) the index of the closest node

.. method:: insertNode(index, point)

   Inserts a node at the specified position.

   **Signature:** ``insertNode(int, PointInImage) -> void``

   **Parameters:**

   * **index** (``int``): - the position at which the node is to be inserted
   * **point** (``PointInImage``)

   **Returns:** ``None``

.. method:: lastNode()

   Returns the last node of this path.

   **Signature:** ``lastNode() -> PointInImage``

   **Returns:** (``PointInImage``) the terminal node, or null if path is empty

.. method:: moveNode(index, destination)

   Assigns a new location to the specified node using raw coordinates. This is a performance-optimized version of `moveNode(int, PointInImage)` that avoids object allocation.

   **Signature:** ``moveNode(int, PointInImage) -> void``

   **Parameters:**

   * **index** (``int``): - the index of the node to move
   * **destination** (``PointInImage``)

   **Returns:** ``None``

.. method:: nearestNodeTo(node, within)

   Gets the closest node associated with the specified node.

   **Signature:** ``nearestNodeTo(PointInImage, double) -> PathNode``

   **Parameters:**

   * **node** (``PointInImage``): - location to be searched for
   * **within** (``float``)

   **Returns:** (``Any``) the closest node to the specified one or null if no such node was found.

.. method:: replaceNodes(replacementPath)

   Replaces all nodes of this path with those from the replacement path, preserving hierarchical relationships (parent, children, connections).

This method is useful for refining path geometry (e.g., from A* tracing) while maintaining the tree structure.

   **Signature:** ``replaceNodes(Path) -> void``

   **Parameters:**

   * **replacementPath** (``Path``): - the path providing the new node geometry

   **Returns:** ``None``

.. method:: reverse()

   Reverses this path so that its starting node becomes the last and vice versa.

   **Signature:** ``reverse() -> void``

   **Returns:** ``None``

.. method:: reversed()

   **Signature:** ``reversed() -> Path``

   **Returns:** (``Path``) a reversed version of this path in which node coordinates are reversed. Note that for legacy reasons only the node coordinates are reversed. Other properties (node colors, etc.) are not included in the returned path

.. method:: sanitizeRadii(apply)

   Sanitizes node radii by enforcing bounds and interpolating outliers.

Identifies nodes with radii outside `[minRadius, maxRadius]` and assigns new values using linear interpolation based on remaining valid nodes. Interpolated values are clamped to the specified range to prevent extrapolation artifacts.

If fewer than two nodes have valid radii, a context-appropriate fallback is used:

- All radii above range → `maxRadius`

- All radii below range → `minRadius`

- Mixed or NaN values → midpoint of range

   **Signature:** ``sanitizeRadii(boolean) -> Map``

   **Parameters:**

   * **apply** (``bool``): - minimum valid radius (inclusive)

   **Returns:** (``Dict[str, Any]``) map of corrected `(node index, radius)` pairs, or `null` if path has no radii or fewer than 2 nodes. Empty map if all radii are already within range.

.. method:: toString()

   This toString() method shows details of the path which is actually being displayed, not necessarily this path object.

   **Signature:** ``toString() -> String``

   **Returns:** (``str``) the string

.. method:: transform(transformation, template, model)

   **Signature:** ``transform(PathTransformer, ImagePlus, ImagePlus) -> Path``

   **Parameters:**

   * **transformation** (``Any``)
   * **template** (``Any``)
   * **model** (``Any``)

   **Returns:** ``Path``

.. method:: upsample(internodeSpacing)

   Upsamples this path by spacing nodes at a specified distance.

The original nodes are preserved and additional interpolated nodes are placed at regular intervals between them. The spacing between adjacent nodes will thus be approximately equal to the specified distance. If the distance between two adjacent original nodes is less than the specified pacing, no additional nodes are added between them.

**NB:**Some assigned properties (node colors, node values, etc.) will be lost.

**Thread Safety:** This method is synchronized to prevent concurrent modification of the path structure during the upsampling operation.

   **Signature:** ``upsample(double) -> void``

   **Parameters:**

   * **internodeSpacing** (``float``): - the desired distance between adjacent nodes

   **Returns:** ``None``


PathAndFillManager
------------------

.. method:: allPointsIterator()

   **Signature:** ``allPointsIterator() -> Iterator``

   **Returns:** ``Any``

.. method:: anySelected()

   Checks whether at least one Path is currently selected in the UI.

   **Signature:** ``anySelected() -> boolean``

   **Returns:** (``bool``) true, if successful

.. method:: assignSpatialSettings(imp)

   **Signature:** ``assignSpatialSettings(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: clear()

   Deletes all paths and fills.

   **Signature:** ``clear() -> void``

   **Returns:** ``None``

.. method:: createFromGraph(graph, keepTreePathStructure)

   Create a new PathAndFillManager instance from the graph.

   **Signature:** ``createFromGraph(DirectedWeightedGraph, boolean) -> PathAndFillManager``

   **Parameters:**

   * **graph** (``DirectedWeightedGraph``): - The input graph
   * **keepTreePathStructure** (``bool``)

   **Returns:** ``PathAndFillManager``

.. method:: createFromNodes(nodes)

   Creates a PathAndFillManager instance from a collection of reconstruction nodes.

   **Signature:** ``createFromNodes(Collection) -> PathAndFillManager``

   **Parameters:**

   * **nodes** (``List[Any]``): - the collection of reconstruction nodes. Nodes will be sorted by id and any duplicate entries pruned.

   **Returns:** (``PathAndFillManager``) the PathAndFillManager instance, or null if file could not be imported

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: downsampleAll(maximumPermittedDistance)

   Downsamples alls path using Ramer-Douglas-Peucker simplification. Downsampling occurs only between branch points and terminal points.

   **Signature:** ``downsampleAll(double) -> void``

   **Parameters:**

   * **maximumPermittedDistance** (``float``): - the maximum permitted distance between nodes.

   **Returns:** ``None``

.. method:: endElement(uri, localName, qName)

   **Signature:** ``endElement(String, String, String) -> void``

   **Parameters:**

   * **uri** (``str``)
   * **localName** (``str``)
   * **qName** (``str``)

   **Returns:** ``None``

.. method:: load(filePath, swcTypes)

   Imports a reconstruction file (any supported extension).

   **Signature:** ``load(String, int[]) -> boolean``

   **Parameters:**

   * **filePath** (``str``): - the absolute path to the file (.Traces, SWC or JSON) to be imported
   * **swcTypes** (``List[int]``)

   **Returns:** (``bool``) true, if successful

.. method:: nearestNodeInUse(paths, x, y, z)

   As `nearestNodeOnPaths(Collection, double, double, double)`, but searching the version in use of each path (see `getVersionInUse(Path)`). The returned `PathAndFillManager.NodeRef.path()` is that version.

   **Signature:** ``nearestNodeInUse(Collection, double, double, double) -> NodeRef``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to be searched
   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** (``Any``) the nearest node, or null if the paths hold no nodes

.. method:: resetListeners(justAdded)

   **Signature:** ``resetListeners(Path) -> void``

   **Parameters:**

   * **justAdded** (``Path``)

   **Returns:** ``None``

.. method:: startElement(uri, localName, qName, attributes)

   **Signature:** ``startElement(String, String, String, Attributes) -> void``

   **Parameters:**

   * **uri** (``str``)
   * **localName** (``str``)
   * **qName** (``str``)
   * **attributes** (``Any``)

   **Returns:** ``None``

.. method:: transformationFinished(view)

   **Signature:** ``transformationFinished(View) -> void``

   **Parameters:**

   * **view** (``Any``)

   **Returns:** ``None``

.. method:: transformationStarted(view)

   **Signature:** ``transformationStarted(View) -> void``

   **Parameters:**

   * **view** (``Any``)

   **Returns:** ``None``

.. method:: transformationUpdated(view)

   **Signature:** ``transformationUpdated(View) -> void``

   **Parameters:**

   * **view** (``Any``)

   **Returns:** ``None``

.. method:: validateImageDimensions()

   Publicly triggers the same "does the loaded image accommodate these nodes" check that `load(java.io.InputStream)` and `addTrees(java.util.Collection<sc.fiji.snt.Tree>, java.lang.String)` perform automatically. Useful for callers (e.g. stream-mode importers) that add `Tree`s one at a time via `addTree(Tree, String)`, which intentionally skips this check since it assumes a currently-traced image is large enough to contain the tree

   **Signature:** ``validateImageDimensions() -> void``

   **Returns:** ``None``


PathFitter
----------

.. method:: applyFit()

   Applies the fitted result to the path. For multithreaded processing: Must be called sequentially after all parallel fitting is complete.

   **Signature:** ``applyFit() -> void``

   **Returns:** ``None``

.. method:: applySettings(pf)

   **Signature:** ``applySettings(PathFitter) -> void``

   **Parameters:**

   * **pf** (``PathFitter``)

   **Returns:** ``None``

.. method:: call()

   Takes the signal from the image specified in the constructor to fit cross-section circles around the nodes of input path. Computation of fit is confined to the neighborhood specified by `setCrossSectionRadius(double)`.

   **Signature:** ``call() -> Path``

   **Returns:** (``Path``) the reference to the computed result. Note that this Path is *not* automatically set as the fitted version of input Path. That only happens when `applyFit()` is called.


PathManagerUI
-------------

.. method:: applyDefaultTags(defaultTags)

   Applies a default (built-in) tag to selected Path(s).

   **Signature:** ``applyDefaultTags(String[]) -> void``

   **Parameters:**

   * **defaultTags** (``List[str]``): - The tags to be applied to selected Paths, as listed in the "Tag" menu, e.g., "Traced Channel", "Traced Frame", "No. of Spine/Varicosity Markers", etc.

   **Returns:** ``None``

.. method:: applySelectionFilter(query)

   Selects paths matching a morphometric criteria.

   **Signature:** ``applySelectionFilter(String) -> void``

   **Parameters:**

   * **query** (``str``): - The morphometric property ("Length", "Path order", etc.) as listed in the "Morphology filter" menu (case-sensitive).

   **Returns:** ``None``

.. method:: applyTag(customTagOrColor)

   Applies a custom tag/ color to selected Path(s).

   **Signature:** ``applyTag(String) -> void``

   **Parameters:**

   * **customTagOrColor** (``str``): - The tag (or color) to be applied to selected Paths. Specifying "null color" will remove color tags from selected paths.

   **Returns:** ``None``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: reload()

   Reloads the contents of `PathAndFillManager`

   **Signature:** ``reload() -> void``

   **Returns:** ``None``

.. method:: runCommand(cmd)

   Runs a menu command with options.

   **Signature:** ``runCommand(String) -> void``

   **Parameters:**

   * **cmd** (``str``): - The command to be run, exactly as listed in the PathManagerUI's menu bar or Right-click contextual menu

   **Returns:** ``None``

.. method:: select(path)

   Selects a specific path in the Path Manager.

   **Signature:** ``select(Path) -> void``

   **Parameters:**

   * **path** (``Path``): - the path to be selected. If the path is not found in the manager, the selection remains unchanged. If null active selection (if any) is cleared.

   **Returns:** ``None``

.. method:: selectAll()

   Selects all paths.

   **Signature:** ``selectAll() -> void``

   **Returns:** ``None``

.. method:: update()

   Refreshes (Repaints) the Path Manager JTree.

   **Signature:** ``update() -> void``

   **Returns:** ``None``

.. method:: valueChanged(e)

   **Signature:** ``valueChanged(TreeSelectionEvent) -> void``

   **Parameters:**

   * **e** (``Any``)

   **Returns:** ``None``


PathProfiler
------------

.. method:: assignValues()

   Retrieves pixel intensities at each node of the Path storing them as Path `values`

   **Signature:** ``assignValues() -> void``

   **Returns:** ``None``

.. method:: findMaxima(path, channel)

   Finds the maxima in the profile of the specified path.

A maxima (peak) will only be considered if protruding more than the profile's standard deviation from the ridge to a higher maximum

   **Signature:** ``findMaxima(Path, int) -> int[]``

   **Parameters:**

   * **path** (``Path``): - the channel to be parsed (base-0 index)
   * **channel** (``int``)

   **Returns:** (``List[int]``) the indices of the maxima

.. method:: findMinima(path, channel)

   Finds the minima in the profile of the specified path.

A maxima (peak) will only be considered if protruding less than the profile's standard deviation from the ridge to a lower minimum

   **Signature:** ``findMinima(Path, int) -> int[]``

   **Parameters:**

   * **path** (``Path``): - the channel to be parsed (base-0 index)
   * **channel** (``int``)

   **Returns:** (``List[int]``) the indices of the minima

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


PathStatistics
--------------

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: fromCollection(trees, metric)

   **Signature:** ``fromCollection(Collection, String) -> TreeStatistics``

   **Parameters:**

   * **trees** (``List[Any]``)
   * **metric** (``str``)

   **Returns:** ``TreeStatistics``

.. method:: resetRestrictions()

   **Signature:** ``resetRestrictions() -> void``

   **Returns:** ``None``

.. method:: restrictToSWCType(types)

   **Signature:** ``restrictToSWCType(int[]) -> void``

   **Parameters:**

   * **types** (``List[int]``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: summarize(groupByType)

   **Signature:** ``summarize(boolean) -> void``

   **Parameters:**

   * **groupByType** (``bool``)

   **Returns:** ``None``

.. method:: updateAndDisplayTable()

   **Signature:** ``updateAndDisplayTable() -> void``

   **Returns:** ``None``


PathStraightener
----------------

.. method:: straighten()

   **Signature:** ``straighten() -> ImagePlus``

   **Returns:** ``Any``


PlausibilityCalibrator
----------------------

.. method:: calibrate()

   **Signature:** ``calibrate() -> CalibrationResult``

   **Returns:** ``Any``

.. method:: load(file, monitor)

   **Signature:** ``load(File, PlausibilityMonitor) -> void``

   **Parameters:**

   * **file** (``str``)
   * **monitor** (``PlausibilityMonitor``)

   **Returns:** ``None``

.. method:: save(monitor, file, comment)

   **Signature:** ``save(PlausibilityMonitor, File, String) -> void``

   **Parameters:**

   * **monitor** (``PlausibilityMonitor``)
   * **file** (``str``)
   * **comment** (``str``)

   **Returns:** ``None``


PlausibilityMonitor
-------------------

.. method:: impactKindFor(checkName)

   **Signature:** ``impactKindFor(String) -> ImpactKind``

   **Parameters:**

   * **checkName** (``str``)

   **Returns:** ``Any``

.. method:: onForkInitiated(parent, branchIndex)

   **Signature:** ``onForkInitiated(Path, int) -> void``

   **Parameters:**

   * **parent** (``Path``)
   * **branchIndex** (``int``)

   **Returns:** ``None``

.. method:: onNodeEdited(editedPath, nodeIndex)

   **Signature:** ``onNodeEdited(Path, int) -> List``

   **Parameters:**

   * **editedPath** (``Path``)
   * **nodeIndex** (``int``)

   **Returns:** ``List[Any]``

.. method:: onSegmentCompleted(candidateChild)

   **Signature:** ``onSegmentCompleted(Path) -> List``

   **Parameters:**

   * **candidateChild** (``Path``)

   **Returns:** ``List[Any]``

.. method:: runDeepScan(paths)

   **Signature:** ``runDeepScan(Collection) -> List``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``List[Any]``

.. method:: runFullScan(paths)

   **Signature:** ``runFullScan(Collection) -> List``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``List[Any]``


PointInImage
------------

.. method:: chebyshevDxTo(point)

   **Signature:** ``chebyshevDxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevXYdxTo(point)

   **Signature:** ``chebyshevXYdxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevZdxTo(point)

   **Signature:** ``chebyshevZdxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: clone()

   Creates a copy of this PointInImage.

This method creates a copy of the point including all properties such as coordinates, value, annotation, and hemisphere information.

   **Signature:** ``clone() -> PointInImage``

   **Returns:** (``PointInImage``) a new PointInImage that is a copy of this point

.. method:: distanceSquaredTo(o)

   **Signature:** ``distanceSquaredTo(PointInImage) -> double``

   **Parameters:**

   * **o** (``PointInImage``)

   **Returns:** ``float``

.. method:: distanceTo(o)

   **Signature:** ``distanceTo(PointInImage) -> double``

   **Parameters:**

   * **o** (``PointInImage``)

   **Returns:** ``float``

.. method:: equals(o)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **o** (``Any``)

   **Returns:** ``bool``

.. method:: euclideanDxTo(point)

   **Signature:** ``euclideanDxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: scale(xScale, yScale, zScale)

   Scales this point coordinates.

   **Signature:** ``scale(double, double, double) -> void``

   **Parameters:**

   * **xScale** (``float``): - the scaling factor for x coordinates
   * **yScale** (``float``)
   * **zScale** (``float``)

   **Returns:** ``None``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``

.. method:: transform(transformer)

   **Signature:** ``transform(PathTransformer) -> PointInImage``

   **Parameters:**

   * **transformer** (``Any``)

   **Returns:** ``PointInImage``


PolarProfileStats
-----------------

.. method:: appendSummaryReport(table)

   **Signature:** ``appendSummaryReport(SNTTable) -> void``

   **Parameters:**

   * **table** (``SNTTable``)

   **Returns:** ``None``

.. method:: detailReport(table)

   **Signature:** ``detailReport(SNTTable) -> void``

   **Parameters:**

   * **table** (``SNTTable``)

   **Returns:** ``None``

.. method:: findDirectionPeaks(rMin, rMax)

   **Signature:** ``findDirectionPeaks(double, double) -> List``

   **Parameters:**

   * **rMin** (``float``)
   * **rMax** (``float``)

   **Returns:** ``List[Any]``

.. method:: findOrientationPeaks(rMin, rMax)

   **Signature:** ``findOrientationPeaks(double, double) -> List``

   **Parameters:**

   * **rMin** (``float``)
   * **rMax** (``float``)

   **Returns:** ``List[Any]``

.. method:: validFit()

   **Signature:** ``validFit() -> boolean``

   **Returns:** ``bool``


Profile
-------

.. method:: add(entry)

   **Signature:** ``add(ProfileEntry) -> boolean``

   **Parameters:**

   * **entry** (``ProfileEntry``)

   **Returns:** ``bool``

.. method:: assignImage(imp)

   **Signature:** ``assignImage(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: center()

   **Signature:** ``center() -> ShollPoint``

   **Returns:** ``Any``

.. method:: counts()

   **Signature:** ``counts() -> List``

   **Returns:** ``List[Any]``

.. method:: countsAsArray()

   **Signature:** ``countsAsArray() -> double[]``

   **Returns:** ``List[float]``

.. method:: duplicate()

   **Signature:** ``duplicate() -> Profile``

   **Returns:** ``Profile``

.. method:: endRadius()

   **Signature:** ``endRadius() -> double``

   **Returns:** ``float``

.. method:: entries()

   **Signature:** ``entries() -> SortedSet``

   **Returns:** ``Any``

.. method:: equals(o)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **o** (``Any``)

   **Returns:** ``bool``

.. method:: extras()

   **Signature:** ``extras() -> List``

   **Returns:** ``List[Any]``

.. method:: identifier()

   **Signature:** ``identifier() -> String``

   **Returns:** ``str``

.. method:: is2D()

   **Signature:** ``is2D() -> boolean``

   **Returns:** ``bool``

.. method:: lengths()

   **Signature:** ``lengths() -> List``

   **Returns:** ``List[Any]``

.. method:: lengthsAsArray()

   **Signature:** ``lengthsAsArray() -> double[]``

   **Returns:** ``List[float]``

.. method:: nDimensions()

   **Signature:** ``nDimensions() -> int``

   **Returns:** ``int``

.. method:: plot()

   **Signature:** ``plot() -> ShollPlot``

   **Returns:** ``ShollPlot``

.. method:: points()

   **Signature:** ``points() -> List``

   **Returns:** ``List[Any]``

.. method:: radii()

   **Signature:** ``radii() -> List``

   **Returns:** ``List[Any]``

.. method:: radiiAsArray()

   **Signature:** ``radiiAsArray() -> double[]``

   **Returns:** ``List[float]``

.. method:: radiiSquared()

   **Signature:** ``radiiSquared() -> List``

   **Returns:** ``List[Any]``

.. method:: scale(xScale, yScale, zScale)

   **Signature:** ``scale(double, double, double) -> void``

   **Parameters:**

   * **xScale** (``float``)
   * **yScale** (``float``)
   * **zScale** (``float``)

   **Returns:** ``None``

.. method:: scaled()

   **Signature:** ``scaled() -> boolean``

   **Returns:** ``bool``

.. method:: source()

   **Signature:** ``source() -> String``

   **Returns:** ``str``

.. method:: spatialCalibration()

   **Signature:** ``spatialCalibration() -> Calibration``

   **Returns:** ``Any``

.. method:: startRadius()

   **Signature:** ``startRadius() -> double``

   **Returns:** ``float``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``

.. method:: trimNaNCounts()

   **Signature:** ``trimNaNCounts() -> void``

   **Returns:** ``None``

.. method:: trimZeroCounts()

   **Signature:** ``trimZeroCounts() -> void``

   **Returns:** ``None``

.. method:: zeroCounts()

   **Signature:** ``zeroCounts() -> int``

   **Returns:** ``int``


ProfileEntry
------------

.. method:: assignPoints(points)

   **Signature:** ``assignPoints(Set) -> void``

   **Parameters:**

   * **points** (``Set[Any]``)

   **Returns:** ``None``

.. method:: compareTo(other)

   **Signature:** ``compareTo(ProfileEntry) -> int``

   **Parameters:**

   * **other** (``ProfileEntry``)

   **Returns:** ``int``

.. method:: radiusSquared()

   **Signature:** ``radiusSquared() -> double``

   **Returns:** ``float``


Reciprocal
----------

.. method:: costMovingTo(valueAtNewPoint)

   **Signature:** ``costMovingTo(double) -> double``

   **Parameters:**

   * **valueAtNewPoint** (``float``)

   **Returns:** ``float``

.. method:: minStepCost()

   **Signature:** ``minStepCost() -> double``

   **Returns:** ``float``


RemoteSWCLoader
---------------

.. method:: download(urlString, destinationFile)

   **Signature:** ``download(String, File) -> boolean``

   **Parameters:**

   * **urlString** (``str``)
   * **destinationFile** (``str``)

   **Returns:** ``bool``


RootAngleAnalyzer
-----------------

.. method:: balancingFactor()

   Returns the balancing factor, computed from `centripetalBias()`.

   **Signature:** ``balancingFactor() -> double``

   **Returns:** (``float``) the balancing factor (dimensionless, range: [0, 1]).

.. method:: centripetalBias()

   Returns the strength of the centripetal bias, also known as κ. κ is defined as the concentration of the von Mises fit of the root angle distribution. κ= 0 indicate no bias (root angles are distributed uniformly). K->∞ indicate that all neurites point directly toward the root of the tree

   **Signature:** ``centripetalBias() -> double``

   **Returns:** (``float``) Returns the centripetal bias, or κ (dimensionless, range: [0, ∞[).

.. method:: max()

   **Signature:** ``max() -> double``

   **Returns:** (``float``) Returns the largest of root angles (in degrees).

.. method:: mean()

   **Signature:** ``mean() -> double``

   **Returns:** (``float``) Returns the arithmetic mean of root angles (in degrees).

.. method:: meanDirection()

   Returns the mean direction of the fitted von Mises distribution.

   **Signature:** ``meanDirection() -> double``

   **Returns:** (``float``) the mean direction (in degrees).

.. method:: min()

   **Signature:** ``min() -> double``

   **Returns:** (``float``) Returns the smallest of root angles (in degrees).


RootDetector
------------

.. method:: detect(trees)

   **Signature:** ``detect(Collection) -> List``

   **Parameters:**

   * **trees** (``List[Any]``)

   **Returns:** ``List[Any]``


SNT
---

.. method:: accessToValidImageData()

   Checks whether valid image data exists.

   **Signature:** ``accessToValidImageData() -> boolean``

   **Returns:** (``bool``) true if a tracing image exists, or (for headless/API usage) cached pixel data remains in memory.

.. method:: autoTrace(pointList, forkPoint)

   Automatically traces a path from a point A to a point B. See `autoTrace(List, PointInImage)` for details.

   **Signature:** ``autoTrace(List, PointInImage) -> Path``

   **Parameters:**

   * **pointList** (``List[Any]``): - the list of PointInImage containing the nodes to be used as target goals during the search. If the search cannot converge into a target point, such point is omitted from path, if Successful, target point will be included in the final path. The final path. The first point in the list is the start of the path, the last its terminus. Null objects not allowed.
   * **forkPoint** (``PointInImage``)

   **Returns:** (``Path``) the path a reference to the computed path.

.. method:: autoTraceSync(pointList, forkPoint)

   Variant of `autoTraceSync(List, PointInImage)` that uses a frozen `SNT.SearchSettingsSnapshot` instead of the live cost function/data structure/secondary-image settings, so every segment of every path in a long-running batch (e.g. `AStarRefiner`) is traced with identical settings, immune to changes made mid-run via the (deliberately still enabled) A* controls.

   **Signature:** ``autoTraceSync(List, PointInImage) -> Path``

   **Parameters:**

   * **pointList** (``List[Any]``): - the waypoints to connect, start to end
   * **forkPoint** (``PointInImage``)

   **Returns:** (``Path``) the stitched path, or null if any segment failed to produce a result

.. method:: buildMaterializedCrop(worldBox)

   As `buildMaterializedCrop(BoundingBox)`, but reading from either this session's main streamed source or its secondary (filtered) image.

   **Signature:** ``buildMaterializedCrop(BoundingBox) -> MaterializedCrop``

   **Parameters:**

   * **worldBox** (``BoundingBox``)

   **Returns:** ``Any``

.. method:: changeUIState(newState)

   **Signature:** ``changeUIState(int) -> void``

   **Parameters:**

   * **newState** (``int``)

   **Returns:** ``None``

.. method:: closeAndResetAllPanes()

   **Signature:** ``closeAndResetAllPanes() -> void``

   **Returns:** ``None``

.. method:: confirmTemporary(updateTracingViewers)

   **Signature:** ``confirmTemporary(boolean) -> void``

   **Parameters:**

   * **updateTracingViewers** (``bool``)

   **Returns:** ``None``

.. method:: createCanvas(imagePlus, plane)

   **Signature:** ``createCanvas(ImagePlus, int) -> InteractiveTracerCanvas``

   **Parameters:**

   * **imagePlus** (``Any``)
   * **plane** (``int``)

   **Returns:** ``Any``

.. method:: editModeAllowed()

   Checks if edit mode can be enabled, optionally using a specific path.

   **Signature:** ``editModeAllowed() -> boolean``

   **Returns:** (``bool``) true if edit mode is allowed, false otherwise

.. method:: enterEditMode(pathToEdit)

   Enables 'Edit Mode' on all front-ends (tracing canvas, Bdv and Bvv)

   **Signature:** ``enterEditMode(Path) -> boolean``

   **Parameters:**

   * **pathToEdit** (``Path``): - the path to be edited. It is selected (replacing the current selection) if not already the single selected path, since all edit operations require the editing path to be selected. If null, the single selected path is used

   **Returns:** (``bool``) true if 'Edit Mode' was enabled. See `getEditModeBlocker()` if not

.. method:: estimateMaterializationBytes(width, height, depth)

   Estimates the number of bytes required to materialize a crop of the given voxel dimensions from this session's streamed source (see `materializeDisplayCanvas(BoundingBox)`), using the source's actual pixel type.

   **Signature:** ``estimateMaterializationBytes(long, long, long) -> long``

   **Parameters:**

   * **width** (``int``): - the crop's width, in voxels
   * **height** (``int``)
   * **depth** (``int``)

   **Returns:** (``int``) the estimated byte count, or -1 if no streamed source is available to estimate from

.. method:: exitEditMode()

   Disables 'Edit Mode' on all front-ends (tracing canvas, Bdv and Bvv)

   **Signature:** ``exitEditMode() -> void``

   **Returns:** ``None``

.. method:: findPointInStack(x_in_pane, y_in_pane, plane, point)

   **Signature:** ``findPointInStack(int, int, int, int[]) -> void``

   **Parameters:**

   * **x_in_pane** (``int``)
   * **y_in_pane** (``int``)
   * **plane** (``int``)
   * **point** (``List[int]``)

   **Returns:** ``None``

.. method:: findPointInStackPrecise(x_in_pane, y_in_pane, plane, point)

   **Signature:** ``findPointInStackPrecise(double, double, int, double[]) -> void``

   **Parameters:**

   * **x_in_pane** (``float``)
   * **y_in_pane** (``float``)
   * **plane** (``int``)
   * **point** (``List[float]``)

   **Returns:** ``None``

.. method:: finished(source, success)

   **Signature:** ``finished(SearchInterface, boolean) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **success** (``bool``)

   **Returns:** ``None``

.. method:: flushSecondaryData()

   **Signature:** ``flushSecondaryData() -> void``

   **Returns:** ``None``

.. method:: initialize(imp)

   **Signature:** ``initialize(ImagePlus) -> void``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``None``

.. method:: installMaterializedCrop(crop)

   Installs a crop built by `buildMaterializedCrop(BoundingBox)` as this session's own XY canvas, in place, the same mechanism `rebuildDisplayCanvases()` uses for the blank placeholder, but with real pixel data instead of an empty image. This allows right-click editing (extend/fork/join/delete nodes, wired into `InteractiveTracerCanvas`) real pixel context in Stream mode, where BDV/BVV have no equivalent context menu.

Deliberately scoped to editing, not tracing: this reuses the normal `initialize(ImagePlus)` pipeline, which also replaces `ctSlice3d` with the crop's own (small) pixel data. A* search/GWDT tracing initiated after materializing is therefore scoped to the crop's own bounds, not the full streamed volume, until a different region is materialized (or the session is reconnected). There is no path for pixel edits to write back into the canonical streamed source: only geometry/paths persist, pixel edits are local to this session.

   **Signature:** ``installMaterializedCrop(MaterializedCrop) -> void``

   **Parameters:**

   * **crop** (``Any``): - the crop to install, from buildMaterializedCrop(BoundingBox)

   **Returns:** ``None``

.. method:: is2D()

   **Signature:** ``is2D() -> boolean``

   **Returns:** (``bool``) true if the image currently loaded does not have a depth (Z) dimension

.. method:: manualTrace(start, end, forkPoint)

   Manually traces a straight path from a point A to a point B, bypassing A* (or any other configured `SearchInterface`) entirely: the two points are simply connected via `ManualTracerThread`. Unlike `autoTrace(SNTPoint, SNTPoint, PointInImage, boolean)`, this method does not depend on, or alter, `isAstarEnabled()`. Runs headless (no SNTUI state changes) and, since it does not search the image, is cheap enough to be safely called off the EDT.

The returned path is *not* added to the Path Manager: callers are responsible for that (see `PathAndFillManager.addPath(Path, boolean, boolean)`).

   **Signature:** ``manualTrace(SNTPoint, SNTPoint, PointInImage) -> Path``

   **Parameters:**

   * **start** (``SNTPoint``): - the SNTPoint start of the path
   * **end** (``SNTPoint``)
   * **forkPoint** (``PointInImage``)

   **Returns:** (``Path``) the path a reference to the computed path.

.. method:: materializeDisplayCanvas(worldBox)

   As `materializeDisplayCanvas(BoundingBox)`, but reading from either this session's main streamed source or its secondary (filtered) image - see `buildMaterializedCrop(BoundingBox, boolean)`.

   **Signature:** ``materializeDisplayCanvas(BoundingBox) -> void``

   **Parameters:**

   * **worldBox** (``BoundingBox``)

   **Returns:** ``None``

.. method:: mouseMovedTo(off_screen_x, off_screen_y, in_plane, shift_down)

   **Signature:** ``mouseMovedTo(double, double, int, boolean) -> void``

   **Parameters:**

   * **off_screen_x** (``float``)
   * **off_screen_y** (``float``)
   * **in_plane** (``int``)
   * **shift_down** (``bool``)

   **Returns:** ``None``

.. method:: notifyActiveNodeChanged(source)

   Refreshes the active-node (and lock) markers of the Bdv/Bvv viewers after the active node of the editing path was changed or (un)locked by another front-end

   **Signature:** ``notifyActiveNodeChanged(AbstractBigViewer) -> void``

   **Parameters:**

   * **source** (``Any``): - the viewer that originated the change, which is not notified. null if the change was not made by a viewer

   **Returns:** ``None``

.. method:: notifyListeners(event)

   **Signature:** ``notifyListeners(SNTEvent) -> void``

   **Parameters:**

   * **event** (``Any``)

   **Returns:** ``None``

.. method:: panEventOccurred(off_screen_x, off_screen_y, in_plane)

   **Signature:** ``panEventOccurred(int, int, int) -> void``

   **Parameters:**

   * **off_screen_x** (``int``)
   * **off_screen_y** (``int``)
   * **in_plane** (``int``)

   **Returns:** ``None``

.. method:: pointsInSearch(source, inOpen, inClosed)

   **Signature:** ``pointsInSearch(SearchInterface, long, long) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **inOpen** (``int``)
   * **inClosed** (``int``)

   **Returns:** ``None``

.. method:: proportionDone(proportion)

   **Signature:** ``proportionDone(double) -> void``

   **Parameters:**

   * **proportion** (``float``)

   **Returns:** ``None``

.. method:: rebuildDisplayCanvases()

   Rebuilds display canvases, i.e., the placeholder canvases used when no valid image data exists (a single-canvas is rebuilt if only the XY view is active).

Useful when multiple files are imported and imported paths 'fall off' the dimensions of current canvas(es). If there is not enough memory to accommodate enlarged dimensions, the resulting canvas will be a 2D image.

   **Signature:** ``rebuildDisplayCanvases() -> void``

   **Returns:** ``None``

.. method:: rebuildZYXZpanes()

   **Signature:** ``rebuildZYXZpanes() -> void``

   **Returns:** ``None``

.. method:: reloadImage(channel, frame)

   **Signature:** ``reloadImage(int, int) -> void``

   **Parameters:**

   * **channel** (``int``)
   * **frame** (``int``)

   **Returns:** ``None``

.. method:: reloadZYXZpanes(frame)

   **Signature:** ``reloadZYXZpanes(int) -> void``

   **Parameters:**

   * **frame** (``int``)

   **Returns:** ``None``

.. method:: repaintAllPanes()

   **Signature:** ``repaintAllPanes() -> void``

   **Returns:** ``None``

.. method:: resolveVoxelBounds(worldBox, cal)

   As `resolveVoxelBounds(BoundingBox, Calibration)`, but resolving against either this session's main streamed source or its secondary (filtered) image - see `buildMaterializedCrop(BoundingBox, boolean)`.

   **Signature:** ``resolveVoxelBounds(BoundingBox, Calibration) -> VoxelBounds``

   **Parameters:**

   * **worldBox** (``BoundingBox``): - if true, resolves against getSecondaryData() instead of the main streamed source
   * **cal** (``Any``)

   **Returns:** ``Any``

.. method:: sameXYZDimensionsAsTracingData(imp)

   RAI-based overload of `sameXYZDimensionsAsTracingData(ImagePlus)`, for candidate sources that never go through an `ImagePlus` at all (e.g. a big-data secondary layer resolved via `SpimDataUtils.resolvePathToSource(String)`). Compares XYZ dimensions directly against `getLoadedData()`, so unlike the `ImagePlus` overload this works the same regardless of whether `MultiDThreePanes.xy` exists.

   **Signature:** ``sameXYZDimensionsAsTracingData(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the candidate image data

   **Returns:** (``bool``) true if dimensions match; false if they don't, or if no tracing data is loaded to compare against

.. method:: seedStatsFromSubVolume(imp)

   In Stream mode, seeds unknown main image statistics (min, max) from a small sub-volume already in memory (e.g., the Sigma Palette crop). Computing them from the whole image would require reading every chunk of lazy/remote data. Statistics from a sub-volume are local estimates. Does nothing if statistics are already known.

   **Signature:** ``seedStatsFromSubVolume(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the sub-volume

   **Returns:** (``bool``) true if main image statistics are available after this call

.. method:: selectNone()

   Clears the current path selection. Does nothing in edit mode

   **Signature:** ``selectNone() -> boolean``

   **Returns:** (``bool``) true if any path was deselected

.. method:: snapshotSearchSettings()

   Captures the search settings currently configured on this instance, for use by long-running batch callers that need to stay internally consistent even if these settings are changed (via the UI) partway through the run. See `SNT.SearchSettingsSnapshot`.

   **Signature:** ``snapshotSearchSettings() -> SearchSettingsSnapshot``

   **Returns:** (``Any``) an immutable snapshot of the current cost function, data structure, and secondary (filtered) image state

.. method:: startHessian(image, sigma, max, wait)

   Constructs and enables an instance of a hessian eigenvalue filter. If the strategy is "preprocess", the entire filtered image is pre-computed and stored in memory. If the strategy is "lazy", the image is filtered locally during path searches, and filtered data is stored in a disk cache when memory runs full. If you are tracing over a large image or if you are in a memory-limited environment, you should choose "lazy".

   **Signature:** ``startHessian(String, double, double, boolean) -> void``

   **Parameters:**

   * **image** (``str``): - the image to filter, either "primary" or "secondary".
   * **sigma** (``float``)
   * **max** (``float``)
   * **wait** (``bool``)

   **Returns:** ``None``

.. method:: startSholl(centerScaled)

   **Signature:** ``startSholl(PointInImage) -> void``

   **Parameters:**

   * **centerScaled** (``PointInImage``)

   **Returns:** ``None``

.. method:: startUI()

   **Signature:** ``startUI() -> void``

   **Returns:** ``None``

.. method:: threadStatus(source, status)

   **Signature:** ``threadStatus(SearchInterface, int) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **status** (``int``)

   **Returns:** ``None``

.. method:: unzoomAllPanes()

   **Signature:** ``unzoomAllPanes() -> void``

   **Returns:** ``None``

.. method:: updateDisplayCanvases()

   Rebuilds display canvas(es) to ensure all paths are contained in the image. Does nothing if placeholder canvas(es) are not being used.

   **Signature:** ``updateDisplayCanvases() -> void``

   **Returns:** ``None``

.. method:: zoom100PercentAllPanes()

   **Signature:** ``zoom100PercentAllPanes() -> void``

   **Returns:** ``None``

.. method:: zoomAllPanes(zoomFactor)

   **Signature:** ``zoomAllPanes(double) -> void``

   **Parameters:**

   * **zoomFactor** (``float``)

   **Returns:** ``None``

.. method:: zoomEventOccurred(in, off_screen_x, off_screen_y, in_plane)

   **Signature:** ``zoomEventOccurred(boolean, int, int, int) -> void``

   **Parameters:**

   * **in** (``bool``)
   * **off_screen_x** (``int``)
   * **off_screen_y** (``int``)
   * **in_plane** (``int``)

   **Returns:** ``None``


SNTChart
--------

.. method:: annotate(label)

   Adds a subtitle to the chart.

   **Signature:** ``annotate(String) -> void``

   **Parameters:**

   * **label** (``str``): - the subtitle text

   **Returns:** ``None``

.. method:: annotateCategory(category, label)

   Annotates the specified category (Category plots only).

   **Signature:** ``annotateCategory(String, String) -> void``

   **Parameters:**

   * **category** (``str``): - the category to be annotated. Ignored if it does not exist in category axis.
   * **label** (``str``)

   **Returns:** ``None``

.. method:: annotatePoint(x, y, label)

   Highlights a point in a histogram/XY plot by drawing a labeled arrow at the specified location.

   **Signature:** ``annotatePoint(double, double, String) -> void``

   **Parameters:**

   * **x** (``float``): - the array holding the focal point coordinates of the profile
   * **y** (``float``)
   * **label** (``str``)

   **Returns:** ``None``

.. method:: annotateXline(xValue, label)

   Annotates the specified X-value (XY plots and histograms).

   **Signature:** ``annotateXline(double, String) -> void``

   **Parameters:**

   * **xValue** (``float``): - the X value to be annotated.
   * **label** (``str``)

   **Returns:** ``None``

.. method:: annotateYline(yValue, label)

   Annotates the specified Y-value (XY plots and histograms).

   **Signature:** ``annotateYline(double, String) -> void``

   **Parameters:**

   * **yValue** (``float``): - the Y value to be annotated.
   * **label** (``str``)

   **Returns:** ``None``

.. method:: applyStyle(template)

   **Signature:** ``applyStyle(SNTChart) -> void``

   **Parameters:**

   * **template** (``SNTChart``)

   **Returns:** ``None``

.. method:: closeAll()

   Closes all open charts

   **Signature:** ``closeAll() -> void``

   **Returns:** ``None``

.. method:: combine(charts)

   Combines a collection of charts into a multipanel montage.

   **Signature:** ``combine(Collection) -> SNTChart``

   **Parameters:**

   * **charts** (``List[Any]``): - input charts

   **Returns:** (``SNTChart``) the frame containing the montage

.. method:: combineAsImagePlus(charts)

   Combines a collection of charts into a ImageJ1 stack.

   **Signature:** ``combineAsImagePlus(Collection) -> ImagePlus``

   **Parameters:**

   * **charts** (``List[Any]``): - input charts

   **Returns:** (``Any``) the stack as an ImagePlus (RGB)

.. method:: containsValidData()

   Checks if the chart contains valid data.

Returns true if the chart object exists and presumably contains data that can be displayed.

   **Signature:** ``containsValidData() -> boolean``

   **Returns:** (``bool``) whether chart contains valid Data

.. method:: dispose()

   Disposes of this chart and releases its resources.

Closes the chart window and removes it from the list of open instances. This method should be called when the chart is no longer needed to prevent memory leaks.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: openCharts()

   **Signature:** ``openCharts() -> List``

   **Returns:** (``List[Any]``) a list of all opened charts

.. method:: replace(other)

   Replaces the current chart with the specified instance

   **Signature:** ``replace(SNTChart) -> void``

   **Parameters:**

   * **other** (``SNTChart``): - the instance replacing current contents

   **Returns:** ``None``

.. method:: save(file)

   Saves this chart.

   **Signature:** ``save(File) -> boolean``

   **Parameters:**

   * **file** (``str``): - the path of the output file (null not permitted). Its filename extension (".svg", ".png", ".pdf"), determines the file format.

   **Returns:** (``bool``) true if file was successfully saved, false otherwise

.. method:: shadeXRegion(from, to, color)

   Shades a region of the domain (X) axis as a background band.

   **Signature:** ``shadeXRegion(double, double, String) -> void``

   **Parameters:**

   * **from** (``float``): - the lower X value of the shaded region
   * **to** (``float``)
   * **color** (``str``)

   **Returns:** ``None``

.. method:: show()

   **Signature:** ``show() -> void``

   **Returns:** ``None``

.. method:: tile(charts)

   Tiles specified charts displaying them on a grid. Charts's windows are made visible if not displayed.

   **Signature:** ``tile(Collection) -> void``

   **Parameters:**

   * **charts** (``List[Any]``): - the charts to be tiled

   **Returns:** ``None``

.. method:: tileAll()

   Tiles all open charts displaying them on a grid. Charts's windows are made visible if not displayed.

   **Signature:** ``tileAll() -> void``

   **Returns:** ``None``


SNTColor
--------

.. method:: average(colors)

   Averages a collection of colors

   **Signature:** ``average(Collection) -> Color``

   **Parameters:**

   * **colors** (``List[Any]``): - the colors to be averaged

   **Returns:** (``Any``) the averaged color. Note that an average will never be accurate because the RGB space is not linear. Color.BLACK is returned if all colors in input collection are null;

.. method:: equals(obj)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **obj** (``Any``)

   **Returns:** ``bool``

.. method:: fromHex(hex)

   Returns an AWT Color from a (#)RRGGBB(AA) hex string.

   **Signature:** ``fromHex(String) -> Color``

   **Parameters:**

   * **hex** (``str``): - the input string

   **Returns:** (``Any``) the converted AWT color

.. method:: fromString(colorName)

   Returns an AWT Color from any css-valid co

   **Signature:** ``fromString(String) -> Color``

   **Parameters:**

   * **colorName** (``str``): - the input string

   **Returns:** (``Any``) the converted AWT color

.. method:: interpolateNullEntries(colors)

   Replaces null colors in an array with the average of flanking non-null colors.

   **Signature:** ``interpolateNullEntries(Color[]) -> void``

   **Parameters:**

   * **colors** (``List[Any]``): - the color array

   **Returns:** ``None``

.. method:: mix(c1, c2, weight)

   Linearly mixes two colors together based on a specified weight, using a gamma-corrected linear blend by squaring the individual color channels before mixing

   **Signature:** ``mix(Color, Color, double) -> Color``

   **Parameters:**

   * **c1** (``Any``): - the starting color (used completely when
   * **c2** (``Any``): is 0.0)
   * **weight** (``float``)

   **Returns:** (``Any``) a new `Color` object representing the combined result

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``

.. method:: type()

   Retrieves the SWC type

   **Signature:** ``type() -> int``

   **Returns:** (``int``) the SWC type integer flag

.. method:: valueOf(colorSpec)

   Parses a color from the given string.

The following formats are supported: Hex format [HTML color codes starting with hash (#)], Color presets (e.g., 'blue', 'pink', 'silver', etc.), and integer triples of the form r,g,b, with each element in the range [0, 255].

   **Signature:** ``valueOf(String) -> ColorRGB``

   **Parameters:**

   * **colorSpec** (``str``): - string defining the color value

   **Returns:** (``Any``) the color


SNTGraph
--------

.. method:: applyEdges(operator)

   **Signature:** ``applyEdges(UnaryOperator) -> void``

   **Parameters:**

   * **operator** (``Any``)

   **Returns:** ``None``

.. method:: applyVertices(operator)

   **Signature:** ``applyVertices(UnaryOperator) -> void``

   **Parameters:**

   * **operator** (``Any``)

   **Returns:** ``None``

.. method:: filterEdges(predicate)

   **Signature:** ``filterEdges(Predicate) -> void``

   **Parameters:**

   * **predicate** (``Any``)

   **Returns:** ``None``

.. method:: filterVertices(predicate)

   **Signature:** ``filterVertices(Predicate) -> void``

   **Parameters:**

   * **predicate** (``Any``)

   **Returns:** ``None``


SNTPoint
--------

.. method:: average(points)

   Computes the average position of a collection of SNTPoints.

   **Signature:** ``average(Collection) -> PointInImage``

   **Parameters:**

   * **points** (``List[Any]``): - the collection of points to average

   **Returns:** (``PointInImage``) the average point, or null if the collection is null or empty

.. method:: fromString(string)

   **Signature:** ``fromString(String) -> PointInImage``

   **Parameters:**

   * **string** (``str``)

   **Returns:** ``PointInImage``

.. method:: of(coords)

   **Signature:** ``of(Number[]) -> PointInImage``

   **Parameters:**

   * **coords** (``List[Union[int, float]]``)

   **Returns:** ``PointInImage``


SNTPrefs
--------

.. method:: ensureWorkspaceExists()

   Creates workspace directory if it doesn't exist.

   **Signature:** ``ensureWorkspaceExists() -> boolean``

   **Returns:** (``bool``) true if directory exists or was created successfully

.. method:: firstRun()

   Checks if SNT has ever been run before on this system, consuming the check in the process: the very first call ever made to this method returns `true`; every call after that returns `false`.

   **Signature:** ``firstRun() -> boolean``

   **Returns:** (``bool``) true only the very first time this is ever called (or after preferences have been cleared)

.. method:: firstRunAfterUpdate()

   Checks if this is the first run after an SNT update.

   **Signature:** ``firstRunAfterUpdate() -> boolean``

   **Returns:** (``bool``) true if this is the first run after an update, false otherwise

.. method:: get(key, defaultValue)

   Gets a string preference value.

   **Signature:** ``get(String, String) -> String``

   **Parameters:**

   * **key** (``str``): - the preference key
   * **defaultValue** (``str``)

   **Returns:** (``str``) the string preference value

.. method:: is2DDisplayCanvas()

   Checks if 2D display canvas is forced.

   **Signature:** ``is2DDisplayCanvas() -> boolean``

   **Returns:** (``bool``) true if 2D display canvas is forced, false otherwise

.. method:: lastKnownDir()

   **Signature:** ``lastKnownDir() -> File``

   **Returns:** ``str``

.. method:: set(key, value)

   Sets a boolean preference value.

   **Signature:** ``set(String, String) -> void``

   **Parameters:**

   * **key** (``str``): - the preference key
   * **value** (``str``)

   **Returns:** ``None``

.. method:: set2DDisplayCanvas(bool)

   Sets whether to force 2D display canvas.

   **Signature:** ``set2DDisplayCanvas(boolean) -> void``

   **Parameters:**

   * **bool** (``bool``): - true to force 2D display canvas, false otherwise

   **Returns:** ``None``

.. method:: workspaceIsValid()

   **Signature:** ``workspaceIsValid() -> boolean``

   **Returns:** (``bool``) true if workspace directory exists and has write permissions.


SNTService
----------

.. method:: assignValues(selectedPathsOnly)

   Assigns pixel intensities at each Path node, storing them as Path values. Assigned intensities are those of the channel and time point currently being traced. Assumes SNT has been initialized with a valid image.

   **Signature:** ``assignValues(boolean) -> void``

   **Parameters:**

   * **selectedPathsOnly** (``bool``): - If true, only selected paths will be assigned values, otherwise voxel intensities will be assigned to all paths

   **Returns:** ``None``

.. method:: demoImage(img)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.

   **Signature:** ``demoImage(String) -> ImagePlus``

   **Parameters:**

   * **img** (``str``): - a string describing the type of demo image. Options include: 'fractal' for the L-system toy neuron; 'ddaC' for the C4 ddaC drosophila neuron (demo image initially distributed with the Sholl plugin); 'OP1'/'OP_1' for the DIADEM OP_1 dataset; 'cil701', 'cil810', or 'ci41458' for the respective Cell Image Library entries, and 'binary timelapse' for a small 4-frame sequence of neurite growth

   **Returns:** (``Any``) the demo image, or null if data could not be retrieved

.. method:: demoImgPlus(img)

   Returns one of the demo images bundled with SNT as an `ImgPlus`. This is the imglib2 counterpart of `demoImage(String)`.

   **Signature:** ``demoImgPlus(String) -> ImgPlus``

   **Parameters:**

   * **img** (``str``): - a string describing the type of demo image (same options as demoImage(String))

   **Returns:** (``Any``) the demo image as an ImgPlus, or null if data could not be retrieved or converted

.. method:: demoTree()

   Returns a demo tree.

   **Signature:** ``demoTree() -> Tree``

   **Returns:** ``Tree``

.. method:: demoTrees()

   Returns a collection of four demo reconstructions (dendrites from pyramidal cells from the MouseLight database). NB: Data is cached locally. No internet connection required.

   **Signature:** ``demoTrees() -> List``

   **Returns:** (``List[Any]``) the list of `Tree`s, corresponding to the dendritic arbors of cells "AA0001", "AA0002", "AA0003", "AA0004" (MouseLight database IDs).

.. method:: dispose()

   Quits SNT. Does nothing if SNT is currently not running.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: initialize(startUI)

   Initializes SNT from an `ImgPlus` image. This is the imglib2 counterpart of `initialize(ImagePlus, boolean)`.

   **Signature:** ``initialize(boolean) -> SNT``

   **Parameters:**

   * **startUI** (``bool``): - the image to be traced (null not allowed)

   **Returns:** (``SNT``) the SNT instance.

.. method:: requireVersion(minVersion)

   Ensures the running SNT version meets a minimum requirement. This is analogous to IJ's `requires()` macro function.

   **Signature:** ``requireVersion(String) -> void``

   **Parameters:**

   * **minVersion** (``str``): - the minimum required version string, e.g.,

   **Returns:** ``None``

.. method:: save(filePath)

   Saves all the existing paths to a file.

   **Signature:** ``save(String) -> boolean``

   **Parameters:**

   * **filePath** (``str``): - the saving output file path. If

   **Returns:** (``bool``) true, if paths exist and file was successfully written.


SNTTable
--------

.. method:: appendToLastRow(colHeader, value)

   Appends a value to the last row in the specified column.

If the table is empty, a new row is created first. The value is then set in the specified column of the last row.

   **Signature:** ``appendToLastRow(String, Object) -> void``

   **Parameters:**

   * **colHeader** (``str``): - the column header
   * **value** (``Any``)

   **Returns:** ``None``

.. method:: asDouble(cell)

   Coerces a table cell to a `double`. Cells may be typed `Double`, `Long`, or `String` depending on how the table was parsed (e.g. CSV column-type inference); this accepts any of those, with a String parse fallback for a numeric-looking value stored in a non-numeric column

   **Signature:** ``asDouble(Object) -> double``

   **Parameters:**

   * **cell** (``Any``): - a cell value, e.g. from

   **Returns:** (``float``) the coerced value, or `Double.NaN` if `cell` is null, empty, or not parseable as a number

.. method:: asInt(cell, fallback)

   Coerces a table cell to an `int`. Tolerates a Double-shaped integer string (e.g. `"1.0"` -> `1`)

   **Signature:** ``asInt(Object, int) -> int``

   **Parameters:**

   * **cell** (``Any``): - a cell value, e.g. from
   * **fallback** (``int``)

   **Returns:** (``int``) the coerced value, or `fallback`

.. method:: asString(cell, fallback)

   Coerces a table cell to a trimmed `String`

   **Signature:** ``asString(Object, String) -> String``

   **Parameters:**

   * **cell** (``Any``): - a cell value, e.g. from
   * **fallback** (``str``)

   **Returns:** (``str``) the coerced value, or `fallback`

.. method:: clear()

   **Signature:** ``clear() -> void``

   **Returns:** ``None``

.. method:: createOrUpdateDisplay()

   Creates a new display or updates an existing one.

If no display exists, creates a new table display window. If a display already exists, updates it with the current table contents.

   **Signature:** ``createOrUpdateDisplay() -> void``

   **Returns:** ``None``

.. method:: fillEmptyCells(value)

   Fills all empty cells in the table with the specified value.

Iterates through all cells in the table and replaces null values with the provided replacement value.

   **Signature:** ``fillEmptyCells(Object) -> void``

   **Parameters:**

   * **value** (``Any``): - the value to use for filling empty cells

   **Returns:** ``None``

.. method:: findColumnIndex(columnHeader)

   Case-/whitespace-insensitive column lookup.

   **Signature:** ``findColumnIndex(String) -> int``

   **Parameters:**

   * **columnHeader** (``str``)

   **Returns:** ``int``

.. method:: fromGenericTable(source)

   **Signature:** ``fromGenericTable(GenericTable) -> SNTTable``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``SNTTable``

.. method:: geColumnStats(colHeader, startRowIndex, endRowIndex)

   **Signature:** ``geColumnStats(String, int, int) -> SummaryStatistics``

   **Parameters:**

   * **colHeader** (``str``)
   * **startRowIndex** (``int``)
   * **endRowIndex** (``int``)

   **Returns:** ``Any``

.. method:: geRowStats(rowHeader, startColumnIndex, endColumnIndex)

   **Signature:** ``geRowStats(String, int, int) -> SummaryStatistics``

   **Parameters:**

   * **rowHeader** (``str``)
   * **startColumnIndex** (``int``)
   * **endColumnIndex** (``int``)

   **Returns:** ``Any``

.. method:: insertRow(header)

   **Signature:** ``insertRow(String) -> int``

   **Parameters:**

   * **header** (``str``)

   **Returns:** ``int``

.. method:: replace(columnHeadersPattern, originalValue, replacementValue)

   **Signature:** ``replace(String, double, double) -> void``

   **Parameters:**

   * **columnHeadersPattern** (``str``)
   * **originalValue** (``float``)
   * **replacementValue** (``float``)

   **Returns:** ``None``

.. method:: save(outputFile)

   **Signature:** ``save(File) -> void``

   **Parameters:**

   * **outputFile** (``str``)

   **Returns:** ``None``

.. method:: set(colHeader, rowHeader, value)

   **Signature:** ``set(String, String, Object) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **rowHeader** (``str``)
   * **value** (``Any``)

   **Returns:** ``None``

.. method:: show()

   **Signature:** ``show() -> void``

   **Returns:** ``None``

.. method:: summarize()

   **Signature:** ``summarize() -> void``

   **Returns:** ``None``

.. method:: toString(table)

   **Signature:** ``toString(GenericTable) -> String``

   **Parameters:**

   * **table** (``Any``)

   **Returns:** ``str``

.. method:: updateDisplay()

   Updates the existing table display.

Refreshes the table display with the current table contents without creating a new display window.

   **Signature:** ``updateDisplay() -> void``

   **Returns:** ``None``


SNTUI
-----

.. method:: changeState(newState)

   Changes this UI to a new state. Does nothing if `newState` is the current UI state

   **Signature:** ``changeState(int) -> void``

   **Parameters:**

   * **newState** (``int``): - the new state, e.g., READY, TRACING_PAUSED, etc.

   **Returns:** ``None``

.. method:: close()

   Closes this SNT session, asking for confirmation only if there are unsaved paths or measurements

   **Signature:** ``close() -> boolean``

   **Returns:** (``bool``) true if the session was closed, false if the user canceled

.. method:: error(msg)

   Displays an error message.

   **Signature:** ``error(String) -> void``

   **Parameters:**

   * **msg** (``str``): - the error message

   **Returns:** ``None``

.. method:: launchSigmaPaletteAround(x, y, z)

   Crops a small region around the given point and launches the `SigmaPalette` preview grid, exactly as if the user had clicked at that position on the classic-mode tracing canvas (see `InteractiveTracerCanvas#startSigmaWizard`). Public (rather than the previous `protected`) so it can also be triggered from a Bdv/Bvv viewer action, since there is no classic canvas to click on in Stream mode (see `AbstractBigViewer.Actions#pickSigmaPointAction()`).

   **Signature:** ``launchSigmaPaletteAround(int, int, int) -> void``

   **Parameters:**

   * **x** (``int``): - pixel X position (0-based)
   * **y** (``int``)
   * **z** (``int``)

   **Returns:** ``None``

.. method:: launchSigmaPaletteAroundStreamed(x, y, z)

   Crop-independent counterpart of `launchSigmaPaletteAround(int, int, int)`: sources its bounds from `SNT.getFullSourceData()` instead of `SNT.getLoadedData()`, so a BDV/BVV click that lands outside a materialized crop's (smaller) bounds still previews the region actually clicked, instead of silently clamping to the crop's edge. See `AbstractBigViewer.Actions#pickSigmaPointAction()`, which pairs this with `SNT.getDefaultCanvasPixelOffset()` to convert the click.

   **Signature:** ``launchSigmaPaletteAroundStreamed(int, int, int) -> void``

   **Parameters:**

   * **x** (``int``): - pixel X position (0-based), in SNT.getFullSourceData()'s own grid
   * **y** (``int``)
   * **z** (``int``)

   **Returns:** ``None``

.. method:: pause(pause)

   Pauses/Resume SNT (equivalent to command in image contextual menu).

   **Signature:** ``pause(boolean) -> void``

   **Parameters:**

   * **pause** (``bool``): - whether SNT should be paused/resumed

   **Returns:** ``None``

.. method:: pauseTracing(pause)

   Pauses/Resume tracing functions (equivalent to command in image contextual menu).

   **Signature:** ``pauseTracing(boolean) -> void``

   **Parameters:**

   * **pause** (``bool``): - whether tracing functions should be paused/resumed

   **Returns:** ``None``

.. method:: refresh()

   Updates the dialog, including status bar and 'computation settings' widget.

   **Signature:** ``refresh() -> void``

   **Returns:** ``None``

.. method:: registerActiveCmdWorker(worker)

   Registers (or clears, if `worker` is `null`) the `SwingWorker` currently executing a long-running `CommonDynamicCmd`. Unlike commands launched via `DynamicCmdRunner`, these keep running on their own background thread long after the initiating dialog has closed and `currentState` has reverted to whatever it was before the dialog opened, so they cannot rely on the switch inside `abortCurrentOperation()`. Cancellation is not forcible: the running code must itself poll `Thread.isInterrupted()` (see `AbstractGWDTTracer`'s hot loops) for this to have any effect.

   **Signature:** ``registerActiveCmdWorker(SwingWorker) -> void``

   **Parameters:**

   * **worker** (``Any``): - the worker to register, or

   **Returns:** ``None``

.. method:: resetUI()

   Full reset: closes any tethered `Bvv`/`Bdv` viewer (via `closeBigViewers()`) and the current image, and clears all paths, restoring the UI to its initial, blank-canvas state. Intended for callers that need a guaranteed-fresh session regardless of whatever was open before.

   **Signature:** ``resetUI() -> boolean``

   **Returns:** (``bool``) true if the reset completed; false if it was aborted (e.g. the current image has unsaved changes and the user did not resolve ImageJ's own "Save Changes?" prompt), in which case nothing else was changed

.. method:: runAutotracingWizard()

   Launches the autotracing wizard for the active image.

The tracer implementation is selected based on image type:

- **Binary images** : `BinaryTracerCmd` (topology-based skeletonization)

- **Grayscale images** : `GWDTTracerCmd` (intensity-weighted distance transform)

   **Signature:** ``runAutotracingWizard() -> void``

   **Returns:** ``None``

.. method:: runCommand(cmd)

   Runs a Scijava command associated with SNT.

   **Signature:** ``runCommand(String) -> void``

   **Parameters:**

   * **cmd** (``str``): - The command class to be run, exactly as listed in SNTUI's menu bar

   **Returns:** ``None``

.. method:: runSecondaryLayerWizard()

   Runs the 'secondary layer wizard' in the background, without displaying prompt.

   **Signature:** ``runSecondaryLayerWizard() -> void``

   **Returns:** ``None``

.. method:: selectTab(tabTitle)

   Activates the specified tab.

   **Signature:** ``selectTab(String) -> void``

   **Parameters:**

   * **tabTitle** (``str``): - The tab title (e.g., "Main", "3D");

   **Returns:** ``None``


SNTUtils
--------

.. method:: csvQuoteAndPrint(pw, o)

   **Signature:** ``csvQuoteAndPrint(PrintWriter, Object) -> void``

   **Parameters:**

   * **pw** (``Any``)
   * **o** (``Any``)

   **Returns:** ``None``

.. method:: downloadAndExtractZip(zipUrl)

   Downloads a zip archive from the specified URL and extracts it to a fresh temporary directory. Both the downloaded archive and the extracted contents are marked for deletion on JVM exit; the archive itself is also deleted immediately once extraction succeeds, since it is not needed afterward.

   **Signature:** ``downloadAndExtractZip(String) -> File``

   **Parameters:**

   * **zipUrl** (``str``): - the URL of the zip archive to download and extract

   **Returns:** (``str``) the temporary directory holding the extracted contents

.. method:: error(string)

   As `error(String, Throwable)`, but allows suppressing the notification-center mirroring, e.g., when the caller has already surfaced the message to the user synchronously (a modal dialog)

   **Signature:** ``error(String) -> void``

   **Parameters:**

   * **string** (``str``): - the message

   **Returns:** ``None``

.. method:: extractReadableTimeStamp(file)

   **Signature:** ``extractReadableTimeStamp(File) -> String``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``str``

.. method:: findClosestPair(file, pairExt)

   **Signature:** ``findClosestPair(File, String) -> File``

   **Parameters:**

   * **file** (``str``)
   * **pairExt** (``str``)

   **Returns:** ``str``

.. method:: formatBytes(bytes)

   **Signature:** ``formatBytes(long) -> String``

   **Parameters:**

   * **bytes** (``int``): - a byte count

   **Returns:** (``str``) a human-readable representation (e.g., "12.3 MB")

.. method:: formatDouble(value, digits)

   **Signature:** ``formatDouble(double, int) -> String``

   **Parameters:**

   * **value** (``float``)
   * **digits** (``int``)

   **Returns:** ``str``

.. method:: log(string)

   **Signature:** ``log(String) -> void``

   **Parameters:**

   * **string** (``str``)

   **Returns:** ``None``

.. method:: nowTruncatedToSeconds()

   Returns the current date-time truncated to whole seconds, e.g., for stamping exported content with a generation time.

   **Signature:** ``nowTruncatedToSeconds() -> LocalDateTime``

   **Returns:** ``Any``

.. method:: openRemoteStream(url)

   Opens an `InputStream` to `url` with explicit connect/read timeouts, so a stalled or unreachable remote host fails with a clear `IOException` instead of hanging indefinitely - the default behavior of `URL.openStream()`, whose underlying `URLConnection` has no timeout at all unless one is set explicitly. Used for remote reconstruction/marker/demo files (e.g. `https://.../autotracings.traces`), which are typically small enough that a single bounded connection (rather than `runWithTimeout(java.util.concurrent.Callable<T>, long, java.lang.String)`'s background-thread wrapper) is enough.

   **Signature:** ``openRemoteStream(String) -> InputStream``

   **Parameters:**

   * **url** (``str``): - the URL to open (e.g. a remote .traces/.csv file, or a .zip archive)

   **Returns:** (``Any``) an InputStream ready to be read

.. method:: runWithTimeout(task, timeoutSeconds, description)

   Runs `task` on a bounded background (daemon) thread, guarding against blocking I/O - typically remote N5/Zarr discovery, that can otherwise hang indefinitely on a stalled connection with no feedback to the user.

Unlike `openRemoteStream(String)` (a single bounded connection), this bounds the *entire* operation, however many network round-trips it internally makes.

On timeout, the background thread is best-effort interrupted via `ExecutorService.shutdownNow()`; if the underlying I/O call ignores interruption (common for plain socket reads), that thread may still leak until the stalled connection itself eventually times out or errors, but the calling thread is freed immediately to report the failure, rather than hanging alongside it.

   **Signature:** ``runWithTimeout(Callable, long, String) -> Object``

   **Parameters:**

   * **task** (``Any``): - the (typically network-bound) operation to run
   * **timeoutSeconds** (``int``)
   * **description** (``str``)

   **Returns:** (``Any``) the result of `task`

.. method:: startApp()

   Convenience method to start up SNT's GUI.

   **Signature:** ``startApp() -> SNT``

   **Returns:** ``SNT``

.. method:: stripExtension(filename)

   **Signature:** ``stripExtension(String) -> String``

   **Parameters:**

   * **filename** (``str``)

   **Returns:** ``str``

.. method:: submitBackground(task, threadName)

   Submits `task` to a bounded background (daemon) thread and returns immediately with a handle to it, instead of waiting for it like `runWithTimeout(java.util.concurrent.Callable<T>, long, java.lang.String)` does. Use this when a caller needs to wait on the same operation more than once - e.g. a retry-prompt loop with a growing timeout budget - without restarting the operation from scratch on every attempt, which is what looping calls to `runWithTimeout(java.util.concurrent.Callable<T>, long, java.lang.String)` would do: each call submits a fresh task to a fresh executor and best-effort cancels it as soon as that call's own wait times out.

   **Signature:** ``submitBackground(Callable, String) -> BackgroundTask``

   **Parameters:**

   * **task** (``Any``): - the (typically network-bound) operation to run
   * **threadName** (``str``)

   **Returns:** (``Any``) a handle bundling the running `Future` and the `ExecutorService` backing it; call `SNTUtils.BackgroundTask.cancel()` exactly once done with it, whether or not it ever completed

.. method:: warn(string)

   **Signature:** ``warn(String) -> void``

   **Parameters:**

   * **string** (``str``)

   **Returns:** ``None``


SWCPoint
--------

.. method:: chebyshevDxTo(point)

   **Signature:** ``chebyshevDxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevXYdxTo(point)

   **Signature:** ``chebyshevXYdxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevZdxTo(point)

   **Signature:** ``chebyshevZdxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: clone()

   **Signature:** ``clone() -> PointInImage``

   **Returns:** ``PointInImage``

.. method:: collectionAsReader(points)

   Converts a collection of SWC points into a Reader.

   **Signature:** ``collectionAsReader(Collection) -> StringReader``

   **Parameters:**

   * **points** (``List[Any]``): - the collection of SWC points to be converted into a space separated String. Points should be sorted by sample number to ensure valid connectivity.

   **Returns:** (``Any``) the Reader

.. method:: compareTo(o)

   **Signature:** ``compareTo(SWCPoint) -> int``

   **Parameters:**

   * **o** (``SWCPoint``)

   **Returns:** ``int``

.. method:: distanceSquaredTo(o)

   **Signature:** ``distanceSquaredTo(PointInImage) -> double``

   **Parameters:**

   * **o** (``PointInImage``)

   **Returns:** ``float``

.. method:: distanceTo(o)

   **Signature:** ``distanceTo(PointInImage) -> double``

   **Parameters:**

   * **o** (``PointInImage``)

   **Returns:** ``float``

.. method:: equals(o)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **o** (``Any``)

   **Returns:** ``bool``

.. method:: euclideanDxTo(point)

   **Signature:** ``euclideanDxTo(PointInImage) -> double``

   **Parameters:**

   * **point** (``PointInImage``)

   **Returns:** ``float``

.. method:: flush(points, pw)

   Prints a list of points as space-separated values.

   **Signature:** ``flush(Collection, PrintWriter) -> void``

   **Parameters:**

   * **points** (``List[Any]``): - the collections of SWC points to be printed.
   * **pw** (``Any``)

   **Returns:** ``None``

.. method:: previous()

   Returns the preceding node (if any)

   **Signature:** ``previous() -> SWCPoint``

   **Returns:** (``SWCPoint``) the previous node or null if set by `setPrevious(SWCPoint)` has not been called

.. method:: scale(xScale, yScale, zScale)

   **Signature:** ``scale(double, double, double) -> void``

   **Parameters:**

   * **xScale** (``float``)
   * **yScale** (``float``)
   * **zScale** (``float``)

   **Returns:** ``None``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``

.. method:: transform(transformer)

   **Signature:** ``transform(PathTransformer) -> PointInImage``

   **Parameters:**

   * **transformer** (``Any``)

   **Returns:** ``PointInImage``

.. method:: xSeparationFromPreviousPoint()

   Returns the X-distance from previous point.

   **Signature:** ``xSeparationFromPreviousPoint() -> double``

   **Returns:** (``float``) the X-distance from previous point or `Double.NaN` if no previousPoint exists.

.. method:: ySeparationFromPreviousPoint()

   Returns the Y-distance from previous point.

   **Signature:** ``ySeparationFromPreviousPoint() -> double``

   **Returns:** (``float``) the Y-distance from previous point or `Double.NaN` if no previousPoint exists.

.. method:: zSeparationFromPreviousPoint()

   Returns the Z-distance from previous point.

   **Signature:** ``zSeparationFromPreviousPoint() -> double``

   **Returns:** (``float``) the Z-distance from previous point or `Double.NaN` if no previousPoint exists.


SearchArtistFactory
-------------------

.. method:: create(search)

   **Signature:** ``create(BiSearch) -> BiSearchArtist``

   **Parameters:**

   * **search** (``BiSearch``)

   **Returns:** ``BiSearchArtist``


SearchImageStack
----------------

.. method:: iterator()

   **Signature:** ``iterator() -> Iterator``

   **Returns:** ``Any``

.. method:: keySet()

   **Signature:** ``keySet() -> Set``

   **Returns:** ``Set[Any]``

.. method:: newSlice(z)

   **Signature:** ``newSlice(int) -> SearchImage``

   **Parameters:**

   * **z** (``int``)

   **Returns:** ``Any``


SearchThread
------------

.. method:: createNewNode(x, y, z, g, h, predecessor, searchStatus)

   **Signature:** ``createNewNode(int, int, int, double, double, DefaultSearchNode, byte) -> DefaultSearchNode``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)
   * **g** (``float``)
   * **h** (``float``)
   * **predecessor** (``DefaultSearchNode``)
   * **searchStatus** (``int``)

   **Returns:** ``DefaultSearchNode``

.. method:: pointsConsideredInSearch()

   Description copied from class: `AbstractSearch`

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   Description copied from class: `AbstractSearch`

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(success)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **success** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


SearchThreadArtist
------------------

.. method:: anyNodeUnderThreshold(x, y, z, threshold)

   **Signature:** ``anyNodeUnderThreshold(int, int, int, double) -> DefaultSearchNode``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)
   * **threshold** (``float``)

   **Returns:** ``DefaultSearchNode``


SeedConfidence
--------------

.. method:: percentileClipNormalize(scores, clipPercent)

   **Signature:** ``percentileClipNormalize(double[], double) -> double[]``

   **Parameters:**

   * **scores** (``List[float]``)
   * **clipPercent** (``float``)

   **Returns:** ``List[float]``


SeedManager
-----------

.. method:: dispose()

   Unregisters the overlay listener and the table-model listener, and closes the detached-table dialog if it's open. Idempotent.

Must be called when this panel is removed from its parent: `overlay.addListener(overlayListener)` pins this panel to the overlay's lifetime, so skipping `dispose()` leaks the panel and its table model until SNT shuts down.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``


SeedOverlay
-----------

.. method:: add(seed)

   **Signature:** ``add(SeedPoint) -> void``

   **Parameters:**

   * **seed** (``SeedPoint``)

   **Returns:** ``None``

.. method:: clear()

   **Signature:** ``clear() -> void``

   **Returns:** ``None``

.. method:: countOutOfBounds(dims, spacing, offset)

   **Signature:** ``countOutOfBounds(long[], double[], double[]) -> int``

   **Parameters:**

   * **dims** (``List[int]``)
   * **spacing** (``List[float]``)
   * **offset** (``List[float]``)

   **Returns:** ``int``

.. method:: filtered()

   **Signature:** ``filtered() -> List``

   **Returns:** ``List[Any]``

.. method:: get(index)

   **Signature:** ``get(int) -> SeedPoint``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``SeedPoint``

.. method:: indexOf(seed)

   **Signature:** ``indexOf(SeedPoint) -> int``

   **Parameters:**

   * **seed** (``SeedPoint``)

   **Returns:** ``int``

.. method:: list()

   **Signature:** ``list() -> List``

   **Returns:** ``List[Any]``

.. method:: nearest(x, y, z, maxDistance)

   **Signature:** ``nearest(double, double, double, double) -> SeedPoint``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)
   * **maxDistance** (``float``)

   **Returns:** ``SeedPoint``

.. method:: parseCsv(file)

   **Signature:** ``parseCsv(File) -> CsvImportResult``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``Any``

.. method:: remove(seed)

   **Signature:** ``remove(SeedPoint) -> boolean``

   **Parameters:**

   * **seed** (``SeedPoint``)

   **Returns:** ``bool``

.. method:: replaceAll(replacement)

   **Signature:** ``replaceAll(Collection) -> void``

   **Parameters:**

   * **replacement** (``List[Any]``)

   **Returns:** ``None``

.. method:: replaceAllAt(replacements)

   **Signature:** ``replaceAllAt(Map) -> int``

   **Parameters:**

   * **replacements** (``Dict[str, Any]``)

   **Returns:** ``int``

.. method:: replaceAt(index, replacement)

   **Signature:** ``replaceAt(int, SeedPoint) -> boolean``

   **Parameters:**

   * **index** (``int``)
   * **replacement** (``SeedPoint``)

   **Returns:** ``bool``

.. method:: scaleConfidence(seeds, factor)

   **Signature:** ``scaleConfidence(Collection, double) -> int``

   **Parameters:**

   * **seeds** (``List[Any]``)
   * **factor** (``float``)

   **Returns:** ``int``

.. method:: scaleRadius(seeds, factor)

   **Signature:** ``scaleRadius(Collection, double) -> int``

   **Parameters:**

   * **seeds** (``List[Any]``)
   * **factor** (``float``)

   **Returns:** ``int``

.. method:: topKByConfidence(k)

   **Signature:** ``topKByConfidence(int) -> List``

   **Parameters:**

   * **k** (``int``)

   **Returns:** ``List[Any]``


SeedPoint
---------

.. method:: asArray()

   **Signature:** ``asArray() -> double[]``

   **Returns:** ``List[float]``

.. method:: distanceSqTo(px, py, pz)

   **Signature:** ``distanceSqTo(double, double, double) -> double``

   **Parameters:**

   * **px** (``float``)
   * **py** (``float``)
   * **pz** (``float``)

   **Returns:** ``float``

.. method:: distanceSquaredTo(other)

   **Signature:** ``distanceSquaredTo(SeedPoint) -> double``

   **Parameters:**

   * **other** (``SeedPoint``)

   **Returns:** ``float``

.. method:: toPointInImage()

   **Signature:** ``toPointInImage() -> PointInImage``

   **Returns:** ``PointInImage``

.. method:: toString()

   **Signature:** ``toString() -> String``

   **Returns:** ``str``


SeedRois
--------

.. method:: toRois(seeds, imp)

   **Signature:** ``toRois(Collection, ImagePlus) -> List``

   **Parameters:**

   * **seeds** (``List[Any]``)
   * **imp** (``Any``)

   **Returns:** ``List[Any]``

.. method:: toSeeds(rois, imp, confidence, type, source)

   **Signature:** ``toSeeds(Roi[], ImagePlus, double, String, String) -> List``

   **Parameters:**

   * **rois** (``List[Any]``)
   * **imp** (``Any``)
   * **confidence** (``float``)
   * **type** (``str``)
   * **source** (``str``)

   **Returns:** ``List[Any]``


ShollOverlay
------------

.. method:: assignProperty(property)

   **Signature:** ``assignProperty(String) -> void``

   **Parameters:**

   * **property** (``str``)

   **Returns:** ``None``

.. method:: remove(overlay, property)

   **Signature:** ``remove(Overlay, String) -> void``

   **Parameters:**

   * **overlay** (``Any``)
   * **property** (``str``)

   **Returns:** ``None``

.. method:: updateDisplay()

   **Signature:** ``updateDisplay() -> void``

   **Returns:** ``None``


ShollPlot
---------

.. method:: defaultXtitle(profile)

   **Signature:** ``defaultXtitle(Profile) -> String``

   **Parameters:**

   * **profile** (``Profile``)

   **Returns:** ``str``

.. method:: markPoint(point, color)

   **Signature:** ``markPoint(ShollPoint, Color) -> void``

   **Parameters:**

   * **point** (``Any``)
   * **color** (``Any``)

   **Returns:** ``None``

.. method:: rebuild()

   **Signature:** ``rebuild() -> void``

   **Returns:** ``None``

.. method:: save(file)

   **Signature:** ``save(File) -> boolean``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``bool``

.. method:: show(plots, title)

   **Signature:** ``show(List, String) -> void``

   **Parameters:**

   * **plots** (``List[Any]``)
   * **title** (``str``)

   **Returns:** ``None``


ShollStats
----------

.. method:: validFit()

   **Signature:** ``validFit() -> boolean``

   **Returns:** ``bool``


ShollTable
----------

.. method:: appendToLastRow(colHeader, value)

   **Signature:** ``appendToLastRow(String, Object) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **value** (``Any``)

   **Returns:** ``None``

.. method:: asDouble(cell)

   **Signature:** ``asDouble(Object) -> double``

   **Parameters:**

   * **cell** (``Any``)

   **Returns:** ``float``

.. method:: asInt(cell, fallback)

   **Signature:** ``asInt(Object, int) -> int``

   **Parameters:**

   * **cell** (``Any``)
   * **fallback** (``int``)

   **Returns:** ``int``

.. method:: asString(cell, fallback)

   **Signature:** ``asString(Object, String) -> String``

   **Parameters:**

   * **cell** (``Any``)
   * **fallback** (``str``)

   **Returns:** ``str``

.. method:: clear()

   **Signature:** ``clear() -> void``

   **Returns:** ``None``

.. method:: createOrUpdateDisplay()

   **Signature:** ``createOrUpdateDisplay() -> void``

   **Returns:** ``None``

.. method:: fillEmptyCells(value)

   **Signature:** ``fillEmptyCells(Object) -> void``

   **Parameters:**

   * **value** (``Any``)

   **Returns:** ``None``

.. method:: findColumnIndex(columnHeader)

   **Signature:** ``findColumnIndex(String) -> int``

   **Parameters:**

   * **columnHeader** (``str``)

   **Returns:** ``int``

.. method:: fromGenericTable(source)

   **Signature:** ``fromGenericTable(GenericTable) -> SNTTable``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``SNTTable``

.. method:: geColumnStats(colHeader, startRowIndex, endRowIndex)

   **Signature:** ``geColumnStats(String, int, int) -> SummaryStatistics``

   **Parameters:**

   * **colHeader** (``str``)
   * **startRowIndex** (``int``)
   * **endRowIndex** (``int``)

   **Returns:** ``Any``

.. method:: geRowStats(rowHeader, startColumnIndex, endColumnIndex)

   **Signature:** ``geRowStats(String, int, int) -> SummaryStatistics``

   **Parameters:**

   * **rowHeader** (``str``)
   * **startColumnIndex** (``int``)
   * **endColumnIndex** (``int``)

   **Returns:** ``Any``

.. method:: insertRow(header)

   **Signature:** ``insertRow(String) -> int``

   **Parameters:**

   * **header** (``str``)

   **Returns:** ``int``

.. method:: replace(columnHeadersPattern, originalValue, replacementValue)

   **Signature:** ``replace(String, double, double) -> void``

   **Parameters:**

   * **columnHeadersPattern** (``str``)
   * **originalValue** (``float``)
   * **replacementValue** (``float``)

   **Returns:** ``None``

.. method:: save(outputFile)

   **Signature:** ``save(File) -> void``

   **Parameters:**

   * **outputFile** (``str``)

   **Returns:** ``None``

.. method:: set(colHeader, rowHeader, value)

   **Signature:** ``set(String, String, Object) -> void``

   **Parameters:**

   * **colHeader** (``str``)
   * **rowHeader** (``str``)
   * **value** (``Any``)

   **Returns:** ``None``

.. method:: show()

   **Signature:** ``show() -> void``

   **Returns:** ``None``

.. method:: summarize()

   **Signature:** ``summarize() -> void``

   **Returns:** ``None``

.. method:: toString(table)

   **Signature:** ``toString(GenericTable) -> String``

   **Parameters:**

   * **table** (``Any``)

   **Returns:** ``str``

.. method:: updateDisplay()

   **Signature:** ``updateDisplay() -> void``

   **Returns:** ``None``


SomaUtils
---------

.. method:: detectAllSomas(source)

   **Signature:** ``detectAllSomas(ImgPlus) -> List``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``List[Any]``

.. method:: detectSoma(source)

   **Signature:** ``detectSoma(ImgPlus) -> SomaResult``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``Any``

.. method:: detectSomaAt(source, seedX, seedY, threshold)

   **Signature:** ``detectSomaAt(RandomAccessibleInterval, long, long, double) -> SomaResult``

   **Parameters:**

   * **source** (``Any``)
   * **seedX** (``int``)
   * **seedY** (``int``)
   * **threshold** (``float``)

   **Returns:** ``Any``

.. method:: detectSomasAt(imp, rois)

   **Signature:** ``detectSomasAt(ImagePlus, Collection) -> List``

   **Parameters:**

   * **imp** (``Any``)
   * **rois** (``List[Any]``)

   **Returns:** ``List[Any]``

.. method:: estimateMinSomaDistance(somas)

   **Signature:** ``estimateMinSomaDistance(List) -> double``

   **Parameters:**

   * **somas** (``List[Any]``)

   **Returns:** ``float``

.. method:: extractContour(mask)

   **Signature:** ``extractContour(Img) -> Polygon``

   **Parameters:**

   * **mask** (``Any``)

   **Returns:** ``Any``

.. method:: filterSomasByIntensity(somas, source)

   **Signature:** ``filterSomasByIntensity(List, RandomAccessibleInterval) -> List``

   **Parameters:**

   * **somas** (``List[Any]``)
   * **source** (``Any``)

   **Returns:** ``List[Any]``

.. method:: filterSomasByThickness(somas, source)

   **Signature:** ``filterSomasByThickness(List, RandomAccessibleInterval) -> List``

   **Parameters:**

   * **somas** (``List[Any]``)
   * **source** (``Any``)

   **Returns:** ``List[Any]``

.. method:: floodFillSoma(source, seedX, seedY, threshold)

   **Signature:** ``floodFillSoma(RandomAccessibleInterval, long, long, double) -> Img``

   **Parameters:**

   * **source** (``Any``)
   * **seedX** (``int``)
   * **seedY** (``int``)
   * **threshold** (``float``)

   **Returns:** ``Any``

.. method:: selectTopSomasByThickness(somas, source, n)

   **Signature:** ``selectTopSomasByThickness(List, RandomAccessibleInterval, int) -> List``

   **Parameters:**

   * **somas** (``List[Any]``)
   * **source** (``Any``)
   * **n** (``int``)

   **Returns:** ``List[Any]``


SparseGWDTTracer
----------------

.. method:: create(source)

   **Signature:** ``create(ImagePlus) -> SparseGWDTTracer``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``SparseGWDTTracer``

.. method:: findRoot(source, spacing)

   **Signature:** ``findRoot(RandomAccessibleInterval, double[]) -> long[]``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[int]``

.. method:: findRootPhysical(source, spacing)

   **Signature:** ``findRootPhysical(RandomAccessibleInterval, double[]) -> double[]``

   **Parameters:**

   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: findThickestPoint(source, threshold, spacing)

   **Signature:** ``findThickestPoint(RandomAccessibleInterval, double, double[]) -> long[]``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[int]``

.. method:: findThickestPointPhysical(source, threshold, spacing)

   **Signature:** ``findThickestPointPhysical(RandomAccessibleInterval, double, double[]) -> double[]``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: honoredSeedRoles()

   **Signature:** ``honoredSeedRoles() -> EnumSet``

   **Returns:** ``Any``

.. method:: iterateNeighbors(delta, dim, nDims, action)

   **Signature:** ``iterateNeighbors(int[], int, int, Runnable) -> void``

   **Parameters:**

   * **delta** (``List[int]``)
   * **dim** (``int``)
   * **nDims** (``int``)
   * **action** (``Any``)

   **Returns:** ``None``

.. method:: posToIndex(pos, dims)

   **Signature:** ``posToIndex(long[], long[]) -> long``

   **Parameters:**

   * **pos** (``List[int]``)
   * **dims** (``List[int]``)

   **Returns:** ``int``

.. method:: trace()

   **Signature:** ``trace() -> Tree``

   **Returns:** ``Tree``

.. method:: traceMultiSoma(somas)

   **Signature:** ``traceMultiSoma(List) -> List``

   **Parameters:**

   * **somas** (``List[Any]``)

   **Returns:** ``List[Any]``

.. method:: traceToGraph()

   **Signature:** ``traceToGraph() -> DirectedWeightedGraph``

   **Returns:** ``DirectedWeightedGraph``

.. method:: traceTrees()

   **Signature:** ``traceTrees() -> List``

   **Returns:** ``List[Any]``


SparseStorageBackend
--------------------

.. method:: buildGraph(dims, spacing, threshold)

   **Signature:** ``buildGraph(long[], double[], double) -> DirectedWeightedGraph``

   **Parameters:**

   * **dims** (``List[int]``)
   * **spacing** (``List[float]``)
   * **threshold** (``float``)

   **Returns:** ``DirectedWeightedGraph``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: estimateMemoryUsage()

   **Signature:** ``estimateMemoryUsage() -> long``

   **Returns:** ``int``

.. method:: initializeFastMarching(dims, seedIndex)

   **Signature:** ``initializeFastMarching(long[], long) -> void``

   **Parameters:**

   * **dims** (``List[int]``)
   * **seedIndex** (``int``)

   **Returns:** ``None``

.. method:: reinitializeFastMarching(dims, seedIndex, excludedIndices)

   **Signature:** ``reinitializeFastMarching(long[], long, Set) -> void``

   **Parameters:**

   * **dims** (``List[int]``)
   * **seedIndex** (``int``)
   * **excludedIndices** (``Set[Any]``)

   **Returns:** ``None``


SpectralSimilarity
------------------

.. method:: accept(output)

   **Signature:** ``accept(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **output** (``Any``)

   **Returns:** ``None``

.. method:: channelSum(vec)

   Sums all elements of a vector. Typically used to compute the total intensity across channels of a color vector.

   **Signature:** ``channelSum(double[]) -> double``

   **Parameters:**

   * **vec** (``List[float]``): - the vector

   **Returns:** (``float``) the sum of all elements

.. method:: nodeToPixelCoords(node, xSpacing, ySpacing, zSpacing)

   As `nodeToPixelCoords(sc.fiji.snt.util.PointInImage, double, double, double)`, but also adding a pixel-space offset after scaling - typically `SNT#getActiveCanvasPixelOffset()`, needed whenever the target image is the crop-local grid of a materialized crop, or the raw streamed source's own voxel grid under a non-zero `SNT#getWorldOriginOffset()` (see `SNT#createSearch(double, double, double, double, double, double)` for the same conversion, applied to A* search endpoints instead of Path nodes).

   **Signature:** ``nodeToPixelCoords(PointInImage, double, double, double) -> int[]``

   **Parameters:**

   * **node** (``PointInImage``): - the node in calibrated coordinates
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)

   **Returns:** (``List[int]``) pixel coordinates as `[x, y, z]`

.. method:: normalizeVector(vec)

   Normalizes a vector to unit length in place. If the vector has zero magnitude, it is left unchanged.

   **Signature:** ``normalizeVector(double[]) -> void``

   **Parameters:**

   * **vec** (``List[float]``): - the vector to normalize

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


StrahlerAnalyzer
----------------

.. method:: classify(graph, reverseOrder)

   **Signature:** ``classify(DirectedWeightedGraph, boolean) -> void``

   **Parameters:**

   * **graph** (``DirectedWeightedGraph``)
   * **reverseOrder** (``bool``)

   **Returns:** ``None``

.. method:: dispose()

   Clears internal caches and mappings to free memory.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``


SupplierUtil
------------

.. method:: createSupplier(clazz, searchNodeClass, width, height)

   **Signature:** ``createSupplier(SearchImageType, Class, int, int) -> Supplier``

   **Parameters:**

   * **clazz** (``Any``)
   * **searchNodeClass** (``type``)
   * **width** (``int``)
   * **height** (``int``)

   **Returns:** ``Any``


TracerCanvas
------------

.. method:: mouseDragged(e)

   **Signature:** ``mouseDragged(MouseEvent) -> void``

   **Parameters:**

   * **e** (``Any``)

   **Returns:** ``None``

.. method:: myOffScreenX(sx)

   **Signature:** ``myOffScreenX(int) -> int``

   **Parameters:**

   * **sx** (``int``)

   **Returns:** ``int``

.. method:: myOffScreenXD(sx)

   **Signature:** ``myOffScreenXD(int) -> double``

   **Parameters:**

   * **sx** (``int``)

   **Returns:** ``float``

.. method:: myOffScreenY(sy)

   **Signature:** ``myOffScreenY(int) -> int``

   **Parameters:**

   * **sy** (``int``)

   **Returns:** ``int``

.. method:: myOffScreenYD(sy)

   **Signature:** ``myOffScreenYD(int) -> double``

   **Parameters:**

   * **sy** (``int``)

   **Returns:** ``float``

.. method:: myScreenX(ox)

   **Signature:** ``myScreenX(int) -> int``

   **Parameters:**

   * **ox** (``int``)

   **Returns:** ``int``

.. method:: myScreenXD(ox)

   **Signature:** ``myScreenXD(double) -> int``

   **Parameters:**

   * **ox** (``float``)

   **Returns:** ``int``

.. method:: myScreenXDprecise(ox)

   **Signature:** ``myScreenXDprecise(double) -> double``

   **Parameters:**

   * **ox** (``float``)

   **Returns:** ``float``

.. method:: myScreenY(oy)

   **Signature:** ``myScreenY(int) -> int``

   **Parameters:**

   * **oy** (``int``)

   **Returns:** ``int``

.. method:: myScreenYD(oy)

   **Signature:** ``myScreenYD(double) -> int``

   **Parameters:**

   * **oy** (``float``)

   **Returns:** ``int``

.. method:: myScreenYDprecise(oy)

   **Signature:** ``myScreenYDprecise(double) -> double``

   **Parameters:**

   * **oy** (``float``)

   **Returns:** ``float``

.. method:: paint(g)

   **Signature:** ``paint(Graphics) -> void``

   **Parameters:**

   * **g** (``Any``)

   **Returns:** ``None``

.. method:: restoreDefaultCursor()

   **Signature:** ``restoreDefaultCursor() -> void``

   **Returns:** ``None``

.. method:: scrollTo(newOffscreenX, newOffscreenY)

   **Signature:** ``scrollTo(int, int) -> void``

   **Parameters:**

   * **newOffscreenX** (``int``)
   * **newOffscreenY** (``int``)

   **Returns:** ``None``

.. method:: updateCursor(x, y, z)

   **Signature:** ``updateCursor(double, double, double) -> void``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** ``None``

.. method:: updatePosition(x, y, z)

   **Signature:** ``updatePosition(double, double, double) -> void``

   **Parameters:**

   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** ``None``

.. method:: zoomIn(sx, sy)

   **Signature:** ``zoomIn(int, int) -> void``

   **Parameters:**

   * **sx** (``int``)
   * **sy** (``int``)

   **Returns:** ``None``

.. method:: zoomOut(sx, sy)

   **Signature:** ``zoomOut(int, int) -> void``

   **Parameters:**

   * **sx** (``int``)
   * **sy** (``int``)

   **Returns:** ``None``


TracerThread
------------

.. method:: createNewNode(x, y, z, g, h, predecessor, searchStatus)

   **Signature:** ``createNewNode(int, int, int, double, double, DefaultSearchNode, byte) -> DefaultSearchNode``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)
   * **z** (``int``)
   * **g** (``float``)
   * **h** (``float``)
   * **predecessor** (``DefaultSearchNode``)
   * **searchStatus** (``int``)

   **Returns:** ``DefaultSearchNode``

.. method:: pointsConsideredInSearch()

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(success)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **success** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


Tree
----

.. method:: add(p)

   Adds a new Path to this Tree.

   **Signature:** ``add(Path) -> boolean``

   **Parameters:**

   * **p** (``Path``): - the Path to be added

   **Returns:** (``bool``) true, if Path successful added

.. method:: applyCanvasOffset(xOffset, yOffset, zOffset)

   Specifies the offset to be used when rendering this Tree in a `TracerCanvas`. Path coordinates remain unaltered.

   **Signature:** ``applyCanvasOffset(double, double, double) -> void``

   **Parameters:**

   * **xOffset** (``float``): - the x offset (in pixels)
   * **yOffset** (``float``)
   * **zOffset** (``float``)

   **Returns:** ``None``

.. method:: applyProperties(tree)

   Applies properties from another Tree to this Tree.

   **Signature:** ``applyProperties(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the Tree whose properties should be copied

   **Returns:** ``None``

.. method:: applyZCorrection(correctionFactor)

   Applies a Z-shrinkage correction to all nodes in this tree. This is typically used to compensate for tissue compression along the Z-axis during histological processing or mounting (e.g., paraffin embedding, cryosectioning). The correction factor is the ratio of the actual (cut) thickness to the measured (mounted) thickness.

   **Signature:** ``applyZCorrection(double) -> void``

   **Parameters:**

   * **correctionFactor** (``float``): - the Z scaling factor (e.g., 2.0 to double all Z coordinates). Must be positive and non-zero.

   **Returns:** ``None``

.. method:: assignImage(dataset)

   Assigns spatial calibration from an ImgPlus to this Tree.

   **Signature:** ``assignImage(Dataset) -> void``

   **Parameters:**

   * **dataset** (``Any``): - the ImgPlus providing the spatial calibration. Null allowed.

   **Returns:** ``None``

.. method:: assignValue(value)

   Assigns a numeric property to this Tree.

   **Signature:** ``assignValue(double) -> void``

   **Parameters:**

   * **value** (``float``): - the value to be assigned to this Tree.

   **Returns:** ``None``

.. method:: clone()

   Creates a deep copy of this Tree.

This method creates a complete copy of the tree including all paths and their relationships. Each path is cloned individually, and then the parent-child relationships are reconstructed in the cloned tree. This ensures that the cloned tree maintains the same structure as the original while being completely independent.

   **Signature:** ``clone() -> Tree``

   **Returns:** (``Tree``) a new Tree that is a deep copy of this tree

.. method:: downsample(internodeSpacing)

   Downsamples the tree, i.e., reduces the density of its nodes by increasing internode spacing.

Note that 1) upsampling is not supported (cf. `Path.upsample(double)`), and 2) the position of nodes at branch points and tips remains unaltered during downsampling, as per `Path.downsample(double)`.

   **Signature:** ``downsample(double) -> void``

   **Parameters:**

   * **internodeSpacing** (``float``): - the maximum allowed distance between path nodes.

   **Returns:** ``None``

.. method:: fitRadii(imp)

   Fits radii to all paths in this Tree by fitting circular cross-sections to the image signal. Paths are fitted in parallel; results are applied sequentially. This is the scripting equivalent of the UI's "Fit Paths" action. Node positions are not modified; only radii and tangent vectors are computed.

   **Signature:** ``fitRadii(ImagePlus) -> int``

   **Parameters:**

   * **imp** (``Any``): - the image containing the signal to fit against

   **Returns:** (``int``) the number of paths successfully fitted

.. method:: get(index)

   Returns the Path at the specified position.

   **Signature:** ``get(int) -> Path``

   **Parameters:**

   * **index** (``int``): - index of the element to return

   **Returns:** (``Path``) the element at the specified position

.. method:: indexOf(path)

   Returns the index of the specified Path in this Tree.

   **Signature:** ``indexOf(Path) -> int``

   **Parameters:**

   * **path** (``Path``): - the Path to be searched for

   **Returns:** (``int``) the path index, or -1 if it was not found

.. method:: is3D()

   Assesses whether this Tree has depth.

   **Signature:** ``is3D() -> boolean``

   **Returns:** (``bool``) true, if is 3D

.. method:: list()

   Gets all the paths from this tree.

   **Signature:** ``list() -> List``

   **Returns:** (``List[Any]``) the paths forming this tree

.. method:: listFromDir(dir)

   Retrieves a list of `Tree`s from reconstruction files stored in a common directory matching the specified criteria.

   **Signature:** ``listFromDir(String) -> List``

   **Parameters:**

   * **dir** (``str``): - the directory containing the reconstruction files (.(e)swc, .traces, .json extension)

   **Returns:** (``List[Any]``) the list of imported `Tree`s. An empty list is retrieved if `dir` is not a valid, readable directory.

.. method:: merge(tree)

   Appends all paths of a specified `Tree` to this one.

   **Signature:** ``merge(Tree) -> boolean``

   **Parameters:**

   * **tree** (``Tree``): - the Tree to be merged

   **Returns:** (``bool``) true if this Tree changed as a result of the merge

.. method:: rebuildGraph()

   Re-assembles the DirectedGraph object returned by `getGraph()` ensuring that no untracked changes exist. Usually, calling this method is not necessary since most changes to this Tree percolate to its graph representation.

   **Signature:** ``rebuildGraph() -> void``

   **Returns:** ``None``

.. method:: remove(p)

   Removes a path from this tree.

   **Signature:** ``remove(Path) -> boolean``

   **Parameters:**

   * **p** (``Path``): - the Path to be removed

   **Returns:** (``bool``) true if this tree contained p

.. method:: replaceAll(paths)

   Replaces all Paths in this Tree.

   **Signature:** ``replaceAll(List) -> void``

   **Parameters:**

   * **paths** (``List[Any]``): - the replacing Paths

   **Returns:** ``None``

.. method:: rotate(axis, angle)

   Rotates the tree.

   **Signature:** ``rotate(int, double) -> void``

   **Parameters:**

   * **axis** (``int``): - the rotation axis. Either X_AXIS, Y_AXIS, or Z_AXIS.
   * **angle** (``float``)

   **Returns:** ``None``

.. method:: save(filePath)

   Saves this Tree to a .TRACES (XML, compressed) file.

   **Signature:** ``save(String) -> boolean``

   **Parameters:**

   * **filePath** (``str``): - the absolute path of the output file.

   **Returns:** (``bool``) true, if file successfully saved.

.. method:: scale(xScale, yScale, zScale)

   Scales the tree by the specified factors.

   **Signature:** ``scale(double, double, double) -> void``

   **Parameters:**

   * **xScale** (``float``): - the scaling factor for x coordinates
   * **yScale** (``float``)
   * **zScale** (``float``)

   **Returns:** ``None``

.. method:: show()

   Displays this Tree in an appropriate viewer (3D if the tree has depth, 2D otherwise).

   **Signature:** ``show() -> void``

   **Returns:** ``None``

.. method:: show2D()

   Displays this Tree in Viewer2D.

   **Signature:** ``show2D() -> Viewer2D``

   **Returns:** (``Viewer2D``) the `Viewer2D` instance displaying this Tree

.. method:: show3D()

   Displays this Tree in Viewer3D.

   **Signature:** ``show3D() -> Viewer3D``

   **Returns:** (``Viewer3D``) the `Viewer3D` instance displaying this Tree

.. method:: skeletonize(destinationImp, value)

   Skeletonizes (rasterizes) this tree on the specified image using Bresenham’s Algorithm (3D).

   **Signature:** ``skeletonize(ImagePlus, int) -> void``

   **Parameters:**

   * **destinationImp** (``Any``): - the destination image (16-bit). It is assumed that the image dimensions are suitable, and that the spatial calibration of the image is compatible with that of this tree. Out of bound locations will be silently ignored.
   * **value** (``int``)

   **Returns:** ``None``

.. method:: subTree(swcTypes)

   Extracts the subset of paths matching the specified criteria.

   **Signature:** ``subTree(String[]) -> Tree``

   **Parameters:**

   * **swcTypes** (``List[str]``): - SWC type(s) (e.g., Path.SWC_AXON, Path.SWC_DENDRITE, etc.) allowed in the subtree

   **Returns:** (``Tree``) the subset of paths matching the filtering criteria, or an empty Tree if no hits were retrieved

.. method:: swapAxes(axis1, axis2)

   Swaps the coordinates of two axes in this Tree.

   **Signature:** ``swapAxes(int, int) -> void``

   **Parameters:**

   * **axis1** (``int``): - the first axis. Either X_AXIS, Y_AXIS, or Z_AXIS
   * **axis2** (``int``)

   **Returns:** ``None``

.. method:: transform(transformOptions)

   Transforms a collection of trees using standardized flags.

   **Signature:** ``transform(String) -> void``

   **Parameters:**

   * **transformOptions** (``str``): - the collection of Trees to be transformed

   **Returns:** (``None``) the collection with transformed trees, or the input collection if transformOptions were invalid

.. method:: transformedCopy(transformOptions)

   Retrieves a transformed duplicate of this tree.

   **Signature:** ``transformedCopy(String) -> Tree``

   **Parameters:**

   * **transformOptions** (``str``): - see transform(String)

   **Returns:** (``Tree``) the duplicated copy of this Tree transformed according to transformOptions

.. method:: translate(xOffset, yOffset, zOffset)

   Translates the tree by the specified offset.

   **Signature:** ``translate(double, double, double) -> void``

   **Parameters:**

   * **xOffset** (``float``): - the x offset
   * **yOffset** (``float``)
   * **zOffset** (``float``)

   **Returns:** ``None``

.. method:: upsample(internodeSpacing)

   Downsamples the tree, i.e., increases the density of its nodes by decreasing internode spacing.

The upscaling will include all the original nodes plus additional interpolated nodes placed at regular intervals between them, approximately equal to the specified distance. The original nodes are preserved in the upsampled tree. If the distance between two adjacent original nodes is less than the specified pacing, no additional nodes are added between them.

   **Signature:** ``upsample(double) -> void``

   **Parameters:**

   * **internodeSpacing** (``float``): - the desired distance between adjacent nodes in the upsampled path

   **Returns:** ``None``

.. method:: validSoma()

   Checks whether this Tree has a valid soma annotation, i.e., a single primary path tagged with `Path.SWC_SOMA`.

   **Signature:** ``validSoma() -> boolean``

   **Returns:** (``bool``) Returns true, if soma annotation is valid.


TreeColorMapper
---------------

.. method:: map(measurement, colorTable)

   Colorizes a tree after the specified measurement. Mapping bounds are automatically determined.

   **Signature:** ``map(String, ColorTable) -> void``

   **Parameters:**

   * **measurement** (``str``): - the tree to be mapped
   * **colorTable** (``Any``)

   **Returns:** ``None``

.. method:: mapTrees(trees, lut)

   Colorizes a list of trees, with each tree being assigned a LUT index.

   **Signature:** ``mapTrees(List, String) -> void``

   **Parameters:**

   * **trees** (``List[Any]``): - the list of trees to be colorized
   * **lut** (``str``)

   **Returns:** ``None``

.. method:: unMap(paths)

   **Signature:** ``unMap(Collection) -> void``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``None``


TreeParser
----------

.. method:: parse()

   **Signature:** ``parse() -> void``

   **Returns:** ``None``

.. method:: successful()

   **Signature:** ``successful() -> boolean``

   **Returns:** ``bool``

.. method:: terminate()

   **Signature:** ``terminate() -> void``

   **Returns:** ``None``


TreeStatistics
--------------

.. method:: dispose()

   Clears internal caches and mappings to free memory.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: fromCollection(trees, metric)

   Creates a TreeStatistics instance from a group of Trees and a specific metric for convenient retrieval of histograms

   **Signature:** ``fromCollection(Collection, String) -> TreeStatistics``

   **Parameters:**

   * **trees** (``List[Any]``): - the collection of trees
   * **metric** (``str``)

   **Returns:** (``TreeStatistics``) the TreeStatistics instance

.. method:: resetRestrictions()

   Removes any filtering restrictions that may have been set. Once called, subsequent analysis will use all paths initially parsed by the constructor. Does nothing if no paths are currently being excluded from the analysis.

   **Signature:** ``resetRestrictions() -> void``

   **Returns:** ``None``

.. method:: restrictToSWCType(types)

   Restricts analysis to Paths sharing the specified SWC flag(s).

   **Signature:** ``restrictToSWCType(int[]) -> void``

   **Parameters:**

   * **types** (``List[int]``): - the allowed SWC flags (e.g., Path.SWC_AXON, etc.)

   **Returns:** ``None``

.. method:: run()

   Generates detailed summaries in which measurements are grouped by SWC-type flags

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: summarize(groupByType)

   Outputs a summary of the current analysis to the measurements table.

   **Signature:** ``summarize(boolean) -> void``

   **Parameters:**

   * **groupByType** (``bool``): - the String to be used as label for the summary

   **Returns:** ``None``

.. method:: updateAndDisplayTable()

   Updates and displays the measurements table. If `Context` has not been set (running headless!?), table is printed to Console.

   **Signature:** ``updateAndDisplayTable() -> void``

   **Returns:** ``None``


TreeToRaster
------------

.. method:: rasterize()

   Rasterizes the tree into a 32-bit (float) image using partial-volume supersampling. Voxel values represent the fraction of the supersampled sub-voxels that fall inside the neuron structure (0.0 = background, 1.0 = fully inside), unless noise has been enabled via `setPoissonNoise(double, double)`, in which case values represent simulated photon counts.

   **Signature:** ``rasterize() -> ImagePlus``

   **Returns:** (``Any``) the rasterized `ImagePlus`

.. method:: rasterizeNodeValueLabels()

   Rasterizes the tree into a 16-bit label image where each voxel is assigned the *node value* of the nearest path node (as stored via `Path.setNodeValue(double, int)`). This enables per-node labeling, e.g., from delineation assignments, atlas annotations, or other node-level classifications.

Node values are expected to be negative integers (as used by `DelineationsManager`); they are negated to produce positive labels in the output image. Nodes with `NaN` or non-negative values are treated as background (0).

Each frustum (segment between consecutive nodes) inherits the label of its start node. At intersection sites, the frustum with the largest local radius wins (thickest-wins), consistent with `rasterizePathLabels()`.

**Note:** The output is 16-bit unsigned (`short`), so label values above 65535 will overflow. In practice this is not a concern when the source is a label/segmentation image with a bounded class count, but callers should be aware of this limit.

   **Signature:** ``rasterizeNodeValueLabels() -> ImagePlus``

   **Returns:** (``Any``) a 16-bit `ImagePlus` of node-value labels


TreeUtils
---------

.. method:: collectChildren(path, children)

   Collects direct children of a path into the provided collection.

   **Signature:** ``collectChildren(Path, Collection) -> void``

   **Parameters:**

   * **path** (``Path``)
   * **children** (``List[Any]``)

   **Returns:** ``None``

.. method:: collectDescendants(path, descendants)

   Collects all descendants (children, grandchildren, etc.) of a path into the provided collection.

   **Signature:** ``collectDescendants(Path, Collection) -> void``

   **Parameters:**

   * **path** (``Path``)
   * **descendants** (``List[Any]``)

   **Returns:** ``None``

.. method:: countDescendants(path)

   Counts all descendants (children, grandchildren, etc.) of a path.

   **Signature:** ``countDescendants(Path) -> int``

   **Parameters:**

   * **path** (``Path``)

   **Returns:** ``int``

.. method:: findClosestEndpoints(p1, p2)

   Finds the closest endpoint pairing between two paths. Checks all four combinations: start-start, start-end, end-start, end-end.

   **Signature:** ``findClosestEndpoints(Path, Path) -> EndpointMatch``

   **Parameters:**

   * **p1** (``Path``): - first path
   * **p2** (``Path``)

   **Returns:** (``Any``) EndpointMatch describing the closest pairing, or null if either path is empty

.. method:: merge(trees)

   Combines all trees into a single Tree container.

Note that **no** effort is made to make the merge structure topographylically valid. This is simply a convenience method to collect paths in a single contained for operations that do not require an accurate graph structure, e.g., Sholl Analysis.

   **Signature:** ``merge(Collection) -> Tree``

   **Parameters:**

   * **trees** (``List[Any]``): -

   **Returns:** (``Tree``) the merged tree

.. method:: orderByEndpointProximity(paths)

   Orders a collection of paths to form a spatially continuous chain based on endpoint proximity. The algorithm greedily connects paths by finding the closest endpoint pairs.

This method does NOT modify the paths (no reversal). Use `orientPathsForMerging(List)` on the result to fix orientations.

   **Signature:** ``orderByEndpointProximity(Collection) -> List``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to order (at least 2)

   **Returns:** (``List[Any]``) ordered list forming a chain, or empty list if paths cannot form a continuous chain

.. method:: rasterize(tree)

   Rasterizes a tree into a 3D image with the specified voxel sizes.

   **Signature:** ``rasterize(Tree) -> ImagePlus``

   **Parameters:**

   * **tree** (``Tree``): - the Tree to rasterize

   **Returns:** (``Any``) the rasterized 32-bit image (voxel values in [0, 1])

.. method:: restoreNodeValues(snapshot)

   Restores per-path node values captured by `snapshotNodeValues(Tree)`.

   **Signature:** ``restoreNodeValues(Map) -> void``

   **Parameters:**

   * **snapshot** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: snapshotNodeValues(tree)

   Snapshots the per-node values (`node.v`) for each path in a Tree so they can be restored later.

   **Signature:** ``snapshotNodeValues(Tree) -> Map``

   **Parameters:**

   * **tree** (``Tree``)

   **Returns:** (``Dict[str, Any]``) map keyed by path; entries are `null` when the path had no assigned values

.. method:: suggestRootLocation(paths, referencePoint)

   Analyzes paths and suggests auto-orientation based on:

#. If a reference point (e.g., ROI centroid) is provided, orient toward it

#. For 3+ paths: find the tighter endpoint cluster as the root

#. For 2 paths: find the closest endpoint pair as the root

   **Signature:** ``suggestRootLocation(Collection, PointInImage) -> PointInImage``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to analyze
   * **referencePoint** (``PointInImage``)

   **Returns:** (``PointInImage``) the suggested root location, or null if it cannot be determined

.. method:: syncCanvasOffset(child, parent)

   Applies the parent's canvas offset to the child path and all its descendants. This ensures paths are in the same coordinate space after connection. Node coordinates are transformed to maintain the same visual position.

   **Signature:** ``syncCanvasOffset(Path, Path) -> void``

   **Parameters:**

   * **child** (``Path``)
   * **parent** (``Path``)

   **Returns:** ``None``


Tubeness
--------

.. method:: accept(output)

   **Signature:** ``accept(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **output** (``Any``)

   **Returns:** ``None``

.. method:: apply(img, scale)

   Apply single-scale tubeness filter to an ImgPlus.

   **Signature:** ``apply(ImgPlus, double) -> ImgPlus``

   **Parameters:**

   * **img** (``Any``): - input image (2D or 3D) with calibrated axes
   * **scale** (``float``)

   **Returns:** (``Any``) filtered ImgPlus with same axes as input

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


TuftDetector
------------

.. method:: detect(tree, types)

   **Signature:** ``detect(Tree, List) -> List``

   **Parameters:**

   * **tree** (``Tree``)
   * **types** (``List[Any]``)

   **Returns:** ``List[Any]``


VFBUtils
--------

.. method:: brainBarycentre(templateBrain)

   Returns the spatial centroid of an adult Drosophila template brain.

   **Signature:** ``brainBarycentre(String) -> SNTPoint``

   **Parameters:**

   * **templateBrain** (``str``): - the template brain to be loaded (case-insensitive). Either "JFRC2" (AKA JFRC2010, VFB), "JFRC3" (AKA JFRC2013), "JFRC2018" or "FCWB" (FlyCircuit Whole Brain Template)

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of brain mesh.


Viewer2D
--------

.. method:: add(object)

   Appends a tree to the viewer rendered after the specified measurement.

   **Signature:** ``add(Object) -> void``

   **Parameters:**

   * **object** (``Any``): - the tree to be plotted

   **Returns:** ``None``

.. method:: map(measurement, colorTable)

   **Signature:** ``map(String, ColorTable) -> void``

   **Parameters:**

   * **measurement** (``str``)
   * **colorTable** (``Any``)

   **Returns:** ``None``

.. method:: mapTrees(trees, lut)

   **Signature:** ``mapTrees(List, String) -> void``

   **Parameters:**

   * **trees** (``List[Any]``)
   * **lut** (``str``)

   **Returns:** ``None``

.. method:: show()

   Displays the current plot on a dedicated frame *

   **Signature:** ``show() -> void``

   **Returns:** ``None``

.. method:: unMap(paths)

   **Signature:** ``unMap(Collection) -> void``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: add(object)

   Script friendly method to add a supported object (`Tree`, `OBJMesh`, AbstractDrawable, etc.) to this viewer. Note that collections of supported objects are also supported, which is an effective way of adding multiple items since the scene is only rebuilt once all items have been added.

   **Signature:** ``add(Object) -> void``

   **Parameters:**

   * **object** (``Any``): - the object to be added. No exception is triggered if null

   **Returns:** ``None``

.. method:: annotateLine(points, label)

   Adds a line annotation to this viewer.

   **Signature:** ``annotateLine(Collection, String) -> Annotation3D``

   **Parameters:**

   * **points** (``List[Any]``): - the collection of points in the line annotation (at least 2 elements required). Start and end of line are highlighted if 2 points are specified.
   * **label** (``str``)

   **Returns:** (``Annotation3D``) the `Annotation3D` or null if collection contains less than 2 elements

.. method:: annotateMidPlane(boundingBox, axis, label)

   **Signature:** ``annotateMidPlane(BoundingBox, int, String) -> Annotation3D``

   **Parameters:**

   * **boundingBox** (``BoundingBox``)
   * **axis** (``int``)
   * **label** (``str``)

   **Returns:** ``Annotation3D``

.. method:: annotatePlane(origin, originOpposite, label)

   **Signature:** ``annotatePlane(SNTPoint, SNTPoint, String) -> Annotation3D``

   **Parameters:**

   * **origin** (``SNTPoint``)
   * **originOpposite** (``SNTPoint``)
   * **label** (``str``)

   **Returns:** ``Annotation3D``

.. method:: annotatePoint(point, label)

   Adds a highlighting point annotation to this viewer.

   **Signature:** ``annotatePoint(SNTPoint, String) -> Annotation3D``

   **Parameters:**

   * **point** (``SNTPoint``): - the node to be highlighted
   * **label** (``str``)

   **Returns:** (``Annotation3D``) the `Annotation3D`

.. method:: annotatePoints(points, label)

   Adds a scatter (point cloud) annotation to this viewer.

   **Signature:** ``annotatePoints(Collection, String) -> Annotation3D``

   **Parameters:**

   * **points** (``List[Any]``): - the collection of points in the annotation
   * **label** (``str``)

   **Returns:** (``Annotation3D``) the `Annotation3D`

.. method:: annotateSurface(points, label)

   Computes a convex hull from a collection of points and adds it to the scene as an annotation.

   **Signature:** ``annotateSurface(Collection, String) -> Annotation3D``

   **Parameters:**

   * **points** (``List[Any]``): - the collection of points defining the convex set.
   * **label** (``str``)

   **Returns:** (``Annotation3D``) the `Annotation3D`

.. method:: dispose()

   Closes and releases all the resources used by this viewer.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: duplicate()

   Creates a duplicate of this viewer containing only visible objects.

This method creates a new Viewer3D instance and copies all currently visible objects (trees, meshes, annotations) from this viewer to the new one. The duplicate viewer maintains the same visual settings and object properties but operates independently from the original.

   **Signature:** ``duplicate() -> Viewer3D``

   **Returns:** (``Viewer3D``) a new Viewer3D instance containing copies of all visible objects

.. method:: equals(obj)

   **Signature:** ``equals(Object) -> boolean``

   **Parameters:**

   * **obj** (``Any``)

   **Returns:** ``bool``

.. method:: freeze()

   Does not allow scene to be interactive. Only static orthogonal views allowed.

   **Signature:** ``freeze() -> void``

   **Returns:** ``None``

.. method:: logSceneControls()

   Logs API calls controlling the scene (view point, bounds, etc.) to Script Recorder (or Console if Script Recorder is not running). Useful for programmatic control of animations.

   **Signature:** ``logSceneControls() -> void``

   **Returns:** ``None``

.. method:: mergeAnnotations(annotations, label)

   Merges a collection of annotations into a single object.

   **Signature:** ``mergeAnnotations(Collection, String) -> Annotation3D``

   **Parameters:**

   * **annotations** (``List[Any]``): - the collection of annotations.
   * **label** (``str``)

   **Returns:** (``Annotation3D``) the merged `Annotation3D`

.. method:: rebuild(obj)

   Rebuilds (repaints) a scene object (e.g., a Tree after being modified elsewhere)

   **Signature:** ``rebuild(Object) -> void``

   **Parameters:**

   * **obj** (``Any``): - the object to be re-rendered (or its label)

   **Returns:** ``None``

.. method:: recordRotation(angle, frames, destinationDirectory)

   Records an animated rotation of the scene around the specified axis as a sequence of images.

   **Signature:** ``recordRotation(float, int, File) -> void``

   **Parameters:**

   * **angle** (``float``): - the rotation angle (e.g., 360 for a full rotation)
   * **frames** (``int``)
   * **destinationDirectory** (``str``)

   **Returns:** ``None``

.. method:: remove(object)

   Script friendly method to remove an object (`Tree`, `OBJMesh`, AbstractDrawable, `String` (object label), etc.) from this viewer's scene.

   **Signature:** ``remove(Object) -> void``

   **Parameters:**

   * **object** (``Any``): - the object to be removed, or the unique String identifying it. Collections supported.

   **Returns:** ``None``

.. method:: rotate(degrees)

   Rotates the scene.

   **Signature:** ``rotate(float) -> void``

   **Parameters:**

   * **degrees** (``float``): - the angle, in degrees

   **Returns:** ``None``

.. method:: runCommand(cmd)

   **Signature:** ``runCommand(String) -> void``

   **Parameters:**

   * **cmd** (``str``): - the recorded command

   **Returns:** ``None``

.. method:: show()

   Displays the viewer under specified dimensions. Useful when generating scene animations programmatically.

   **Signature:** ``show() -> Frame``

   **Returns:** ``Any``

.. method:: snapshot()

   Retrieves the specified scene view as an image.

   **Signature:** ``snapshot() -> ImagePlus``

   **Returns:** ``Any``

.. method:: snapshotWYSIWYG()

   Retrieves the current scene as an image using a screen capture that matches the on-screen rendering exactly (WYSIWYG). This bypasses the OpenGL framebuffer readback, avoiding color discrepancies from premultiplied alpha and display color management. Falls back to `snapshot()` when the viewer is not visible (e.g., offscreen rendering or headless environments).

   **Signature:** ``snapshotWYSIWYG() -> ImagePlus``

   **Returns:** (``Any``) the bitmap image of the current scene as displayed on screen

.. method:: translate(treeLabels, offset)

   Translates the specified collection of `Tree`s.

   **Signature:** ``translate(Collection, SNTPoint) -> void``

   **Parameters:**

   * **treeLabels** (``List[Any]``): - the collection of Tree identifiers (as per addTree(Tree)) specifying the Trees to be translated
   * **offset** (``SNTPoint``)

   **Returns:** ``None``

.. method:: unfreeze()

   Allows scene to be interactive.

   **Signature:** ``unfreeze() -> void``

   **Returns:** ``None``

.. method:: validate()

   Checks if all drawables in the 3D scene are being rendered properly, rebuilding the entire scene if not. Useful to "hard-reset" the viewer, e.g., to ensure all meshes are redrawn.

   **Signature:** ``validate() -> void``

   **Returns:** ``None``

.. method:: zoomTo(objects)

   Zooms the scene into the bounding box enclosing the specified objects.

   **Signature:** ``zoomTo(Object[]) -> void``

   **Parameters:**

   * **objects** (``List[Any]``): - the objects to be zoomed into. These can be OBJMesh, Tree, Annotation3D, etc., or string(s) defining objects listed in the control panel. Collections of supported objects are also supported. If Null view is reset. If "visible" view is zoomed to visible objects

   **Returns:** ``None``


WekaModelLoader
---------------

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


ZBAtlasUtils
------------

.. method:: brainBarycentre()

   Returns the spatial centroid of the template brain.

   **Signature:** ``brainBarycentre() -> SNTPoint``

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of the brain outline.


----

*Category index generated on 2026-11-05 07:43:37*