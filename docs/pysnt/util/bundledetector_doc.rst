
``BundleDetector`` Class Documentation
===================================


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

Detects regions where two paths run parallel to each other for a sustained distance, complementary to CrossoverFinder (which catches brief perpendicular near-crossings). Common use case: identifying axons bundled along the same nerve, or a path that was inadvertently hijacked by signal from a neighboring neurite running side-by-side.

This is a thin wrapper over CrossoverFinder: it reuses the entire grid/proximity/run-extraction pipeline and only inverts the angle filter. Where CrossoverFinder (with thetaMinDeg > 0) keeps only high-angle approaches (X-shaped crossings), BundleDetector uses thetaMaxDeg > 0 to keep only low-angle approaches (||-shaped sustained proximity). Defaults are also tuned for sustained runs: higher minRunNodes, similar proximity.

The output type is `CrossoverFinder.CrossoverEvent`: Callers should interpret the events as "bundled run" regions rather than crossings; the medianAngleDeg field will be small (parallel), and the index-window span will be wide (sustained).


Methods
-------


Other Methods
~~~~~~~~~~~~~


.. py:method:: static find(Collection, BundleDetector$Config)

   Entry point: detect bundle events for a collection of paths using the given config. Internally constructs a `CrossoverFinder.Config` ith the inverted angle filter (`CrossoverFinder.Config.thetaMaxDeg` set, `CrossoverFinder.Config.thetaMinDeg` disabled) and delegates to 
```
CrossoverFinder.find(java.util.Collection<sc.fiji.snt.Path>, sc.fiji.snt.util.CrossoverFinder.Config)
```
.


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.BundleDetector>`_
* `BundleDetector JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/BundleDetector.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
