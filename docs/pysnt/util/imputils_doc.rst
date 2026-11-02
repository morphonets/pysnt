
``ImpUtils`` Class Documentation
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

Static utilities for handling and manipulation of `ImagePlus`s


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearAllTags()

   Clears both tag registries entirely. Intended as a session-teardown safety net, not for routine use: individual images are already forgotten via ``forgetTags(ImagePlus)`` as they close.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCT(ImagePlus, int, int)

   


.. py:method:: getChannel(ImagePlus, int)

   


.. py:method:: getChannelStack(ImagePlus, int)

   Returns a lightweight read-only view of a single channel as an ImageStack. Unlike ``getChannel(ImagePlus, int)``, the returned stack shares the underlying pixel arrays with the source image (no data copy), making it suitable for read-only access on large multichannel images.


.. py:method:: getCurrentImage()

   


.. py:method:: getFilePath(ImagePlus)

   Returns the file path of an image.


.. py:method:: getForegroundRect(ImagePlus, Number)

   Returns the cropping rectangle around non-background values, considering all slices of the stack.


.. py:method:: getFrame(ImagePlus, int)

   


.. py:method:: getMIP(Collection)

   


.. py:method:: getMagnification(ImagePlus)

   


.. py:method:: getMinMax(ImagePlus)

   


.. py:method:: getNonSNTOpenImages()

   Returns all currently open images in ImageJ that were not created by SNT.


.. py:method:: getOpenImages()

   Returns all currently open images in ImageJ's ``WindowManager``.


.. py:method:: getSliceLabels(ImageStack)

   


.. py:method:: getSystemClipboard(boolean)

   Retrieves an ImagePlus from the system clipboard


.. py:method:: isBinary(ImagePlus)

   


.. py:method:: isDisplayCanvas(ImagePlus)

   Checks whether an image is a placeholder canvas


.. py:method:: isMaterializedCrop(ImagePlus)

   Checks whether an image is a materialized crop of a streamed volume.


.. py:method:: isPointVisible(ImagePlus, int, int)

   Checks if a given point (in image coordinates) is currently visible in an image


.. py:method:: isVirtualStack(ImagePlus)

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setIsDisplayCanvas(ImagePlus)

   Used by SNT to tag an image as a Display Canvas (typically a blank placeholder image).


.. py:method:: setIsMaterializedCrop(ImagePlus)

   Used by SNT to tag an eagerly-materialized pixel crop of a streamed volume as such.


.. py:method:: setLut(ImagePlus, String)

   


.. py:method:: setSliceLabels(ImageStack, String)

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: save(ImagePlus, String)

   Saves the specified image.


Other Methods
~~~~~~~~~~~~~


.. py:method:: applyColorTable(ImagePlus, ColorTable)

   


.. py:method:: ascii(ImagePlus, boolean, int, int)

   Converts the specified image into ascii art.


.. py:method:: binarize(ImagePlus, double, double)

   Binarize an ImagePlus using lower and upper thresholds. Pixels within [lower, upper] become 255 (white), others become 0 (black).


.. py:method:: calibrationToAxes(Calibration, int)

   Creates ImgPlus axes from IJ1 Calibration


.. py:method:: combineSkeletons(Collection)

   


.. py:method:: convertRGBtoComposite(ImagePlus)

   


.. py:method:: convertTo16bit(ImagePlus)

   


.. py:method:: convertTo32bit(ImagePlus)

   


.. py:method:: convertTo8bit(ImagePlus)

   


.. py:method:: convertToSimple2D(ImagePlus, int)

   Converts the specified image into an easy displayable form, i.e., a non-composite 2D image If the image is a timelapse, only the first frame is considered; if 3D, a MIP is retrieved; if multichannel, an RGB version is obtained. The image is flattened if its Overlay has ROIs.


.. py:method:: create(String, int, int, int, int)

   


.. py:method:: crop(ImagePlus, Number)

   Crops the image around non-background values. Does nothing if the image does not have non-background values.


.. py:method:: demo(String)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.


.. py:method:: forgetTags(ImagePlus)

   Removes ``imp`` from both the materialized-crop and display-canvas tag registries. Call once an image is known to be closed/discarded, for deterministic (rather than GC-timed) cleanup; harmless if ``imp`` was never tagged.


.. py:method:: fromBufferedImage(String, BufferedImage)

   


.. py:method:: imageTypeToString(int)

   


.. py:method:: invertLut(ImagePlus)

   


.. py:method:: mergeChannels(Object[])

   Script-friendly method for merging separate channels into a multichannel composite image.


.. py:method:: nextZoomLevel(double)

   


.. py:method:: open(File)

   


.. py:method:: previousZoomLevel(double)

   


.. py:method:: removeIsolatedPixels(ImagePlus)

   


.. py:method:: removeSlices(ImageStack, Collection)

   


.. py:method:: rotate90(ImagePlus, String)

   Rotates an image 90 degrees.


.. py:method:: sameCTDimensions(ImagePlus, ImagePlus)

   


.. py:method:: sameCalibration(ImagePlus, ImagePlus)

   


.. py:method:: sameXYZDimensions(ImagePlus, ImagePlus)

   


.. py:method:: toDataset(ImagePlus)

   


.. py:method:: toImgPlus(ImagePlus)

   Convert an ImagePlus to an ImgPlus with calibration and origin metadata.

   Creates an ImgPlus with proper axis types (X, Y, Z, Channel, Time) and transfers calibration including pixel sizes, units, and origin offsets.


.. py:method:: toImgPlus3D(ImagePlus, int, int)

   Convert an ImagePlus to a 3D (XYZ) ImgPlus, extracting a single channel/frame if needed.

   Useful for analysis that expects simple 3D images without channel/time dimensions.


.. py:method:: toStack(Collection)

   


.. py:method:: zoomTo(ImagePlus, Collection)

   Zooms the image canvas to the specified magnification level, centered on the bounding box of the given paths.


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.ImpUtils>`_
* `ImpUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/ImpUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
