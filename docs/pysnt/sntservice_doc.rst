
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

Service for accessing and scripting the active instance of SNT.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnalyzer(boolean)

   


.. py:method:: getContext()

   


.. py:method:: getIdentifier()

   


.. py:method:: getInfo()

   


.. py:method:: getInstance()

   Returns a reference to the active SNT instance.


.. py:method:: getLocation()

   


.. py:method:: getOrCreateSciViewSNT()

   


.. py:method:: getPathAndFillManager()

   Returns the PathAndFillManager associated with the current SNT instance.


.. py:method:: getPaths()

   Gets the paths currently listed in the Path Manager


.. py:method:: getPlugin()

   


.. py:method:: getPriority()

   


.. py:method:: getRecViewer(int)

   Returns a reference to an opened Reconstruction Viewer (standalone instance). *


.. py:method:: getSciViewSNT()

   


.. py:method:: getSelectedPaths()

   Gets the paths currently selected in the Path Manager list.


.. py:method:: getStatistics(boolean)

   Returns a TreeStatistics instance constructed from current Paths.


.. py:method:: getTable()

   Returns a reference to SNT's main table of measurements.


.. py:method:: getTree()

   Gets the collection of paths listed in the Path Manager as a Tree object.


.. py:method:: getTrees()

   Gets the collection of paths listed in the Path Manager as a Tree object.


.. py:method:: getUI()

   Returns a reference to SNT's UI.


.. py:method:: getVersion()

   


.. py:method:: isActive()

   Gets whether SNT is running.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setContext(Context)

   


.. py:method:: setInfo(PluginInfo)

   


.. py:method:: setPriority(double)

   


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

   Loads the specified tree. Note that if SNT has not been properly initialized, spatial calibration mismatches may occur. In that case, assign the spatial calibration of the image to {#@code Tree} using `Tree.assignImage(ImagePlus)`, before loading it.


.. py:method:: save(String)

   Saves all the existing paths to a file.


Other Methods
~~~~~~~~~~~~~


.. py:method:: assignValues(boolean)

   Assigns pixel intensities at each Path node, storing them as Path values. Assigned intensities are those of the channel and time point currently being traced. Assumes SNT has been initialized with a valid image.


.. py:method:: compareTo(Object)

   


.. py:method:: context()

   


.. py:method:: demoImage(String)

   Returns one of the demo images bundled with SNT image associated with the demo (fractal) tree.


.. py:method:: demoTree(String)

   Returns a demo tree.


.. py:method:: demoTreeImage()

   Returns the image associated with the demo (fractal) tree.


.. py:method:: demoTrees()

   Returns a collection of four demo reconstructions (dendrites from pyramidal cells from the MouseLight database). NB: Data is cached locally. No internet connection required.


.. py:method:: dispose()

   Quits SNT. Does nothing if SNT is currently not running.


.. py:method:: initialize(ImagePlus, boolean)

   Initializes SNT.


.. py:method:: log()

   


.. py:method:: registerEventHandlers()

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNTService>`_
* `SNTService JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTService.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
