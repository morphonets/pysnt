Getters Methods
===============

Methods that retrieve values or properties from objects.

Total methods in this category: **532**

.. contents:: Classes in this Category
   :local:

AllenCompartment
----------------

.. method:: getAncestor(arg0)

   Gets the nth ancestor of this compartment.

   **Signature:** ``getAncestor(int) -> AllenCompartment``

   **Parameters:**

   * **arg0** (``int``): - the ancestor level as negative 1-based index. E.g.,

   **Returns:** (``Any``) the nth ancestor

.. method:: getAncestors()

   Gets the ancestor ontologies of this compartment as a flat (non-hierarchical) list.

   **Signature:** ``getAncestors() -> List``

   **Returns:** (``List[Any]``) the "flattened" list of ancestors

.. method:: getChildren()

   Gets the child ontologies of this compartment as a flat (non-hierarchical) list.

   **Signature:** ``getChildren() -> List``

   **Returns:** ``List[Any]``

.. method:: getMesh()

   **Signature:** ``getMesh() -> OBJMesh``

   **Returns:** (``Any``) the mesh associated with this compartment

.. method:: getOntologyDepth()

   Gets the ontology depth of this compartment.

   **Signature:** ``getOntologyDepth() -> int``

   **Returns:** (``int``) the ontological depth of this compartment, i.e., its ontological distance relative to the root (e.g., a compartment of hierarchical level 9, has a depth of 8).

.. method:: getParent()

   Gets the parent of this compartment.

   **Signature:** ``getParent() -> AllenCompartment``

   **Returns:** (``Any``) the parent of this compartment, of null if this compartment is root.

.. method:: getTreePath()

   Gets the tree path of this compartment. The TreePath is the list of parent compartments that uniquely identify this compartment in the ontologies hierarchical tree. The elements of the list are ordered with the root ('Whole Brain') as the first element of the list. In practice, this is equivalent to appending this compartment to the list returned by getAncestors().

   **Signature:** ``getTreePath() -> List``

   **Returns:** (``List[Any]``) the tree path that uniquely identifies this compartment as a node in the CCF ontologies tree

.. method:: getUUID()

   **Signature:** ``getUUID() -> UUID``

   **Returns:** ``Any``

.. method:: isChildOf(arg0)

   Assesses if this annotation is a child of a specified compartment.

   **Signature:** ``isChildOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **arg0** (``Any``): - the compartment to be tested

   **Returns:** (``bool``) true, if successful, i.e., parentCompartment is not this compartment and getTreePath() contains parentCompartment

.. method:: isMeshAvailable()

   Checks whether a mesh is known to be available for this compartment.

   **Signature:** ``isMeshAvailable() -> boolean``

   **Returns:** (``bool``) true, if a mesh is available.

.. method:: isParentOf(arg0)

   Assesses if this annotation is the parent of the specified compartment.

   **Signature:** ``isParentOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **arg0** (``Any``): - the compartment to be tested

   **Returns:** (``bool``) true, if successful, i.e., childCompartment is not this compartment and is present in getChildren()


BiSearch
--------

.. method:: getNodesAsImage()

   **Signature:** ``getNodesAsImage() -> SearchImageStack``

   **Returns:** ``Any``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``


BiSearchNode
------------

.. method:: getF(arg0)

   **Signature:** ``getF(boolean) -> double``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``float``

.. method:: getFFromGoal()

   **Signature:** ``getFFromGoal() -> double``

   **Returns:** ``float``

.. method:: getFFromStart()

   **Signature:** ``getFFromStart() -> double``

   **Returns:** ``float``

.. method:: getG(arg0)

   **Signature:** ``getG(boolean) -> double``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``float``

.. method:: getGFromGoal()

   **Signature:** ``getGFromGoal() -> double``

   **Returns:** ``float``

.. method:: getGFromStart()

   **Signature:** ``getGFromStart() -> double``

   **Returns:** ``float``

.. method:: getHeapHandle(arg0)

   **Signature:** ``getHeapHandle(boolean) -> AddressableHeap$Handle``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``Any``

.. method:: getHeapHandleFromGoal()

   **Signature:** ``getHeapHandleFromGoal() -> AddressableHeap$Handle``

   **Returns:** ``Any``

.. method:: getHeapHandleFromStart()

   **Signature:** ``getHeapHandleFromStart() -> AddressableHeap$Handle``

   **Returns:** ``Any``

.. method:: getPredecessorFromGoal()

   **Signature:** ``getPredecessorFromGoal() -> BiSearchNode``

   **Returns:** ``BiSearchNode``

.. method:: getPredecessorFromStart()

   **Signature:** ``getPredecessorFromStart() -> BiSearchNode``

   **Returns:** ``BiSearchNode``

.. method:: getState(arg0)

   **Signature:** ``getState(boolean) -> BiSearchNode$State``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``Any``

.. method:: getStateFromGoal()

   **Signature:** ``getStateFromGoal() -> BiSearchNode$State``

   **Returns:** ``Any``

.. method:: getStateFromStart()

   **Signature:** ``getStateFromStart() -> BiSearchNode$State``

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

   **Signature:** ``getDimensions() -> [D``

   **Returns:** ``Any``

.. method:: getUnit()

   Gets the length unit of voxel spacing

   **Signature:** ``getUnit() -> String``

   **Returns:** (``str``) the unit

.. method:: hasDimensions()

   **Signature:** ``hasDimensions() -> boolean``

   **Returns:** ``bool``

.. method:: isScaled()

   Checks whether this BoundingBox is spatially calibrated, i.e., if voxel spacing has been specified

   **Signature:** ``isScaled() -> boolean``

   **Returns:** (``bool``) true, if voxel spacing has been specified


ConvexHull2D
------------

.. method:: boundarySize()

   **Signature:** ``boundarySize() -> double``

   **Returns:** ``float``

.. method:: getPolygon()

   **Signature:** ``getPolygon() -> Polygon2D``

   **Returns:** ``Any``

.. method:: size()

   **Signature:** ``size() -> double``

   **Returns:** ``float``


ConvexHull3D
------------

.. method:: boundarySize()

   **Signature:** ``boundarySize() -> double``

   **Returns:** ``float``

.. method:: getMesh()

   **Signature:** ``getMesh() -> Mesh``

   **Returns:** ``Any``

.. method:: size()

   **Signature:** ``size() -> double``

   **Returns:** ``float``


ConvexHullAnalyzer
------------------

.. method:: cancel(arg0)

   **Signature:** ``cancel(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

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

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

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

.. method:: getUnit(arg0)

   Returns the physical unit associated with the specified metric.

   **Signature:** ``getUnit(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - the supported metric to be queried (case-sensitive)

   **Returns:** (``str``) physical unit

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``


DefaultSearchNode
-----------------

.. method:: getHandle()

   **Signature:** ``getHandle() -> AddressableHeap$Handle``

   **Returns:** ``Any``

.. method:: getPredecessor()

   **Signature:** ``getPredecessor() -> DefaultSearchNode``

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


Fill
----

.. method:: getEstimatedMeanRadius()

   Returns the estimated mean radius of the fill, assuming a cylindric shape

   **Signature:** ``getEstimatedMeanRadius() -> double``

   **Returns:** (``float``) the estimated mean radius

.. method:: getMetric()

   **Signature:** ``getMetric() -> SNT$CostType``

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

   Merges the input FillerThreads into a single SearchImageStack. When a filled voxel position is present in multiple filler instances, the node with the lowest g-score is chosen for inclusion in the merged stack.

   **Signature:** ``getFillerStack() -> SearchImageStack``

   **Returns:** (``Any``) the merged filler stack


FillerThread
------------

.. method:: getDistanceAtPoint(arg0, arg1, arg2)

   **Signature:** ``getDistanceAtPoint(double, double, double) -> double``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``float``

.. method:: getExitReason()

   **Signature:** ``getExitReason() -> int``

   **Returns:** ``int``

.. method:: getFill()

   **Signature:** ``getFill() -> Fill``

   **Returns:** ``Any``

.. method:: getNodesAsImage()

   **Signature:** ``getNodesAsImage() -> SearchImageStack``

   **Returns:** ``Any``

.. method:: getNodesAsImageFromGoal()

   **Signature:** ``getNodesAsImageFromGoal() -> SearchImageStack``

   **Returns:** ``Any``

.. method:: getNodesAsImageFromStart()

   **Signature:** ``getNodesAsImageFromStart() -> SearchImageStack``

   **Returns:** ``Any``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``

.. method:: getThreshold()

   **Signature:** ``getThreshold() -> double``

   **Returns:** ``float``


FlyCircuitLoader
----------------

.. method:: getReader(arg0)

   Gets the SWC data associated with the specified cell ID as a reader

   **Signature:** ``getReader(String) -> BufferedReader``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Any``) the character stream containing the data, or null if cell ID was not found or could not be retrieved

.. method:: getReconstructionURL(arg0)

   Gets the URL of the SWC file associated with the specified cell ID.

   **Signature:** ``getReconstructionURL(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``str``) the reconstruction URL

.. method:: getTree(arg0)

   Gets the collection of Paths for the specified cell ID

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Tree``) the data for the specified cell as a Tree, or null if data could not be retrieved

.. method:: isDatabaseAvailable()

   Checks whether a connection to the FlyCircuit database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established, false otherwise


GroupedTreeStatistics
---------------------

.. method:: getBoxPlot(arg0)

   Assembles a Box and Whisker Plot for the specified feature.

   **Signature:** ``getBoxPlot(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``SNTChart``

.. method:: getFlowPlot(arg0, arg1, arg2, arg3)

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.

   **Signature:** ``getFlowPlot(String, int, double, boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``int``)
   * **arg2** (``float``)
   * **arg3** (``bool``)

   **Returns:** ``SNTChart``

.. method:: getGroupStats(arg0)

   Gets the group statistics.

   **Signature:** ``getGroupStats(String) -> MultiTreeStatistics``

   **Parameters:**

   * **arg0** (``str``): - the unique label identifying the group

   **Returns:** (``MultiTreeStatistics``) the group statistics or null if no group is mapped to groupLabel

.. method:: getGroups()

   Gets the group identifiers currently queued for analysis.

   **Signature:** ``getGroups() -> List``

   **Returns:** (``List[Any]``) the group identifiers

.. method:: getHistogram(arg0)

   Gets the relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram

.. method:: getN(arg0)

   Gets the number of Trees in a specified group.

   **Signature:** ``getN(String) -> int``

   **Parameters:**

   * **arg0** (``str``): - the unique label identifying the group

   **Returns:** (``int``) the number of Trees or -1 if no group is mapped to groupLabel

.. method:: getPolarHistogram(arg0)

   Gets the relative frequencies histogram for a univariate measurement as a polar (rose) plot assuming a data range between [0-360]. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getPolarHistogram(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``): - the measurement (e.g., MultiTreeStatistics.AVG_REMOTE_ANGLE

   **Returns:** (``SNTChart``) the frame holding the histogram


InsectBrainCompartment
----------------------

.. method:: getAncestor(arg0)

   **Signature:** ``getAncestor(int) -> BrainAnnotation``

   **Parameters:**

   * **arg0** (``int``): - the ancestor level as negative 1-based index. E.g.,

   **Returns:** (``Any``) the ancestor of this compartment at the nth level

.. method:: getMesh()

   **Signature:** ``getMesh() -> OBJMesh``

   **Returns:** (``Any``) the mesh associated with this compartment

.. method:: getOntologyDepth()

   **Signature:** ``getOntologyDepth() -> int``

   **Returns:** ``int``

.. method:: getParent()

   **Signature:** ``getParent() -> BrainAnnotation``

   **Returns:** (``Any``) the parent of this compartment

.. method:: isChildOf(arg0)

   **Signature:** ``isChildOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** (``bool``) whether this compartment is a sub-compartment of annotation

.. method:: isMeshAvailable()

   **Signature:** ``isMeshAvailable() -> boolean``

   **Returns:** (``bool``) whether a mesh is available for this compartment

.. method:: isParentOf(arg0)

   **Signature:** ``isParentOf(BrainAnnotation) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** (``bool``) whether this compartment is a parentCompartment of annotation


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

   **Signature:** ``getNeuronInfo() -> InsectBrainLoader$NeuronInfo``

   **Returns:** ``Any``

.. method:: getTree()

   Gets the collection of Paths for the specified cell ID

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the data for the specified cell as a Tree, or null if data could not be retrieved


InteractiveTracerCanvas
-----------------------

.. method:: getAccessibleContext()

   **Signature:** ``getAccessibleContext() -> AccessibleContext``

   **Returns:** ``Any``

.. method:: getAlignmentX()

   **Signature:** ``getAlignmentX() -> float``

   **Returns:** ``float``

.. method:: getAlignmentY()

   **Signature:** ``getAlignmentY() -> float``

   **Returns:** ``float``

.. method:: getAnnotationsColor()

   **Signature:** ``getAnnotationsColor() -> Color``

   **Returns:** ``Any``

.. method:: getBackground()

   **Signature:** ``getBackground() -> Color``

   **Returns:** ``Any``

.. method:: getBaseline(arg0, arg1)

   **Signature:** ``getBaseline(int, int) -> int``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``int``


MouseLightLoader
----------------

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

   **Returns:** (``Any``) the AllenCompartment containing the soma

.. method:: getSomaLocation()

   Gets the soma location for this neuron.

   **Signature:** ``getSomaLocation() -> SWCPoint``

   **Returns:** (``SWCPoint``) the SWCPoint representing the soma location

.. method:: getTree()

   Script-friendly method to extract the entire neuron as a collection of Paths.

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the neuron as a Tree, or null if data could not be retrieved

.. method:: static getNeuronCount()

   Gets the number of cells publicly available in the MouseLight database.

   **Signature:** ``static getNeuronCount() -> int``

   **Returns:** (``int``) the number of available cells, or -1 if the database could not be reached.


MouseLightQuerier
-----------------

.. method:: static getNeuronCount()

   Gets the number of cells publicly available in the MouseLight database.

   **Signature:** ``static getNeuronCount() -> int``

   **Returns:** (``int``) the number of available cells, or -1 if the database could not be reached.


MultiTreeColorMapper
--------------------

.. method:: getAvailableLuts()

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getColor(arg0)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(arg0)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable(arg0)

   **Signature:** ``getColorTable(String) -> ColorTable``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getMinMax()

   **Signature:** ``getMinMax() -> [D``

   **Returns:** ``Any``

.. method:: getMultiViewer()

   Description copied from class: TreeColorMapper

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


MultiTreeStatistics
-------------------

.. method:: cancel(arg0)

   Main method for testing and demonstration purposes.

Creates a MultiTreeStatistics instance using demo data and displays various analysis plots including histograms and flow plots. This method is primarily used for development and debugging.

   **Signature:** ``cancel(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - command line arguments (not used)

   **Returns:** ``None``

.. method:: getAnnotatedLength(arg0, arg1)

   Description copied from class: TreeStatistics

   **Signature:** ``getAnnotatedLength(int, String) -> Map``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedLengthHistogram()

   **Signature:** ``getAnnotatedLengthHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedLengthsByHemisphere(arg0)

   Description copied from class: TreeStatistics

   **Signature:** ``getAnnotatedLengthsByHemisphere(int) -> Map``

   **Parameters:**

   * **arg0** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain compartments as keys, and cable lengths per hemisphere as values.

.. method:: getAnnotations(arg0)

   Description copied from class: TreeStatistics

   **Signature:** ``getAnnotations(int) -> Set``

   **Parameters:**

   * **arg0** (``int``): - the max. ontological depth of the compartments to be retrieved

   **Returns:** (``Set[Any]``) the set of brain compartments (BrainAnnotations)

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

   Description copied from class: TreeStatistics

   **Signature:** ``getBranchPoints() -> Set``

   **Returns:** (``Set[Any]``) the branch points positions

.. method:: getBranches()

   Description copied from class: TreeStatistics

   **Signature:** ``getBranches() -> List``

   **Returns:** (``List[Any]``) the list of branches as Path objects.

.. method:: getCableLength(arg0)

   Description copied from class: TreeStatistics

   **Signature:** ``getCableLength(BrainAnnotation) -> double``

   **Parameters:**

   * **arg0** (``Any``): - the query compartment (null not allowed). All of its children will be considered

   **Returns:** (``float``) the filtered cable length

.. method:: getCableLengthNorm(arg0)

   **Signature:** ``getCableLengthNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``float``

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getConvexAnalyzer()

   **Signature:** ``getConvexAnalyzer() -> ConvexHullAnalyzer``

   **Returns:** ``Any``

.. method:: getConvexHullMetric(arg0)

   **Signature:** ``getConvexHullMetric(String) -> double``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``float``

.. method:: getDepth()

   **Signature:** ``getDepth() -> double``

   **Returns:** ``float``

.. method:: getDescriptiveStats(arg0)

   Description copied from class: TreeStatistics

   **Signature:** ``getDescriptiveStats(String) -> DescriptiveStatistics``

   **Parameters:**

   * **arg0** (``str``): - the measurement (TreeStatistics.N_NODES, TreeStatistics.NODE_RADIUS, etc.)

   **Returns:** (``Any``) the DescriptiveStatistics object.

.. method:: getFlowPlot(arg0, arg1, arg2, arg3)

   Description copied from class: TreeStatistics

   **Signature:** ``getFlowPlot(String, int, double, boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``int``)
   * **arg2** (``float``)
   * **arg3** (``bool``)

   **Returns:** ``SNTChart``

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

.. method:: getHistogram(arg0)

   Description copied from class: TreeStatistics

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``): - the measurement (TreeStatistics.N_NODES, TreeStatistics.NODE_RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram

.. method:: getInnerBranches()

   Description copied from class: TreeStatistics

   **Signature:** ``getInnerBranches() -> List``

   **Returns:** (``List[Any]``) the list containing the "inner" branches. Note that these branches (Path segments) will not carry any connectivity information.

.. method:: getInnerLength()

   **Signature:** ``getInnerLength() -> double``

   **Returns:** ``float``

.. method:: getMetric(arg0)

   **Signature:** ``getMetric(String) -> Number``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Union[int, float]``


NeuroMorphoLoader
-----------------

.. method:: getReader(arg0)

   Gets the SWC data ('CNG version') associated with the specified cell ID as a reader

   **Signature:** ``getReader(String) -> BufferedReader``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Any``) the character stream containing the data, or null if cell ID was not found or could not be retrieved

.. method:: getReconstructionURL(arg0)

   Gets the URL of the SWC file ('CNG version') associated with the specified cell ID.

   **Signature:** ``getReconstructionURL(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``str``) the reconstruction URL, or null if cell ID was not found or could not be retrieved

.. method:: getTree(arg0)

   Gets the collection of Paths for the specified cell ID

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved

   **Returns:** (``Tree``) the data ('CNG version') for the specified cell as a Tree, or null if data could not be retrieved

.. method:: isDatabaseAvailable()

   Checks whether a connection to the NeuroMorpho database can be established.

   **Signature:** ``isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established, false otherwise


NodeColorMapper
---------------

.. method:: getAvailableLuts()

   Gets the available LUTs.

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** (``Set[Any]``) the set of keys, corresponding to the set of LUTs available

.. method:: getColor(arg0)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(arg0)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable(arg0)

   Description copied from class: ColorMapper

   **Signature:** ``getColorTable(String) -> ColorTable``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getMinMax()

   Description copied from class: ColorMapper

   **Signature:** ``getMinMax() -> [D``

   **Returns:** (``Any``) a two-element array with current {minimum, maximum} mapping bounds

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

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getDelegateObject()

   **Signature:** ``getDelegateObject() -> Object``

   **Returns:** ``Any``

.. method:: getInfo()

   **Signature:** ``getInfo() -> ModuleInfo``

   **Returns:** ``Any``

.. method:: getInput(arg0)

   **Signature:** ``getInput(String) -> Object``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getInputs()

   **Signature:** ``getInputs() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getOutput(arg0)

   **Signature:** ``getOutput(String) -> Object``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getOutputs()

   **Signature:** ``getOutputs() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getPlot(arg0)

   **Signature:** ``getPlot(Path) -> Plot``

   **Parameters:**

   * **arg0** (``Path``): - the path to be profiled

   **Returns:** (``Any``) The profile (Mean±SD of all the profiled data)

.. method:: getTable(arg0)

   **Signature:** ``getTable(Path) -> SNTTable``

   **Parameters:**

   * **arg0** (``Path``): - the path to be profiled, using its CT positions in the image

   **Returns:** (``SNTTable``) the profiled raw data in tabular form (1 column-per profiled node)

.. method:: getValues(arg0, arg1, arg2)

   Gets the profile for the specified path as a map of lists of pixel intensities (profile indices as keys)

   **Signature:** ``getValues(Path, int, int) -> SortedMap``

   **Parameters:**

   * **arg0** (``Path``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``Any``

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``

.. method:: isInputResolved(arg0)

   **Signature:** ``isInputResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: isOutputResolved(arg0)

   **Signature:** ``isOutputResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: isResolved(arg0)

   **Signature:** ``isResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``


NodeStatistics
--------------

.. method:: getAnnotatedFrequencies(arg0, arg1)

   Retrieves the count frequencies across brain compartment.

   **Signature:** ``getAnnotatedFrequencies(int, String) -> Map``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedFrequenciesByHemisphere(arg0, arg1)

   **Signature:** ``getAnnotatedFrequenciesByHemisphere(int, Tree) -> Map``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``Tree``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedFrequencyHistogram(arg0, arg1, arg2)

   Retrieves the histogram of count frequencies across brain areas of the specified ontology level across the specified hemisphere.

   **Signature:** ``getAnnotatedFrequencyHistogram(int, String, Tree) -> SNTChart``

   **Parameters:**

   * **arg0** (``int``): - the ontological depth of the compartments to be considered
   * **arg1** (``str``)
   * **arg2** (``Tree``)

   **Returns:** (``SNTChart``) the annotated frequencies histogram

.. method:: getAnnotatedHistogram()

   Retrieves the histogram of count frequencies across brain areas of the specified ontology level.

   **Signature:** ``getAnnotatedHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedNodes(arg0)

   Splits the nodes being analyzed into groups sharing the same brain annotation.

   **Signature:** ``getAnnotatedNodes(int) -> Map``

   **Parameters:**

   * **arg0** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain annotations as keys, and list of nodes as values.

.. method:: getDescriptiveStatistics(arg0)

   Computes the `DescriptiveStatistics` for the specified measurement.

   **Signature:** ``getDescriptiveStatistics(String) -> DescriptiveStatistics``

   **Parameters:**

   * **arg0** (``str``): - the measurement (X_COORDINATES, Y_COORDINATES, etc.)

   **Returns:** (``Any``) the DescriptiveStatistics object.

.. method:: getHistogram(arg0)

   Gets the relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``): - the measurement (X_COORDINATES, RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram


Path
----

.. method:: getAngle(arg0)

   Computes the angle between the specified node and its two flanking neighbors.

With B being the specified node, A its previous neighbor, and C is next neighbor, computes the angle between the vectors AB, and BC.

   **Signature:** ``getAngle(int) -> double``

   **Parameters:**

   * **arg0** (``int``)

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

   This is a version of findJunctions() ensuring that a junction node is only retrieved once even if multiple child paths are associated with it.

   **Signature:** ``getBranchPoints() -> Set``

   **Returns:** (``Set[Any]``) the junction nodes

.. method:: getCalibration()

   Gets the spatial calibration of this Path.

   **Signature:** ``getCalibration() -> Calibration``

   **Returns:** (``Any``) the calibration details associated with this Path

.. method:: getCanvasOffset()

   Returns the translation offset used to render this Path in a TracerCanvas.

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

   **Returns:** (``float``) the Contraction of this Path, or NaN if this Path has no length

.. method:: getEditableNodeIndex()

   Gets the position of the node tagged as 'editable', if any.

   **Signature:** ``getEditableNodeIndex() -> int``

   **Returns:** (``int``) the index of the point currently tagged as editable, or -1 if no such point exists

.. method:: getExtensionAngle3D(arg0)

   Returns a single angle representing the 3D extension direction. This is the angle between the path's direction vector and a reference vector.

   **Signature:** ``getExtensionAngle3D(boolean) -> double``

   **Parameters:**

   * **arg0** (``bool``): - the reference vector to measure angle from (e.g., new Vector3d(0, 0, 1) for vertical reference, or new Vector3d(1, 0, 0) for horizontal)

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

   **Signature:** ``getExtensionAngles3D() -> [D``

   **Returns:** (``Any``) double array containing [azimuth, elevation] in degrees, where:

azimuth (index 0): Compass bearing in XY plane (0-360°) following navigation convention:

0° = North (negative Y direction in image coordinates) 90° = East (positive X direction) 180° = South (positive Y direction in image coordinates) 270° = West (negative X direction)

elevation (index 1): Vertical angle from XY plane (-90° to +90°):

0° = horizontal (parallel to XY plane) +90° = pointing straight up (positive Z direction) -90° = pointing straight down (negative Z direction)

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


PathAndFillManager
------------------

.. method:: getBoundingBox(arg0)

   Returns the BoundingBox enclosing all nodes of all existing Paths.

   **Signature:** ``getBoundingBox(boolean) -> BoundingBox``

   **Parameters:**

   * **arg0** (``bool``): - If true, BoundingBox dimensions will be computed for all the existing Paths. If false, the last computed BoundingBox will be returned. Also, if BoundingBox is not scaled, its spacing will be computed from the smallest inter-node distance of an arbitrary ' large' Path. Computations of Path boundaries typically occur during import operations.

   **Returns:** (``BoundingBox``) the BoundingBox enclosing existing nodes, or an 'empty' BoundingBox if no computation of boundaries has not yet occurred. Output is never null.

.. method:: getCorrespondences(arg0, arg1)

   For each point in this PathAndFillManager, find the corresponding point on the other one. If there's no corresponding one, include a null instead. *

   **Signature:** ``getCorrespondences(PathAndFillManager, double) -> List``

   **Parameters:**

   * **arg0** (``Any``): - the other PathAndFillManager holding the corresponding Paths
   * **arg1** (``float``)

   **Returns:** (``List[Any]``) the cloud of NearPoint correspondences

.. method:: getLoadedFills()

   **Signature:** ``getLoadedFills() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getPath(arg0)

   Returns the Path at the specified position in the PathAndFillManager list.

   **Signature:** ``getPath(int) -> Path``

   **Parameters:**

   * **arg0** (``int``): - the index of the Path

   **Returns:** (``Path``) the Path at the specified index

.. method:: getPathFromID(arg0)

   Returns the Path with the specified id.

   **Signature:** ``getPathFromID(int) -> Path``

   **Parameters:**

   * **arg0** (``int``): - the id of the Path to be retrieved

   **Returns:** (``Path``) the Path with the specified id, or null if id was not found.

.. method:: getPathFromName(arg0, arg1)

   Returns the Path with the specified name.

   **Signature:** ``getPathFromName(String, boolean) -> Path``

   **Parameters:**

   * **arg0** (``str``): - the name of the Path to be retrieved
   * **arg1** (``bool``)

   **Returns:** (``Path``) the Path with the specified name, or null if name was not found.

.. method:: getPaths()

   Returns all the paths.

   **Signature:** ``getPaths() -> ArrayList``

   **Returns:** (``List[Any]``) the paths associated with this PathAndFillManager instance.

.. method:: getPathsFiltered()

   Returns the 'de facto' Paths.

   **Signature:** ``getPathsFiltered() -> List``

   **Returns:** (``List[Any]``) the paths associated with this PathAndFillManager instance excluding those that are null or fitted version of o paths.

.. method:: getPathsInROI(arg0)

   **Signature:** ``getPathsInROI(Roi) -> Collection``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``List[Any]``

.. method:: getPathsStructured()

   **Signature:** ``getPathsStructured() -> Path;``

   **Returns:** ``Any``

.. method:: getPlugin()

   Gets the SNT instance.

   **Signature:** ``getPlugin() -> SNT``

   **Returns:** (``Any``) the SNT instance associated with this PathManager (if any)

.. method:: getSWCFor(arg0)

   Converts a collection of connected Path objects into SWC points for export.

SWC is the standardized format used for neuromorphological data exchange. The conversion process:

Validates that paths form a proper tree structure with exactly one primary path (tree's root) Uses breadth-first traversal to ensure correct parent-child relationships Assigns sequential SWC IDs starting from 1 Establishes proper parent references based on path connectivity Preserves path properties including SWC type, color, annotations, and custom tags

Path Requirements:

Must contain exactly one primary path (root of the tree) All non-primary paths must have valid parent relationships Paths must form a connected tree structure (no disconnected components) Empty paths (size == 0) are automatically skipped

   **Signature:** ``getSWCFor(Collection) -> List``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of Path objects to convert. Must contain exactly one primary path and form a connected tree structure. Empty paths are automatically skipped. Cannot be null or empty.

   **Returns:** (``List[Any]``) a list of SWCPoint objects representing the neuronal structure in SWC format. Points are ordered by their sequential SWC IDs, with proper parent-child relationships established. The list is never null but may be empty if all input paths are empty.

.. method:: getSelectedPaths()

   Gets all paths selected in the GUI

   **Signature:** ``getSelectedPaths() -> Set``

   **Returns:** (``Set[Any]``) the collection of selected paths


PathFitter
----------

.. method:: getMaxRadius()

   Gets the current max radius (in pixels)

   **Signature:** ``getMaxRadius() -> int``

   **Returns:** (``int``) the maximum radius currently being considered, or DEFAULT_MAX_RADIUS if setMaxRadius(int) has not been called

.. method:: getPath()

   **Signature:** ``getPath() -> Path``

   **Returns:** (``Path``) the path being fitted

.. method:: getSucceeded()

   Checks whether the fit succeeded.

   **Signature:** ``getSucceeded() -> boolean``

   **Returns:** (``bool``) true if fit was successful, false otherwise


PathProfiler
------------

.. method:: cancel()

   **Signature:** ``cancel() -> void``

   **Returns:** ``None``

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getDelegateObject()

   **Signature:** ``getDelegateObject() -> Object``

   **Returns:** ``Any``

.. method:: getInfo()

   **Signature:** ``getInfo() -> ModuleInfo``

   **Returns:** ``Any``

.. method:: getInput(arg0)

   **Signature:** ``getInput(String) -> Object``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getInputs()

   **Signature:** ``getInputs() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getOutput(arg0)

   **Signature:** ``getOutput(String) -> Object``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getOutputs()

   **Signature:** ``getOutputs() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getPlot(arg0)

   Gets the plot profile as an ImageJ plot (all channels included).

   **Signature:** ``getPlot(int) -> Plot``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Any``

.. method:: getValues(arg0, arg1)

   Gets the profile for the specified path as a map of lists, with distances (or indices) stored under X_VALUES ("x-values") and intensities under Y_VALUES ("y-values").

   **Signature:** ``getValues(Path, int) -> Map``

   **Parameters:**

   * **arg0** (``Path``)
   * **arg1** (``int``)

   **Returns:** ``Dict[str, Any]``

.. method:: getXYPlot(arg0)

   Gets the plot profile as an PlotService plot. It is recommended to call `DynamicCommand.setContext(org.scijava.Context)` beforehand.

   **Signature:** ``getXYPlot(int) -> XYPlot``

   **Parameters:**

   * **arg0** (``int``): - the channel to be parsed (base-0 index)

   **Returns:** (``Any``) the plot

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``

.. method:: isInputResolved(arg0)

   **Signature:** ``isInputResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: isOutputResolved(arg0)

   **Signature:** ``isOutputResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: isResolved(arg0)

   **Signature:** ``isResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``


PathResult
----------

.. method:: getErrorMessage()

   **Signature:** ``getErrorMessage() -> String``

   **Returns:** ``str``

.. method:: getNumberOfPoints()

   **Signature:** ``getNumberOfPoints() -> int``

   **Returns:** ``int``

.. method:: getPath()

   **Signature:** ``getPath() -> [F``

   **Returns:** ``Any``

.. method:: getSuccess()

   **Signature:** ``getSuccess() -> boolean``

   **Returns:** ``bool``


PathStatistics
--------------

.. method:: cancel(arg0)

   Measures specified metrics for each individual path and creates a detailed table.

This method generates a comprehensive measurement table where each row represents an individual path and columns contain the requested morphometric measurements. This is particularly useful for comparative analysis of path properties or for exporting detailed morphometric data.

The generated table includes:

Path identification information (name, SWC type) All requested morphometric measurements Optional summary statistics (if summarize is true)

   **Signature:** ``cancel(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the collection of metric names to measure for each path. If null or empty, a default "safe" set of metrics is used

   **Returns:** ``None``

.. method:: getAnnotatedLength(arg0, arg1)

   **Signature:** ``getAnnotatedLength(int, String) -> Map``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedLengthHistogram()

   **Signature:** ``getAnnotatedLengthHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedLengthsByHemisphere(arg0)

   **Signature:** ``getAnnotatedLengthsByHemisphere(int) -> Map``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotations(arg0)

   **Signature:** ``getAnnotations(int) -> Set``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Set[Any]``

.. method:: getAvgBranchLength()

   Gets the total length of terminal branches.

Calculates the sum of lengths of all terminal branches as defined by `getTerminalBranches()`.

   **Signature:** ``getAvgBranchLength() -> double``

   **Returns:** (``float``) the total length of terminal branches

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

.. method:: getBranchPoints(arg0, arg1)

   **Signature:** ``getBranchPoints(BrainAnnotation, boolean) -> Set``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``Set[Any]``

.. method:: getBranches()

   Gets all the paths being analyzed as branches.

In PathStatistics, all paths are considered as branches since each path represents a distinct structural element.

   **Signature:** ``getBranches() -> List``

   **Returns:** (``List[Any]``) the list of all paths

.. method:: getCableLength()

   **Signature:** ``getCableLength() -> double``

   **Returns:** ``float``

.. method:: getCableLengthNorm(arg0)

   **Signature:** ``getCableLengthNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``float``

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getConvexAnalyzer()

   **Signature:** ``getConvexAnalyzer() -> ConvexHullAnalyzer``

   **Returns:** ``Any``

.. method:: getConvexHullMetric(arg0)

   **Signature:** ``getConvexHullMetric(String) -> double``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``float``

.. method:: getDepth()

   **Signature:** ``getDepth() -> double``

   **Returns:** ``float``

.. method:: getDescriptiveStats(arg0)

   **Signature:** ``getDescriptiveStats(String) -> DescriptiveStatistics``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getFlowPlot(arg0, arg1, arg2, arg3)

   **Signature:** ``getFlowPlot(String, int, double, boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``int``)
   * **arg2** (``float``)
   * **arg3** (``bool``)

   **Returns:** ``SNTChart``

.. method:: getFractalDimension()

   **Signature:** ``getFractalDimension() -> List``

   **Returns:** ``List[Any]``

.. method:: getHeight()

   **Signature:** ``getHeight() -> double``

   **Returns:** ``float``

.. method:: getHighestPathOrder()

   Gets the number of branches (paths) being analyzed.

Returns the total count of paths in this PathStatistics instance.

   **Signature:** ``getHighestPathOrder() -> int``

   **Returns:** (``int``) the number of paths

.. method:: getHistogram(arg0)

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``SNTChart``

.. method:: getInnerBranches()

   Gets the inner branches from the analyzed paths.

In PathStatistics, inner branches are equivalent to primary branches.

   **Signature:** ``getInnerBranches() -> List``

   **Returns:** (``List[Any]``) the list of inner branches (same as primary branches)

.. method:: getInnerLength()

   Gets the total length of inner branches.

In PathStatistics, this returns the same value as getPrimaryLength().

   **Signature:** ``getInnerLength() -> double``

   **Returns:** (``float``) the total length of inner branches

.. method:: getMetric(arg0)

   Gets a specific metric value for an individual path.

This method provides direct access to morphometric properties of individual paths, including geometric measurements, connectivity information, and structural characteristics. It supports all standard path metrics plus PathStatistics-specific measurements.

Supported metrics include:

Geometric: length, volume, surface area, mean radius Structural: number of nodes, branch points, children Angular: extension angles in XY, XZ, ZY planes Morphological: contraction, fractal dimension, spine density Metadata: path ID, channel, frame, order

   **Signature:** ``getMetric(String) -> Number``

   **Parameters:**

   * **arg0** (``str``): - the name of the metric to retrieve

   **Returns:** (``Union[int, float]``) the metric value for the specified path


PersistenceAnalyzer
-------------------

.. method:: getBarcode(arg0)

   Gets the persistence barcode for the specified filter function.

The barcode is a simplified representation of the persistence diagram that contains only the persistence values (death - birth) for each topological feature, akin to a one-dimensional summary of branch significance.

Interpretation:

High values: Morphologically significant branches Low values: Minor branches or potential noise Distribution: The spread of values indicates branching complexity

Special Properties:

All values are non-negative (|death - birth|) For geodesic descriptor: sum of all values equals total cable length Number of values equals number of tips in the tree

Example Usage: 
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

   * **arg0** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z".

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

.. method:: getDiagram(arg0)

   Gets the persistence diagram for the specified filter function.

The persistence diagram is the core output of the analysis, consisting of birth-death pairs that represent the "lifespan" of topological features (branches) during the filtration process. Each point in the diagram corresponds to a branch in the neuronal tree.

Structure: Returns a list where each inner list contains exactly two values:

Birth [0]: The filter value where the branch appears (branch point) Death [1]: The filter value where the branch disappears (tip)

Properties:

Number of points = Number of tips in the tree All values are non-negative For geodesic descriptor: sum of all (death-birth) = total cable length High persistence (death-birth) indicates morphologically significant branches

Example usage: 
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

   * **arg0** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z". Alternative names like "reverse strahler" for "centrifugal" are also accepted.

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

.. method:: getDiagramNodes(arg0)

   Gets the tree nodes associated with each point in the persistence diagram.

This method returns the actual SWCPoint nodes from the neuronal tree that correspond to each birth-death pair in the persistence diagram. This allows you to map topological features back to specific locations in the original morphology.

Structure: Returns a list where each inner list contains exactly two nodes:

Birth Node [0]: The branch point where the topological feature appears Death Node [1]: The tip node where the topological feature disappears

Correspondence: The order of node pairs matches the order of birth-death pairs returned by getDiagram(String), allowing direct correlation between topological features and their spatial locations.

Example Usage: 
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

   * **arg0** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z".

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

.. method:: getLandscape(arg0, arg1, arg2)

   Gets the persistence landscape as a vectorized representation.

Persistence landscapes transform persistence diagrams into a vector space representation that The landscape is a collection of piecewise-linear functions that capture the "shape" of the persistence diagram in a stable, vectorized format.

Mathematical Background: Each point (birth, death) in the persistence diagram contributes a "tent" function to the landscape. The k-th landscape function at any point is the k-th largest value among all tent functions at that point. This creates a stable, multi-resolution representation of the topological features.

Output Structure: Returns a 1D array of length `numLandscapes × resolution` where the first resolution values represent the first landscape function, the next resolution values represent the second landscape function, and so on.

   **Signature:** ``getLandscape(String, int, int) -> [D``

   **Parameters:**

   * **arg0** (``str``): - A descriptor for the filter function as per getDescriptors() (case-insensitive). Supported values: "geodesic", "radial", "centrifugal", "path order", "x", "y", "z".
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** (``Any``) the persistence landscape as a 1D array of length `numLandscapes × resolution`. All values are non-negative and scaled by √2 for proper L² normalization.


PointInImage
------------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the neuropil annotation assigned to this point

.. method:: getCoordinateOnAxis(arg0)

   Gets the coordinate along the specified axis.

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **arg0** (``int``): - the axis. Either Tree.X_AXIS, Tree.Y_AXIS, or Tree.Z_AXIS

   **Returns:** (``float``) the coordinate on the specified axis

.. method:: getHemisphere()

   **Signature:** ``getHemisphere() -> char``

   **Returns:** ``str``

.. method:: getPath()

   Returns the Path associated with this node (if any)

   **Signature:** ``getPath() -> Path``

   **Returns:** (``Path``) the path associated with this node or null if setPath(Path) has not been called.

.. method:: getUnscaledPoint(arg0)

   Converts the coordinates of this point into pixel units if this point is associated with a Path.

   **Signature:** ``getUnscaledPoint(int) -> PointInCanvas``

   **Parameters:**

   * **arg0** (``int``): - MultiDThreePanes.XY_PLANE, MultiDThreePanes.ZY_PLANE, etc.

   **Returns:** (``Any``) this point in pixel coordinates

.. method:: getX()

   **Signature:** ``getX() -> double``

   **Returns:** (``float``) the X-coordinate of the point

.. method:: getY()

   **Signature:** ``getY() -> double``

   **Returns:** (``float``) the Y-coordinate of the point

.. method:: getZ()

   **Signature:** ``getZ() -> double``

   **Returns:** (``float``) the Z-coordinate of the point

.. method:: isReal()

   **Signature:** ``isReal() -> boolean``

   **Returns:** ``bool``

.. method:: isSameLocation(arg0)

   **Signature:** ``isSameLocation(PointInImage) -> boolean``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``bool``


RemoteSWCLoader
---------------

.. method:: getReader(arg0)

   **Signature:** ``getReader(String) -> BufferedReader``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getReconstructionURL(arg0)

   **Signature:** ``getReconstructionURL(String) -> String``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``

.. method:: getTree(arg0)

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``)

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

.. method:: getHistogram(arg0)

   **Signature:** ``getHistogram(boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``SNTChart``

.. method:: getTaggedGraph()

   **Signature:** ``getTaggedGraph() -> DirectedWeightedGraph``

   **Returns:** (``DirectedWeightedGraph``) the graph of the tree being parsed. Vertices are tagged with the root angles (See: PointInImage.v).

.. method:: getTaggedTree(arg0, arg1, arg2)

   Returns a recolored copy of the analyzed tree with the root angles assigned to its node values.

   **Signature:** ``getTaggedTree(String, double, double) -> Tree``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``Tree``


SNT
---

.. method:: cancelPath()

   Cancels the temporary path.

   **Signature:** ``cancelPath() -> void``

   **Returns:** ``None``

.. method:: cancelSearch(arg0)

   **Signature:** ``cancelSearch(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: cancelTemporary()

   **Signature:** ``cancelTemporary() -> void``

   **Returns:** ``None``

.. method:: getAverageSeparation()

   **Signature:** ``getAverageSeparation() -> double``

   **Returns:** ``float``

.. method:: getChannel()

   **Signature:** ``getChannel() -> int``

   **Returns:** ``int``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getCostType()

   **Signature:** ``getCostType() -> SNT$CostType``

   **Returns:** ``Any``

.. method:: getCurrentPath()

   **Signature:** ``getCurrentPath() -> Path``

   **Returns:** ``Path``

.. method:: getDataset()

   **Signature:** ``getDataset() -> Dataset``

   **Returns:** ``Any``

.. method:: getDepth()

   **Signature:** ``getDepth() -> int``

   **Returns:** ``int``

.. method:: getDrawDiameters()

   **Signature:** ``getDrawDiameters() -> boolean``

   **Returns:** ``bool``

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

.. method:: getFilterType()

   **Signature:** ``getFilterType() -> SNT$FilterType``

   **Returns:** ``Any``

.. method:: getFrame()

   **Signature:** ``getFrame() -> int``

   **Returns:** ``int``

.. method:: getHeight()

   **Signature:** ``getHeight() -> int``

   **Returns:** ``int``

.. method:: getHeuristicType()

   **Signature:** ``getHeuristicType() -> SNT$HeuristicType``

   **Returns:** ``Any``

.. method:: getImagePlus()

   Gets the Image associated with a view pane.

   **Signature:** ``getImagePlus() -> ImagePlus``

   **Returns:** ``Any``

.. method:: getLoadedData()

   **Signature:** ``getLoadedData() -> RandomAccessibleInterval``

   **Returns:** ``Any``

.. method:: getLoadedDataAsImp()

   Retrieves the pixel data of the main image currently loaded in memory as an ImagePlus object. Returned image is always a single channel image.

   **Signature:** ``getLoadedDataAsImp() -> ImagePlus``

   **Returns:** (``Any``) the loaded data corresponding to the C,T position currently being traced, or null if no image data has been loaded into memory.

.. method:: getLoadedIterable()

   **Signature:** ``getLoadedIterable() -> IterableInterval``

   **Returns:** ``Any``


SNTColor
--------

.. method:: isTypeDefined()

   Checks if an SWC type has been defined.

   **Signature:** ``isTypeDefined() -> boolean``

   **Returns:** (``bool``) true, if an SWC integer flag has been specified


SNTPoint
--------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the neuropil annotation assigned to this point

.. method:: getCoordinateOnAxis(arg0)

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **arg0** (``int``)

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


SNTService
----------

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getIdentifier()

   **Signature:** ``getIdentifier() -> String``

   **Returns:** ``str``

.. method:: getInfo()

   **Signature:** ``getInfo() -> PluginInfo``

   **Returns:** ``Any``

.. method:: getInstance()

   Returns a reference to the active SNT instance.

   **Signature:** ``getInstance() -> SNT``

   **Returns:** (``Any``) the SNT instance

.. method:: getLocation()

   **Signature:** ``getLocation() -> String``

   **Returns:** ``str``

.. method:: getOrCreateSciViewSNT()

   **Signature:** ``getOrCreateSciViewSNT() -> SciViewSNT``

   **Returns:** ``Any``

.. method:: getPathAndFillManager()

   Returns the PathAndFillManager associated with the current SNT instance.

   **Signature:** ``getPathAndFillManager() -> PathAndFillManager``

   **Returns:** (``Any``) the PathAndFillManager instance

.. method:: getPaths()

   Gets the paths currently listed in the Path Manager

   **Signature:** ``getPaths() -> List``

   **Returns:** (``List[Any]``) all the listed paths, or null if the Path Manager is empty

.. method:: getPriority()

   **Signature:** ``getPriority() -> double``

   **Returns:** ``float``

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

.. method:: getStatistics(arg0)

   Returns a TreeStatistics instance constructed from current Paths.

   **Signature:** ``getStatistics(boolean) -> TreeStatistics``

   **Parameters:**

   * **arg0** (``bool``): - If true only selected paths will be considered

   **Returns:** (``TreeStatistics``) the TreeStatistics instance

.. method:: getTable()

   Returns a reference to SNT's main table of measurements.

   **Signature:** ``getTable() -> SNTTable``

   **Returns:** (``SNTTable``) SNT measurements table (a DefaultGenericTable)

.. method:: getTree()

   Gets the collection of paths listed in the Path Manager as a Tree object.

   **Signature:** ``getTree() -> Tree``

   **Returns:** (``Tree``) the Tree holding the Path collection

.. method:: getTrees()

   Gets the collection of paths listed in the Path Manager as a Tree object.

   **Signature:** ``getTrees() -> Collection``

   **Returns:** (``List[Any]``) the Tree holding the Path collection

.. method:: getUI()

   Returns a reference to SNT's UI.

   **Signature:** ``getUI() -> SNTUI``

   **Returns:** (``Any``) the SNTUI window, or null if SNT is not running, or is running without GUI

.. method:: getVersion()

   **Signature:** ``getVersion() -> String``

   **Returns:** ``str``

.. method:: isActive()

   Gets whether SNT is running.

   **Signature:** ``isActive() -> boolean``

   **Returns:** (``bool``) true if this SNTService is active, tied to the active instance of SNT


SNTTable
--------

.. method:: getColumnCount()

   **Signature:** ``getColumnCount() -> int``

   **Returns:** ``int``

.. method:: getColumnHeader(arg0)

   **Signature:** ``getColumnHeader(int) -> String``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``str``

.. method:: getColumnIndex(arg0)

   **Signature:** ``getColumnIndex(String) -> int``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``int``

.. method:: getFirst()

   **Signature:** ``getFirst() -> Object``

   **Returns:** ``Any``

.. method:: getLast()

   **Signature:** ``getLast() -> Object``

   **Returns:** ``Any``

.. method:: getRowCount()

   **Signature:** ``getRowCount() -> int``

   **Returns:** ``int``

.. method:: getRowHeader(arg0)

   **Signature:** ``getRowHeader(int) -> String``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``str``

.. method:: getRowIndex(arg0)

   **Signature:** ``getRowIndex(String) -> int``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``int``

.. method:: getSummaryRow()

   **Signature:** ``getSummaryRow() -> int``

   **Returns:** ``int``


SWCPoint
--------

.. method:: getAnnotation()

   **Signature:** ``getAnnotation() -> BrainAnnotation``

   **Returns:** (``Any``) the neuropil annotation assigned to this point

.. method:: getColor()

   Gets the color of this point.

   **Signature:** ``getColor() -> Color``

   **Returns:** (``Any``) the color

.. method:: getCoordinateOnAxis(arg0)

   **Signature:** ``getCoordinateOnAxis(int) -> double``

   **Parameters:**

   * **arg0** (``int``)

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

.. method:: getUnscaledPoint(arg0)

   **Signature:** ``getUnscaledPoint(int) -> PointInCanvas``

   **Parameters:**

   * **arg0** (``int``)

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

.. method:: isReal()

   **Signature:** ``isReal() -> boolean``

   **Returns:** ``bool``

.. method:: isSameLocation(arg0)

   **Signature:** ``isSameLocation(PointInImage) -> boolean``

   **Parameters:**

   * **arg0** (``PointInImage``)

   **Returns:** ``bool``


SciViewSNT
----------

.. method:: getSciView()

   Gets the SciView instance currently in use.

   **Signature:** ``getSciView() -> SciView``

   **Returns:** (``Any``) the SciView instance. It is never null: A new instance is created if none has been specified

.. method:: getTreeAsSceneryNode(arg0)

   Gets the specified Tree as a Scenery Node.

   **Signature:** ``getTreeAsSceneryNode(Tree) -> Node``

   **Parameters:**

   * **arg0** (``Tree``): - the tree previously added to SciView using addTree(Tree)

   **Returns:** (``Any``) the scenery Node


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

   **Returns:** ``Any``

.. method:: getNodesAsImageFromStart()

   **Signature:** ``getNodesAsImageFromStart() -> SearchImageStack``

   **Returns:** ``Any``

.. method:: getResult()

   **Signature:** ``getResult() -> Path``

   **Returns:** ``Path``


ShollAnalyzer
-------------

.. method:: getLinearStats()

   Gets the LinearProfileStats associated with this analyzer. By default, it is set to determine the polynomial of 'best-fit' (2-20 degree range.)

   **Signature:** ``getLinearStats() -> LinearProfileStats``

   **Returns:** (``Any``) the LinearProfileStats instance

.. method:: getMaximaRadii()

   **Signature:** ``getMaximaRadii() -> ArrayList``

   **Returns:** ``List[Any]``

.. method:: getNormStats()

   Gets the `NormalizedProfileStats` associated with this analyzer. By default it is set to determine the regression method of 'best-fit' (log-log or semi-log) using shell volume as normalizer (if Tree has a depth component) or shell area if Tree is 2D.

   **Signature:** ``getNormStats() -> NormalizedProfileStats``

   **Returns:** (``Any``) the LinearProfileStats instance

.. method:: getSecondaryMaxima()

   **Signature:** ``getSecondaryMaxima() -> ArrayList``

   **Returns:** ``List[Any]``

.. method:: getSingleValueMetrics()

   **Signature:** ``getSingleValueMetrics() -> Map``

   **Returns:** ``Dict[str, Any]``


SkeletonConverter
-----------------

.. method:: getGraphs()

   Generates a list of `DirectedWeightedGraph`s from the skeleton image. Each graph corresponds to one connected component of the graph returned by `SkeletonResult.getGraph()`.

   **Signature:** ``getGraphs() -> List``

   **Returns:** (``List[Any]``) the list of skeletonized graphs

.. method:: getPruneMode()

   Gets the loop pruning strategy.

   **Signature:** ``getPruneMode() -> int``

   **Returns:** ``int``

.. method:: getRootRoiStrategy()

   Gets the current root ROI strategy.

Returns the strategy used for handling root ROIs during skeleton conversion. If no root ROI is set, returns ROI_UNSET.

   **Signature:** ``getRootRoiStrategy() -> int``

   **Returns:** (``int``) the root ROI strategy constant

.. method:: getSingleGraph()

   Generates a single `DirectedWeightedGraph`s by combining getGraphs()'s list into a single, combined graph. Typically, this method assumes that the skeletonization handles a known single component (e.g., an image of a single cell). If multiple graphs() do exist, this method requires that setRootRoi(Roi, int) has been called using ROI_CENTROID or `ROI_CENTROID_WEIGHTED`.

   **Signature:** ``getSingleGraph() -> DirectedWeightedGraph``

   **Returns:** (``DirectedWeightedGraph``) the single graph

.. method:: getSingleTree()

   Generates a single Tree from getSingleGraph(). If a ROI-based centroid has been set, Root is converted to a single node, root path with radius set to that of a circle with the same area of root-defining soma.

   **Signature:** ``getSingleTree() -> Tree``

   **Returns:** (``Tree``) the single tree

.. method:: getTrees()

   Generates a list of Trees from the skeleton image. Each Tree corresponds to one connected component of the graph returned by `SkeletonResult.getGraph()`.

   **Signature:** ``getTrees() -> List``

   **Returns:** (``List[Any]``) the skeleton tree list

.. method:: setPruneByLength(arg0)

   Sets whether to prune components below a threshold length from the result.

   **Signature:** ``setPruneByLength(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``


StrahlerAnalyzer
----------------

.. method:: getAvgBifurcationRatio()

   **Signature:** ``getAvgBifurcationRatio() -> double``

   **Returns:** (``float``) the average bifurcation ratio of the parsed tree. In a complete binary tree, the bifurcation ratio is 2.

.. method:: getAvgContractions()

   **Signature:** ``getAvgContractions() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getAvgExtensionAngle(arg0, arg1)

   Gets the average relative extension angle for branches of a specific Strahler order.

   **Signature:** ``getAvgExtensionAngle(boolean, int) -> double``

   **Parameters:**

   * **arg0** (``bool``): - the Strahler order
   * **arg1** (``int``)

   **Returns:** (``float``) the average relative extension angle in degrees, or Double.NaN if no valid angles

.. method:: getAvgExtensionAngles(arg0)

   Gets a map of average relative extension angles for all Strahler orders.

   **Signature:** ``getAvgExtensionAngles(boolean) -> Map``

   **Parameters:**

   * **arg0** (``bool``)

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

.. method:: getBranches(arg0)

   **Signature:** ``getBranches(int) -> List``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``List[Any]``

.. method:: getExtensionAngles(arg0)

   Gets a map of relative extension angles for all branches in each Strahler order.

   **Signature:** ``getExtensionAngles(boolean) -> Map``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** (``Dict[str, Any]``) map with Strahler order as key and list of relative extension angles as values

.. method:: getGraph()

   **Signature:** ``getGraph() -> DirectedWeightedGraph``

   **Returns:** (``DirectedWeightedGraph``) the graph of the tree being parsed.

.. method:: getHighestBranchOrder()

   **Signature:** ``getHighestBranchOrder() -> int``

   **Returns:** (``int``) the highest Horton-Strahler number associated with a branch in the parsed tree. Either getRootNumber() or getRootNumber()-1.

.. method:: getLengths()

   **Signature:** ``getLengths() -> Map``

   **Returns:** (``Dict[str, Any]``) the map containing the cable lengh associated to each order ( Horton-Strahler numbers as key and cable length as value).

.. method:: getRelativeExtensionAngle(arg0)

   Computes the relative extension angle for a StrahlerAnalyzer branch by finding the parent direction from the graph structure.

   **Signature:** ``getRelativeExtensionAngle(Path) -> double``

   **Parameters:**

   * **arg0** (``Path``): - the branch path to analyze

   **Returns:** (``float``) the relative extension angle in degrees (0-180°), or Double.NaN if computation fails

.. method:: getRootAssociatedBranches()

   **Signature:** ``getRootAssociatedBranches() -> List``

   **Returns:** ``List[Any]``

.. method:: getRootNumber()

   **Signature:** ``getRootNumber() -> int``

   **Returns:** (``int``) the highest Horton-Strahler number in the parsed tree.


TracerCanvas
------------

.. method:: getAccessibleContext()

   **Signature:** ``getAccessibleContext() -> AccessibleContext``

   **Returns:** ``Any``

.. method:: getAlignmentX()

   **Signature:** ``getAlignmentX() -> float``

   **Returns:** ``float``

.. method:: getAlignmentY()

   **Signature:** ``getAlignmentY() -> float``

   **Returns:** ``float``

.. method:: getAnnotationsColor()

   **Signature:** ``getAnnotationsColor() -> Color``

   **Returns:** ``Any``

.. method:: getBackground()

   **Signature:** ``getBackground() -> Color``

   **Returns:** ``Any``

.. method:: getBaseline(arg0, arg1)

   **Signature:** ``getBaseline(int, int) -> int``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``int``)

   **Returns:** ``int``


TracerThread
------------

.. method:: getExitReason()

   **Signature:** ``getExitReason() -> int``

   **Returns:** ``int``

.. method:: getNodesAsImageFromGoal()

   **Signature:** ``getNodesAsImageFromGoal() -> SearchImageStack``

   **Returns:** ``Any``

.. method:: getNodesAsImageFromStart()

   **Signature:** ``getNodesAsImageFromStart() -> SearchImageStack``

   **Returns:** ``Any``

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

.. method:: getImpContainer(arg0, arg1)

   Gets an empty image capable of holding the skeletonized version of this tree.

   **Signature:** ``getImpContainer(int, int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``int``): - the pane flag indicating the SNT view for this image e.g., MultiDThreePanes.XY_PLANE
   * **arg1** (``int``)

   **Returns:** (``Any``) the empty ImagePlus container

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

   **Signature:** ``getRoot() -> PointInImage``

   **Returns:** (``PointInImage``) the root node, or null if the main primary path is undefined for this tree.

.. method:: getSWCTypeNames(arg0)

   Gets the set of SWC type labels present in this tree with optional soma inclusion in a readable form.

   **Signature:** ``getSWCTypeNames(boolean) -> Set``

   **Parameters:**

   * **arg0** (``bool``): - if true, includes soma in the returned set; if false, excludes Path.SWC_SOMA from the result

   **Returns:** (``Set[Any]``) a Set containing the SWC type labels (e.g., Path.SWC_AXON_LABEL, `Path.SWC_DENDRITE_LABEL`, etc.) present in the tree

.. method:: getSWCTypes()

   Gets the set of SWC types present in this tree with optional soma inclusion.

   **Signature:** ``getSWCTypes() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getSkeleton(arg0)

   Retrieves the rasterized skeleton of this tree at 1:1 scaling.

   **Signature:** ``getSkeleton(int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``int``): - the voxel intensities of the skeleton. If

   **Returns:** (``Any``) the skeletonized 16-bit binary image

.. method:: getSkeleton2D(arg0)

   Retrieves a 2D projection of the rasterized skeleton of this tree at 1:1 scaling.

   **Signature:** ``getSkeleton2D(int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``int``): - the pixel intensities of the skeleton. If

   **Returns:** (``Any``) the skeletonized 16-bit binary image

.. method:: getSomaNodes()

   Gets the list of all nodes tagged as Path.SWC_SOMA.

   **Signature:** ``getSomaNodes() -> List``

   **Returns:** (``List[Any]``) the soma nodes or null if no Paths are tagged as soma.

.. method:: getTips()

   Gets the end points (tips) of the graph. This is simply an alias for `DirectedWeightedGraph.getTips()`.

   **Signature:** ``getTips() -> List``

   **Returns:** (``List[Any]``) the list of end points

.. method:: isAnnotated()

   Checks if the nodes of this Tree have been assigned BrainAnnotations (neuropil labels).

   **Signature:** ``isAnnotated() -> boolean``

   **Returns:** (``bool``) true if at least one node in the Tree has a valid annotation, false otherwise

.. method:: isEmpty()

   Checks if this Tree is empty.

   **Signature:** ``isEmpty() -> boolean``

   **Returns:** (``bool``) true if this tree contains no Paths, false otherwise


TreeColorMapper
---------------

.. method:: getAvailableLuts()

   Gets the available LUTs.

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** (``Set[Any]``) the set of keys, corresponding to the set of LUTs available

.. method:: getColor(arg0)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(arg0)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable(arg0)

   **Signature:** ``getColorTable(String) -> ColorTable``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getMinMax()

   **Signature:** ``getMinMax() -> [D``

   **Returns:** ``Any``

.. method:: getMultiViewer()

   Assembles a Multi-pane viewer using all the Trees mapped so far.

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


TreeStatistics
--------------

.. method:: cancel(arg0)

   Sets the table for this TreeStatistics instance.

   **Signature:** ``cancel(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - the table to be used by this TreeStatistics instance

   **Returns:** ``None``

.. method:: getAnnotatedLength(arg0, arg1)

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron.

   **Signature:** ``getAnnotatedLength(int, String) -> Map``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: getAnnotatedLengthHistogram()

   Retrieves the histogram of cable length frequencies across brain areas of the specified ontology level across the specified hemisphere.

   **Signature:** ``getAnnotatedLengthHistogram() -> SNTChart``

   **Returns:** ``SNTChart``

.. method:: getAnnotatedLengthsByHemisphere(arg0)

   Retrieves the amount of cable length present on each brain compartment innervated by the analyzed neuron in the two brain hemispheres. Lengths are absolute and not normalized to the cells' cable length.

   **Signature:** ``getAnnotatedLengthsByHemisphere(int) -> Map``

   **Parameters:**

   * **arg0** (``int``): - the ontological depth of the compartments to be considered

   **Returns:** (``Dict[str, Any]``) the map containing the brain compartments as keys, and cable lengths per hemisphere as values.

.. method:: getAnnotations(arg0)

   Retrieves the brain compartments (neuropil labels) associated with the Tree being measured innervated by the analyzed neuron.

   **Signature:** ``getAnnotations(int) -> Set``

   **Parameters:**

   * **arg0** (``int``): - the max. ontological depth of the compartments to be retrieved

   **Returns:** (``Set[Any]``) the set of brain compartments (BrainAnnotations)

.. method:: getAvgBranchLength()

   Gets average length for all the branches of the analyzed tree.

   **Signature:** ``getAvgBranchLength() -> double``

   **Returns:** (``float``) the average branch length

.. method:: getAvgContraction()

   Gets average contraction for all the branches of the analyzed tree.

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

.. method:: getBranchPoints(arg0, arg1)

   Gets the position of all the branch points in the analyzed tree associated with the specified annotation.

   **Signature:** ``getBranchPoints(BrainAnnotation, boolean) -> Set``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``Set[Any]``

.. method:: getBranches()

   Gets all the branches in the analyzed tree. A branch is defined as the Path composed of all the nodes between two branching points or between one branching point and a termination point.

   **Signature:** ``getBranches() -> List``

   **Returns:** (``List[Any]``) the list of branches as Path objects.

.. method:: getCableLength()

   Gets the cable length associated with the specified compartment (neuropil label).

   **Signature:** ``getCableLength() -> double``

   **Returns:** ``float``

.. method:: getCableLengthNorm(arg0)

   Gets the cable length associated with the specified compartment (neuropil label) as a ratio of total length.

   **Signature:** ``getCableLengthNorm(BrainAnnotation) -> double``

   **Parameters:**

   * **arg0** (``Any``): - the query compartment (null not allowed)

   **Returns:** (``float``) the filtered cable length normalized to total cable length

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getConvexAnalyzer()

   Gets the ConvexHullAnalyzer instance associated with this TreeStatistics instance.

   **Signature:** ``getConvexAnalyzer() -> ConvexHullAnalyzer``

   **Returns:** (``Any``) the ConvexHullAnalyzer instance

.. method:: getConvexHullMetric(arg0)

   Convenience method to obtain a single-value metric from ConvexHullAnalyzer

   **Signature:** ``getConvexHullMetric(String) -> double``

   **Parameters:**

   * **arg0** (``str``): - the metric to be retrieved, one of ConvexHullAnalyzer.supportedMetrics()

   **Returns:** (``float``) the convex hull metric

.. method:: getDepth()

   Returns the depth of the BoundingBox box of the tree being measured

   **Signature:** ``getDepth() -> double``

   **Returns:** (``float``) the bounding box depth

.. method:: getDescriptiveStats(arg0)

   Computes the `DescriptiveStatistics` for the specified measurement.

   **Signature:** ``getDescriptiveStats(String) -> DescriptiveStatistics``

   **Parameters:**

   * **arg0** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``Any``) the DescriptiveStatistics object.

.. method:: getFlowPlot(arg0, arg1, arg2, arg3)

   Assembles a Flow plot (aka Sankey diagram) for the specified feature.

   **Signature:** ``getFlowPlot(String, int, double, boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``int``)
   * **arg2** (``float``)
   * **arg3** (``bool``)

   **Returns:** ``SNTChart``

.. method:: getFractalDimension()

   Gets the fractal dimension of each branch in the analyzed tree. Note that branches with less than 5 points are ignored.

   **Signature:** ``getFractalDimension() -> List``

   **Returns:** (``List[Any]``) a list containing the fractal dimension of each branch

.. method:: getHeight()

   Returns the height of the BoundingBox box of the tree being measured

   **Signature:** ``getHeight() -> double``

   **Returns:** (``float``) the bounding box height

.. method:: getHighestPathOrder()

   Gets the highest path order of the analyzed tree

   **Signature:** ``getHighestPathOrder() -> int``

   **Returns:** (``int``) the highest Path order, or -1 if Paths in the Tree have no defined order

.. method:: getHistogram(arg0)

   Retrieves the histogram of relative frequencies histogram for a univariate measurement. The number of bins is determined using the Freedman-Diaconis rule.

   **Signature:** ``getHistogram(String) -> SNTChart``

   **Parameters:**

   * **arg0** (``str``): - the measurement (N_NODES, NODE_RADIUS, etc.)

   **Returns:** (``SNTChart``) the frame holding the histogram

.. method:: getInnerBranches()

   Retrieves the branches of highest Strahler order in the Tree. This typically correspond to the most 'internal' branches of the Tree in direct sequence from the root.

   **Signature:** ``getInnerBranches() -> List``

   **Returns:** (``List[Any]``) the list containing the "inner" branches. Note that these branches (Path segments) will not carry any connectivity information.

.. method:: getInnerLength()

   Gets the cable length of inner branches

   **Signature:** ``getInnerLength() -> double``

   **Returns:** (``float``) the length sum of all inner branches

.. method:: getMetric(arg0)

   Computes the specified metric.

   **Signature:** ``getMetric(String) -> Number``

   **Parameters:**

   * **arg0** (``str``): - the single-value metric to be computed (case-insensitive). While it is expected to be an element of getAllMetrics(), if isExactMetricMatch() is set,

   **Returns:** (``Union[int, float]``) the computed value (average if metric is associated with multiple values)

.. method:: getNBranchPoints(arg0, arg1)

   Gets the number of branch points in the analyzed tree associated with the specified annotation.

   **Signature:** ``getNBranchPoints(BrainAnnotation, boolean) -> int``

   **Parameters:**

   * **arg0** (``Any``): - the BrainAnnotation to be queried.
   * **arg1** (``bool``)

   **Returns:** (``int``) the number of branch points


Viewer2D
--------

.. method:: getAvailableLuts()

   **Signature:** ``getAvailableLuts() -> Set``

   **Returns:** ``Set[Any]``

.. method:: getChart()

   Gets the current viewer as a SNTChart object

   **Signature:** ``getChart() -> SNTChart``

   **Returns:** (``SNTChart``) the converted viewer

.. method:: getColor(arg0)

   **Signature:** ``getColor(double) -> Color``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorRGB(arg0)

   **Signature:** ``getColorRGB(double) -> ColorRGB``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``Any``

.. method:: getColorTable(arg0)

   **Signature:** ``getColorTable(String) -> ColorTable``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getJFreeChart()

   Gets the current viewer as a JFreeChart object

   **Signature:** ``getJFreeChart() -> JFreeChart``

   **Returns:** (``Any``) the converted viewer

.. method:: getMinMax()

   **Signature:** ``getMinMax() -> [D``

   **Returns:** ``Any``

.. method:: getMultiViewer()

   **Signature:** ``getMultiViewer() -> MultiViewer2D``

   **Returns:** ``MultiViewer2D``

.. method:: getNaNColor()

   **Signature:** ``getNaNColor() -> Color``

   **Returns:** ``Any``

.. method:: getPlot()

   Gets the current plot as a XYPlot object

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

.. method:: setPreferredSize(arg0, arg1)

   Sets the preferred size of the plot to a constant value.

   **Signature:** ``setPreferredSize(int, int) -> void``

   **Parameters:**

   * **arg0** (``int``): - the preferred width
   * **arg1** (``int``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: getAnnotation(arg0)

   Gets the annotation associated with the specified label.

   **Signature:** ``getAnnotation(String) -> Annotation3D``

   **Parameters:**

   * **arg0** (``str``): - the (unique) label as displayed in Viewer's list

   **Returns:** (``Any``) the annotation or null if no annotation is associated with the specified label

.. method:: getAnnotations()

   Returns all annotations added to this viewer.

   **Signature:** ``getAnnotations() -> List``

   **Returns:** (``List[Any]``) the annotation list

.. method:: getFrame(arg0)

   Gets the frame containing this viewer, optionally controlling its visibility.

Returns the AWT Frame that contains this viewer's 3D canvas and UI components. If no frame exists, one will be created with the specified visibility setting. This method is useful when you need to control whether the viewer window appears immediately or remains hidden for programmatic manipulation.

   **Signature:** ``getFrame(boolean) -> Frame``

   **Parameters:**

   * **arg0** (``bool``): - whether the frame should be visible when created

   **Returns:** (``Any``) the frame containing the viewer

.. method:: getID()

   Returns this Viewer's id.

   **Signature:** ``getID() -> int``

   **Returns:** (``int``) this Viewer's unique numeric ID.

.. method:: getManagerPanel()

   Returns a reference to 'RV Controls' panel.

   **Signature:** ``getManagerPanel() -> Viewer3D$ManagerPanel``

   **Returns:** (``Any``) the ManagerPanel associated with this Viewer, or null if the 'RV Controls' dialog is not being displayed.

.. method:: getMesh(arg0)

   Gets the mesh associated with the specified label.

   **Signature:** ``getMesh(String) -> OBJMesh``

   **Parameters:**

   * **arg0** (``str``): - the (unique) label as displayed in Viewer's list

   **Returns:** (``Any``) the mesh or null if no mesh is associated with the specified label

.. method:: getMeshes(arg0)

   Returns all meshes added to this viewer.

   **Signature:** ``getMeshes(boolean) -> List``

   **Parameters:**

   * **arg0** (``bool``): - If true, only visible meshes are retrieved.

   **Returns:** (``List[Any]``) the mesh list

.. method:: getRecorder(arg0)

   Gets the script recorder for this viewer, optionally creating one if needed.

   **Signature:** ``getRecorder(boolean) -> ScriptRecorder``

   **Parameters:**

   * **arg0** (``bool``): - if true, creates a new recorder if one doesn't exist; if false, returns null when no recorder exists

   **Returns:** (``Any``) the ScriptRecorder instance, or null if none exists and createIfNeeded is false

.. method:: getTree(arg0)

   Gets the tree associated with the specified label.

   **Signature:** ``getTree(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - the (unique) label as displayed in Viewer's list

   **Returns:** (``Tree``) the Tree or null if no Tree is associated with the specified label

.. method:: getTrees(arg0)

   Returns all trees added to this viewer.

   **Signature:** ``getTrees(boolean) -> List``

   **Parameters:**

   * **arg0** (``bool``): - If true, only visible Trees are retrieved.

   **Returns:** (``List[Any]``) the Tree list

.. method:: isActive()

   Checks whether this instance is currently active

   **Signature:** ``isActive() -> boolean``

   **Returns:** (``bool``) true, if active, false otherwise

.. method:: isDarkModeOn()

   Checks if scene is being rendered under dark or light background.

   **Signature:** ``isDarkModeOn() -> boolean``

   **Returns:** (``bool``) true, if "Dark Mode" is active

.. method:: isSNTInstance()

   Checks whether this instance is SNT's Reconstruction Viewer.

   **Signature:** ``isSNTInstance() -> boolean``

   **Returns:** (``bool``) true, if SNT instance, false otherwise

.. method:: isSplitDendritesFromAxons()

   Checks whether axons and dendrites of imported Trees are set to be imported as separated objects.

   **Signature:** ``isSplitDendritesFromAxons() -> boolean``

   **Returns:** (``bool``) if imported trees are set to be split into axonal and dendritic subtrees.


WekaModelLoader
---------------

.. method:: cancel()

   **Signature:** ``cancel() -> void``

   **Returns:** ``None``

.. method:: getCancelReason()

   **Signature:** ``getCancelReason() -> String``

   **Returns:** ``str``

.. method:: getContext()

   **Signature:** ``getContext() -> Context``

   **Returns:** ``Any``

.. method:: getDelegateObject()

   **Signature:** ``getDelegateObject() -> Object``

   **Returns:** ``Any``

.. method:: getInfo()

   **Signature:** ``getInfo() -> ModuleInfo``

   **Returns:** ``Any``

.. method:: getInput(arg0)

   **Signature:** ``getInput(String) -> Object``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getInputs()

   **Signature:** ``getInputs() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: getOutput(arg0)

   **Signature:** ``getOutput(String) -> Object``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``

.. method:: getOutputs()

   **Signature:** ``getOutputs() -> Map``

   **Returns:** ``Dict[str, Any]``

.. method:: isCanceled()

   **Signature:** ``isCanceled() -> boolean``

   **Returns:** ``bool``

.. method:: isInputResolved(arg0)

   **Signature:** ``isInputResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: isOutputResolved(arg0)

   **Signature:** ``isOutputResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: isResolved(arg0)

   **Signature:** ``isResolved(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``


----

*Category index generated on 2025-11-13 22:40:29*