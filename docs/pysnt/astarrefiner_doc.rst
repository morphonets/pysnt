
``AStarRefiner`` Class Documentation
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


**Package:** ``sc.fiji.snt``

Post-hoc A* re-tracing of a single, already-existing Path: treats the path's current nodes as waypoints and re-derives the geometry between them via 
```
SNT.autoTraceSync(List, sc.fiji.snt.util.PointInImage, SNT.SearchSettingsSnapshot)
```
, using either the cost function/search parameters currently configured on the active SNT instance, or a frozen `SNT.SearchSettingsSnapshot` shared across a whole batch (see `AStarRefiner(SNT, Path, SNT.SearchSettingsSnapshot)`).

Intended for manually-traced paths against data streamed from disk/network, where running A* interactively may be too slow to be practical. See PathManagerUI's "Refine" menu ("Re-trace with A*...").

call() is thread-safe for parallel execution across paths (it does not modify the original path, and calls 
```
SNT.autoTraceSync(java.util.List<sc.fiji.snt.util.SNTPoint>, sc.fiji.snt.util.PointInImage)
```
 rather than the interactive tracing entry points, so concurrent workers do not serialize behind the single-threaded pool used by interactive tracing). apply() must be called sequentially afterward to commit the result via `Path.replaceNodes(Path)`, which also reconciles this path's own branch point (if it has a parent) and any of its children's branch points against the new geometry.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getFailureReason()

   Human-readable reason call() failed, or null if it succeeded (or hasn't run yet).


.. py:method:: getPath()

   Returns the original path being re-traced.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: readPreferences()

   No-op: kept for consistency with PathFitter/MultiSpectralRefiner, which read persisted preferences here. A* re-tracing simply reuses whichever search parameters are already configured on the live SNT instance.


Other Methods
~~~~~~~~~~~~~


.. py:method:: apply()

   Applies the re-traced geometry to the original path via `Path.replaceNodes(Path)`. Must be called sequentially (not thread-safe), typically on the EDT after all parallel call() invocations have completed.


.. py:method:: applySettings(AStarRefiner)

   No-op: kept for consistency with the other AbstractRefineHelper workers; there are no per-worker settings to propagate here (see readPreferences()).


.. py:method:: call()

   Runs the A* re-trace on this path's current waypoints. Thread-safe: does not modify the original path. Call apply() afterward (sequentially) to commit results.


.. py:method:: succeeded()

   Whether the re-trace succeeded. Only meaningful after call().


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.AStarRefiner>`_
* `AStarRefiner JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/AStarRefiner.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
