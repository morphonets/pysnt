Utilities Methods
=================

General utility methods and helper functions.

Total methods in this category: **324**

.. contents:: Classes in this Category
   :local:

AllenCompartment
----------------

.. method:: acronym()

   **Signature:** ``acronym() -> String``

   **Returns:** (``str``) the compartment's acronym

.. method:: aliases()

   **Signature:** ``aliases() -> String;``

   **Returns:** (``Any``) the compartment's alias(es)

.. method:: id()

   **Signature:** ``id() -> int``

   **Returns:** (``int``) the compartment's unique id

.. method:: includes(arg0)

   **Signature:** ``includes(BrainAnnotation) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: name()

   **Signature:** ``name() -> String``

   **Returns:** (``str``) the compartment's name


BiSearch
--------

.. method:: pointsConsideredInSearch()

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(arg0)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


BiSearchNode
------------

.. method:: heapDecreaseKey(arg0)

   **Signature:** ``heapDecreaseKey(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: heapInsert(arg0, arg1)

   **Signature:** ``heapInsert(AddressableHeap, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``


BoundingBox
-----------

.. method:: append(arg0)

   Computes the bounding box of the specified point cloud and appends it to this bounding box, resizing it as needed.

   **Signature:** ``append(Iterator) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the iterator of the points Collection

   **Returns:** ``None``

.. method:: clone()

   Creates a copy of this BoundingBox.

   **Signature:** ``clone() -> BoundingBox``

   **Returns:** (``BoundingBox``) a new BoundingBox that is a copy of this bounding box

.. method:: combine(arg0)

   Combines this bounding box with another one. It is assumed both boxes share the same voxel spacing/Calibration.

   **Signature:** ``combine(BoundingBox) -> void``

   **Parameters:**

   * **arg0** (``BoundingBox``): - the bounding box to be combined.

   **Returns:** ``None``

.. method:: contains(arg0)

   **Signature:** ``contains(BoundingBox) -> boolean``

   **Parameters:**

   * **arg0** (``BoundingBox``)

   **Returns:** ``bool``

.. method:: contains2D(arg0)

   **Signature:** ``contains2D(SNTPoint) -> boolean``

   **Parameters:**

   * **arg0** (``SNTPoint``)

   **Returns:** ``bool``

.. method:: depth()

   **Signature:** ``depth() -> double``

   **Returns:** ``float``

.. method:: height()

   **Signature:** ``height() -> double``

   **Returns:** ``float``

.. method:: inferSpacing(arg0)

   Infers the voxel spacing of this box from the inter-node distances of a Collection of SWCPoints.

   **Signature:** ``inferSpacing(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - the point collection

   **Returns:** ``None``

.. method:: intersection(arg0)

   Retrieves the intersection cuboid between this bounding with another bounding box. It is assumed both boxes share the same voxel spacing/Calibration.

   **Signature:** ``intersection(BoundingBox) -> BoundingBox``

   **Parameters:**

   * **arg0** (``BoundingBox``): - the second bounding box.

   **Returns:** (``BoundingBox``) The intersection cuboid.

.. method:: origin()

   Retrieves the origin of this box.

   **Signature:** ``origin() -> PointInImage``

   **Returns:** (``PointInImage``) the origin

.. method:: originOpposite()

   Retrieves the origin opposite of this box.

   **Signature:** ``originOpposite() -> PointInImage``

   **Returns:** (``PointInImage``) the origin

.. method:: toBoundingBox3d()

   **Signature:** ``toBoundingBox3d() -> BoundingBox3d``

   **Returns:** ``Any``

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


ConvexHull2D
------------

.. method:: intersection(arg0)

   **Signature:** ``intersection(AbstractConvexHull;) -> AbstractConvexHull``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: intersectionBox(arg0)

   **Signature:** ``intersectionBox(AbstractConvexHull;) -> BoundingBox``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``BoundingBox``


ConvexHull3D
------------

.. method:: intersection(arg0)

   **Signature:** ``intersection(AbstractConvexHull;) -> ConvexHull3D``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``ConvexHull3D``

.. method:: intersectionBox(arg0)

   **Signature:** ``intersectionBox(AbstractConvexHull;) -> BoundingBox``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``BoundingBox``


ConvexHullAnalyzer
------------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: dump(arg0)

   **Signature:** ``dump(SNTTable) -> void``

   **Parameters:**

   * **arg0** (``SNTTable``)

   **Returns:** ``None``

.. method:: get(arg0)

   Gets the value of a specific convex hull metric.

Retrieves the computed value for the specified metric name. The metric must be one of the supported metrics returned by supportedMetrics().

   **Signature:** ``get(String) -> double``

   **Parameters:**

   * **arg0** (``str``): - the name of the metric to retrieve

   **Returns:** (``float``) the computed value for the metric

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


DefaultSearchNode
-----------------

.. method:: compareTo(arg0)

   **Signature:** ``compareTo(DefaultSearchNode) -> int``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``int``


Fill
----

.. method:: add(arg0, arg1, arg2, arg3, arg4, arg5)

   Adds a node to the filled structure.

   **Signature:** ``add(int, int, int, double, int, boolean) -> void``

   **Parameters:**

   * **arg0** (``int``): - the x-coordinate of the node
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``float``)
   * **arg4** (``int``)
   * **arg5** (``bool``)

   **Returns:** ``None``


FillConverter
-------------

.. method:: convert(arg0, arg1)

   Map values between the input and output at fill voxel positions.

   **Signature:** ``convert(RandomAccessible, RandomAccessible) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the input rai
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: convertBinary(arg0)

   Set 1 at fill voxel positions.

   **Signature:** ``convertBinary(RandomAccessible) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the output rai

   **Returns:** ``None``

.. method:: convertDistance(arg0)

   Map the node distance measure to fill voxel positions. This corresponds to the g-score of a node assigned during the Dijkstra search. This value is stored as Double.

   **Signature:** ``convertDistance(RandomAccessible) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the output rai

   **Returns:** ``None``

.. method:: convertLabels(arg0)

   Map the fill component label to fill voxel positions. The concrete IntegerType should be chosen based on the cardinality of the given Collection of FillerThreads. For example, if there are less than 256 FillerThreads, choose UnsignedByteType. If there are more than 255 but less than 65536, choose UnsignedShortType, etc. Fill components are assigned labels based on their order in the collection. If you want to ensure labels are assigned based on insertion order, make sure to use an ordered collection such as List or LinkedHashSet. The first component will have label == 1, the second label == 2, and so on. The label 0 is not assigned to any voxel positions. 0-valued voxels may already exist in the output image.

   **Signature:** ``convertLabels(RandomAccessible) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the output rai

   **Returns:** ``None``


FillerThread
------------

.. method:: createNewNode(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

   **Signature:** ``createNewNode(int, int, int, double, double, DefaultSearchNode, byte) -> DefaultSearchNode``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``float``)
   * **arg4** (``float``)
   * **arg5** (``Any``)
   * **arg6** (``int``)

   **Returns:** ``Any``

.. method:: pointsConsideredInSearch()

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(arg0)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


GroupedTreeStatistics
---------------------

.. method:: anovaPValue(arg0)

   Computes the one-way ANOVA P-value for all the groups being analyzed. It is assumed that data fulfills basic assumptions on normality, variance homogeneity, sample size, etc.

   **Signature:** ``anovaPValue(String) -> double``

   **Parameters:**

   * **arg0** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``float``) the p-value

.. method:: tTest(arg0, arg1, arg2)

   Computes a two-sample, two-tailed t-test P-value for two of groups being analyzed. It is assumed that data fulfills basic assumptions on normality, variance homogeneity, etc.

   **Signature:** ``tTest(String, String, String) -> double``

   **Parameters:**

   * **arg0** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** (``float``) the p-value


InsectBrainCompartment
----------------------

.. method:: acronym()

   **Signature:** ``acronym() -> String``

   **Returns:** (``str``) the compartment's acronym

.. method:: aliases()

   **Signature:** ``aliases() -> String;``

   **Returns:** (``Any``) the compartment's alias(es)

.. method:: id()

   **Signature:** ``id() -> int``

   **Returns:** (``int``) the compartment's unique id

.. method:: name()

   **Signature:** ``name() -> String``

   **Returns:** (``str``) the compartment's name


InsectBrainLoader
-----------------

.. method:: idExists()

   Checks whether the neuron to be loaded was found in the database.

   **Signature:** ``idExists() -> boolean``

   **Returns:** (``bool``) true, if the neuron id specified in the constructor was found in the database


InteractiveTracerCanvas
-----------------------

.. method:: action(arg0, arg1)

   **Signature:** ``action(Event, Object) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: add(arg0)

   **Signature:** ``add(PopupMenu) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: applyComponentOrientation(arg0)

   **Signature:** ``applyComponentOrientation(ComponentOrientation) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: areFocusTraversalKeysSet(arg0)

   **Signature:** ``areFocusTraversalKeysSet(int) -> boolean``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``bool``

.. method:: bounds()

   **Signature:** ``bounds() -> Rectangle``

   **Returns:** ``Any``

.. method:: checkImage(arg0, arg1, arg2, arg3)

   **Signature:** ``checkImage(Image, int, int, ImageObserver) -> int``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``int``

.. method:: contains(arg0)

   **Signature:** ``contains(Point) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: createBufferStrategy(arg0)

   **Signature:** ``createBufferStrategy(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: createImage(arg0)

   **Signature:** ``createImage(ImageProducer) -> Image``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: createVolatileImage(arg0, arg1)

   **Signature:** ``createVolatileImage(int, int) -> VolatileImage``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: cursorOverImage()

   **Signature:** ``cursorOverImage() -> boolean``

   **Returns:** ``bool``

.. method:: deliverEvent(arg0)

   **Signature:** ``deliverEvent(Event) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disable()

   **Signature:** ``disable() -> void``

   **Returns:** ``None``

.. method:: dispatchEvent(arg0)

   **Signature:** ``dispatchEvent(AWTEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: doLayout()

   **Signature:** ``doLayout() -> void``

   **Returns:** ``None``

.. method:: enable(arg0)

   **Signature:** ``enable(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: firePropertyChange(arg0, arg1, arg2)

   **Signature:** ``firePropertyChange(String, char, char) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: fitToWindow()

   **Signature:** ``fitToWindow() -> void``

   **Returns:** ``None``


MouseLightLoader
----------------

.. method:: idExists()

   Checks if the neuron ID exists in the database.

   **Signature:** ``idExists() -> boolean``

   **Returns:** (``bool``) true if the ID exists, false otherwise

.. method:: save(arg0)

   Convenience method to save JSON data.

   **Signature:** ``save(File) -> boolean``

   **Parameters:**

   * **arg0** (``str``): - the output directory or the output file

   **Returns:** (``bool``) true, if successful


MultiTreeColorMapper
--------------------

.. method:: map(arg0, arg1)

   Description copied from class: ColorMapper

   **Signature:** ``map(String, ColorTable) -> void``

   **Parameters:**

   * **arg0** (``str``): - the measurement to be mapped
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: mapRootDistanceToCentroid(arg0, arg1)

   **Signature:** ``mapRootDistanceToCentroid(AllenCompartment, ColorTable) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: mapTrees(arg0, arg1)

   **Signature:** ``mapTrees(List, String) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: sortedMappedTrees()

   **Signature:** ``sortedMappedTrees() -> List``

   **Returns:** ``List[Any]``


MultiTreeStatistics
-------------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: dispose()

   Description copied from class: TreeStatistics

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``


MultiViewer2D
-------------

.. method:: save(arg0)

   **Signature:** ``save(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: show()

   **Signature:** ``show() -> JFrame``

   **Returns:** ``Any``


MultiViewer3D
-------------

.. method:: show()

   **Signature:** ``show() -> JFrame``

   **Returns:** ``Any``


NodeColorMapper
---------------

.. method:: map(arg0, arg1)

   Maps nodes after the specified measurement. Mapping bounds are automatically determined.

   **Signature:** ``map(String, String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the measurement (X_COORDINATES, Y_COORDINATES, etc.)
   * **arg1** (``str``)

   **Returns:** ``None``


NodeProfiler
------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: initialize()

   **Signature:** ``initialize() -> void``

   **Returns:** ``None``

.. method:: resolveInput(arg0)

   **Signature:** ``resolveInput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: resolveOutput(arg0)

   **Signature:** ``resolveOutput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: uncancel()

   **Signature:** ``uncancel() -> void``

   **Returns:** ``None``

.. method:: unresolveInput(arg0)

   **Signature:** ``unresolveInput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: unresolveOutput(arg0)

   **Signature:** ``unresolveOutput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``


NodeStatistics
--------------

.. method:: assignBranches(arg0)

   Associates the nodes being analyzed to the branches of the specified tree

   **Signature:** ``assignBranches(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the association tree

   **Returns:** ``None``

.. method:: filter(arg0, arg1, arg2)

   Filters the current pool of nodes matching a measurement-based criterion.

   **Signature:** ``filter(String, double, double) -> List``

   **Parameters:**

   * **arg0** (``str``): - the measurement (X_COORDINATES, Y_COORDINATES, BRANCH_ORDER, etc.)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** (``List[Any]``) the filtered list.

.. method:: get(arg0, arg1)

   Gets the list of nodes associated with the specified compartment (neuropil label).

   **Signature:** ``get(BrainAnnotation, boolean) -> List``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``List[Any]``


Path
----

.. method:: add(arg0)

   **Signature:** ``add(Path) -> void``

   **Parameters:**

   * **arg0** (``Path``)

   **Returns:** ``None``

.. method:: clone(arg0)

   Creates a copy of this Path with optional inclusion of immediate children.

This method creates a clone of this path and optionally includes clones of its immediate child paths. When children are included, they are properly reconnected to the cloned parent path, maintaining the parent-child relationships. Note that only immediate children are cloned - grandchildren and deeper descendants are not included.

Limitations: This method only clones the immediate children and does not recursively clone the entire subtree. For complex tree structures, consider using Tree.clone() instead.

   **Signature:** ``clone(boolean) -> Path``

   **Parameters:**

   * **arg0** (``bool``): - if true, includes clones of immediate child paths; if false, returns a clone without children

   **Returns:** (``Path``) a new Path that is a copy of this path, optionally including children

.. method:: compareTo(arg0)

   **Signature:** ``compareTo(Object) -> int``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``int``

.. method:: contains(arg0)

   Checks if this path contains the specified point within the given tolerance.

   **Signature:** ``contains(PointInImage) -> boolean``

   **Parameters:**

   * **arg0** (``PointInImage``): - the point to check

   **Returns:** (``bool``) true if the path contains the point within tolerance

.. method:: detachFromParent()

   Detaches this path from its parent, converting it into an independent primary path.

Removes the parent-child relationship established by `setBranchFrom(Path, PointInImage)` In

Clears the parent path reference and branch point Removes this path from the parent's children collection Updates bidirectional references for tree traversal Resets the path order to -1 (no hierarchical position) Converts this path from a branch to a primary path

   **Signature:** ``detachFromParent() -> void``

   **Returns:** ``None``

.. method:: downsample(arg0)

   Downsamples this path (in-place) by reducing the number of nodes while preserving its overall shape.

This method reduces the density of nodes in the path by removing redundant points expected to not significantly contribute to the path's shape. The downsampling is performed using the Douglas-Peucker algorithm, which preserves fidelity within the specified tolerance.

The method operates on the segments flanked by anchor points (junctions, start, and end points). Each segment is downsampled independently, and the results are combined to form the final downsampled path. Node radii are averaged appropriately for retained points

Thread Safety: This method is synchronized to prevent concurrent modification of the path structure during the downsampling operation.

   **Signature:** ``downsample(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the target spacing between nodes after downsampling. This parameter controls the aggressiveness of the downsampling - smaller values preserve more detail, larger values result in more aggressive simplification. Must be greater than zero.

   **Returns:** ``None``

.. method:: findJunctionIndices()

   Returns the indices of nodes which are indicated to be a join, either in this Path object, or any other that starts or ends on it.

   **Signature:** ``findJunctionIndices() -> TreeSet``

   **Returns:** (``Set[Any]``) the indices of junction nodes, naturally sorted

.. method:: findJunctions()

   Returns the nodes which are indicated to be a join (junction/branch point), either in this Path object, or any other that starts or ends on it.

   **Signature:** ``findJunctions() -> List``

   **Returns:** (``List[Any]``) the list of nodes as PointInImage objects

.. method:: firstNode()

   Returns the first node of this path.

   **Signature:** ``firstNode() -> PointInImage``

   **Returns:** (``PointInImage``) the root node, or null if path is empty


PathAndFillManager
------------------

.. method:: allPointsIterator()

   **Signature:** ``allPointsIterator() -> Iterator``

   **Returns:** ``Any``

.. method:: anySelected()

   Checks whether at least one Path is currently selected in the UI.

   **Signature:** ``anySelected() -> boolean``

   **Returns:** (``bool``) true, if successful

.. method:: assignSpatialSettings(arg0)

   **Signature:** ``assignSpatialSettings(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: characters(arg0, arg1, arg2)

   **Signature:** ``characters([C, int, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``None``

.. method:: clear()

   Deletes all paths and fills.

   **Signature:** ``clear() -> void``

   **Returns:** ``None``

.. method:: declaration(arg0, arg1, arg2)

   **Signature:** ``declaration(String, String, String) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: downsampleAll(arg0)

   Downsamples alls path using Ramer–Douglas–Peucker simplification. Downsampling occurs only between branch points and terminal points.

   **Signature:** ``downsampleAll(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the maximum permitted distance between nodes.

   **Returns:** ``None``

.. method:: endDocument()

   **Signature:** ``endDocument() -> void``

   **Returns:** ``None``

.. method:: endElement(arg0, arg1, arg2)

   **Signature:** ``endElement(String, String, String) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: endPrefixMapping(arg0)

   Sets whether this PathAndFillManager instance should run headless.

   **Signature:** ``endPrefixMapping(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - true to activate headless calls, otherwise false

   **Returns:** ``None``

.. method:: error(arg0)

   **Signature:** ``error(SAXParseException) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: fatalError(arg0)

   **Signature:** ``fatalError(SAXParseException) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


PathFitter
----------

.. method:: applySettings(arg0)

   **Signature:** ``applySettings(PathFitter) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: call()

   Takes the signal from the image specified in the constructor to fit cross-section circles around the nodes of input path. Computation of fit is confined to the neighborhood specified by setMaxRadius(int). Note that connectivity of path may need to be rebuilt upon fit.

   **Signature:** ``call() -> Path``

   **Returns:** (``Path``) the reference to the computed result. This Path is automatically set as the fitted version of input Path.


PathManagerUI
-------------

.. method:: action(arg0, arg1)

   **Signature:** ``action(Event, Object) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: add(arg0, arg1, arg2)

   Runs a menu command with options.

   **Signature:** ``add(Component, Object, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``int``)

   **Returns:** ``None``

.. method:: applyComponentOrientation(arg0)

   **Signature:** ``applyComponentOrientation(ComponentOrientation) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: applyDefaultTags(arg0)

   Applies a default (built-in) tag to selected Path(s).

   **Signature:** ``applyDefaultTags(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``): - The tags to be applied to selected Paths, as listed in the "Tag" menu, e.g., "Traced Channel", "Traced Frame", "No. of Spine/Varicosity Markers", etc.

   **Returns:** ``None``

.. method:: applyResourceBundle(arg0)

   **Signature:** ``applyResourceBundle(ResourceBundle) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: applySelectionFilter(arg0, arg1, arg2)

   Selects paths matching a morphometric criteria.

   **Signature:** ``applySelectionFilter(String, Number, Number) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Union[int, float]``)
   * **arg2** (``Union[int, float]``)

   **Returns:** ``None``

.. method:: applyTag(arg0)

   Applies a custom tag/ color to selected Path(s).

   **Signature:** ``applyTag(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - The tag (or color) to be applied to selected Paths. Specifying "null color" will remove color tags from selected paths.

   **Returns:** ``None``

.. method:: areFocusTraversalKeysSet(arg0)

   **Signature:** ``areFocusTraversalKeysSet(int) -> boolean``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``bool``

.. method:: bounds()

   **Signature:** ``bounds() -> Rectangle``

   **Returns:** ``Any``

.. method:: checkImage(arg0, arg1, arg2, arg3)

   **Signature:** ``checkImage(Image, int, int, ImageObserver) -> int``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``int``

.. method:: contains(arg0)

   **Signature:** ``contains(Point) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: countComponents()

   **Signature:** ``countComponents() -> int``

   **Returns:** ``int``

.. method:: createBufferStrategy(arg0)

   **Signature:** ``createBufferStrategy(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: createImage(arg0)

   **Signature:** ``createImage(ImageProducer) -> Image``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: createVolatileImage(arg0, arg1)

   **Signature:** ``createVolatileImage(int, int) -> VolatileImage``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: deliverEvent(arg0)

   **Signature:** ``deliverEvent(Event) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disable()

   **Signature:** ``disable() -> void``

   **Returns:** ``None``

.. method:: dispatchEvent(arg0)

   **Signature:** ``dispatchEvent(AWTEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: doLayout()

   **Signature:** ``doLayout() -> void``

   **Returns:** ``None``


PathProfiler
------------

.. method:: assignValues(arg0)

   Retrieves pixel intensities at each node of the Path storing them as Path values

   **Signature:** ``assignValues(Path) -> void``

   **Parameters:**

   * **arg0** (``Path``): - the Path to be profiled

   **Returns:** ``None``

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: findMaxima(arg0, arg1)

   Finds the maxima in the profile of the specified path.

A maxima (peak) will only be considered if protruding more than the profile's standard deviation from the ridge to a higher maximum

   **Signature:** ``findMaxima(Path, int) -> [I``

   **Parameters:**

   * **arg0** (``Path``): - the channel to be parsed (base-0 index)
   * **arg1** (``int``)

   **Returns:** (``Any``) the indices of the maxima

.. method:: findMinima(arg0, arg1)

   Finds the minima in the profile of the specified path.

A maxima (peak) will only be considered if protruding less than the profile's standard deviation from the ridge to a lower minimum

   **Signature:** ``findMinima(Path, int) -> [I``

   **Parameters:**

   * **arg0** (``Path``): - the channel to be parsed (base-0 index)
   * **arg1** (``int``)

   **Returns:** (``Any``) the indices of the minima

.. method:: initialize()

   **Signature:** ``initialize() -> void``

   **Returns:** ``None``

.. method:: resolveInput(arg0)

   **Signature:** ``resolveInput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: resolveOutput(arg0)

   **Signature:** ``resolveOutput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


PathStatistics
--------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``


PathStraightener
----------------

.. method:: straighten(arg0)

   **Signature:** ``straighten(int) -> ImageProcessor``

   **Parameters:**

   * **arg0** (``int``): - the channel to bes straightened

   **Returns:** (``Any``) the straightened path for the specified channel as an ImageProcessor object


PointInImage
------------

.. method:: chebyshevDxTo(arg0)

   **Signature:** ``chebyshevDxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevXYdxTo(arg0)

   **Signature:** ``chebyshevXYdxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevZdxTo(arg0)

   **Signature:** ``chebyshevZdxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: clone()

   Creates a copy of this PointInImage.

This method creates a copy of the point including all properties such as coordinates, value, annotation, and hemisphere information.

   **Signature:** ``clone() -> PointInImage``

   **Returns:** (``PointInImage``) a new PointInImage that is a copy of this point

.. method:: distanceSquaredTo(arg0)

   **Signature:** ``distanceSquaredTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: distanceTo(arg0)

   **Signature:** ``distanceTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: euclideanDxTo(arg0)

   **Signature:** ``euclideanDxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: scale(arg0, arg1, arg2)

   Scales this point coordinates.

   **Signature:** ``scale(double, double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the scaling factor for x coordinates
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: transform(arg0)

   **Signature:** ``transform(PathTransformer) -> PointInImage``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``PointInImage``


RootAngleAnalyzer
-----------------

.. method:: balancingFactor()

   Returns the balancing factor, computed from centripetalBias().

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


SNT
---

.. method:: accessToValidImageData()

   **Signature:** ``accessToValidImageData() -> boolean``

   **Returns:** ``bool``

.. method:: autoTrace(arg0, arg1, arg2, arg3)

   Automatically traces a path from a point A to a point B. See `autoTrace(List, PointInImage)` for details.

   **Signature:** ``autoTrace(SNTPoint, SNTPoint, PointInImage, boolean) -> Path``

   **Parameters:**

   * **arg0** (``SNTPoint``)
   * **arg1** (``SNTPoint``)
   * **arg2** (``PointInImage``)
   * **arg3** (``bool``)

   **Returns:** ``Path``

.. method:: changeUIState(arg0)

   **Signature:** ``changeUIState(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: closeAndResetAllPanes()

   **Signature:** ``closeAndResetAllPanes() -> void``

   **Returns:** ``None``

.. method:: confirmTemporary(arg0)

   **Signature:** ``confirmTemporary(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: createCanvas(arg0, arg1)

   **Signature:** ``createCanvas(ImagePlus, int) -> InteractiveTracerCanvas``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: editModeAllowed()

   Assesses if activation of 'Edit Mode' is possible.

   **Signature:** ``editModeAllowed() -> boolean``

   **Returns:** (``bool``) true, if possible, false otherwise

.. method:: findPointInStack(arg0, arg1, arg2, arg3)

   **Signature:** ``findPointInStack(int, int, int, [I) -> void``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``None``

.. method:: findPointInStackPrecise(arg0, arg1, arg2, arg3)

   **Signature:** ``findPointInStackPrecise(double, double, int, [D) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``None``

.. method:: finished(arg0, arg1)

   **Signature:** ``finished(SearchInterface, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: flushSecondaryData()

   **Signature:** ``flushSecondaryData() -> void``

   **Returns:** ``None``


SNTChart
--------

.. method:: action(arg0, arg1)

   **Signature:** ``action(Event, Object) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: actionPerformed(arg0)

   Shows a bivariate histogram (two-dimensional histogram) from two DescriptiveStatistics objects. The number of bins is automatically determined using the Freedman-Diaconis rule.

   **Signature:** ``actionPerformed(ActionEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``): - DescriptiveStatistics for the first distribution

   **Returns:** ``None``

.. method:: add(arg0, arg1, arg2)

   **Signature:** ``add(Component, Object, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``int``)

   **Returns:** ``None``

.. method:: annotate(arg0, arg1, arg2)

   Adds a subtitle to the chart.

   **Signature:** ``annotate(String, String, String) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: annotateCategory(arg0, arg1, arg2)

   Annotates the specified category (Category plots only).

   **Signature:** ``annotateCategory(String, String, String) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: annotatePoint(arg0, arg1, arg2)

   Highlights a point in a histogram/XY plot by drawing a labeled arrow at the specified location.

   **Signature:** ``annotatePoint([D, String, String) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the array holding the focal point coordinates of the profile
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: annotateXline(arg0, arg1)

   Annotates the specified X-value (XY plots and histograms).

   **Signature:** ``annotateXline(double, String) -> void``

   **Parameters:**

   * **arg0** (``float``): - the X value to be annotated.
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: annotateYline(arg0, arg1, arg2)

   Annotates the specified Y-value (XY plots and histograms).

   **Signature:** ``annotateYline(double, String, String) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: applyComponentOrientation(arg0)

   **Signature:** ``applyComponentOrientation(ComponentOrientation) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: applyStyle(arg0)

   **Signature:** ``applyStyle(SNTChart) -> void``

   **Parameters:**

   * **arg0** (``SNTChart``)

   **Returns:** ``None``

.. method:: areFocusTraversalKeysSet(arg0)

   Saves this chart.

   **Signature:** ``areFocusTraversalKeysSet(int) -> boolean``

   **Parameters:**

   * **arg0** (``int``): - the path of the output file (null not permitted). Its filename extension (".svg", ".png", ".pdf"), determines the file format.

   **Returns:** (``bool``) true if file was successfully saved, false otherwise

.. method:: bounds()

   **Signature:** ``bounds() -> Rectangle``

   **Returns:** ``Any``

.. method:: chartChanged(arg0)

   **Signature:** ``chartChanged(ChartChangeEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: chartProgress(arg0)

   **Signature:** ``chartProgress(ChartProgressEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: checkImage(arg0, arg1, arg2, arg3)

   **Signature:** ``checkImage(Image, int, int, ImageObserver) -> int``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``int``


SNTColor
--------

.. method:: type()

   Retrieves the SWC type

   **Signature:** ``type() -> int``

   **Returns:** (``int``) the SWC type integer flag


SNTService
----------

.. method:: assignValues(arg0)

   Assigns pixel intensities at each Path node, storing them as Path values. Assigned intensities are those of the channel and time point currently being traced. Assumes SNT has been initialized with a valid image.

   **Signature:** ``assignValues(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - If true, only selected paths will be assigned values, otherwise voxel intensities will be assigned to all paths

   **Returns:** ``None``

.. method:: compareTo(arg0)

   **Signature:** ``compareTo(Object) -> int``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``int``

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: demoImage(arg0)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.

   **Signature:** ``demoImage(String) -> ImagePlus``

   **Parameters:**

   * **arg0** (``str``): - a string describing the type of demo image. Options include: 'fractal' for the L-system toy neuron; 'ddaC' for the C4 ddaC drosophila neuron (demo image initially distributed with the Sholl plugin); 'OP1'/'OP_1' for the DIADEM OP_1 dataset; 'cil701' and 'cil810' for the respective Cell Image Library entries, and 'binary timelapse' for a small 4-frame sequence of neurite growth

   **Returns:** (``Any``) the demo image, or null if data could no be retrieved

.. method:: demoTree(arg0)

   Returns a demo tree.

   **Signature:** ``demoTree(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - a string describing the type of demo tree. Either 'fractal' for the L-system toy neuron, 'pyramidal' for the dendritic arbor of mouse pyramidal cell (MouseLight's cell AA0001), 'OP1'for the DIADEM OP_1 reconstruction, or 'DG' for the dentate gyrus granule cell (Neuromorpho's Beining archive)

   **Returns:** ``Tree``

.. method:: demoTrees()

   Returns a collection of four demo reconstructions (dendrites from pyramidal cells from the MouseLight database). NB: Data is cached locally. No internet connection required.

   **Signature:** ``demoTrees() -> List``

   **Returns:** (``List[Any]``) the list of Trees, corresponding to the dendritic arbors of cells "AA0001", "AA0002", "AA0003", "AA0004" (MouseLight database IDs).

.. method:: dispose()

   Quits SNT. Does nothing if SNT is currently not running.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: initialize(arg0, arg1)

   Initializes SNT.

   **Signature:** ``initialize(ImagePlus, boolean) -> SNT``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``Any``

.. method:: log()

   **Signature:** ``log() -> LogService``

   **Returns:** ``Any``

.. method:: registerEventHandlers()

   **Signature:** ``registerEventHandlers() -> void``

   **Returns:** ``None``

.. method:: save(arg0)

   Saves all the existing paths to a file.

   **Signature:** ``save(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``): - the saving output file path. If

   **Returns:** (``bool``) true, if paths exist and file was successfully written.


SNTTable
--------

.. method:: add(arg0)

   **Signature:** ``add(Column) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: appendColumn(arg0)

   **Signature:** ``appendColumn(String) -> Column``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: appendColumns(arg0)

   **Signature:** ``appendColumns(int) -> List``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``List[Any]``

.. method:: appendRow(arg0)

   **Signature:** ``appendRow(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: appendRows(arg0)

   **Signature:** ``appendRows(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: appendToLastRow(arg0, arg1)

   Appends a value to the last row in the specified column.

If the table is empty, a new row is created first. The value is then set in the specified column of the last row.

   **Signature:** ``appendToLastRow(String, Object) -> void``

   **Parameters:**

   * **arg0** (``str``): - the column header
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: clear()

   **Signature:** ``clear() -> void``

   **Returns:** ``None``

.. method:: clone()

   **Signature:** ``clone() -> Object``

   **Returns:** ``Any``

.. method:: contains(arg0)

   **Signature:** ``contains(Object) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: containsAll(arg0)

   **Signature:** ``containsAll(Collection) -> boolean``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``bool``

.. method:: createOrUpdateDisplay()

   Creates a new display or updates an existing one.

If no display exists, creates a new table display window. If a display already exists, updates it with the current table contents.

   **Signature:** ``createOrUpdateDisplay() -> void``

   **Returns:** ``None``

.. method:: ensureCapacity(arg0)

   **Signature:** ``ensureCapacity(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: fillEmptyCells(arg0)

   Fills all empty cells in the table with the specified value.

Iterates through all cells in the table and replaces null values with the provided replacement value.

   **Signature:** ``fillEmptyCells(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the value to use for filling empty cells

   **Returns:** ``None``

.. method:: forEach(arg0)

   **Signature:** ``forEach(Consumer) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: geColumnHeaders(arg0)

   **Signature:** ``geColumnHeaders(String) -> List``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``List[Any]``

.. method:: geColumnStats(arg0, arg1, arg2)

   **Signature:** ``geColumnStats(String, int, int) -> SummaryStatistics``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``Any``

.. method:: geRowStats(arg0, arg1, arg2)

   **Signature:** ``geRowStats(int, int, int) -> SummaryStatistics``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``Any``

.. method:: get(arg0)

   **Signature:** ``get(int) -> Column``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Any``


SNTUI
-----

.. method:: action(arg0, arg1)

   **Signature:** ``action(Event, Object) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: add(arg0, arg1, arg2)

   Updates the status bar.

   **Signature:** ``add(Component, Object, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``int``)

   **Returns:** ``None``

.. method:: applyComponentOrientation(arg0)

   **Signature:** ``applyComponentOrientation(ComponentOrientation) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: applyResourceBundle(arg0)

   **Signature:** ``applyResourceBundle(ResourceBundle) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: areFocusTraversalKeysSet(arg0)

   **Signature:** ``areFocusTraversalKeysSet(int) -> boolean``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``bool``

.. method:: bounds()

   **Signature:** ``bounds() -> Rectangle``

   **Returns:** ``Any``

.. method:: changeState(arg0)

   Changes this UI to a new state. Does nothing if newState is the current UI state

   **Signature:** ``changeState(int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the new state, e.g., READY, TRACING_PAUSED, etc.

   **Returns:** ``None``

.. method:: checkImage(arg0, arg1, arg2, arg3)

   **Signature:** ``checkImage(Image, int, int, ImageObserver) -> int``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``int``

.. method:: contains(arg0)

   **Signature:** ``contains(Point) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: countComponents()

   Gets the current UI state.

   **Signature:** ``countComponents() -> int``

   **Returns:** (``int``) the current UI state, e.g., READY, RUNNING_CMD, etc.

.. method:: createBufferStrategy(arg0)

   **Signature:** ``createBufferStrategy(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: createImage(arg0)

   **Signature:** ``createImage(ImageProducer) -> Image``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: createVolatileImage(arg0, arg1)

   **Signature:** ``createVolatileImage(int, int) -> VolatileImage``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: deliverEvent(arg0)

   **Signature:** ``deliverEvent(Event) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disable()

   **Signature:** ``disable() -> void``

   **Returns:** ``None``

.. method:: dispatchEvent(arg0)

   **Signature:** ``dispatchEvent(AWTEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: dispose()

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: doLayout()

   **Signature:** ``doLayout() -> void``

   **Returns:** ``None``

.. method:: enable(arg0)

   **Signature:** ``enable(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: error(arg0)

   **Signature:** ``error(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: findComponentAt(arg0, arg1)

   **Signature:** ``findComponentAt(int, int) -> Component``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``Any``


SWCPoint
--------

.. method:: chebyshevDxTo(arg0)

   **Signature:** ``chebyshevDxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevXYdxTo(arg0)

   **Signature:** ``chebyshevXYdxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: chebyshevZdxTo(arg0)

   **Signature:** ``chebyshevZdxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: clone()

   **Signature:** ``clone() -> PointInImage``

   **Returns:** ``PointInImage``

.. method:: compareTo(arg0)

   **Signature:** ``compareTo(Object) -> int``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``int``

.. method:: distanceSquaredTo(arg0)

   **Signature:** ``distanceSquaredTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: distanceTo(arg0)

   **Signature:** ``distanceTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: euclideanDxTo(arg0)

   **Signature:** ``euclideanDxTo(PointInImage) -> double``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``float``

.. method:: previous()

   Returns the preceding node (if any)

   **Signature:** ``previous() -> SWCPoint``

   **Returns:** (``SWCPoint``) the previous node or null if set by `setPrevious(SWCPoint)` has not been called

.. method:: scale(arg0, arg1, arg2)

   **Signature:** ``scale(double, double, double) -> void``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: transform(arg0)

   **Signature:** ``transform(PathTransformer) -> PointInImage``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``PointInImage``

.. method:: xSeparationFromPreviousPoint()

   Returns the X-distance from previous point.

   **Signature:** ``xSeparationFromPreviousPoint() -> double``

   **Returns:** (``float``) the X-distance from previous point or Double.NaN if no previousPoint exists.

.. method:: ySeparationFromPreviousPoint()

   Returns the Y-distance from previous point.

   **Signature:** ``ySeparationFromPreviousPoint() -> double``

   **Returns:** (``float``) the Y-distance from previous point or Double.NaN if no previousPoint exists.

.. method:: zSeparationFromPreviousPoint()

   Returns the Z-distance from previous point.

   **Signature:** ``zSeparationFromPreviousPoint() -> double``

   **Returns:** (``float``) the Z-distance from previous point or Double.NaN if no previousPoint exists.


SearchThread
------------

.. method:: createNewNode(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

   **Signature:** ``createNewNode(int, int, int, double, double, DefaultSearchNode, byte) -> DefaultSearchNode``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``float``)
   * **arg4** (``float``)
   * **arg5** (``Any``)
   * **arg6** (``int``)

   **Returns:** ``Any``

.. method:: pointsConsideredInSearch()

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(arg0)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


StrahlerAnalyzer
----------------

.. method:: dispose()

   Clears internal caches and mappings to free memory.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``


TracerCanvas
------------

.. method:: action(arg0, arg1)

   **Signature:** ``action(Event, Object) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: add(arg0)

   **Signature:** ``add(PopupMenu) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: applyComponentOrientation(arg0)

   **Signature:** ``applyComponentOrientation(ComponentOrientation) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: areFocusTraversalKeysSet(arg0)

   **Signature:** ``areFocusTraversalKeysSet(int) -> boolean``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``bool``

.. method:: bounds()

   **Signature:** ``bounds() -> Rectangle``

   **Returns:** ``Any``

.. method:: checkImage(arg0, arg1, arg2, arg3)

   **Signature:** ``checkImage(Image, int, int, ImageObserver) -> int``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``Any``)

   **Returns:** ``int``

.. method:: contains(arg0)

   **Signature:** ``contains(Point) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: createBufferStrategy(arg0)

   **Signature:** ``createBufferStrategy(int) -> void``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``None``

.. method:: createImage(arg0)

   **Signature:** ``createImage(ImageProducer) -> Image``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: createVolatileImage(arg0, arg1)

   **Signature:** ``createVolatileImage(int, int) -> VolatileImage``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: cursorOverImage()

   **Signature:** ``cursorOverImage() -> boolean``

   **Returns:** ``bool``

.. method:: deliverEvent(arg0)

   **Signature:** ``deliverEvent(Event) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: disable()

   **Signature:** ``disable() -> void``

   **Returns:** ``None``

.. method:: dispatchEvent(arg0)

   **Signature:** ``dispatchEvent(AWTEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: doLayout()

   **Signature:** ``doLayout() -> void``

   **Returns:** ``None``

.. method:: enable(arg0)

   **Signature:** ``enable(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: firePropertyChange(arg0, arg1, arg2)

   **Signature:** ``firePropertyChange(String, char, char) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: fitToWindow()

   **Signature:** ``fitToWindow() -> void``

   **Returns:** ``None``


TracerThread
------------

.. method:: createNewNode(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

   **Signature:** ``createNewNode(int, int, int, double, double, DefaultSearchNode, byte) -> DefaultSearchNode``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``float``)
   * **arg4** (``float``)
   * **arg5** (``Any``)
   * **arg6** (``int``)

   **Returns:** ``Any``

.. method:: pointsConsideredInSearch()

   **Signature:** ``pointsConsideredInSearch() -> long``

   **Returns:** ``int``

.. method:: printStatus()

   **Signature:** ``printStatus() -> void``

   **Returns:** ``None``

.. method:: reportFinished(arg0)

   **Signature:** ``reportFinished(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``


Tree
----

.. method:: add(arg0)

   Adds a new Path to this Tree.

   **Signature:** ``add(Path) -> boolean``

   **Parameters:**

   * **arg0** (``Path``): - the Path to be added

   **Returns:** (``bool``) true, if Path successful added

.. method:: applyCanvasOffset(arg0, arg1, arg2)

   Specifies the offset to be used when rendering this Tree in a TracerCanvas. Path coordinates remain unaltered.

   **Signature:** ``applyCanvasOffset(double, double, double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the x offset (in pixels)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: applyProperties(arg0)

   Applies properties from another Tree to this Tree.

   **Signature:** ``applyProperties(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree whose properties should be copied

   **Returns:** ``None``

.. method:: assignImage(arg0)

   Assigns spatial calibration from a Dataset to this Tree.

   **Signature:** ``assignImage(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the Dataset providing the spatial calibration. Null allowed.

   **Returns:** ``None``

.. method:: assignValue(arg0)

   Assigns a numeric property to this Tree.

   **Signature:** ``assignValue(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the value to be assigned to this Tree.

   **Returns:** ``None``

.. method:: clone()

   Creates a deep copy of this Tree.

This method creates a complete copy of the tree including all paths and their relationships. Each path is cloned individually, and then the parent-child relationships are reconstructed in the cloned tree. This ensures that the cloned tree maintains the same structure as the original while being completely independent.

   **Signature:** ``clone() -> Object``

   **Returns:** ``Any``

.. method:: downsample(arg0)

   Downsamples the tree, i.e., reduces the density of its nodes by increasing internode spacing.

Note that 1) upsampling is not supported (cf. {upsample(double)}, and 2) the position of nodes at branch points and tips remains unaltered during downsampling, as per `Path.downsample(double)`.

   **Signature:** ``downsample(double) -> void``

   **Parameters:**

   * **arg0** (``float``): - the maximum allowed distance between path nodes.

   **Returns:** ``None``

.. method:: get(arg0)

   Returns the Path at the specified position.

   **Signature:** ``get(int) -> Path``

   **Parameters:**

   * **arg0** (``int``): - index of the element to return

   **Returns:** (``Path``) the element at the specified position

.. method:: indexOf(arg0)

   Returns the index of the specified Path in this Tree.

   **Signature:** ``indexOf(Path) -> int``

   **Parameters:**

   * **arg0** (``Path``): - the Path to be searched for

   **Returns:** (``int``) the path index, or -1 if it was not found

.. method:: is3D()

   Assesses whether this Tree has depth.

   **Signature:** ``is3D() -> boolean``

   **Returns:** (``bool``) true, if is 3D

.. method:: list()

   Gets all the paths from this tree.

   **Signature:** ``list() -> ArrayList``

   **Returns:** (``List[Any]``) the paths forming this tree


TreeColorMapper
---------------

.. method:: map(arg0, arg1, arg2)

   Colorizes a tree after the specified measurement. Mapping bounds are automatically determined.

   **Signature:** ``map(Tree, String, String) -> void``

   **Parameters:**

   * **arg0** (``Tree``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: mapTrees(arg0, arg1)

   Colorizes a list of trees, with each tree being assigned a LUT index.

   **Signature:** ``mapTrees(List, String) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - the list of trees to be colorized
   * **arg1** (``str``)

   **Returns:** ``None``


TreeStatistics
--------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: dispose()

   Clears internal caches and mappings to free memory.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``


Viewer2D
--------

.. method:: add(arg0, arg1)

   Appends a tree to the viewer rendered after the specified measurement.

   **Signature:** ``add(Tree, String) -> void``

   **Parameters:**

   * **arg0** (``Tree``)
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: map(arg0, arg1, arg2)

   **Signature:** ``map(Tree, String, String) -> void``

   **Parameters:**

   * **arg0** (``Tree``)
   * **arg1** (``str``)
   * **arg2** (``str``)

   **Returns:** ``None``

.. method:: mapTrees(arg0, arg1)

   **Signature:** ``mapTrees(List, String) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: show(arg0, arg1)

   Displays the current plot on a dedicated frame *

   **Signature:** ``show(int, int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the preferred frame width
   * **arg1** (``int``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: add(arg0)

   Script friendly method to add a supported object (Tree, OBJMesh, AbstractDrawable, etc.) to this viewer. Note that collections of supported objects are also supported, which is an effective way of adding multiple items since the scene is only rebuilt once all items have been added.

   **Signature:** ``add(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the object to be added. No exception is triggered if null

   **Returns:** ``None``

.. method:: annotateLine(arg0, arg1)

   Adds a line annotation to this viewer.

   **Signature:** ``annotateLine(Collection, String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of points in the line annotation (at least 2 elements required). Start and end of line are highlighted if 2 points are specified.
   * **arg1** (``str``)

   **Returns:** (``Any``) the Annotation3D or null if collection contains less than 2 elements

.. method:: annotateMidPlane(arg0, arg1, arg2)

   **Signature:** ``annotateMidPlane(BoundingBox, int, String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``BoundingBox``)
   * **arg1** (``int``)
   * **arg2** (``str``)

   **Returns:** ``Any``

.. method:: annotatePlane(arg0, arg1, arg2)

   **Signature:** ``annotatePlane(SNTPoint, SNTPoint, String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``SNTPoint``)
   * **arg1** (``SNTPoint``)
   * **arg2** (``str``)

   **Returns:** ``Any``

.. method:: annotatePoint(arg0, arg1)

   Adds a highlighting point annotation to this viewer.

   **Signature:** ``annotatePoint(SNTPoint, String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``SNTPoint``): - the node to be highlighted
   * **arg1** (``str``)

   **Returns:** (``Any``) the Annotation3D

.. method:: annotatePoints(arg0, arg1)

   Adds a scatter (point cloud) annotation to this viewer.

   **Signature:** ``annotatePoints(Collection, String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of points in the annotation
   * **arg1** (``str``)

   **Returns:** (``Any``) the Annotation3D

.. method:: annotateSurface(arg0, arg1, arg2)

   Computes a convex hull from a collection of points and adds it to the scene as an annotation.

   **Signature:** ``annotateSurface(Collection, String, boolean) -> Annotation3D``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)
   * **arg2** (``bool``)

   **Returns:** ``Any``

.. method:: dispose()

   Closes and releases all the resources used by this viewer.

   **Signature:** ``dispose() -> void``

   **Returns:** ``None``

.. method:: duplicate()

   Creates a duplicate of this viewer containing only visible objects.

This method creates a new Viewer3D instance and copies all currently visible objects (trees, meshes, annotations) from this viewer to the new one. The duplicate viewer maintains the same visual settings and object properties but operates independently from the original.

   **Signature:** ``duplicate() -> Viewer3D``

   **Returns:** (``Viewer3D``) a new Viewer3D instance containing copies of all visible objects

.. method:: freeze()

   Does not allow scene to be interactive. Only static orthogonal views allowed.

   **Signature:** ``freeze() -> void``

   **Returns:** ``None``

.. method:: logSceneControls()

   Logs API calls controlling the scene (view point, bounds, etc.) to Script Recorder (or Console if Script Recorder is not running). Useful for programmatic control of animations.

   **Signature:** ``logSceneControls() -> void``

   **Returns:** ``None``

.. method:: mergeAnnotations(arg0, arg1)

   Merges a collection of annotations into a single object.

   **Signature:** ``mergeAnnotations(Collection, String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of annotations.
   * **arg1** (``str``)

   **Returns:** (``Any``) the merged Annotation3D

.. method:: rebuild(arg0)

   Rebuilds (repaints) a scene object (e.g., a Tree after being modified elsewhere)

   **Signature:** ``rebuild(Object) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the object to be re-rendered (or its label)

   **Returns:** ``None``

.. method:: recordRotation(arg0, arg1, arg2)

   Records an animated rotation of the scene as a sequence of images.

   **Signature:** ``recordRotation(float, int, File) -> void``

   **Parameters:**

   * **arg0** (``float``): - the rotation angle (e.g., 360 for a full rotation)
   * **arg1** (``int``)
   * **arg2** (``str``)

   **Returns:** ``None``


WekaModelLoader
---------------

.. method:: context()

   **Signature:** ``context() -> Context``

   **Returns:** ``Any``

.. method:: initialize()

   **Signature:** ``initialize() -> void``

   **Returns:** ``None``

.. method:: resolveInput(arg0)

   **Signature:** ``resolveInput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: resolveOutput(arg0)

   **Signature:** ``resolveOutput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: run()

   **Signature:** ``run() -> void``

   **Returns:** ``None``

.. method:: uncancel()

   **Signature:** ``uncancel() -> void``

   **Returns:** ``None``

.. method:: unresolveInput(arg0)

   **Signature:** ``unresolveInput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: unresolveOutput(arg0)

   **Signature:** ``unresolveOutput(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``


----

*Category index generated on 2025-11-13 22:40:29*