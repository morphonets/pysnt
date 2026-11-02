
``SNTService`` Class Documentation
===============================


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

Service for accessing and scripting the active instance of ``SNT``.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnalyzer(boolean)

   


.. py:method:: getContext()

   


.. py:method:: getInstance()

   Returns a reference to the active ``SNT`` instance.


.. py:method:: getOrCreateSciViewSNT()

   


.. py:method:: getPathAndFillManager()

   Returns the ``PathAndFillManager`` associated with the current SNT instance.


.. py:method:: getPaths()

   Gets the paths currently listed in the Path Manager


.. py:method:: getPlugin()

   


.. py:method:: getRecViewer()

   Returns a reference to an opened Reconstruction Viewer (standalone instance). *


.. py:method:: getSciViewSNT()

   


.. py:method:: getSelectedPaths()

   Gets the paths currently selected in the Path Manager list.


.. py:method:: getStatistics(boolean)

   Returns a ``TreeStatistics`` instance constructed from current Paths.


.. py:method:: getTable()

   Returns a reference to SNT's main table of measurements.


.. py:method:: getTree()

   Gets the collection of paths listed in the Path Manager as a ``Tree`` object.


.. py:method:: getTrees()

   Gets the collection of paths listed in the Path Manager as a ``Tree`` object.


.. py:method:: getUI()

   Returns a reference to SNT's UI.


.. py:method:: hasUnsavedPaths()

   Checks whether SNT holds paths that have not been saved.


.. py:method:: isActive()

   Gets whether SNT is running.


.. py:method:: isStreamMode()

   Gets whether SNT is currently running in Stream mode ("SNT Stream"), i.e., tethered to a streamed dataset (N5/OME-Zarr/IMS/BDV-XML) via the Big Data Loader, with no in-core ``ImagePlus``/classic canvas available. Several script-facing APIs (ImagePlus-based snapshots, ROI-based inputs, ``SNT#rebuildDisplayCanvases()``, etc.) are not available in this mode. Scripts can use this method to detect that and abort/adapt early.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: newRecViewer(boolean)

   Instantiates a new standalone Reconstruction Viewer.


.. py:method:: updateViewers()

   Script-friendly method for updating (refreshing) all viewers currently in use by SNT. Does nothing if no SNT instance exists.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: loadGraph(DirectedWeightedGraph)

   


.. py:method:: loadTracings(String)

   Loads the specified tracings file.


.. py:method:: loadTree(Tree)

   Loads the specified tree. Note that if SNT has not been properly initialized, spatial calibration mismatches may occur. In that case, assign the spatial calibration of the image to {#@code Tree} using ``Tree.assignImage(ImagePlus)``, before loading it.


.. py:method:: loadTrees(Collection)

   Loads the specified collection of trees.


.. py:method:: save(String)

   Saves all the existing paths to a file.


Other Methods
~~~~~~~~~~~~~


.. py:method:: assignValues(boolean)

   Assigns pixel intensities at each Path node, storing them as Path values. Assigned intensities are those of the channel and time point currently being traced. Assumes SNT has been initialized with a valid image.


.. py:method:: demoImage(String)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.


.. py:method:: demoImgPlus(String)

   Returns one of the demo images bundled with SNT as an ``ImgPlus``. This is the imglib2 counterpart of ``demoImage(String)``.


.. py:method:: demoTree()

   Returns a demo tree.


.. py:method:: demoTreeImage()

   Returns the image associated with the demo (fractal) tree.


.. py:method:: demoTrees()

   Returns a collection of four demo reconstructions (dendrites from pyramidal cells from the MouseLight database). NB: Data is cached locally. No internet connection required.


.. py:method:: dispose()

   Quits SNT. Does nothing if SNT is currently not running.


.. py:method:: initialize(boolean)

   Initializes SNT from an ``ImgPlus`` image. This is the imglib2 counterpart of ``initialize(ImagePlus, boolean)``.


.. py:method:: requireVersion(String)

   Ensures the running SNT version meets a minimum requirement. This is analogous to IJ's ``requires()`` macro function.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNTService>`_
* `SNTService JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTService.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
