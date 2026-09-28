
``PathFitter`` Class Documentation
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

Class for fitting circular cross-sections around existing nodes of a Path in order to compute radii (node thickness) and midpoint refinement of existing coordinates. Thread Safety: When fitting multiple paths in parallel: 1. Call call() in parallel (thread-safe) 2. Call applyFit() sequentially (modifies path hierarchy)

Example: 
```
List<PathFitter> fitters = paths.stream()
     .map(p -> new PathFitter(img, p))
     .collect(Collectors.toList());
 <p>
 // Parallel fitting
 fitters.parallelStream().forEach(PathFitter::call);
 <p>
 // Sequential application
 fitters.forEach(PathFitter::applyFit);
```


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getPath()

   


.. py:method:: getSucceeded()

   Checks whether the fit succeeded.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setCrossSectionRadius(double)

   Sets the radius of cross-sectional planes sampled around each node.

At each node, PathFitter samples a square cross-section perpendicular to the path tangent. This radius controls the physical extent of that sampling.


.. py:method:: setImage(RandomAccessibleInterval)

   Sets the target image


.. py:method:: setNodeRadiusFallback(int)

   Sets the fallback strategy for node radii at locations where fitting failed.

When cross-section fitting fails at a node (e.g., low SNR, ambiguous geometry), this strategy determines what radius value to assign to that node.


.. py:method:: setProgressCallback(int, MultiTaskProgress)

   


.. py:method:: setReplaceNodes(boolean)

   Sets whether fitting should occur "in place".


.. py:method:: setScope(int)

   Sets the fitting scope.


.. py:method:: setShowAnnotatedView(boolean)

   Sets whether an interactive image of the result should be displayed.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: readPreferences()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: applyFit()

   Applies the fitted result to the path. For multithreaded processing: Must be called sequentially after all parallel fitting is complete.


.. py:method:: applySettings(PathFitter)

   


.. py:method:: call()

   Takes the signal from the image specified in the constructor to fit cross-section circles around the nodes of input path. Computation of fit is confined to the neighborhood specified by `setCrossSectionRadius(double)`.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.PathFitter>`_
* `PathFitter JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathFitter.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
