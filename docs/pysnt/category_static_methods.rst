Static Methods Methods
======================

Static utility methods that can be called without object instances.

Total methods in this category: **237**

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

   **Signature:** ``static getCompartment(int) -> AllenCompartment``

   **Parameters:**

   * **arg0** (``int``): - the name or acronym (case-insensitive) identifying the compartment

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


BundleDetector
--------------

.. method:: static find(arg0, arg1)

   Entry point: detect bundle events for a collection of paths using the given config. Internally constructs a `CrossoverFinder.Config` ith the inverted angle filter (`CrossoverFinder.Config.thetaMaxDeg` set, `CrossoverFinder.Config.thetaMinDeg` disabled) and delegates to 
```
CrossoverFinder.find(java.util.Collection<sc.fiji.snt.Path>, sc.fiji.snt.util.CrossoverFinder.Config)
```
.

   **Signature:** ``static find(Collection, BundleDetector$Config) -> List``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of paths
   * **arg1** (``Any``)

   **Returns:** (``List[Any]``) list of detected bundle events (typed as `CrossoverFinder.CrossoverEvent`)


BvvUtils
--------

.. method:: static preferMultiResolutionIfSafe(arg0, arg1)

   Forces BVV to render source with its pyramid-aware, block-streaming path (`bvv.core.multires.MultiResolutionStack3D`) instead of the naive single-texture path (`bvv.core.multires.SimpleStack3D`), when it is safe to do so.

BVV auto-detects which path to use (`bvv.core.multires.SourceStacks#inferSourceStackType`): it only picks the multi-resolution path when source's pixel type is TileAccess-supported AND `source.getSource(timepoint, 0)` is (or wraps, via VolatileView) an AbstractCellImg. Many BDV/N5 source builders wrap their levels in a plain Views-based interval (not an AbstractCellImg), which makes BVV fall back to SimpleStack3D even for a genuinely multi-resolution, remote source. SimpleStack3D uploads the entire full-resolution volume as one texture on first paint, fetching all of it synchronously

This mirrors BVV's own inferSourceStackType check before overriding it, so it never forces multi-resolution rendering on a source that would actually fail it (which would throw `UnsupportedOperationException` from TileAccess.create on the render thread). If the check fails, this method does nothing and BVV falls back to its own (slower) default

   **Signature:** ``static preferMultiResolutionIfSafe(Source, int) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the source about to be shown in BVV
   * **arg1** (``int``)

   **Returns:** ``None``

.. method:: static prefetchForShow(arg0, arg1)

   Fetches and locally caches whichever mipmap level BVV will actually render first for source, by touching every pixel on the calling thread. Call `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` first so the stack type is already decided when this runs

SimpleStack3D always uploads level 0 (full resolution) as a single texture on first paint (see `bvv.core.render.DefaultSimpleStackManager`) so that upload is what must be warmed for it. `MultiResolutionStack3D` streams blocks progressively and never blocks the EDT regardless of what is cached, so warming its coarsest level here is only a courtesy (a faster first frame).

Call this on a background thread before bvv.show(...) so the EDT only ever sees already-cached data

   **Signature:** ``static prefetchForShow(Source, int) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the source to warm up
   * **arg1** (``int``)

   **Returns:** ``None``

.. method:: static synthesizeMipmapPyramid(arg0, arg1)

   Wraps a single-resolution Source in a synthetic mipmap pyramid, built by materializing it locally (see `ImgUtils.materialize(net.imglib2.RandomAccessibleInterval<T>)`) and lazily subsampling that local copy. BVV's VolumeRenderer requires multiple resolution levels to pick a LOD; without one it throws on every repaint. Use this for non-pyramidal N5/Zarr sources that cannot be re-exported with a real pyramid.

Level 0 is the full-resolution, now-local copy; each extra level doubles the previous step size along X/Y/Z, matching how a real N5/Zarr multiscale pyramid is laid out

   **Signature:** ``static synthesizeMipmapPyramid(Source, int) -> Source``

   **Parameters:**

   * **arg0** (``Any``): - the single-level source to wrap
   * **arg1** (``int``)

   **Returns:** (``Any``) a multi-resolution Source wrapping source, or source unchanged if it already has more than one level

.. method:: static warnIfLikelyRemoteImgPlus(arg0, arg1)

   Diagnostic-only warning for the plain ImgPlus fallback path (see `SpimDataUtils.resolvePathToSource(String)`). Unlike `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`/ `warnIfLikelySimpleStack(bdv.viewer.Source<?>, int)`, an ImgPlus always has a single mipmap level, so BVV always renders it via the non-pyramid-aware SimpleStack3D path regardless of pixel type or backing storage - there is no "is it structurally eligible for MULTIRESOLUTION" question to ask here the way there is for AbstractSpimData/N5Sources.

resolvePathToSource already knows this at resolution time - a remote ImgPlus is only ever produced by its own URL fallback branch (ImgUtils.open(url)) - so this simply carries that signal forward rather than trying to re-derive it by introspecting the RAI (which, for a lazily-opened remote image, may not even be a recognizable cache type)

   **Signature:** ``static warnIfLikelyRemoteImgPlus(ImgPlus, String) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the resolved
   * **arg1** (``str``): about to be shown in BVV

   **Returns:** ``None``

.. method:: static warnIfLikelySimpleStack(arg0, arg1)

   Read-only counterpart to `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` for AbstractSpimData sources (BDV-XML/HDF5, IMS): logs a warning if source looks likely to fall back to BVV's non-pyramid-aware SimpleStack3D renderer, without attempting to prevent it.

Unlike the `SpimDataUtils.N5Sources` path, 
```
BvvFunctions.show(AbstractSpimData,
 BvvOptions)
```
 builds its own Source instances internally (via `BigDataViewer#initSetups`), so there is no hook to call `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` on the actual instance before it first renders. inferSourceStackType's check is a pure function of the source's structural properties (pixel type, whether level 0 is an AbstractCellImg), not of instance identity or any per-instance cached state, so running the same check here - on the Source SNT already has a handle to after `show()` returns - still gives an accurate answer; it just can't change the outcome

This is diagnostic only: it neither prefetches nor forces a stack type, so it carries none of `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`/`prefetchForShow(bdv.viewer.Source<T>, int)`'s risk of misbehaving on a source shape this hasn't been exercised against - it only makes a slow first paint traceable in the log after the fact, for whichever AbstractSpimData backend produced it

   **Signature:** ``static warnIfLikelySimpleStack(Source, int) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the (already-shown) source to inspect
   * **arg1** (``int``)

   **Returns:** ``None``


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

   Apply multiscale Frangi vesselness filter to an ImgPlus.

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

   Crop a region from a RandomAccessibleInterval using (x, y, z) pixel coordinates.

For RAIs without axis metadata, assumes ZYX dimension order. Returns a view (no data copy) with the specified bounds, clamped to image bounds.

Important: This method assumes ZYX dimension order (dim0=Z, dim1=Y, dim2=X), which is common for OME-ZARR and N5 datasets. For images with different axis orders, wrap as ImgPlus with proper axis metadata and use `crop(ImgPlus, long[], long[], boolean)`.

   **Signature:** ``static crop(ImgPlus, [J, [J, boolean) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``bool``)

   **Returns:** ``Any``

.. method:: static dropSingletonDimensions(arg0)

   Remove singleton dimensions from an ImgPlus, preserving axis metadata.

   **Signature:** ``static dropSingletonDimensions(ImgPlus) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``): - the source ImgPlus (e.g., 5D XYZCT with C=1, T=1)

   **Returns:** (``Any``) ImgPlus with singleton dimensions removed

.. method:: static findSpatialAxisIndices(arg0)

   Find dimension indices for X, Y, Z axes in an ImgPlus.

   **Signature:** ``static findSpatialAxisIndices(ImgPlus) -> [I``

   **Parameters:**

   * **arg0** (``Any``): - the ImgPlus

   **Returns:** (``Any``) int array {xIdx, yIdx, zIdx}, with -1 for missing axes

.. method:: static findSpatialAxisIndicesWithFallback(arg0)

   Find dimension indices for X, Y, Z axes, with fallback to assumed ZYX order.

   **Signature:** ``static findSpatialAxisIndicesWithFallback(ImgPlus) -> [I``

   **Parameters:**

   * **arg0** (``Any``): - the ImgPlus

   **Returns:** (``Any``) int array {xIdx, yIdx, zIdx}

.. method:: static getCalibration(arg0)

   Extracts ImageJ1 Calibration from ImgPlus axes, including origin offsets.

   **Signature:** ``static getCalibration(ImgPlus) -> Calibration``

   **Parameters:**

   * **arg0** (``Any``): - the source ImgPlus

   **Returns:** (``Any``) Calibration with pixel sizes, unit, and origins

.. method:: static getCtSlice(arg0, arg1, arg2)

   Extracts a channel/time slice by squeezing singleton dimensions.

Convenience overload that removes any singleton (size=1) channel or time dimensions from the image. Non-singleton C/T dimensions are preserved.

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

   Get the origin offset for a specific axis from an ImgPlus.

   **Signature:** ``static getOrigin(ImgPlus, AxisType) -> double``

   **Parameters:**

   * **arg0** (``Any``): - the ImgPlus
   * **arg1** (``Any``)

   **Returns:** (``float``) the origin offset in calibrated units, or 0 if not found

.. method:: static getOrigins(arg0)

   Get the origin offsets as {xOrigin, yOrigin, zOrigin} from an ImgPlus.

   **Signature:** ``static getOrigins(ImgPlus) -> [D``

   **Parameters:**

   * **arg0** (``Any``): - the ImgPlus

   **Returns:** (``Any``) array of {xOrigin, yOrigin, zOrigin} in calibrated units

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

   Get an N-D sub-interval of an N-D image, given two corner points and specified padding.

Works in native dimension order (no XYZ remapping). The sub-interval is clamped to image bounds.

   **Signature:** ``static subInterval(RandomAccessibleInterval, Localizable, Localizable, long) -> RandomAccessibleInterval``

   **Parameters:**

   * **arg0** (``Any``): - the source interval
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``int``)

   **Returns:** (``Any``) the sub-interval

.. method:: static subVolume(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

   Get a 3D sub-volume of an image, given two corner points and specified padding.

Coordinates are in XYZ order. If the input is 2D, a singleton dimension is added. The sub-volume is clamped to image bounds.

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

   **Returns:** (``Any``) the sub-volume

.. method:: static toImagePlus(arg0)

   Convert an ImgPlus to an ImagePlus, cropping to a bounding box. Convenience overload without padding.

   **Signature:** ``static toImagePlus(ImgPlus) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``Any``

.. method:: static wrapWithAxes(arg0, arg1, arg2)

   Wrap a RandomAccessibleInterval with axis metadata from a source ImgPlus.

Useful for wrapping op results with proper calibration.

   **Signature:** ``static wrapWithAxes(RandomAccessibleInterval, ImgPlus, String) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``): - the RAI to wrap
   * **arg1** (``Any``)
   * **arg2** (``str``)

   **Returns:** (``Any``) ImgPlus with copied axis metadata


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

   Binarize an ImagePlus using lower and upper thresholds. Pixels within [lower, upper] become 255 (white), others become 0 (black).

   **Signature:** ``static binarize(ImagePlus, double, double) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the image to be binarized
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``None``

.. method:: static calibrationToAxes(arg0, arg1)

   Creates ImgPlus axes from IJ1 Calibration

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

   Converts the specified image into an easy displayable form, i.e., a non-composite 2D image If the image is a timelapse, only the first frame is considered; if 3D, a MIP is retrieved; if multichannel, an RGB version is obtained. The image is flattened if its Overlay has ROIs.

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

   * **arg0** (``str``): - a string describing the type of demo image. Options include: 'fractal' for the L-system toy neuron; 'ddaC' for the C4 ddaC drosophila neuron (demo image initially distributed with the Sholl plugin); 'OP1'/'OP_1' for the DIADEM OP_1 dataset; 'cil701', 'cil810', or 'ci41458' for the respective Cell Image Library entries, 'microglia' for a MIP of tiled microglia cells in the mouse retina, and 'binary timelapse' for a small 4-frame sequence of neurite growth

   **Returns:** (``Any``) the demo image, or null if data could not be retrieved

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

   Returns the cropping rectangle around non-background values, considering all slices of the stack.

   **Signature:** ``static getForegroundRect(ImagePlus, Number) -> Roi``

   **Parameters:**

   * **arg0** (``Any``): - The image to be parsed
   * **arg1** (``Union[int, float]``)

   **Returns:** (``Any``) the rectangular ROI defining non-background bounds, or null if all pixels are background

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

   Convert an ImagePlus to an ImgPlus with calibration and origin metadata.

Creates an ImgPlus with proper axis types (X, Y, Z, Channel, Time) and transfers calibration including pixel sizes, units, and origin offsets.

   **Signature:** ``static toImgPlus(ImagePlus) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``): - the source ImagePlus

   **Returns:** (``Any``) ImgPlus with calibrated axes

.. method:: static toImgPlus3D(arg0, arg1, arg2)

   Convert an ImagePlus to a 3D (XYZ) ImgPlus, extracting a single channel/frame if needed.

Useful for analysis that expects simple 3D images without channel/time dimensions.

   **Signature:** ``static toImgPlus3D(ImagePlus, int, int) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``): - the source ImagePlus
   * **arg1** (``int``)
   * **arg2** (``int``)

   **Returns:** (``Any``) 3D ImgPlus with X, Y, Z axes

.. method:: static toStack(arg0)

   **Signature:** ``static toStack(Collection) -> ImagePlus``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``Any``

.. method:: static zoomTo(arg0, arg1)

   Zooms the image canvas to the specified magnification level, centered on the bounding box of the given paths.

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

   **Signature:** ``static extractNodes(InputStream, String) -> Map``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``str``)

   **Returns:** ``Dict[str, Any]``

.. method:: static extractTrees(arg0, arg1)

   **Signature:** ``static extractTrees(File, String) -> Map``

   **Parameters:**

   * **arg0** (``str``)
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

.. method:: static getIDs(arg0)

   Gets neuron IDs matching the specified collection of IDs or DOIs.

   **Signature:** ``static getIDs(Collection) -> List``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of IDs or DOIs to search for

   **Returns:** (``List[Any]``) list of matching neuron IDs

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

   **Signature:** ``static unMap(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``)

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

   * **arg0** (``str``): - the ID of the cell to be retrieved (case-sensitive). It may be the neuron name or its qualified filename. E.g., "cnic_002" or "cnic_002.swc" or "cnic_002.CNG.swc". By default, the standardized (CNG) version is assumed. Examples:

"cnic_002" -> CNG version of neuron cnic_002 is retrieved "cnic_002.CNG.swc" -> CNG version of neuron cnic_002 is retrieved "cnic_002.swc" -> Source version of neuron cnic_002 is retrieved

   **Returns:** (``Tree``) the specified neuron as a Tree object, or null if data could not be retrieved

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


NeurolucidaImporter
-------------------

.. method:: static isNeurolucidaXML(arg0)

   Checks whether the given input stream starts with Neurolucida XML content. The stream must support `InputStream.mark(int)`.

   **Signature:** ``static isNeurolucidaXML(InputStream) -> boolean``

   **Parameters:**

   * **arg0** (``Any``): - a mark-supported input stream positioned at the start of the file

   **Returns:** (``bool``) true if the content appears to be a Neurolucida XML file


NodeColorMapper
---------------

.. method:: static main(arg0)

   **Signature:** ``static main(String;) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: static unMap(arg0)

   **Signature:** ``static unMap(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``)

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

   **Signature:** ``static getPrincipalAxes(Path) -> PCAnalyzer$PrincipalAxis;``

   **Parameters:**

   * **arg0** (``Path``): - the collection of points to analyze

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

.. method:: static fromString(arg0)

   Returns an AWT Color from any css-valid co

   **Signature:** ``static fromString(String) -> Color``

   **Parameters:**

   * **arg0** (``str``): - the input string

   **Returns:** (``Any``) the converted AWT color

.. method:: static interpolateNullEntries(arg0)

   Replaces null colors in an array with the average of flanking non-null colors.

   **Signature:** ``static interpolateNullEntries(Color;) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the color array

   **Returns:** ``None``

.. method:: static mix(arg0, arg1, arg2)

   Linearly mixes two colors together based on a specified weight, using a gamma-corrected linear blend by squaring the individual color channels before mixing

   **Signature:** ``static mix(Color, Color, double) -> Color``

   **Parameters:**

   * **arg0** (``Any``): - the starting color (used completely when
   * **arg1** (``Any``): is 0.0)
   * **arg2** (``float``)

   **Returns:** (``Any``) a new Color object representing the combined result

.. method:: static valueOf(arg0)

   Parses a color from the given string.

The following formats are supported: Hex format [HTML color codes starting with hash (#)], Color presets (e.g., 'blue', 'pink', 'silver', etc.), and integer triples of the form r,g,b, with each element in the range [0, 255].

   **Signature:** ``static valueOf(String) -> ColorRGB``

   **Parameters:**

   * **arg0** (``str``): - string defining the color value

   **Returns:** (``Any``) the color


SNTPoint
--------

.. method:: static average(arg0)

   Computes the average position of a collection of SNTPoints.

   **Signature:** ``static average(Collection) -> PointInImage``

   **Parameters:**

   * **arg0** (``List[Any]``): - the collection of points to average

   **Returns:** (``PointInImage``) the average point, or null if the collection is null or empty

.. method:: static fromString(arg0)

   **Signature:** ``static fromString(String) -> PointInImage``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``PointInImage``

.. method:: static of(arg0, arg1, arg2)

   **Signature:** ``static of(Number, Number, Number) -> PointInImage``

   **Parameters:**

   * **arg0** (``Union[int, float]``)
   * **arg1** (``Union[int, float]``)
   * **arg2** (``Union[int, float]``)

   **Returns:** ``PointInImage``


SNTTable
--------

.. method:: static asDouble(arg0)

   Coerces a table cell to a double. Cells may be typed Double, Long, or String depending on how the table was parsed (e.g. CSV column-type inference); this accepts any of those, with a String parse fallback for a numeric-looking value stored in a non-numeric column

   **Signature:** ``static asDouble(Object) -> double``

   **Parameters:**

   * **arg0** (``Any``): - a cell value, e.g. from

   **Returns:** (``float``) the coerced value, or Double.NaN if cell is null, empty, or not parseable as a number

.. method:: static asInt(arg0, arg1)

   Coerces a table cell to an int. Tolerates a Double-shaped integer string (e.g. "1.0" -> 1)

   **Signature:** ``static asInt(Object, int) -> int``

   **Parameters:**

   * **arg0** (``Any``): - a cell value, e.g. from
   * **arg1** (``int``)

   **Returns:** (``int``) the coerced value, or fallback

.. method:: static asString(arg0, arg1)

   Coerces a table cell to a trimmed String

   **Signature:** ``static asString(Object, String) -> String``

   **Parameters:**

   * **arg0** (``Any``): - a cell value, e.g. from
   * **arg1** (``str``)

   **Returns:** (``str``) the coerced value, or fallback

.. method:: static fromGenericTable(arg0)

   **Signature:** ``static fromGenericTable(GenericTable) -> SNTTable``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``SNTTable``


SNTUtils
--------

.. method:: static csvQuoteAndPrint(arg0, arg1)

   **Signature:** ``static csvQuoteAndPrint(PrintWriter, Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``

.. method:: static downloadAndExtractZip(arg0)

   Downloads a zip archive from the specified URL and extracts it to a fresh temporary directory. Both the downloaded archive and the extracted contents are marked for deletion on JVM exit; the archive itself is also deleted immediately once extraction succeeds, since it is not needed afterward.

   **Signature:** ``static downloadAndExtractZip(String) -> File``

   **Parameters:**

   * **arg0** (``str``): - the URL of the zip archive to download and extract

   **Returns:** (``str``) the temporary directory holding the extracted contents

.. method:: static error(arg0, arg1)

   As `error(String, Throwable)`, but allows suppressing the notification-center mirroring, e.g., when the caller has already surfaced the message to the user synchronously (a modal dialog)

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

.. method:: static formatBytes(arg0)

   **Signature:** ``static formatBytes(long) -> String``

   **Parameters:**

   * **arg0** (``int``): - a byte count

   **Returns:** (``str``) a human-readable representation (e.g., "12.3 MB")

.. method:: static formatDouble(arg0, arg1)

   **Signature:** ``static formatDouble(double, int) -> String``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``int``)

   **Returns:** ``str``

.. method:: static getBackupCopies(arg0, arg1)

   Returns all timestamped backup copies in the specified location. Convenience method that matches all traces files with timestamps.

   **Signature:** ``static getBackupCopies(File, String) -> List``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)

   **Returns:** ``List[Any]``

.. method:: static getCacheDir()

   Returns SNT's own scratch/cache directory, used by disk-backed operations (e.g. `DiskBackedStorageBackend`, Lazy). Unlike the workspace directory (see `SNTPrefs#getWorkspaceDir()`), this directory holds only disposable, regenerable scratch data -- never anything a user created -- so it lives under the OS temp root.

Individual operations create their own uniquely-named subdirectory here and clean up after themselves once done. This parent directory itself is created lazily and left in place across sessions, so that (1) it is always at the same, discoverable path and (2) leftovers from a crashed session (which skipped its own cleanup) remain visible and removable.

   **Signature:** ``static getCacheDir() -> File``

   **Returns:** (``str``) SNT's cache directory (created if it did not already exist), or, if that path could not be created/written to (e.g. permissions, a network-mounted or read-only temp location, a stray file already occupying that path), a fallback directory under the user's home folder. Callers relying on this directory for disk-backed caching should still be prepared for IOExceptions down the line (e.g. if the disk is full).

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

.. method:: static getHeapInfo()

   **Signature:** ``static getHeapInfo() -> SNTUtils$HeapInfo``

   **Returns:** (``Any``) a snapshot of current JVM heap usage

.. method:: static getInstance()

   **Signature:** ``static getInstance() -> SNT``

   **Returns:** ``Any``

.. method:: static getLastElement(arg0)

   Extracts the last path/URL element (typically a filename) from a file path, URL, or cloud-storage link, e.g., "/data/sample.n5" or `"https://host/a/b.zarr?x=1"` both yield "b.zarr"/"sample.n5". Handles Windows-style backslashes, trailing slashes, and URL query parameters/anchors.

   **Signature:** ``static getLastElement(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - the path/URL/link to parse

   **Returns:** (``str``) the last element, or an empty string if `filePathOrUrlOrCloudLink` is null or blank

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

.. method:: static isReachable(arg0, arg1)

   Checks for whether url's host can be reached, meant to be called before a real download/stream attempt (e.g., `downloadToTempFile(java.lang.String)`) so that a missing network connection surfaces as one clear message. est-effort: only http(s) URLs are actually probed; any other scheme (e.g. a bare host-less URI) is assumed reachable, deferring to the real caller

   **Signature:** ``static isReachable(String, int) -> boolean``

   **Parameters:**

   * **arg0** (``str``): - the URL to check
   * **arg1** (``int``)

   **Returns:** (``bool``) true if the host could be reached (or url is not a plain http(s) URL); false if a connection could not be established within timeoutMs

.. method:: static isStandaloneContext()

   Returns whether the current context was self-initialized by SNT (i.e., no host application like ImageJ/Fiji provided one). This is useful for determining if it is safe to modify global UI state such as the Look and Feel.

   **Signature:** ``static isStandaloneContext() -> boolean``

   **Returns:** (``bool``) true if the context was created by SNT itself, false if provided externally

.. method:: static log(arg0)

   **Signature:** ``static log(String) -> void``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``None``

.. method:: static nowTruncatedToSeconds()

   Returns the current date-time truncated to whole seconds, e.g., for stamping exported content with a generation time.

   **Signature:** ``static nowTruncatedToSeconds() -> LocalDateTime``

   **Returns:** ``Any``

.. method:: static openRemoteStream(arg0)

   Opens an InputStream to url with explicit connect/read timeouts, so a stalled or unreachable remote host fails with a clear IOException instead of hanging indefinitely - the default behavior of URL.openStream(), whose underlying URLConnection has no timeout at all unless one is set explicitly. Used for remote reconstruction/marker/demo files (e.g. `https://.../autotracings.traces`), which are typically small enough that a single bounded connection (rather than `runWithTimeout(java.util.concurrent.Callable<T>, long, java.lang.String)`'s background-thread wrapper) is enough.

   **Signature:** ``static openRemoteStream(String) -> InputStream``

   **Parameters:**

   * **arg0** (``str``): - the URL to open (e.g. a remote .traces/.csv file, or a .zip archive)

   **Returns:** (``Any``) an InputStream ready to be read

.. method:: static runWithTimeout(arg0, arg1, arg2)

   Runs task on a bounded background (daemon) thread, guarding against blocking I/O - typically remote N5/Zarr discovery, that can otherwise hang indefinitely on a stalled connection with no feedback to the user.

Unlike `openRemoteStream(String)` (a single bounded connection), this bounds the *entire* operation, however many network round-trips it internally makes.

On timeout, the background thread is best-effort interrupted via `ExecutorService.shutdownNow()`; if the underlying I/O call ignores interruption (common for plain socket reads), that thread may still leak until the stalled connection itself eventually times out or errors, but the calling thread is freed immediately to report the failure, rather than hanging alongside it.

   **Signature:** ``static runWithTimeout(Callable, long, String) -> Object``

   **Parameters:**

   * **arg0** (``Any``): - the (typically network-bound) operation to run
   * **arg1** (``int``)
   * **arg2** (``str``)

   **Returns:** (``Any``) the result of task

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

.. method:: static setIsLoading(arg0, arg1)

   Shows or hides the loading splash screen. Calls nest safely: several independent call chains can be "loading" at once, so the splash only actually closes once every true has been balanced by a matching false, hence calls should be made in a try/finally block.

   **Signature:** ``static setIsLoading(boolean, boolean) -> void``

   **Parameters:**

   * **arg0** (``bool``): - true to show the splash screen (or register one more caller that wants it showing, if already showing); false to release one such registration, closing the splash once no callers still hold it
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: static startApp(arg0)

   Convenience method to start up SNT's GUI.

   **Signature:** ``static startApp(boolean) -> SNT``

   **Parameters:**

   * **arg0** (``bool``): - If

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

   **Signature:** ``static skeletonize(ImagePlus, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``

.. method:: static skeletonizeTimeLapse(arg0, arg1)

   **Signature:** ``static skeletonizeTimeLapse(ImagePlus, boolean) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``bool``)

   **Returns:** ``None``


SpectralSimilarity
------------------

.. method:: static channelSum(arg0)

   Sums all elements of a vector. Typically used to compute the total intensity across channels of a color vector.

   **Signature:** ``static channelSum([D) -> double``

   **Parameters:**

   * **arg0** (``Any``): - the vector

   **Returns:** (``float``) the sum of all elements

.. method:: static nodeToPixelCoords(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

   As `nodeToPixelCoords(sc.fiji.snt.util.PointInImage, double, double, double)`, but also adding a pixel-space offset after scaling - typically `SNT#getActiveCanvasPixelOffset()`, needed whenever the target image is the crop-local grid of a materialized crop, or the raw streamed source's own voxel grid under a non-zero `SNT#getWorldOriginOffset()` (see `SNT#createSearch(double, double, double, double, double, double)` for the same conversion, applied to A* search endpoints instead of Path nodes).

   **Signature:** ``static nodeToPixelCoords(PointInImage, double, double, double, double, double, double) -> [I``

   **Parameters:**

   * **arg0** (``PointInImage``): - the node in calibrated coordinates
   * **arg1** (``float``)
   * **arg2** (``float``)
   * **arg3** (``float``)
   * **arg4** (``float``)
   * **arg5** (``float``)
   * **arg6** (``float``)

   **Returns:** (``Any``) pixel coordinates as [x, y, z]

.. method:: static normalizeVector(arg0)

   Normalizes a vector to unit length in place. If the vector has zero magnitude, it is left unchanged.

   **Signature:** ``static normalizeVector([D) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the vector to normalize

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

   **Signature:** ``static unMap(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``)

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


TreeUtils
---------

.. method:: static canFormContinuousChain(arg0, arg1)

   Checks if a collection of paths can form a spatially continuous chain within a given tolerance.

   **Signature:** ``static canFormContinuousChain(Collection, double) -> boolean``

   **Parameters:**

   * **arg0** (``List[Any]``): - the paths to check
   * **arg1** (``float``)

   **Returns:** (``bool``) true if paths can be ordered into a continuous chain within tolerance

.. method:: static collectChildren(arg0, arg1)

   Collects direct children of a path into the provided collection.

   **Signature:** ``static collectChildren(Path, Collection) -> void``

   **Parameters:**

   * **arg0** (``Path``)
   * **arg1** (``List[Any]``)

   **Returns:** ``None``

.. method:: static collectDescendants(arg0, arg1)

   Collects all descendants (children, grandchildren, etc.) of a path into the provided collection.

   **Signature:** ``static collectDescendants(Path, Collection) -> void``

   **Parameters:**

   * **arg0** (``Path``)
   * **arg1** (``List[Any]``)

   **Returns:** ``None``

.. method:: static countDescendants(arg0)

   Counts all descendants (children, grandchildren, etc.) of a path.

   **Signature:** ``static countDescendants(Path) -> int``

   **Parameters:**

   * **arg0** (``Path``)

   **Returns:** ``int``

.. method:: static findClosestEndpoints(arg0, arg1)

   Finds the closest endpoint pairing between two paths. Checks all four combinations: start-start, start-end, end-start, end-end.

   **Signature:** ``static findClosestEndpoints(Path, Path) -> TreeUtils$EndpointMatch``

   **Parameters:**

   * **arg0** (``Path``): - first path
   * **arg1** (``Path``)

   **Returns:** (``Any``) EndpointMatch describing the closest pairing, or null if either path is empty

.. method:: static getConnectedTree(arg0)

   Gets the connected tree (component) containing the given path. This traverses up to the root and then collects all descendants, ensuring we only get paths that are actually connected via parent-child relationships.

This is useful when paths may share a tree ID but are not actually connected (e.g., orphaned paths or paths awaiting relationship rebuild).

   **Signature:** ``static getConnectedTree(Path) -> Tree``

   **Parameters:**

   * **arg0** (``Path``): - a path in the tree

   **Returns:** (``Tree``) a Tree containing only the connected component

.. method:: static getMaxOrder(arg0)

   Returns the maximum path order in the connected tree containing the given path. Higher values indicate deeper/more developed trees.

   **Signature:** ``static getMaxOrder(Path) -> int``

   **Parameters:**

   * **arg0** (``Path``): - a path in the tree

   **Returns:** (``int``) the maximum order value found in the connected tree, or 0 if retrieval fails

.. method:: static isAncestorOf(arg0, arg1)

   Checks if 'potentialAncestor' is an ancestor of 'potentialDescendant'. This traverses up the parent chain from potentialDescendant.

   **Signature:** ``static isAncestorOf(Path, Path) -> boolean``

   **Parameters:**

   * **arg0** (``Path``): - the path to check if it's an ancestor
   * **arg1** (``Path``)

   **Returns:** (``bool``) true if potentialAncestor is an ancestor of potentialDescendant

.. method:: static isDescendantOf(arg0, arg1)

   Checks if 'potentialDescendant' is a descendant of 'potentialAncestor'. This is equivalent to checking if potentialDescendant is in the subtree rooted at potentialAncestor (excluding potentialAncestor itself).

   **Signature:** ``static isDescendantOf(Path, Path) -> boolean``

   **Parameters:**

   * **arg0** (``Path``): - the path to check if it's a descendant
   * **arg1** (``Path``)

   **Returns:** (``bool``) true if potentialDescendant is a descendant of potentialAncestor

.. method:: static isInSubtree(arg0, arg1)

   Checks if 'target' is in the subtree rooted at 'root'. This traverses down through all descendants of root.

   **Signature:** ``static isInSubtree(Path, Path) -> boolean``

   **Parameters:**

   * **arg0** (``Path``): - the path to search for
   * **arg1** (``Path``)

   **Returns:** (``bool``) true if target is root or any descendant of root

.. method:: static merge(arg0)

   Combines all trees into a single Tree container.

Note that no effort is made to make the merge structure topographylically valid. This is simply a convenience method to collect paths in a single contained for operations that do not require an accurate graph structure, e.g., Sholl Analysis.

   **Signature:** ``static merge(Collection) -> Tree``

   **Parameters:**

   * **arg0** (``List[Any]``): -

   **Returns:** (``Tree``) the merged tree

.. method:: static orderByEndpointProximity(arg0)

   Orders a collection of paths to form a spatially continuous chain based on endpoint proximity. The algorithm greedily connects paths by finding the closest endpoint pairs.

This method does NOT modify the paths (no reversal). Use `orientPathsForMerging(List)` on the result to fix orientations.

   **Signature:** ``static orderByEndpointProximity(Collection) -> List``

   **Parameters:**

   * **arg0** (``List[Any]``): - the paths to order (at least 2)

   **Returns:** (``List[Any]``) ordered list forming a chain, or empty list if paths cannot form a continuous chain

.. method:: static rasterize(arg0, arg1, arg2)

   Rasterizes a tree into a 3D image with the specified voxel sizes.

   **Signature:** ``static rasterize(Tree, double, double) -> ImagePlus``

   **Parameters:**

   * **arg0** (``Tree``)
   * **arg1** (``float``)
   * **arg2** (``float``)

   **Returns:** ``Any``

.. method:: static restoreNodeValues(arg0)

   Restores per-path node values captured by `snapshotNodeValues(Tree)`.

   **Signature:** ``static restoreNodeValues(Map) -> void``

   **Parameters:**

   * **arg0** (``Dict[str, Any]``)

   **Returns:** ``None``

.. method:: static snapshotNodeValues(arg0)

   Snapshots the per-node values (node.v) for each path in a Tree so they can be restored later.

   **Signature:** ``static snapshotNodeValues(Tree) -> Map``

   **Parameters:**

   * **arg0** (``Tree``)

   **Returns:** (``Dict[str, Any]``) map keyed by path; entries are null when the path had no assigned values

.. method:: static suggestRootLocation(arg0, arg1)

   Analyzes paths and suggests auto-orientation based on:

If a reference point (e.g., ROI centroid) is provided, orient toward it For 3+ paths: find the tighter endpoint cluster as the root For 2 paths: find the closest endpoint pair as the root

   **Signature:** ``static suggestRootLocation(Collection, PointInImage) -> PointInImage``

   **Parameters:**

   * **arg0** (``List[Any]``): - the paths to analyze
   * **arg1** (``PointInImage``)

   **Returns:** (``PointInImage``) the suggested root location, or null if it cannot be determined

.. method:: static syncCanvasOffset(arg0, arg1)

   Applies the parent's canvas offset to the child path and all its descendants. This ensures paths are in the same coordinate space after connection. Node coordinates are transformed to maintain the same visual position.

   **Signature:** ``static syncCanvasOffset(Path, Path) -> void``

   **Parameters:**

   * **arg0** (``Path``)
   * **arg1** (``Path``)

   **Returns:** ``None``


Tubeness
--------

.. method:: static apply(arg0, arg1)

   Apply single-scale tubeness filter to an ImgPlus.

   **Signature:** ``static apply(ImgPlus, [D) -> ImgPlus``

   **Parameters:**

   * **arg0** (``Any``): - input image (2D or 3D) with calibrated axes
   * **arg1** (``Any``)

   **Returns:** (``Any``) filtered ImgPlus with same axes as input


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

*Category index generated on 2026-09-27 23:02:20*