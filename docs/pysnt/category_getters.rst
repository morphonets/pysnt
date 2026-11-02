Getters Methods
===============

Methods that retrieve values or properties from objects.

Total methods in this category: **1370**

.. contents:: Classes in this Category
   :local:

AStarRefiner
------------

.. method:: getFailureReason()

   Human-readable reason `call()` failed, or null if it succeeded (or hasn't run yet).

   **Signature:** ``getFailureReason() -> String``

   **Returns:** (``str``) the failure reason, or null

.. method:: getPath()

   Returns the original path being re-traced.

   **Signature:** ``getPath() -> Path``

   **Returns:** (``Path``) the path


AllenCompartment
----------------

.. method:: getAncestor(level)

   Gets the nth ancestor of this compartment.

   **Signature:** ``getAncestor(int) -> AllenCompartment``

   **Parameters:**

   * **level** (``int``): - the ancestor level as negative 1-based index. E.g.,

   **Returns:** (``AllenCompartment``) the nth ancestor

.. method:: getAncestors()

   Gets the ancestor ontologies of this compartment as a flat (non-hierarchical) list.

   **Signature:** ``getAncestors() -> List``

   **Returns:** (``List[Any]``) the "flattened" list of ancestors

.. method:: getChildren()

   Gets the child ontologies of this compartment as a flat (non-hierarchical) list.

   **Signature:** ``getChildren() -> List``

   **Returns:** ``List[Any]``

.. method:: getMesh()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``getMesh() -> OBJMesh``

   **Returns:** ``OBJMesh``

.. method:: getOntologyDepth()

   Gets the ontology depth of this compartment.

   **Signature:** ``getOntologyDepth() -> int``

   **Returns:** (``int``) the ontological depth of this compartment, i.e., its ontological distance relative to the root (e.g., a compartment of hierarchical level `9`, has a depth of `8`).

.. method:: getParent()

   Gets the parent of this compartment.

   **Signature:** ``getParent() -> AllenCompartment``

   **Returns:** (``AllenCompartment``) the parent of this compartment, of null if this compartment is root.

.. method:: getTreePath()

   Gets the tree path of this compartment. The TreePath is the list of parent compartments that uniquely identify this compartment in the ontologies hierarchical tree. The elements of the list are ordered with the root ('Whole Brain') as the first element of the list. In practice, this is equivalent to appending this compartment to the list returned by `getAncestors()`.

   **Signature:** ``getTreePath() -> List``

   **Returns:** (``List[Any]``) the tree path that uniquely identifies this compartment as a node in the CCF ontologies tree

.. method:: getUUID()

   **Signature:** ``getUUID() -> UUID``

   **Returns:** ``Any``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isChildOf(parentCompartment)

   Assesses if this annotation is a child of a specified compartment.

   **Signature:** ``isChildOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **parentCompartment** (``Any``): - the compartment to be tested

   **Returns:** (``bool``) true, if successful, i.e., `parentCompartment` is not this compartment and `getTreePath()` contains `parentCompartment`

.. method:: isMeshAvailable()

   Checks whether a mesh is known to be available for this compartment.

   **Signature:** ``isMeshAvailable() -> boolean``

   **Returns:** (``bool``) true, if a mesh is available.

.. method:: isParentOf(childCompartment)

   Assesses if this annotation is the parent of the specified compartment.

   **Signature:** ``isParentOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **childCompartment** (``Any``): - the compartment to be tested

   **Returns:** (``bool``) true, if successful, i.e., `childCompartment` is not this compartment and is present in `getChildren()`


AllenUtils
----------

.. method:: getAnatomicalPlane(cartesianPlane)

   Retrieves the anatomical plane matching the specified cartesian plane.

   **Signature:** ``getAnatomicalPlane(String) -> String``

   **Parameters:**

   * **cartesianPlane** (``str``): - either "xy", "yz", or "xz"

   **Returns:** (``str``) the cartesian plane. Either "coronal", "sagittal", "transverse", or null if `cartesianPlane` was not recognized.

.. method:: getAxisDefiningSagittalPlane()

   Gets the axis defining the sagittal plane.

   **Signature:** ``getAxisDefiningSagittalPlane() -> int``

   **Returns:** (``int``) the axis defining the sagittal plane where X=0; Y=1; Z=2;

.. method:: getCartesianPlane(anatomicalPlane)

   Retrieves the Cartesian plane matching the specified anatomical plane.

   **Signature:** ``getCartesianPlane(String) -> String``

   **Parameters:**

   * **anatomicalPlane** (``str``): - either "sagittal", "coronal", or "transverse"

   **Returns:** (``str``) the cartesian plane. Either "xy", "yz", "xz", or null if `anatomicalPlane` was not recognized.

.. method:: getCompartment(nameOrAcronym)

   Constructs a compartment from its CCF name or acronym

   **Signature:** ``getCompartment(String) -> AllenCompartment``

   **Parameters:**

   * **nameOrAcronym** (``str``): - the name or acronym (case-insensitive) identifying the compartment

   **Returns:** (``AllenCompartment``) the compartment whose name or acronym matches the specified string or null if no match was found

.. method:: getHemisphere(tree)

   Checks the hemisphere a neuron belongs to.

   **Signature:** ``getHemisphere(Tree) -> String``

   **Parameters:**

   * **tree** (``Tree``): - the Tree to be tested

   **Returns:** (``str``) the hemisphere label: either "left", or "right"

.. method:: getHighestOntologyDepth()

   Gets the maximum number of ontology levels in the Allen CCF.

   **Signature:** ``getHighestOntologyDepth() -> int``

   **Returns:** (``int``) the max number of ontology levels.

.. method:: getOntologies()

   Gets a flat (non-hierarchical) list of all the compartments of the specified ontology depth.

   **Signature:** ``getOntologies() -> List``

   **Returns:** ``List[Any]``

.. method:: getRootMesh(color)

   Retrieves the surface contours for the Allen Mouse Brain Atlas (CCF), bundled with SNT.

   **Signature:** ``getRootMesh(ColorRGB) -> OBJMesh``

   **Parameters:**

   * **color** (``Any``): - the color to be assigned to the mesh

   **Returns:** (``OBJMesh``) a reference to the retrieved mesh

.. method:: getTreeModel(meshesOnly)

   Retrieves the Allen CCF hierarchical tree data.

   **Signature:** ``getTreeModel(boolean) -> DefaultTreeModel``

   **Parameters:**

   * **meshesOnly** (``bool``): - Whether only compartments with known meshes should be included

   **Returns:** (``Any``) the Allen CCF tree data model

.. method:: getXYZLabels()

   **Signature:** ``getXYZLabels() -> String[]``

   **Returns:** (``List[str]``) the anatomical descriptions associated with the Cartesian X,Y,Z axes

.. method:: isLeftHemisphere(point)

   **Signature:** ``isLeftHemisphere(SNTPoint) -> boolean``

   **Parameters:**

   * **point** (``SNTPoint``)

   **Returns:** ``bool``


Annotation3D
------------

.. method:: getBarycentre()

   Returns the center of this annotation bounding box.

   **Signature:** ``getBarycentre() -> SNTPoint``

   **Returns:** (``SNTPoint``) the barycentre of this annotation. All coordinates are set to Double.NaN if the bounding box is not available.

.. method:: getColor()

   **Signature:** ``getColor() -> ColorRGB``

   **Returns:** ``Any``

.. method:: getDrawable()

   Returns the AbstractDrawable associated with this annotation.

   **Signature:** ``getDrawable() -> Drawable``

   **Returns:** (``Any``) the AbstractDrawable

.. method:: getLabel()

   Gets the annotation label

   **Signature:** ``getLabel() -> String``

   **Returns:** (``str``) the label, as listed in Reconstruction Viewer's list.

.. method:: getType()

   Gets the type of this annotation.

   **Signature:** ``getType() -> String``

   **Returns:** (``str``) the annotation type. Either `cloud` (point cloud), `surface`, `line`, `plane`, or `mixed` (composite shape).

.. method:: getVolume()

   **Signature:** ``getVolume() -> double``

   **Returns:** ``float``

.. method:: isColorCodeAllowed()

   **Signature:** ``isColorCodeAllowed() -> boolean``

   **Returns:** ``bool``

.. method:: setSize(floatSize)

   Sets the annotation width.

   **Signature:** ``setSize(Number) -> void``

   **Parameters:**

   * **floatSize** (``Union[int, float]``): - the new width. A negative value will set width to Viewer3D's default.

   **Returns:** ``None``


AnnotationGraph
---------------

.. method:: getEdgeColor(edge)

   **Signature:** ``getEdgeColor(DefaultWeightedEdge) -> ColorRGB``

   **Parameters:**

   * **edge** (``Any``)

   **Returns:** ``Any``

.. method:: getEdgeColorRGBMap()

   **Signature:** ``getEdgeColorRGBMap() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getMaxOntologyDepth()

   **Signature:** ``getMaxOntologyDepth() -> int``

   **Returns:** ``int``

.. method:: getMetric()

   **Signature:** ``getMetric() -> String``

   **Returns:** ``str``

.. method:: getMetrics()

   **Signature:** ``getMetrics() -> String[]``

   **Returns:** ``List[str]``

.. method:: getThreshold()

   **Signature:** ``getThreshold() -> double``

   **Returns:** ``float``

.. method:: getTrees()

   **Signature:** ``getTrees() -> List``

   **Returns:** ``List[Any]``

.. method:: getVertexColor(vertex)

   **Signature:** ``getVertexColor(Object) -> ColorRGB``

   **Parameters:**

   * **vertex** (``Any``)

   **Returns:** ``Any``

.. method:: getVertexColorRGBMap()

   **Signature:** ``getVertexColorRGBMap() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getVertexValue(vertex)

   **Signature:** ``getVertexValue(Object) -> double``

   **Parameters:**

   * **vertex** (``Any``)

   **Returns:** ``float``

.. method:: getVertexValueMap()

   **Signature:** ``getVertexValueMap() -> Map``

   **Returns:** ``Dict[str, Any]``


ArraySearchImage
----------------

.. method:: getValue(x, y)

   **Signature:** ``getValue(int, int) -> Object``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)

   **Returns:** ``Any``


ArrayStorageBackend
-------------------

.. method:: getAliveIndices()

   **Signature:** ``getAliveIndices() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getBackendType()

   **Signature:** ``getBackendType() -> String``

   **Returns:** ``str``

.. method:: getDistance(index)

   **Signature:** ``getDistance(long) -> double``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``float``

.. method:: getGWDT(index)

   **Signature:** ``getGWDT(long) -> double``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``float``

.. method:: getMaxGWDT()

   **Signature:** ``getMaxGWDT() -> double``

   **Returns:** ``float``

.. method:: getParent(index)

   **Signature:** ``getParent(long) -> long``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``int``

.. method:: getState(index)

   **Signature:** ``getState(long) -> byte``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``int``


AutoTraceConfig
---------------

.. method:: getBackgroundThreshold()

   **Signature:** ``getBackgroundThreshold() -> double``

   **Returns:** ``float``

.. method:: getBranchTuneMaxAngle()

   **Signature:** ``getBranchTuneMaxAngle() -> double``

   **Returns:** ``float``

.. method:: getMeanContraction()

   **Signature:** ``getMeanContraction() -> double``

   **Returns:** ``float``

.. method:: getMeanIntensity()

   **Signature:** ``getMeanIntensity() -> double``

   **Returns:** ``float``

.. method:: getMeanRadius()

   **Signature:** ``getMeanRadius() -> double``

   **Returns:** ``float``

.. method:: getMinBranchIntensityLength()

   **Signature:** ``getMinBranchIntensityLength() -> double``

   **Returns:** ``float``

.. method:: getNodeCount()

   **Signature:** ``getNodeCount() -> int``

   **Returns:** ``int``

.. method:: getPathCount()

   **Signature:** ``getPathCount() -> int``

   **Returns:** ``int``

.. method:: getRecommendations()

   **Signature:** ``getRecommendations() -> List``

   **Returns:** ``List[Any]``

.. method:: getReconnectMaxAngleDeg()

   **Signature:** ``getReconnectMaxAngleDeg() -> double``

   **Returns:** ``float``

.. method:: getReconnectMaxBridgeDist()

   **Signature:** ``getReconnectMaxBridgeDist() -> double``

   **Returns:** ``float``

.. method:: getReconnectMinContraction()

   **Signature:** ``getReconnectMinContraction() -> double``

   **Returns:** ``float``

.. method:: getResampleStep()

   **Signature:** ``getResampleStep() -> double``

   **Returns:** ``float``

.. method:: getScoreMapScales()

   **Signature:** ``getScoreMapScales() -> double[]``

   **Returns:** ``List[float]``

.. method:: getSphereOverlapThreshold()

   **Signature:** ``getSphereOverlapThreshold() -> double``

   **Returns:** ``float``

.. method:: getSummary()

   **Signature:** ``getSummary() -> String``

   **Returns:** ``str``

.. method:: getWarnings()

   **Signature:** ``getWarnings() -> List``

   **Returns:** ``List[Any]``


Bdv
---

.. method:: getBdvHandle()

   Returns the underlying `BdvHandle` that manages sources and the viewer state.

   **Signature:** ``getBdvHandle() -> BdvHandle``

   **Returns:** ``Any``

.. method:: getBoundingBox()

   **Signature:** ``getBoundingBox() -> BoundingBox``

   **Returns:** ``BoundingBox``

.. method:: getCalibration()

   **Signature:** ``getCalibration() -> double[]``

   **Returns:** ``List[float]``

.. method:: getCurrentTimepoint()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getCurrentTimepoint() -> int``

   **Returns:** ``int``

.. method:: getDefaultMarkerColor()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getDefaultMarkerColor() -> Color``

   **Returns:** ``Any``

.. method:: getDefaultMarkerSize()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getDefaultMarkerSize() -> float``

   **Returns:** ``float``

.. method:: getDefaultRenderingStyle()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getDefaultRenderingStyle() -> Style``

   **Returns:** (``Any``) the default style

.. method:: getDisplayRadii()

   Returns whether paths are rendered as frusta (true) or centerlines (false).

   **Signature:** ``getDisplayRadii() -> boolean``

   **Returns:** ``bool``

.. method:: getDisplayRange(sourceIndex)

   **Signature:** ``getDisplayRange(int) -> double[]``

   **Parameters:**

   * **sourceIndex** (``int``)

   **Returns:** ``List[float]``

.. method:: getDownsamplingFactors(sourceIndex, level)

   **Signature:** ``getDownsamplingFactors(int, int) -> double[]``

   **Parameters:**

   * **sourceIndex** (``int``)
   * **level** (``int``)

   **Returns:** ``List[float]``

.. method:: getGlobalMouseCoordinates(pos)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getGlobalMouseCoordinates(RealPoint) -> void``

   **Parameters:**

   * **pos** (``Any``): - 3D point to receive the world-space cursor position

   **Returns:** ``None``

.. method:: getInstance()

   Returns the most recently created `Bdv` instance, or `null`. Convenience accessor for scripts.

   **Signature:** ``getInstance() -> Bdv``

   **Returns:** ``Bdv``

.. method:: getMarkerManager()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getMarkerManager() -> BookmarkManager``

   **Returns:** ``BookmarkManager``

.. method:: getNumResolutionLevels(sourceIndex)

   **Signature:** ``getNumResolutionLevels(int) -> int``

   **Parameters:**

   * **sourceIndex** (``int``)

   **Returns:** ``int``

.. method:: getPhysicalUnit()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getPhysicalUnit() -> String``

   **Returns:** ``str``

.. method:: getPrimarySourcePath()

   **Signature:** ``getPrimarySourcePath() -> String``

   **Returns:** ``str``

.. method:: getRenderSettleTime()

   **Signature:** ``getRenderSettleTime() -> long``

   **Returns:** ``int``

.. method:: getRenderedTrees()

   **Signature:** ``getRenderedTrees() -> Collection``

   **Returns:** ``List[Any]``

.. method:: getRenderingOptions()

   Returns the rendering options controlling path thickness, transparency, etc. For BDV, slab clipping options have no effect (slab mode is BVV-only).

   **Signature:** ``getRenderingOptions() -> PathRenderingOptions``

   **Returns:** ``Any``

.. method:: getSNT()

   **Signature:** ``getSNT() -> SNT``

   **Returns:** ``SNT``

.. method:: getSceneCenter()

   **Signature:** ``getSceneCenter() -> SNTPoint``

   **Returns:** ``SNTPoint``

.. method:: getSourceData(sourceIndex, level)

   **Signature:** ``getSourceData(int, int) -> RandomAccessibleInterval``

   **Parameters:**

   * **sourceIndex** (``int``)
   * **level** (``int``)

   **Returns:** ``Any``

.. method:: getSourceName(sourceIndex)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getSourceName(int) -> String``

   **Parameters:**

   * **sourceIndex** (``int``): - the action key (e.g., "align XY plane")

   **Returns:** ``str``

.. method:: getSourcePaths()

   **Signature:** ``getSourcePaths() -> List``

   **Returns:** ``List[Any]``

.. method:: getViewerCanvas()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerCanvas() -> Component``

   **Returns:** ``Any``

.. method:: getViewerFrame()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerFrame() -> ViewerFrame``

   **Returns:** ``Any``

.. method:: getViewerHeight()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerHeight() -> int``

   **Returns:** ``int``

.. method:: getViewerPanel()

   Returns the BDV display panel. Unlike BVV, BDV uses a `ViewerPanel` (orthographic slice viewer).

   **Signature:** ``getViewerPanel() -> ViewerPanel``

   **Returns:** ``Any``

.. method:: getViewerTransform()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerTransform() -> AffineTransform3D``

   **Returns:** ``Any``

.. method:: getViewerWidth()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerWidth() -> int``

   **Returns:** ``int``

.. method:: hasMarkerManager()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``hasMarkerManager() -> boolean``

   **Returns:** ``bool``

.. method:: isDisposed()

   **Signature:** ``isDisposed() -> boolean``

   **Returns:** ``bool``

.. method:: isEditModeEnabled()

   **Signature:** ``isEditModeEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isOpen()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``isOpen() -> boolean``

   **Returns:** ``bool``

.. method:: isPathInProgress()

   **Signature:** ``isPathInProgress() -> boolean``

   **Returns:** ``bool``

.. method:: isTracingEnabled()

   **Signature:** ``isTracingEnabled() -> boolean``

   **Returns:** ``bool``


BiSearch
--------

.. method:: getNodesAsImage()

   **Signature:** ``getNodesAsImage() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``


BiSearchArtist
--------------

.. method:: getSearch()

   **Signature:** ``getSearch() -> SearchInterface``

   **Returns:** ``Any``


BiSearchNode
------------

.. method:: getF(fromStart)

   **Signature:** ``getF(boolean) -> double``

   **Parameters:**

   * **fromStart** (``bool``)

   **Returns:** ``float``

.. method:: getFFromGoal()

   **Signature:** ``getFFromGoal() -> double``

   **Returns:** ``float``

.. method:: getFFromStart()

   **Signature:** ``getFFromStart() -> double``

   **Returns:** ``float``

.. method:: getG(fromStart)

   **Signature:** ``getG(boolean) -> double``

   **Parameters:**

   * **fromStart** (``bool``)

   **Returns:** ``float``

.. method:: getGFromGoal()

   **Signature:** ``getGFromGoal() -> double``

   **Returns:** ``float``

.. method:: getGFromStart()

   **Signature:** ``getGFromStart() -> double``

   **Returns:** ``float``

.. method:: getHeapHandle(fromStart)

   **Signature:** ``getHeapHandle(boolean) -> Handle``

   **Parameters:**

   * **fromStart** (``bool``)

   **Returns:** ``Any``

.. method:: getHeapHandleFromGoal()

   **Signature:** ``getHeapHandleFromGoal() -> Handle``

   **Returns:** ``Any``

.. method:: getHeapHandleFromStart()

   **Signature:** ``getHeapHandleFromStart() -> Handle``

   **Returns:** ``Any``

.. method:: getPredecessorFromGoal()

   **Signature:** ``getPredecessorFromGoal() -> BiSearchNode``

   **Returns:** ``BiSearchNode``

.. method:: getPredecessorFromStart()

   **Signature:** ``getPredecessorFromStart() -> BiSearchNode``

   **Returns:** ``BiSearchNode``

.. method:: getState(fromStart)

   **Signature:** ``getState(boolean) -> State``

   **Parameters:**

   * **fromStart** (``bool``)

   **Returns:** ``Any``

.. method:: getStateFromGoal()

   **Signature:** ``getStateFromGoal() -> State``

   **Returns:** ``Any``

.. method:: getStateFromStart()

   **Signature:** ``getStateFromStart() -> State``

   **Returns:** ``Any``

.. method:: getX()

   **Signature:** ``getX() -> int``

   **Returns:** ``int``

.. method:: getY()

   **Signature:** ``getY() -> int``

   **Returns:** ``int``

.. method:: getZ()

   **Signature:** ``getZ() -> int``

   **Returns:** ``int``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``


BinaryTracer
------------

.. method:: getGraphs()

   **Signature:** ``getGraphs() -> List``

   **Returns:** ``List[Any]``

.. method:: getPruneMode()

   **Signature:** ``getPruneMode() -> int``

   **Returns:** ``int``

.. method:: getRootRoiStrategy()

   **Signature:** ``getRootRoiStrategy() -> int``

   **Returns:** ``int``

.. method:: getSingleGraph()

   **Signature:** ``getSingleGraph() -> DirectedWeightedGraph``

   **Returns:** ``DirectedWeightedGraph``

.. method:: getSingleTree()

   **Signature:** ``getSingleTree() -> Tree``

   **Returns:** ``Tree``

.. method:: getTrees()

   **Signature:** ``getTrees() -> List``

   **Returns:** ``List[Any]``

.. method:: setPruneByLength(pruneByLength)

   **Signature:** ``setPruneByLength(boolean) -> void``

   **Parameters:**

   * **pruneByLength** (``bool``)

   **Returns:** ``None``


BookmarkManager
---------------

.. method:: getCount()

   Returns the number of bookmarks.

   **Signature:** ``getCount() -> int``

   **Returns:** (``int``) the number of bookmarks currently stored in the manager.

.. method:: getLastPosition()

   Returns the position of the most recently added bookmark/marker, in spatially calibrated ("world") coordinates (canonical storage format).

In viewer mode (BVV/BDV), this is the last marker placed with the `M` key (or added programmatically). In SNT-UI mode, this is the last entry added to the Bookmark Manager pane. Since new entries are always appended, this reflects placement order in the common case; it can become stale relative to placement order after an explicit list-reordering operation (e.g. the table's "Sort by Distance..." menu, or a Merge/Colocalize operation, both of which re-write the backing list).

   **Signature:** ``getLastPosition() -> SNTPoint``

   **Returns:** (``SNTPoint``) the position of the last bookmark, or `null` if none have been added

.. method:: getPixelPositions(onlySelectedRows)

   Returns bookmark/marker positions in **pixel/voxel** coordinates, converted from this manager's canonical world/calibrated storage via `worldToPixel(Bookmark)`.

   **Signature:** ``getPixelPositions(boolean) -> List``

   **Parameters:**

   * **onlySelectedRows** (``bool``): - if true, only selected rows are included; otherwise, all bookmarks in the manager are included

   **Returns:** (``List[Any]``) the list of Points (fresh `PointInImage` copies) of the bookmarks, in pixel/voxel coordinates

.. method:: getPositions(onlySelectedRows)

   Returns bookmark/marker positions in spatially calibrated (**"world"**) coordinates, i.e., this manager's canonical storage format, returned as-is (fresh copies) in both modes.

   **Signature:** ``getPositions(boolean) -> List``

   **Parameters:**

   * **onlySelectedRows** (``bool``): - if true, only selected rows are included; otherwise, all bookmarks in the manager are included

   **Returns:** (``List[Any]``) the list of Points representing the bookmarks, in calibrated ("world") coordinates

.. method:: getROIs(onlySelectedRows)

   Returns a list of ROIs representing the bookmarks.

   **Signature:** ``getROIs(boolean) -> List``

   **Parameters:**

   * **onlySelectedRows** (``bool``): - if true, only selected rows are included; otherwise, all ROIs in the manager are included

   **Returns:** (``List[Any]``) the list of ROIs (PointRoi) representing the bookmarks

.. method:: getRois(commonLabel, xyzctLocations)

   Creates a list of `PointRoi`s from XYZCT locations with a color tag.

   **Signature:** ``getRois(String, List) -> List``

   **Parameters:**

   * **commonLabel** (``str``): - the label prefix for each ROI
   * **xyzctLocations** (``List[Any]``)

   **Returns:** (``List[Any]``) list of PointRoi objects

.. method:: getViewerDialogPanel()

   Returns the floating dialog for viewer mode, creating it on first call.

   **Signature:** ``getViewerDialogPanel() -> JDialog``

   **Returns:** ``Any``

.. method:: hasBookmarks()

   Returns whether any bookmarks exist.

   **Signature:** ``hasBookmarks() -> boolean``

   **Returns:** (``bool``) true if there is at least one bookmark

.. method:: isVisible()

   Returns whether this manager's markers are currently rendered in the big-viewer's shared `AbstractBigViewer.AnnotationOverlay`, independently of the paths and seed-annotation layers.

   **Signature:** ``isVisible() -> boolean``

   **Returns:** (``bool``) true if markers are shown, false if hidden


BoundingBox
-----------

.. method:: getCalibration()

   Creates a Calibration object using information from this BoundingBox

   **Signature:** ``getCalibration() -> Calibration``

   **Returns:** (``Any``) the Calibration object

.. method:: getCentroid()

   **Signature:** ``getCentroid() -> SNTPoint``

   **Returns:** ``SNTPoint``

.. method:: getDiagonal()

   Gets the box diagonal

   **Signature:** ``getDiagonal() -> double``

   **Returns:** (``float``) the diagonal of BoundingBox

.. method:: getDimensions()

   Gets this BoundingBox dimensions.

   **Signature:** ``getDimensions() -> double[]``

   **Returns:** ``List[float]``

.. method:: getUnit()

   Gets the length unit of voxel spacing

   **Signature:** ``getUnit() -> String``

   **Returns:** (``str``) the unit

.. method:: hasDimensions()

   **Signature:** ``hasDimensions() -> boolean``

   **Returns:** ``bool``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isScaled()

   Checks whether this BoundingBox is spatially calibrated, i.e., if voxel spacing has been specified

   **Signature:** ``isScaled() -> boolean``

   **Returns:** (``bool``) true, if voxel spacing has been specified


Bvv
---

.. method:: getBoundingBox()

   **Signature:** ``getBoundingBox() -> BoundingBox``

   **Returns:** ``BoundingBox``

.. method:: getCalibration()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getCalibration() -> double[]``

   **Returns:** (``List[float]``) calibrated (x,y,z) position, or null if it could not be resolved

.. method:: getCurrentTimepoint()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getCurrentTimepoint() -> int``

   **Returns:** ``int``

.. method:: getDefaultMarkerColor()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getDefaultMarkerColor() -> Color``

   **Returns:** ``Any``

.. method:: getDefaultMarkerSize()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getDefaultMarkerSize() -> float``

   **Returns:** ``float``

.. method:: getDefaultRenderingStyle()

   **Signature:** ``getDefaultRenderingStyle() -> Style``

   **Returns:** ``Any``

.. method:: getDisplayRadii()

   Returns whether paths are currently rendered with per-node radii as tapered frusta (`true`) or as simple lines (`false`).

   **Signature:** ``getDisplayRadii() -> boolean``

   **Returns:** (``bool``) `true` if frustum/radius rendering is active

.. method:: getDisplayRange(sourceIndex)

   **Signature:** ``getDisplayRange(int) -> double[]``

   **Parameters:**

   * **sourceIndex** (``int``)

   **Returns:** ``List[float]``

.. method:: getDownsamplingFactors(sourceIndex, level)

   **Signature:** ``getDownsamplingFactors(int, int) -> double[]``

   **Parameters:**

   * **sourceIndex** (``int``)
   * **level** (``int``)

   **Returns:** ``List[float]``

.. method:: getGlobalMouseCoordinates(pos)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getGlobalMouseCoordinates(RealPoint) -> void``

   **Parameters:**

   * **pos** (``Any``): - 3D point to receive the world-space cursor position

   **Returns:** ``None``

.. method:: getInstance()

   Returns the most recently created `Bvv` instance, or `null` if none has been created yet. Convenience accessor for scripts.

   **Signature:** ``getInstance() -> Bvv``

   **Returns:** (``Bvv``) the last initialised Bvv, or `null`

.. method:: getMarkerManager()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getMarkerManager() -> BookmarkManager``

   **Returns:** ``BookmarkManager``

.. method:: getMultiSources()

   Returns all `BvvMultiSource` groups currently managed by this viewer. This includes multichannel images and any grouped multi-image sources.

   **Signature:** ``getMultiSources() -> List``

   **Returns:** (``List[Any]``) unmodifiable list of `BvvMultiSource` groups

.. method:: getNumResolutionLevels(sourceIndex)

   **Signature:** ``getNumResolutionLevels(int) -> int``

   **Parameters:**

   * **sourceIndex** (``int``)

   **Returns:** ``int``

.. method:: getOptions()

   **Signature:** ``getOptions() -> BvvOptions``

   **Returns:** (``Any``) a reference to the viewer's options.

.. method:: getPhysicalUnit()

   Resolves the physical unit string for the currently loaded volume.

   **Signature:** ``getPhysicalUnit() -> String``

   **Returns:** (``str``) the physical unit. Checks (in order): `calUnit` field, first source's VoxelDimensions (same source used by the scale bar renderer), and SNT spacing units. Returns `BoundingBox.UNSET_SPACING_UNIT` if unit is unknown or unset.

.. method:: getPrimarySourcePath()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getPrimarySourcePath() -> String``

   **Returns:** ``str``

.. method:: getRenderSettleTime()

   **Signature:** ``getRenderSettleTime() -> long``

   **Returns:** ``int``

.. method:: getRenderedTrees()

   **Signature:** ``getRenderedTrees() -> Collection``

   **Returns:** ``List[Any]``

.. method:: getRenderingOptions()

   Gets the path rendering options for controlling thickness, transparency, etc.

   **Signature:** ``getRenderingOptions() -> PathRenderingOptions``

   **Returns:** (``Any``) the rendering options

.. method:: getSNT()

   **Signature:** ``getSNT() -> SNT``

   **Returns:** ``SNT``

.. method:: getSceneCenter()

   The world-space point currently at the center of this viewer's display: the intensity-peak result of `findSceneCenterMaxima()` when available, otherwise the same focal-plane fallback used by `AbstractBigViewer.getSceneCenter()`.

   **Signature:** ``getSceneCenter() -> SNTPoint``

   **Returns:** (``SNTPoint``) the world-space scene center, or `null` if the viewport has not yet been realized

.. method:: getSourceData(sourceIndex, level)

   **Signature:** ``getSourceData(int, int) -> RandomAccessibleInterval``

   **Parameters:**

   * **sourceIndex** (``int``)
   * **level** (``int``)

   **Returns:** ``Any``

.. method:: getSourceName(sourceIndex)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getSourceName(int) -> String``

   **Parameters:**

   * **sourceIndex** (``int``): - the action key (e.g., "align XY plane")

   **Returns:** ``str``

.. method:: getSourcePaths()

   **Signature:** ``getSourcePaths() -> List``

   **Returns:** ``List[Any]``

.. method:: getViewer()

   **Signature:** ``getViewer() -> BigVolumeViewer``

   **Returns:** (``Any``) a reference to the underlying BigVolumeViewer instance.

.. method:: getViewerCanvas()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerCanvas() -> Component``

   **Returns:** ``Any``

.. method:: getViewerFrame()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerFrame() -> VolumeViewerFrame``

   **Returns:** (``Any``) a reference to the viewer's frame.

.. method:: getViewerHeight()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerHeight() -> int``

   **Returns:** ``int``

.. method:: getViewerPanel()

   **Signature:** ``getViewerPanel() -> VolumeViewerPanel``

   **Returns:** (``Any``) a reference to the viewer's panel.

.. method:: getViewerTransform()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerTransform() -> AffineTransform3D``

   **Returns:** ``Any``

.. method:: getViewerWidth()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``getViewerWidth() -> int``

   **Returns:** ``int``

.. method:: hasMarkerManager()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``hasMarkerManager() -> boolean``

   **Returns:** ``bool``

.. method:: isDisposed()

   **Signature:** ``isDisposed() -> boolean``

   **Returns:** ``bool``

.. method:: isEditModeEnabled()

   **Signature:** ``isEditModeEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isOpen()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``isOpen() -> boolean``

   **Returns:** ``bool``

.. method:: isPathInProgress()

   **Signature:** ``isPathInProgress() -> boolean``

   **Returns:** ``bool``

.. method:: isTracingEnabled()

   **Signature:** ``isTracingEnabled() -> boolean``

   **Returns:** ``bool``


BvvMultiSource
--------------

.. method:: getFollowers()

   **Signature:** ``getFollowers() -> List``

   **Returns:** (``List[Any]``) unmodifiable view of the follower sources

.. method:: getLeader()

   **Signature:** ``getLeader() -> BvvStackSource``

   **Returns:** (``Any``) the leader source

.. method:: getLeaderTransform(result)

   Returns a copy of the most recently cached leader fixed transform.

   **Signature:** ``getLeaderTransform(AffineTransform3D) -> void``

   **Parameters:**

   * **result** (``Any``): - set to the cached transform

   **Returns:** ``None``

.. method:: getSources()

   **Signature:** ``getSources() -> List``

   **Returns:** (``List[Any]``) all sources (leader + followers) as an unmodifiable list

.. method:: isLiveSync()

   **Signature:** ``isLiveSync() -> boolean``

   **Returns:** (``bool``) `true` if live transform sync is enabled

.. method:: size()

   **Signature:** ``size() -> int``

   **Returns:** (``int``) number of sources in the group (leader + followers)


BvvUtils
--------

.. method:: getCachePrefMB()

   **Signature:** ``getCachePrefMB() -> int``

   **Returns:** (``int``) the user's GPU tile cache preference (MB). 0 means automatic

.. method:: getFetchersPref()

   **Signature:** ``getFetchersPref() -> int``

   **Returns:** (``int``) the user's tile fetcher thread preference. 0 means automatic

.. method:: getRenderQuality()

   **Signature:** ``getRenderQuality() -> RenderQuality``

   **Returns:** (``Any``) the persisted render quality preset (applies the next time a BVV window is opened)

.. method:: isCachePromptSuppressed()

   **Signature:** ``isCachePromptSuppressed() -> boolean``

   **Returns:** ``bool``


ConvexHull2D
------------

.. method:: boundarySize()

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``boundarySize() -> double``

   **Returns:** ``float``

.. method:: getPolygon()

   **Signature:** ``getPolygon() -> Polygon2D``

   **Returns:** ``Any``

.. method:: size()

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``size() -> double``

   **Returns:** ``float``


ConvexHull3D
------------

.. method:: boundarySize()

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``boundarySize() -> double``

   **Returns:** ``float``

.. method:: getMesh()

   **Signature:** ``getMesh() -> Mesh``

   **Returns:** ``Any``

.. method:: size()

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``size() -> double``

   **Returns:** ``float``


ConvexHullAnalyzer
------------------

.. method:: getAnalysis()

   Gets all computed convex hull analysis metrics.

Returns a map containing all the computed convex hull metrics and their values. The metrics are computed lazily and cached for subsequent calls. If the hull cannot be computed, all metrics return NaN.

   **Signature:** ``getAnalysis() -> Map``

   **Returns:** (``Dict[str, Any]``) a map of metric names to their computed values

.. method:: getBoundarySize()

   Gets the boundary size (perimeter for 2D hulls or surface area for 3D hulls) of the convex hull.

   **Signature:** ``getBoundarySize() -> double``

   **Returns:** (``float``) the boundary size of the convex hull

.. method:: getBoxivity()

   Gets the boxivity of the convex hull, which measures how box-like the convex hull is. Values closer to 1 indicate a more box-like shape.

   **Signature:** ``getBoxivity() -> double``

   **Returns:** (``float``) the boxivity value

.. method:: getCentroid()

   **Signature:** ``getCentroid() -> PointInImage``

   **Returns:** ``PointInImage``

.. method:: getCompactness()

   **Signature:** ``getCompactness() -> double``

   **Returns:** ``float``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getEccentricity()

   **Signature:** ``getEccentricity() -> double``

   **Returns:** ``float``

.. method:: getElongation()

   Gets the elongation of the convex hull, which measures how elongated the convex hull is. Higher values indicate more elongated shapes.

   **Signature:** ``getElongation() -> double``

   **Returns:** (``float``) the elongation value

.. method:: getHull()

   Gets the convex hull object being analyzed. The hull is initialized if needed.

   **Signature:** ``getHull() -> AbstractConvexHull``

   **Returns:** (``Any``) the convex hull object

.. method:: getRoundness()

   Gets the roundness of the convex hull, which measures how round or circular the convex hull is. Values closer to 1 indicate a more round shape.

   **Signature:** ``getRoundness() -> double``

   **Returns:** (``float``) the roundness value

.. method:: getSize()

   Gets the size (area or volume) of the convex hull, which is the area for 2D hulls or the volume for 3D hulls.

   **Signature:** ``getSize() -> double``

   **Returns:** (``float``) the size of the convex hull

.. method:: getTree()

   Gets the tree being analyzed.

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the tree being analyzed, or null if the analyzer was created directly from a convex hull.

.. method:: getUnit(metric)

   Returns the physical unit associated with the specified metric.

   **Signature:** ``getUnit(String) -> String``

   **Parameters:**

   * **metric** (``str``): - the supported metric to be queried (case-sensitive)

   **Returns:** (``str``) physical unit


CrossSectionUtils
-----------------

.. method:: computeGridSize(physicalRadius, scale, maxSide)

   Computes the grid size needed to cover a given physical radius at the specified scale, capped to a maximum.

   **Signature:** ``computeGridSize(double, double, int) -> int``

   **Parameters:**

   * **physicalRadius** (``float``): - radius in calibrated units
   * **scale** (``float``)
   * **maxSide** (``int``)

   **Returns:** (``int``) the grid size (always odd, so center pixel is well-defined)


CurationManager
---------------

.. method:: getPanel()

   Builds and returns the panel to be added as a tab in SNTUI.

   **Signature:** ``getPanel() -> JPanel``

   **Returns:** ``Any``

.. method:: getStatusSummary()

   Generates a summary string for the status bar: shows the most severe warning, suitable for display in the QUERY_KEEP status text.

   **Signature:** ``getStatusSummary() -> String``

   **Returns:** (``str``) the summary string, or `null` if no warnings exist


DefaultSearchNode
-----------------

.. method:: getHandle()

   **Signature:** ``getHandle() -> Handle``

   **Returns:** ``Any``

.. method:: getPredecessor()

   **Signature:** ``getPredecessor() -> DefaultSearchNode``

   **Returns:** ``DefaultSearchNode``

.. method:: getX()

   **Signature:** ``getX() -> int``

   **Returns:** ``int``

.. method:: getY()

   **Signature:** ``getY() -> int``

   **Returns:** ``int``

.. method:: getZ()

   **Signature:** ``getZ() -> int``

   **Returns:** ``int``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``


DelineationsManager
-------------------

.. method:: getDelineationROIs()

   **Signature:** ``getDelineationROIs() -> List``

   **Returns:** ``List[Any]``

.. method:: hasDelineationLabels(trees)

   Checks if the given tree has any delineation labels.

   **Signature:** ``hasDelineationLabels(Collection) -> boolean``

   **Parameters:**

   * **trees** (``List[Any]``): - the collection of paths to be inspected

   **Returns:** (``bool``) true if the tree has delineation labels, false otherwise


DirectedWeightedGraph
---------------------

.. method:: getBPs()

   **Signature:** ``getBPs() -> List``

   **Returns:** ``List[Any]``

.. method:: getBreadthFirstIterator()

   **Signature:** ``getBreadthFirstIterator() -> BreadthFirstIterator``

   **Returns:** ``Any``

.. method:: getComponents()

   **Signature:** ``getComponents() -> List``

   **Returns:** ``List[Any]``

.. method:: getDepthFirstIterator()

   **Signature:** ``getDepthFirstIterator() -> DepthFirstIterator``

   **Returns:** ``Any``

.. method:: getEdgeColor(edge)

   **Signature:** ``getEdgeColor(DefaultWeightedEdge) -> ColorRGB``

   **Parameters:**

   * **edge** (``Any``)

   **Returns:** ``Any``

.. method:: getEdgeColorRGBMap()

   **Signature:** ``getEdgeColorRGBMap() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getLongestPath(useDirected)

   **Signature:** ``getLongestPath(boolean) -> Path``

   **Parameters:**

   * **useDirected** (``bool``)

   **Returns:** ``Path``

.. method:: getLongestPathVertices(useDirected)

   **Signature:** ``getLongestPathVertices(boolean) -> Deque``

   **Parameters:**

   * **useDirected** (``bool``)

   **Returns:** ``Any``

.. method:: getNodeStatistics()

   **Signature:** ``getNodeStatistics() -> NodeStatistics``

   **Returns:** ``NodeStatistics``

.. method:: getNodesFromLeavesToRoot()

   **Signature:** ``getNodesFromLeavesToRoot() -> List``

   **Returns:** ``List[Any]``

.. method:: getNodesFromRootToLeaves()

   **Signature:** ``getNodesFromRootToLeaves() -> List``

   **Returns:** ``List[Any]``

.. method:: getRoot()

   **Signature:** ``getRoot() -> SWCPoint``

   **Returns:** ``SWCPoint``

.. method:: getShortestPath(v1, v2)

   **Signature:** ``getShortestPath(SWCPoint, SWCPoint) -> Path``

   **Parameters:**

   * **v1** (``SWCPoint``)
   * **v2** (``SWCPoint``)

   **Returns:** ``Path``

.. method:: getShortestPathVertices(v1, v2)

   **Signature:** ``getShortestPathVertices(SWCPoint, SWCPoint) -> Deque``

   **Parameters:**

   * **v1** (``SWCPoint``)
   * **v2** (``SWCPoint``)

   **Returns:** ``Any``

.. method:: getSimplifiedGraph()

   **Signature:** ``getSimplifiedGraph() -> DirectedWeightedGraph``

   **Returns:** ``DirectedWeightedGraph``

.. method:: getSubgraph(nodeSubset)

   **Signature:** ``getSubgraph(Set) -> DirectedWeightedSubgraph``

   **Parameters:**

   * **nodeSubset** (``Set[Any]``)

   **Returns:** ``DirectedWeightedSubgraph``

.. method:: getTips()

   **Signature:** ``getTips() -> List``

   **Returns:** ``List[Any]``

.. method:: getTopologicalOrderIterator()

   **Signature:** ``getTopologicalOrderIterator() -> TopologicalOrderIterator``

   **Returns:** ``Any``

.. method:: getTree()

   **Signature:** ``getTree() -> Tree``

   **Returns:** ``Tree``

.. method:: getTreeWithSamePathStructure()

   **Signature:** ``getTreeWithSamePathStructure() -> Tree``

   **Returns:** ``Tree``

.. method:: getTrees()

   **Signature:** ``getTrees() -> List``

   **Returns:** ``List[Any]``

.. method:: getVertexColor(vertex)

   **Signature:** ``getVertexColor(Object) -> ColorRGB``

   **Parameters:**

   * **vertex** (``Any``)

   **Returns:** ``Any``

.. method:: getVertexColorRGBMap()

   **Signature:** ``getVertexColorRGBMap() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getVertexValue(vertex)

   **Signature:** ``getVertexValue(Object) -> double``

   **Parameters:**

   * **vertex** (``Any``)

   **Returns:** ``float``

.. method:: getVertexValueMap()

   **Signature:** ``getVertexValueMap() -> Map``

   **Returns:** ``Dict[str, Any]``


DirectedWeightedSubgraph
------------------------

.. method:: getBPs()

   **Signature:** ``getBPs() -> List``

   **Returns:** ``List[Any]``

.. method:: getDepthFirstIterator()

   **Signature:** ``getDepthFirstIterator() -> DepthFirstIterator``

   **Returns:** ``Any``

.. method:: getLabel()

   **Signature:** ``getLabel() -> String``

   **Returns:** ``str``

.. method:: getNodeStatistics(type)

   **Signature:** ``getNodeStatistics(String) -> NodeStatistics``

   **Parameters:**

   * **type** (``str``)

   **Returns:** ``NodeStatistics``

.. method:: getRoot()

   **Signature:** ``getRoot() -> SWCPoint``

   **Returns:** ``SWCPoint``

.. method:: getTips()

   **Signature:** ``getTips() -> List``

   **Returns:** ``List[Any]``

.. method:: getTree()

   **Signature:** ``getTree() -> Tree``

   **Returns:** ``Tree``


DiskBackedGWDTTracer
--------------------

.. method:: getCaliperFraction()

   **Signature:** ``getCaliperFraction() -> double``

   **Returns:** ``float``

.. method:: getMaxGapVoxels()

   **Signature:** ``getMaxGapVoxels() -> int``

   **Returns:** ``int``

.. method:: getMinSomaDistance()

   **Signature:** ``getMinSomaDistance() -> double``

   **Returns:** ``float``

.. method:: getNSomas()

   **Signature:** ``getNSomas() -> int``

   **Returns:** ``int``

.. method:: getRootStrategy()

   **Signature:** ``getRootStrategy() -> int``

   **Returns:** ``int``

.. method:: getScoreMap()

   **Signature:** ``getScoreMap() -> RandomAccessibleInterval``

   **Returns:** ``Any``

.. method:: getSomaRoi()

   **Signature:** ``getSomaRoi() -> Roi``

   **Returns:** ``Any``

.. method:: getTipExtensionDistance()

   **Signature:** ``getTipExtensionDistance() -> double``

   **Returns:** ``float``

.. method:: getTracedRegionBuffer()

   **Signature:** ``getTracedRegionBuffer() -> int``

   **Returns:** ``int``

.. method:: isAllowVoxelGap()

   **Signature:** ``isAllowVoxelGap() -> boolean``

   **Returns:** ``bool``

.. method:: isAutoFilter()

   **Signature:** ``isAutoFilter() -> boolean``

   **Returns:** ``bool``

.. method:: isParallelBranchPruneEnabled()

   **Signature:** ``isParallelBranchPruneEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isPathFittingEnabled()

   **Signature:** ``isPathFittingEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isVerbose()

   **Signature:** ``isVerbose() -> boolean``

   **Returns:** ``bool``

.. method:: setMinBranchIntensityLength(threshold)

   **Signature:** ``setMinBranchIntensityLength(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setMinSegmentLength(lengthInPhysicalUnits)

   **Signature:** ``setMinSegmentLength(double) -> void``

   **Parameters:**

   * **lengthInPhysicalUnits** (``float``)

   **Returns:** ``None``

.. method:: setSmoothWindowSize(windowSize)

   **Signature:** ``setSmoothWindowSize(int) -> void``

   **Parameters:**

   * **windowSize** (``int``)

   **Returns:** ``None``


DiskBackedStorageBackend
------------------------

.. method:: getAliveIndices()

   **Signature:** ``getAliveIndices() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getBackendType()

   **Signature:** ``getBackendType() -> String``

   **Returns:** ``str``

.. method:: getDistance(index)

   **Signature:** ``getDistance(long) -> double``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``float``

.. method:: getGWDT(index)

   **Signature:** ``getGWDT(long) -> double``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``float``

.. method:: getMaxGWDT()

   **Signature:** ``getMaxGWDT() -> double``

   **Returns:** ``float``

.. method:: getParent(index)

   **Signature:** ``getParent(long) -> long``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``int``

.. method:: getState(index)

   **Signature:** ``getState(long) -> byte``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``int``


Fill
----

.. method:: getEstimatedMeanRadius()

   Returns the estimated mean radius of the fill, assuming a cylindric shape

   **Signature:** ``getEstimatedMeanRadius() -> double``

   **Returns:** (``float``) the estimated mean radius

.. method:: getMetric()

   **Signature:** ``getMetric() -> CostType``

   **Returns:** ``Any``

.. method:: getNodeList()

   Returns the list of nodes in the filled structure.

   **Signature:** ``getNodeList() -> List``

   **Returns:** (``List[Any]``) the list of nodes

.. method:: getSourcePaths()

   Returns the set of source paths for the filled structure.

   **Signature:** ``getSourcePaths() -> Set``

   **Returns:** (``Set[Any]``) the set of source paths

.. method:: getSourcePathsStringHuman()

   **Signature:** ``getSourcePathsStringHuman() -> String``

   **Returns:** ``str``

.. method:: getSourcePathsStringMachine()

   **Signature:** ``getSourcePathsStringMachine() -> String``

   **Returns:** ``str``

.. method:: getThreshold()

   **Signature:** ``getThreshold() -> double``

   **Returns:** ``float``

.. method:: getVolume()

   Returns the Fill volume. It assumes that the volume is just the number of sub-threshold nodes multiplied by x_spacing * y_spacing * z_spacing.

   **Signature:** ``getVolume() -> double``

   **Returns:** (``float``) the volume


FillConverter
-------------

.. method:: getFillerStack()

   Merges the input `FillerThread`s into a single `SearchImageStack`. When a filled voxel position is present in multiple filler instances, the node with the lowest g-score is chosen for inclusion in the merged stack.

   **Signature:** ``getFillerStack() -> SearchImageStack``

   **Returns:** (``SearchImageStack``) the merged filler stack


FillerThread
------------

.. method:: getDistanceAtPoint(xd, yd, zd)

   **Signature:** ``getDistanceAtPoint(double, double, double) -> double``

   **Parameters:**

   * **xd** (``float``)
   * **yd** (``float``)
   * **zd** (``float``)

   **Returns:** ``float``

.. method:: getExitReason()

   **Signature:** ``getExitReason() -> int``

   **Returns:** ``int``

.. method:: getFill()

   **Signature:** ``getFill() -> Fill``

   **Returns:** ``Fill``

.. method:: getNodesAsImage()

   **Signature:** ``getNodesAsImage() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getNodesAsImageFromGoal()

   **Signature:** ``getNodesAsImageFromGoal() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getNodesAsImageFromStart()

   **Signature:** ``getNodesAsImageFromStart() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``

.. method:: getSourcePaths()

   Returns the paths this fill originated from.

   **Signature:** ``getSourcePaths() -> Set``

   **Returns:** (``Set[Any]``) the source paths (empty if undefined)

.. method:: getThreshold()

   **Signature:** ``getThreshold() -> double``

   **Returns:** ``float``


FillerThreadArtist
------------------

.. method:: getSearch()

   **Signature:** ``getSearch() -> SearchInterface``

   **Returns:** ``Any``


FlyCircuitLoader
----------------

.. method:: getReader(cellId)

   Gets the SWC data associated with the specified cell ID as a reader

   **Signature:** ``getReader(String) -> BufferedReader``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Any``) the character stream containing the data, or null if cell ID was not found or could not be retrieved

.. method:: getReconstructionURL(cellId)

   Gets the URL of the SWC file associated with the specified cell ID.

   **Signature:** ``getReconstructionURL(String) -> String``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``str``) the reconstruction URL

.. method:: getTree(cellId)

   Gets the collection of Paths for the specified cell ID

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Tree``) the data for the specified cell as a `Tree`, or null if data could not be retrieved

.. method:: isDatabaseAvailable()

   Checks whether a connection to the FlyCircuit database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established, false otherwise


GWDTTracer
----------

.. method:: getCaliperFraction()

   **Signature:** ``getCaliperFraction() -> double``

   **Returns:** ``float``

.. method:: getMaxGapVoxels()

   **Signature:** ``getMaxGapVoxels() -> int``

   **Returns:** ``int``

.. method:: getMinSomaDistance()

   **Signature:** ``getMinSomaDistance() -> double``

   **Returns:** ``float``

.. method:: getNSomas()

   **Signature:** ``getNSomas() -> int``

   **Returns:** ``int``

.. method:: getRootStrategy()

   **Signature:** ``getRootStrategy() -> int``

   **Returns:** ``int``

.. method:: getScoreMap()

   **Signature:** ``getScoreMap() -> RandomAccessibleInterval``

   **Returns:** ``Any``

.. method:: getSomaRoi()

   **Signature:** ``getSomaRoi() -> Roi``

   **Returns:** ``Any``

.. method:: getTipExtensionDistance()

   **Signature:** ``getTipExtensionDistance() -> double``

   **Returns:** ``float``

.. method:: getTracedRegionBuffer()

   **Signature:** ``getTracedRegionBuffer() -> int``

   **Returns:** ``int``

.. method:: isAllowVoxelGap()

   **Signature:** ``isAllowVoxelGap() -> boolean``

   **Returns:** ``bool``

.. method:: isAutoFilter()

   **Signature:** ``isAutoFilter() -> boolean``

   **Returns:** ``bool``

.. method:: isParallelBranchPruneEnabled()

   **Signature:** ``isParallelBranchPruneEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isPathFittingEnabled()

   **Signature:** ``isPathFittingEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isVerbose()

   **Signature:** ``isVerbose() -> boolean``

   **Returns:** ``bool``

.. method:: setMinBranchIntensityLength(threshold)

   **Signature:** ``setMinBranchIntensityLength(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setMinSegmentLength(lengthInPhysicalUnits)

   **Signature:** ``setMinSegmentLength(double) -> void``

   **Parameters:**

   * **lengthInPhysicalUnits** (``float``)

   **Returns:** ``None``

.. method:: setSmoothWindowSize(windowSize)

   **Signature:** ``setSmoothWindowSize(int) -> void``

   **Parameters:**

   * **windowSize** (``int``)

   **Returns:** ``None``


GWDTTracerFactory
-----------------

.. method:: getCurrentThresholds()

   **Signature:** ``getCurrentThresholds() -> long[]``

   **Returns:** ``List[int]``


GroupedTreeStatistics
---------------------

.. method:: getBoxPlot(measurement)

   Assembles a Box and Whisker Plot for the specified feature.

   **Signature:** ``getBoxPlot(String) -> SNTChart``

   **Parameters:**

   * **measurement** (``str``)

   **Returns:** ``SNTChart``

.. method:: getFlowPlot(feature, depth)

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.

   **Signature:** ``getFlowPlot(String, int) -> SNTChart``

   **Parameters:**

   * **feature** (``str``): - the feature ("Cable length", "No. of branch points", "No. of tips", etc.). Note that the majority of TreeStatistics.getAllMetrics() metrics are currently not supported.
   * **depth** (``int``)

   **Returns:** (``SNTChart``) the SNTChart holding the flow plot

.. method:: getGroupStats(groupLabel)

   Gets the group statistics.

   **Signature:** ``getGroupStats(String) -> MultiTreeStatistics``

   **Parameters:**

   * **groupLabel** (``str``): - the unique label identifying the group

   **Returns:** (``MultiTreeStatistics``) the group statistics or null if no group is mapped to `groupLabel`

.. method:: getGroups()

   Gets the group identifiers currently queued for analysis.

   **Signature:** ``getGroups() -> List``

   **Returns:** (``List[Any]``) the group identifiers

.. method:: getHistogram(measurement)

   Gets the relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **measurement** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram

.. method:: getN(groupLabel)

   Gets the number of Trees in a specified group.

   **Signature:** ``getN(String) -> int``

   **Parameters:**

   * **groupLabel** (``str``): - the unique label identifying the group

   **Returns:** (``int``) the number of Trees or -1 if no group is mapped to `groupLabel`

.. method:: getPolarHistogram(measurement)

   Gets the relative frequencies histogram for a univariate measurement as a polar (rose) plot assuming a data range between [0-360]. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getPolarHistogram(String) -> SNTChart``

   **Parameters:**

   * **measurement** (``str``): - the measurement (e.g., MultiTreeStatistics.AVG_REMOTE_ANGLE

   **Returns:** (``SNTChart``) the frame holding the histogram


GrowthAnalysisResults
---------------------

.. method:: getFrameInterval()

   **Signature:** ``getFrameInterval() -> double``

   **Returns:** ``float``

.. method:: getNeuriteCount()

   **Signature:** ``getNeuriteCount() -> int``

   **Returns:** ``int``

.. method:: getNeuriteGrowthData()

   **Signature:** ``getNeuriteGrowthData() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getNeuritePhases()

   **Signature:** ``getNeuritePhases() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getNeuritesByPattern(criterion)

   **Signature:** ``getNeuritesByPattern(NeuriteSelectionCriterion) -> List``

   **Parameters:**

   * **criterion** (``Any``)

   **Returns:** ``List[Any]``

.. method:: getPhaseDistribution()

   **Signature:** ``getPhaseDistribution() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getPhaseDistributionForVisualization()

   **Signature:** ``getPhaseDistributionForVisualization() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getPhasePercentage(phaseType)

   **Signature:** ``getPhasePercentage(GrowthPhaseType) -> double``

   **Parameters:**

   * **phaseType** (``Any``)

   **Returns:** ``float``

.. method:: getSummaryStatistics()

   **Signature:** ``getSummaryStatistics() -> GrowthSummaryStatistics``

   **Returns:** ``Any``

.. method:: getTimeUnits()

   **Signature:** ``getTimeUnits() -> String``

   **Returns:** ``str``

.. method:: getTotalPhaseCount()

   **Signature:** ``getTotalPhaseCount() -> int``

   **Returns:** ``int``


GrowthAnalyzer
--------------

.. method:: getAbsoluteWindowSize()

   **Signature:** ``getAbsoluteWindowSize() -> int``

   **Returns:** ``int``

.. method:: getBaseThresholdFraction()

   **Signature:** ``getBaseThresholdFraction() -> double``

   **Returns:** ``float``

.. method:: getPhaseSensitivity()

   **Signature:** ``getPhaseSensitivity() -> double``

   **Returns:** ``float``

.. method:: getRapidThresholdMultiple()

   **Signature:** ``getRapidThresholdMultiple() -> double``

   **Returns:** ``float``

.. method:: getRetractionThreshold()

   **Signature:** ``getRetractionThreshold() -> double``

   **Returns:** ``float``

.. method:: getWindowSizeFraction()

   **Signature:** ``getWindowSizeFraction() -> double``

   **Returns:** ``float``

.. method:: isUseAbsoluteWindowSize()

   **Signature:** ``isUseAbsoluteWindowSize() -> boolean``

   **Returns:** ``bool``

.. method:: isUseGlobalThresholds()

   **Signature:** ``isUseGlobalThresholds() -> boolean``

   **Returns:** ``bool``

.. method:: setAbsoluteWindowSize(absoluteWindowSize)

   **Signature:** ``setAbsoluteWindowSize(int) -> void``

   **Parameters:**

   * **absoluteWindowSize** (``int``)

   **Returns:** ``None``

.. method:: setMinPathLength(minPathLength)

   **Signature:** ``setMinPathLength(double) -> void``

   **Parameters:**

   * **minPathLength** (``float``)

   **Returns:** ``None``

.. method:: setUseAbsoluteWindowSize(useAbsoluteWindowSize)

   **Signature:** ``setUseAbsoluteWindowSize(boolean) -> void``

   **Parameters:**

   * **useAbsoluteWindowSize** (``bool``)

   **Returns:** ``None``


IOUtils
-------

.. method:: getReconstructionExtensions()

   Returns the extensions (lower case, without the leading period) of the supported reconstruction formats that can be identified by name alone, i.e., not including Neurolucida .xml files

   **Signature:** ``getReconstructionExtensions() -> String[]``

   **Returns:** (``List[str]``) a new array of extensions, e.g., "swc", "traces", etc.

.. method:: isReconstructionFile(file)

   Checks if a file is a reconstruction file. Apart from the extension-only check, XML files are recognized as Neurolucida reconstructions if `sniffXml` is true and their header is that of a Neurolucida file. Only the first few KB of XML files are read.

   **Signature:** ``isReconstructionFile(File) -> boolean``

   **Parameters:**

   * **file** (``str``): - the file to be tested

   **Returns:** (``bool``) true if the file is a supported reconstruction file

.. method:: isSWCFile(file)

   Checks if a file has an SWC extension, i.e., .swc or .eswc (extended SWC, which holds extra columns that are ignored on import). Case-insensitive.

   **Signature:** ``isSWCFile(File) -> boolean``

   **Parameters:**

   * **file** (``str``): - the file to be tested

   **Returns:** (``bool``) true if the file name ends with ".swc" or ".eswc"


ImageParser2D
-------------

.. method:: getCircumferencePoints(cx, cy, radius)

   **Signature:** ``getCircumferencePoints(int, int, int) -> int[][]``

   **Parameters:**

   * **cx** (``int``)
   * **cy** (``int``)
   * **radius** (``int``)

   **Returns:** ``List[List[int]]``

.. method:: getIsotropicVoxelSize()

   **Signature:** ``getIsotropicVoxelSize() -> double``

   **Returns:** ``float``

.. method:: getMask()

   **Signature:** ``getMask() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getMaskProcessor(floatProcessor, maskValues)

   **Signature:** ``getMaskProcessor(boolean, double[]) -> ImageProcessor``

   **Parameters:**

   * **floatProcessor** (``bool``)
   * **maskValues** (``List[float]``)

   **Returns:** ``Any``

.. method:: getProfile()

   **Signature:** ``getProfile() -> Profile``

   **Returns:** ``Profile``

.. method:: isRetrieveIntDensitiesSet()

   **Signature:** ``isRetrieveIntDensitiesSet() -> boolean``

   **Returns:** ``bool``


ImageParser3D
-------------

.. method:: getCircumferencePoints(cx, cy, radius)

   **Signature:** ``getCircumferencePoints(int, int, int) -> int[][]``

   **Parameters:**

   * **cx** (``int``)
   * **cy** (``int``)
   * **radius** (``int``)

   **Returns:** ``List[List[int]]``

.. method:: getIsotropicVoxelSize()

   **Signature:** ``getIsotropicVoxelSize() -> double``

   **Returns:** ``float``

.. method:: getMask()

   **Signature:** ``getMask() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getMaskProcessor(floatProcessor, maskValues)

   **Signature:** ``getMaskProcessor(boolean, double[]) -> ImageProcessor``

   **Parameters:**

   * **floatProcessor** (``bool``)
   * **maskValues** (``List[float]``)

   **Returns:** ``Any``

.. method:: getProfile()

   **Signature:** ``getProfile() -> Profile``

   **Returns:** ``Profile``

.. method:: isRetrieveIntDensitiesSet()

   **Signature:** ``isRetrieveIntDensitiesSet() -> boolean``

   **Returns:** ``bool``

.. method:: isSkipSingleVoxels()

   **Signature:** ``isSkipSingleVoxels() -> boolean``

   **Returns:** ``bool``


ImgUtils
--------

.. method:: exceedsVoxelCount(imgPlus, maxVoxels)

   Checks whether the spatial (X, Y, Z) volume of an `ImgPlus` has more voxels than the given limit. Channel and Time axes are ignored.

   **Signature:** ``exceedsVoxelCount(ImgPlus, long) -> boolean``

   **Parameters:**

   * **imgPlus** (``Any``): - the image to check
   * **maxVoxels** (``int``)

   **Returns:** (``bool``) `true` if the spatial volume exceeds the limit

.. method:: getCalibration(imgPlus)

   Extracts ImageJ1 Calibration from ImgPlus axes, including origin offsets.

   **Signature:** ``getCalibration(ImgPlus) -> Calibration``

   **Parameters:**

   * **imgPlus** (``Any``): - the source ImgPlus

   **Returns:** (``Any``) Calibration with pixel sizes, unit, and origins

.. method:: getCtSlice(imp)

   Extracts a channel/time slice by squeezing singleton dimensions.

Convenience overload that removes any singleton (size=1) channel or time dimensions from the image. Non-singleton C/T dimensions are preserved.

   **Signature:** ``getCtSlice(ImagePlus) -> RandomAccessibleInterval``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``Any``

.. method:: getCtSlice3d(dataset, channelIndex, frameIndex)

   Get a view of the `ImagePlus` at the specified channel and frame.

   **Signature:** ``getCtSlice3d(Dataset, int, int) -> RandomAccessibleInterval``

   **Parameters:**

   * **dataset** (``Any``): - the input ImagePlus
   * **channelIndex** (``int``)
   * **frameIndex** (``int``)

   **Returns:** (``Any``) the view RAI

.. method:: getLocalOmeZarrDir(path)

   Resolves a path to a local OME-Zarr (OME-NGFF v0.5) container directory. Accepts the directory itself or its `zarr.json` file (as returned by some file choosers)

   **Signature:** ``getLocalOmeZarrDir(String) -> File``

   **Parameters:**

   * **path** (``str``): - the path to check

   **Returns:** (``str``) the container directory, or null if `path` is not a local OME-Zarr v0.5 container

.. method:: getOmeZarrCalibration(path)

   Reads the spatial calibration from the root metadata of a local OME-Zarr (OME-NGFF v0.5) container

   **Signature:** ``getOmeZarrCalibration(String) -> OmeZarrCalibration``

   **Parameters:**

   * **path** (``str``): - the container directory (or its

   **Returns:** (``Any``) the calibration of the first multiscale image, or null if unavailable

.. method:: getOrigin(img, axisType)

   Get the origin offset for a specific axis from an ImgPlus.

   **Signature:** ``getOrigin(ImgPlus, AxisType) -> double``

   **Parameters:**

   * **img** (``Any``): - the ImgPlus
   * **axisType** (``Any``)

   **Returns:** (``float``) the origin offset in calibrated units, or 0 if not found

.. method:: getOrigins(img)

   Get the origin offsets as {xOrigin, yOrigin, zOrigin} from an ImgPlus.

   **Signature:** ``getOrigins(ImgPlus) -> double[]``

   **Parameters:**

   * **img** (``Any``): - the ImgPlus

   **Returns:** (``List[float]``) array of {xOrigin, yOrigin, zOrigin} in calibrated units

.. method:: getSpacing(img)

   Returns the voxel spacing for a specific axis type, defaulting to 1.0 if the axis is absent or has zero scale. Unlike `getSpacing(ImgPlus)`, this is axis-order-independent.

   **Signature:** ``getSpacing(ImgPlus) -> double[]``

   **Parameters:**

   * **img** (``Any``)

   **Returns:** ``List[float]``

.. method:: getSpacingUnits(img)

   Extracts spacing units from an ImgPlus.

   **Signature:** ``getSpacingUnits(ImgPlus) -> String``

   **Parameters:**

   * **img** (``Any``): - the image

   **Returns:** (``str``) the unit string (e.g., "µm"), or null if not calibrated

.. method:: getXYZCImage(imp)

   Gets a 4D (X, Y, Z, C) view of the `ImagePlus` at the current time frame, retaining all channels. This is useful for multichannel/spectral operations that need access to all channel data simultaneously.

The returned RAI has axis order [X, Y, Z, C], obtained from the canonical 5D [X, Y, C, Z, T] representation by fixing T and permuting C past Z.

   **Signature:** ``getXYZCImage(ImagePlus) -> RandomAccessibleInterval``

   **Parameters:**

   * **imp** (``Any``): - the input ImagePlus (must have at least 2 channels)

   **Returns:** (``Any``) 4D RAI with axis order [X, Y, Z, C], or null if the image has fewer than 2 channels

.. method:: hasN5ZarrMetadata(dir)

   Checks whether a local directory has the root metadata of an N5 or Zarr (v2/v3) container, i.e., whether it can be opened as one. An empty or incomplete directory (hidden files such as `.DS_Store` do not count) fails this check. Does not validate the metadata's content

   **Signature:** ``hasN5ZarrMetadata(File) -> boolean``

   **Parameters:**

   * **dir** (``str``): - the directory to check

   **Returns:** (``bool``) true if `dir` is a directory containing `zarr.json`, `.zgroup`, `.zarray`, `.zattrs` or `attributes.json`

.. method:: hasXYZLeading(img)

   Returns whether the first three axes of an image are X, Y and Z (in that order)

   **Signature:** ``hasXYZLeading(ImgPlus) -> boolean``

   **Parameters:**

   * **img** (``Any``)

   **Returns:** ``bool``

.. method:: isBinary(rai)

   **Signature:** ``isBinary(RandomAccessibleInterval) -> boolean``

   **Parameters:**

   * **rai** (``Any``)

   **Returns:** ``bool``

.. method:: isLabelImage(img)

   Checks whether a `RandomAccessibleInterval` appears to be a label image, using a default maximum of 500 classes.

   **Signature:** ``isLabelImage(RandomAccessibleInterval) -> boolean``

   **Parameters:**

   * **img** (``Any``): - the image to check

   **Returns:** (``bool``) `true` if the image passes label-image heuristics

.. method:: isMultiChannelRGB(img)

   Checks if an ImgPlus appears to be a multi-channel RGB image (3 channels of 8-bit data, not packed ARGB).

   **Signature:** ``isMultiChannelRGB(ImgPlus) -> boolean``

   **Parameters:**

   * **img** (``Any``)

   **Returns:** ``bool``

.. method:: isRGB(img)

   Checks if an ImgPlus contains packed RGB data (ARGBType).

   **Signature:** ``isRGB(ImgPlus) -> boolean``

   **Parameters:**

   * **img** (``Any``): - the image to check

   **Returns:** (``bool``) true if the image uses ARGBType pixels


ImpUtils
--------

.. method:: getCT(imp, channel, frame)

   **Signature:** ``getCT(ImagePlus, int, int) -> ImagePlus``

   **Parameters:**

   * **imp** (``Any``)
   * **channel** (``int``)
   * **frame** (``int``)

   **Returns:** ``Any``

.. method:: getChannel(imp, channel)

   **Signature:** ``getChannel(ImagePlus, int) -> ImagePlus``

   **Parameters:**

   * **imp** (``Any``)
   * **channel** (``int``)

   **Returns:** ``Any``

.. method:: getChannelStack(imp, channel)

   Returns a lightweight read-only view of a single channel as an ImageStack. Unlike `getChannel(ImagePlus, int)`, the returned stack shares the underlying pixel arrays with the source image (no data copy), making it suitable for read-only access on large multichannel images.

   **Signature:** ``getChannelStack(ImagePlus, int) -> ImageStack``

   **Parameters:**

   * **imp** (``Any``): - the source image
   * **channel** (``int``)

   **Returns:** (``Any``) the channel's ImageStack (shared pixel data)

.. method:: getCurrentImage()

   **Signature:** ``getCurrentImage() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getFilePath(imp)

   Returns the file path of an image.

   **Signature:** ``getFilePath(ImagePlus) -> String``

   **Parameters:**

   * **imp** (``Any``): - the image to be parsed

   **Returns:** (``str``) the absolute file path of the image or "unknown" if not known

.. method:: getForegroundRect(imp, backgroundValue)

   Returns the cropping rectangle around non-background values, considering all slices of the stack.

   **Signature:** ``getForegroundRect(ImagePlus, Number) -> Roi``

   **Parameters:**

   * **imp** (``Any``): - The image to be parsed
   * **backgroundValue** (``Union[int, float]``)

   **Returns:** (``Any``) the rectangular ROI defining non-background bounds, or null if all pixels are background

.. method:: getFrame(imp, frame)

   **Signature:** ``getFrame(ImagePlus, int) -> ImagePlus``

   **Parameters:**

   * **imp** (``Any``)
   * **frame** (``int``)

   **Returns:** ``Any``

.. method:: getMIP(imps)

   **Signature:** ``getMIP(Collection) -> ImagePlus``

   **Parameters:**

   * **imps** (``List[Any]``)

   **Returns:** ``Any``

.. method:: getMagnification(imp)

   **Signature:** ``getMagnification(ImagePlus) -> double``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** (``float``) the Image current magnification. A value between 0.0139 (1.4%), and 32 (3200%) or -1, if the zoom factor could not be assessed.

.. method:: getMinMax(imp)

   **Signature:** ``getMinMax(ImagePlus) -> double[]``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``List[float]``

.. method:: getNonSNTOpenImages()

   Returns all currently open images in ImageJ that were not created by SNT.

   **Signature:** ``getNonSNTOpenImages() -> ImagePlus[]``

   **Returns:** (``List[Any]``) array of open `ImagePlus` instances, or an empty array if non-SNT created images are open

.. method:: getOpenImages()

   Returns all currently open images in ImageJ's `WindowManager`.

   **Signature:** ``getOpenImages() -> ImagePlus[]``

   **Returns:** (``List[Any]``) array of open `ImagePlus` instances, or an empty array if none are open

.. method:: getSliceLabels(stack)

   **Signature:** ``getSliceLabels(ImageStack) -> List``

   **Parameters:**

   * **stack** (``Any``)

   **Returns:** ``List[Any]``

.. method:: getSystemClipboard(asMultiChannel)

   Retrieves an ImagePlus from the system clipboard

   **Signature:** ``getSystemClipboard(boolean) -> ImagePlus``

   **Parameters:**

   * **asMultiChannel** (``bool``): - if true and clipboard contains RGB data image is returned as composite (RGB/8-bit grayscale otherwise)

   **Returns:** (``Any``) the image stored in the system clipboard or null if no image found

.. method:: isBinary(imp)

   **Signature:** ``isBinary(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``bool``

.. method:: isDisplayCanvas(imp)

   Checks whether an image is a placeholder canvas

   **Signature:** ``isDisplayCanvas(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the image to be checked

   **Returns:** (``bool``) true if `setIsDisplayCanvas(ij.ImagePlus)` was previous called on `imp`

.. method:: isMaterializedCrop(imp)

   Checks whether an image is a materialized crop of a streamed volume.

   **Signature:** ``isMaterializedCrop(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the image to be checked

   **Returns:** (``bool``) true if `setIsMaterializedCrop(ij.ImagePlus)` was previous called on `imp`

.. method:: isPointVisible(imp, x, y)

   Checks if a given point (in image coordinates) is currently visible in an image

   **Signature:** ``isPointVisible(ImagePlus, int, int) -> boolean``

   **Parameters:**

   * **imp** (``Any``): - the ImagePlus to check
   * **x** (``int``)
   * **y** (``int``)

   **Returns:** (``bool``) true if the point is visible in the current view, false otherwise

.. method:: isVirtualStack(imp)

   **Signature:** ``isVirtualStack(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``bool``


InsectBrainCompartment
----------------------

.. method:: getAncestor(level)

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``getAncestor(int) -> BrainAnnotation``

   **Parameters:**

   * **level** (``int``): - the ancestor level as negative 1-based index. E.g.,

   **Returns:** (``Any``) the ancestor at the given level

.. method:: getMesh()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``getMesh() -> OBJMesh``

   **Returns:** ``OBJMesh``

.. method:: getOntologyDepth()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``getOntologyDepth() -> int``

   **Returns:** ``int``

.. method:: getParent()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``getParent() -> BrainAnnotation``

   **Returns:** ``Any``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isChildOf(annotation)

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``isChildOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **annotation** (``Any``)

   **Returns:** ``bool``

.. method:: isMeshAvailable()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``isMeshAvailable() -> boolean``

   **Returns:** ``bool``

.. method:: isParentOf(parentCompartment)

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``isParentOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **parentCompartment** (``Any``)

   **Returns:** ``bool``


InsectBrainLoader
-----------------

.. method:: getAnnotations()

   Gets the brain compartment annotations for this neuron.

   **Signature:** ``getAnnotations() -> List``

   **Returns:** (``List[Any]``) list of InsectBrainCompartment annotations, or null if not available

.. method:: getMeshes()

   Gets the 3D meshes associated with this neuron's brain compartments.

   **Signature:** ``getMeshes() -> List``

   **Returns:** (``List[Any]``) list of OBJMesh objects representing brain compartments

.. method:: getNeuronInfo()

   **Signature:** ``getNeuronInfo() -> NeuronInfo``

   **Returns:** ``Any``

.. method:: getTree()

   Gets the collection of Paths for the specified cell ID

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the data for the specified cell as a `Tree`, or null if data could not be retrieved

.. method:: isDatabaseAvailable()

   Checks whether a connection to the Insect Brain Database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HTTP connection could be established


InsectBrainUtils
----------------

.. method:: getAllNeuronIDs()

   **Signature:** ``getAllNeuronIDs() -> List``

   **Returns:** ``List[Any]``

.. method:: getAllSpecies()

   **Signature:** ``getAllSpecies() -> List``

   **Returns:** ``List[Any]``

.. method:: getBrainCompartments(speciesId, sex)

   **Signature:** ``getBrainCompartments(int, String) -> List``

   **Parameters:**

   * **speciesId** (``int``)
   * **sex** (``str``)

   **Returns:** ``List[Any]``

.. method:: getBrainJSON(speciesId)

   **Signature:** ``getBrainJSON(int) -> JSONObject``

   **Parameters:**

   * **speciesId** (``int``)

   **Returns:** ``Any``

.. method:: getBrainMeshes(speciesId, sex)

   **Signature:** ``getBrainMeshes(int, String) -> List``

   **Parameters:**

   * **speciesId** (``int``)
   * **sex** (``str``)

   **Returns:** ``List[Any]``

.. method:: getSpeciesNeuronIDs(speciesId)

   **Signature:** ``getSpeciesNeuronIDs(int) -> List``

   **Parameters:**

   * **speciesId** (``int``)

   **Returns:** ``List[Any]``


LabelsToSeeds
-------------

.. method:: isBinaryMask(imp)

   **Signature:** ``isBinaryMask(ImagePlus) -> boolean``

   **Parameters:**

   * **imp** (``Any``)

   **Returns:** ``bool``


LinearProfileStats
------------------

.. method:: getBranchingIndex(fittedData)

   **Signature:** ``getBranchingIndex(boolean) -> double``

   **Parameters:**

   * **fittedData** (``bool``)

   **Returns:** ``float``

.. method:: getCenteredMaximum()

   **Signature:** ``getCenteredMaximum() -> ShollPoint``

   **Returns:** ``Any``

.. method:: getCentroid()

   **Signature:** ``getCentroid() -> ShollPoint``

   **Returns:** ``Any``

.. method:: getEnclosingRadius(cutoff)

   **Signature:** ``getEnclosingRadius(double) -> double``

   **Parameters:**

   * **cutoff** (``float``)

   **Returns:** ``float``

.. method:: getFitYValues()

   **Signature:** ``getFitYValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getIndexOfInters(fittedData, inters)

   **Signature:** ``getIndexOfInters(boolean, double) -> int``

   **Parameters:**

   * **fittedData** (``bool``)
   * **inters** (``float``)

   **Returns:** ``int``

.. method:: getIndexOfRadius(radius)

   **Signature:** ``getIndexOfRadius(double) -> int``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``int``

.. method:: getIntersectingRadii()

   **Signature:** ``getIntersectingRadii() -> int``

   **Returns:** ``int``

.. method:: getKurtosis()

   **Signature:** ``getKurtosis() -> double``

   **Returns:** ``float``

.. method:: getMax()

   **Signature:** ``getMax() -> double``

   **Returns:** ``float``

.. method:: getMaxEvaluations()

   **Signature:** ``getMaxEvaluations() -> int``

   **Returns:** ``int``

.. method:: getMaxima()

   **Signature:** ``getMaxima() -> ArrayList``

   **Returns:** ``List[Any]``

.. method:: getMean()

   **Signature:** ``getMean() -> double``

   **Returns:** ``float``

.. method:: getMeanValueOfPolynomialFit(lowerBound, upperBound)

   **Signature:** ``getMeanValueOfPolynomialFit(double, double) -> double``

   **Parameters:**

   * **lowerBound** (``float``)
   * **upperBound** (``float``)

   **Returns:** ``float``

.. method:: getMedian()

   **Signature:** ``getMedian() -> double``

   **Returns:** ``float``

.. method:: getMin()

   **Signature:** ``getMin() -> double``

   **Returns:** ``float``

.. method:: getPolygonCentroid()

   **Signature:** ``getPolygonCentroid() -> ShollPoint``

   **Returns:** ``Any``

.. method:: getPolynomial()

   **Signature:** ``getPolynomial() -> PolynomialFunction``

   **Returns:** ``Any``

.. method:: getPolynomialAsString(detailed)

   **Signature:** ``getPolynomialAsString(boolean) -> String``

   **Parameters:**

   * **detailed** (``bool``)

   **Returns:** ``str``

.. method:: getPolynomialDegree()

   **Signature:** ``getPolynomialDegree() -> int``

   **Returns:** ``int``

.. method:: getPolynomialMaxima(lowerBound, upperBound, initialGuess)

   **Signature:** ``getPolynomialMaxima(double, double, double) -> Set``

   **Parameters:**

   * **lowerBound** (``float``)
   * **upperBound** (``float``)
   * **initialGuess** (``float``)

   **Returns:** ``Set[Any]``

.. method:: getPrimaryBranches()

   **Signature:** ``getPrimaryBranches() -> double``

   **Returns:** ``float``

.. method:: getRSquaredOfFit(adjusted)

   **Signature:** ``getRSquaredOfFit(boolean) -> double``

   **Parameters:**

   * **adjusted** (``bool``)

   **Returns:** ``float``

.. method:: getRamificationIndex()

   **Signature:** ``getRamificationIndex() -> double``

   **Returns:** ``float``

.. method:: getSkewness()

   **Signature:** ``getSkewness() -> double``

   **Returns:** ``float``

.. method:: getSum()

   **Signature:** ``getSum() -> double``

   **Returns:** ``float``

.. method:: getSumSq()

   **Signature:** ``getSumSq() -> double``

   **Returns:** ``float``

.. method:: getVariance()

   **Signature:** ``getVariance() -> double``

   **Returns:** ``float``

.. method:: getXValues()

   **Signature:** ``getXValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getYValues()

   **Signature:** ``getYValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: isPrimaryBranchesInferred()

   **Signature:** ``isPrimaryBranchesInferred() -> boolean``

   **Returns:** ``bool``


ListSearchImage
---------------

.. method:: getValue(x, y)

   **Signature:** ``getValue(int, int) -> Object``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)

   **Returns:** ``Any``


MapSearchImage
--------------

.. method:: getValue(x, y)

   **Signature:** ``getValue(int, int) -> Object``

   **Parameters:**

   * **x** (``int``)
   * **y** (``int``)

   **Returns:** ``Any``


MouseLightLoader
----------------

.. method:: getAllLoaders()

   Gets the loaders for all the cells publicly available in the MouseLight database.

   **Signature:** ``getAllLoaders() -> List``

   **Returns:** (``List[Any]``) the list of loaders

.. method:: getDOI()

   Gets the DOI for this neuron.

   **Signature:** ``getDOI() -> String``

   **Returns:** (``str``) the DOI string, or null if not available

.. method:: getID()

   Gets the neuron ID for this loader.

   **Signature:** ``getID() -> String``

   **Returns:** (``str``) the neuron ID

.. method:: getJSON()

   Gets all the data associated with this reconstruction as a JSON object.

   **Signature:** ``getJSON() -> JSONObject``

   **Returns:** (``Any``) the JSON data (null if data could not be retrieved).

.. method:: getNeuronCount()

   Gets the number of cells publicly available in the MouseLight database.

   **Signature:** ``getNeuronCount() -> int``

   **Returns:** (``int``) the number of available cells, or -1 if the database could not be reached.

.. method:: getNodes()

   Script-friendly method to extract the nodes of a cellular compartment.

   **Signature:** ``getNodes() -> TreeSet``

   **Returns:** ``Set[Any]``

.. method:: getSWC()

   Gets all the data associated with this reconstruction in the SWC format.

   **Signature:** ``getSWC() -> String``

   **Returns:** (``str``) the SWC data (null if data could not be retrieved).

.. method:: getSampleInfo()

   Gets sample information for this neuron.

   **Signature:** ``getSampleInfo() -> String``

   **Returns:** (``str``) the sample information as a JSON string, or null if not available

.. method:: getSomaCompartment()

   Gets the brain compartment containing the soma.

   **Signature:** ``getSomaCompartment() -> AllenCompartment``

   **Returns:** (``AllenCompartment``) the AllenCompartment containing the soma

.. method:: getSomaLocation()

   Gets the soma location for this neuron.

   **Signature:** ``getSomaLocation() -> SWCPoint``

   **Returns:** (``SWCPoint``) the SWCPoint representing the soma location

.. method:: getTree()

   Script-friendly method to extract the entire neuron as a collection of Paths.

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the neuron as a `Tree`, or null if data could not be retrieved

.. method:: isDatabaseAvailable()

   Checks whether a connection to the MouseLight database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established


MouseLightQuerier
-----------------

.. method:: getAllIDs()

   Gets all available neuron IDs from the database.

   **Signature:** ``getAllIDs() -> List``

   **Returns:** (``List[Any]``) list of all neuron IDs

.. method:: getIDs(compartment)

   Gets neuron IDs matching the specified collection of IDs or DOIs.

   **Signature:** ``getIDs(AllenCompartment) -> List``

   **Parameters:**

   * **compartment** (``AllenCompartment``): - the collection of IDs or DOIs to search for

   **Returns:** (``List[Any]``) list of matching neuron IDs

.. method:: getNeuronCount()

   Gets the number of cells publicly available in the MouseLight database.

   **Signature:** ``getNeuronCount() -> int``

   **Returns:** (``int``) the number of available cells, or -1 if the database could not be reached.

.. method:: isDatabaseAvailable()

   Checks whether a connection to the MouseLight database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established


MultiSpectralRefiner
--------------------

.. method:: getFinalNodeCosts()

   Returns the per-node cost values after refinement. Only valid after `call()` has been invoked.

   **Signature:** ``getFinalNodeCosts() -> double[]``

   **Returns:** (``List[float]``) array of per-node costs (same length as the path), or null if call() hasn't run

.. method:: getFinalPenalty()

   Returns the total penalty of the path after refinement. Only valid after `call()` has been invoked.

   **Signature:** ``getFinalPenalty() -> double``

   **Returns:** ``float``

.. method:: getInitialNodeCosts()

   Returns the per-node cost values before refinement. Only valid after `call()` has been invoked.

   **Signature:** ``getInitialNodeCosts() -> double[]``

   **Returns:** (``List[float]``) array of per-node costs (same length as the path), or null if call() hasn't run

.. method:: getInitialPenalty()

   Returns the total penalty of the path before refinement. Only valid after `call()` has been invoked.

   **Signature:** ``getInitialPenalty() -> double``

   **Returns:** ``float``


MultiTreeColorMapper
--------------------

.. method:: getAvailableHeatmapLuts()

   **Signature:** ``getAvailableHeatmapLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvailableLuts()

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getColor(mappedValue)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(mappedValue)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable()

   **Signature:** ``getColorTable() -> ColorTable``

   **Returns:** ``Any``

.. method:: getMeasurement()

   Description copied from class: `ColorMapper`

   **Signature:** ``getMeasurement() -> String``

   **Returns:** (``str``) the unit, or an empty string if unknown/not applicable

.. method:: getMeasurementLabel()

   **Signature:** ``getMeasurementLabel() -> String``

   **Returns:** ``str``

.. method:: getMetrics()

   Gets the list of supported mapping metrics.

   **Signature:** ``getMetrics() -> List``

   **Returns:** ``List[Any]``

.. method:: getMinMax()

   **Signature:** ``getMinMax() -> double[]``

   **Returns:** ``List[float]``

.. method:: getMultiViewer()

   Description copied from class: `TreeColorMapper`

   **Signature:** ``getMultiViewer() -> MultiViewer2D``

   **Returns:** (``MultiViewer2D``) the multi-viewer instance

.. method:: getNaNColor()

   **Signature:** ``getNaNColor() -> Color``

   **Returns:** ``Any``

.. method:: getSingleValueMetrics()

   Gets the list of single-value mapping metrics.

   **Signature:** ``getSingleValueMetrics() -> List``

   **Returns:** (``List[Any]``) the list of single-value mapping metrics.

.. method:: isIntegerScale()

   **Signature:** ``isIntegerScale() -> boolean``

   **Returns:** ``bool``

.. method:: isNodeMapping()

   **Signature:** ``isNodeMapping() -> boolean``

   **Returns:** ``bool``


MultiTreeStatistics
-------------------

.. method:: getAllMetrics()

   **Signature:** ``getAllMetrics() -> List``

   **Returns:** ``List[Any]``

.. method:: getAnnotatedLength(level)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getAnnotatedLength(int) -> Map``

   **Parameters:**

   * **level** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain compartments as keys, and cable lengths as values.

.. method:: getAnnotatedLengthHistogram()

   **Signature:** ``getAnnotatedLengthHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedLengthsByHemisphere(level)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getAnnotatedLengthsByHemisphere(int) -> Map``

   **Parameters:**

   * **level** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain compartments as keys, and cable lengths per hemisphere as values.

.. method:: getAnnotations()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getAnnotations() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvgBranchLength()

   **Signature:** ``getAvgBranchLength() -> double``

   **Returns:** ``float``

.. method:: getAvgContraction()

   **Signature:** ``getAvgContraction() -> double``

   **Returns:** ``float``

.. method:: getAvgFractalDimension()

   **Signature:** ``getAvgFractalDimension() -> double``

   **Returns:** ``float``

.. method:: getAvgFragmentation()

   **Signature:** ``getAvgFragmentation() -> double``

   **Returns:** ``float``

.. method:: getAvgPartitionAsymmetry()

   **Signature:** ``getAvgPartitionAsymmetry() -> double``

   **Returns:** ``float``

.. method:: getAvgRemoteBifAngle()

   **Signature:** ``getAvgRemoteBifAngle() -> double``

   **Returns:** ``float``

.. method:: getBoxPlot(measurement)

   Assembles a Box and Whisker Plot for the specified measurement (cell morphometry).

   **Signature:** ``getBoxPlot(String) -> SNTChart``

   **Parameters:**

   * **measurement** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``SNTChart``) the SNTChart holding the box plot

.. method:: getBranchPoints()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getBranchPoints() -> Set``

   **Returns:** (``Set[Any]``) the branch points positions

.. method:: getBranches()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getBranches() -> List``

   **Returns:** (``List[Any]``) the list of branches as Path objects.

.. method:: getCableLength()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getCableLength() -> double``

   **Returns:** ``float``

.. method:: getCableLengthNorm(compartment)

   **Signature:** ``getCableLengthNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **compartment** (``Any``)

   **Returns:** ``float``

.. method:: getConvexAnalyzer()

   **Signature:** ``getConvexAnalyzer() -> ConvexHullAnalyzer``

   **Returns:** ``ConvexHullAnalyzer``

.. method:: getConvexHullMetric(metric)

   **Signature:** ``getConvexHullMetric(String) -> double``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``float``

.. method:: getDepth()

   **Signature:** ``getDepth() -> double``

   **Returns:** ``float``

.. method:: getDescriptiveStats(metric)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getDescriptiveStats(String) -> DescriptiveStatistics``

   **Parameters:**

   * **metric** (``str``): - the measurement (TreeStatistics.N_NODES, TreeStatistics.NODE_RADIUS, etc.)

   **Returns:** (``Any``) the DescriptiveStatistics object.

.. method:: getFlowPlot(feature, annotations)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getFlowPlot(String, Collection) -> SNTChart``

   **Parameters:**

   * **feature** (``str``): - the feature ("Cable length", "No. of branch points", "No. of tips", etc.). Note that the majority of TreeStatistics.getAllMetrics() metrics are currently not supported.
   * **annotations** (``List[Any]``)

   **Returns:** (``SNTChart``) the SNTChart holding the flow plot

.. method:: getFractalDimension()

   **Signature:** ``getFractalDimension() -> List``

   **Returns:** ``List[Any]``

.. method:: getGroup()

   Gets the collection of Trees being analyzed.

   **Signature:** ``getGroup() -> Collection``

   **Returns:** (``List[Any]``) the Tree group

.. method:: getHeight()

   **Signature:** ``getHeight() -> double``

   **Returns:** ``float``

.. method:: getHighestPathOrder()

   **Signature:** ``getHighestPathOrder() -> int``

   **Returns:** ``int``

.. method:: getHistogram(metric)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``): - the measurement (TreeStatistics.N_NODES, TreeStatistics.NODE_RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram

.. method:: getInnerBranches()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getInnerBranches() -> List``

   **Returns:** (``List[Any]``) the list containing the "inner" branches. Note that these branches (Path segments) will not carry any connectivity information.

.. method:: getInnerLength()

   **Signature:** ``getInnerLength() -> double``

   **Returns:** ``float``

.. method:: getMetric(metric)

   **Signature:** ``getMetric(String) -> Number``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``Union[int, float]``

.. method:: getMetrics()

   Gets the list of metrics supported by MultiTreeStatistics.

Returns all the metrics that can be computed for groups of trees, including aggregate measures and group-specific statistics.

   **Signature:** ``getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metric names

.. method:: getNBranchPoints(annot)

   **Signature:** ``getNBranchPoints(BrainAnnotation) -> int``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``int``

.. method:: getNBranchPointsNorm(annot)

   **Signature:** ``getNBranchPointsNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``float``

.. method:: getNBranches()

   **Signature:** ``getNBranches() -> int``

   **Returns:** ``int``

.. method:: getNNodes()

   **Signature:** ``getNNodes() -> long``

   **Returns:** ``int``

.. method:: getNPaths()

   **Signature:** ``getNPaths() -> int``

   **Returns:** ``int``

.. method:: getNTips(annot)

   **Signature:** ``getNTips(BrainAnnotation) -> int``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``int``

.. method:: getNTipsNorm(annot)

   **Signature:** ``getNTipsNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``float``

.. method:: getNoSpinesOrVaricosities()

   **Signature:** ``getNoSpinesOrVaricosities() -> int``

   **Returns:** ``int``

.. method:: getNodeStatistics()

   **Signature:** ``getNodeStatistics() -> NodeStatistics``

   **Returns:** ``NodeStatistics``

.. method:: getParsedTree()

   **Signature:** ``getParsedTree() -> Tree``

   **Returns:** ``Tree``

.. method:: getPartitionAsymmetry()

   **Signature:** ``getPartitionAsymmetry() -> List``

   **Returns:** ``List[Any]``

.. method:: getPolarHistogram(metric)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getPolarHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``): - the metric to be plotted (e.g., TreeStatistics.BRANCH_EXTENSION_ANGLE_XY, TreeStatistics.PATH_EXT_ANGLE_XY, etc.)

   **Returns:** (``SNTChart``) the polar histogram chart

.. method:: getPrimaryBranches()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getPrimaryBranches() -> List``

   **Returns:** (``List[Any]``) the primary branches. Note that these branches (Path segments) will not carry any connectivity information.

.. method:: getPrimaryLength()

   **Signature:** ``getPrimaryLength() -> double``

   **Returns:** ``float``

.. method:: getPrimaryPaths()

   **Signature:** ``getPrimaryPaths() -> List``

   **Returns:** ``List[Any]``

.. method:: getRawValues(metric)

   **Signature:** ``getRawValues(String) -> SNTTable``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``SNTTable``

.. method:: getRemoteBifAngles()

   **Signature:** ``getRemoteBifAngles() -> List``

   **Returns:** ``List[Any]``

.. method:: getRootAngleAnalyzer()

   **Signature:** ``getRootAngleAnalyzer() -> RootAngleAnalyzer``

   **Returns:** ``RootAngleAnalyzer``

.. method:: getRootAngleMetric(metric)

   **Signature:** ``getRootAngleMetric(String) -> double``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``float``

.. method:: getShollAnalyzer()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getShollAnalyzer() -> ShollAnalyzer``

   **Returns:** (``ShollAnalyzer``) the ShollAnalyzer instance associated with this TreeStatistics instance

.. method:: getSpineOrVaricosityDensity()

   **Signature:** ``getSpineOrVaricosityDensity() -> double``

   **Returns:** ``float``

.. method:: getStrahlerAnalyzer()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getStrahlerAnalyzer() -> StrahlerAnalyzer``

   **Returns:** (``StrahlerAnalyzer``) the StrahlerAnalyzer instance associated with this TreeStatistics instance

.. method:: getStrahlerBifurcationRatio()

   **Signature:** ``getStrahlerBifurcationRatio() -> double``

   **Returns:** ``float``

.. method:: getStrahlerNumber()

   **Signature:** ``getStrahlerNumber() -> int``

   **Returns:** ``int``

.. method:: getSummaryStats(metric)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getSummaryStats(String) -> SummaryStatistics``

   **Parameters:**

   * **metric** (``str``): - the measurement (TreeStatistics.N_NODES, TreeStatistics.NODE_RADIUS, etc.)

   **Returns:** (``Any``) the SummaryStatistics object.

.. method:: getTable()

   **Signature:** ``getTable() -> DefaultGenericTable``

   **Returns:** ``Any``

.. method:: getTerminalBranches()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getTerminalBranches() -> List``

   **Returns:** (``List[Any]``) the terminal branches. Note that as per `Path.getSection(int, int)`, these branches will not carry any connectivity information.

.. method:: getTerminalLength()

   **Signature:** ``getTerminalLength() -> double``

   **Returns:** ``float``

.. method:: getTips()

   Description copied from class: `TreeStatistics`

   **Signature:** ``getTips() -> Set``

   **Returns:** (``Set[Any]``) the set of terminal points

.. method:: getUnit(metric)

   **Signature:** ``getUnit(String) -> String``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``str``

.. method:: getWidth()

   **Signature:** ``getWidth() -> double``

   **Returns:** ``float``

.. method:: isExactMetricMatch()

   The group is 3D if any of its (non-empty) trees is

   **Signature:** ``isExactMetricMatch() -> boolean``

   **Returns:** ``bool``

.. method:: isValid()

   **Signature:** ``isValid() -> boolean``

   **Returns:** ``bool``


NeuroMorphoLoader
-----------------

.. method:: getReader(cellId)

   Gets the SWC data ('CNG version') associated with the specified cell ID as a reader

   **Signature:** ``getReader(String) -> BufferedReader``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Any``) the character stream containing the data, or null if cell ID was not found or could not be retrieved

.. method:: getReconstructionURL(cellId)

   Gets the URL of the SWC file ('CNG version') associated with the specified cell ID.

   **Signature:** ``getReconstructionURL(String) -> String``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``str``) the reconstruction URL, or null if cell ID was not found or could not be retrieved

.. method:: getTree(cellId)

   Gets the collection of Paths for the specified cell ID

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **cellId** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Tree``) the data ('CNG version') for the specified cell as a `Tree`, or null if data could not be retrieved

.. method:: isDatabaseAvailable()

   Checks whether a connection to the NeuroMorpho database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established, false otherwise


NeurolucidaImporter
-------------------

.. method:: getCalibration()

   Returns the spatial calibration parsed from the file header.

   **Signature:** ``getCalibration() -> double[]``

   **Returns:** (``List[float]``) a double array {xScale, yScale, zSpacing} in the file's units

.. method:: getMarkerColors()

   Returns the colors for each parsed marker, in the same order as `getMarkerPoints()`.

   **Signature:** ``getMarkerColors() -> List``

   **Returns:** (``List[Any]``) list of marker colors (may contain nulls)

.. method:: getMarkerLabels()

   Returns the labels for each parsed marker, in the same order as `getMarkerPoints()`.

   **Signature:** ``getMarkerLabels() -> List``

   **Returns:** (``List[Any]``) list of marker labels

.. method:: getMarkerPoints()

   Returns the marker centroids parsed from `<marker>` elements. Each entry is a `double[3]` array of {x, y, z} coordinates in the file's coordinate system (typically micrometers).

   **Signature:** ``getMarkerPoints() -> List``

   **Returns:** (``List[Any]``) list of marker centroid positions

.. method:: getSpacingUnits()

   Returns the spacing units string (default "um").

   **Signature:** ``getSpacingUnits() -> String``

   **Returns:** (``str``) the spacing units

.. method:: getTrees()

   Returns the parsed trees (one per `<tree>` element in the file).

   **Signature:** ``getTrees() -> Collection``

   **Returns:** (``List[Any]``) collection of Tree objects; may be empty if no trees were found

.. method:: isNeurolucidaXML(is)

   Checks whether the given input stream starts with Neurolucida XML content. The stream must support `InputStream.mark(int)`.

   **Signature:** ``isNeurolucidaXML(InputStream) -> boolean``

   **Parameters:**

   * **is** (``Any``): - a mark-supported input stream positioned at the start of the file

   **Returns:** (``bool``) true if the content appears to be a Neurolucida XML file


NodeColorMapper
---------------

.. method:: getAvailableHeatmapLuts()

   **Signature:** ``getAvailableHeatmapLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvailableLuts()

   Gets the available LUTs.

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** (``Set[Any]``) the set of keys, corresponding to the set of LUTs available

.. method:: getColor(mappedValue)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(mappedValue)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable()

   Description copied from class: `ColorMapper`

   **Signature:** ``getColorTable() -> ColorTable``

   **Returns:** (``Any``) the current color table

.. method:: getMeasurement()

   Description copied from class: `ColorMapper`

   **Signature:** ``getMeasurement() -> String``

   **Returns:** (``str``) the unit, or an empty string if unknown/not applicable

.. method:: getMeasurementLabel()

   **Signature:** ``getMeasurementLabel() -> String``

   **Returns:** ``str``

.. method:: getMetrics()

   Gets the list of supported mapping metrics.

   **Signature:** ``getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of mapping metrics.

.. method:: getMinMax()

   Description copied from class: `ColorMapper`

   **Signature:** ``getMinMax() -> double[]``

   **Returns:** (``List[float]``) a two-element array with current {minimum, maximum} mapping bounds

.. method:: getNaNColor()

   **Signature:** ``getNaNColor() -> Color``

   **Returns:** ``Any``

.. method:: getNodes()

   Gets the collection of nodes being mapped.

   **Signature:** ``getNodes() -> Collection``

   **Returns:** (``List[Any]``) the collection of SNTPoint nodes

.. method:: getNodesByColor()

   **Signature:** ``getNodesByColor() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: isIntegerScale()

   **Signature:** ``isIntegerScale() -> boolean``

   **Returns:** ``bool``


NodeProfiler
------------

.. method:: cancel()

   **Signature:** ``cancel() -> void``

   **Returns:** ``None``

.. method:: getPlot(path)

   **Signature:** ``getPlot(Path) -> Plot``

   **Parameters:**

   * **path** (``Path``): - the path to be profiled

   **Returns:** (``Any``) The profile (Mean±SD of all the profiled data)

.. method:: getTable(path)

   **Signature:** ``getTable(Path) -> SNTTable``

   **Parameters:**

   * **path** (``Path``): - the path to be profiled, using its CT positions in the image

   **Returns:** (``SNTTable``) the profiled raw data in tabular form (1 column-per profiled node)

.. method:: getValues(p)

   Gets the profile for the specified path as a map of lists of pixel intensities (profile indices as keys)

   **Signature:** ``getValues(Path) -> SortedMap``

   **Parameters:**

   * **p** (``Path``): - the path to be profiled

   **Returns:** (``Any``) The profile

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``


NodeStatistics
--------------

.. method:: getAnnotatedFrequencies()

   Retrieves the count frequencies across brain compartment.

   **Signature:** ``getAnnotatedFrequencies() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedFrequenciesByHemisphere(level, tree)

   **Signature:** ``getAnnotatedFrequenciesByHemisphere(int, Tree) -> Map``

   **Parameters:**

   * **level** (``int``)
   * **tree** (``Tree``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedFrequencyHistogram(depth, hemisphere, tree)

   Retrieves the histogram of count frequencies across brain areas of the specified ontology level across the specified hemisphere.

   **Signature:** ``getAnnotatedFrequencyHistogram(int, String, Tree) -> SNTChart``

   **Parameters:**

   * **depth** (``int``): - the ontological depth of the compartments to be considered
   * **hemisphere** (``str``)
   * **tree** (``Tree``)

   **Returns:** (``SNTChart``) the annotated frequencies histogram

.. method:: getAnnotatedHistogram()

   Retrieves the histogram of count frequencies across brain areas of the specified ontology level.

   **Signature:** ``getAnnotatedHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedNodes()

   Splits the nodes being analyzed into groups sharing the same brain annotation.

   **Signature:** ``getAnnotatedNodes() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getDescriptiveStatistics(metric)

   Computes the `DescriptiveStatistics` for the specified measurement.

   **Signature:** ``getDescriptiveStatistics(String) -> DescriptiveStatistics``

   **Parameters:**

   * **metric** (``str``): - the measurement (X_COORDINATES, Y_COORDINATES, etc.)

   **Returns:** (``Any``) the DescriptiveStatistics object.

.. method:: getHistogram(metric)

   Gets the relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``): - the measurement (X_COORDINATES, RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram

.. method:: getMetrics()

   Gets the list of supported metrics.

   **Signature:** ``getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metrics


NormalizedProfileStats
----------------------

.. method:: getDeterminationRatio()

   **Signature:** ``getDeterminationRatio() -> double``

   **Returns:** ``float``

.. method:: getFitYValues()

   **Signature:** ``getFitYValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getIntercept()

   **Signature:** ``getIntercept() -> double``

   **Returns:** ``float``

.. method:: getMethod()

   **Signature:** ``getMethod() -> int``

   **Returns:** ``int``

.. method:: getMethodDescription()

   **Signature:** ``getMethodDescription() -> String``

   **Returns:** ``str``

.. method:: getMethodFlag(string)

   **Signature:** ``getMethodFlag(String) -> int``

   **Parameters:**

   * **string** (``str``)

   **Returns:** ``int``

.. method:: getNormalizer()

   **Signature:** ``getNormalizer() -> int``

   **Returns:** ``int``

.. method:: getNormalizerDescription()

   **Signature:** ``getNormalizerDescription() -> String``

   **Returns:** ``str``

.. method:: getNormalizerFlag(string)

   **Signature:** ``getNormalizerFlag(String) -> int``

   **Parameters:**

   * **string** (``str``)

   **Returns:** ``int``

.. method:: getR()

   **Signature:** ``getR() -> double``

   **Returns:** ``float``

.. method:: getRSquaredOfFit()

   **Signature:** ``getRSquaredOfFit() -> double``

   **Returns:** ``float``

.. method:: getRegression()

   **Signature:** ``getRegression() -> SimpleRegression``

   **Returns:** ``Any``

.. method:: getShollDecay()

   **Signature:** ``getShollDecay() -> double``

   **Returns:** ``float``

.. method:: getSlope()

   **Signature:** ``getSlope() -> double``

   **Returns:** ``float``

.. method:: getXValues()

   **Signature:** ``getXValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getYValues()

   **Signature:** ``getYValues() -> double[]``

   **Returns:** ``List[float]``


OBJMesh
-------

.. method:: getAngleWithLocalDirection(point, direction, hemiHalf, neighborCount)

   Computes the angle between a direction vector and the local mesh direction at a point. This is useful for e.g., analyzing how neuronal processes align with the local curvature of surfaces (neuropil meshes).

   **Signature:** ``getAngleWithLocalDirection(SNTPoint, double[], String, int) -> double``

   **Parameters:**

   * **point** (``SNTPoint``): - the point at which to compute the local mesh direction
   * **direction** (``List[float]``)
   * **hemiHalf** (``str``)
   * **neighborCount** (``int``)

   **Returns:** (``float``) the acute angle in degrees (0-90°) between the direction vector and local mesh direction, or NaN if computation fails

.. method:: getBoundingBox(hemiHalf)

   Gets the minimum bounding box of this mesh.

   **Signature:** ``getBoundingBox(String) -> BoundingBox``

   **Parameters:**

   * **hemiHalf** (``str``): - either "left", "l", "right", "r" otherwise bounding box is retrieved for both hemi-halves, i.e., the full mesh. It is ignored if a hemisphere was already specified in the constructor.

   **Returns:** (``BoundingBox``) the minimum bounding box

.. method:: getCentroid(hemihalf)

   Returns the spatial centroid of the specified (hemi)mesh.

   **Signature:** ``getCentroid(String) -> SNTPoint``

   **Parameters:**

   * **hemihalf** (``str``): - either "left", "l", "right", "r", otherwise centroid is retrieved for both hemi-halves, i.e., the full mesh

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of the (hemi)mesh.

.. method:: getDisplayedHemisphere()

   Returns the currently displayed hemisphere: "left", "right", or "both".

   **Signature:** ``getDisplayedHemisphere() -> String``

   **Returns:** (``str``) the displayed hemisphere

.. method:: getDrawable()

   Returns the `DrawableVBO` associated with this mesh

   **Signature:** ``getDrawable() -> DrawableVBO``

   **Returns:** (``Any``) the DrawableVBO

.. method:: getLocalDirection(point, hemiHalf, neighborCount)

   Computes the local direction of the mesh at a specific point using nearest neighbor analysis. This method finds the dominant direction of mesh curvature in the local neighborhood of the specified point, which is useful for analyzing how structures align with curved anatomical surfaces.

   **Signature:** ``getLocalDirection(SNTPoint, String, int) -> double[]``

   **Parameters:**

   * **point** (``SNTPoint``): - the point at which to compute the local mesh direction
   * **hemiHalf** (``str``)
   * **neighborCount** (``int``)

   **Returns:** (``List[float]``) the local mesh direction as a normalized vector, or null if computation fails

.. method:: getObj()

   Returns the `OBJFile` associated with this mesh

   **Signature:** ``getObj() -> OBJFile``

   **Returns:** (``Any``) the OBJFile

.. method:: getPrincipalAxes(hemiHalf)

   Computes the principal axes of the mesh using Principal Component Analysis (PCA). The principal axes represent the directions of maximum, medium, and minimum variance in the mesh geometry, providing insight into the overall shape orientation of this mesh.

   **Signature:** ``getPrincipalAxes(String) -> PrincipalAxis[]``

   **Parameters:**

   * **hemiHalf** (``str``): - either "left", "l", "right", "r", otherwise principal axes are computed for both hemi-halves, i.e., the full mesh

   **Returns:** (``List[Any]``) array of three PrincipalAxis objects ordered by decreasing variance (primary, secondary, tertiary), or null if computation fails

.. method:: getSourceAnnotation()

   Returns the `BrainAnnotation` (atlas compartment) from which this mesh was retrieved, or null if this mesh was loaded from a standalone file.

   **Signature:** ``getSourceAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the source annotation, or null

.. method:: getSymmetryAxis()

   **Signature:** ``getSymmetryAxis() -> int``

   **Returns:** ``int``

.. method:: getVertices()

   Returns the mesh vertices.

   **Signature:** ``getVertices() -> Collection``

   **Returns:** ``List[Any]``

.. method:: getVolume()

   Gets the volume of this mesh.

   **Signature:** ``getVolume() -> double``

   **Returns:** (``float``) the mesh volume

.. method:: hasFileColor()

   Returns whether the color of this mesh was defined in the material (.mtl) file associated with the imported .obj file.

   **Signature:** ``hasFileColor() -> boolean``

   **Returns:** (``bool``) true, if the mesh color was read from the file


OneMinusErf
-----------

.. method:: getZFudge()

   **Signature:** ``getZFudge() -> double``

   **Returns:** ``float``


PCAnalyzer
----------

.. method:: getPrincipalAxes(points)

   Computes the principal axes for a collection of SNTPoints.

   **Signature:** ``getPrincipalAxes(Collection) -> PrincipalAxis[]``

   **Parameters:**

   * **points** (``List[Any]``): - the collection of points to analyze

   **Returns:** (``List[Any]``) array of three PrincipalAxis objects ordered by decreasing variance (primary, secondary, tertiary), or null if computation fails

.. method:: getVariancePercentages(axes)

   Computes the variance percentages for an array of principal axes. This is a convenience method that returns the percentage of total variance explained by each principal axis.

   **Signature:** ``getVariancePercentages(PrincipalAxis[]) -> double[]``

   **Parameters:**

   * **axes** (``List[Any]``): - the array of three PrincipalAxis objects (primary, secondary, tertiary)

   **Returns:** (``List[float]``) array of three percentages (primary, secondary, tertiary) that sum to 100%, or null if axes is null


Path
----

.. method:: getAngle(nodeIndex)

   Computes the angle between the specified node and its two flanking neighbors.

With B being the specified node, A its previous neighbor, and C is next neighbor, computes the angle between the vectors AB, and BC.

   **Signature:** ``getAngle(int) -> double``

   **Parameters:**

   * **nodeIndex** (``int``)

   **Returns:** (``float``) the angle in degrees (0-360 range) or Double.NaN if specified node does not have sufficient neighbors

.. method:: getApproximatedSurface()

   Returns an estimated surface area of this path, treating each inter-node segment as a frustum.

   **Signature:** ``getApproximatedSurface() -> double``

   **Returns:** (``float``) the approximate surface area (in physical units), or 0 if this Path has no radii

.. method:: getApproximatedVolume()

   Returns an estimated volume of this path.

The most accurate volume of each path segment would be the volume of a convex hull of two arbitrarily oriented and sized circles in space. This is tough to work out analytically, and this precision isn't really warranted given the errors introduced in the fitting process, the tracing in the first place, etc. So, this method produces an approximate volume assuming that the volume of each of these parts is that of a truncated cone (Frustum) , with circles of the same size (i.e., as if the circles had simply been reoriented to be parallel and have a common normal vector)

For more accurate measurements of the volumes of a neuron, you should use the filling interface.

   **Signature:** ``getApproximatedVolume() -> double``

   **Returns:** (``float``) the approximate fitted volume (in physical units), or NaN if this Path has no radii

.. method:: getBranchPoint()

   Gets the branch point (junction) where this path starts, i.e., connects to its parent path.

   **Signature:** ``getBranchPoint() -> PointInImage``

   **Returns:** (``PointInImage``) the start junction point, or null if this is a primary path

.. method:: getBranchPointIndex()

   Gets the index of the branch point in the parent path.

   **Signature:** ``getBranchPointIndex() -> int``

   **Returns:** (``int``) the branch point index, or -1 if this is a primary path

.. method:: getBranchPoints()

   This is a version of `findJunctions()` ensuring that a junction node is only retrieved once even if multiple child paths are associated with it.

   **Signature:** ``getBranchPoints() -> Set``

   **Returns:** (``Set[Any]``) the junction nodes

.. method:: getCalibration()

   Gets the spatial calibration of this Path.

   **Signature:** ``getCalibration() -> Calibration``

   **Returns:** (``Any``) the calibration details associated with this Path

.. method:: getCanvasOffset()

   Returns the translation offset used to render this Path in a `TracerCanvas`.

   **Signature:** ``getCanvasOffset() -> PointInCanvas``

   **Returns:** (``Any``) the rendering offset (in pixel coordinates)

.. method:: getChannel()

   Gets the hyperstack channel associated with this Path.

   **Signature:** ``getChannel() -> int``

   **Returns:** (``int``) the channel position of this path (1-based index). Note that if the channel associated with a path is not known, it is assumed to be 1;

.. method:: getChildren()

   Gets the list of child paths that branch from this path.

Returns the collection of paths that have this path as their parent. The returned list is the actual internal list, so modifications to it will affect the path's structure.

   **Signature:** ``getChildren() -> List``

   **Returns:** (``List[Any]``) the List of child paths. May be empty if this path has no children, but never null.

.. method:: getColor()

   Gets the color of this Path

   **Signature:** ``getColor() -> Color``

   **Returns:** (``Any``) the color, or null if no color has been assigned to this Path

.. method:: getColorRGB()

   Gets the color of this Path

   **Signature:** ``getColorRGB() -> ColorRGB``

   **Returns:** (``Any``) the color, or null if no color has been assigned to this Path

.. method:: getContraction()

   Returns the ratio between the "Euclidean distance" of this path and its length. The Euclidean distance of this path is defined as the distance between this Path's start and end point.

   **Signature:** ``getContraction() -> double``

   **Returns:** (``float``) the Contraction of this Path, or `NaN` if this Path has no length

.. method:: getEditableNodeIndex()

   Gets the position of the node tagged as 'editable', if any.

   **Signature:** ``getEditableNodeIndex() -> int``

   **Returns:** (``int``) the index of the point currently tagged as editable, or -1 if no such point exists

.. method:: getExtensionAngle3D(referenceVector)

   Returns a single angle representing the 3D extension direction. This is the angle between the path's direction vector and a reference vector.

   **Signature:** ``getExtensionAngle3D(Vector3d) -> double``

   **Parameters:**

   * **referenceVector** (``Any``): - the reference vector to measure angle from (e.g., new Vector3d(0, 0, 1) for vertical reference, or new Vector3d(1, 0, 0) for horizontal)

   **Returns:** (``float``) the acute angle in degrees (0-180°), or Double.NaN if path has only one point

.. method:: getExtensionAngleFromHorizontal()

   Returns the angle between the path's 3D direction and the horizontal axis.

   **Signature:** ``getExtensionAngleFromHorizontal() -> double``

   **Returns:** (``float``) angle from horizontal in degrees (09° = vertical, 0° = horizontal), or Double.NaN if path has only one point.

.. method:: getExtensionAngleFromVertical()

   Returns the angle between the path's 3D direction and the vertical axis.

   **Signature:** ``getExtensionAngleFromVertical() -> double``

   **Returns:** (``float``) angle from vertical in degrees (0° = vertical, 90° = horizontal), or Double.NaN if path has only one point, or 90° if path is 2D

.. method:: getExtensionAngleXY()

   Returns the overall extension angle of this path in the XY plane. The angle is obtained from the slope of a linear regression across all the path nodes.

   **Signature:** ``getExtensionAngleXY() -> double``

   **Returns:** (``float``) the overall 'extension' angle in degrees [0-360[ of this path in the XY plane.

.. method:: getExtensionAngleXZ()

   Returns the overall extension angle of this path in the XZ plane. The angle is obtained from the slope of a linear regression across all the path nodes.

   **Signature:** ``getExtensionAngleXZ() -> double``

   **Returns:** (``float``) the overall 'extension' angle in degrees [0-360[ in the XZ plane or NaN if path is 2D.

.. method:: getExtensionAngleZY()

   Returns the overall extension angle of this path in the ZY plane. The angle is obtained from the slope of a linear regression across all the path nodes.

   **Signature:** ``getExtensionAngleZY() -> double``

   **Returns:** (``float``) the overall 'extension' angle in degrees [0-360[ in the ZY plane or NaN if path is 2D.

.. method:: getExtensionAngles3D()

   Returns the complete 3D orientation of this path's extension direction as spherical coordinates using navigation/compass convention.

This method provides both horizontal direction (azimuth) and vertical inclination (elevation) of the path's overall extension direction.

   **Signature:** ``getExtensionAngles3D() -> double[]``

   **Returns:** (``List[float]``) double array containing [azimuth, elevation] in degrees, where:

**azimuth** (index 0): Compass bearing in XY plane (0-360°) following navigation convention:

- 0° = North (negative Y direction in image coordinates)

- 90° = East (positive X direction)

- 180° = South (positive Y direction in image coordinates)

- 270° = West (negative X direction)

**elevation** (index 1): Vertical angle from XY plane (-90° to +90°):

- 0° = horizontal (parallel to XY plane)

- +90° = pointing straight up (positive Z direction)

- -90° = pointing straight down (negative Z direction)

Returns null if path has only one point or extension direction cannot be determined

.. method:: getExtensionDirection3D()

   Returns the 3D extension direction vector of this path using linear regression. The vector represents the overall direction from start to end of the path, fitted through all its nodes.

   **Signature:** ``getExtensionDirection3D() -> Vector3d``

   **Returns:** (``Any``) the normalized Vector3d (length of 1) representing the extension direction, or null if path has only one point

.. method:: getFitted()

   Gets the fitted version ('flavor') of this Path.

   **Signature:** ``getFitted() -> Path``

   **Returns:** (``Path``) the fitted version, or null if this Path has not been fitted

.. method:: getFractalDimension()

   Gets the fractal dimension of this path.

   **Signature:** ``getFractalDimension() -> double``

   **Returns:** (``float``) the fractal dimension of this path or Double.NaN if this path has less than 5 nodes

.. method:: getFrame()

   Gets the hyperstack frame position associated with this Path.

   **Signature:** ``getFrame() -> int``

   **Returns:** (``int``) the frame position of this path (1-based index). Note that if the frame associated with a path is not known, it is assumed to be 1;

.. method:: getID()

   Gets the identifier of this Path

   **Signature:** ``getID() -> int``

   **Returns:** (``int``) the identifier

.. method:: getInitialDirection(maxNodes)

   Returns a (non-normalized) direction vector from the first node to the node at index `min(maxNodes, size()-1)`. This is useful for measuring the initial heading of a child path near a fork point.

   **Signature:** ``getInitialDirection(int) -> double[]``

   **Parameters:**

   * **maxNodes** (``int``): - the maximum node index to use as the end point

   **Returns:** (``List[float]``) a 3-element array `[dx, dy, dz]`, or `null` if the path has fewer than 2 nodes or the resulting vector is zero-length

.. method:: getInterpolatedPath(maxDistance)

   Returns a new Path in which nodes have been interpolated to ensure that the distance between consecutive nodes does not exceed the specified threshold.

   **Signature:** ``getInterpolatedPath(double) -> Path``

   **Parameters:**

   * **maxDistance** (``float``): - the maximum distance allowed between consecutive nodes

   **Returns:** (``Path``) the interpolated path

.. method:: getLength()

   Gets the length of this Path

   **Signature:** ``getLength() -> double``

   **Returns:** (``float``) the length of this Path

.. method:: getMeanRadius()

   Gets the path mean radius.

   **Signature:** ``getMeanRadius() -> double``

   **Returns:** (``float``) the average radius of the path, or zero if path has no defined thickness

.. method:: getMinimumSeparation()

   **Signature:** ``getMinimumSeparation() -> double``

   **Returns:** ``float``

.. method:: getName()

   Gets this Path's name.

   **Signature:** ``getName() -> String``

   **Returns:** (``str``) the name. If no name as been set, the default name is returned.

.. method:: getNode(pos)

   **Signature:** ``getNode(int) -> PathNode``

   **Parameters:**

   * **pos** (``int``)

   **Returns:** ``Any``

.. method:: getNodeAnnotation(pos)

   Returns the neuropil annotation associated with this node.

   **Signature:** ``getNodeAnnotation(int) -> BrainAnnotation``

   **Parameters:**

   * **pos** (``int``): - the node position

   **Returns:** (``Any``) the annotation of this node,

.. method:: getNodeColor(pos)

   Gets the node color.

   **Signature:** ``getNodeColor(int) -> Color``

   **Parameters:**

   * **pos** (``int``): - the node position

   **Returns:** (``Any``) the node color, or null if no color nodes have been assigned to this path

.. method:: getNodeColors()

   Gets the node colors.

   **Signature:** ``getNodeColors() -> Color[]``

   **Returns:** (``List[Any]``) the colors used to render the nodes of this path, or null if nodes are rendered using the Path color

.. method:: getNodeHemisphereFlag(pos)

   Returns the hemisphere flag associated with this node.

   **Signature:** ``getNodeHemisphereFlag(int) -> char``

   **Parameters:**

   * **pos** (``int``): - the node position

   **Returns:** (``str``) the flag associated with this node, either `BrainAnnotation.LEFT_HEMISPHERE`, `BrainAnnotation.RIGHT_HEMISPHERE`, or `BrainAnnotation.ANY_HEMISPHERE`

.. method:: getNodeIndex(pim)

   Gets the first node index associated with the specified image coordinates. Returns -1 if no such node was found.

   **Signature:** ``getNodeIndex(PointInImage) -> int``

   **Parameters:**

   * **pim** (``PointInImage``): - the image position (calibrated coordinates)

   **Returns:** (``int``) the index of the first node occurrence or -1 if there is no such occurrence

.. method:: getNodeRadius(pos)

   Gets the radius of the specified node.

   **Signature:** ``getNodeRadius(int) -> double``

   **Parameters:**

   * **pos** (``int``): - the node position

   **Returns:** (``float``) the radius at the specified position, or zero if path has no defined thickness

.. method:: getNodeTangent(pos)

   Gets the tangent vector of a specific node.

   **Signature:** ``getNodeTangent(int) -> double[]``

   **Parameters:**

   * **pos** (``int``): - the node position

   **Returns:** (``List[float]``) the tangent vector [x, y, z] or null if not defined

.. method:: getNodeValue(pos)

   Returns the "value" property of this node.

   **Signature:** ``getNodeValue(int) -> double``

   **Parameters:**

   * **pos** (``int``): - the node position

   **Returns:** (``float``) the value property of this node

.. method:: getNodes()

   Gets all nodes as a list.

   **Signature:** ``getNodes() -> List``

   **Returns:** (``List[Any]``) a new list containing all nodes

.. method:: getOrder()

   Gets the "bifurcation" (branching) order of this Path. If registered in the GUI, this would correspond to the level of this Path in `PathManagerUI`'s JTree: E.g., a Path connected to a primary Path (order 1) will be assigned order 2, etc. N.B.: Albeit related to reverse Horton-Strahler classification, Path ordering is formally distinct, as it classifies *Paths* instead of *branches*.

   **Signature:** ``getOrder() -> int``

   **Returns:** (``int``) the order of this path. A primary path is always of order 1.

.. method:: getParentPath()

   Gets the parent path that this path branches from.

Returns the path from which this path originates as a branch. For primary (root) paths, this method returns null since they don't branch from any other path. The parent-child relationship is established when a path is created as a branch using `setBranchFrom(Path, PointInImage)`.

   **Signature:** ``getParentPath() -> Path``

   **Returns:** (``Path``) the parent path, or null if this is a primary (root) path

.. method:: getPointInCanvas(node)

   **Signature:** ``getPointInCanvas(int) -> PointInCanvas``

   **Parameters:**

   * **node** (``int``)

   **Returns:** ``Any``

.. method:: getResampledPath(targetSpacing)

   Returns a new Path in which nodes have been resampled to ensure uniform spacing along the path.

   **Signature:** ``getResampledPath(double) -> Path``

   **Parameters:**

   * **targetSpacing** (``float``): - the desired spacing between consecutive nodes

   **Returns:** (``Path``) the resampled path

.. method:: getSWCType()

   Gets the SWC type.

   **Signature:** ``getSWCType() -> int``

   **Returns:** (``int``) the SWC type

.. method:: getSWCcolor(swcType)

   Gets the default SWC colors used by SNT.

   **Signature:** ``getSWCcolor(int) -> Color``

   **Parameters:**

   * **swcType** (``int``): - the SEC type (e.g., SWC_AXON, SWC_DENDRITE, etc.)

   **Returns:** (``Any``) the SWC color

.. method:: getSWCtypeName(type, capitalized)

   Gets the SWC type label associated with the specified type flag. SNT follows the specification detailed at swc-specification.readthedocs.io

   **Signature:** ``getSWCtypeName(int, boolean) -> String``

   **Parameters:**

   * **type** (``int``): - the SWC type flag
   * **capitalized** (``bool``)

   **Returns:** (``str``) the respective label, or `SWC_UNDEFINED_LABEL` if flag was not recognized

.. method:: getSWCtypeNames()

   Gets the list of string representations of SWC types

   **Signature:** ``getSWCtypeNames() -> List``

   **Returns:** (``List[Any]``) the list of SWC type names

.. method:: getSWCtypes()

   Gets the list of SWC types.

   **Signature:** ``getSWCtypes() -> List``

   **Returns:** (``List[Any]``) the list of SWC type flags

.. method:: getSection(startIndex, endIndex)

   Gets a section between two nodes of this Path.

   **Signature:** ``getSection(int, int) -> Path``

   **Parameters:**

   * **startIndex** (``int``): - the node index defining the first node of the section
   * **endIndex** (``int``)

   **Returns:** (``Path``) the section. Note that the sectioned Path will share of all of this Path's properties but will not contain any information on junction points or connectivity to other Paths.

.. method:: getSmoothedPath(windowSize)

   Returns a smoothed version of this path using a simple moving average filter.

   **Signature:** ``getSmoothedPath(int) -> Path``

   **Parameters:**

   * **windowSize** (``int``): - the size of the smoothing window (must be odd and >= 3)

   **Returns:** (``Path``) the smoothed path

.. method:: getSpineOrVaricosityCount()

   Gets the number of spines or varicosities associated with this path.

   **Signature:** ``getSpineOrVaricosityCount() -> int``

   **Returns:** (``int``) the number of spines or varicosities. Returns 0 if no features have been annotated.

.. method:: getTangent(i, pointsEitherSide, result)

   **Signature:** ``getTangent(int, int, double[]) -> void``

   **Parameters:**

   * **i** (``int``)
   * **pointsEitherSide** (``int``)
   * **result** (``List[float]``)

   **Returns:** ``None``

.. method:: getTreeID()

   Gets the identifier of the `Tree` associated to this Path (if any).

   **Signature:** ``getTreeID() -> int``

   **Returns:** (``int``) the Tree identifier

.. method:: getTreeLabel()

   **Signature:** ``getTreeLabel() -> String``

   **Returns:** ``str``

.. method:: getUnfitted()

   Gets the original (unfitted) path that this path is a fitted version of.

   **Signature:** ``getUnfitted() -> Path``

   **Returns:** (``Path``) the unfitted original, or `null` if this is not a fitted path

.. method:: getUnscaledNodes()

   **Signature:** ``getUnscaledNodes() -> List``

   **Returns:** (``List[Any]``) the list of nodes in image space (pixel coordinates). This takes already takes into account `getCanvasOffset()`.

.. method:: getUseFitted()

   Gets whether the fitted 'flavor' of this Path is in use.

   **Signature:** ``getUseFitted() -> boolean``

   **Returns:** (``bool``) true, if the fitted version of this Path is in use, otherwise false

.. method:: getVersionInUse()

   Returns the version of this path that is in use, i.e., the one that is displayed and analyzed: its fitted flavor if `getUseFitted()`, otherwise this path. This is the registry-free rule: for the registry-aware one see `PathAndFillManager.getVersionInUse(Path)`

   **Signature:** ``getVersionInUse() -> Path``

   **Returns:** (``Path``) the version in use. Never null

.. method:: getXUnscaled(i)

   Returns the unscaled X position of a node.

   **Signature:** ``getXUnscaled(int) -> int``

   **Parameters:**

   * **i** (``int``): - the index of the path node

   **Returns:** (``int``) the 0-based index of the X-position of the node.

.. method:: getXUnscaledDouble(i)

   **Signature:** ``getXUnscaledDouble(int) -> double``

   **Parameters:**

   * **i** (``int``)

   **Returns:** ``float``

.. method:: getYUnscaled(i)

   Returns the unscaled Y position of a node.

   **Signature:** ``getYUnscaled(int) -> int``

   **Parameters:**

   * **i** (``int``): - the index of the path node

   **Returns:** (``int``) the 0-based index of the Y-position of the node.

.. method:: getYUnscaledDouble(i)

   **Signature:** ``getYUnscaledDouble(int) -> double``

   **Parameters:**

   * **i** (``int``)

   **Returns:** ``float``

.. method:: getZUnscaled(i)

   Returns the unscaled Z position of a node.

   **Signature:** ``getZUnscaled(int) -> int``

   **Parameters:**

   * **i** (``int``): - the index of the path node

   **Returns:** (``int``) the 0-based index of the Z-position of the node. Note that Z-indices in ImagePlus are 1-based, i.e., outside SNT the proper Z-slice for this position in an ImagePlus is `getZUnscaled(i) + 1`

.. method:: getZUnscaledDouble(i)

   **Signature:** ``getZUnscaledDouble(int) -> double``

   **Parameters:**

   * **i** (``int``)

   **Returns:** ``float``

.. method:: hasCustomColor()

   Assesses whether a custom color has been assigned to this Path.

   **Signature:** ``hasCustomColor() -> boolean``

   **Returns:** (``bool``) true, if successful

.. method:: hasNodeAnnotations()

   Assesses whether the nodes of this path have been assigned `BrainAnnotation`s.

   **Signature:** ``hasNodeAnnotations() -> boolean``

   **Returns:** (``bool``) true, if successful

.. method:: hasNodeColors()

   Checks whether any nodes have custom colors assigned.

   **Signature:** ``hasNodeColors() -> boolean``

   **Returns:** (``bool``) true if any nodes have custom colors

.. method:: hasNodeHemisphereFlags()

   Assesses whether the nodes of this path have been assigned hemisphere flags.

   **Signature:** ``hasNodeHemisphereFlags() -> boolean``

   **Returns:** (``bool``) true, if successful

.. method:: hasNodeValues()

   Assesses whether the nodes of this path have been assigned an array of values

   **Signature:** ``hasNodeValues() -> boolean``

   **Returns:** (``bool``) true, if successful

.. method:: hasRadii()

   Checks whether the nodes of this path have been assigned defined thickness.

   **Signature:** ``hasRadii() -> boolean``

   **Returns:** (``bool``) true, if the points defining with this path are associated with a list of radii

.. method:: hasTangents()

   Checks whether any nodes have tangent vectors defined.

   **Signature:** ``hasTangents() -> boolean``

   **Returns:** (``bool``) true if any nodes have tangents

.. method:: isActiveVersion()

   Checks if this version of the path is currently being used for display/analysis.

   **Signature:** ``isActiveVersion() -> boolean``

   **Returns:** (``bool``) true if this version is active, false otherwise

.. method:: isConnectedTo(other)

   **Signature:** ``isConnectedTo(Path) -> boolean``

   **Parameters:**

   * **other** (``Path``)

   **Returns:** ``bool``

.. method:: isDeFactoPath(paths)

   Single source of truth for the "should this fitted-version path be treated as redundant/standalone" decision used throughout listings, filters, and measurements.

A fitted-version path (`isFittedVersionOfAnotherPath()`) is normally considered redundant -- it is expected to be represented instead by its un-fitted counterpart (`getUnfitted()`), which is typically registered alongside it. But that assumption can be violated: `Tree(java.util.Collection)` (used e.g. by `Tree.listFromFile(String)`) substitutes a path's fitted flavor in place of the original whenever `getUseFitted()` is true, so if the source file also flagged that original path as primary/root, only the fitted substitute ever ends up in `paths`, and its un-fitted twin never arrives. In that case this path is the only remaining representative and must NOT be treated as redundant, or it silently vanishes from whatever is being listed/measured.

   **Signature:** ``isDeFactoPath(Collection) -> boolean``

   **Parameters:**

   * **paths** (``List[Any]``): - the collection this path is being considered against (e.g., an entire PathAndFillManager's paths, or a Tree's own path list). For large collections, prefer passing a Set -- membership is tested with Collection.contains(Object)

   **Returns:** (``bool``) true if this path should be treated as a normal, standalone/"de facto" path (either it is not a fitted version, or its un-fitted counterpart is missing from `paths`); false if it is redundant and should be skipped in favor of that counterpart

.. method:: isFittedVersionOfAnotherPath()

   Checks if this Path is a fitted version of another path.

   **Signature:** ``isFittedVersionOfAnotherPath() -> boolean``

   **Returns:** (``bool``) true, if it is a fitted version of another path

.. method:: isPrimary()

   Checks if this Path is root.

   **Signature:** ``isPrimary() -> boolean``

   **Returns:** (``bool``) true, if is primary (root)

.. method:: isSelected()

   **Signature:** ``isSelected() -> boolean``

   **Returns:** ``bool``

.. method:: setSpineOrVaricosityCount(newCount)

   Sets the number of spines or varicosities associated with this path.

   **Signature:** ``setSpineOrVaricosityCount(int) -> void``

   **Parameters:**

   * **newCount** (``int``): - the new count of spines or varicosities. Should be non-negative.

   **Returns:** ``None``

.. method:: size()

   Returns the number of nodes of this path

   **Signature:** ``size() -> int``

   **Returns:** (``int``) the size, i.e., number of nodes


PathAndFillManager
------------------

.. method:: getBoundingBox(compute)

   Returns the BoundingBox enclosing all nodes of all existing Paths.

   **Signature:** ``getBoundingBox(boolean) -> BoundingBox``

   **Parameters:**

   * **compute** (``bool``): - If true, BoundingBox dimensions will be computed for all the existing Paths. If false, the last computed BoundingBox will be returned. Also, if BoundingBox is not scaled, its spacing will be computed from the smallest inter-node distance of an arbitrary ' large' Path. Computations of Path boundaries typically occur during import operations.

   **Returns:** (``BoundingBox``) the BoundingBox enclosing existing nodes, or an 'empty' BoundingBox if no computation of boundaries has not yet occurred. Output is never null.

.. method:: getCorrespondences(other, maxDistance)

   For each point in this PathAndFillManager, find the corresponding point on the other one. If there's no corresponding one, include a null instead. *

   **Signature:** ``getCorrespondences(PathAndFillManager, double) -> List``

   **Parameters:**

   * **other** (``PathAndFillManager``): - the other PathAndFillManager holding the corresponding Paths
   * **maxDistance** (``float``)

   **Returns:** (``List[Any]``) the cloud of `NearPoint` correspondences

.. method:: getLoadedFills()

   **Signature:** ``getLoadedFills() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getOrphanedFittedPaths()

   Returns the "orphaned" fitted paths currently registered with this manager: fitted-version paths (`Path.isFittedVersionOfAnotherPath()`) whose un-fitted original was never registered here (see `isDeFactoPath(Path)`). Their pre-fit geometry no longer exists in this session, and saving them (see `writeXML(java.lang.String, boolean)`) writes a `fittedversionof` reference to a path ID that is not present in the saved file.

   **Signature:** ``getOrphanedFittedPaths() -> List``

   **Returns:** (``List[Any]``) the orphaned fitted paths, or an empty list if none

.. method:: getPath(i)

   Returns the Path at the specified position in the PathAndFillManager list.

   **Signature:** ``getPath(int) -> Path``

   **Parameters:**

   * **i** (``int``): - the index of the Path

   **Returns:** (``Path``) the Path at the specified index

.. method:: getPathFromID(id)

   Returns the Path with the specified id.

   **Signature:** ``getPathFromID(int) -> Path``

   **Parameters:**

   * **id** (``int``): - the id of the Path to be retrieved

   **Returns:** (``Path``) the Path with the specified id, or null if id was not found.

.. method:: getPathFromName(name, caseSensitive)

   Returns the Path with the specified name.

   **Signature:** ``getPathFromName(String, boolean) -> Path``

   **Parameters:**

   * **name** (``str``): - the name of the Path to be retrieved
   * **caseSensitive** (``bool``)

   **Returns:** (``Path``) the Path with the specified name, or null if name was not found.

.. method:: getPaths()

   Returns the "main" paths managed by this PathAndFillManager. This is a convenience method that excludes:

- Null entries (defensive filtering)

- Fitted paths (i.e., paths that are refined versions of other paths, created by path-fitting algorithms). These are typically displayed alongside their parent path rather than as standalone entries.

The returned list is a snapshot safe for iteration even if paths are concurrently added or removed.

   **Signature:** ``getPaths() -> List``

   **Returns:** (``List[Any]``) a filtered list of paths, excluding nulls and fitted versions

.. method:: getPathsFiltered()

   Returns the 'de facto' Paths (excluding null or fitted versions). he returned list is a snapshot safe for iteration even if paths are concurrently added or removed.

A fitted-version path is only excluded when its un-fitted counterpart is also registered with this manager, i.e., when that counterpart is available to represent it instead. See `isDeFactoPath(Path)` for why that check -- rather than an unconditional exclusion -- is necessary.

   **Signature:** ``getPathsFiltered() -> List``

   **Returns:** (``List[Any]``) a filtered list of paths, excluding nulls and redundant fitted versions

.. method:: getPathsInROI(roi)

   **Signature:** ``getPathsInROI(Roi) -> Collection``

   **Parameters:**

   * **roi** (``Any``)

   **Returns:** ``List[Any]``

.. method:: getPathsStructured()

   **Signature:** ``getPathsStructured() -> Path[]``

   **Returns:** ``List[Path]``

.. method:: getPhantomFittedPaths()

   Returns "phantom" fitted paths: registered paths that look like ordinary, standalone paths but are actually the fitted flavor of an original that no longer exists in any form -- neither registered here nor resolvable from a `fittedversionof` reference. This happens when a traces file is loaded whose `fittedversionof` attribute points to a path ID absent from the file itself (e.g. the raw/unfitted original was deleted before saving), which leaves `Path.fittedVersionOf` `null` rather than merely unregistered. Such paths pass loading validation silently and are indistinguishable from a normal path except for their negative ID (see `Path.setFitted(Path)`).

   **Signature:** ``getPhantomFittedPaths() -> List``

   **Returns:** (``List[Any]``) the phantom fitted paths, or an empty list if none

.. method:: getPlugin()

   Gets the SNT instance.

   **Signature:** ``getPlugin() -> SNT``

   **Returns:** (``SNT``) the `SNT` instance associated with this PathManager (if any)

.. method:: getSWCFor(paths)

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

   **Signature:** ``getSWCFor(Collection) -> List``

   **Parameters:**

   * **paths** (``List[Any]``): - the collection of Path objects to convert. Must contain exactly one primary path and form a connected tree structure. Empty paths are automatically skipped. Cannot be null or empty.

   **Returns:** (``List[Any]``) a list of SWCPoint objects representing the neuronal structure in SWC format. Points are ordered by their sequential SWC IDs, with proper parent-child relationships established. The list is never null but may be empty if all input paths are empty.

.. method:: getSelectedPaths()

   Gets all paths selected in the GUI

   **Signature:** ``getSelectedPaths() -> Set``

   **Returns:** (``Set[Any]``) the collection of selected paths

.. method:: getTree(treeLabel)

   Returns the specified Tree.

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **treeLabel** (``str``): - the Tree's id

   **Returns:** (``Tree``) the tree or null if this PathAndFillManager instance holds no such treeId

.. method:: getTrees()

   Returns all the paths associated with this PathAndFillManager instance, grouped by Tree.

   **Signature:** ``getTrees() -> Collection``

   **Returns:** (``List[Any]``) the Trees associated with this PathAndFillManager instance

.. method:: getVersionInUse(p)

   Returns the version of a path that is in use, i.e., the one that is displayed and analyzed: its fitted flavor if `Path.getUseFitted()`, otherwise the path itself. Same rule as `Tree(Collection)`, which uses the collection itself as registry. A fitted copy whose original is registered with this manager is first resolved to that original (see `isDeFactoPath(Path)`), so that both flavors of a path always resolve to the same version.

   **Signature:** ``getVersionInUse(Path) -> Path``

   **Parameters:**

   * **p** (``Path``): - the path

   **Returns:** (``Path``) the version in use. null if `p` is null

.. method:: isDeFactoPath(p)

   Single source of truth (manager-bound convenience over `Path.isDeFactoPath(Collection)`) for whether `p` should be treated as a normal, standalone/"de facto" path rather than one redundant with an un-fitted counterpart already registered here.

Deliberately checks object identity against `allPaths` rather than looking up `p.getUnfitted().getID()` via `getPathFromID(int)`: registration (e.g. `addTree(Tree, String)` with `forceNewId=true`) reassigns every path a new ID, discarding whatever ID it had in its source file. An un-fitted counterpart that was never registered still carries its *original* file ID, which can -- and in practice does -- collide with the freshly assigned ID of some unrelated, actually-registered path, making an ID-based lookup a false positive.

   **Signature:** ``isDeFactoPath(Path) -> boolean``

   **Parameters:**

   * **p** (``Path``): - the path to check

   **Returns:** (``bool``) true if `p` is not a fitted-version path, or its un-fitted counterpart is not registered with this manager; false if it is redundant and should be skipped

.. method:: isSelected(path)

   Checks if a Path is currently selected in the GUI.

   **Signature:** ``isSelected(Path) -> boolean``

   **Parameters:**

   * **path** (``Path``): - the path to be checked

   **Returns:** (``bool``) true, if is selected

.. method:: size()

   Returns the number of Paths in the PathAndFillManager list.

   **Signature:** ``size() -> int``

   **Returns:** (``int``) the number of Paths


PathFitter
----------

.. method:: getPath()

   **Signature:** ``getPath() -> Path``

   **Returns:** (``Path``) the path being fitted

.. method:: getSucceeded()

   Checks whether the fit succeeded.

   **Signature:** ``getSucceeded() -> boolean``

   **Returns:** (``bool``) true if fit was successful, false otherwise


PathManagerUI
-------------

.. method:: getFilteringToolBar()

   **Signature:** ``getFilteringToolBar() -> JToolBar``

   **Returns:** ``Any``

.. method:: getJTree()

   Gets the JTree component used to display paths.

   **Signature:** ``getJTree() -> JTree``

   **Returns:** (``Any``) the JTree component

.. method:: getNavigationToolBar()

   **Signature:** ``getNavigationToolBar() -> JToolBar``

   **Returns:** ``Any``

.. method:: getPathAndFillManager()

   Gets the PathAndFillManager instance.

   **Signature:** ``getPathAndFillManager() -> PathAndFillManager``

   **Returns:** (``PathAndFillManager``) the PathAndFillManager instance

.. method:: getProofReadingToolBar()

   **Signature:** ``getProofReadingToolBar() -> JToolBar``

   **Returns:** ``Any``

.. method:: getSNT()

   Gets the SNT instance associated with this Path Manager.

   **Signature:** ``getSNT() -> SNT``

   **Returns:** (``SNT``) the SNT instance

.. method:: getSearchable()

   Gets the Searchable interface for the JTree.

   **Signature:** ``getSearchable() -> Searchable``

   **Returns:** (``Any``) the Searchable interface

.. method:: getSelectedPaths(ifNoneSelectedGetAll)

   Gets the paths currently selected in the Manager's `JTree` list.

   **Signature:** ``getSelectedPaths(boolean) -> List``

   **Parameters:**

   * **ifNoneSelectedGetAll** (``bool``): - if true and no paths are currently selected, all Paths in the list will be returned

   **Returns:** (``List[Any]``) the selected paths. Note that children of a Path are not returned if unselected.

.. method:: getSelectedPathsOrganizedByTrees(ifNoneSelectedGetAll)

   Gets the paths currently selected in the Manager's `JTree` list as `Tree`s.

   **Signature:** ``getSelectedPathsOrganizedByTrees(boolean) -> Map``

   **Parameters:**

   * **ifNoneSelectedGetAll** (``bool``): - if true and no paths are currently selected, all Paths in the list are considered

   **Returns:** (``Dict[str, Any]``) the map of selected paths (`as keys`

.. method:: hasTags(p)

   return true if the path name contains any tag delimiters ({ or [).

   **Signature:** ``hasTags(Path) -> boolean``

   **Parameters:**

   * **p** (``Path``)

   **Returns:** ``bool``


PathProfiler
------------

.. method:: cancel()

   **Signature:** ``cancel() -> void``

   **Returns:** ``None``

.. method:: getMultiFrameProfile(paths, channel, nSamples, normalizeDistance)

   Builds a multi-frame intensity profile matrix from a list of matched paths (one per time frame, ordered by frame number), suitable for kymograph-style visualization via 
```
SNTChart.showHeatmap(double[][], net.imglib2.display.ColorTable, java.lang.String...)
```
.

The returned matrix has dimensions [nPaths][nSamples], where `matrix[i][j]` is the interpolated intensity at distance sample j for the i-th path. Entries beyond a path's actual length are `Double.NaN`.

   **Signature:** ``getMultiFrameProfile(List, int, int, boolean) -> double[][]``

   **Parameters:**

   * **paths** (``List[Any]``): - ordered list of paths, one per time frame
   * **channel** (``int``)
   * **nSamples** (``int``)
   * **normalizeDistance** (``bool``)

   **Returns:** (``List[List[float]]``) a 2D array [nPaths][nSamples] of intensity values

.. method:: getPlot()

   Gets the plot profile as an ImageJ plot (all channels included).

   **Signature:** ``getPlot() -> Plot``

   **Returns:** (``Any``) the plot

.. method:: getResampledValues(p, channel, nSamples, gridMax)

   Resamples the intensity profile of a path onto a uniform distance grid via linear interpolation. Entries beyond the path's actual length are set to `Double.NaN`, which allows variable-length paths to be compared in the same matrix without padding with zeros.

   **Signature:** ``getResampledValues(Path, int, int, double) -> double[]``

   **Parameters:**

   * **p** (``Path``): - the path to profile (values are assigned if not yet set)
   * **channel** (``int``)
   * **nSamples** (``int``)
   * **gridMax** (``float``)

   **Returns:** (``List[float]``) array of length `nSamples` with interpolated intensities

.. method:: getTimeProfile(path, channel)

   Gets the time profile for the specified path as a list of `getValues(Path, int, int)` profiles, with one entry per frame of the dataset.

   **Signature:** ``getTimeProfile(Path, int) -> List``

   **Parameters:**

   * **path** (``Path``): - the path to be profiled
   * **channel** (``int``)

   **Returns:** (``List[Any]``) the list of profile values (one entry per frame)

.. method:: getValues(p)

   Gets the profile for the specified path as a map of lists, with distances (or indices) stored under `X_VALUES` ("x-values") and intensities under `Y_VALUES` ("y-values").

   **Signature:** ``getValues(Path) -> Map``

   **Parameters:**

   * **p** (``Path``): - the path to be profiled

   **Returns:** (``Dict[str, Any]``) the profile map

.. method:: getXYPlot()

   Gets the plot profile as an `PlotService` plot. It is recommended to call `DynamicCommand.setContext(org.scijava.Context)` beforehand.

   **Signature:** ``getXYPlot() -> XYPlot``

   **Returns:** ``Any``

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``


PathStatistics
--------------

.. method:: getAllMetrics()

   **Signature:** ``getAllMetrics() -> List``

   **Returns:** ``List[Any]``

.. method:: getAnnotatedLength(level)

   **Signature:** ``getAnnotatedLength(int) -> Map``

   **Parameters:**

   * **level** (``int``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedLengthHistogram()

   **Signature:** ``getAnnotatedLengthHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedLengthsByHemisphere(level)

   **Signature:** ``getAnnotatedLengthsByHemisphere(int) -> Map``

   **Parameters:**

   * **level** (``int``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotations()

   **Signature:** ``getAnnotations() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvgBranchLength()

   **Signature:** ``getAvgBranchLength() -> double``

   **Returns:** ``float``

.. method:: getAvgContraction()

   **Signature:** ``getAvgContraction() -> double``

   **Returns:** ``float``

.. method:: getAvgFractalDimension()

   **Signature:** ``getAvgFractalDimension() -> double``

   **Returns:** ``float``

.. method:: getAvgFragmentation()

   **Signature:** ``getAvgFragmentation() -> double``

   **Returns:** ``float``

.. method:: getAvgPartitionAsymmetry()

   **Signature:** ``getAvgPartitionAsymmetry() -> double``

   **Returns:** ``float``

.. method:: getAvgRemoteBifAngle()

   **Signature:** ``getAvgRemoteBifAngle() -> double``

   **Returns:** ``float``

.. method:: getBranchPoints()

   **Signature:** ``getBranchPoints() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getBranches()

   Gets all the paths being analyzed as branches.

In PathStatistics, all paths are considered as branches since each path represents a distinct structural element.

   **Signature:** ``getBranches() -> List``

   **Returns:** (``List[Any]``) the list of all paths

.. method:: getCableLength()

   **Signature:** ``getCableLength() -> double``

   **Returns:** ``float``

.. method:: getCableLengthNorm(compartment)

   **Signature:** ``getCableLengthNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **compartment** (``Any``)

   **Returns:** ``float``

.. method:: getConvexAnalyzer()

   **Signature:** ``getConvexAnalyzer() -> ConvexHullAnalyzer``

   **Returns:** ``ConvexHullAnalyzer``

.. method:: getConvexHullMetric(metric)

   **Signature:** ``getConvexHullMetric(String) -> double``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``float``

.. method:: getDepth()

   **Signature:** ``getDepth() -> double``

   **Returns:** ``float``

.. method:: getDescriptiveStats(metric)

   **Signature:** ``getDescriptiveStats(String) -> DescriptiveStatistics``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``Any``

.. method:: getFlowPlot(feature, annotations)

   **Signature:** ``getFlowPlot(String, Collection) -> SNTChart``

   **Parameters:**

   * **feature** (``str``)
   * **annotations** (``List[Any]``)

   **Returns:** ``SNTChart``

.. method:: getFractalDimension()

   **Signature:** ``getFractalDimension() -> List``

   **Returns:** ``List[Any]``

.. method:: getHeight()

   **Signature:** ``getHeight() -> double``

   **Returns:** ``float``

.. method:: getHighestPathOrder()

   **Signature:** ``getHighestPathOrder() -> int``

   **Returns:** ``int``

.. method:: getHistogram(metric)

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``SNTChart``

.. method:: getInnerBranches()

   Gets the inner branches from the analyzed paths.

In PathStatistics, inner branches are equivalent to primary branches.

   **Signature:** ``getInnerBranches() -> List``

   **Returns:** (``List[Any]``) the list of inner branches (same as primary branches)

.. method:: getInnerLength()

   Gets the total length of inner branches.

In PathStatistics, this returns the same value as `getPrimaryLength()`.

   **Signature:** ``getInnerLength() -> double``

   **Returns:** (``float``) the total length of inner branches

.. method:: getMetric(metric)

   Gets a specific metric value for an individual path.

This method provides direct access to morphometric properties of individual paths, including geometric measurements, connectivity information, and structural characteristics. It supports all standard path metrics plus PathStatistics-specific measurements.

Supported metrics include:

- Geometric: length, volume, surface area, mean radius

- Structural: number of nodes, branch points, children

- Angular: extension angles in XY, XZ, ZY planes

- Morphological: contraction, fractal dimension, spine density

- Metadata: path ID, channel, frame, order

   **Signature:** ``getMetric(String) -> Number``

   **Parameters:**

   * **metric** (``str``): - the name of the metric to retrieve

   **Returns:** (``Union[int, float]``) the metric value for the specified path

.. method:: getMetrics()

   **Signature:** ``getMetrics() -> List``

   **Returns:** ``List[Any]``

.. method:: getNBranchPoints(annot)

   **Signature:** ``getNBranchPoints(BrainAnnotation) -> int``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``int``

.. method:: getNBranchPointsNorm(annot)

   **Signature:** ``getNBranchPointsNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``float``

.. method:: getNBranches()

   Gets the number of branches (paths) being analyzed.

Returns the total count of paths in this PathStatistics instance.

   **Signature:** ``getNBranches() -> int``

   **Returns:** (``int``) the number of paths

.. method:: getNNodes()

   **Signature:** ``getNNodes() -> long``

   **Returns:** ``int``

.. method:: getNPaths()

   **Signature:** ``getNPaths() -> int``

   **Returns:** ``int``

.. method:: getNTips(annot)

   **Signature:** ``getNTips(BrainAnnotation) -> int``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``int``

.. method:: getNTipsNorm(annot)

   **Signature:** ``getNTipsNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **annot** (``Any``)

   **Returns:** ``float``

.. method:: getNoSpinesOrVaricosities()

   **Signature:** ``getNoSpinesOrVaricosities() -> int``

   **Returns:** ``int``

.. method:: getNodeStatistics()

   **Signature:** ``getNodeStatistics() -> NodeStatistics``

   **Returns:** ``NodeStatistics``

.. method:: getParsedTree()

   **Signature:** ``getParsedTree() -> Tree``

   **Returns:** ``Tree``

.. method:: getPartitionAsymmetry()

   **Signature:** ``getPartitionAsymmetry() -> List``

   **Returns:** ``List[Any]``

.. method:: getPolarHistogram(metric)

   **Signature:** ``getPolarHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``SNTChart``

.. method:: getPrimaryBranches()

   Gets the primary branches from the analyzed paths.

Returns only those paths that are marked as primary branches, typically those that originate directly from the root or soma.

   **Signature:** ``getPrimaryBranches() -> List``

   **Returns:** (``List[Any]``) the list of primary paths

.. method:: getPrimaryLength()

   Gets the total length of primary branches.

Calculates the sum of lengths of all paths marked as primary branches.

   **Signature:** ``getPrimaryLength() -> double``

   **Returns:** (``float``) the total length of primary branches

.. method:: getPrimaryPaths()

   **Signature:** ``getPrimaryPaths() -> List``

   **Returns:** ``List[Any]``

.. method:: getRemoteBifAngles()

   **Signature:** ``getRemoteBifAngles() -> List``

   **Returns:** ``List[Any]``

.. method:: getRootAngleAnalyzer()

   **Signature:** ``getRootAngleAnalyzer() -> RootAngleAnalyzer``

   **Returns:** ``RootAngleAnalyzer``

.. method:: getRootAngleMetric(metric)

   **Signature:** ``getRootAngleMetric(String) -> double``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``float``

.. method:: getShollAnalyzer()

   **Signature:** ``getShollAnalyzer() -> ShollAnalyzer``

   **Returns:** ``ShollAnalyzer``

.. method:: getSpineOrVaricosityDensity()

   **Signature:** ``getSpineOrVaricosityDensity() -> double``

   **Returns:** ``float``

.. method:: getStrahlerAnalyzer()

   **Signature:** ``getStrahlerAnalyzer() -> StrahlerAnalyzer``

   **Returns:** ``StrahlerAnalyzer``

.. method:: getStrahlerBifurcationRatio()

   **Signature:** ``getStrahlerBifurcationRatio() -> double``

   **Returns:** ``float``

.. method:: getStrahlerNumber()

   **Signature:** ``getStrahlerNumber() -> int``

   **Returns:** ``int``

.. method:: getSummaryStats(metric)

   Description copied from class: `TreeStatistics`

   **Signature:** ``getSummaryStats(String) -> SummaryStatistics``

   **Parameters:**

   * **metric** (``str``): - the measurement (TreeStatistics.N_NODES, TreeStatistics.NODE_RADIUS, etc.)

   **Returns:** (``Any``) the SummaryStatistics object.

.. method:: getTable()

   **Signature:** ``getTable() -> DefaultGenericTable``

   **Returns:** ``Any``

.. method:: getTerminalBranches()

   Gets the terminal branches from the analyzed paths.

Returns paths that have children, representing non-terminal segments. Note: This implementation differs from typical terminal branch definition as it returns paths with children rather than leaf paths.

   **Signature:** ``getTerminalBranches() -> List``

   **Returns:** (``List[Any]``) the list of paths with children

.. method:: getTerminalLength()

   Gets the total length of terminal branches.

Calculates the sum of lengths of all terminal branches as defined by `getTerminalBranches()`.

   **Signature:** ``getTerminalLength() -> double``

   **Returns:** (``float``) the total length of terminal branches

.. method:: getTips()

   **Signature:** ``getTips() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getUnit(metric)

   **Signature:** ``getUnit(String) -> String``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``str``

.. method:: getWidth()

   **Signature:** ``getWidth() -> double``

   **Returns:** ``float``

.. method:: isExactMetricMatch()

   **Signature:** ``isExactMetricMatch() -> boolean``

   **Returns:** ``bool``

.. method:: isValid()

   **Signature:** ``isValid() -> boolean``

   **Returns:** ``bool``


PersistenceAnalyzer
-------------------

.. method:: getBarcode(descriptor)

   Gets the persistence barcode for the specified filter function.

The barcode is a simplified representation of the persistence diagram that contains only the persistence values (death - birth) for each topological feature, akin to a one-dimensional summary of branch significance.

**Interpretation:**

- **High values:** Morphologically significant branches

- **Low values:** Minor branches or potential noise

- **Distribution:** The spread of values indicates branching complexity

**Special Properties:**

- All values are non-negative (|death - birth|)

- For geodesic descriptor: sum of all values equals total cable length

- Number of values equals number of tips in the tree

**Example Usage:** 
```
List<Double> barcode = analyzer.getBarcode("geodesic");
 
 // Find most significant branches
 barcode.sort(Collections.reverseOrder());
 System.out.println("Top 5 most persistent branches:");
 for (int i = 0; i < Math.min(5, barcode.size()); i++) {
     System.out.println("Branch " + (i+1) + ": " + barcode.get(i));
 }
```


   **Signature:** ``getBarcode(String) -> List``

   **Parameters:**

   * **descriptor** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z".

   **Returns:** (``List[Any]``) the barcode as a list of persistence values (death - birth). Each value represents the "lifespan" or significance of a topological feature (branch).

   **Example:**

   .. code-block:: java

      List<Double> barcode = analyzer.getBarcode("geodesic");
       
       // Find most significant branches
       barcode.sort(Collections.reverseOrder());
       System.out.println("Top 5 most persistent branches:");
       for (int i = 0; i < Math.min(5, barcode.size()); i++) {
           System.out.println("Branch " + (i+1) + ": " + barcode.get(i));
       }

.. method:: getDescriptors()

   Gets a list of supported descriptor functions for persistence analysis.

Returns the string identifiers for all available filter functions that can be used with `getDiagram(String)`, `getBarcode(String)`, and other analysis methods. These descriptors are case-insensitive when used in method calls.

   **Signature:** ``getDescriptors() -> List``

   **Returns:** (``List[Any]``) the list of available descriptors: ["geodesic", "radial", "centrifugal", "path order", "x", "y", "z"]

.. method:: getDiagram(descriptor)

   Gets the persistence diagram for the specified filter function.

The persistence diagram is the core output of the analysis, consisting of birth-death pairs that represent the "lifespan" of topological features (branches) during the filtration process. Each point in the diagram corresponds to a branch in the neuronal tree.

**Structure:** Returns a list where each inner list contains exactly two values:

- **Birth [0]:** The filter value where the branch appears (branch point)

- **Death [1]:** The filter value where the branch disappears (tip)

**Properties:**

- Number of points = Number of tips in the tree

- All values are non-negative

- For geodesic descriptor: sum of all (death-birth) = total cable length

- High persistence (death-birth) indicates morphologically significant branches

**Example usage:** 
```
List<List<Double>> diagram = analyzer.getDiagram("geodesic");
 for (List<Double> point : diagram) {
     double birth = point.get(0);
     double death = point.get(1);
     double persistence = death - birth;
     System.out.println("Branch: persistence = " + persistence);
 }
```


   **Signature:** ``getDiagram(String) -> List``

   **Parameters:**

   * **descriptor** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z". Alternative names like "reverse strahler" for "centrifugal" are also accepted.

   **Returns:** (``List[Any]``) the persistence diagram as a list of [birth, death] pairs. Each inner list contains exactly two Double values representing the birth and death of a topological feature.

   **Example:**

   .. code-block:: java

      List<List<Double>> diagram = analyzer.getDiagram("geodesic");
       for (List<Double> point : diagram) {
           double birth = point.get(0);
           double death = point.get(1);
           double persistence = death - birth;
           System.out.println("Branch: persistence = " + persistence);
       }

.. method:: getDiagramNodes(descriptor)

   Gets the tree nodes associated with each point in the persistence diagram.

This method returns the actual `SWCPoint` nodes from the neuronal tree that correspond to each birth-death pair in the persistence diagram. This allows you to map topological features back to specific locations in the original morphology.

**Structure:** Returns a list where each inner list contains exactly two nodes:

- **Birth Node [0]:** The branch point where the topological feature appears

- **Death Node [1]:** The tip node where the topological feature disappears

**Correspondence:** The order of node pairs matches the order of birth-death pairs returned by `getDiagram(String)`, allowing direct correlation between topological features and their spatial locations.

**Example Usage:** 
```
List<List<Double>> diagram = analyzer.getDiagram("geodesic");
 List<List<SWCPoint>> nodes = analyzer.getDiagramNodes("geodesic");
 
 for (int i = 0; i < diagram.size(); i++) {
     List<Double> birthDeath = diagram.get(i);
     List<SWCPoint> nodesPair = nodes.get(i);
     
     double persistence = birthDeath.get(1) - birthDeath.get(0);
     SWCPoint branchPoint = nodesPair.get(0);
     SWCPoint tipPoint = nodesPair.get(1);
     
     System.out.printf("Branch with persistence %.2f: from (%.1f,%.1f,%.1f) to (%.1f,%.1f,%.1f)%n",
                       persistence, 
                       branchPoint.getX(), branchPoint.getY(), branchPoint.getZ(),
                       tipPoint.getX(), tipPoint.getY(), tipPoint.getZ());
 }
```


   **Signature:** ``getDiagramNodes(String) -> List``

   **Parameters:**

   * **descriptor** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z".

   **Returns:** (``List[Any]``) the persistence diagram nodes as a list of [birth_node, death_node] pairs. Each inner list contains exactly two SWCPoint objects representing the spatial locations of the topological feature.

   **Example:**

   .. code-block:: java

      List<List<Double>> diagram = analyzer.getDiagram("geodesic");
       List<List<SWCPoint>> nodes = analyzer.getDiagramNodes("geodesic");
       
       for (int i = 0; i < diagram.size(); i++) {
           List<Double> birthDeath = diagram.get(i);
           List<SWCPoint> nodesPair = nodes.get(i);
           
           double persistence = birthDeath.get(1) - birthDeath.get(0);
           SWCPoint branchPoint = nodesPair.get(0);
           SWCPoint tipPoint = nodesPair.get(1);
           
           System.out.printf("Branch with persistence %.2f: from (%.1f,%.1f,%.1f) to (%.1f,%.1f,%.1f)%n",
                             persistence, 
                             branchPoint.getX(), branchPoint.getY(), branchPoint.getZ(),
                             tipPoint.getX(), tipPoint.getY(), tipPoint.getZ());
       }

.. method:: getLandscape(descriptor, numLandscapes, resolution)

   Gets the persistence landscape as a vectorized representation.

Persistence landscapes transform persistence diagrams into a vector space representation that The landscape is a collection of piecewise-linear functions that capture the "shape" of the persistence diagram in a stable, vectorized format.

**Mathematical Background:** Each point (birth, death) in the persistence diagram contributes a "tent" function to the landscape. The k-th landscape function at any point is the k-th largest value among all tent functions at that point. This creates a stable, multi-resolution representation of the topological features.

**Output Structure:** Returns a 1D array of length `numLandscapes × resolution` where the first `resolution` values represent the first landscape function, the next `resolution` values represent the second landscape function, and so on.

   **Signature:** ``getLandscape(String, int, int) -> double[]``

   **Parameters:**

   * **descriptor** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z".
   * **numLandscapes** (``int``)
   * **resolution** (``int``)

   **Returns:** (``List[float]``) the persistence landscape as a 1D array of length `numLandscapes × resolution`. All values are non-negative and scaled by √2 for proper L² normalization.


PlausibilityCalibrator
----------------------

.. method:: getCurationsDirectory(workspaceDir)

   **Signature:** ``getCurationsDirectory(File) -> File``

   **Parameters:**

   * **workspaceDir** (``str``)

   **Returns:** ``str``


PlausibilityMonitor
-------------------

.. method:: getCurrentWarnings()

   **Signature:** ``getCurrentWarnings() -> List``

   **Returns:** ``List[Any]``

.. method:: getDeepCheck(type)

   **Signature:** ``getDeepCheck(Class) -> DeepCheck``

   **Parameters:**

   * **type** (``type``)

   **Returns:** ``Any``

.. method:: getDeepChecks()

   **Signature:** ``getDeepChecks() -> List``

   **Returns:** ``List[Any]``

.. method:: getLiveCheck(type)

   **Signature:** ``getLiveCheck(Class) -> LiveCheck``

   **Parameters:**

   * **type** (``type``)

   **Returns:** ``Any``

.. method:: getLiveChecks()

   **Signature:** ``getLiveChecks() -> List``

   **Returns:** ``List[Any]``

.. method:: isEnabled()

   **Signature:** ``isEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isLastUpdateFromLiveCheck()

   **Signature:** ``isLastUpdateFromLiveCheck() -> boolean``

   **Returns:** ``bool``


PointInImage
------------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the neuropil annotation assigned to this point

.. method:: getCoordinateOnAxis(axis)

   Gets the coordinate along the specified axis.

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **axis** (``int``): - the axis. Either Tree.X_AXIS, Tree.Y_AXIS, or Tree.Z_AXIS

   **Returns:** (``float``) the coordinate on the specified axis

.. method:: getHemisphere()

   **Signature:** ``getHemisphere() -> char``

   **Returns:** ``str``

.. method:: getPath()

   Returns the Path associated with this node (if any)

   **Signature:** ``getPath() -> Path``

   **Returns:** (``Path``) the path associated with this node or null if `setPath(Path)` has not been called.

.. method:: getUnscaledPoint()

   Converts the coordinates of this point into pixel units if this point is associated with a Path.

   **Signature:** ``getUnscaledPoint() -> PointInCanvas``

   **Returns:** ``Any``

.. method:: getX()

   **Signature:** ``getX() -> double``

   **Returns:** (``float``) the X-coordinate of the point

.. method:: getY()

   **Signature:** ``getY() -> double``

   **Returns:** (``float``) the Y-coordinate of the point

.. method:: getZ()

   **Signature:** ``getZ() -> double``

   **Returns:** (``float``) the Z-coordinate of the point

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isReal()

   **Signature:** ``isReal() -> boolean``

   **Returns:** ``bool``

.. method:: isSameLocation(pim)

   **Signature:** ``isSameLocation(PointInImage) -> boolean``

   **Parameters:**

   * **pim** (``PointInImage``)

   **Returns:** ``bool``


PolarProfileStats
-----------------

.. method:: getAngleStepSize()

   **Signature:** ``getAngleStepSize() -> double``

   **Returns:** ``float``

.. method:: getAngularDistribution()

   **Signature:** ``getAngularDistribution() -> double[]``

   **Returns:** ``List[float]``

.. method:: getAngularDistributionCoherence()

   **Signature:** ``getAngularDistributionCoherence() -> double``

   **Returns:** ``float``

.. method:: getDataMode()

   **Signature:** ``getDataMode() -> DataMode``

   **Returns:** ``Any``

.. method:: getFitYValues()

   **Signature:** ``getFitYValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getMatrix()

   **Signature:** ``getMatrix() -> double[][]``

   **Returns:** ``List[List[float]]``

.. method:: getN()

   **Signature:** ``getN() -> int``

   **Returns:** ``int``

.. method:: getOrientationDistributionCoherence()

   **Signature:** ``getOrientationDistributionCoherence() -> double``

   **Returns:** ``float``

.. method:: getPlot()

   **Signature:** ``getPlot() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getPreferredDirection()

   **Signature:** ``getPreferredDirection() -> double``

   **Returns:** ``float``

.. method:: getPreferredOrientation()

   **Signature:** ``getPreferredOrientation() -> double``

   **Returns:** ``float``

.. method:: getProfile()

   **Signature:** ``getProfile() -> Profile``

   **Returns:** ``Profile``

.. method:: getReport()

   **Signature:** ``getReport() -> Report``

   **Returns:** ``Any``

.. method:: getXValues()

   **Signature:** ``getXValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getYValues()

   **Signature:** ``getYValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: setAngleStepSize(angleStepSize)

   **Signature:** ``setAngleStepSize(double) -> void``

   **Parameters:**

   * **angleStepSize** (``float``)

   **Returns:** ``None``


Profile
-------

.. method:: getCountAtRadius(radius)

   **Signature:** ``getCountAtRadius(double) -> double``

   **Parameters:**

   * **radius** (``float``)

   **Returns:** ``float``

.. method:: getExtraMeasurement()

   **Signature:** ``getExtraMeasurement() -> String``

   **Returns:** ``str``

.. method:: getProperties()

   **Signature:** ``getProperties() -> Properties``

   **Returns:** ``Any``

.. method:: getROIs()

   **Signature:** ``getROIs() -> Overlay``

   **Returns:** ``Any``

.. method:: hasExtraMeasurement()

   **Signature:** ``hasExtraMeasurement() -> boolean``

   **Returns:** ``bool``

.. method:: hasPoints()

   **Signature:** ``hasPoints() -> boolean``

   **Returns:** ``bool``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isEmpty()

   **Signature:** ``isEmpty() -> boolean``

   **Returns:** ``bool``

.. method:: isIntDensityProfile()

   **Signature:** ``isIntDensityProfile() -> boolean``

   **Returns:** ``bool``

.. method:: size()

   **Signature:** ``size() -> int``

   **Returns:** ``int``

.. method:: stepSize()

   **Signature:** ``stepSize() -> double``

   **Returns:** ``float``


RemoteSWCLoader
---------------

.. method:: getReader(cellId)

   **Signature:** ``getReader(String) -> BufferedReader``

   **Parameters:**

   * **cellId** (``str``)

   **Returns:** ``Any``

.. method:: getReconstructionURL(cellId)

   **Signature:** ``getReconstructionURL(String) -> String``

   **Parameters:**

   * **cellId** (``str``)

   **Returns:** ``str``

.. method:: getTree(cellId)

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **cellId** (``str``)

   **Returns:** ``Tree``

.. method:: isDatabaseAvailable()

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** ``bool``


RootAngleAnalyzer
-----------------

.. method:: getAnalysis()

   **Signature:** ``getAnalysis() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getAngles()

   **Signature:** ``getAngles() -> List``

   **Returns:** (``List[Any]``) the list of root angles sorted from leaves to root (in degrees).

.. method:: getCramerVonMisesStatistic()

   Computes the Cramér-von Mises statistic between computed root angles and fitted von Mises distribution. A value of 0 indicates a perfect fit between the empirical distribution and the theoretical distribution, and larger values indicate a greater discrepancy between the two distributions.

   **Signature:** ``getCramerVonMisesStatistic() -> double``

   **Returns:** (``float``) the Cramér-von Mises statistic. Range: [0, ∞[ (dimensionless).

.. method:: getDensityPlot()

   **Signature:** ``getDensityPlot() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getDescriptiveStatistics()

   **Signature:** ``getDescriptiveStatistics() -> DescriptiveStatistics``

   **Returns:** (``Any``) the descriptive statistics of the root angles (in degrees).

.. method:: getHistogram(polar)

   **Signature:** ``getHistogram(boolean) -> SNTChart``

   **Parameters:**

   * **polar** (``bool``)

   **Returns:** ``SNTChart``

.. method:: getTaggedGraph()

   **Signature:** ``getTaggedGraph() -> DirectedWeightedGraph``

   **Returns:** (``DirectedWeightedGraph``) the graph of the tree being parsed. Vertices are tagged with the root angles (See: `PointInImage.v`).

.. method:: getTaggedTree()

   Returns a recolored copy of the analyzed tree with the root angles assigned to its node values.

   **Signature:** ``getTaggedTree() -> Tree``

   **Returns:** ``Tree``


SNT
---

.. method:: cancelPath()

   Cancels the temporary path.

   **Signature:** ``cancelPath() -> void``

   **Returns:** ``None``

.. method:: cancelSearch(cancelFillToo)

   **Signature:** ``cancelSearch(boolean) -> void``

   **Parameters:**

   * **cancelFillToo** (``bool``)

   **Returns:** ``None``

.. method:: cancelTemporary()

   **Signature:** ``cancelTemporary() -> void``

   **Returns:** ``None``

.. method:: getActiveCanvasPixelOffset()

   **Signature:** ``getActiveCanvasPixelOffset() -> PointInCanvas``

   **Returns:** (``Any``) the pixel offset (in whatever grid `ctSlice3d`/`getLoadedData()` is currently indexed by - the crop-local grid when a materialized crop is active, or the raw streamed source's own voxel grid otherwise) of (0,0,0) in the true/world grid `Path` node coordinates are stored in

.. method:: getAverageSeparation()

   **Signature:** ``getAverageSeparation() -> double``

   **Returns:** ``float``

.. method:: getBatchRetraceChannelFrame()

   **Signature:** ``getBatchRetraceChannelFrame() -> int[]``

   **Returns:** (``List[int]``) `{channel, frame}` (1-based) the active batch re-trace is running against, or `null` if none is active. See `setBatchRetraceChannelFrame(java.lang.Integer, java.lang.Integer)`.

.. method:: getCalibration()

   **Signature:** ``getCalibration() -> Calibration``

   **Returns:** (``Any``) this session's current spatial calibration (pixel width/height/depth and unit), for converting between pixel and world/calibrated coordinates without affecting world origin: see `setWorldOriginOffset(double, double, double)` for the separate mechanism that handles a non-zero-anchored source.

Calibration is trusted from initialized ImagePlus (traditional mode) or from the stream source in Stream mode (`isSpacingKnownFromSource()`); If the streamed N5/Zarr source whose own `getVoxelDimensions()` returned null (see `BigDataLoaderCmd#applyFallbackCalibration` ), this falls back to a representative loaded `Path`'s own calibration.

That fallback is inherently a guess SNT cannot verify: nothing guarantees a loaded Path (e.g. imported from an SWC/traces file) was actually traced against the currently streamed source, so its calibration could be wrong for this data. Callers driving user-facing operations should warn accordingly, see `SNTUI#materializeDisplayCanvas()`'s use of `isSpacingKnownFromSource()`.

.. method:: getCanvas(pane)

   **Signature:** ``getCanvas(int) -> TracerCanvas``

   **Parameters:**

   * **pane** (``int``)

   **Returns:** ``TracerCanvas``

.. method:: getChannel()

   **Signature:** ``getChannel() -> int``

   **Returns:** ``int``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getCostType()

   **Signature:** ``getCostType() -> CostType``

   **Returns:** ``Any``

.. method:: getCurrentPath()

   **Signature:** ``getCurrentPath() -> Path``

   **Returns:** ``Path``

.. method:: getDataset()

   Gets the Image being traced as Dataset. If the loaded image has been closed, cached pixel data is returned as per `getLoadedDataAsImp()`. If no resident `ImagePlus` exists at all (e.g., data streamed from disk/network, backed only by `ctSlice3d`), a Dataset is instead built directly from `getLoadedDataAsImg(boolean)`, so Dataset-only commands. Null is returned if no image data exists at all.

NB: in the streamed-data fallback, the returned Dataset only ever contains a single channel/ frame (whichever is currently active): `ctSlice3d` is a single C/T slice by construction. Commands that need every channel or frame simultaneously will still require a resident `ImagePlus`.

NB2: a materialized crop (see `isMaterializedCrop()`) always has a resident `ImagePlus` (the crop itself), so it never takes the streamed-data fallback above, returning the crop's own Dataset as-is, matching whatever `buildMaterializedCrop(BoundingBox)` captured (see `getMaterializedCropChannel()`/`getMaterializedCropFrame()`).

   **Signature:** ``getDataset() -> Dataset``

   **Returns:** ``Any``

.. method:: getDefaultCanvasPixelOffset()

   Public wrapper around `defaultCanvasPixelOffset()`, for callers outside this class that need the crop-independent baseline offset even while a materialized crop is active on the classic 2D canvas - e.g. a BDV/BVV interaction that should behave the same regardless of what the classic canvas currently has materialized, mirroring how 
```
createSearch(double, double, double, double, double, double, SearchSettingsSnapshot, boolean)
```
's `useStreamedSource` parameter picks between the two.

   **Signature:** ``getDefaultCanvasPixelOffset() -> PointInCanvas``

   **Returns:** (``Any``) the same value as `getActiveCanvasPixelOffset()` whenever no crop is materialized; the crop-independent baseline otherwise

.. method:: getDepth()

   **Signature:** ``getDepth() -> int``

   **Returns:** ``int``

.. method:: getDrawDiameters()

   **Signature:** ``getDrawDiameters() -> boolean``

   **Returns:** ``bool``

.. method:: getEditModeBlocker()

   As `getEditModeBlocker()`, for front-ends that select the path to be edited themselves (e.g., the one nearest to the cursor) when no single path is selected

   **Signature:** ``getEditModeBlocker() -> String``

   **Returns:** ``str``

.. method:: getFillThreshold()

   **Signature:** ``getFillThreshold() -> double``

   **Returns:** ``float``

.. method:: getFilledBinaryImp()

   **Signature:** ``getFilledBinaryImp() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getFilledDistanceImp()

   **Signature:** ``getFilledDistanceImp() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getFilledImp()

   **Signature:** ``getFilledImp() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getFilledLabelImp()

   **Signature:** ``getFilledLabelImp() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getFilledMeshes(smoothing)

   Converts the currently loaded fills to meshes, one per fill, in the spatially calibrated coordinates of the image (the same space as path nodes). Only voxels within each fill's threshold are included.

   **Signature:** ``getFilledMeshes(double) -> Map``

   **Parameters:**

   * **smoothing** (``float``): - the sigma (in calibrated units) of a Gaussian blur applied before meshing. 0 disables smoothing. Note that thin fills shrink and may vanish if smoothed

   **Returns:** (``Dict[str, Any]``) the (non-empty) meshes, mapped by name (that of the source path(s) of each fill, or "Fill_1", "Fill_2", etc. if undefined). Empty if no fills are loaded

.. method:: getFilterType()

   **Signature:** ``getFilterType() -> FilterType``

   **Returns:** ``Any``

.. method:: getFrame()

   **Signature:** ``getFrame() -> int``

   **Returns:** ``int``

.. method:: getFullImageDimensions()

   Returns the dimensions of the full loaded image/dataset, even while a materialized crop (see `materializeDisplayCanvas(BoundingBox)`) is installed as this session's own canvas. Unlike `width`/`height`/`depth`, which temporarily reflect the crop's own (small) size for as long as it stays open (see `installMaterializedCrop(sc.fiji.snt.SNT.MaterializedCrop)`), this always resolves against `streamedSourceData` (the pristine, pre-crop source) when one is cached, falling back to width/height/depth otherwise (i.e. no crop is open, or this is a classic/non-streamed session where streamedSourceData is never populated).

Intended for callers that need the true dataset extent regardless of any transient crop, e.g. `PathAndFillManager.writeXML(java.lang.String, boolean)` when writing the `<imagesize>` element of a .traces file.

   **Signature:** ``getFullImageDimensions() -> int[]``

   **Returns:** (``List[int]``) `{width, height, depth}` of the full dataset

.. method:: getFullSourceData()

   Non-generic wrapper around `getStreamedOrLoadedData()`, for callers outside this class that need the full, crop-independent source data - e.g. BDV/BVV's own tracing/search (shared by both viewers, see `AbstractBigViewer`) or the Sigma preview palette, which must show data around the point actually clicked, not clamped to whatever (possibly smaller) crop happens to be materialized on the classic canvas at the same time. In classic (non-streamed) sessions this is simply `getLoadedData()`, since no crop can ever be materialized there. Pair with `getDefaultCanvasPixelOffset()` for converting a click into a pixel index into this data.

   **Signature:** ``getFullSourceData() -> RandomAccessibleInterval``

   **Returns:** (``Any``) the same data as `getStreamedOrLoadedData()`

.. method:: getFullSourceDataAsImp()

   Crop-independent counterpart of `getLoadedDataAsImp()`: the full source data (`getFullSourceData()`) as an ImagePlus, e.g., for a preview that must show the region actually clicked in BDV/BVV regardless of the crop that may be materialized on the classic canvas. Its pixel grid is the one described by `getDefaultCanvasPixelOffset()`. Same as `getLoadedDataAsImp()` if no crop is materialized.

   **Signature:** ``getFullSourceDataAsImp() -> ImagePlus``

   **Returns:** (``Any``) the full source data, or null if no image data has been loaded

.. method:: getHeight()

   **Signature:** ``getHeight() -> int``

   **Returns:** ``int``

.. method:: getHeuristicType()

   **Signature:** ``getHeuristicType() -> HeuristicType``

   **Returns:** ``Any``

.. method:: getImageFilenamePrefix()

   Returns a filesystem-safe basename identifying the image currently being traced, for use as a prefix when generating output filenames (backups, exported bookmarks, notes, etc). Handles both standard mode (title of `getImagePlus()`) and `stream mode` (title of the source loaded in the active `big viewer`, if any).

   **Signature:** ``getImageFilenamePrefix() -> String``

   **Returns:** (``str``) the sanitized, extension-stripped image basename, or a fallback placeholder ("streamed_data"/"snt_data") if unavailable

.. method:: getImagePlus()

   Gets the Image associated with a view pane.

   **Signature:** ``getImagePlus() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getIsolatedTreeID()

   **Signature:** ``getIsolatedTreeID() -> int``

   **Returns:** (``int``) the ID of the currently isolated tree, or -1 if no isolation is active

.. method:: getLastTracedPath()

   Returns the path most recently traced interactively in this session, as opposed to paths loaded from file or created by other means.

   **Signature:** ``getLastTracedPath() -> Path``

   **Returns:** (``Path``) the path, or null if no path has been traced yet or it no longer exists

.. method:: getLoadedData()

   **Signature:** ``getLoadedData() -> RandomAccessibleInterval``

   **Returns:** ``Any``

.. method:: getLoadedDataAsImg(secondaryLayer)

   **Signature:** ``getLoadedDataAsImg(boolean) -> ImgPlus``

   **Parameters:**

   * **secondaryLayer** (``bool``)

   **Returns:** ``Any``

.. method:: getLoadedDataAsImp()

   Retrieves the pixel data of the main image currently loaded in memory as an ImagePlus object. Returned image is always a single channel image.

   **Signature:** ``getLoadedDataAsImp() -> ImagePlus``

   **Returns:** (``Any``) the loaded data corresponding to the C,T position currently being traced, or null if no image data has been loaded into memory.

.. method:: getLoadedIterable()

   **Signature:** ``getLoadedIterable() -> IterableInterval``

   **Returns:** ``Any``

.. method:: getMaterializationMemoryBudget()

   **Signature:** ``getMaterializationMemoryBudget() -> long``

   **Returns:** (``int``) the number of bytes currently available for a `materializeDisplayCanvas(BoundingBox)` call, i.e. `MEM_FRACTION` of free heap. `Long.MAX_VALUE` if the JVM's max memory cannot be determined.

.. method:: getMaterializedCropChannel()

   **Signature:** ``getMaterializedCropChannel() -> Integer``

   **Returns:** (``int``) the (1-based) channel the currently materialized crop (see `materializeDisplayCanvas(BoundingBox)`) was actually read from, or `null` if no crop is active, or if the crop is genuinely multichannel - in that case every one of its channels is resident, so there is no single "the channel it came from" to report, and callers should instead treat it like any other resident multichannel image with no restriction.

.. method:: getMaterializedCropFrame()

   **Signature:** ``getMaterializedCropFrame() -> Integer``

   **Returns:** (``int``) the (1-based) frame the currently materialized crop (see `materializeDisplayCanvas(BoundingBox)`) as actually read from, or `null` if no crop is active. A materialized crop is always single-frame regardless of how many channels it captures (see `SNT.MaterializedCrop.frame()` - a single int, set by `installMaterializedCropOnEDT()`), so this stays meaningful even for a multichannel crop, where `getMaterializedCropChannel()` returns `null`. Callers that only care about frame should use this rather than falling back to `getFrame()` (reset to 1 by any materialized crop, single- or multichannel, regardless of its true source frame) when `getMaterializedCropChannel()` is null.

.. method:: getMaterializedCropWorldBounds()

   **Signature:** ``getMaterializedCropWorldBounds() -> BoundingBox``

   **Returns:** (``BoundingBox``) the world-space (calibrated) extent of the currently materialized crop (see `materializeDisplayCanvas(BoundingBox)`), or `null` if none is active. Useful for callers (e.g. `SkeletonizerCmd`) that want to restrict an operation to the region actually materialized, since BDV/BVV have no ROI equivalent. Derived from `getActiveCanvasPixelOffset()` and the live `width`/`height`/`depth` (the crop's own small dimensions while materialized - see `getFullImageDimensions()`): since 
```
voxelIndex =
         world/spacing + canvasOffset
```
 (see `defaultCanvasPixelOffset()`), the crop's local voxel 0 and voxel `width`/`height`/`depth` map back to world coordinates via 
```
world =
         (voxelIndex - canvasOffset) * spacing
```
 - `getWorldOriginOffset()` cancels out of that algebra, so it does not need to be looked up separately here.

.. method:: getMinimumSeparation()

   **Signature:** ``getMinimumSeparation() -> double``

   **Returns:** ``float``

.. method:: getNodeEditor()

   Returns the node editor shared by all front-ends of this instance (tracing canvas, Bdv and Bvv). It holds the path being edited, its active node and the undo history of 'Edit Mode'.

   **Signature:** ``getNodeEditor() -> PathNodeEditor``

   **Returns:** (``Any``) the node editor

.. method:: getPathAndFillManager()

   **Signature:** ``getPathAndFillManager() -> PathAndFillManager``

   **Returns:** ``PathAndFillManager``

.. method:: getPixelDepth()

   **Signature:** ``getPixelDepth() -> double``

   **Returns:** ``float``

.. method:: getPixelHeight()

   **Signature:** ``getPixelHeight() -> double``

   **Returns:** ``float``

.. method:: getPixelWidth()

   **Signature:** ``getPixelWidth() -> double``

   **Returns:** ``float``

.. method:: getPrefs()

   **Signature:** ``getPrefs() -> SNTPrefs``

   **Returns:** ``SNTPrefs``

.. method:: getSearchImageType()

   **Signature:** ``getSearchImageType() -> SearchImageType``

   **Returns:** ``Any``

.. method:: getSearchType()

   **Signature:** ``getSearchType() -> SearchType``

   **Returns:** ``Any``

.. method:: getSecondaryData()

   **Signature:** ``getSecondaryData() -> RandomAccessibleInterval``

   **Returns:** ``Any``

.. method:: getSecondaryDataAsImp()

   Retrieves the 'secondary image' data currently loaded in memory as an ImagePlus object. Returned image is always of 32-bit type.

   **Signature:** ``getSecondaryDataAsImp() -> ImagePlus``

   **Returns:** (``Any``) the loaded data or null if no image has been loaded.

.. method:: getSecondaryImageMinMax()

   **Signature:** ``getSecondaryImageMinMax() -> double[]``

   **Returns:** ``List[float]``

.. method:: getSeedOverlay()

   Returns the `SeedOverlay` associated with this SNT instance. The overlay holds candidate `SeedPoint`s (e.g., output of upstream point detectors) and is rendered on the tracing canvas when non-empty.

The overlay is **transient**: it is automatically cleared when the active image changes (see `initialize(ImagePlus)`) and is not persisted with the `.traces` file. Importers should use `SeedOverlay.addAll(java.util.Collection)` for bulk loads.

   **Signature:** ``getSeedOverlay() -> SeedOverlay``

   **Returns:** (``SeedOverlay``) the seed overlay (never `null`)

.. method:: getSelectedPaths()

   **Signature:** ``getSelectedPaths() -> Collection``

   **Returns:** ``List[Any]``

.. method:: getSinglePane()

   **Signature:** ``getSinglePane() -> boolean``

   **Returns:** ``bool``

.. method:: getSingleSelectedPath()

   **Signature:** ``getSingleSelectedPath() -> Path``

   **Returns:** ``Path``

.. method:: getSpacingUnits()

   **Signature:** ``getSpacingUnits() -> String``

   **Returns:** ``str``

.. method:: getStats()

   **Signature:** ``getStats() -> ImageStatistics``

   **Returns:** ``Any``

.. method:: getStatsSecondary()

   **Signature:** ``getStatsSecondary() -> ImageStatistics``

   **Returns:** ``Any``

.. method:: getUI()

   Gets the main UI.

   **Signature:** ``getUI() -> SNTUI``

   **Returns:** (``SNTUI``) the main dialog of SNT's UI

.. method:: getUseSubVolumeStats()

   **Signature:** ``getUseSubVolumeStats() -> boolean``

   **Returns:** ``bool``

.. method:: getWidth()

   **Signature:** ``getWidth() -> int``

   **Returns:** ``int``

.. method:: getWorldOriginOffset()

   **Signature:** ``getWorldOriginOffset() -> double[]``

   **Returns:** (``List[float]``) the world-space origin offset (calibrated units) previously set via `setWorldOriginOffset(double, double, double)`, as `{xOffset, yOffset, zOffset}`. All-zero (the default) unless explicitly set. See `setWorldOriginOffset(double, double, double)` for why this is distinct from `ij.measure.Calibration`'s own `xOrigin/yOrigin/zOrigin` fields.

.. method:: getZYXZ(xy, frame)

   **Signature:** ``getZYXZ(ImagePlus, int) -> ImagePlus[]``

   **Parameters:**

   * **xy** (``Any``)
   * **frame** (``int``)

   **Returns:** ``List[Any]``

.. method:: isAstarEnabled()

   Checks if A* search is enabled

   **Signature:** ``isAstarEnabled() -> boolean``

   **Returns:** (``bool``) true, if A* search is enabled, otherwise false

.. method:: isEditModeEnabled()

   **Signature:** ``isEditModeEnabled() -> boolean``

   **Returns:** (``bool``) true if 'Edit Mode' is currently enabled, i.e., the path returned by `getEditingPath()` is being edited on all front-ends

.. method:: isMaterializedCrop()

   **Signature:** ``isMaterializedCrop() -> boolean``

   **Returns:** (``bool``) true if this stream session's own XY canvas is currently a materialized crop (see `materializeDisplayCanvas(BoundingBox)`), i.e. `ctSlice3d` holds the crop's own (small) pixel data rather than the full Stream-mode source. Checked by `AbstractBigViewer`'s click-tracer to refuse tracing against stale pixel data while its own rendering still shows the full (unaffected) volume, and by pixel-scoped commands to warn that they will run against the crop's bounds only.

.. method:: isOnlySelectedPathsVisible()

   **Signature:** ``isOnlySelectedPathsVisible() -> boolean``

   **Returns:** ``bool``

.. method:: isSecondaryDataAvailable()

   Assesses if the 'secondary image' has been loaded into memory. Note that while some tracer Threads will load the image into memory, others may waive the loading to third party libraries

   **Signature:** ``isSecondaryDataAvailable() -> boolean``

   **Returns:** (``bool``) true, if image has been loaded into memory.

.. method:: isShowOnlyActiveCTposPaths()

   **Signature:** ``isShowOnlyActiveCTposPaths() -> boolean``

   **Returns:** (``bool``) whether only paths matching the current channel/frame position are being displayed (classic canvas), or, for Bvv/Bdv, only paths matching the current timepoint

.. method:: isSpacingKnownFromSource()

   **Signature:** ``isSpacingKnownFromSource() -> boolean``

   **Returns:** (``bool``) true if `getCalibration()` can trust this session's own spacing fields outright (the streamed source itself reported real voxel dimensions at some point); false if it instead has to fall back to a loaded Path's own (unverifiable) calibration, or this session's hardwired 1-unit default. Used by `SNTUI` to warn before an operation that depends on this calibration being correct (e.g. materializing a region), since SNT itself cannot confirm that a loaded Path was actually traced against the currently streamed source.

.. method:: isStreamMode()

   Returns whether this session is running in stream mode ("SNT Stream"), i.e., without access to a full in-core materialized image but rather a lazily-loaded BDV/BVV-backed source (typically an OME-Zarr/N5 dataset; see `BigDataLoaderCmd`).

   **Signature:** ``isStreamMode() -> boolean``

   **Returns:** (``bool``) true if in stream mode

.. method:: isTracingActive()

   **Signature:** ``isTracingActive() -> boolean``

   **Returns:** (``bool``) whether tracing functions are currently allowed

.. method:: isTracingOnSecondaryImageActive()

   **Signature:** ``isTracingOnSecondaryImageActive() -> boolean``

   **Returns:** ``bool``

.. method:: isTracingPaused()

   **Signature:** ``isTracingPaused() -> boolean``

   **Returns:** (``bool``) whether tracing functions are currently paused (see `SNTUI.pauseTracing(boolean)`)

.. method:: isTreeIsolationActive()

   **Signature:** ``isTreeIsolationActive() -> boolean``

   **Returns:** (``bool``) whether a single tree is currently isolated for display (see `setIsolatedTreeID(int)`)

.. method:: isZoomAllPanesDisabled()

   **Signature:** ``isZoomAllPanesDisabled() -> boolean``

   **Returns:** ``bool``


SNTChart
--------

.. method:: getDefaultDirectoryForSaveAs()

   **Signature:** ``getDefaultDirectoryForSaveAs() -> File``

   **Returns:** ``str``

.. method:: getFrame()

   **Signature:** ``getFrame() -> JFrame``

   **Returns:** ``Any``

.. method:: getHistogram(table, polar)

   Builds a single-series histogram from an array of values. The number of bins is chosen automatically (Freedman-Diaconis rule).

   **Signature:** ``getHistogram(SNTTable, boolean) -> SNTChart``

   **Parameters:**

   * **table** (``SNTTable``): - the data points to histogram
   * **polar** (``bool``)

   **Returns:** (``SNTChart``) a single-series histogram chart

.. method:: getImage()

   Gets an ImagePlus representation of the chart.

Creates an ImagePlus object containing a rasterized version of the chart at default scaling (1.0x).

   **Signature:** ``getImage() -> ImagePlus``

   **Returns:** (``Any``) an ImagePlus containing the chart image

.. method:: getImages(scalingFactor)

   **Signature:** ``getImages(float) -> List``

   **Parameters:**

   * **scalingFactor** (``float``)

   **Returns:** ``List[Any]``

.. method:: getPaintScaleLegend(title, colorTable, min, max, nDecimalPlaces)

   **Signature:** ``getPaintScaleLegend(String, ColorTable, double, double, int) -> PaintScaleLegend``

   **Parameters:**

   * **title** (``str``)
   * **colorTable** (``Any``)
   * **min** (``float``)
   * **max** (``float``)
   * **nDecimalPlaces** (``int``)

   **Returns:** ``Any``

.. method:: getPolarHistogram(values, axisLabel, unit)

   Builds a single-series polar histogram from an array of values. The number of bins is chosen automatically (Freedman-Diaconis rule).

   **Signature:** ``getPolarHistogram(double[], String, String) -> SNTChart``

   **Parameters:**

   * **values** (``List[float]``): - the data points to histogram
   * **axisLabel** (``str``)
   * **unit** (``str``)

   **Returns:** (``SNTChart``) a single-series polar histogram chart

.. method:: getTitle()

   **Signature:** ``getTitle() -> String``

   **Returns:** ``str``

.. method:: isCombined()

   Checks if this chart is part of a multi-panel montage

   **Signature:** ``isCombined() -> boolean``

   **Returns:** (``bool``) true, if is combined

.. method:: isEqualized()

   Checks if the axes of the underlying XY plot are equalized.

Returns true if both X and Y axes use the same scale.

   **Signature:** ``isEqualized() -> boolean``

   **Returns:** (``bool``) true if axes are equalized, false otherwise

.. method:: isGMMDistributionVisible()

   Gets whether the GMM distribution curve is being overlaid over histogram frequencies

   **Signature:** ``isGMMDistributionVisible() -> boolean``

   **Returns:** (``bool``) true if current chart is a histogram with overlaid GMM curve

.. method:: isGridlinesVisible()

   **Signature:** ``isGridlinesVisible() -> boolean``

   **Returns:** ``bool``

.. method:: isLegendVisible()

   **Signature:** ``isLegendVisible() -> boolean``

   **Returns:** ``bool``

.. method:: isNormDistributionVisible()

   Gets whether a normal distribution curve is being overlaid over histogram frequencies

   **Signature:** ``isNormDistributionVisible() -> boolean``

   **Returns:** (``bool``) true if current chart is a histogram with overlaid normal curve

.. method:: isOutlineVisible()

   Checks if the plot outline is visible.

Returns true if the plot's border outline is currently visible.

   **Signature:** ``isOutlineVisible() -> boolean``

   **Returns:** (``bool``) true if outline is visible, false otherwise

.. method:: isQuartilesVisible()

   Gets whether quartile markers (Q1, Median, Q3) are being overlaid over histogram frequencies

   **Signature:** ``isQuartilesVisible() -> boolean``

   **Returns:** (``bool``) true if current chart is a histogram with overlaid quartile markers

.. method:: setFontSize(size)

   Sets the font size for this chart.

   **Signature:** ``setFontSize(float) -> void``

   **Parameters:**

   * **size** (``float``): - the new font size

   **Returns:** ``None``


SNTColor
--------

.. method:: getDistinctColors(nColors)

   Returns distinct colors based on Kenneth Kelly's 22 colors of maximum contrast (black and white excluded). More details on this SO discussion

   **Signature:** ``getDistinctColors(int) -> ColorRGB[]``

   **Parameters:**

   * **nColors** (``int``): - the number of colors to be retrieved

   **Returns:** (``List[Any]``) the maximum contrast colors

.. method:: getDistinctColorsAWT(nColors)

   **Signature:** ``getDistinctColorsAWT(int) -> Color[]``

   **Parameters:**

   * **nColors** (``int``)

   **Returns:** ``List[Any]``

.. method:: getDistinctColorsColorblindSafe(nColors)

   Returns distinct colors from the Okabe-Ito colorblind-safe palette, cycling through its 6 hues once `nColors` exceeds that count

   **Signature:** ``getDistinctColorsColorblindSafe(int) -> ColorRGB[]``

   **Parameters:**

   * **nColors** (``int``): - the number of colors to be retrieved

   **Returns:** (``List[Any]``) the colorblind-safe colors

.. method:: getDistinctColorsColorblindSafeAWT(nColors)

   AWT variant of `getDistinctColorsColorblindSafe(int)`

   **Signature:** ``getDistinctColorsColorblindSafeAWT(int) -> Color[]``

   **Parameters:**

   * **nColors** (``int``): - the number of colors to be retrieved

   **Returns:** (``List[Any]``) the colorblind-safe colors, as AWT colors

.. method:: getDistinctColorsHex(nColors)

   Returns distinct colors based on Kenneth Kelly's 22 colors of maximum contrast (black and white excluded) as Hex values. More details on this SO discussion

   **Signature:** ``getDistinctColorsHex(int) -> String[]``

   **Parameters:**

   * **nColors** (``int``): - the number of colors to be retrieved

   **Returns:** (``List[str]``) the maximum contrast colors as hex color strings

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isTypeDefined()

   Checks if an SWC type has been defined.

   **Signature:** ``isTypeDefined() -> boolean``

   **Returns:** (``bool``) true, if an SWC integer flag has been specified


SNTGraph
--------

.. method:: getEdgeColor(edge)

   **Signature:** ``getEdgeColor(DefaultWeightedEdge) -> ColorRGB``

   **Parameters:**

   * **edge** (``Any``)

   **Returns:** ``Any``

.. method:: getEdgeColorRGBMap()

   **Signature:** ``getEdgeColorRGBMap() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getVertexColor(vertex)

   **Signature:** ``getVertexColor(Object) -> ColorRGB``

   **Parameters:**

   * **vertex** (``Any``)

   **Returns:** ``Any``

.. method:: getVertexColorRGBMap()

   **Signature:** ``getVertexColorRGBMap() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getVertexValue(vertex)

   **Signature:** ``getVertexValue(Object) -> double``

   **Parameters:**

   * **vertex** (``Any``)

   **Returns:** ``float``

.. method:: getVertexValueMap()

   **Signature:** ``getVertexValueMap() -> Map``

   **Returns:** ``Dict[str, Any]``


SNTPoint
--------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the neuropil annotation assigned to this point

.. method:: getCoordinateOnAxis(axis)

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **axis** (``int``)

   **Returns:** (``float``) the coordinate on the specified axis

.. method:: getHemisphere()

   **Signature:** ``getHemisphere() -> char``

   **Returns:** ``str``

.. method:: getX()

   **Signature:** ``getX() -> double``

   **Returns:** (``float``) the X-coordinate of the point

.. method:: getY()

   **Signature:** ``getY() -> double``

   **Returns:** (``float``) the Y-coordinate of the point

.. method:: getZ()

   **Signature:** ``getZ() -> double``

   **Returns:** (``float``) the Z-coordinate of the point


SNTPrefs
--------

.. method:: getAutoLoadToolbarButton()

   Gets whether the SNT button is auto-installed in the IJ toolbar at Fiji startup.

   **Signature:** ``getAutoLoadToolbarButton() -> boolean``

   **Returns:** (``bool``) true if the button is loaded at startup (the default)

.. method:: getAutoSelectionOfFinishedPath()

   **Signature:** ``getAutoSelectionOfFinishedPath() -> boolean``

   **Returns:** ``bool``

.. method:: getAutosaveFile()

   **Signature:** ``getAutosaveFile() -> File``

   **Returns:** ``str``

.. method:: getBackupDir()

   Returns the backup directory, or null if workspace doesn't exist. Does NOT create directories.

   **Signature:** ``getBackupDir() -> File``

   **Returns:** ``str``

.. method:: getBigViewerPickRadius()

   **Signature:** ``getBigViewerPickRadius() -> double``

   **Returns:** (``float``) the screen-space radius (pixels) within which Bdv/Bvv interactions snap to existing paths

.. method:: getBoolean(key, defaultValue)

   Gets a boolean preference value.

   **Signature:** ``getBoolean(String, boolean) -> boolean``

   **Parameters:**

   * **key** (``str``): - the preference key
   * **defaultValue** (``bool``)

   **Returns:** (``bool``) the boolean preference value

.. method:: getBvvCacheMB()

   **Signature:** ``getBvvCacheMB() -> int``

   **Returns:** (``int``) the persisted BVV GPU tile cache size (MB). 0 means automatic

.. method:: getBvvFetchers()

   **Signature:** ``getBvvFetchers() -> int``

   **Returns:** (``int``) the persisted number of BVV tile fetcher threads. 0 means automatic

.. method:: getBvvMaxStep()

   **Signature:** ``getBvvMaxStep() -> double``

   **Returns:** (``float``) the persisted BVV maximum ray-marching step (voxels), within its limits

.. method:: getBvvRenderQuality()

   **Signature:** ``getBvvRenderQuality() -> String``

   **Returns:** (``str``) the name of the persisted BVV render quality preset, or null if none has been set

.. method:: getDefaultLookAndFeel()

   **Signature:** ``getDefaultLookAndFeel() -> String``

   **Returns:** ``str``

.. method:: getDisplayCustomPathColors()

   **Signature:** ``getDisplayCustomPathColors() -> boolean``

   **Returns:** ``bool``

.. method:: getLookAndFeel()

   Gets the current look and feel preference.

   **Signature:** ``getLookAndFeel() -> String``

   **Returns:** (``str``) the look and feel class name

.. method:: getNextImgExtensions()

   Returns the list of filename suffixes used to identify images when navigating to the next/previous image in a folder (see `SNTUI`). Matching is case-insensitive and applied to the end of the filename (i.e., `endsWith`). Suffixes may include a leading dot (e.g., `".tif"`) or a partial filename suffix (e.g., `"_max.tif"`).

   **Signature:** ``getNextImgExtensions() -> List``

   **Returns:** (``List[Any]``) a non-null, non-empty list of suffixes; defaults to `[".tif", ".tiff"]` if no preference has been set

.. method:: getPref(key)

   **Signature:** ``getPref(int) -> boolean``

   **Parameters:**

   * **key** (``int``)

   **Returns:** ``bool``

.. method:: getRecentDir()

   **Signature:** ``getRecentDir() -> File``

   **Returns:** ``str``

.. method:: getRequireShiftToFork()

   **Signature:** ``getRequireShiftToFork() -> boolean``

   **Returns:** ``bool``

.. method:: getSessionsDir()

   Returns the sessions directory, or null if workspace doesn't exist. Does NOT create directories.

   **Signature:** ``getSessionsDir() -> File``

   **Returns:** ``str``

.. method:: getTemp(key, defaultValue)

   Gets a temporary string preference value that will be cleared at session end.

   **Signature:** ``getTemp(String, String) -> String``

   **Parameters:**

   * **key** (``str``): - the preference key
   * **defaultValue** (``str``)

   **Returns:** (``str``) the string preference value

.. method:: getThreads()

   Gets the current number of threads setting.

   **Signature:** ``getThreads() -> int``

   **Returns:** (``int``) the number of threads

.. method:: getUseNativeFileChooser()

   Gets whether SNT's open/save dialogs should use the OS native file dialogs (FlatLaf's `SystemFileChooser`) instead of SNT's own `FileChooser`.

   **Signature:** ``getUseNativeFileChooser() -> boolean``

   **Returns:** (``bool``) true if native OS file dialogs should be used when possible

.. method:: getWorkspaceDir()

   **Signature:** ``getWorkspaceDir() -> File``

   **Returns:** ``str``

.. method:: isBvvCachePromptSuppressed()

   **Signature:** ``isBvvCachePromptSuppressed() -> boolean``

   **Returns:** (``bool``) whether the user opted out of BVV's GPU tile cache prompt

.. method:: isCanvasAutoActivationEnabled()

   **Signature:** ``isCanvasAutoActivationEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isFastCropMaterializationEnabled()

   **Signature:** ``isFastCropMaterializationEnabled() -> boolean``

   **Returns:** (``bool``) whether `SNT.buildMaterializedCrop(sc.fiji.snt.util.BoundingBox)` should attempt the faster, single-copy 
```
ImgUtils.raiToImpFast(net.imglib2.RandomAccessibleInterval<T>, java.lang.String)
```
 path before falling back to `ImgUtils.raiToImp(net.imglib2.RandomAccessibleInterval<T>, java.lang.String)`+`ImagePlus.duplicate()`. Default: `true`.

.. method:: isSaveCompressedTraces()

   Checks if traces should be saved in compressed format.

   **Signature:** ``isSaveCompressedTraces() -> boolean``

   **Returns:** (``bool``) true if compressed traces are enabled, false otherwise

.. method:: isSaveWinLocations()

   Checks if window locations should be saved and restored.

   **Signature:** ``isSaveWinLocations() -> boolean``

   **Returns:** (``bool``) true if window locations are saved, false otherwise

.. method:: isScrollDiameterEnabled()

   **Signature:** ``isScrollDiameterEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isSomaDisplayTriangle()

   Sets whether single-node paths tagged as are rendered w/ triangular shape.

   **Signature:** ``isSomaDisplayTriangle() -> boolean``

   **Returns:** (``bool``) true if triangular shape is enable, false otherwise


SNTService
----------

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getInstance()

   Returns a reference to the active `SNT` instance.

   **Signature:** ``getInstance() -> SNT``

   **Returns:** (``SNT``) the `SNT` instance

.. method:: getOrCreateSciViewSNT()

   **Signature:** ``getOrCreateSciViewSNT() -> SciViewSNT``

   **Returns:** ``Any``

.. method:: getPathAndFillManager()

   Returns the `PathAndFillManager` associated with the current SNT instance.

   **Signature:** ``getPathAndFillManager() -> PathAndFillManager``

   **Returns:** (``PathAndFillManager``) the PathAndFillManager instance

.. method:: getPaths()

   Gets the paths currently listed in the Path Manager

   **Signature:** ``getPaths() -> List``

   **Returns:** (``List[Any]``) all the listed paths, or null if the Path Manager is empty

.. method:: getRecViewer()

   Returns a reference to an opened Reconstruction Viewer (standalone instance). *

   **Signature:** ``getRecViewer() -> Viewer3D``

   **Returns:** ``Viewer3D``

.. method:: getSciViewSNT()

   **Signature:** ``getSciViewSNT() -> SciViewSNT``

   **Returns:** ``Any``

.. method:: getSelectedPaths()

   Gets the paths currently selected in the Path Manager list.

   **Signature:** ``getSelectedPaths() -> Collection``

   **Returns:** (``List[Any]``) the paths currently selected, or null if no selection exists

.. method:: getStatistics(selectedPathsOnly)

   Returns a `TreeStatistics` instance constructed from current Paths.

   **Signature:** ``getStatistics(boolean) -> TreeStatistics``

   **Parameters:**

   * **selectedPathsOnly** (``bool``): - If true only selected paths will be considered

   **Returns:** (``TreeStatistics``) the TreeStatistics instance

.. method:: getTable()

   Returns a reference to SNT's main table of measurements.

   **Signature:** ``getTable() -> SNTTable``

   **Returns:** (``SNTTable``) SNT measurements table (a `DefaultGenericTable`)

.. method:: getTree()

   Gets the collection of paths listed in the Path Manager as a `Tree` object.

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the Tree holding the Path collection

.. method:: getTrees()

   Gets the collection of paths listed in the Path Manager as a `Tree` object.

   **Signature:** ``getTrees() -> Collection``

   **Returns:** (``List[Any]``) the Tree holding the Path collection

.. method:: getUI()

   Returns a reference to SNT's UI.

   **Signature:** ``getUI() -> SNTUI``

   **Returns:** (``SNTUI``) the `SNTUI` window, or null if SNT is not running, or is running without GUI

.. method:: hasUnsavedPaths()

   Checks whether SNT holds paths that have not been saved.

   **Signature:** ``hasUnsavedPaths() -> boolean``

   **Returns:** (``bool``) true if SNT is running and has unsaved paths

.. method:: isActive()

   Gets whether SNT is running.

   **Signature:** ``isActive() -> boolean``

   **Returns:** (``bool``) true if this `SNTService` is active, tied to the active instance of SNT

.. method:: isStreamMode()

   Gets whether SNT is currently running in Stream mode ("SNT Stream"), i.e., tethered to a streamed dataset (N5/OME-Zarr/IMS/BDV-XML) via the Big Data Loader, with no in-core `ImagePlus`/classic canvas available. Several script-facing APIs (ImagePlus-based snapshots, ROI-based inputs, `SNT#rebuildDisplayCanvases()`, etc.) are not available in this mode. Scripts can use this method to detect that and abort/adapt early.

   **Signature:** ``isStreamMode() -> boolean``

   **Returns:** (``bool``) true if SNT is active and running in Stream mode; false otherwise (including when SNT is not running, or is running without a GUI)


SNTTable
--------

.. method:: getColumnHeaders()

   **Signature:** ``getColumnHeaders() -> List``

   **Returns:** ``List[Any]``

.. method:: getSummaryRow()

   **Signature:** ``getSummaryRow() -> int``

   **Returns:** ``int``

.. method:: getTitle()

   Gets the title of the table.

Returns the table's title, or "SNT Measurements" if no title has been set.

   **Signature:** ``getTitle() -> String``

   **Returns:** (``str``) the table title

.. method:: hasUnsavedData()

   Checks if the table has unsaved data.

Returns true if the table contains data and has been modified since the last save operation.

   **Signature:** ``hasUnsavedData() -> boolean``

   **Returns:** (``bool``) true if there is unsaved data, false otherwise

.. method:: isSummarized()

   Checks if the table contains summary statistics.

Returns true if the table has been summarized with statistical measures like mean, standard deviation, etc. This is determined by looking for specific row headers in the expected positions.

   **Signature:** ``isSummarized() -> boolean``

   **Returns:** (``bool``) true if table contains summary statistics, false otherwise


SNTUI
-----

.. method:: getActiveBigViewer()

   Returns the `AbstractBigViewer` (BVV or BDV) currently tethered to this UI, in particular, Stream mode's own viewer or `null` if neither is open.

   **Signature:** ``getActiveBigViewer() -> AbstractBigViewer``

   **Returns:** ``Any``

.. method:: getBookmarkManager()

   Gets the Bookmark Manager pane.

   **Signature:** ``getBookmarkManager() -> BookmarkManager``

   **Returns:** (``BookmarkManager``) the `BookmarkManager` associated with this UI

.. method:: getCommandFinder()

   Returns the command palette instance, so that other components can register their own entries into it.

   **Signature:** ``getCommandFinder() -> SNTCommandFinder``

   **Returns:** ``Any``

.. method:: getCurationManager()

   Returns the Curation Manager (Curation Assistant).

   **Signature:** ``getCurationManager() -> CurationManager``

   **Returns:** ``CurationManager``

.. method:: getDelineationsManager()

   Gets the Delineations Manager pane.

   **Signature:** ``getDelineationsManager() -> DelineationsManager``

   **Returns:** (``DelineationsManager``) the `DelineationsManager` associated with this UI

.. method:: getFillManager()

   Gets the Fill Manager dialog.

   **Signature:** ``getFillManager() -> FillManagerUI``

   **Returns:** (``FillManagerUI``) the `FillManagerUI` associated with this UI

.. method:: getNotesPane()

   Gets the Bookmark Manager pane.

   **Signature:** ``getNotesPane() -> NotesUI``

   **Returns:** (``Any``) the `BookmarkManager` associated with this UI

.. method:: getOpenBigViewers()

   **Signature:** ``getOpenBigViewers() -> List``

   **Returns:** (``List[Any]``) all tethered Bvv/Bdv viewers (zero, one or two), for operations that must reach every open viewer

.. method:: getOrPromptForWorkspace()

   Returns the workspace directory, prompting user to create it if it doesn't exist.

   **Signature:** ``getOrPromptForWorkspace() -> File``

   **Returns:** (``str``) workspace directory, or null if user declined creation

.. method:: getPathManager()

   Gets the Path Manager dialog.

   **Signature:** ``getPathManager() -> PathManagerUI``

   **Returns:** (``PathManagerUI``) the `PathManagerUI` associated with this UI

.. method:: getPlausibilityMonitor()

   Returns the plausibility monitor used by the Curation Manager (Curation Assistant).

   **Signature:** ``getPlausibilityMonitor() -> PlausibilityMonitor``

   **Returns:** ``PlausibilityMonitor``

.. method:: getPrefs()

   **Signature:** ``getPrefs() -> SNTPrefs``

   **Returns:** (``SNTPrefs``) the preferences associated with this instance

.. method:: getReconstructionViewer(initializeIfNull)

   Gets the Reconstruction Viewer.

   **Signature:** ``getReconstructionViewer(boolean) -> Viewer3D``

   **Parameters:**

   * **initializeIfNull** (``bool``): - it true, initializes the Viewer if it has not yet been initialized

   **Returns:** (``Viewer3D``) the reconstruction viewer

.. method:: getRecorder(createIfNeeded)

   **Signature:** ``getRecorder(boolean) -> ScriptRecorder``

   **Parameters:**

   * **createIfNeeded** (``bool``)

   **Returns:** ``Any``

.. method:: getSciViewSNT(initializeIfNull)

   Gets the SciViewSNT instance.

   **Signature:** ``getSciViewSNT(boolean) -> SciViewSNT``

   **Parameters:**

   * **initializeIfNull** (``bool``): - whether a new instance should be created if one hasn't been initialized

   **Returns:** (``Any``) the SciViewSNT instance

.. method:: getState()

   Gets the current UI state.

   **Signature:** ``getState() -> int``

   **Returns:** (``int``) the current UI state, e.g., `READY`, `RUNNING_CMD`, etc.

.. method:: getTable()

   **Signature:** ``getTable() -> SNTTable``

   **Returns:** ``SNTTable``

.. method:: getTracingCanvas()

   **Signature:** ``getTracingCanvas() -> TracerCanvas``

   **Returns:** ``TracerCanvas``

.. method:: getTracingCanvasPopupMenu()

   **Signature:** ``getTracingCanvasPopupMenu() -> JPopupMenu``

   **Returns:** ``Any``

.. method:: isOtherBigViewerEditing(viewer)

   **Signature:** ``isOtherBigViewerEditing(AbstractBigViewer) -> boolean``

   **Parameters:**

   * **viewer** (``Any``)

   **Returns:** (``bool``) whether a Bvv/Bdv other than `viewer` is still open and in Edit Mode

.. method:: isReady()

   Assesses whether the UI is blocked.

   **Signature:** ``isReady() -> boolean``

   **Returns:** (``bool``) true if the UI is currently unblocked, i.e., ready for tracing/editing/analysis *


SNTUtils
--------

.. method:: getBackupCopies(location)

   Returns all timestamped backup copies in the specified location. Convenience method that matches all traces files with timestamps.

   **Signature:** ``getBackupCopies(File) -> List``

   **Parameters:**

   * **location** (``str``): - the directory to search for backup files

   **Returns:** (``List[Any]``) list of backup files (never null, may be empty), sorted most recent first

.. method:: getCacheDir()

   Returns SNT's own scratch/cache directory, used by disk-backed operations (e.g. `DiskBackedStorageBackend`, `Lazy`). Unlike the workspace directory (see `SNTPrefs#getWorkspaceDir()`), this directory holds only disposable, regenerable scratch data -- never anything a user created -- so it lives under the OS temp root.

Individual operations create their own uniquely-named subdirectory here and clean up after themselves once done. This parent directory itself is created lazily and left in place across sessions, so that (1) it is always at the same, discoverable path and (2) leftovers from a crashed session (which skipped its own cleanup) remain visible and removable.

   **Signature:** ``getCacheDir() -> File``

   **Returns:** (``str``) SNT's cache directory (created if it did not already exist), or, if that path could not be created/written to (e.g. permissions, a network-mounted or read-only temp location, a stray file already occupying that path), a fallback directory under the user's home folder. Callers relying on this directory for disk-backed caching should still be prepared for `IOException`s down the line (e.g. if the disk is full).

.. method:: getCacheDirSize()

   Computes the on-disk size of `getCacheDir()`. This walks the whole cache tree, so it can be slow once many files have accumulated; avoid calling this on the EDT

   **Signature:** ``getCacheDirSize() -> long``

   **Returns:** (``int``) the cache directory's size in bytes, or 0 if it could not be read

.. method:: getContext()

   Convenience method to access the context of the running Fiji instance

   **Signature:** ``getContext() -> Context``

   **Returns:** (``Any``) the context of the active ImageJ instance. Never null

.. method:: getDecimalFormat(value, digits)

   **Signature:** ``getDecimalFormat(double, int) -> DecimalFormat``

   **Parameters:**

   * **value** (``float``)
   * **digits** (``int``)

   **Returns:** ``Any``

.. method:: getElapsedTime(fromStart)

   **Signature:** ``getElapsedTime(long) -> String``

   **Parameters:**

   * **fromStart** (``int``)

   **Returns:** ``str``

.. method:: getHeapInfo()

   **Signature:** ``getHeapInfo() -> HeapInfo``

   **Returns:** (``Any``) a snapshot of current JVM heap usage

.. method:: getInstance()

   **Signature:** ``getInstance() -> SNT``

   **Returns:** ``SNT``

.. method:: getLastElement(filePathOrUrlOrCloudLink)

   Extracts the last path/URL element (typically a filename) from a file path, URL, or cloud-storage link, e.g., `"/data/sample.n5"` or `"https://host/a/b.zarr?x=1"` both yield `"b.zarr"`/`"sample.n5"`. Handles Windows-style backslashes, trailing slashes, and URL query parameters/anchors.

   **Signature:** ``getLastElement(String) -> String``

   **Parameters:**

   * **filePathOrUrlOrCloudLink** (``str``): - the path/URL/link to parse

   **Returns:** (``str``) the last element, or an empty string if `filePathOrUrlOrCloudLink` is null or blank

.. method:: getReadableVersion()

   **Signature:** ``getReadableVersion() -> String``

   **Returns:** ``str``

.. method:: getReconstructionFiles(dir, pattern)

   Retrieves a list of reconstruction files stored in a common directory matching the specified criteria.

   **Signature:** ``getReconstructionFiles(File, String) -> File[]``

   **Parameters:**

   * **dir** (``str``): - the directory containing the reconstruction files (.(e)swc, .traces, .json extension)
   * **pattern** (``str``)

   **Returns:** (``List[str]``) the array of files. An empty list is retrieved if `dir` is not a valid, readable directory.

.. method:: getSanitizedUnit(unit)

   **Signature:** ``getSanitizedUnit(String) -> String``

   **Parameters:**

   * **unit** (``str``)

   **Returns:** ``str``

.. method:: getTimeStamp()

   **Signature:** ``getTimeStamp() -> String``

   **Returns:** ``str``

.. method:: getUniquelySuffixedFile(referenceFile)

   **Signature:** ``getUniquelySuffixedFile(File) -> File``

   **Parameters:**

   * **referenceFile** (``str``)

   **Returns:** ``str``

.. method:: getUniquelySuffixedTifFile(referenceFile)

   **Signature:** ``getUniquelySuffixedTifFile(File) -> File``

   **Parameters:**

   * **referenceFile** (``str``)

   **Returns:** ``str``

.. method:: isContextSet()

   **Signature:** ``isContextSet() -> boolean``

   **Returns:** ``bool``

.. method:: isDebugMode()

   Assesses if SNT is running in debug mode

   **Signature:** ``isDebugMode() -> boolean``

   **Returns:** (``bool``) the debug flag

.. method:: isReachable(url, timeoutMs)

   Checks for whether `url`'s host can be reached, meant to be called before a real download/stream attempt (e.g., `downloadToTempFile(java.lang.String)`) so that a missing network connection surfaces as one clear message. est-effort: only http(s) URLs are actually probed; any other scheme (e.g. a bare host-less URI) is assumed reachable, deferring to the real caller

   **Signature:** ``isReachable(String, int) -> boolean``

   **Parameters:**

   * **url** (``str``): - the URL to check
   * **timeoutMs** (``int``)

   **Returns:** (``bool``) true if the host could be reached (or `url` is not a plain http(s) URL); false if a connection could not be established within `timeoutMs`

.. method:: isReconstructionFile(file)

   Checks if a file is a reconstruction file, optionally inspecting the header of .xml files (Neurolucida).

   **Signature:** ``isReconstructionFile(File) -> boolean``

   **Parameters:**

   * **file** (``str``): - the file to be tested

   **Returns:** (``bool``) true if the file is a supported reconstruction file

.. method:: isStandaloneContext()

   Returns whether the current context was self-initialized by SNT (i.e., no host application like ImageJ/Fiji provided one). This is useful for determining if it is safe to modify global UI state such as the Look and Feel.

   **Signature:** ``isStandaloneContext() -> boolean``

   **Returns:** (``bool``) true if the context was created by SNT itself, false if provided externally


SWCPoint
--------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the neuropil annotation assigned to this point

.. method:: getColor()

   Gets the color of this point.

   **Signature:** ``getColor() -> Color``

   **Returns:** (``Any``) the color

.. method:: getCoordinateOnAxis(axis)

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **axis** (``int``)

   **Returns:** ``float``

.. method:: getHemisphere()

   **Signature:** ``getHemisphere() -> char``

   **Returns:** ``str``

.. method:: getNextPoints()

   Returns the list holding the subsequent nodes in the reconstructed structure after this one.

   **Signature:** ``getNextPoints() -> List``

   **Returns:** (``List[Any]``) the list of "next points"

.. method:: getPath()

   **Signature:** ``getPath() -> Path``

   **Returns:** ``Path``

.. method:: getTags()

   Gets the tags associated with this point.

   **Signature:** ``getTags() -> String``

   **Returns:** (``str``) the tags string

.. method:: getUnscaledPoint()

   **Signature:** ``getUnscaledPoint() -> PointInCanvas``

   **Returns:** ``Any``

.. method:: getX()

   **Signature:** ``getX() -> double``

   **Returns:** (``float``) the X-coordinate of the point

.. method:: getY()

   **Signature:** ``getY() -> double``

   **Returns:** (``float``) the Y-coordinate of the point

.. method:: getZ()

   **Signature:** ``getZ() -> double``

   **Returns:** (``float``) the Z-coordinate of the point

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isReal()

   **Signature:** ``isReal() -> boolean``

   **Returns:** ``bool``

.. method:: isSameLocation(pim)

   **Signature:** ``isSameLocation(PointInImage) -> boolean``

   **Parameters:**

   * **pim** (``PointInImage``)

   **Returns:** ``bool``


SearchImageStack
----------------

.. method:: getSlice(z)

   **Signature:** ``getSlice(int) -> SearchImage``

   **Parameters:**

   * **z** (``int``)

   **Returns:** ``Any``

.. method:: size()

   **Signature:** ``size() -> int``

   **Returns:** ``int``


SearchNode
----------

.. method:: getX()

   **Signature:** ``getX() -> int``

   **Returns:** ``int``

.. method:: getY()

   **Signature:** ``getY() -> int``

   **Returns:** ``int``

.. method:: getZ()

   **Signature:** ``getZ() -> int``

   **Returns:** ``int``


SearchThread
------------

.. method:: getExitReason()

   **Signature:** ``getExitReason() -> int``

   **Returns:** ``int``

.. method:: getNodesAsImageFromGoal()

   **Signature:** ``getNodesAsImageFromGoal() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getNodesAsImageFromStart()

   **Signature:** ``getNodesAsImageFromStart() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``


SearchThreadArtist
------------------

.. method:: getSearch()

   **Signature:** ``getSearch() -> SearchInterface``

   **Returns:** ``Any``


SeedOverlay
-----------

.. method:: getColorMode()

   **Signature:** ``getColorMode() -> ColorMode``

   **Returns:** ``Any``

.. method:: getColorTable()

   **Signature:** ``getColorTable() -> ColorTable``

   **Returns:** ``Any``

.. method:: getColorTableName()

   **Signature:** ``getColorTableName() -> String``

   **Returns:** ``str``

.. method:: getHighConfidence()

   **Signature:** ``getHighConfidence() -> double``

   **Returns:** ``float``

.. method:: getLowConfidence()

   **Signature:** ``getLowConfidence() -> double``

   **Returns:** ``float``

.. method:: getSelectedSeeds()

   **Signature:** ``getSelectedSeeds() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getTransparency()

   **Signature:** ``getTransparency() -> double``

   **Returns:** ``float``

.. method:: getUnknownConfidenceColor()

   **Signature:** ``getUnknownConfidenceColor() -> Color``

   **Returns:** ``Any``

.. method:: isEmpty()

   **Signature:** ``isEmpty() -> boolean``

   **Returns:** ``bool``

.. method:: isSelected(seed)

   **Signature:** ``isSelected(SeedPoint) -> boolean``

   **Parameters:**

   * **seed** (``SeedPoint``)

   **Returns:** ``bool``

.. method:: isVisible()

   **Signature:** ``isVisible() -> boolean``

   **Returns:** ``bool``

.. method:: size()

   **Signature:** ``size() -> int``

   **Returns:** ``int``

.. method:: visibleSize()

   **Signature:** ``visibleSize() -> int``

   **Returns:** ``int``


SeedPoint
---------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** ``Any``

.. method:: getCoordinateOnAxis(axis)

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **axis** (``int``)

   **Returns:** ``float``

.. method:: getHemisphere()

   **Signature:** ``getHemisphere() -> char``

   **Returns:** ``str``

.. method:: getX()

   **Signature:** ``getX() -> double``

   **Returns:** ``float``

.. method:: getY()

   **Signature:** ``getY() -> double``

   **Returns:** ``float``

.. method:: getZ()

   **Signature:** ``getZ() -> double``

   **Returns:** ``float``


ShollAnalyzer
-------------

.. method:: getLinearStats()

   Gets the `LinearProfileStats` associated with this analyzer. By default, it is set to determine the polynomial of 'best-fit' (2-20 degree range.)

   **Signature:** ``getLinearStats() -> LinearProfileStats``

   **Returns:** (``LinearProfileStats``) the LinearProfileStats instance

.. method:: getMaximaRadii()

   **Signature:** ``getMaximaRadii() -> ArrayList``

   **Returns:** ``List[Any]``

.. method:: getMetrics()

   **Signature:** ``getMetrics() -> List``

   **Returns:** ``List[Any]``

.. method:: getNormStats()

   Gets the `NormalizedProfileStats` associated with this analyzer. By default it is set to determine the regression method of 'best-fit' (log-log or semi-log) using shell volume as normalizer (if Tree has a depth component) or shell area if Tree is 2D.

   **Signature:** ``getNormStats() -> NormalizedProfileStats``

   **Returns:** (``NormalizedProfileStats``) the LinearProfileStats instance

.. method:: getSecondaryMaxima()

   **Signature:** ``getSecondaryMaxima() -> ArrayList``

   **Returns:** ``List[Any]``

.. method:: getSingleValueMetrics()

   **Signature:** ``getSingleValueMetrics() -> Map``

   **Returns:** ``Dict[str, Any]``


ShollOverlay
------------

.. method:: getLUTs()

   **Signature:** ``getLUTs() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getOverlay()

   **Signature:** ``getOverlay() -> Overlay``

   **Returns:** ``Any``

.. method:: setPointsSize(size)

   **Signature:** ``setPointsSize(String) -> void``

   **Parameters:**

   * **size** (``str``)

   **Returns:** ``None``


ShollPlot
---------

.. method:: getStats()

   **Signature:** ``getStats() -> ShollStats``

   **Returns:** ``ShollStats``

.. method:: isUsingCumulativeFrequencies()

   **Signature:** ``isUsingCumulativeFrequencies() -> boolean``

   **Returns:** ``bool``

.. method:: isVisible()

   **Signature:** ``isVisible() -> boolean``

   **Returns:** ``bool``


ShollStats
----------

.. method:: getDataMode()

   **Signature:** ``getDataMode() -> DataMode``

   **Returns:** ``Any``

.. method:: getFitYValues()

   **Signature:** ``getFitYValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getN()

   **Signature:** ``getN() -> int``

   **Returns:** ``int``

.. method:: getProfile()

   **Signature:** ``getProfile() -> Profile``

   **Returns:** ``Profile``

.. method:: getXValues()

   **Signature:** ``getXValues() -> double[]``

   **Returns:** ``List[float]``

.. method:: getYValues()

   **Signature:** ``getYValues() -> double[]``

   **Returns:** ``List[float]``


ShollTable
----------

.. method:: getColumnHeaders()

   **Signature:** ``getColumnHeaders() -> List``

   **Returns:** ``List[Any]``

.. method:: getSummaryRow()

   **Signature:** ``getSummaryRow() -> int``

   **Returns:** ``int``

.. method:: getTitle()

   **Signature:** ``getTitle() -> String``

   **Returns:** ``str``

.. method:: hasContext()

   **Signature:** ``hasContext() -> boolean``

   **Returns:** ``bool``

.. method:: hasUnsavedData()

   **Signature:** ``hasUnsavedData() -> boolean``

   **Returns:** ``bool``

.. method:: isSummarized()

   **Signature:** ``isSummarized() -> boolean``

   **Returns:** ``bool``


SparseGWDTTracer
----------------

.. method:: getCaliperFraction()

   **Signature:** ``getCaliperFraction() -> double``

   **Returns:** ``float``

.. method:: getMaxGapVoxels()

   **Signature:** ``getMaxGapVoxels() -> int``

   **Returns:** ``int``

.. method:: getMinSomaDistance()

   **Signature:** ``getMinSomaDistance() -> double``

   **Returns:** ``float``

.. method:: getNSomas()

   **Signature:** ``getNSomas() -> int``

   **Returns:** ``int``

.. method:: getRootStrategy()

   **Signature:** ``getRootStrategy() -> int``

   **Returns:** ``int``

.. method:: getScoreMap()

   **Signature:** ``getScoreMap() -> RandomAccessibleInterval``

   **Returns:** ``Any``

.. method:: getSomaRoi()

   **Signature:** ``getSomaRoi() -> Roi``

   **Returns:** ``Any``

.. method:: getTipExtensionDistance()

   **Signature:** ``getTipExtensionDistance() -> double``

   **Returns:** ``float``

.. method:: getTracedRegionBuffer()

   **Signature:** ``getTracedRegionBuffer() -> int``

   **Returns:** ``int``

.. method:: isAllowVoxelGap()

   **Signature:** ``isAllowVoxelGap() -> boolean``

   **Returns:** ``bool``

.. method:: isAutoFilter()

   **Signature:** ``isAutoFilter() -> boolean``

   **Returns:** ``bool``

.. method:: isParallelBranchPruneEnabled()

   **Signature:** ``isParallelBranchPruneEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isPathFittingEnabled()

   **Signature:** ``isPathFittingEnabled() -> boolean``

   **Returns:** ``bool``

.. method:: isVerbose()

   **Signature:** ``isVerbose() -> boolean``

   **Returns:** ``bool``

.. method:: setMinBranchIntensityLength(threshold)

   **Signature:** ``setMinBranchIntensityLength(double) -> void``

   **Parameters:**

   * **threshold** (``float``)

   **Returns:** ``None``

.. method:: setMinSegmentLength(lengthInPhysicalUnits)

   **Signature:** ``setMinSegmentLength(double) -> void``

   **Parameters:**

   * **lengthInPhysicalUnits** (``float``)

   **Returns:** ``None``

.. method:: setSmoothWindowSize(windowSize)

   **Signature:** ``setSmoothWindowSize(int) -> void``

   **Parameters:**

   * **windowSize** (``int``)

   **Returns:** ``None``


SparseStorageBackend
--------------------

.. method:: getAliveIndices()

   **Signature:** ``getAliveIndices() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getBackendType()

   **Signature:** ``getBackendType() -> String``

   **Returns:** ``str``

.. method:: getDistance(index)

   **Signature:** ``getDistance(long) -> double``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``float``

.. method:: getGWDT(index)

   **Signature:** ``getGWDT(long) -> double``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``float``

.. method:: getMaxGWDT()

   **Signature:** ``getMaxGWDT() -> double``

   **Returns:** ``float``

.. method:: getParent(index)

   **Signature:** ``getParent(long) -> long``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``int``

.. method:: getState(index)

   **Signature:** ``getState(long) -> byte``

   **Parameters:**

   * **index** (``int``)

   **Returns:** ``int``


SpectralSimilarity
------------------

.. method:: getReferenceColor()

   Returns the reference color vector used by this filter.

   **Signature:** ``getReferenceColor() -> double[]``

   **Returns:** (``List[float]``) a copy of the reference color array


StrahlerAnalyzer
----------------

.. method:: getAvgBifurcationRatio()

   **Signature:** ``getAvgBifurcationRatio() -> double``

   **Returns:** (``float``) the average `bifurcation ratio` of the parsed tree. In a complete binary tree, the bifurcation ratio is 2.

.. method:: getAvgContractions()

   **Signature:** ``getAvgContractions() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getAvgExtensionAngle(relative, order)

   Gets the average relative extension angle for branches of a specific Strahler order.

   **Signature:** ``getAvgExtensionAngle(boolean, int) -> double``

   **Parameters:**

   * **relative** (``bool``): - the Strahler order
   * **order** (``int``)

   **Returns:** (``float``) the average relative extension angle in degrees, or Double.NaN if no valid angles

.. method:: getAvgExtensionAngles(relative)

   Gets a map of average relative extension angles for all Strahler orders.

   **Signature:** ``getAvgExtensionAngles(boolean) -> Map``

   **Parameters:**

   * **relative** (``bool``)

   **Returns:** (``Dict[str, Any]``) map with Strahler order as key and average relative extension angle as value

.. method:: getAvgFragmentations()

   **Signature:** ``getAvgFragmentations() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getBifurcationRatios()

   **Signature:** ``getBifurcationRatios() -> Map``

   **Returns:** (``Dict[str, Any]``) the map containing the bifurcation ratios obtained as the ratio of no. of branches between consecutive orders (Horton-Strahler numbers as key and ratios as value).

.. method:: getBranchCounts()

   **Signature:** ``getBranchCounts() -> Map``

   **Returns:** (``Dict[str, Any]``) the map containing the number of branches on each order (Horton-Strahler numbers as key and branch count as value).

.. method:: getBranchPointCounts()

   **Signature:** ``getBranchPointCounts() -> Map``

   **Returns:** (``Dict[str, Any]``) the map containing the number of branch points on each order (Horton-Strahler numbers as key and branch points count as value).

.. method:: getBranches()

   **Signature:** ``getBranches() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getExtensionAngles(relative)

   Gets a map of relative extension angles for all branches in each Strahler order.

   **Signature:** ``getExtensionAngles(boolean) -> Map``

   **Parameters:**

   * **relative** (``bool``)

   **Returns:** (``Dict[str, Any]``) map with Strahler order as key and list of relative extension angles as values

.. method:: getGraph()

   **Signature:** ``getGraph() -> DirectedWeightedGraph``

   **Returns:** (``DirectedWeightedGraph``) the graph of the tree being parsed.

.. method:: getHighestBranchOrder()

   **Signature:** ``getHighestBranchOrder() -> int``

   **Returns:** (``int``) the highest Horton-Strahler number associated with a branch in the parsed tree. Either `getRootNumber()` or `getRootNumber()-1`.

.. method:: getLengths()

   **Signature:** ``getLengths() -> Map``

   **Returns:** (``Dict[str, Any]``) the map containing the cable lengh associated to each order ( Horton-Strahler numbers as key and cable length as value).

.. method:: getRelativeExtensionAngle(branch)

   Computes the relative extension angle for a StrahlerAnalyzer branch by finding the parent direction from the graph structure.

   **Signature:** ``getRelativeExtensionAngle(Path) -> double``

   **Parameters:**

   * **branch** (``Path``): - the branch path to analyze

   **Returns:** (``float``) the relative extension angle in degrees (0-180°), or Double.NaN if computation fails

.. method:: getRootAssociatedBranches()

   **Signature:** ``getRootAssociatedBranches() -> List``

   **Returns:** ``List[Any]``

.. method:: getRootNumber()

   **Signature:** ``getRootNumber() -> int``

   **Returns:** (``int``) the highest Horton-Strahler number in the parsed tree.


TracerCanvas
------------

.. method:: getAnnotationsColor()

   **Signature:** ``getAnnotationsColor() -> Color``

   **Returns:** ``Any``

.. method:: getCanvasLabel()

   **Signature:** ``getCanvasLabel() -> String``

   **Returns:** ``str``

.. method:: getCursorPos()

   **Signature:** ``getCursorPos() -> PointInCanvas``

   **Returns:** ``Any``

.. method:: getEitherSide()

   **Signature:** ``getEitherSide() -> int``

   **Returns:** (``int``) the depth-band radius (in slices either side of the current slice) used when `isJustNearSlices()` is `true`.

.. method:: getGraphics2D(g)

   **Signature:** ``getGraphics2D(Graphics) -> Graphics2D``

   **Parameters:**

   * **g** (``Any``)

   **Returns:** ``Any``

.. method:: getLabelForegroundColor()

   **Signature:** ``getLabelForegroundColor() -> Color``

   **Returns:** ``Any``

.. method:: getPlane()

   Returns the MultiDThreePanes plane associated with this canvas.

   **Signature:** ``getPlane() -> int``

   **Returns:** (``int``) Either MultiDThreePanes.XY_PLANE, XZ_PLANE, or ZY_PLANE

.. method:: getViewPort()

   **Signature:** ``getViewPort() -> BoundingBox``

   **Returns:** ``BoundingBox``

.. method:: isEventsDisabled()

   **Signature:** ``isEventsDisabled() -> boolean``

   **Returns:** ``bool``

.. method:: isJustNearSlices()

   **Signature:** ``isJustNearSlices() -> boolean``

   **Returns:** (``bool``) whether per-slice depth-band rendering is currently enabled (i.e. paths only render near the active slice).


TracerThread
------------

.. method:: getExitReason()

   **Signature:** ``getExitReason() -> int``

   **Returns:** ``int``

.. method:: getNodesAsImageFromGoal()

   **Signature:** ``getNodesAsImageFromGoal() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getNodesAsImageFromStart()

   **Signature:** ``getNodesAsImageFromStart() -> SearchImageStack``

   **Returns:** ``SearchImageStack``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``


Tree
----

.. method:: getApproximatedSurface()

   Retrieves an approximate estimate of Tree's surface are by approximating the surface area of each path, and summing to total. The surface of each path is computed assuming the lateral surface area of a conical frustum between nodes.

   **Signature:** ``getApproximatedSurface() -> double``

   **Returns:** (``float``) the approximate surface area or NaN if this Tree's paths have no radius

.. method:: getApproximatedVolume()

   Retrieves an approximate estimate of Tree's volume by approximating the volume of each path, and summing to total. The volume of each path is computed assuming the volume of each of inter-node segment to be that of a truncated cone (Frustum).

   **Signature:** ``getApproximatedVolume() -> double``

   **Returns:** (``float``) the approximate volume or NaN if this Tree's paths have no radius

.. method:: getAssignedValue()

   Retrieves the numeric property assigned to this Tree.

   **Signature:** ``getAssignedValue() -> double``

   **Returns:** (``float``) the assigned value.

.. method:: getBPs()

   Gets the branch points (junctions) of the graph. This is simply an alias for `DirectedWeightedGraph.getBPs()`.

   **Signature:** ``getBPs() -> List``

   **Returns:** (``List[Any]``) the list of branch points

.. method:: getBoundingBox()

   Gets the bounding box associated with this tree.

   **Signature:** ``getBoundingBox() -> BoundingBox``

   **Returns:** ``BoundingBox``

.. method:: getCanvasOffset()

   Returns the canvas offset of this tree.

   **Signature:** ``getCanvasOffset() -> PointInCanvas``

   **Returns:** (``Any``) the canvas offset. Never null (defaults to 0,0,0) if no offset exists.

.. method:: getColor()

   Gets the color assigned to this Tree.

   **Signature:** ``getColor() -> ColorRGB``

   **Returns:** (``Any``) the Tree color, or null if no color has been assigned

.. method:: getConvexHull()

   Retrieves the convex hull of this tree.

   **Signature:** ``getConvexHull() -> AbstractConvexHull``

   **Returns:** ``Any``

.. method:: getGraph()

   Assembles a DirectedGraph from this Tree.

   **Signature:** ``getGraph() -> DirectedWeightedGraph``

   **Returns:** ``DirectedWeightedGraph``

.. method:: getImpContainer(multiDThreePaneView, bitDepth)

   Gets an empty image capable of holding the skeletonized version of this tree.

   **Signature:** ``getImpContainer(int, int) -> ImagePlus``

   **Parameters:**

   * **multiDThreePaneView** (``int``): - the pane flag indicating the SNT view for this image e.g., MultiDThreePanes.XY_PLANE
   * **bitDepth** (``int``)

   **Returns:** (``Any``) the empty `ImagePlus` container

.. method:: getLabel()

   Returns the identifying label of this tree. When importing files, the label typically defaults to the imported filename,

   **Signature:** ``getLabel() -> String``

   **Returns:** (``str``) the Tree label (or null) if none has been set.

.. method:: getNodes()

   Gets all the nodes (path points) forming this tree.

   **Signature:** ``getNodes() -> List``

   **Returns:** (``List[Any]``) the points

.. method:: getNodesAsSWCPoints()

   **Signature:** ``getNodesAsSWCPoints() -> List``

   **Returns:** ``List[Any]``

.. method:: getNodesCount()

   Gets the total number of nodes across all paths in this Tree.

   **Signature:** ``getNodesCount() -> long``

   **Returns:** (``int``) the total node count

.. method:: getProperties()

   Returns the Properties instance holding the persistent set of properties. Useful to associate metadata to this tree. E.g.


```
getProperties().setProperty(Tree.KEY_SPATIAL_UNIT, "um");
 String unit = getProperties().getProperty(Tree.KEY_SPATIAL_UNIT);
 getProperties().setProperty(Tree.KEY_COMPARTMENT, Tree.DENDRITIC);
```


   **Signature:** ``getProperties() -> Properties``

   **Returns:** (``Any``) the Properties instance

   **Example:**

   .. code-block:: java

      getProperties().setProperty(Tree.KEY_SPATIAL_UNIT, "um");
       String unit = getProperties().getProperty(Tree.KEY_SPATIAL_UNIT);
       getProperties().setProperty(Tree.KEY_COMPARTMENT, Tree.DENDRITIC);

.. method:: getRoot()

   Gets the first node of the main primary path of this tree

   **Signature:** ``getRoot() -> PathNode``

   **Returns:** (``Any``) the root node, or null if the main primary path is undefined for this tree.

.. method:: getSWCTypeMap()

   Returns the SWC Type flags used by SNT.

   **Signature:** ``getSWCTypeMap() -> Map``

   **Returns:** (``Dict[str, Any]``) the map mapping swct type flags (e.g., `Path.SWC_AXON`, `Path.SWC_DENDRITE`, etc.) and their respective labels

.. method:: getSWCTypeNames(includeSoma)

   Gets the set of SWC type labels present in this tree with optional soma inclusion in a readable form.

   **Signature:** ``getSWCTypeNames(boolean) -> Set``

   **Parameters:**

   * **includeSoma** (``bool``): - if true, includes soma in the returned set; if false, excludes Path.SWC_SOMA from the result

   **Returns:** (``Set[Any]``) a Set containing the SWC type labels (e.g., `Path.SWC_AXON_LABEL`, `Path.SWC_DENDRITE_LABEL`, etc.) present in the tree

.. method:: getSWCTypes()

   Gets the set of SWC types present in this tree with optional soma inclusion.

   **Signature:** ``getSWCTypes() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getSkeleton()

   Retrieves the rasterized skeleton of this tree at 1:1 scaling.

   **Signature:** ``getSkeleton() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getSkeleton2D()

   Retrieves a 2D projection of the rasterized skeleton of this tree at 1:1 scaling.

   **Signature:** ``getSkeleton2D() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getSomaNodes()

   Gets the list of all nodes tagged as `Path.SWC_SOMA`.

   **Signature:** ``getSomaNodes() -> List``

   **Returns:** (``List[Any]``) the soma nodes or null if no Paths are tagged as soma.

.. method:: getSparseGraph()

   Assembles a memory-efficient CSR-backed `DirectedWeightedGraph` from this Tree. Functionally equivalent to `getGraph()` (same vertex / edge content, same edge weights), but the underlying storage uses ~20x less heap per vertex than the default jgrapht specifics. Useful in batch workflows where many trees' graphs are held simultaneously, or where an analyzer is run across very large neuron collections.

Trade-off: `getEdge(v1, v2)` is O(out-degree of v1) instead of O(1), and per-vertex edge iteration is in reverse insertion order. Both are negligible for permutation-invariant analyses such as Strahler ordering.

   **Signature:** ``getSparseGraph() -> SparseDirectedWeightedGraph``

   **Returns:** (``Any``) the Tree's CSR-backed graph (cached on the Tree instance, separately from `getGraph()`)

.. method:: getTips()

   Gets the end points (tips) of the graph. This is simply an alias for `DirectedWeightedGraph.getTips()`.

   **Signature:** ``getTips() -> List``

   **Returns:** (``List[Any]``) the list of end points

.. method:: getTreeID()

   Returns the ID shared by every `Path` in this tree (see `Path.getTreeID()`), i.e., the arbor's identity as tracked by the `PathAndFillManager` that assigned it.

**Uniqueness is scoped to a single `PathAndFillManager` instance**, e.g., all the Trees of a running SNT session, or all the Trees parsed from one multi-tree reconstruction file. It is *not* guaranteed across independently-created Trees: each standalone parse (a call to `fromFile(String)`, or each individual file visited by `listFromFile(String)`/`listFromDir(String)`) gets its own manager with its own ID sequence starting from scratch, so two such Trees - even from the same `listFromDir()` call - may share the same ID. Once a Tree is merged into a live manager (e.g., via `PathAndFillManager.addTree(Tree)`), its paths are assigned fresh, unique, collision-free IDs scoped to that manager; any IDs from the Tree's original source file are discarded.

   **Signature:** ``getTreeID() -> int``

   **Returns:** (``int``) the tree ID, or -1 if this tree has no paths (a treeID is always >= 1 otherwise - see `PathAndFillManager#maxUsedTreeID`)

.. method:: isAnnotated()

   Checks if the nodes of this Tree have been assigned `BrainAnnotation`s (neuropil labels).

   **Signature:** ``isAnnotated() -> boolean``

   **Returns:** (``bool``) true if at least one node in the Tree has a valid annotation, false otherwise

.. method:: isEmpty()

   Checks if this Tree is empty.

   **Signature:** ``isEmpty() -> boolean``

   **Returns:** (``bool``) true if this tree contains no Paths, false otherwise

.. method:: size()

   Retrieves the number of paths in this tree.

   **Signature:** ``size() -> int``

   **Returns:** (``int``) Returns the number of paths in this tree.


TreeColorMapper
---------------

.. method:: getAvailableHeatmapLuts()

   **Signature:** ``getAvailableHeatmapLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvailableLuts()

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getColor(mappedValue)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(mappedValue)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable()

   **Signature:** ``getColorTable() -> ColorTable``

   **Returns:** ``Any``

.. method:: getMeasurement()

   Description copied from class: `ColorMapper`

   **Signature:** ``getMeasurement() -> String``

   **Returns:** (``str``) the unit, or an empty string if unknown/not applicable

.. method:: getMeasurementLabel()

   **Signature:** ``getMeasurementLabel() -> String``

   **Returns:** ``str``

.. method:: getMetrics()

   Gets the list of supported mapping metrics.

   **Signature:** ``getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of mapping metrics.

.. method:: getMinMax()

   **Signature:** ``getMinMax() -> double[]``

   **Returns:** ``List[float]``

.. method:: getMultiViewer()

   Assembles a `Multi-pane viewer` using all the Trees mapped so far.

   **Signature:** ``getMultiViewer() -> MultiViewer2D``

   **Returns:** (``MultiViewer2D``) the multi-viewer instance

.. method:: getNaNColor()

   **Signature:** ``getNaNColor() -> Color``

   **Returns:** ``Any``

.. method:: isIntegerScale()

   **Signature:** ``isIntegerScale() -> boolean``

   **Returns:** ``bool``

.. method:: isNodeMapping()

   **Signature:** ``isNodeMapping() -> boolean``

   **Returns:** ``bool``


TreeParser
----------

.. method:: getCenter()

   **Signature:** ``getCenter() -> PointInImage``

   **Returns:** ``PointInImage``

.. method:: getLabelsImage(templateImg, cTable)

   **Signature:** ``getLabelsImage(ImagePlus, ColorTable) -> ImagePlus``

   **Parameters:**

   * **templateImg** (``Any``)
   * **cTable** (``Any``)

   **Returns:** ``Any``

.. method:: getProfile()

   **Signature:** ``getProfile() -> Profile``

   **Returns:** ``Profile``

.. method:: getTree()

   **Signature:** ``getTree() -> Tree``

   **Returns:** ``Tree``

.. method:: isSkipSomaticSegments()

   **Signature:** ``isSkipSomaticSegments() -> boolean``

   **Returns:** ``bool``

.. method:: setStepSize(stepSize)

   **Signature:** ``setStepSize(double) -> void``

   **Parameters:**

   * **stepSize** (``float``)

   **Returns:** ``None``


TreeProperties
--------------

.. method:: getStandardizedCompartment(description)

   **Signature:** ``getStandardizedCompartment(String) -> String``

   **Parameters:**

   * **description** (``str``)

   **Returns:** ``str``


TreeStatistics
--------------

.. method:: getAllMetrics()

   Gets the list of supported metrics.

   **Signature:** ``getAllMetrics() -> List``

   **Returns:** (``List[Any]``) the list of available metrics

.. method:: getAnnotatedLength(level)

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron.

   **Signature:** ``getAnnotatedLength(int) -> Map``

   **Parameters:**

   * **level** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain compartments as keys, and cable lengths as values.

.. method:: getAnnotatedLengthHistogram()

   **Signature:** ``getAnnotatedLengthHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedLengthsByHemisphere(level)

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron in the two brain hemispheres. Lengths are absolute and not normalized to the cells' cable length.

   **Signature:** ``getAnnotatedLengthsByHemisphere(int) -> Map``

   **Parameters:**

   * **level** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain compartments as keys, and cable lengths per hemisphere as values.

.. method:: getAnnotations()

   Retrieves the brain compartments (neuropil labels) associated with the Tree being measured innervated by the analyzed neuron.

   **Signature:** ``getAnnotations() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvgBranchLength()

   Gets average length for all the branches of the analyzed tree.

   **Signature:** ``getAvgBranchLength() -> double``

   **Returns:** (``float``) the average branch length

.. method:: getAvgContraction()

   Gets average `contraction` for all the branches of the analyzed tree.

   **Signature:** ``getAvgContraction() -> double``

   **Returns:** (``float``) the average branch contraction

.. method:: getAvgFractalDimension()

   Gets the average fractal dimension of the analyzed tree. Note that branches with less than 5 points are ignored during the computation.

   **Signature:** ``getAvgFractalDimension() -> double``

   **Returns:** (``float``) the average fractal dimension

.. method:: getAvgFragmentation()

   Gets the average no. of nodes (fragmentation) for all the branches of the analyzed tree.

   **Signature:** ``getAvgFragmentation() -> double``

   **Returns:** (``float``) the average no. of branch nodes (average branch fragmentation)

.. method:: getAvgPartitionAsymmetry()

   Gets the average partition asymmetry of the analyzed tree. Note that branch points with more than 2 children are ignored during the computation.

   **Signature:** ``getAvgPartitionAsymmetry() -> double``

   **Returns:** (``float``) the average partition asymmetry

.. method:: getAvgRemoteBifAngle()

   Gets the average remote bifurcation angle of the analyzed tree. Note that branch points with more than 2 children are ignored during the computation.

   **Signature:** ``getAvgRemoteBifAngle() -> double``

   **Returns:** (``float``) the average remote bifurcation angle

.. method:: getBranchPoints()

   Gets the position of all the branch points in the analyzed tree associated with the specified annotation.

   **Signature:** ``getBranchPoints() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getBranches()

   Gets all the branches in the analyzed tree. A branch is defined as the Path composed of all the nodes between two branching points or between one branching point and a termination point.

   **Signature:** ``getBranches() -> List``

   **Returns:** (``List[Any]``) the list of branches as Path objects.

.. method:: getCableLength()

   Gets the cable length associated with the specified compartment (neuropil label).

   **Signature:** ``getCableLength() -> double``

   **Returns:** ``float``

.. method:: getCableLengthNorm(compartment)

   Gets the cable length associated with the specified compartment (neuropil label) as a ratio of total length.

   **Signature:** ``getCableLengthNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **compartment** (``Any``): - the query compartment (null not allowed)

   **Returns:** (``float``) the filtered cable length normalized to total cable length

.. method:: getConvexAnalyzer()

   Gets the `ConvexHullAnalyzer` instance associated with this TreeStatistics instance.

   **Signature:** ``getConvexAnalyzer() -> ConvexHullAnalyzer``

   **Returns:** (``ConvexHullAnalyzer``) the ConvexHullAnalyzer instance

.. method:: getConvexHullMetric(metric)

   Convenience method to obtain a single-value metric from `ConvexHullAnalyzer`

   **Signature:** ``getConvexHullMetric(String) -> double``

   **Parameters:**

   * **metric** (``str``): - the metric to be retrieved, one of ConvexHullAnalyzer.supportedMetrics()

   **Returns:** (``float``) the convex hull metric

.. method:: getDepth()

   Returns the depth of the `BoundingBox` box of the tree being measured

   **Signature:** ``getDepth() -> double``

   **Returns:** (``float``) the bounding box depth

.. method:: getDescriptiveStats(metric)

   Computes the `DescriptiveStatistics` for the specified measurement.

   **Signature:** ``getDescriptiveStats(String) -> DescriptiveStatistics``

   **Parameters:**

   * **metric** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``Any``) the DescriptiveStatistics object.

.. method:: getFlowPlot(feature, annotations)

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.

   **Signature:** ``getFlowPlot(String, Collection) -> SNTChart``

   **Parameters:**

   * **feature** (``str``): - the feature ("Cable length", "No. of branch points", "No. of tips", etc.). Note that the majority of getAllMetrics() metrics are currently not supported.
   * **annotations** (``List[Any]``)

   **Returns:** (``SNTChart``) the SNTChart holding the flow plot

.. method:: getFractalDimension()

   Gets the fractal dimension of each branch in the analyzed tree. Note that branches with less than 5 points are ignored.

   **Signature:** ``getFractalDimension() -> List``

   **Returns:** (``List[Any]``) a list containing the fractal dimension of each branch

.. method:: getHeight()

   Returns the height of the `BoundingBox` box of the tree being measured

   **Signature:** ``getHeight() -> double``

   **Returns:** (``float``) the bounding box height

.. method:: getHighestPathOrder()

   Gets the highest `path order` of the analyzed tree

   **Signature:** ``getHighestPathOrder() -> int``

   **Returns:** (``int``) the highest Path order, or -1 if Paths in the Tree have no defined order

.. method:: getHistogram(metric)

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``)

   **Returns:** ``SNTChart``

.. method:: getInnerBranches()

   Retrieves the branches of highest `Strahler order` in the Tree. This typically correspond to the most 'internal' branches of the Tree in direct sequence from the root.

   **Signature:** ``getInnerBranches() -> List``

   **Returns:** (``List[Any]``) the list containing the "inner" branches. Note that these branches (Path segments) will not carry any connectivity information.

.. method:: getInnerLength()

   Gets the cable length of inner branches

   **Signature:** ``getInnerLength() -> double``

   **Returns:** (``float``) the length sum of all inner branches

.. method:: getMetric(metric)

   Computes the specified metric.

   **Signature:** ``getMetric(String) -> Number``

   **Parameters:**

   * **metric** (``str``): - the single-value metric to be computed (case-insensitive). While it is expected to be an element of getAllMetrics(), unless isExactMetricMatch() is set,

   **Returns:** (``Union[int, float]``) the computed value (average if metric is associated with multiple values)

.. method:: getNBranchPoints(annot)

   Gets the number of branch points in the analyzed tree associated with the specified annotation.

   **Signature:** ``getNBranchPoints(BrainAnnotation) -> int``

   **Parameters:**

   * **annot** (``Any``): - the BrainAnnotation to be queried.

   **Returns:** (``int``) the number of branch points

.. method:: getNBranchPointsNorm(annot)

   Gets the percentage of branch points in the analyzed tree associated with the specified annotation

   **Signature:** ``getNBranchPointsNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **annot** (``Any``): - the BrainAnnotation to be queried.

   **Returns:** (``float``) the ratio between the no. of branch points associated with `annot` and the total number of branch points in the tree.

.. method:: getNBranches()

   Gets the number of branches in the analyzed tree.

   **Signature:** ``getNBranches() -> int``

   **Returns:** (``int``) the number of branches

.. method:: getNNodes()

   Gets the number of nodes in the analyzed tree.

   **Signature:** ``getNNodes() -> long``

   **Returns:** (``int``) the number of nodes

.. method:: getNPaths()

   Gets the no. of parsed paths.

   **Signature:** ``getNPaths() -> int``

   **Returns:** (``int``) the number of paths

.. method:: getNTips(annot)

   Gets the number of end points in the analyzed tree associated with the specified annotation.

   **Signature:** ``getNTips(BrainAnnotation) -> int``

   **Parameters:**

   * **annot** (``Any``): - the BrainAnnotation to be queried.

   **Returns:** (``int``) the number of end points

.. method:: getNTipsNorm(annot)

   Gets the percentage of end points in the analyzed tree associated with the specified annotation

   **Signature:** ``getNTipsNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **annot** (``Any``): - the BrainAnnotation to be queried.

   **Returns:** (``float``) the ratio between the no. of branch points associated with `annot` and the total number of end points in the tree.

.. method:: getNoSpinesOrVaricosities()

   Gets the number of spines/varicosities that have been (manually) assigned to tree being analyzed.

   **Signature:** ``getNoSpinesOrVaricosities() -> int``

   **Returns:** (``int``) the number of spines/varicosities

.. method:: getNodeStatistics()

   Convenience method to initialize a `NodeStatistics` from a subset of the nodes of the Tree being analyzed.

   **Signature:** ``getNodeStatistics() -> NodeStatistics``

   **Returns:** ``NodeStatistics``

.. method:: getParsedTree()

   Returns the set of parsed Paths.

   **Signature:** ``getParsedTree() -> Tree``

   **Returns:** (``Tree``) the set of paths currently being considered for analysis.

.. method:: getPartitionAsymmetry()

   Gets the partition asymmetry at each bifurcation point in the analyzed tree. Note that branch points with more than 2 children are ignored.

   **Signature:** ``getPartitionAsymmetry() -> List``

   **Returns:** (``List[Any]``) a list containing the partition asymmetry at each bifurcation point

.. method:: getPolarHistogram(metric)

   Assembles a polar histogram for the specified metric (assumed to be an angular measurements (e.g., branch angles, path orientations).

   **Signature:** ``getPolarHistogram(String) -> SNTChart``

   **Parameters:**

   * **metric** (``str``): - the metric to be plotted (e.g., BRANCH_EXTENSION_ANGLE_XY, PATH_EXT_ANGLE_XY, etc.)

   **Returns:** (``SNTChart``) the polar histogram chart

.. method:: getPrimaryBranches()

   Retrieves the primary branches of the analyzed Tree. Primary branches (or root-associated) have origin in the Tree's root, extending to the closest branch/end-point. Note that a primary branch can also be terminal.

   **Signature:** ``getPrimaryBranches() -> List``

   **Returns:** (``List[Any]``) the primary branches. Note that these branches (Path segments) will not carry any connectivity information.

.. method:: getPrimaryLength()

   Gets the cable length of primary branches.

   **Signature:** ``getPrimaryLength() -> double``

   **Returns:** (``float``) the length sum of all primary branches

.. method:: getPrimaryPaths()

   Retrieves all the Paths in the analyzed Tree tagged as primary.

   **Signature:** ``getPrimaryPaths() -> List``

   **Returns:** (``List[Any]``) the list of primary paths.

.. method:: getRemoteBifAngles()

   Gets the angle between each bifurcation point and its children in the simplified graph, which comprise either branch points or terminal nodes. Note that branch points with more than 2 children are ignored.

   **Signature:** ``getRemoteBifAngles() -> List``

   **Returns:** (``List[Any]``) the list of remote bifurcation angles

.. method:: getRootAngleAnalyzer()

   Gets the `RootAngleAnalyzer` instance associated with this TreeStatistics instance.

   **Signature:** ``getRootAngleAnalyzer() -> RootAngleAnalyzer``

   **Returns:** (``RootAngleAnalyzer``) the RootAngleAnalyzer instance

.. method:: getRootAngleMetric(metric)

   Convenience method to obtain a single-value metric from `RootAngleAnalyzer`.

   **Signature:** ``getRootAngleMetric(String) -> double``

   **Parameters:**

   * **metric** (``str``): - the metric to be retrieved, one of RootAngleAnalyzer.supportedMetrics()

   **Returns:** (``float``) the root angle metric

.. method:: getShollAnalyzer()

   Gets the `ShollAnalyzer` instance associated with this TreeStatistics instance. Note that changes to `ShollAnalyzer` must be performed before retrieving Sholl related metrics, i.e., before calling `measure(Collection, boolean)`, etc.

   **Signature:** ``getShollAnalyzer() -> ShollAnalyzer``

   **Returns:** (``ShollAnalyzer``) the ShollAnalyzer instance associated with this TreeStatistics instance

.. method:: getSpineOrVaricosityDensity()

   Gets the overall density of spines/varicosities associated with this tree

   **Signature:** ``getSpineOrVaricosityDensity() -> double``

   **Returns:** (``float``) the spine/varicosity density (same as `getNoSpinesOrVaricosities()/getCableLength()`)

.. method:: getStrahlerAnalyzer()

   Gets the `StrahlerAnalyzer` instance associated with this TreeStatistics instance

   **Signature:** ``getStrahlerAnalyzer() -> StrahlerAnalyzer``

   **Returns:** (``StrahlerAnalyzer``) the StrahlerAnalyzer instance associated with this TreeStatistics instance

.. method:: getStrahlerBifurcationRatio()

   Gets the average `Strahler bifurcation ratio` of analyzed tree.

   **Signature:** ``getStrahlerBifurcationRatio() -> double``

   **Returns:** (``float``) the average bifurcation ratio

.. method:: getStrahlerNumber()

   Gets the highest `Strahler number` of the analyzed tree.

   **Signature:** ``getStrahlerNumber() -> int``

   **Returns:** (``int``) the highest Strahler (root) number order

.. method:: getSummaryStats(metric)

   Computes the `SummaryStatistics` for the specified measurement.

   **Signature:** ``getSummaryStats(String) -> SummaryStatistics``

   **Parameters:**

   * **metric** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``Any``) the SummaryStatistics object.

.. method:: getTable()

   Gets the table currently being used by this TreeStatistics instance

   **Signature:** ``getTable() -> DefaultGenericTable``

   **Returns:** (``Any``) the table

.. method:: getTerminalBranches()

   Retrieves the terminal branches of the analyzed Tree. A terminal branch corresponds to the section of a terminal Path between its last branch-point and its terminal point (tip). A terminal branch can also be primary.

   **Signature:** ``getTerminalBranches() -> List``

   **Returns:** (``List[Any]``) the terminal branches. Note that as per `Path.getSection(int, int)`, these branches will not carry any connectivity information.

.. method:: getTerminalLength()

   Gets the cable length of terminal branches

   **Signature:** ``getTerminalLength() -> double``

   **Returns:** (``float``) the length sum of all terminal branches

.. method:: getTips()

   Gets the position of all tips in the analyzed tree that are within the specified distance range from the root. This method is useful for analyzing tree morphology within specific distance bands from the soma.

   **Signature:** ``getTips() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getUnit(metric)

   Returns the physical unit associated with the specified metric. This is the single source of truth for metric units: histograms, tables and color legends all rely on it.

   **Signature:** ``getUnit(String) -> String``

   **Parameters:**

   * **metric** (``str``): - the metric to be queried (case-insensitive)

   **Returns:** (``str``) physical unit, or an empty string if the metric is dimensionless

.. method:: getWidth()

   Returns the width of the `BoundingBox` box of the tree being measured

   **Signature:** ``getWidth() -> double``

   **Returns:** (``float``) the bounding box width

.. method:: isExactMetricMatch()

   Checks if 'fuzzy matching' of metrics is disabled for this instance.

   **Signature:** ``isExactMetricMatch() -> boolean``

   **Returns:** (``bool``) true if only exact (case and punctuation insensitive) matching is active, false if loose phrases such as "# bps" are also matched

.. method:: isValid()

   Checks whether this tree is topologically valid, i.e., contains only one root and no loops.

   **Signature:** ``isValid() -> boolean``

   **Returns:** (``bool``) true, if Tree is valid, false otherwise


TreeToRaster
------------

.. method:: getAxialRes()

   Gets the axial (z) voxel size.

   **Signature:** ``getAxialRes() -> double``

   **Returns:** (``float``) the axial (z) voxel size in the tree's spatial units (typically µm), or `0` when rasterizing in 2D mode

.. method:: getLateralRes()

   Gets the lateral (x, y) voxel size.

   **Signature:** ``getLateralRes() -> double``

   **Returns:** (``float``) the lateral (x,y) voxel size in the tree's spatial units (typically µm)

.. method:: getRadiusScale()

   Gets the uniform radius multiplier applied to node radii.

   **Signature:** ``getRadiusScale() -> double``

   **Returns:** (``float``) the radius multiplier (1.0 by default)

.. method:: getRasterOrigin()

   Gets the position, in the tree's coordinate system, of the center of voxel (0, 0, 0) of the image returned by `rasterize()`. The rasterized image is not calibrated with an origin, so this is needed to place it (e.g., a mesh extracted from it) back on the tree. The result depends on the current resolution and reference bounds settings, which should be set before calling this method.

   **Signature:** ``getRasterOrigin() -> double[]``

   **Returns:** (``List[float]``) the {x, y, z} position of the center of the first voxel

.. method:: getRasterVoxelCount()

   Gets the number of voxels of the image `rasterize()` would allocate with the current settings, so that callers can avoid oversized requests.

   **Signature:** ``getRasterVoxelCount() -> long``

   **Returns:** (``int``) the voxel count


TreeUtils
---------

.. method:: canFormContinuousChain(paths, tolerance)

   Checks if a collection of paths can form a spatially continuous chain within a given tolerance.

   **Signature:** ``canFormContinuousChain(Collection, double) -> boolean``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to check
   * **tolerance** (``float``)

   **Returns:** (``bool``) true if paths can be ordered into a continuous chain within tolerance

.. method:: filterByCableLength(trees, minLength, maxLength)

   Returns the subset of trees whose cable length falls within the specified range.

   **Signature:** ``filterByCableLength(Collection, double, double) -> List``

   **Parameters:**

   * **trees** (``List[Any]``): - the input collection
   * **minLength** (``float``)
   * **maxLength** (``float``)

   **Returns:** (``List[Any]``) a new list containing only the trees that satisfy the bounds

.. method:: filterBySize(trees, minPaths, maxPaths)

   Returns the subset of trees whose path count falls within the specified range.

   **Signature:** ``filterBySize(Collection, int, int) -> List``

   **Parameters:**

   * **trees** (``List[Any]``): - the input collection
   * **minPaths** (``int``)
   * **maxPaths** (``int``)

   **Returns:** (``List[Any]``) a new list containing only the trees that satisfy the bounds

.. method:: getConnectedTree(path)

   Gets the connected tree (component) containing the given path. This traverses up to the root and then collects all descendants, ensuring we only get paths that are actually connected via parent-child relationships.

This is useful when paths may share a tree ID but are not actually connected (e.g., orphaned paths or paths awaiting relationship rebuild).

   **Signature:** ``getConnectedTree(Path) -> Tree``

   **Parameters:**

   * **path** (``Path``): - a path in the tree

   **Returns:** (``Tree``) a Tree containing only the connected component

.. method:: getMaxOrder(path)

   Returns the maximum path order in the connected tree containing the given path. Higher values indicate deeper/more developed trees.

   **Signature:** ``getMaxOrder(Path) -> int``

   **Parameters:**

   * **path** (``Path``): - a path in the tree

   **Returns:** (``int``) the maximum order value found in the connected tree, or 0 if retrieval fails

.. method:: getRootPath(path)

   Gets the root path of the tree containing the given path.

   **Signature:** ``getRootPath(Path) -> Path``

   **Parameters:**

   * **path** (``Path``)

   **Returns:** ``Path``

.. method:: isAncestorOf(potentialAncestor, potentialDescendant)

   Checks if 'potentialAncestor' is an ancestor of 'potentialDescendant'. This traverses up the parent chain from potentialDescendant.

   **Signature:** ``isAncestorOf(Path, Path) -> boolean``

   **Parameters:**

   * **potentialAncestor** (``Path``): - the path to check if it's an ancestor
   * **potentialDescendant** (``Path``)

   **Returns:** (``bool``) true if potentialAncestor is an ancestor of potentialDescendant

.. method:: isDescendantOf(potentialDescendant, potentialAncestor)

   Checks if 'potentialDescendant' is a descendant of 'potentialAncestor'. This is equivalent to checking if potentialDescendant is in the subtree rooted at potentialAncestor (excluding potentialAncestor itself).

   **Signature:** ``isDescendantOf(Path, Path) -> boolean``

   **Parameters:**

   * **potentialDescendant** (``Path``): - the path to check if it's a descendant
   * **potentialAncestor** (``Path``)

   **Returns:** (``bool``) true if potentialDescendant is a descendant of potentialAncestor

.. method:: isInSubtree(target, root)

   Checks if 'target' is in the subtree rooted at 'root'. This traverses down through all descendants of root.

   **Signature:** ``isInSubtree(Path, Path) -> boolean``

   **Parameters:**

   * **target** (``Path``): - the path to search for
   * **root** (``Path``)

   **Returns:** (``bool``) true if target is root or any descendant of root


VFBUtils
--------

.. method:: getMesh(vfbId)

   Retrieves the mesh associated with the specified VFB id.

   **Signature:** ``getMesh(String) -> OBJMesh``

   **Parameters:**

   * **vfbId** (``str``): - the VFB id, e.g., VFB_00017894, 00017894

   **Returns:** (``OBJMesh``) a reference to the retrieved mesh

.. method:: getRefBrain(templateBrain)

   Retrieves the surface mesh of an adult Drosophila template brain. No Internet connection is required, as these meshes (detailed on the nat.flybrains documentation) are bundled with SNT.

   **Signature:** ``getRefBrain(String) -> OBJMesh``

   **Parameters:**

   * **templateBrain** (``str``): - the template brain to be loaded (case-insensitive). Either "JFRC2" (AKA JFRC2010, VFB), "JFRC3" (AKA JFRC2013), "JFRC2018", or "FCWB" (FlyCircuit Whole Brain Template)

   **Returns:** (``OBJMesh``) the template mesh.

.. method:: getXYZLabels()

   **Signature:** ``getXYZLabels() -> String[]``

   **Returns:** (``List[str]``) the anatomical descriptions associated with the Cartesian X,Y,Z axes

.. method:: isDatabaseAvailable()

   Checks whether a connection to the Virtual Fly Brain database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established


Viewer2D
--------

.. method:: getAvailableHeatmapLuts()

   **Signature:** ``getAvailableHeatmapLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getAvailableLuts()

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getChart()

   Gets the current viewer as a `SNTChart` object

   **Signature:** ``getChart() -> SNTChart``

   **Returns:** (``SNTChart``) the converted viewer

.. method:: getColor(mappedValue)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(mappedValue)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **mappedValue** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable()

   **Signature:** ``getColorTable() -> ColorTable``

   **Returns:** ``Any``

.. method:: getJFreeChart()

   Gets the current viewer as a `JFreeChart` object

   **Signature:** ``getJFreeChart() -> JFreeChart``

   **Returns:** (``Any``) the converted viewer

.. method:: getMeasurement()

   **Signature:** ``getMeasurement() -> String``

   **Returns:** ``str``

.. method:: getMeasurementLabel()

   **Signature:** ``getMeasurementLabel() -> String``

   **Returns:** ``str``

.. method:: getMetrics()

   **Signature:** ``getMetrics() -> List``

   **Returns:** ``List[Any]``

.. method:: getMinMax()

   **Signature:** ``getMinMax() -> double[]``

   **Returns:** ``List[float]``

.. method:: getMultiViewer()

   **Signature:** ``getMultiViewer() -> MultiViewer2D``

   **Returns:** ``MultiViewer2D``

.. method:: getNaNColor()

   **Signature:** ``getNaNColor() -> Color``

   **Returns:** ``Any``

.. method:: getPlot()

   Gets the current plot as a `XYPlot` object

   **Signature:** ``getPlot() -> XYPlot``

   **Returns:** (``Any``) the current plot

.. method:: getTitle()

   Gets the plot display title.

   **Signature:** ``getTitle() -> String``

   **Returns:** (``str``) the current display title

.. method:: isIntegerScale()

   **Signature:** ``isIntegerScale() -> boolean``

   **Returns:** ``bool``

.. method:: isNodeMapping()

   **Signature:** ``isNodeMapping() -> boolean``

   **Returns:** ``bool``

.. method:: setPreferredSize(width, height)

   Sets the preferred size of the plot to a constant value.

   **Signature:** ``setPreferredSize(int, int) -> void``

   **Parameters:**

   * **width** (``int``): - the preferred width
   * **height** (``int``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: getAnimationAxis()

   Gets the current rotation axis for the live animation.

   **Signature:** ``getAnimationAxis() -> RotationAxis``

   **Returns:** (``Any``) the current rotation axis, or Z if not set

.. method:: getAnimationMode()

   Gets the current animation mode.

   **Signature:** ``getAnimationMode() -> AnimationMode``

   **Returns:** (``Any``) the current animation mode

.. method:: getAnnotation(label)

   Gets the annotation associated with the specified label.

   **Signature:** ``getAnnotation(String) -> Annotation3D``

   **Parameters:**

   * **label** (``str``): - the (unique) label as displayed in Viewer's list

   **Returns:** (``Annotation3D``) the annotation or null if no annotation is associated with the specified label

.. method:: getAnnotations()

   Returns all annotations added to this viewer.

   **Signature:** ``getAnnotations() -> List``

   **Returns:** (``List[Any]``) the annotation list

.. method:: getColorCodeLabel()

   Gets the label (measurement and unit, e.g., "Path length (µm)") of the last color coding performed through `colorCode()`. Useful as legend title.

   **Signature:** ``getColorCodeLabel() -> String``

   **Returns:** (``str``) the label, or null if no color coding has been performed

.. method:: getFrame()

   Gets the frame containing this viewer, optionally controlling its visibility.

Returns the AWT Frame that contains this viewer's 3D canvas and UI components. If no frame exists, one will be created with the specified visibility setting. This method is useful when you need to control whether the viewer window appears immediately or remains hidden for programmatic manipulation.

   **Signature:** ``getFrame() -> Frame``

   **Returns:** ``Any``

.. method:: getID()

   Returns this Viewer's id.

   **Signature:** ``getID() -> int``

   **Returns:** (``int``) this Viewer's unique numeric ID.

.. method:: getManagerPanel()

   Returns a reference to control panel.

   **Signature:** ``getManagerPanel() -> ManagerPanel``

   **Returns:** (``Any``) the ManagerPanel associated with this Viewer, or null if the 'RV Controls' dialog is not being displayed.

.. method:: getMesh(label)

   Gets the mesh associated with the specified label.

   **Signature:** ``getMesh(String) -> OBJMesh``

   **Parameters:**

   * **label** (``str``): - the (unique) label as displayed in Viewer's list

   **Returns:** (``OBJMesh``) the mesh or null if no mesh is associated with the specified label

.. method:: getMeshShadingMode()

   Returns the current mesh shading mode.

   **Signature:** ``getMeshShadingMode() -> int``

   **Returns:** (``int``) `OBJMesh.SHADING_DEFAULT` or `OBJMesh.SHADING_SMOOTH`

.. method:: getMeshes()

   Returns all meshes added to this viewer.

   **Signature:** ``getMeshes() -> List``

   **Returns:** ``List[Any]``

.. method:: getRecorder(createIfNeeded)

   Gets the script recorder for this viewer, optionally creating one if needed.

   **Signature:** ``getRecorder(boolean) -> ScriptRecorder``

   **Parameters:**

   * **createIfNeeded** (``bool``): - if true, creates a new recorder if one doesn't exist; if false, returns null when no recorder exists

   **Returns:** (``Any``) the ScriptRecorder instance, or null if none exists and createIfNeeded is false

.. method:: getTree(label)

   Gets the tree associated with the specified label.

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **label** (``str``): - the (unique) label as displayed in Viewer's list

   **Returns:** (``Tree``) the Tree or null if no Tree is associated with the specified label

.. method:: getTrees()

   Returns all trees added to this viewer.

   **Signature:** ``getTrees() -> List``

   **Returns:** ``List[Any]``

.. method:: hashCode()

   **Signature:** ``hashCode() -> int``

   **Returns:** ``int``

.. method:: isActive()

   Checks whether this instance is currently active

   **Signature:** ``isActive() -> boolean``

   **Returns:** (``bool``) true, if active, false otherwise

.. method:: isAutoDetectAnimationAxis()

   Returns whether automatic rotation axis detection is enabled.

   **Signature:** ``isAutoDetectAnimationAxis() -> boolean``

   **Returns:** (``bool``) true if auto-detection is active

.. method:: isDarkModeOn()

   Checks if scene is being rendered under dark or light background.

   **Signature:** ``isDarkModeOn() -> boolean``

   **Returns:** (``bool``) true, if "Dark Mode" is active

.. method:: isMeshBackfaceCull()

   Returns whether backface culling is enabled for OBJ meshes.

   **Signature:** ``isMeshBackfaceCull() -> boolean``

   **Returns:** (``bool``) true if backface culling is enabled

.. method:: isSNTInstance()

   Checks whether this instance is SNT's Reconstruction Viewer.

   **Signature:** ``isSNTInstance() -> boolean``

   **Returns:** (``bool``) true, if SNT instance, false otherwise

.. method:: isScaleBarDisplayed()

   Checks whether the scale bar is being displayed.

   **Signature:** ``isScaleBarDisplayed() -> boolean``

   **Returns:** (``bool``) true if the scale bar is displayed

.. method:: isSplitDendritesFromAxons()

   Checks whether axons and dendrites of imported Trees are set to be imported as separated objects.

   **Signature:** ``isSplitDendritesFromAxons() -> boolean``

   **Returns:** (``bool``) if imported trees are set to be split into axonal and dendritic subtrees.

.. method:: setFrameSize(width, height)

   Resizes the viewer to the specified dimensions. Useful when generating scene animations programmatically. Does nothing if viewer's frame does not exist.

   **Signature:** ``setFrameSize(int, int) -> void``

   **Parameters:**

   * **width** (``int``): - the width of the frame.
   * **height** (``int``): will set width to its maximum.

   **Returns:** ``None``


WekaModelLoader
---------------

.. method:: cancel()

   **Signature:** ``cancel() -> void``

   **Returns:** ``None``

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``


ZBAtlasUtils
------------

.. method:: getRefBrain()

   Retrieves the surface mesh (outline) of the zebrafish template brain.

   **Signature:** ``getRefBrain() -> OBJMesh``

   **Returns:** (``OBJMesh``) the outline mesh.

.. method:: getXYZLabels()

   **Signature:** ``getXYZLabels() -> String[]``

   **Returns:** (``List[str]``) the anatomical descriptions associated with the Cartesian X,Y,Z axes

.. method:: isDatabaseAvailable()

   Checks whether a connection to the FishAtlas database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established


----

*Category index generated on 2026-11-02 07:57:40*