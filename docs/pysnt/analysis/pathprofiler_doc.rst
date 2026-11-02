
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


.. py:method:: getMultiFrameProfile(List, int, int, boolean)

   Builds a multi-frame intensity profile matrix from a list of matched paths (one per time frame, ordered by frame number), suitable for kymograph-style visualization via 


   ::

       SNTChart.showHeatmap(double[][], net.imglib2.display.ColorTable, java.lang.String...)


   .

   The returned matrix has dimensions [nPaths][nSamples], where ``matrix[i][j]`` is the interpolated intensity at distance sample j for the i-th path. Entries beyond a path's actual length are ``Double.NaN``.


.. py:method:: getPlot()

   Gets the plot profile as an ImageJ plot (all channels included).


.. py:method:: getResampledValues(Path, int, int, double)

   Resamples the intensity profile of a path onto a uniform distance grid via linear interpolation. Entries beyond the path's actual length are set to ``Double.NaN``, which allows variable-length paths to be compared in the same matrix without padding with zeros.


.. py:method:: getTimeProfile(Path, int)

   Gets the time profile for the specified path as a list of ``getValues(Path, int, int)`` profiles, with one entry per frame of the dataset.


.. py:method:: getValues(Path)

   Gets the profile for the specified path as a map of lists, with distances (or indices) stored under ``X_VALUES`` ("x-values") and intensities under ``Y_VALUES`` ("y-values").


.. py:method:: getXYPlot()

   Gets the plot profile as an ``PlotService`` plot. It is recommended to call ``DynamicCommand.setContext(org.scijava.Context)`` beforehand.


.. py:method:: isCanceled()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setMetric(Metric)

   


.. py:method:: setNodeIndicesAsDistances(boolean)

   Sets whether the profile abscissae should be reported in real-word units (the default) or node indices (zero-based). Must be called before calling ``getValues(Path)``, ``getPlot()`` or ``getXYPlot()``.


.. py:method:: setRadius(int)

   


.. py:method:: setShape(Shape)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: assignValues()

   Retrieves pixel intensities at each node of the Path storing them as Path ``values``


.. py:method:: cancel()

   


.. py:method:: findMaxima(Path, int)

   Finds the maxima in the profile of the specified path.

   A maxima (peak) will only be considered if protruding more than the profile's standard deviation from the ridge to a higher maximum


.. py:method:: findMinima(Path, int)

   Finds the minima in the profile of the specified path.

   A maxima (peak) will only be considered if protruding less than the profile's standard deviation from the ridge to a lower minimum


.. py:method:: run()

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.PathProfiler>`_
* `PathProfiler JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/PathProfiler.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
