Static Methods Methods
======================

Static utility methods that can be called without object instances.

Total methods in this category: **195**

.. contents:: Classes in this Category
   :local:

AllenCompartment
----------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


AllenUtils
----------

.. method:: static assignAnnotationsFromNodeValues(arg0)

   Assigns brain annotations (interpreted as CCF IDs) to node values for all paths in a Tree.

This method is the inverse operation of `transferAnnotationIdsToNodeValues(Tree)`.

   **Signature:** ``static assignAnnotationsFromNodeValues(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree containing paths with node values to be converted to annotations. Must not be null. Paths without node values are skipped. Invalid node values result in null annotations.

   **Returns:** ``None``

.. method:: static assignHemisphereTags(arg0)

   **Signature:** ``static assignHemisphereTags(DirectedWeightedGraph) -> void``

   **Parameters:**

   * **arg0** (``DirectedWeightedGraph``)

   **Returns:** ``None``

.. method:: static assignToLeftHemisphere(arg0)

   Assigns a tree to the left hemisphere by mirroring it if necessary.

   **Signature:** ``static assignToLeftHemisphere(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the tree to assign to the left hemisphere

   **Returns:** ``None``

.. method:: static assignToRightHemisphere(arg0)

   Assigns a tree to the right hemisphere by mirroring it if necessary.

   **Signature:** ``static assignToRightHemisphere(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the tree to assign to the right hemisphere

   **Returns:** ``None``

.. method:: static brainCenter()

   Returns the spatial centroid of the Allen CCF.

   **Signature:** ``static brainCenter() -> SNTPoint``

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of the ARA

.. method:: static getAnatomicalPlane(arg0)

   Retrieves the anatomical plane matching the specified cartesian plane.

   **Signature:** ``static getAnatomicalPlane(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - either "xy", "yz", or "xz"

   **Returns:** (``str``) the cartesian plane. Either "coronal", "sagittal", "transverse", or null if cartesianPlane was not recognized.

.. method:: static getAxisDefiningSagittalPlane()

   Gets the axis defining the sagittal plane.

   **Signature:** ``static getAxisDefiningSagittalPlane() -> int``

   **Returns:** (``int``) the axis defining the sagittal plane where X=0; Y=1; Z=2;

.. method:: static getCartesianPlane(arg0)

   Retrieves the Cartesian plane matching the specified anatomical plane.

   **Signature:** ``static getCartesianPlane(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - either "sagittal", "coronal", or "transverse"

   **Returns:** (``str``) the cartesian plane. Either "xy", "yz", "xz", or null if anatomicalPlane was not recognized.

.. method:: static getCompartment(arg0)

   Constructs a compartment from its CCF name or acronym

   **Signature:** ``static getCompartment(String) -> AllenCompartment``

   **Parameters:**

   * **arg0** (``str``): - the name or acronym (case-insensitive) identifying the compartment

   **Returns:** (``Any``) the compartment whose name or acronym matches the specified string or null if no match was found

.. method:: static getHemisphere(arg0)

   Checks the hemisphere a neuron belongs to.

   **Signature:** ``static getHemisphere(Tree) -> String``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree to be tested

   **Returns:** (``str``) the hemisphere label: either "left", or "right"

.. method:: static getHighestOntologyDepth()

   Gets the maximum number of ontology levels in the Allen CCF.

   **Signature:** ``static getHighestOntologyDepth() -> int``

   **Returns:** (``int``) the max number of ontology levels.

.. method:: static getOntologies()

   Gets a flat (non-hierarchical) list of all the compartments of the specified ontology depth.

   **Signature:** ``static getOntologies() -> List``

   **Returns:** ``List[Any]``

.. method:: static getRootMesh(arg0)

   Retrieves the surface contours for the Allen Mouse Brain Atlas (CCF), bundled with SNT.

   **Signature:** ``static getRootMesh(ColorRGB) -> OBJMesh``

   **Parameters:**

   * **arg0** (``Any``): - the color to be assigned to the mesh

   **Returns:** (``Any``) a reference to the retrieved mesh

.. method:: static getTreeModel(arg0)

   Retrieves the Allen CCF hierarchical tree data.

   **Signature:** ``static getTreeModel(boolean) -> DefaultTreeModel``

   **Parameters:**

   * **arg0** (``bool``): - Whether only compartments with known meshes should be included

   **Returns:** (``Any``) the Allen CCF tree data model

.. method:: static getXYZLabels()

   **Signature:** ``static getXYZLabels() -> String;``

   **Returns:** (``Any``) the anatomical descriptions associated with the Cartesian X,Y,Z axes

.. method:: static isLeftHemisphere(arg0, arg1, arg2)

   **Signature:** ``static isLeftHemisphere(double, double, double) -> boolean``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``bool``

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static splitByHemisphere(arg0)

   **Signature:** ``static splitByHemisphere(DirectedWeightedGraph) -> List``

   **Parameters:**

   * **arg0** (``DirectedWeightedGraph``)

   **Returns:** ``List[Any]``

.. method:: static transferAnnotationIdsToNodeValues(arg0)

   Transfers brain annotation IDs to node values for all paths in a Tree.

This is useful for preserving annotation information when saving data to TRACES files. Note that this method overwrites any existing node values. Nodes without annotations (null) are assigned BRAIN_ROOT_ID.

   **Signature:** ``static transferAnnotationIdsToNodeValues(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree containing paths with brain annotations to be transferred. Must not be null and must contain valid annotations.

   **Returns:** ``None``


Annotation3D
------------

.. method:: static meshToDrawable(arg0)

   **Signature:** ``static meshToDrawable(Mesh) -> Drawable``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``


ColorMaps
---------

.. method:: static applyPlasma(arg0, arg1, arg2)

   Applies the "plasma" colormap to the specified (non-RGB) image

   **Signature:** ``static applyPlasma(ImagePlus, int, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``bool``)

   **Returns:** ``None``

.. method:: static applyViridis(arg0, arg1, arg2)

   Applies the "viridis" colormap to the specified (non-RGB) image

   **Signature:** ``static applyViridis(ImagePlus, int, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``bool``)

   **Returns:** ``None``

.. method:: static get(arg0)

   Returns a 'core' color table from its title

   **Signature:** ``static get(String) -> ColorTable``

   **Parameters:**

   * **arg0** (``str``): - the color table name (e.g., "fire", "viridis", etc)

   **Returns:** (``Any``) the color table


ConvexHull2D
------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


ConvexHull3D
------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


ConvexHullAnalyzer
------------------

.. method:: static main(arg0)

   Main method for testing and demonstration purposes.

Creates a ConvexHullAnalyzer instance using demo data and runs the analysis. This method is primarily used for development and debugging.

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``): - command line arguments (not used)

   **Returns:** ``None``


CrossoverFinder
---------------

.. method:: static find(arg0, arg1)

   Entry point: detect crossover events for a collection of paths using the given config.

   **Signature:** ``static find(Collection, CrossoverFinder$Config) -> List``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of paths
   * **arg1** (``Any``)

   **Returns:** ``List[Any]``


FillerThread
------------

.. method:: static fromFill(arg0, arg1, arg2, arg3)

   **Signature:** ``static fromFill(RandomAccessibleInterval, Calibration, ImageStatistics, Fill) -> FillerThread``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``Any``)

   **Returns:** ``FillerThread``


FlyCircuitLoader
----------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


Frangi
------

.. method:: static apply(arg0, arg1, arg2, arg3)

   **Signature:** ``static apply(ImgPlus, [D, double, int) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``float``)
   * **arg3** (``int``)

   **Returns:** ``Any``


GroupedTreeStatistics
---------------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


ImgUtils
--------

.. method:: static createIntervals(arg0, arg1)

   Partition the source dimensions into a list of Intervals with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have slightly different dimensions.

   **Signature:** ``static createIntervals([J, [J) -> List``

   **Parameters:**

   * **arg0** (``Any``): - the source dimensions
   * **arg1** (``Any``)

   **Returns:** (``List[Any]``) the list of Intervals

.. method:: static crop(arg0, arg1, arg2, arg3)

   **Signature:** ``static crop(ImgPlus, [J, [J, boolean) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``bool``)

   **Returns:** ``Any``

.. method:: static dropSingletonDimensions(arg0)

   **Signature:** ``static dropSingletonDimensions(ImgPlus) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static findSpatialAxisIndices(arg0)

   **Signature:** ``static findSpatialAxisIndices(ImgPlus) -> [I``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static findSpatialAxisIndicesWithFallback(arg0)

   **Signature:** ``static findSpatialAxisIndicesWithFallback(ImgPlus) -> [I``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static getCalibration(arg0)

   **Signature:** ``static getCalibration(ImgPlus) -> Calibration``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static getCtSlice(arg0, arg1, arg2)

   **Signature:** ``static getCtSlice(Dataset, int, int) -> RandomAccessibleInterval``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``Any``

.. method:: static getCtSlice3d(arg0, arg1, arg2)

   Get a view of the ImagePlus at the specified channel and frame.

   **Signature:** ``static getCtSlice3d(ImagePlus, int, int) -> RandomAccessibleInterval``

   **Parameters:**

   * **arg0** (``Any``): - the input ImagePlus
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** (``Any``) the view RAI

.. method:: static getOrigin(arg0, arg1)

   **Signature:** ``static getOrigin(ImgPlus, AxisType) -> double``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``float``

.. method:: static getOrigins(arg0)

   **Signature:** ``static getOrigins(ImgPlus) -> [D``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static imgPlusToCalibration(arg0)

   **Signature:** ``static imgPlusToCalibration(ImgPlus) -> Calibration``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static impToRealRai5d(arg0)

   Wrap an ImagePlus to a `RandomAccessibleInterval` such that the number of dimensions in the resulting rai is 5 and the axis order is XYCZT. Axes that are not present in the input imp have singleton dimensions in the rai.

For example, given a 2D, multichannel imp, the dimensions of the result rai are [ |X|, |Y|, |C|, 1, 1 ]

   **Signature:** ``static impToRealRai5d(ImagePlus) -> RandomAccessibleInterval``

   **Parameters:**

   * **arg0** (``Any``): -

   **Returns:** (``Any``) the 5D rai

.. method:: static maxDimension(arg0)

   **Signature:** ``static maxDimension([J) -> int``

   **Parameters:**

   * **arg0** (``Any``): -

   **Returns:** (``int``) the index of the largest dimension

.. method:: static outOfBounds(arg0, arg1, arg2)

   Checks if pos is outside the bounds given by min and max

   **Signature:** ``static outOfBounds([J, [J, [J) -> boolean``

   **Parameters:**

   * **arg0** (``Any``): - the position to check
   * **arg1** (``Any``)
   * **arg2** (``Any``)

   **Returns:** (``bool``) true if pos is out of bounds, false otherwise

.. method:: static raiToImp(arg0, arg1)

   Convert a `RandomAccessibleInterval` to an ImagePlus. If the input has 3 dimensions, the 3rd dimension is treated as depth.

   **Signature:** ``static raiToImp(RandomAccessibleInterval, String) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``): - the source rai
   * **arg1** (``str``)

   **Returns:** (``Any``) the ImagePlus

.. method:: static splitIntoBlocks(arg0, arg1)

   Partition the source rai into a list of IntervalView with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have truncated dimensions.

   **Signature:** ``static splitIntoBlocks(RandomAccessibleInterval, [J) -> List``

   **Parameters:**

   * **arg0** (``Any``): - the source rai
   * **arg1** (``Any``)

   **Returns:** (``List[Any]``) the list of blocks

.. method:: static subInterval(arg0, arg1, arg2, arg3)

   Get an N-D sub-interval of an N-D image, given two corner points and specified padding. If necessary, the computed sub-interval is clamped at the min and max of each dimension of the input interval.

   **Signature:** ``static subInterval(RandomAccessibleInterval, Localizable, Localizable, long) -> RandomAccessibleInterval``

   **Parameters:**

   * **arg0** (``Any``): - the source interval
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``int``)

   **Returns:** (``Any``) the sub-interval

.. method:: static subVolume(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

   Get a 3D sub-volume of an image, given two corner points and specified padding. If the input is 2D, a singleton dimension is added. If necessary, the computed sub-volume is clamped at the min and max of each dimension of the input interval.

   **Signature:** ``static subVolume(RandomAccessibleInterval, long, long, long, long, long, long, long) -> RandomAccessibleInterval``

   **Parameters:**

   * **arg0** (``Any``): - the source interval
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``int``)
   * **arg4** (``int``)
   * **arg5** (``int``)
   * **arg6** (``int``)
   * **arg7** (``int``)

   **Returns:** (``Any``) the subvolume

.. method:: static toImagePlus(arg0)

   **Signature:** ``static toImagePlus(ImgPlus) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static wrapWithAxes(arg0, arg1, arg2)

   **Signature:** ``static wrapWithAxes(RandomAccessibleInterval, ImgPlus, String) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``str``)

   **Returns:** ``Any``


ImpUtils
--------

.. method:: static ascii(arg0, arg1, arg2, arg3)

   Converts the specified image into ascii art.

   **Signature:** ``static ascii(ImagePlus, boolean, int, int) -> String``

   **Parameters:**

   * **arg0** (``Any``): - The image to be converted to ascii art
   * **arg1** (``bool``)
   * **arg2** (``int``)
   * **arg3** (``int``)

   **Returns:** (``str``) ascii art

.. method:: static binarize(arg0, arg1, arg2)

   **Signature:** ``static binarize(ImagePlus, double, double) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: static calibrationToAxes(arg0, arg1)

   **Signature:** ``static calibrationToAxes(Calibration, int) -> CalibratedAxis;``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: static combineSkeletons(arg0, arg1)

   **Signature:** ``static combineSkeletons(Collection, boolean) -> ImagePlus``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``bool``)

   **Returns:** ``Any``

.. method:: static convertRGBtoComposite(arg0)

   **Signature:** ``static convertRGBtoComposite(ImagePlus) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static convertTo32bit(arg0)

   **Signature:** ``static convertTo32bit(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static convertTo8bit(arg0)

   **Signature:** ``static convertTo8bit(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static convertToSimple2D(arg0, arg1)

   Converts the specified image into an easy displayable form, i.e., a non-composite 2D image If the image is a timelapse, only the first frame is considered; if 3D, a MIP is retrieved; if multichannel a RGB version is obtained. The image is flattened if its Overlay has ROIs.

   **Signature:** ``static convertToSimple2D(ImagePlus, int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``): - The image to be converted
   * **arg1** (``int``)

   **Returns:** (``Any``) a 2D 'flattened' version of the image

.. method:: static create(arg0, arg1, arg2, arg3, arg4)

   **Signature:** ``static create(String, int, int, int, int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``int``)
   * **arg4** (``int``)

   **Returns:** ``Any``

.. method:: static crop(arg0, arg1)

   Crops the image around non-background values. Does nothing if the image does not have non-background values.

   **Signature:** ``static crop(ImagePlus, Number) -> void``

   **Parameters:**

   * **arg0** (``Any``): - The image to be cropped
   * **arg1** (``Union[int, float]``)

   **Returns:** ``None``

.. method:: static demo(arg0)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.

   **Signature:** ``static demo(String) -> ImagePlus``

   **Parameters:**

   * **arg0** (``str``): - a string describing the type of demo image. Options include: 'fractal' for the L-system toy neuron; 'ddaC' for the C4 ddaC drosophila neuron (demo image initially distributed with the Sholl plugin); 'OP1'/'OP_1' for the DIADEM OP_1 dataset; 'cil701' and 'cil810' for the respective Cell Image Library entries, and 'binary timelapse' for a small 4-frame sequence of neurite growth

   **Returns:** (``Any``) the demo image, or null if data could no be retrieved

.. method:: static getCT(arg0, arg1, arg2)

   **Signature:** ``static getCT(ImagePlus, int, int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``Any``

.. method:: static getChannel(arg0, arg1)

   **Signature:** ``static getChannel(ImagePlus, int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: static getCurrentImage()

   **Signature:** ``static getCurrentImage() -> ImagePlus``

   **Returns:** ``Any``

.. method:: static getForegroundRect(arg0, arg1)

   Returns the cropping rectangle around non-background values.

   **Signature:** ``static getForegroundRect(ImagePlus, Number) -> Roi``

   **Parameters:**

   * **arg0** (``Any``): - The image to be parsed
   * **arg1** (``Union[int, float]``)

   **Returns:** (``Any``) the rectangular ROI defining non-background bounds

.. method:: static getFrame(arg0, arg1)

   **Signature:** ``static getFrame(ImagePlus, int) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: static getMIP(arg0)

   **Signature:** ``static getMIP(Collection) -> ImagePlus``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``Any``

.. method:: static getMinMax(arg0)

   **Signature:** ``static getMinMax(ImagePlus) -> [D``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static getSliceLabels(arg0)

   **Signature:** ``static getSliceLabels(ImageStack) -> List``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``List[Any]``

.. method:: static getSystemClipboard(arg0)

   Retrieves an ImagePlus from the system clipboard

   **Signature:** ``static getSystemClipboard(boolean) -> ImagePlus``

   **Parameters:**

   * **arg0** (``bool``): - if true and clipboard contains RGB data image is returned as composite (RGB/8-bit grayscale otherwise)

   **Returns:** (``Any``) the image stored in the system clipboard or null if no image found

.. method:: static imageTypeToString(arg0)

   **Signature:** ``static imageTypeToString(int) -> String``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``str``

.. method:: static invertLut(arg0)

   **Signature:** ``static invertLut(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static isBinary(arg0)

   **Signature:** ``static isBinary(ImagePlus) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: static isPointVisible(arg0, arg1, arg2)

   Checks if a given point (in image coordinates) is currently visible in an image

   **Signature:** ``static isPointVisible(ImagePlus, int, int) -> boolean``

   **Parameters:**

   * **arg0** (``Any``): - the ImagePlus to check
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** (``bool``) true if the point is visible in the current view, false otherwise

.. method:: static isVirtualStack(arg0)

   **Signature:** ``static isVirtualStack(ImagePlus) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``bool``

.. method:: static nextZoomLevel(arg0)

   **Signature:** ``static nextZoomLevel(double) -> double``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``float``

.. method:: static open(arg0, arg1)

   **Signature:** ``static open(String, String) -> ImagePlus``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)

   **Returns:** ``Any``

.. method:: static previousZoomLevel(arg0)

   **Signature:** ``static previousZoomLevel(double) -> double``

   **Parameters:**

   * **arg0** (``float``)

   **Returns:** ``float``

.. method:: static removeIsolatedPixels(arg0)

   **Signature:** ``static removeIsolatedPixels(ImagePlus) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static removeSlices(arg0, arg1)

   **Signature:** ``static removeSlices(ImageStack, Collection) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``List[Any]``)

   **Returns:** ``None``

.. method:: static rotate90(arg0, arg1)

   Rotates an image 90 degrees.

   **Signature:** ``static rotate90(ImagePlus, String) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the image to be rotated
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: static sameCTDimensions(arg0, arg1)

   **Signature:** ``static sameCTDimensions(ImagePlus, ImagePlus) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: static sameCalibration(arg0, arg1)

   **Signature:** ``static sameCalibration(ImagePlus, ImagePlus) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: static sameXYZDimensions(arg0, arg1)

   **Signature:** ``static sameXYZDimensions(ImagePlus, ImagePlus) -> boolean``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``bool``

.. method:: static save(arg0, arg1)

   Saves the specified image.

   **Signature:** ``static save(ImagePlus, String) -> void``

   **Parameters:**

   * **arg0** (``Any``): - The image to be saved
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: static setLut(arg0, arg1)

   **Signature:** ``static setLut(ImagePlus, String) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``str``)

   **Returns:** ``None``

.. method:: static toDataset(arg0)

   **Signature:** ``static toDataset(ImagePlus) -> Dataset``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static toImgPlus(arg0)

   **Signature:** ``static toImgPlus(ImagePlus) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static toImgPlus3D(arg0, arg1, arg2)

   **Signature:** ``static toImgPlus3D(ImagePlus, int, int) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** ``Any``

.. method:: static toStack(arg0)

   **Signature:** ``static toStack(Collection) -> ImagePlus``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``Any``

.. method:: static zoomTo(arg0, arg1)

   **Signature:** ``static zoomTo(ImagePlus, Collection) -> double``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``List[Any]``)

   **Returns:** ``float``


InsectBrainLoader
-----------------

.. method:: static isDatabaseAvailable()

   Checks whether a connection to the Insect Brain Database can be established.

   **Signature:** ``static isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HTTP connection could be established

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


InsectBrainUtils
----------------

.. method:: static getAllNeuronIDs()

   **Signature:** ``static getAllNeuronIDs() -> List``

   **Returns:** ``List[Any]``

.. method:: static getAllSpecies()

   **Signature:** ``static getAllSpecies() -> List``

   **Returns:** ``List[Any]``

.. method:: static getBrainCompartments(arg0, arg1)

   **Signature:** ``static getBrainCompartments(int, String) -> List``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``List[Any]``

.. method:: static getBrainJSON(arg0)

   **Signature:** ``static getBrainJSON(int) -> JSONObject``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Any``

.. method:: static getBrainMeshes(arg0, arg1)

   **Signature:** ``static getBrainMeshes(int, String) -> List``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``List[Any]``

.. method:: static getSpeciesNeuronIDs(arg0)

   **Signature:** ``static getSpeciesNeuronIDs(int) -> List``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``List[Any]``


MouseLightLoader
----------------

.. method:: static demoTrees()

   Returns a collection of four demo reconstructions NB: Data is cached locally. No internet connection required.

   **Signature:** ``static demoTrees() -> List``

   **Returns:** (``List[Any]``) the list of Trees, corresponding to the dendritic arbors of cells "AA0001", "AA0002", "AA0003", "AA0004"

.. method:: static extractNodes(arg0, arg1)

   Extracts reconstruction(s) from a JSON file.

   **Signature:** ``static extractNodes(File, String) -> Map``

   **Parameters:**

   * **arg0** (``str``): - the JSON file to be parsed
   * **arg1** (``str``)

   **Returns:** (``Dict[str, Any]``) the map containing the reconstruction nodes as SWCPoints

.. method:: static extractTrees(arg0, arg1)

   **Signature:** ``static extractTrees(InputStream, String) -> Map``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: static getAllLoaders()

   Gets the loaders for all the cells publicly available in the MouseLight database.

   **Signature:** ``static getAllLoaders() -> List``

   **Returns:** (``List[Any]``) the list of loaders

.. method:: static isDatabaseAvailable()

   Checks whether a connection to the MouseLight database can be established.

   **Signature:** ``static isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


MouseLightQuerier
-----------------

.. method:: static getAllIDs()

   Gets all available neuron IDs from the database.

   **Signature:** ``static getAllIDs() -> List``

   **Returns:** (``List[Any]``) list of all neuron IDs

.. method:: static getIDs(arg0, arg1)

   Gets neuron IDs matching the specified collection of IDs or DOIs.

   **Signature:** ``static getIDs(String, boolean) -> List``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``bool``)

   **Returns:** ``List[Any]``

.. method:: static isDatabaseAvailable()

   Checks whether a connection to the MouseLight database can be established.

   **Signature:** ``static isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static setCCFVersion(arg0)

   Sets the version of the Common Coordinate Framework to be used by the Querier.

   **Signature:** ``static setCCFVersion(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - Either "3" (the default), or "2.5" (MouseLight legacy)

   **Returns:** ``None``


MultiTreeColorMapper
--------------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static unMap(arg0)

   **Signature:** ``static unMap(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``None``


MultiTreeStatistics
-------------------

.. method:: static fromCollection(arg0, arg1)

   **Signature:** ``static fromCollection(Collection, String) -> TreeStatistics``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)

   **Returns:** ``TreeStatistics``


MultiViewer2D
-------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


MultiViewer3D
-------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


NeuroMorphoLoader
-----------------

.. method:: static get(arg0)

   Convenience method for retrieving SWC data,

   **Signature:** ``static get(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - the ID of the cell to be retrieved (case-sensitive). It may be the neuron name or its qualified filename. E.g., "cnic_002" or "cnic_002.swc" or "cnic_002.CNG.swc". By default, the standardized (CNG) version is assumed. Examples: "cnic_002" -> CNG version of neuron cnic_002 is retrieved "cnic_002.CNG.swc" -> CNG version of neuron cnic_002 is retrieved "cnic_002.swc" -> Source version of neuron cnic_002 is retrieved

   **Returns:** (``Tree``) the specified neuron as a Tree object, or null if data could not be retrieved

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


NodeColorMapper
---------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static unMap(arg0)

   **Signature:** ``static unMap(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``None``


NodeProfiler
------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


NodeStatistics
--------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


PCAnalyzer
----------

.. method:: static getPrincipalAxes(arg0)

   Computes the principal axes for a collection of SNTPoints.

   **Signature:** ``static getPrincipalAxes(Vertices) -> PCAnalyzer$PrincipalAxis;``

   **Parameters:**

   * **arg0** (``Any``): - the collection of points to analyze

   **Returns:** (``Any``) array of three PrincipalAxis objects ordered by decreasing variance (primary, secondary, tertiary), or null if computation fails

.. method:: static getVariancePercentages(arg0)

   Computes the variance percentages for an array of principal axes. This is a convenience method that returns the percentage of total variance explained by each principal axis.

   **Signature:** ``static getVariancePercentages(PCAnalyzer$PrincipalAxis;) -> [D``

   **Parameters:**

   * **arg0** (``Any``): - the array of three PrincipalAxis objects (primary, secondary, tertiary)

   **Returns:** (``Any``) array of three percentages (primary, secondary, tertiary) that sum to 100%, or null if axes is null

.. method:: static orientTowardDirection(arg0, arg1)

   Orients principal axes so the primary axis points toward a reference direction, i.e., the primary axis is oriented to minimize the angle with the reference direction. If the primary axis points away from the reference (dot product < 0), it's flipped.\

   **Signature:** ``static orientTowardDirection(PCAnalyzer$PrincipalAxis;, [D) -> PCAnalyzer$PrincipalAxis;``

   **Parameters:**

   * **arg0** (``Any``): - the principal axes to orient
   * **arg1** (``Any``)

   **Returns:** (``Any``) oriented principal axes

.. method:: static orientTowardTips(arg0, arg1)

   Convenience method to orient existing principal axes toward a tree's tips centroid. For several topologies, this orients the primary axis is so it aligns with the general growth direction of the arbor.

   **Signature:** ``static orientTowardTips(PCAnalyzer$PrincipalAxis;, Tree) -> PCAnalyzer$PrincipalAxis;``

   **Parameters:**

   * **arg0** (``Any``): - the principal axes to orient
   * **arg1** (``Tree``)

   **Returns:** (``Any``) oriented principal axes


PathAndFillManager
------------------

.. method:: static createFromGraph(arg0, arg1)

   Create a new PathAndFillManager instance from the graph.

   **Signature:** ``static createFromGraph(DirectedWeightedGraph, boolean) -> PathAndFillManager``

   **Parameters:**

   * **arg0** (``DirectedWeightedGraph``): - The input graph
   * **arg1** (``bool``)

   **Returns:** ``Any``

.. method:: static createFromNodes(arg0)

   Creates a PathAndFillManager instance from a collection of reconstruction nodes.

   **Signature:** ``static createFromNodes(Collection) -> PathAndFillManager``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of reconstruction nodes. Nodes will be sorted by id and any duplicate entries pruned.

   **Returns:** (``Any``) the PathAndFillManager instance, or null if file could not be imported


PathProfiler
------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


PathStatistics
--------------

.. method:: static fromCollection(arg0, arg1)

   **Signature:** ``static fromCollection(Collection, String) -> TreeStatistics``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)

   **Returns:** ``TreeStatistics``


PathStraightener
----------------

.. method:: static main(arg0)

   Main method for testing and demonstration purposes.

Creates a PathStraightener instance using demo data and displays the straightened path result. This method is primarily used for development and debugging.

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``): - command line arguments (not used)

   **Returns:** ``None``


PersistenceAnalyzer
-------------------

.. method:: static getDescriptors()

   Gets a list of supported descriptor functions for persistence analysis.

Returns the string identifiers for all available filter functions that can be used with getDiagram(String), getBarcode(String), and other analysis methods. These descriptors are case-insensitive when used in method calls.

   **Signature:** ``static getDescriptors() -> List``

   **Returns:** (``List[Any]``) the list of available descriptors: ["geodesic", "radial", "centrifugal", "path order", "x", "y", "z"]

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


RemoteSWCLoader
---------------

.. method:: static download(arg0, arg1)

   **Signature:** ``static download(String, File) -> boolean``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)

   **Returns:** ``bool``


RootAngleAnalyzer
-----------------

.. method:: static getDensityPlot(arg0)

   **Signature:** ``static getDensityPlot(List) -> SNTChart``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``SNTChart``

.. method:: static getHistogram(arg0, arg1)

   **Signature:** ``static getHistogram(List, boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``bool``)

   **Returns:** ``SNTChart``

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


SNTChart
--------

.. method:: static closeAll()

   Closes all open charts

   **Signature:** ``static closeAll() -> void``

   **Returns:** ``None``

.. method:: static combine(arg0, arg1, arg2, arg3)

   Combines a collection of charts into a multipanel montage.

   **Signature:** ``static combine(Collection, int, int, boolean) -> SNTChart``

   **Parameters:**

   * **arg0** (``List[Any]``): - input charts
   * **arg1** (``int``)
   * **arg2** (``int``)
   * **arg3** (``bool``)

   **Returns:** (``SNTChart``) the frame containing the montage


SNTColor
--------

.. method:: static average(arg0)

   Averages a collection of colors

   **Signature:** ``static average(Collection) -> Color``

   **Parameters:**

   * **arg0** (``List[Any]``): - the colors to be averaged

   **Returns:** (``Any``) the averaged color. Note that an average will never be accurate because the RGB space is not linear. Color.BLACK is returned if all colors in input collection are null;

.. method:: static fromHex(arg0)

   Returns an AWT Color from a (#)RRGGBB(AA) hex string.

   **Signature:** ``static fromHex(String) -> Color``

   **Parameters:**

   * **arg0** (``str``): - the input string

   **Returns:** (``Any``) the converted AWT color

.. method:: static interpolateNullEntries(arg0)

   Replaces null colors in an array with the average of flanking non-null colors.

   **Signature:** ``static interpolateNullEntries(Color;) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the color array

   **Returns:** ``None``

.. method:: static valueOf(arg0)

   **Signature:** ``static valueOf(String) -> ColorRGB``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``Any``


SNTPoint
--------

.. method:: static average(arg0)

   Computes the average position of a collection of SNTPoints.

   **Signature:** ``static average(Collection) -> PointInImage``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of points to average

   **Returns:** (``PointInImage``) the average point, or null if the collection is null or empty

.. method:: static of(arg0, arg1, arg2)

   **Signature:** ``static of(Number, Number, Number) -> PointInImage``

   **Parameters:**

   * **arg0** (``Union[int, float]``)
   * **arg1** (``Union[int, float]``)
   * **arg2** (``Union[int, float]``)

   **Returns:** ``PointInImage``


SNTUtils
--------

.. method:: static buildDate()

   Retrieves Sholl Analysis implementation date

   **Signature:** ``static buildDate() -> String``

   **Returns:** (``str``) the implementation date or an empty strong if date could not be retrieved.

.. method:: static csvQuoteAndPrint(arg0, arg1)

   **Signature:** ``static csvQuoteAndPrint(PrintWriter, Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: static error(arg0, arg1)

   **Signature:** ``static error(String, Throwable) -> void``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: static extractReadableTimeStamp(arg0)

   **Signature:** ``static extractReadableTimeStamp(File) -> String``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``

.. method:: static findClosestPair(arg0, arg1)

   **Signature:** ``static findClosestPair(File, String) -> File``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)

   **Returns:** ``str``

.. method:: static formatDouble(arg0, arg1)

   **Signature:** ``static formatDouble(double, int) -> String``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``int``)

   **Returns:** ``str``

.. method:: static getBackupCopies(arg0)

   Retrieves a list of time-stamped backup files associated with a TRACES file

   **Signature:** ``static getBackupCopies(File) -> List``

   **Parameters:**

   * **arg0** (``str``): - the TRACES file

   **Returns:** (``List[Any]``) the list of backup files. An empty list is retrieved if none could be found.

.. method:: static getContext()

   Convenience method to access the context of the running Fiji instance

   **Signature:** ``static getContext() -> Context``

   **Returns:** (``Any``) the context of the active ImageJ instance. Never null

.. method:: static getDecimalFormat(arg0, arg1)

   **Signature:** ``static getDecimalFormat(double, int) -> DecimalFormat``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: static getElapsedTime(arg0)

   **Signature:** ``static getElapsedTime(long) -> String``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``str``

.. method:: static getInstance()

   **Signature:** ``static getInstance() -> SNT``

   **Returns:** ``Any``

.. method:: static getReadableVersion()

   **Signature:** ``static getReadableVersion() -> String``

   **Returns:** ``str``

.. method:: static getSanitizedUnit(arg0)

   **Signature:** ``static getSanitizedUnit(String) -> String``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``

.. method:: static getTimeStamp()

   **Signature:** ``static getTimeStamp() -> String``

   **Returns:** ``str``

.. method:: static isContextSet()

   **Signature:** ``static isContextSet() -> boolean``

   **Returns:** ``bool``

.. method:: static isDebugMode()

   Assesses if SNT is running in debug mode

   **Signature:** ``static isDebugMode() -> boolean``

   **Returns:** (``bool``) the debug flag

.. method:: static log(arg0)

   **Signature:** ``static log(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: static setContext(arg0)

   **Signature:** ``static setContext(Context) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static setDebugMode(arg0)

   Enables/disables debug mode

   **Signature:** ``static setDebugMode(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - verbose flag

   **Returns:** ``None``

.. method:: static setIsLoading(arg0)

   **Signature:** ``static setIsLoading(boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** ``None``

.. method:: static startApp()

   Convenience method to start up SNT's GUI.

   **Signature:** ``static startApp() -> SNT``

   **Returns:** (``Any``) a reference to the SNT instance just started.s

.. method:: static stripExtension(arg0)

   **Signature:** ``static stripExtension(String) -> String``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``


SWCPoint
--------

.. method:: static collectionAsReader(arg0)

   Converts a collection of SWC points into a Reader.

   **Signature:** ``static collectionAsReader(Collection) -> StringReader``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of SWC points to be converted into a space separated String. Points should be sorted by sample number to ensure valid connectivity.

   **Returns:** (``Any``) the Reader

.. method:: static flush(arg0, arg1)

   Prints a list of points as space-separated values.

   **Signature:** ``static flush(Collection, PrintWriter) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collections of SWC points to be printed.
   * **arg1** (``Any``)

   **Returns:** ``None``


SciViewSNT
----------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


ShollAnalyzer
-------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


SkeletonConverter
-----------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static skeletonize(arg0, arg1)

   Convenience method to skeletonize a thresholded image using Skeletonize3D_.

   **Signature:** ``static skeletonize(ImagePlus, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``): - The thresholded image to be skeletonized. If the image is not thresholded all non-zero values are considered to be foreground.
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: static skeletonizeTimeLapse(arg0, arg1)

   Convenience method to skeletonize a thresholded time-lapse using Skeletonize3D_.

   **Signature:** ``static skeletonizeTimeLapse(ImagePlus, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``): - The timelapse to be skeletonized. If the image is not thresholded all non-zero values are considered to be foreground.
   * **arg1** (``bool``)

   **Returns:** ``None``


StrahlerAnalyzer
----------------

.. method:: static classify(arg0, arg1)

   **Signature:** ``static classify(DirectedWeightedGraph, boolean) -> void``

   **Parameters:**

   * **arg0** (``DirectedWeightedGraph``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


Tree
----

.. method:: static getSWCTypeMap()

   Returns the SWC Type flags used by SNT.

   **Signature:** ``static getSWCTypeMap() -> Map``

   **Returns:** (``Dict[str, Any]``) the map mapping swct type flags (e.g., Path.SWC_AXON, Path.SWC_DENDRITE, etc.) and their respective labels

.. method:: static listFromDir(arg0, arg1, arg2)

   Retrieves a list of Trees from reconstruction files stored in a common directory matching the specified criteria.

   **Signature:** ``static listFromDir(String, String, String;) -> List``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)
   * **arg2** (``Any``)

   **Returns:** ``List[Any]``


TreeColorMapper
---------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static unMap(arg0)

   **Signature:** ``static unMap(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``None``


TreeProperties
--------------

.. method:: static getStandardizedCompartment(arg0)

   **Signature:** ``static getStandardizedCompartment(String) -> String``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``


TreeStatistics
--------------

.. method:: static fromCollection(arg0, arg1)

   Creates a TreeStatistics instance from a group of Trees and a specific metric for convenient retrieval of histograms

   **Signature:** ``static fromCollection(Collection, String) -> TreeStatistics``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of trees
   * **arg1** (``str``)

   **Returns:** (``TreeStatistics``) the TreeStatistics instance


Tubeness
--------

.. method:: static apply(arg0, arg1)

   **Signature:** ``static apply(ImgPlus, double) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``float``)

   **Returns:** ``Any``


VFBUtils
--------

.. method:: static brainBarycentre(arg0)

   Returns the spatial centroid of an adult Drosophila template brain.

   **Signature:** ``static brainBarycentre(String) -> SNTPoint``

   **Parameters:**

   * **arg0** (``str``): - the template brain to be loaded (case-insensitive). Either "JFRC2" (AKA JFRC2010, VFB), "JFRC3" (AKA JFRC2013), "JFRC2018" or "FCWB" (FlyCircuit Whole Brain Template)

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of brain mesh.

.. method:: static getMesh(arg0, arg1)

   Retrieves the mesh associated with the specified VFB id.

   **Signature:** ``static getMesh(String, ColorRGB) -> OBJMesh``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``Any``)

   **Returns:** ``Any``

.. method:: static getRefBrain(arg0)

   Retrieves the surface mesh of an adult Drosophila template brain. No Internet connection is required, as these meshes (detailed on the nat.flybrains documentation) are bundled with SNT.

   **Signature:** ``static getRefBrain(String) -> OBJMesh``

   **Parameters:**

   * **arg0** (``str``): - the template brain to be loaded (case-insensitive). Either "JFRC2" (AKA JFRC2010, VFB), "JFRC3" (AKA JFRC2013), "JFRC2018", or "FCWB" (FlyCircuit Whole Brain Template)

   **Returns:** (``Any``) the template mesh.

.. method:: static getXYZLabels()

   **Signature:** ``static getXYZLabels() -> String;``

   **Returns:** (``Any``) the anatomical descriptions associated with the Cartesian X,Y,Z axes

.. method:: static isDatabaseAvailable()

   Checks whether a connection to the Virtual Fly Brain database can be established.

   **Signature:** ``static isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


Viewer2D
--------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


ZBAtlasUtils
------------

.. method:: static brainBarycentre()

   Returns the spatial centroid of the template brain.

   **Signature:** ``static brainBarycentre() -> SNTPoint``

   **Returns:** (``SNTPoint``) the SNT point defining the (X,Y,Z) center of the brain outline.

.. method:: static getRefBrain()

   Retrieves the surface mesh (outline) of the zebrafish template brain.

   **Signature:** ``static getRefBrain() -> OBJMesh``

   **Returns:** (``Any``) the outline mesh.

.. method:: static getXYZLabels()

   **Signature:** ``static getXYZLabels() -> String;``

   **Returns:** (``Any``) the anatomical descriptions associated with the Cartesian X,Y,Z axes

.. method:: static isDatabaseAvailable()

   Checks whether a connection to the FishAtlas database can be established.

   **Signature:** ``static isDatabaseAvailable() -> boolean``

   **Returns:** (``bool``) true, if an HHTP connection could be established


----

*Category index generated on 2026-01-02 22:43:26*