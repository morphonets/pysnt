
``PathProfiler`` Class Documentation
=================================


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


**Package:** ``sc.fiji.snt.analysis``

Command to retrieve Path profiles (plots of voxel intensities values along a Path)


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCancelReason()

   


.. py:method:: getContext()

   


.. py:method:: getDelegateObject()

   


.. py:method:: getInfo()

   


.. py:method:: getInput(String)

   


.. py:method:: getInputs()

   


.. py:method:: getOutput(String)

   


.. py:method:: getOutputs()

   


.. py:method:: getPlot()

   Gets the plot profile as an ImageJ plot (all channels included).


.. py:method:: getValues(Path)

   Gets the profile for the specified path as a map of lists, with distances (or indices) stored under X_VALUES ("x-values") and intensities under Y_VALUES ("y-values").


.. py:method:: getXYPlot(int)

   Gets the plot profile as an PlotService plot. It is recommended to call `DynamicCommand.setContext(org.scijava.Context)` beforehand.


.. py:method:: isCanceled()

   


.. py:method:: isInputResolved(String)

   


.. py:method:: isOutputResolved(String)

   


.. py:method:: isResolved(String)

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setContext(Context)

   


.. py:method:: setInput(String, Object)

   


.. py:method:: setInputs(Map)

   


.. py:method:: setMetric(ProfileProcessor$Metric)

   


.. py:method:: setNodeIndicesAsDistances(boolean)

   Sets whether the profile abscissae should be reported in real-word units (the default) or node indices (zero-based). Must be called before calling getValues(Path), getPlot() or getXYPlot().


.. py:method:: setOutput(String, Object)

   


.. py:method:: setOutputs(Map)

   


.. py:method:: setRadius(int)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: preview()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addInput(String, Class)

   


.. py:method:: addOutput(ModuleItem)

   


.. py:method:: assignValues(Path, int)

   Retrieves pixel intensities at each node of the Path storing them as Path values


.. py:method:: cancel(String)

   


.. py:method:: context()

   


.. py:method:: findMaxima(Path, int)

   Finds the maxima in the profile of the specified path.

A maxima (peak) will only be considered if protruding more than the profile's standard deviation from the ridge to a higher maximum


.. py:method:: findMinima(Path, int)

   Finds the minima in the profile of the specified path.

A maxima (peak) will only be considered if protruding less than the profile's standard deviation from the ridge to a lower minimum


.. py:method:: initialize()

   


.. py:method:: static main(String;)

   


.. py:method:: removeInput(ModuleItem)

   


.. py:method:: removeOutput(ModuleItem)

   


.. py:method:: resolveInput(String)

   


.. py:method:: resolveOutput(String)

   


.. py:method:: run()

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.PathProfiler>`_
* `PathProfiler JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/PathProfiler.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
