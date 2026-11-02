
``SNT`` Class Documentation
========================


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

Implements the SNT plugin.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearIsolatedTreeID()

   Convenience for ``setIsolatedTreeID(-1)``: lifts any active tree isolation.


.. py:method:: closeAndResetAllPanes()

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getActiveCanvasPixelOffset()

   


.. py:method:: getAverageSeparation()

   


.. py:method:: getBatchRetraceChannelFrame()

   


.. py:method:: getCalibration()

   


.. py:method:: getCanvas(int)

   


.. py:method:: getChannel()

   


.. py:method:: getContext()

   


.. py:method:: getCostType()

   


.. py:method:: getCurrentPath()

   


.. py:method:: getDataset()

   Gets the Image being traced as Dataset. If the loaded image has been closed, cached pixel data is returned as per ``getLoadedDataAsImp()``. If no resident ``ImagePlus`` exists at all (e.g., data streamed from disk/network, backed only by ``ctSlice3d``), a Dataset is instead built directly from ``getLoadedDataAsImg(boolean)``, so Dataset-only commands. Null is returned if no image data exists at all.

   NB: in the streamed-data fallback, the returned Dataset only ever contains a single channel/ frame (whichever is currently active): ``ctSlice3d`` is a single C/T slice by construction. Commands that need every channel or frame simultaneously will still require a resident ``ImagePlus``.

   NB2: a materialized crop (see ``isMaterializedCrop()``) always has a resident ``ImagePlus`` (the crop itself), so it never takes the streamed-data fallback above, returning the crop's own Dataset as-is, matching whatever ``buildMaterializedCrop(BoundingBox)`` captured (see ``getMaterializedCropChannel()``/``getMaterializedCropFrame()``).


.. py:method:: getDefaultCanvasPixelOffset()

   Public wrapper around ``defaultCanvasPixelOffset()``, for callers outside this class that need the crop-independent baseline offset even while a materialized crop is active on the classic 2D canvas - e.g. a BDV/BVV interaction that should behave the same regardless of what the classic canvas currently has materialized, mirroring how 


   ::

       createSearch(double, double, double, double, double, double, SearchSettingsSnapshot, boolean)


   's ``useStreamedSource`` parameter picks between the two.


.. py:method:: getDepth()

   


.. py:method:: getDrawDiameters()

   


.. py:method:: getEditModeBlocker()

   As ``getEditModeBlocker()``, for front-ends that select the path to be edited themselves (e.g., the one nearest to the cursor) when no single path is selected


.. py:method:: getFillThreshold()

   


.. py:method:: getFilledBinaryImp()

   


.. py:method:: getFilledDistanceImp()

   


.. py:method:: getFilledImp()

   


.. py:method:: getFilledLabelImp()

   


.. py:method:: getFilledMeshes(double)

   Converts the currently loaded fills to meshes, one per fill, in the spatially calibrated coordinates of the image (the same space as path nodes). Only voxels within each fill's threshold are included.


.. py:method:: getFilterType()

   


.. py:method:: getFrame()

   


.. py:method:: getFullImageDimensions()

   Returns the dimensions of the full loaded image/dataset, even while a materialized crop (see ``materializeDisplayCanvas(BoundingBox)``) is installed as this session's own canvas. Unlike ``width``/``height``/``depth``, which temporarily reflect the crop's own (small) size for as long as it stays open (see ``installMaterializedCrop(sc.fiji.snt.SNT.MaterializedCrop)``), this always resolves against ``streamedSourceData`` (the pristine, pre-crop source) when one is cached, falling back to width/height/depth otherwise (i.e. no crop is open, or this is a classic/non-streamed session where streamedSourceData is never populated).

   Intended for callers that need the true dataset extent regardless of any transient crop, e.g. ``PathAndFillManager.writeXML(java.lang.String, boolean)`` when writing the ``<imagesize>`` element of a .traces file.


.. py:method:: getFullSourceData()

   Non-generic wrapper around ``getStreamedOrLoadedData()``, for callers outside this class that need the full, crop-independent source data - e.g. BDV/BVV's own tracing/search (shared by both viewers, see ``AbstractBigViewer``) or the Sigma preview palette, which must show data around the point actually clicked, not clamped to whatever (possibly smaller) crop happens to be materialized on the classic canvas at the same time. In classic (non-streamed) sessions this is simply ``getLoadedData()``, since no crop can ever be materialized there. Pair with ``getDefaultCanvasPixelOffset()`` for converting a click into a pixel index into this data.


.. py:method:: getFullSourceDataAsImp()

   Crop-independent counterpart of ``getLoadedDataAsImp()``: the full source data (``getFullSourceData()``) as an ImagePlus, e.g., for a preview that must show the region actually clicked in BDV/BVV regardless of the crop that may be materialized on the classic canvas. Its pixel grid is the one described by ``getDefaultCanvasPixelOffset()``. Same as ``getLoadedDataAsImp()`` if no crop is materialized.


.. py:method:: getHeight()

   


.. py:method:: getHeuristicType()

   


.. py:method:: getImageFilenamePrefix()

   Returns a filesystem-safe basename identifying the image currently being traced, for use as a prefix when generating output filenames (backups, exported bookmarks, notes, etc). Handles both standard mode (title of ``getImagePlus()``) and ``stream mode`` (title of the source loaded in the active ``big viewer``, if any).


.. py:method:: getImagePlus()

   Gets the Image associated with a view pane.


.. py:method:: getIsolatedTreeID()

   


.. py:method:: getLastTracedPath()

   Returns the path most recently traced interactively in this session, as opposed to paths loaded from file or created by other means.


.. py:method:: getLoadedData()

   


.. py:method:: getLoadedDataAsImg(boolean)

   


.. py:method:: getLoadedDataAsImp()

   Retrieves the pixel data of the main image currently loaded in memory as an ImagePlus object. Returned image is always a single channel image.


.. py:method:: getLoadedIterable()

   


.. py:method:: getMaterializationMemoryBudget()

   


.. py:method:: getMaterializedCropChannel()

   


.. py:method:: getMaterializedCropFrame()

   


.. py:method:: getMaterializedCropWorldBounds()

   


.. py:method:: getMinimumSeparation()

   


.. py:method:: getNodeEditor()

   Returns the node editor shared by all front-ends of this instance (tracing canvas, Bdv and Bvv). It holds the path being edited, its active node and the undo history of 'Edit Mode'.


.. py:method:: getPathAndFillManager()

   


.. py:method:: getPixelDepth()

   


.. py:method:: getPixelHeight()

   


.. py:method:: getPixelWidth()

   


.. py:method:: getPrefs()

   


.. py:method:: getSearchImageType()

   


.. py:method:: getSearchType()

   


.. py:method:: getSecondaryData()

   


.. py:method:: getSecondaryDataAsImp()

   Retrieves the 'secondary image' data currently loaded in memory as an ImagePlus object. Returned image is always of 32-bit type.


.. py:method:: getSecondaryImageMinMax()

   


.. py:method:: getSeedOverlay()

   Returns the ``SeedOverlay`` associated with this SNT instance. The overlay holds candidate `SeedPoint`s (e.g., output of upstream point detectors) and is rendered on the tracing canvas when non-empty.

   The overlay is **transient**: it is automatically cleared when the active image changes (see ``initialize(ImagePlus)``) and is not persisted with the ``.traces`` file. Importers should use ``SeedOverlay.addAll(java.util.Collection)`` for bulk loads.


.. py:method:: getSelectedPaths()

   


.. py:method:: getSinglePane()

   


.. py:method:: getSingleSelectedPath()

   


.. py:method:: getSpacingUnits()

   


.. py:method:: getStats()

   


.. py:method:: getStatsSecondary()

   


.. py:method:: getUI()

   Gets the main UI.


.. py:method:: getUseSubVolumeStats()

   


.. py:method:: getWidth()

   


.. py:method:: getWorldOriginOffset()

   


.. py:method:: getZYXZ(ImagePlus, int)

   


.. py:method:: is2D()

   


.. py:method:: isAstarEnabled()

   Checks if A* search is enabled


.. py:method:: isEditModeEnabled()

   


.. py:method:: isMaterializedCrop()

   


.. py:method:: isOnlySelectedPathsVisible()

   


.. py:method:: isSecondaryDataAvailable()

   Assesses if the 'secondary image' has been loaded into memory. Note that while some tracer Threads will load the image into memory, others may waive the loading to third party libraries


.. py:method:: isShowOnlyActiveCTposPaths()

   


.. py:method:: isSpacingKnownFromSource()

   


.. py:method:: isStreamMode()

   Returns whether this session is running in stream mode ("SNT Stream"), i.e., without access to a full in-core materialized image but rather a lazily-loaded BDV/BVV-backed source (typically an OME-Zarr/N5 dataset; see ``BigDataLoaderCmd``).


.. py:method:: isTracingActive()

   


.. py:method:: isTracingOnSecondaryImageActive()

   


.. py:method:: isTracingPaused()

   


.. py:method:: isTreeIsolationActive()

   


.. py:method:: isZoomAllPanesDisabled()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAnnotationsColorAllPanes(Color)

   


.. py:method:: setAnnotationsVisible(boolean)

   Enables/Disables SNT overlays over tracing views. Note that disabling overlays will also suppress most GUI-related operations.


.. py:method:: setBatchRetraceChannelFrame(Integer, Integer)

   Sets or clears the channel/frame lock described in ``getBatchRetraceChannelFrame()``.


.. py:method:: setCanvasLabelAllPanes(String)

   


.. py:method:: setChannelAndFrame(int, int)

   Sets the channel/frame (1-based, IJ hyperstack convention) to be associated with subsequently traced paths (via ``Path.setCTposition(int, int)``), and, for 


   ::

       manualTrace(sc.fiji.snt.util.SNTPoint, sc.fiji.snt.util.SNTPoint, sc.fiji.snt.util.PointInImage)


   , with the pixel data A* search reads (see ``setImageData(net.imglib2.RandomAccessibleInterval<?>)``).

   Useful alongside ``setImageData(net.imglib2.RandomAccessibleInterval<?>)``/``setImageMetadata(int, int, int, double, double, double, java.lang.String)`` when pixel data comes from a source with no single, already-loaded multichannel/multi-timepoint array to index into (e.g. each channel of a BigDataViewer/SpimData or N5/Zarr source is its own separate object): callers are responsible for keeping the three in sync when the active channel/timepoint changes.


.. py:method:: setCostType(CostType)

   


.. py:method:: setCurrentPath(Path)

   


.. py:method:: setCursorTextAllPanes(String)

   


.. py:method:: setDrawCrosshairsAllPanes(boolean)

   


.. py:method:: setDrawDiameters(boolean)

   


.. py:method:: setFillList(List)

   


.. py:method:: setFillThreshold(double)

   Sets the fill threshold distance. Typically, this value is set before a filling operation as a starting value for the ``FillerThread``.


.. py:method:: setFillThresholdFrom(double, double, double)

   


.. py:method:: setFilterType(FilterType)

   


.. py:method:: setHeuristicType(HeuristicType)

   


.. py:method:: setImageData(RandomAccessibleInterval)

   Directly sets the image data backing A* search, without requiring an ``ImgPlus`` wrapper. Useful when pixel data comes from a source whose ``RandomAccessibleInterval`` is already resolved elsewhere (e.g., a BigDataViewer/SpimData ``ImgLoader``, or a BDV/BVV ``Source``), and building/discarding a full ``ImgPlus`` just to satisfy ``SNT(ImgPlus)`` would be wasteful, or would not preserve lazy/chunked access the way the original object does.

   Callers remain responsible for also calling ``setImageMetadata(int, int, int, double, double, double, java.lang.String)`` (or equivalent) with matching dimensions/calibration; this method does not attempt to infer them from ``data``.

   ``data``'s pixel type must be a ``RealType``; other types (e.g. ``ARGBType``) will throw a ``ClassCastException`` later, e.g., the first time A* search accesses a pixel.


.. py:method:: setImageMetadata(int, int, int, double, double, double, String)

   Sets image dimensions and calibration without providing actual pixel data. Useful when the source image is not directly accessible as random-access data (e.g., a BigDataViewer ``AbstractSpimData``/IMS source, or an ambiguous N5/Zarr layout) but its metadata (size, voxel spacing) is still known. This allows features that only need bounds/scale (e.g., manual tracing, bounds/distance checks) to work correctly with the image's real dimensions, even though ``accessToValidImageData()`` keeps reporting no data is available (this does NOT set ``ctSlice3d``, so A* search remains unavailable).


.. py:method:: setIsolatedTreeID(int)

   Isolates a single tree (arbor) for display across every tracing viewer, hiding paths belonging to any other tree. Orthogonal to ``setShowOnlySelectedPaths(boolean)``: does not touch path selection or rendered colors, it only restricts which trees are candidates for display at all. Pass -1 (or call ``clearIsolatedTreeID()``) to lift the restriction.


.. py:method:: setPathList(Path, boolean)

   


.. py:method:: setSearchImageType(SearchImageType)

   


.. py:method:: setSearchType(SearchType)

   


.. py:method:: setSecondaryImage(File)

   Specifies the 'secondary image' to be used during a tracing session.


.. py:method:: setSecondaryImageMinMax(double, double)

   


.. py:method:: setSelectedPaths(Collection, Object)

   


.. py:method:: setShowOnlySelectedPaths(boolean)

   


.. py:method:: setSinglePane(boolean)

   


.. py:method:: setStopFillAtThreshold(boolean)

   


.. py:method:: setStoreExtraFillNodes(boolean)

   


.. py:method:: setTemporaryPath(Path)

   


.. py:method:: setUseSubVolumeStats(boolean)

   


.. py:method:: setWorldOriginOffset(double, double, double)

   Sets a rigid world-space origin offset (in calibrated units) to be applied on top of the usual ``voxelIndex * spacing`` coordinate mapping. Not needed for a normally-loaded ``ImgPlus`` (its calibration/origin is assumed anchored at world (0,0,0)), but required when pixel data was wired in via ``setImageData(net.imglib2.RandomAccessibleInterval<?>)``/``setImageMetadata(int, int, int, double, double, double, java.lang.String)`` from a source whose own coordinate frame is *not* anchored at (0,0,0) - e.g. a BigDataViewer/N5 ``Source`` whose ``sourceTransform`` carries a translation (see ``BigDataLoaderCmd#applyFallbackCalibration``).

   This offset is not applied automatically to coordinates read elsewhere in this class (e.g. manual tracing, A* search); callers that produce ``Tree``/``Path`` results from such a source are responsible for applying it themselves, e.g. via ``Tree.translate(double, double, double)``.

   **Not the same thing as ``ij.measure.Calibration#xOrigin/yOrigin/zOrigin``** (nor a drop-in replacement for it), despite the similar name/purpose. The two use different conventions and are not numerically interchangeable:

   - This offset is applied in **world** space, after scaling: ``world = voxelIndex * spacing + offset`` .

   - ``Calibration`` 's origin is applied in **pixel** space, before scaling (see ``Calibration#getRawX/Y/Z`` , and ``ShollPoint#rawZ`` for the equivalent hand-written formula): ``world = (voxelIndex - origin) * spacing`` , i.e. ``voxelIndex = world / spacing + origin`` .

   Converting between the two requires the spacing too (``offset = -origin * spacing``); they are not the same number and must not be assigned to/read from each other directly. ``getCalibration()`` always returns spacing-only calibration objects with ``xOrigin/yOrigin/zOrigin`` left at their default of 0, regardless of this offset; callers needing pixel<->world conversions that account for this offset must use ``getWorldOriginOffset()`` directly (see ``BookmarkManager#pixelToWorld``/ ``#worldToPixel`` for a worked example), not ``getCalibration()`` alone.


.. py:method:: setZPositionAllPanes(int, int, int)

   


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: computeImgStats(Iterable, ImageStatistics, CostType)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: captureView(String, ColorRGB)

   Retrieves a WYSIWYG 'snapshot' of a tracing canvas without voxel data.


.. py:method:: materializeDisplayCanvas(BoundingBox)

   As ``materializeDisplayCanvas(BoundingBox)``, but reading from either this session's main streamed source or its secondary (filtered) image - see ``buildMaterializedCrop(BoundingBox, boolean)``.


.. py:method:: rebuildDisplayCanvases()

   Rebuilds display canvases, i.e., the placeholder canvases used when no valid image data exists (a single-canvas is rebuilt if only the XY view is active).

   Useful when multiple files are imported and imported paths 'fall off' the dimensions of current canvas(es). If there is not enough memory to accommodate enlarged dimensions, the resulting canvas will be a 2D image.


.. py:method:: showCorrespondencesTo(File, Color, double)

   


.. py:method:: showMIPOverlays(double)

   


.. py:method:: showStatus(int, int, String)

   Description copied from interface: ``PaneOwner``


.. py:method:: updateAllViewers()

   


.. py:method:: updateDisplayCanvases()

   Rebuilds display canvas(es) to ensure all paths are contained in the image. Does nothing if placeholder canvas(es) are not being used.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: loadLabelsFile(String)

   


.. py:method:: loadSecondaryImage(File)

   


.. py:method:: loadTracings(File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: accessToValidImageData()

   Checks whether valid image data exists.


.. py:method:: addFillerThread(FillerThread)

   


.. py:method:: addListener(SNTListener)

   


.. py:method:: autoTrace(List, PointInImage)

   Automatically traces a path from a point A to a point B. See ``autoTrace(List, PointInImage)`` for details.


.. py:method:: autoTraceSync(List, PointInImage)

   Variant of ``autoTraceSync(List, PointInImage)`` that uses a frozen ``SNT.SearchSettingsSnapshot`` instead of the live cost function/data structure/secondary-image settings, so every segment of every path in a long-running batch (e.g. ``AStarRefiner``) is traced with identical settings, immune to changes made mid-run via the (deliberately still enabled) A* controls.


.. py:method:: buildMaterializedCrop(BoundingBox)

   As ``buildMaterializedCrop(BoundingBox)``, but reading from either this session's main streamed source or its secondary (filtered) image.


.. py:method:: cancelPath()

   Cancels the temporary path.


.. py:method:: cancelSearch(boolean)

   


.. py:method:: cancelTemporary()

   


.. py:method:: changeUIState(int)

   


.. py:method:: confirmTemporary(boolean)

   


.. py:method:: createCanvas(ImagePlus, int)

   


.. py:method:: deselectLastPath()

   Removes the most recently selected path from the current selection (so nothing remains selected if only one path was selected). Does nothing in edit mode, in which a single path is always selected


.. py:method:: disableEventsAllPanes(boolean)

   Sets default path colors.


.. py:method:: disableZoomAllPanes(boolean)

   


.. py:method:: editModeAllowed()

   Checks if edit mode can be enabled, optionally using a specific path.


.. py:method:: enableAstar(boolean)

   Toggles the A* search algorithm (enabled by default)


.. py:method:: enableSecondaryLayerTracing(boolean)

   


.. py:method:: enableSnapCursor(boolean)

   Enables SNT's XYZ snap cursor feature. Does nothing if no image data is available or currently loaded image is binary


.. py:method:: enterEditMode(Path)

   Enables 'Edit Mode' on all front-ends (tracing canvas, Bdv and Bvv)


.. py:method:: estimateMaterializationBytes(long, long, long)

   Estimates the number of bytes required to materialize a crop of the given voxel dimensions from this session's streamed source (see ``materializeDisplayCanvas(BoundingBox)``), using the source's actual pixel type.


.. py:method:: exitEditMode()

   Disables 'Edit Mode' on all front-ends (tracing canvas, Bdv and Bvv)


.. py:method:: findPointInStack(int, int, int, int[])

   


.. py:method:: findPointInStackPrecise(double, double, int, double[])

   


.. py:method:: finished(SearchInterface, boolean)

   


.. py:method:: flushSecondaryData()

   


.. py:method:: initPathsToFill(Set, boolean)

   


.. py:method:: initialize(ImagePlus)

   


.. py:method:: installMaterializedCrop(MaterializedCrop)

   Installs a crop built by ``buildMaterializedCrop(BoundingBox)`` as this session's own XY canvas, in place, the same mechanism ``rebuildDisplayCanvases()`` uses for the blank placeholder, but with real pixel data instead of an empty image. This allows right-click editing (extend/fork/join/delete nodes, wired into ``InteractiveTracerCanvas``) real pixel context in Stream mode, where BDV/BVV have no equivalent context menu.

   Deliberately scoped to editing, not tracing: this reuses the normal ``initialize(ImagePlus)`` pipeline, which also replaces ``ctSlice3d`` with the crop's own (small) pixel data. A* search/GWDT tracing initiated after materializing is therefore scoped to the crop's own bounds, not the full streamed volume, until a different region is materialized (or the session is reconnected). There is no path for pixel edits to write back into the canonical streamed source: only geometry/paths persist, pixel edits are local to this session.


.. py:method:: makePathVolume(Collection, boolean)

   Rasterizes centerline of paths into an ImagePlus


.. py:method:: manualTrace(SNTPoint, SNTPoint, PointInImage)

   Manually traces a straight path from a point A to a point B, bypassing A* (or any other configured ``SearchInterface``) entirely: the two points are simply connected via ``ManualTracerThread``. Unlike ``autoTrace(SNTPoint, SNTPoint, PointInImage, boolean)``, this method does not depend on, or alter, ``isAstarEnabled()``. Runs headless (no SNTUI state changes) and, since it does not search the image, is cheap enough to be safely called off the EDT.

   The returned path is *not* added to the Path Manager: callers are responsible for that (see ``PathAndFillManager.addPath(Path, boolean, boolean)``).


.. py:method:: mouseMovedTo(double, double, int, boolean)

   


.. py:method:: notifyActiveNodeChanged(AbstractBigViewer)

   Refreshes the active-node (and lock) markers of the Bdv/Bvv viewers after the active node of the editing path was changed or (un)locked by another front-end


.. py:method:: notifyEditingPathChanged()

   Refreshes the Bdv/Bvv rendering of the path being edited after it was modified by the tracing canvas. Throttled so that continuous gestures (e.g., dragging a node) do not flood the viewers


.. py:method:: notifyListeners(SNTEvent)

   


.. py:method:: panEventOccurred(int, int, int)

   


.. py:method:: pointsInSearch(SearchInterface, long, long)

   


.. py:method:: proportionDone(double)

   


.. py:method:: rebuildZYXZpanes()

   


.. py:method:: reloadImage(int, int)

   


.. py:method:: reloadZYXZpanes(int)

   


.. py:method:: removeMIPOverlayAllPanes()

   


.. py:method:: repaintAllPanes()

   


.. py:method:: resolveVoxelBounds(BoundingBox, Calibration)

   As ``resolveVoxelBounds(BoundingBox, Calibration)``, but resolving against either this session's main streamed source or its secondary (filtered) image - see ``buildMaterializedCrop(BoundingBox, boolean)``.


.. py:method:: sameXYZDimensionsAsTracingData(ImagePlus)

   RAI-based overload of ``sameXYZDimensionsAsTracingData(ImagePlus)``, for candidate sources that never go through an ``ImagePlus`` at all (e.g. a big-data secondary layer resolved via ``SpimDataUtils.resolvePathToSource(String)``). Compares XYZ dimensions directly against ``getLoadedData()``, so unlike the ``ImagePlus`` overload this works the same regardless of whether ``MultiDThreePanes.xy`` exists.


.. py:method:: seedStatsFromSubVolume(ImagePlus)

   In Stream mode, seeds unknown main image statistics (min, max) from a small sub-volume already in memory (e.g., the Sigma Palette crop). Computing them from the whole image would require reading every chunk of lazy/remote data. Statistics from a sub-volume are local estimates. Does nothing if statistics are already known.


.. py:method:: selectNone()

   Clears the current path selection. Does nothing in edit mode


.. py:method:: selectPath(Path, boolean)

   


.. py:method:: snapshotSearchSettings()

   Captures the search settings currently configured on this instance, for use by long-running batch callers that need to stay internally consistent even if these settings are changed (via the UI) partway through the run. See ``SNT.SearchSettingsSnapshot``.


.. py:method:: startHessian(String, double, double, boolean)

   Constructs and enables an instance of a hessian eigenvalue filter. If the strategy is "preprocess", the entire filtered image is pre-computed and stored in memory. If the strategy is "lazy", the image is filtered locally during path searches, and filtered data is stored in a disk cache when memory runs full. If you are tracing over a large image or if you are in a memory-limited environment, you should choose "lazy".


.. py:method:: startSholl(PointInImage)

   


.. py:method:: startUI()

   


.. py:method:: threadStatus(SearchInterface, int)

   


.. py:method:: unzoomAllPanes()

   


.. py:method:: zoom100PercentAllPanes()

   


.. py:method:: zoomAllPanes(double)

   


.. py:method:: zoomEventOccurred(boolean, int, int, int)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNT>`_
* `SNT JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNT.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
