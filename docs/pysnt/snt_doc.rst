
``SNT`` Class Documentation
========================


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


**Package:** ``sc.fiji.snt``

Implements the SNT plugin.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: closeAndResetAllPanes()

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAverageSeparation()

   


.. py:method:: getChannel()

   


.. py:method:: getContext()

   


.. py:method:: getCostType()

   


.. py:method:: getCurrentPath()

   


.. py:method:: getDataset()

   Gets the Image being traced as Dataset. If the loaded image has been closed, cached pixel data is returned as per getLoadedDataAsImp(). If no resident ImagePlus exists at all (e.g., data streamed from disk/network, backed only by ctSlice3d), a Dataset is instead built directly from `getLoadedDataAsImg(boolean)`, so Dataset-only commands. Null is returned if no image data exists at all.

NB: in the streamed-data fallback, the returned Dataset only ever contains a single channel/ frame (whichever is currently active): ctSlice3d is a single C/T slice by construction. Commands that need every channel or frame simultaneously will still require a resident ImagePlus.

NB2: a materialized crop (see isMaterializedCrop()) always has a resident ImagePlus (the crop itself), so it never takes the streamed-data fallback above, returning the crop's own Dataset as-is, matching whatever `buildMaterializedCrop(BoundingBox)` captured (see `getMaterializedCropChannel()`/`getMaterializedCropFrame()`).


.. py:method:: getDepth()

   


.. py:method:: getDrawDiameters()

   


.. py:method:: getFilledBinaryImp()

   


.. py:method:: getFilledDistanceImp()

   


.. py:method:: getFilledImp()

   


.. py:method:: getFilledLabelImp()

   


.. py:method:: getFilterType()

   


.. py:method:: getFrame()

   


.. py:method:: getHeight()

   


.. py:method:: getHeuristicType()

   


.. py:method:: getImagePlus()

   Gets the Image associated with a view pane.


.. py:method:: getLoadedData()

   


.. py:method:: getLoadedDataAsImp()

   Retrieves the pixel data of the main image currently loaded in memory as an ImagePlus object. Returned image is always a single channel image.


.. py:method:: getLoadedIterable()

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: captureView(String, ColorRGB)

   Retrieves a WYSIWYG 'snapshot' of a tracing canvas without voxel data.


Other Methods
~~~~~~~~~~~~~


.. py:method:: accessToValidImageData()

   Checks whether valid image data exists.


.. py:method:: addFillerThread(FillerThread)

   


.. py:method:: addListener(SNTListener)

   


.. py:method:: autoTrace(SNTPoint, SNTPoint, PointInImage)

   Automatically traces a path from a point A to a point B. See `autoTrace(List, PointInImage)` for details.


.. py:method:: cancelPath()

   Cancels the temporary path.


.. py:method:: cancelSearch(boolean)

   


.. py:method:: cancelTemporary()

   


.. py:method:: changeUIState(int)

   


.. py:method:: confirmTemporary(boolean)

   


.. py:method:: createCanvas(ImagePlus, int)

   


.. py:method:: disableEventsAllPanes(boolean)

   Sets or clears the channel/frame lock described in `getBatchRetraceChannelFrame()`.


.. py:method:: disableZoomAllPanes(boolean)

   


.. py:method:: editModeAllowed()

   Checks if edit mode can be enabled, optionally using a specific path.


.. py:method:: enableAstar(boolean)

   Toggles the A* search algorithm (enabled by default)


.. py:method:: enableAutoActivation(boolean)

   


.. py:method:: enableAutoSelectionOfFinishedPath(boolean)

   


.. py:method:: enableSecondaryLayerTracing(boolean)

   


.. py:method:: enableSnapCursor(boolean)

   Enables SNT's XYZ snap cursor feature. Does nothing if no image data is available or currently loaded image is binary


.. py:method:: findPointInStack(int, int, int, [I)

   


.. py:method:: findPointInStackPrecise(double, double, int, [D)

   


.. py:method:: finished(SearchInterface, boolean)

   


.. py:method:: flushSecondaryData()

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNT>`_
* `SNT JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNT.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
