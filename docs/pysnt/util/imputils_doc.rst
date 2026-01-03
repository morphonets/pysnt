
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

Static utilities for handling and manipulation of ImagePluss


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getCT(ImagePlus, int, int)

   


.. py:method:: static getChannel(ImagePlus, int)

   


.. py:method:: static getCurrentImage()

   


.. py:method:: static getForegroundRect(ImagePlus, Number)

   Returns the cropping rectangle around non-background values.


.. py:method:: static getFrame(ImagePlus, int)

   


.. py:method:: static getMIP(Collection)

   


.. py:method:: static getMinMax(ImagePlus)

   


.. py:method:: static getSliceLabels(ImageStack)

   


.. py:method:: static getSystemClipboard(boolean)

   Retrieves an ImagePlus from the system clipboard


.. py:method:: static isBinary(ImagePlus)

   


.. py:method:: static isPointVisible(ImagePlus, int, int)

   Checks if a given point (in image coordinates) is currently visible in an image


.. py:method:: static isVirtualStack(ImagePlus)

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: static setLut(ImagePlus, String)

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static save(ImagePlus, String)

   Saves the specified image.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static applyColorTable(ImagePlus, ColorTable)

   


.. py:method:: static ascii(ImagePlus, boolean, int, int)

   Converts the specified image into ascii art.


.. py:method:: static binarize(ImagePlus, double, double)

   


.. py:method:: static calibrationToAxes(Calibration, int)

   


.. py:method:: static combineSkeletons(Collection, boolean)

   


.. py:method:: static convertRGBtoComposite(ImagePlus)

   


.. py:method:: static convertTo32bit(ImagePlus)

   


.. py:method:: static convertTo8bit(ImagePlus)

   


.. py:method:: static convertToSimple2D(ImagePlus, int)

   Converts the specified image into an easy displayable form, i.e., a non-composite 2D image If the image is a timelapse, only the first frame is considered; if 3D, a MIP is retrieved; if multichannel a RGB version is obtained. The image is flattened if its Overlay has ROIs.


.. py:method:: static create(String, int, int, int, int)

   


.. py:method:: static crop(ImagePlus, Number)

   Crops the image around non-background values. Does nothing if the image does not have non-background values.


.. py:method:: static demo(String)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.


.. py:method:: static imageTypeToString(int)

   


.. py:method:: static invertLut(ImagePlus)

   


.. py:method:: static nextZoomLevel(double)

   


.. py:method:: static open(String, String)

   


.. py:method:: static previousZoomLevel(double)

   


.. py:method:: static removeIsolatedPixels(ImagePlus)

   


.. py:method:: static removeSlices(ImageStack, Collection)

   


.. py:method:: static rotate90(ImagePlus, String)

   Rotates an image 90 degrees.


.. py:method:: static sameCTDimensions(ImagePlus, ImagePlus)

   


.. py:method:: static sameCalibration(ImagePlus, ImagePlus)

   


.. py:method:: static sameXYZDimensions(ImagePlus, ImagePlus)

   


.. py:method:: static toDataset(ImagePlus)

   


.. py:method:: static toImgPlus(ImagePlus)

   


.. py:method:: static toImgPlus3D(ImagePlus, int, int)

   


.. py:method:: static toStack(Collection)

   


.. py:method:: static zoomTo(ImagePlus, Collection)

   


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.ImpUtils>`_
* `ImpUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/ImpUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
