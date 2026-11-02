
``ImgUtils`` Class Documentation
=============================


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


**Package:** ``sc.fiji.snt.util``

Static utilities for handling and manipulation of `RandomAccessibleInterval`s


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCalibration(ImgPlus)

   Extracts ImageJ1 Calibration from ImgPlus axes, including origin offsets.


.. py:method:: getCtSlice(ImagePlus)

   Extracts a channel/time slice by squeezing singleton dimensions.

   Convenience overload that removes any singleton (size=1) channel or time dimensions from the image. Non-singleton C/T dimensions are preserved.


.. py:method:: getCtSlice3d(Dataset, int, int)

   Get a view of the ``ImagePlus`` at the specified channel and frame.


.. py:method:: getLocalOmeZarrDir(String)

   Resolves a path to a local OME-Zarr (OME-NGFF v0.5) container directory. Accepts the directory itself or its ``zarr.json`` file (as returned by some file choosers)


.. py:method:: getOmeZarrCalibration(String)

   Reads the spatial calibration from the root metadata of a local OME-Zarr (OME-NGFF v0.5) container


.. py:method:: getOrigin(ImgPlus, AxisType)

   Get the origin offset for a specific axis from an ImgPlus.


.. py:method:: getOrigins(ImgPlus)

   Get the origin offsets as {xOrigin, yOrigin, zOrigin} from an ImgPlus.


.. py:method:: getSpacing(ImgPlus)

   Returns the voxel spacing for a specific axis type, defaulting to 1.0 if the axis is absent or has zero scale. Unlike ``getSpacing(ImgPlus)``, this is axis-order-independent.


.. py:method:: getSpacingUnits(ImgPlus)

   Extracts spacing units from an ImgPlus.


.. py:method:: getXYZCImage(ImagePlus)

   Gets a 4D (X, Y, Z, C) view of the ``ImagePlus`` at the current time frame, retaining all channels. This is useful for multichannel/spectral operations that need access to all channel data simultaneously.

   The returned RAI has axis order [X, Y, Z, C], obtained from the canonical 5D [X, Y, C, Z, T] representation by fixing T and permuting C past Z.


.. py:method:: hasN5ZarrMetadata(File)

   Checks whether a local directory has the root metadata of an N5 or Zarr (v2/v3) container, i.e., whether it can be opened as one. An empty or incomplete directory (hidden files such as ``.DS_Store`` do not count) fails this check. Does not validate the metadata's content


.. py:method:: hasXYZLeading(ImgPlus)

   Returns whether the first three axes of an image are X, Y and Z (in that order)


.. py:method:: isBinary(RandomAccessibleInterval)

   


.. py:method:: isLabelImage(RandomAccessibleInterval)

   Checks whether a ``RandomAccessibleInterval`` appears to be a label image, using a default maximum of 500 classes.


.. py:method:: isMultiChannelRGB(ImgPlus)

   Checks if an ImgPlus appears to be a multi-channel RGB image (3 channels of 8-bit data, not packed ARGB).


.. py:method:: isRGB(ImgPlus)

   Checks if an ImgPlus contains packed RGB data (ARGBType).


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setOmeZarrCalibration(String, double[], String)

   Sets the spacing and/or unit in the root metadata of a local OME-Zarr (OME-NGFF v0.5) container. Spacing is the level 0 voxel size: the scale and translation of every pyramid level are rescaled by the ratio between the new and the stored spacing, so the pyramid stays consistent. Only the metadata file is rewritten


.. py:method:: setOmeZarrUnit(String, String)

   Sets the unit of the spatial axes in the root metadata of a local OME-Zarr (OME-NGFF v0.5) container. Only the metadata file is rewritten


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: computeIntensityStats(RandomAccessibleInterval)

   Computes basic intensity statistics of an image.


.. py:method:: computeMeanIntensity(RandomAccessibleInterval)

   Computes the mean intensity of an image.


.. py:method:: computePercentile(RandomAccessibleInterval, double)

   Computes an approximate percentile by random sampling.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: save(RandomAccessibleInterval, String)

   Saves an image to disk as a TIFF file, converting pixel values to the specified output type before writing. This is the save counterpart of ``open(String)``.

   The image is materialized into a concrete in-memory ``Img`` of the requested type, so the caller must ensure sufficient RAM is available. Conversion is done via ``ComplexType.setReal(double)``, which clamps values to the target type's range automatically (e.g. 16-bit unsigned values are clamped to [0, 65535]).

   Typical usage: 


   ::

       ImgUtils.save(rai, "/path/to/out.tif", new UnsignedShortType());
       ImgUtils.save(rai, "/path/to/out.tif", new UnsignedByteType());
       ImgUtils.save(rai, "/path/to/out.tif", new FloatType());





.. py:method:: saveAsOmeZarr(ImgPlus, File, int, Consumer)

   Writes an image as a multiscale OME-Zarr (OME-NGFF v0.5, Zarr v3) directory. Level 0 is streamed from ``img`` one slab of Z planes at a time (so every plane is read once), and each coarser level is computed from the previous one, one block at a time, by averaging 2x2x2 neighborhoods. Peak memory is therefore a single slab plus the blocks in flight, regardless of image size. Chunks are zstd-compressed and, for larger levels, grouped into shards (one file per shard)

   Levels are halved along X, Y and Z until a level fits a 3D texture (2048 voxels per side, and ``BvvUtils.MAX_SINGLE_TEXTURE_VOXELS``), with a minimum of 3 levels


Other Methods
~~~~~~~~~~~~~


.. py:method:: axisReport(ImgPlus)

   Builds a one-line diagnostic string listing all axes of an ``ImgPlus`` with their type, size, and scale. Used by ``open(String)`` to report the axis layout of freshly opened images.


.. py:method:: createIntervals(long[], long[])

   Partition the source dimensions into a list of `Interval`s with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have slightly different dimensions.


.. py:method:: crop(ImgPlus, long[], long[], boolean)

   Crop a region from a RandomAccessibleInterval using (x, y, z) pixel coordinates.

   For RAIs without axis metadata, assumes ZYX dimension order. Returns a view (no data copy) with the specified bounds, clamped to image bounds.

   **Important:** This method assumes ZYX dimension order (dim0=Z, dim1=Y, dim2=X), which is common for OME-ZARR and N5 datasets. For images with different axis orders, wrap as ImgPlus with proper axis metadata and use ``crop(ImgPlus, long[], long[], boolean)``.


.. py:method:: depthCodedProjection(RandomAccessibleInterval, int, long, long, ColorTable, double, double)

   Computes a depth color-coded slab max-intensity projection (analogous to ImageJ's "Temporal-Color Code" or "Hyperstack Depth Color" tools). Hue is determined by the depth of the maximum within the slab, and brightness by the intensity of the maximum.


.. py:method:: downsampleToFit(ImgPlus, int)

   Same as ``downsampleToFit(ImgPlus, int)``, but additionally caps the number of voxels of the spatial (X, Y, Z) volume, e.g., to fit BVV's single-texture capacity. After satisfying ``maxDimSize``, the step of the axis with the finest physical voxel size is repeatedly increased until the cap is met, which keeps the resulting voxels as isotropic as possible


.. py:method:: dropSingletonDimensions(ImgPlus)

   Remove singleton dimensions from an ImgPlus, preserving axis metadata.


.. py:method:: exceedsDimension(ImgPlus, int)

   Checks whether any spatial dimension of an ``ImgPlus`` exceeds the given limit. Only X, Y, and Z axes are considered.


.. py:method:: exceedsVoxelCount(ImgPlus, long)

   Checks whether the spatial (X, Y, Z) volume of an ``ImgPlus`` has more voxels than the given limit. Channel and Time axes are ignored.


.. py:method:: findSpatialAxisIndices(ImgPlus)

   Find dimension indices for X, Y, Z axes in an ImgPlus.


.. py:method:: findSpatialAxisIndicesWithFallback(ImgPlus)

   Find dimension indices for X, Y, Z axes, with fallback to assumed ZYX order.


.. py:method:: haveSameSpatialDimensions(ImagePlus, RandomAccessibleInterval)

   Checks whether an ``ImagePlus`` and a ``RandomAccessibleInterval`` have compatible spatial dimensions (width, height, and optionally depth).


.. py:method:: imgPlusToCalibration(ImgPlus)

   


.. py:method:: impToRealRai5d(ImagePlus)

   Wrap an ``ImagePlus`` to a ``RandomAccessibleInterval`` such that the number of dimensions in the resulting rai is 5 and the axis order is XYCZT. Axes that are not present in the input imp have singleton dimensions in the rai.

   For example, given a 2D, multichannel imp, the dimensions of the result rai are [ |X|, |Y|, |C|, 1, 1 ]


.. py:method:: materialize(RandomAccessibleInterval)

   Copies a (possibly lazy/remote) view into a local, contiguous ``ArrayImgFactory``-backed image. Use before repeated random-access operations on a view backed by something expensive to re-read, e.g. a remote N5/Zarr source.


.. py:method:: materializeTiled(RandomAccessibleInterval, int)

   Copies a (possibly lazy/remote) view into a local ``CellImg``. Unlike ``materialize(net.imglib2.RandomAccessibleInterval<T>)``, the result is an ``AbstractCellImg``, which is what BVV requires to stream tiles through its GPU cache instead of uploading the whole volume as a single 3D texture. It also avoids the 2^31 elements limit of ``ArrayImg``


.. py:method:: maxDimension(long[])

   


.. py:method:: maxIntensityProjection(ImgPlus)

   Computes a type-preserving max-intensity projection along the Z axis of an ``ImgPlus``.

   The Z axis is located via ``Axes.Z`` metadata, falling back to dim 2 if no labeled Z axis is found. The input pixel type ``T`` is preserved in the output, and the non-Z axes' calibration is copied across.

   If the source has no Z axis (e.g., a 2D image), the source is returned unchanged. If the Z axis exists but has depth 1, a 2D copy is returned.


.. py:method:: maxProjectionWithDepth(RandomAccessibleInterval, int, long, long)

   Computes a slab max-intensity projection of a (possibly lazy, e.g., cell-cached) image along an arbitrary axis, also keeping track of the depth at which each maximum occurs. The source is read plane by plane and only the 2D results are held in memory, so this is suitable for slabs of large datasets (see ``maxIntensityProjection(ImgPlus)`` for the ImgPlus/Z-only counterpart). To project a multichannel image, slice the channel first, e.g., with ``Views.hyperSlice(RandomAccessibleInterval, int, long)``


.. py:method:: normalizeToXYZ(ImgPlus)

   Normalizes the axes of an ``ImgPlus`` for volume viewers and tracing: singleton axes are dropped and the remaining ones are ordered X, Y, Z, [C], [T], with no pixel copy.

   - Unlabeled axes: if exactly 3 axes are present and none is labeled, they are assumed to be XYZ; if X and Y are labeled and a single third axis is unlabeled, it is assumed to be Z. Both cases are logged. Anything else unlabeled is rejected as ambiguous

   - Images without a Z axis after singleton removal (2D, or 2D plus C/T) are returned as is: callers are expected to reject them as non-volumetric

   - Images with Z but any other non-singleton axis than C or T (e.g., Position, Series) are rejected

   Images already in the normalized layout are returned unchanged (same instance).


.. py:method:: open(File)

   Opens an image file as an ImgPlus.


.. py:method:: outOfBounds(long[], long[], long[])

   Checks if pos is outside the bounds given by min and max


.. py:method:: permuteToXYZCT(ImgPlus)

   Reorders the axes of an ``ImgPlus`` to the canonical XYZCT order expected by BVV and most ImageJ tools, applying swaps as needed. Axes not present in the image are left in place. No pixel data is copied.

   This is useful when SCIFIO opens an image with axis order XYCZT (as ImageJ saves it) but BVV expects XYZCT, causing Z and C to be misinterpreted.


.. py:method:: raiToImp(RandomAccessibleInterval, String)

   Convert a ``RandomAccessibleInterval`` to an ``ImagePlus``. If the input has 3 dimensions, the 3rd dimension is treated as depth.


.. py:method:: raiToImpFast(RandomAccessibleInterval, String)

   Faster, single-copy alternative to ``raiToImp(rai, title).duplicate()``. That combination routes through a lazy ``ImageJVirtualStack`` (which performs a full copy of every slice on first/every access) and then ``ImagePlus.duplicate()`` which performs a SECOND full, single-threaded copy of every stack slice. For large crops this double-copy, single-threaded path may be quite heavy.

   This method instead copies ``rai`` directly into an ``ImagePlusImg``-backed destination, in one pass, optionally multithreaded via ``LoopBuilder``. ``ImagePlusImg``'s own per-plane pixel arrays ARE the ``ImagePlus``'s eventual ``ImageStack`` slice arrays (see ``ByteImagePlus`` and its siblings), so ``ImagePlusImg.getImagePlus()`` needs no further copy.

   Only pixel types ``ImagePlusImg`` can back with a real ``ImagePlus`` are supported: in practice ``byte``/``short``/``int``/``float`` `NativeType`s, i.e. everything ``raiToImp(RandomAccessibleInterval, String)`` is normally called with here. Anything else throws ``ImgLibException``; callers wanting a guaranteed-to-work fallback should catch it and fall back to ``raiToImp(rai, title).duplicate()``.


.. py:method:: resolveSpacing(RandomAccessibleInterval, double[])

   Resolves pixel spacing for a ``RandomAccessibleInterval``. If explicit spacing is provided and has enough dimensions, it is used directly. Otherwise, axis metadata is extracted from ``ImgPlus`` if available. Falls back to isotropic spacing of 1.0.


.. py:method:: sampledStats(Iterable, long)

   Computes min, max, mean and (sample) standard deviation in a single pass. If the image holds more than ``maxSamples`` voxels, only a regular grid of voxels is visited (same stride along all dimensions), so the result is approximate. Exact otherwise.


.. py:method:: spatialNgffUnit(ImgPlus)

   Returns the first recognized spatial unit (as an OME-NGFF name) among the X, Y and Z axes of ``img``, or null if none is recognized. Bio-Formats readers do not always set the unit on every axis (or spell it as expected), so all spatial axes are checked, not just the first


.. py:method:: splitIntoBlocks(RandomAccessibleInterval, long[])

   Partition the source rai into a list of ``IntervalView`` with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have truncated dimensions.


.. py:method:: subInterval(RandomAccessibleInterval, Localizable, Localizable, long)

   Get an N-D sub-interval of an N-D image, given two corner points and specified padding.

   Works in native dimension order (no XYZ remapping). The sub-interval is clamped to image bounds.


.. py:method:: subVolume(RandomAccessibleInterval, long, long, long, long, long, long, long)

   Get a 3D sub-volume of an image, given two corner points and specified padding.

   Coordinates are in XYZ order. If the input is 2D, a singleton dimension is added. The sub-volume is clamped to image bounds.


.. py:method:: swapAxes(ImgPlus, AxisType, AxisType)

   Returns a new ``ImgPlus`` with two axes swapped. The underlying data is a lazy permuted view (no pixel data is copied). Axis metadata (type, scale, unit) is reordered to match the new dimension order. Example: swap Z and Channel in an XYZCT image: 


   ::

       ImgPlus<?> xyzct = ImgUtils.open("image.tif");
       ImgPlus<?> xyczT = ImgUtils.swapAxes(xyzct, Axes.Z, Axes.CHANNEL);





.. py:method:: toImagePlus(ImgPlus)

   Convert an ImgPlus to an ImagePlus, cropping to a bounding box. Convenience overload without padding.


.. py:method:: toUnsignedShortIfFloat(RandomAccessibleInterval)

   Returns a 16-bit view of the given RAI if its pixel type is ``FloatType``, normalizing to the given min/max range.


.. py:method:: wrapWithAxes(RandomAccessibleInterval, ImgPlus, String)

   Wrap a RandomAccessibleInterval with axis metadata from a source ImgPlus.

   Useful for wrapping op results with proper calibration.


.. py:method:: wrapWithSpacing(RandomAccessibleInterval, double[])

   Wraps a RandomAccessibleInterval as an ImgPlus with calibrated axes (no unit).


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.ImgUtils>`_
* `ImgUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/ImgUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
