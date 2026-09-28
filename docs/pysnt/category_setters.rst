Setters Methods
===============

Methods that modify values or properties of objects.

Total methods in this category: **268**

.. contents:: Classes in this Category
   :local:

Annotation3D
------------

.. method:: setBoundingBoxColor(arg0)

   Determines whether the mesh bounding box should be displayed.

   **Signature:** ``setBoundingBoxColor(ColorRGB) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the color of the mesh bounding box. If null, no bounding box is displayed

   **Returns:** ``None``

.. method:: setColor(arg0, arg1)

   Script friendly method to assign a color to the annotation.

   **Signature:** ``setColor(String, double) -> void``

   **Parameters:**

   * **arg0** (``str``): - the color to render the imported file, either a 1) HTML color codes starting with hash (
   * **arg1** (``float``): ), a color preset ("red", "blue", etc.), or integer triples of the form

   **Returns:** ``None``

.. method:: setTransparency(arg0)

   Script friendly method to assign a transparency to the annotation.

   **Signature:** ``setTransparency(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the color transparency (in percentage)

   **Returns:** ``None``

.. method:: setWireframeColor(arg0)

   Assigns a wireframe color to the annotation.

   **Signature:** ``setWireframeColor(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the wireframe color. Ignored if the annotation has no wireframe.

   **Returns:** ``None``


BiSearch
--------

.. method:: addProgressListener(arg0)

   Description copied from class: AbstractSearch

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the callback to register

   **Returns:** ``None``


BiSearchNode
------------

.. method:: setFFromGoal(arg0)

   **Signature:** ``setFFromGoal(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``

.. method:: setFFromStart(arg0)

   **Signature:** ``setFFromStart(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``

.. method:: setFrom(arg0, arg1, arg2, arg3)

   **Signature:** ``setFrom(double, double, BiSearchNode, boolean) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``BiSearchNode``)
   * **arg3** (``bool``)

   **Returns:** ``None``

.. method:: setFromGoal(arg0, arg1, arg2)

   **Signature:** ``setFromGoal(double, double, BiSearchNode) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setFromStart(arg0, arg1, arg2)

   **Signature:** ``setFromStart(double, double, BiSearchNode) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setGFromGoal(arg0)

   **Signature:** ``setGFromGoal(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``

.. method:: setGFromStart(arg0)

   **Signature:** ``setGFromStart(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``

.. method:: setHeapHandle(arg0, arg1)

   **Signature:** ``setHeapHandle(AddressableHeap$Handle, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: setHeapHandleFromGoal(arg0)

   **Signature:** ``setHeapHandleFromGoal(AddressableHeap$Handle) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setHeapHandleFromStart(arg0)

   **Signature:** ``setHeapHandleFromStart(AddressableHeap$Handle) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setPosition(arg0, arg1, arg2)

   **Signature:** ``setPosition(int, int, int) -> void``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``None``

.. method:: setPredecessorFromGoal(arg0)

   **Signature:** ``setPredecessorFromGoal(BiSearchNode) -> void``

   **Parameters:**

   * **arg0** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setPredecessorFromStart(arg0)

   **Signature:** ``setPredecessorFromStart(BiSearchNode) -> void``

   **Parameters:**

   * **arg0** (``BiSearchNode``)

   **Returns:** ``None``

.. method:: setState(arg0, arg1)

   **Signature:** ``setState(BiSearchNode$State, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: setStateFromGoal(arg0)

   **Signature:** ``setStateFromGoal(BiSearchNode$State) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setStateFromStart(arg0)

   **Signature:** ``setStateFromStart(BiSearchNode$State) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setX(arg0)

   **Signature:** ``setX(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: setY(arg0)

   **Signature:** ``setY(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: setZ(arg0)

   **Signature:** ``setZ(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``


BoundingBox
-----------

.. method:: setDimensions(arg0, arg1, arg2)

   Sets the dimensions of this bounding box using uncalibrated (pixel) lengths.

   **Signature:** ``setDimensions(long, long, long) -> void``

   **Parameters:**

   * **arg0** (``int``): - the uncalibrated width
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``None``

.. method:: setOrigin(arg0)

   Sets the origin for this box, i.e., its (xMin, yMin, zMin) vertex.

   **Signature:** ``setOrigin(PointInImage) -> void``

   **Parameters:**

   * **arg0** (``PointInImage``): - the new origin

   **Returns:** ``None``

.. method:: setOriginOpposite(arg0)

   Sets the origin opposite for this box, i.e., its (xMax, yMax, zMax) vertex.

   **Signature:** ``setOriginOpposite(PointInImage) -> void``

   **Parameters:**

   * **arg0** (``PointInImage``): - the new origin opposite.

   **Returns:** ``None``

.. method:: setSpacing(arg0, arg1, arg2, arg3)

   Sets the voxel spacing.

   **Signature:** ``setSpacing(double, double, double, String) -> void``

   **Parameters:**

   * **arg0** (``float``): - the 'voxel width' of the bounding box
   * **arg1** (``float``)
   * **arg2** (``float``)
   * **arg3** (``str``)

   **Returns:** ``None``

.. method:: setUnit(arg0)

   Sets the default length unit for voxel spacing (typically um, for SWC reconstructions)

   **Signature:** ``setUnit(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the new unit

   **Returns:** ``None``


ConvexHullAnalyzer
------------------

.. method:: setContext(arg0)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setLabel(arg0)

   Sets the optional description for the analysis

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - a string describing the analysis

   **Returns:** ``None``


DefaultSearchNode
-----------------

.. method:: setFrom(arg0)

   **Signature:** ``setFrom(DefaultSearchNode) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setHandle(arg0)

   **Signature:** ``setHandle(AddressableHeap$Handle) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setPredecessor(arg0)

   **Signature:** ``setPredecessor(DefaultSearchNode) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


Fill
----

.. method:: setMetric(arg0)

   Sets the cost metric for the filled structure.

   **Signature:** ``setMetric(SNT$CostType) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the cost type to set

   **Returns:** ``None``

.. method:: setSourcePaths(arg0)

   Sets the source paths for the filled structure using a set of paths.

   **Signature:** ``setSourcePaths(Path;) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the set of new source paths

   **Returns:** ``None``

.. method:: setSpacing(arg0, arg1, arg2, arg3)

   **Signature:** ``setSpacing(double, double, double, String) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)
   * **arg3** (``str``)

   **Returns:** ``None``

.. method:: setThreshold(arg0)

   Sets the distance threshold for the filled structure.

   **Signature:** ``setThreshold(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the threshold value to set

   **Returns:** ``None``


FillerThread
------------

.. method:: addNode(arg0, arg1)

   **Signature:** ``addNode(DefaultSearchNode, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: addProgressListener(arg0)

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setSourcePaths(arg0)

   **Signature:** ``setSourcePaths(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``None``

.. method:: setStopAtThreshold(arg0)

   Whether to terminate the fill operation once all nodes less than or equal to the distance threshold have been explored. If false, the search will run until it has explored the entire image. The default is false.

   **Signature:** ``setStopAtThreshold(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): -

   **Returns:** ``None``

.. method:: setStoreExtraNodes(arg0)

   Whether to store above-threshold nodes in the Fill object. The default is true.

   **Signature:** ``setStoreExtraNodes(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): -

   **Returns:** ``None``

.. method:: setThreshold(arg0)

   **Signature:** ``setThreshold(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``


Frangi
------

.. method:: setEnvironment(arg0)

   **Signature:** ``setEnvironment(OpEnvironment) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setInput(arg0)

   **Signature:** ``setInput(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setOutput(arg0)

   **Signature:** ``setOutput(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


GroupedTreeStatistics
---------------------

.. method:: addGroup(arg0, arg1, arg2)

   Adds a comparison group to the analysis queue.

   **Signature:** ``addGroup(Collection, String, String;) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)
   * **arg2** (``Any``)

   **Returns:** ``None``

.. method:: setMinNBins(arg0)

   Sets the minimum number of bins when assembling histograms.

   **Signature:** ``setMinNBins(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the minimum number of bins.

   **Returns:** ``None``


InteractiveTracerCanvas
-----------------------

.. method:: addComponentListener(arg0)

   **Signature:** ``addComponentListener(ComponentListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addFocusListener(arg0)

   **Signature:** ``addFocusListener(FocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyBoundsListener(arg0)

   **Signature:** ``addHierarchyBoundsListener(HierarchyBoundsListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyListener(arg0)

   **Signature:** ``addHierarchyListener(HierarchyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addInputMethodListener(arg0)

   **Signature:** ``addInputMethodListener(InputMethodListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addKeyListener(arg0)

   **Signature:** ``addKeyListener(KeyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseListener(arg0)

   **Signature:** ``addMouseListener(MouseListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseMotionListener(arg0)

   **Signature:** ``addMouseMotionListener(MouseMotionListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseWheelListener(arg0)

   **Signature:** ``addMouseWheelListener(MouseWheelListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addNotify()

   **Signature:** ``addNotify() -> void``

   **Returns:** ``None``

.. method:: addPropertyChangeListener(arg0)

   **Signature:** ``addPropertyChangeListener(PropertyChangeListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disableEvents(arg0)

   **Signature:** ``disableEvents(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: disablePopupMenu(arg0)

   **Signature:** ``disablePopupMenu(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``


MultiTreeColorMapper
--------------------

.. method:: setMinMax(arg0, arg1)

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(arg0)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


MultiViewer2D
-------------

.. method:: setAxesVisible(arg0)

   **Signature:** ``setAxesVisible(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setColorBarLegend(arg0, arg1, arg2)

   **Signature:** ``setColorBarLegend(String, double, double) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: setGridlinesVisible(arg0)

   **Signature:** ``setGridlinesVisible(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setLayoutColumns(arg0)

   **Signature:** ``setLayoutColumns(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: setOutlineVisible(arg0)

   **Signature:** ``setOutlineVisible(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setTitle(arg0)

   Sets the title of this Viewer's frame.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the viewer's title.

   **Returns:** ``None``

.. method:: setXrange(arg0, arg1)

   Sets a manual range for the viewers' X-axis. Calling setXrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setXrange(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the lower-limit for the X-axis
   * **arg1** (``float``)

   **Returns:** ``None``

.. method:: setYrange(arg0, arg1)

   Sets a manual range for the viewers' Y-axis. Calling setYrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setYrange(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the lower-limit for the Y-axis
   * **arg1** (``float``)

   **Returns:** ``None``


MultiViewer3D
-------------

.. method:: addColorBarLegend(arg0)

   **Signature:** ``addColorBarLegend(ColorMapper) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setAnimationEnabled(arg0)

   **Signature:** ``setAnimationEnabled(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setGap(arg0)

   **Signature:** ``setGap(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: setLabels(arg0)

   **Signature:** ``setLabels(List) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``None``

.. method:: setLayoutColumns(arg0)

   **Signature:** ``setLayoutColumns(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: setTitle(arg0)

   Sets the title of the Viewer's frame.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the viewer's title.

   **Returns:** ``None``

.. method:: setViewMode(arg0)

   **Signature:** ``setViewMode(Viewer3D$ViewMode) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


NeuroMorphoLoader
-----------------

.. method:: enableSourceVersion(arg0)

   Enables or disables the use of source version URLs.

   **Signature:** ``enableSourceVersion(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - true to enable source version URLs, false otherwise

   **Returns:** ``None``


NodeColorMapper
---------------

.. method:: setMinMax(arg0, arg1)

   Description copied from class: ColorMapper

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the mapping lower bound (i.e., the highest measurement value for the LUT scale). It is automatically calculated (the default) when set to Double.NaN
   * **arg1** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(arg0)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


NodeProfiler
------------

.. method:: addInput(arg0, arg1)

   **Signature:** ``addInput(String, Class) -> MutableModuleItem``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``type``)

   **Returns:** ``Any``

.. method:: addOutput(arg0)

   **Signature:** ``addOutput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: removeInput(arg0)

   **Signature:** ``removeInput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: removeOutput(arg0)

   **Signature:** ``removeOutput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setContext(arg0)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setInput(arg0, arg1)

   **Signature:** ``setInput(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setInputs(arg0)

   **Signature:** ``setInputs(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: setNodeStep(arg0)

   **Signature:** ``setNodeStep(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - sets the sampling frequency. I.e., if 10, each 10th node is sampled.

   **Returns:** ``None``

.. method:: setOutput(arg0, arg1)

   **Signature:** ``setOutput(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setOutputs(arg0)

   **Signature:** ``setOutputs(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: setRadius(arg0)

   **Signature:** ``setRadius(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the radius (in pixels) of sampling shape

   **Returns:** ``None``

.. method:: setResolved(arg0, arg1)

   **Signature:** ``setResolved(String, boolean) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: setShape(arg0)

   Sets the shape of the iterating cursor.

   **Signature:** ``setShape(ProfileProcessor$Shape) -> void``

   **Parameters:**

   * **arg0** (``Any``): - A ProfileProcessor.Shape

   **Returns:** ``None``


NodeStatistics
--------------

.. method:: setLabel(arg0)

   Sets a descriptive label to this statistic analysis to be used in histograms, etc.

   **Signature:** ``setLabel(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the descriptive label

   **Returns:** ``None``


Path
----

.. method:: addNode(arg0)

   Appends a node to this Path.

   **Signature:** ``addNode(PointInImage) -> void``

   **Parameters:**

   * **arg0** (``PointInImage``): - the node to be inserted

   **Returns:** ``None``

.. method:: addPointDouble(arg0, arg1, arg2)

   **Signature:** ``addPointDouble(double, double, double) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``


PathAndFillManager
------------------

.. method:: addPath(arg0)

   **Signature:** ``addPath(Path) -> void``

   **Parameters:**

   * **arg0** (``Path``)

   **Returns:** ``None``

.. method:: addPathAndFillListener(arg0)

   Adds a PathAndFillListener. This is used by the interface to have changes in the path manager reported so that they can be reflected in the UI.

   **Signature:** ``addPathAndFillListener(PathAndFillListener) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the listener

   **Returns:** ``None``

.. method:: addTree(arg0, arg1)

   Adds a Tree. If an image is currently being traced, it is assumed it is large enough to contain the tree.

   **Signature:** ``addTree(Tree, String) -> void``

   **Parameters:**

   * **arg0** (``Tree``)
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: addTrees(arg0)

   Adds a collection of Trees.

   **Signature:** ``addTrees(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of trees to be added

   **Returns:** ``None``


PathFitter
----------

.. method:: setCrossSectionRadius(arg0)

   Sets the radius of cross-sectional planes sampled around each node.

At each node, PathFitter samples a square cross-section perpendicular to the path tangent. This radius controls the physical extent of that sampling.

   **Signature:** ``setCrossSectionRadius(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the physical search radius (in physical units)

   **Returns:** ``None``

.. method:: setImage(arg0)

   Sets the target image

   **Signature:** ``setImage(RandomAccessibleInterval) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the Image containing the signal to which the fit will be performed

   **Returns:** ``None``

.. method:: setNodeRadiusFallback(arg0)

   Sets the fallback strategy for node radii at locations where fitting failed.

When cross-section fitting fails at a node (e.g., low SNR, ambiguous geometry), this strategy determines what radius value to assign to that node.

   **Signature:** ``setNodeRadiusFallback(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the fallback strategy: FALLBACK_MODE, FALLBACK_MIN_SEP, or FALLBACK_NAN

   **Returns:** ``None``

.. method:: setProgressCallback(arg0, arg1)

   **Signature:** ``setProgressCallback(int, MultiTaskProgress) -> void``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setReplaceNodes(arg0)

   Sets whether fitting should occur "in place".

   **Signature:** ``setReplaceNodes(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - If true, the nodes of the input Path will be replaced by those of the fitted result. If false, the fitted result is kept as a separated Path linked to the input as per Path.getFitted(). Note that in the latter case, some topological operations (e.g., forking) performed on the fitted result may not percolate to the non-fitted Path.

   **Returns:** ``None``

.. method:: setScope(arg0)

   Sets the fitting scope.

   **Signature:** ``setScope(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - Either RADII, MIDPOINTS, or RADII_AND_MIDPOINTS

   **Returns:** ``None``

.. method:: setShowAnnotatedView(arg0)

   Sets whether an interactive image of the result should be displayed.

   **Signature:** ``setShowAnnotatedView(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - If true, an interactive stack (cross-section view) of the fit is displayed. Note that this is probably only useful if SNT's UI is visible and functional.

   **Returns:** ``None``


PathManagerUI
-------------

.. method:: addComponentListener(arg0)

   **Signature:** ``addComponentListener(ComponentListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addContainerListener(arg0)

   **Signature:** ``addContainerListener(ContainerListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addFocusListener(arg0)

   **Signature:** ``addFocusListener(FocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyBoundsListener(arg0)

   **Signature:** ``addHierarchyBoundsListener(HierarchyBoundsListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyListener(arg0)

   **Signature:** ``addHierarchyListener(HierarchyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addInputMethodListener(arg0)

   **Signature:** ``addInputMethodListener(InputMethodListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addKeyListener(arg0)

   **Signature:** ``addKeyListener(KeyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseListener(arg0)

   **Signature:** ``addMouseListener(MouseListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseMotionListener(arg0)

   **Signature:** ``addMouseMotionListener(MouseMotionListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseWheelListener(arg0)

   **Signature:** ``addMouseWheelListener(MouseWheelListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addNotify()

   **Signature:** ``addNotify() -> void``

   **Returns:** ``None``

.. method:: addPropertyChangeListener(arg0)

   **Signature:** ``addPropertyChangeListener(PropertyChangeListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addWindowFocusListener(arg0)

   **Signature:** ``addWindowFocusListener(WindowFocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addWindowListener(arg0)

   **Signature:** ``addWindowListener(WindowListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addWindowStateListener(arg0)

   **Signature:** ``addWindowStateListener(WindowStateListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: clearSelection()

   Clears the current path selection.

   **Signature:** ``clearSelection() -> void``

   **Returns:** ``None``


PathProfiler
------------

.. method:: addInput(arg0, arg1)

   **Signature:** ``addInput(String, Class) -> MutableModuleItem``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``type``)

   **Returns:** ``Any``

.. method:: addOutput(arg0)

   **Signature:** ``addOutput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: removeInput(arg0)

   **Signature:** ``removeInput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: removeOutput(arg0)

   **Signature:** ``removeOutput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setContext(arg0)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setInput(arg0, arg1)

   **Signature:** ``setInput(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``): - Either ProfileProcessor.Shape
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setInputs(arg0)

   **Signature:** ``setInputs(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: setMetric(arg0)

   **Signature:** ``setMetric(ProfileProcessor$Metric) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setNodeIndicesAsDistances(arg0)

   Sets whether the profile abscissae should be reported in real-word units (the default) or node indices (zero-based). Must be called before calling getValues(Path), getPlot() or getXYPlot().

   **Signature:** ``setNodeIndicesAsDistances(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - If true, distances will be reported as indices.

   **Returns:** ``None``

.. method:: setOutput(arg0, arg1)

   **Signature:** ``setOutput(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setOutputs(arg0)

   **Signature:** ``setOutputs(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: setRadius(arg0)

   **Signature:** ``setRadius(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``


PathResult
----------

.. method:: setErrorMessage(arg0)

   **Signature:** ``setErrorMessage(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: setPath(arg0)

   **Signature:** ``setPath([F) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setSuccess(arg0)

   **Signature:** ``setSuccess(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``


PathStraightener
----------------

.. method:: setWidth(arg0)

   Sets the width of the straightened path image.

   **Signature:** ``setWidth(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the width in pixels

   **Returns:** ``None``


PointInImage
------------

.. method:: setAnnotation(arg0)

   Description copied from interface: SNTPoint

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the annotation to be assigned to this point

   **Returns:** ``None``

.. method:: setHemisphere(arg0)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: setPath(arg0)

   Associates a Path with this node

   **Signature:** ``setPath(Path) -> void``

   **Parameters:**

   * **arg0** (``Path``): - the Path to be associated with this node

   **Returns:** ``None``


SNT
---

.. method:: addFillerThread(arg0)

   **Signature:** ``addFillerThread(FillerThread) -> void``

   **Parameters:**

   * **arg0** (``FillerThread``)

   **Returns:** ``None``

.. method:: addListener(arg0)

   **Signature:** ``addListener(SNTListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disableEventsAllPanes(arg0)

   Sets or clears the channel/frame lock described in `getBatchRetraceChannelFrame()`.

   **Signature:** ``disableEventsAllPanes(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - 1-based channel, or null to clear the lock

   **Returns:** ``None``

.. method:: disableZoomAllPanes(arg0)

   **Signature:** ``disableZoomAllPanes(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: enableAstar(arg0)

   Toggles the A* search algorithm (enabled by default)

   **Signature:** ``enableAstar(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - true to enable A* search, false otherwise

   **Returns:** ``None``

.. method:: enableAutoActivation(arg0)

   **Signature:** ``enableAutoActivation(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: enableAutoSelectionOfFinishedPath(arg0)

   **Signature:** ``enableAutoSelectionOfFinishedPath(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: enableSecondaryLayerTracing(arg0)

   **Signature:** ``enableSecondaryLayerTracing(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: enableSnapCursor(arg0)

   Enables SNT's XYZ snap cursor feature. Does nothing if no image data is available or currently loaded image is binary

   **Signature:** ``enableSnapCursor(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - whether cursor snapping should be enabled

   **Returns:** ``None``


SNTChart
--------

.. method:: addAncestorListener(arg0)

   **Signature:** ``addAncestorListener(AncestorListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addChartMouseListener(arg0)

   **Signature:** ``addChartMouseListener(ChartMouseListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addColorBarLegend(arg0, arg1, arg2, arg3, arg4)

   Adds a color bar legend (LUT ramp).

   **Signature:** ``addColorBarLegend(String, ColorTable, double, double, int) -> void``

   **Parameters:**

   * **arg0** (``str``): - the color bar label
   * **arg1** (``Any``)
   * **arg2** (``float``)
   * **arg3** (``float``)
   * **arg4** (``int``)

   **Returns:** ``None``

.. method:: addComponentListener(arg0)

   **Signature:** ``addComponentListener(ComponentListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addContainerListener(arg0)

   **Signature:** ``addContainerListener(ContainerListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addFocusListener(arg0)

   **Signature:** ``addFocusListener(FocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyBoundsListener(arg0)

   **Signature:** ``addHierarchyBoundsListener(HierarchyBoundsListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyListener(arg0)

   **Signature:** ``addHierarchyListener(HierarchyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addInputMethodListener(arg0)

   **Signature:** ``addInputMethodListener(InputMethodListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addKeyListener(arg0)

   **Signature:** ``addKeyListener(KeyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseListener(arg0)

   **Signature:** ``addMouseListener(MouseListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseMotionListener(arg0)

   **Signature:** ``addMouseMotionListener(MouseMotionListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseWheelListener(arg0)

   **Signature:** ``addMouseWheelListener(MouseWheelListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addNotify()

   **Signature:** ``addNotify() -> void``

   **Returns:** ``None``

.. method:: addOverlay(arg0)

   **Signature:** ``addOverlay(Overlay) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addPolygon(arg0, arg1, arg2)

   **Signature:** ``addPolygon(Polygon2D, String, String) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: addPropertyChangeListener(arg0, arg1)

   **Signature:** ``addPropertyChangeListener(String, PropertyChangeListener) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: addVetoableChangeListener(arg0)

   **Signature:** ``addVetoableChangeListener(VetoableChangeListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


SNTColor
--------

.. method:: setAWTColor(arg0)

   Re-assigns an AWT color.

   **Signature:** ``setAWTColor(Color) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the new color

   **Returns:** ``None``

.. method:: setSWCType(arg0)

   Re-assigns a SWC type integer flag

   **Signature:** ``setSWCType(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the new SWC type

   **Returns:** ``None``


SNTPoint
--------

.. method:: setAnnotation(arg0)

   Assigns a neuropil annotation (e.g., atlas compartment) to this point.

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the annotation to be assigned to this point

   **Returns:** ``None``

.. method:: setHemisphere(arg0)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``


SNTService
----------

.. method:: setContext(arg0)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setInfo(arg0)

   **Signature:** ``setInfo(PluginInfo) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setPriority(arg0)

   **Signature:** ``setPriority(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``


SNTTable
--------

.. method:: addAll(arg0)

   **Signature:** ``addAll(Collection) -> boolean``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``bool``

.. method:: addColumn(arg0, arg1)

   **Signature:** ``addColumn(String, [D) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: addFirst(arg0)

   Sets the title of the table.

   **Signature:** ``addFirst(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the table's title

   **Returns:** ``None``

.. method:: addGenericColumn(arg0, arg1)

   **Signature:** ``addGenericColumn(String, Collection) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``List[Any]``)

   **Returns:** ``None``

.. method:: addLast(arg0)

   **Signature:** ``addLast(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


SNTUI
-----

.. method:: addComponentListener(arg0)

   **Signature:** ``addComponentListener(ComponentListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addContainerListener(arg0)

   **Signature:** ``addContainerListener(ContainerListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addFocusListener(arg0)

   **Signature:** ``addFocusListener(FocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyBoundsListener(arg0)

   **Signature:** ``addHierarchyBoundsListener(HierarchyBoundsListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyListener(arg0)

   **Signature:** ``addHierarchyListener(HierarchyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addInputMethodListener(arg0)

   **Signature:** ``addInputMethodListener(InputMethodListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addKeyListener(arg0)

   **Signature:** ``addKeyListener(KeyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseListener(arg0)

   **Signature:** ``addMouseListener(MouseListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseMotionListener(arg0)

   **Signature:** ``addMouseMotionListener(MouseMotionListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseWheelListener(arg0)

   **Signature:** ``addMouseWheelListener(MouseWheelListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addNotify()

   **Signature:** ``addNotify() -> void``

   **Returns:** ``None``

.. method:: addPropertyChangeListener(arg0)

   **Signature:** ``addPropertyChangeListener(PropertyChangeListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addWindowFocusListener(arg0)

   **Signature:** ``addWindowFocusListener(WindowFocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addWindowListener(arg0)

   **Signature:** ``addWindowListener(WindowListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addWindowStateListener(arg0)

   **Signature:** ``addWindowStateListener(WindowStateListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


SWCPoint
--------

.. method:: setAnnotation(arg0)

   Description copied from interface: SNTPoint

   **Signature:** ``setAnnotation(BrainAnnotation) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the annotation to be assigned to this point

   **Returns:** ``None``

.. method:: setColor(arg0)

   Sets the color of this point.

   **Signature:** ``setColor(Color) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the color to set

   **Returns:** ``None``

.. method:: setHemisphere(arg0)

   **Signature:** ``setHemisphere(char) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: setPath(arg0)

   **Signature:** ``setPath(Path) -> void``

   **Parameters:**

   * **arg0** (``Path``)

   **Returns:** ``None``

.. method:: setPrevious(arg0)

   Sets the preceding node in the reconstruction

   **Signature:** ``setPrevious(SWCPoint) -> void``

   **Parameters:**

   * **arg0** (``SWCPoint``): - the previous node preceding this one

   **Returns:** ``None``

.. method:: setTags(arg0)

   Sets the tags associated with this point.

   **Signature:** ``setTags(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the tags string

   **Returns:** ``None``


SciViewSNT
----------

.. method:: addTree(arg0)

   Adds a tree to the associated SciView instance. A new SciView instance is automatically instantiated if setSciView(SciView) has not been called.

   **Signature:** ``addTree(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree to be added. The Tree's label will be used as identifier. It is expected to be unique when rendering multiple Trees, if not (or no label exists) a unique label will be generated.

   **Returns:** ``None``

.. method:: removeTree(arg0)

   Removes the specified Tree.

   **Signature:** ``removeTree(Tree) -> boolean``

   **Parameters:**

   * **arg0** (``Tree``): - the tree previously added to SciView using addTree(Tree)

   **Returns:** (``bool``) true, if tree was successfully removed.

.. method:: setSciView(arg0)

   Sets the SciView to be used.

   **Signature:** ``setSciView(SciView) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the SciView instance. Null allowed.

   **Returns:** ``None``


SearchThread
------------

.. method:: addNode(arg0, arg1)

   **Signature:** ``addNode(DefaultSearchNode, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: addProgressListener(arg0)

   Description copied from class: AbstractSearch

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the callback to register

   **Returns:** ``None``


ShollAnalyzer
-------------

.. method:: setEnableCurveFitting(arg0)

   Sets whether curve fitting computations should be performed.

   **Signature:** ``setEnableCurveFitting(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - if

   **Returns:** ``None``

.. method:: setPolynomialFitRange(arg0, arg1)

   Sets the polynomial fit range for linear Sholl statistics.

   **Signature:** ``setPolynomialFitRange(int, int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the lowest degree to be considered. Set it to -1 to skip polynomial fit
   * **arg1** (``int``)

   **Returns:** ``None``


SkeletonConverter
-----------------

.. method:: setConnectComponents(arg0)

   **Signature:** ``setConnectComponents(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setLengthThreshold(arg0)

   **Signature:** ``setLengthThreshold(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``

.. method:: setMaxConnectDist(arg0)

   **Signature:** ``setMaxConnectDist(double) -> void``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``None``

.. method:: setOrigIP(arg0)

   **Signature:** ``setOrigIP(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setPruneEnds(arg0)

   **Signature:** ``setPruneEnds(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setPruneMode(arg0)

   **Signature:** ``setPruneMode(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: setRootRoi(arg0, arg1)

   **Signature:** ``setRootRoi(Roi, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``None``

.. method:: setShortestPath(arg0)

   **Signature:** ``setShortestPath(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setSilent(arg0)

   **Signature:** ``setSilent(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setVerbose(arg0)

   **Signature:** ``setVerbose(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``


TracerCanvas
------------

.. method:: addComponentListener(arg0)

   **Signature:** ``addComponentListener(ComponentListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addFocusListener(arg0)

   **Signature:** ``addFocusListener(FocusListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyBoundsListener(arg0)

   **Signature:** ``addHierarchyBoundsListener(HierarchyBoundsListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addHierarchyListener(arg0)

   **Signature:** ``addHierarchyListener(HierarchyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addInputMethodListener(arg0)

   **Signature:** ``addInputMethodListener(InputMethodListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addKeyListener(arg0)

   **Signature:** ``addKeyListener(KeyListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseListener(arg0)

   **Signature:** ``addMouseListener(MouseListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseMotionListener(arg0)

   **Signature:** ``addMouseMotionListener(MouseMotionListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addMouseWheelListener(arg0)

   **Signature:** ``addMouseWheelListener(MouseWheelListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: addNotify()

   **Signature:** ``addNotify() -> void``

   **Returns:** ``None``

.. method:: addPropertyChangeListener(arg0)

   **Signature:** ``addPropertyChangeListener(PropertyChangeListener) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disableEvents(arg0)

   **Signature:** ``disableEvents(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: disablePopupMenu(arg0)

   **Signature:** ``disablePopupMenu(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``


TracerThread
------------

.. method:: addNode(arg0, arg1)

   **Signature:** ``addNode(DefaultSearchNode, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: addProgressListener(arg0)

   **Signature:** ``addProgressListener(SearchProgressCallback) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


TreeColorMapper
---------------

.. method:: setMinMax(arg0, arg1)

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(arg0)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


Tubeness
--------

.. method:: setEnvironment(arg0)

   **Signature:** ``setEnvironment(OpEnvironment) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setInput(arg0)

   **Signature:** ``setInput(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setOutput(arg0)

   **Signature:** ``setOutput(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


Viewer2D
--------

.. method:: addColorBarLegend(arg0, arg1, arg2)

   Adds a color bar legend (LUT ramp) to the viewer. Does nothing if no measurement mapping occurred successfully. Note that when performing mapping to different measurements, the legend reflects only the last mapped measurement.

   **Signature:** ``addColorBarLegend(ColorTable, double, double) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: addNodes(arg0)

   **Signature:** ``addNodes(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: addPolygon(arg0, arg1)

   **Signature:** ``addPolygon(Polygon2D, String) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: setAxesVisible(arg0)

   **Signature:** ``setAxesVisible(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setDefaultColor(arg0)

   Sets the default (fallback) color for plotting paths.

   **Signature:** ``setDefaultColor(ColorRGB) -> void``

   **Parameters:**

   * **arg0** (``Any``): - null not allowed

   **Returns:** ``None``

.. method:: setEqualizeAxes(arg0)

   /** Sets whether the axes should be equalized (same scale).

When enabled, both X and Y axes will use the same scale to maintain equal aspect ratio. When disabled, each axis maximizes its range.

   **Signature:** ``setEqualizeAxes(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - true to equalize axes, false otherwise

   **Returns:** ``None``

.. method:: setGridlinesVisible(arg0)

   **Signature:** ``setGridlinesVisible(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setMinMax(arg0, arg1)

   **Signature:** ``setMinMax(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)

   **Returns:** ``None``

.. method:: setNaNColor(arg0)

   **Signature:** ``setNaNColor(Color) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setOutlineVisible(arg0)

   **Signature:** ``setOutlineVisible(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: setTitle(arg0)

   Sets the plot display title.

   **Signature:** ``setTitle(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the new title

   **Returns:** ``None``

.. method:: setXrange(arg0, arg1)

   Sets a manual range for the viewers' X-axis. Calling setXrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setXrange(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the lower-limit for the X-axis
   * **arg1** (``float``)

   **Returns:** ``None``

.. method:: setYrange(arg0, arg1)

   Sets a manual range for the viewers' Y-axis. Calling setYrange(-1, -1) enables auto-range (the default). Must be called before Viewer is fully assembled.

   **Signature:** ``setYrange(double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the lower-limit for the Y-axis
   * **arg1** (``float``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: addColorBarLegend(arg0)

   Adds a color bar legend (LUT ramp).

   **Signature:** ``addColorBarLegend(ColorMapper) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the color table

   **Returns:** ``None``

.. method:: addLabel(arg0)

   Adds an annotation label to the scene.

   **Signature:** ``addLabel(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the annotation text

   **Returns:** ``None``

.. method:: addMesh(arg0)

   Loads a Wavefront .OBJ file. Should be called before_ displaying the scene, otherwise, if the scene is already visible, validate() should be called to ensure all meshes are visible.

   **Signature:** ``addMesh(OBJMesh) -> boolean``

   **Parameters:**

   * **arg0** (``Any``): - the mesh to be loaded

   **Returns:** (``bool``) true, if successful

.. method:: addTree(arg0)

   Adds a tree to this viewer. Note that calling updateView() may be required to ensure that the current View's bounding box includes the added Tree.

   **Signature:** ``addTree(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree to be added. The Tree's label will be used as identifier. It is expected to be unique when rendering multiple Trees, if not (or no label exists) a unique label will be generated.

   **Returns:** ``None``


WekaModelLoader
---------------

.. method:: addInput(arg0, arg1)

   **Signature:** ``addInput(String, Class) -> MutableModuleItem``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``type``)

   **Returns:** ``Any``

.. method:: addOutput(arg0)

   **Signature:** ``addOutput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: removeInput(arg0)

   **Signature:** ``removeInput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: removeOutput(arg0)

   **Signature:** ``removeOutput(ModuleItem) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setContext(arg0)

   **Signature:** ``setContext(Context) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: setInput(arg0, arg1)

   **Signature:** ``setInput(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setInputs(arg0)

   **Signature:** ``setInputs(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: setOutput(arg0, arg1)

   **Signature:** ``setOutput(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: setOutputs(arg0)

   **Signature:** ``setOutputs(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: setResolved(arg0, arg1)

   **Signature:** ``setResolved(String, boolean) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``bool``)

   **Returns:** ``None``


----

*Category index generated on 2026-09-27 22:17:09*