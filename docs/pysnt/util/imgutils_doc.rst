
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


.. py:method:: static getCalibration(ImgPlus)

   


.. py:method:: static getCtSlice(Dataset, int, int)

   


.. py:method:: static getCtSlice3d(ImagePlus, int, int)

   Get a view of the ImagePlus at the specified channel and frame.


.. py:method:: static getOrigin(ImgPlus, AxisType)

   


.. py:method:: static getOrigins(ImgPlus)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: static createIntervals([J, [J)

   Partition the source dimensions into a list of Intervals with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have slightly different dimensions.


.. py:method:: static crop(ImgPlus, [J, [J, boolean)

   


.. py:method:: static dropSingletonDimensions(ImgPlus)

   


.. py:method:: static findSpatialAxisIndices(ImgPlus)

   


.. py:method:: static findSpatialAxisIndicesWithFallback(ImgPlus)

   


.. py:method:: static imgPlusToCalibration(ImgPlus)

   


.. py:method:: static impToRealRai5d(ImagePlus)

   Wrap an ImagePlus to a `RandomAccessibleInterval` such that the number of dimensions in the resulting rai is 5 and the axis order is XYCZT. Axes that are not present in the input imp have singleton dimensions in the rai.

For example, given a 2D, multichannel imp, the dimensions of the result rai are [ |X|, |Y|, |C|, 1, 1 ]


.. py:method:: static maxDimension([J)

   


.. py:method:: static outOfBounds([J, [J, [J)

   Checks if pos is outside the bounds given by min and max


.. py:method:: static raiToImp(RandomAccessibleInterval, String)

   Convert a `RandomAccessibleInterval` to an ImagePlus. If the input has 3 dimensions, the 3rd dimension is treated as depth.


.. py:method:: static splitIntoBlocks(RandomAccessibleInterval, [J)

   Partition the source rai into a list of IntervalView with given dimensions. If the block dimensions are not multiples of the image dimensions, some blocks will have truncated dimensions.


.. py:method:: static subInterval(RandomAccessibleInterval, Localizable, Localizable, long)

   Get an N-D sub-interval of an N-D image, given two corner points and specified padding. If necessary, the computed sub-interval is clamped at the min and max of each dimension of the input interval.


.. py:method:: static subVolume(RandomAccessibleInterval, long, long, long, long, long, long, long)

   Get a 3D sub-volume of an image, given two corner points and specified padding. If the input is 2D, a singleton dimension is added. If necessary, the computed sub-volume is clamped at the min and max of each dimension of the input interval.


.. py:method:: static toImagePlus(ImgPlus)

   


.. py:method:: static wrapWithAxes(RandomAccessibleInterval, ImgPlus, String)

   


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.ImgUtils>`_
* `ImgUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/ImgUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
