
``CrossoverFinder`` Class Documentation
====================================


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

Utility to detect crossover locations between paths: spatially close locations between paths that look like intersections in the image but are not topological joins in the traced graph.

Here, a crossover is defined as a spatial location where two distinct paths approach within a distance threshold (in real units) for at least minRunNodes consecutive node pairs, but do not share an actual tracing node at that location. Optional geometric filtering by crossing angle is supported.

Usage: 
```
CrossoverFinder.Config cfg = new CrossoverFinder.Config()
      .proximity(2.0)          // spatial threshold in spatially calibrated units (e.g., microns)
      .thetaMinDeg(25)         // optional minimum crossing angle (0 to disable)
      .minRunNodes(2)          // consecutive near-node pairs to accept a crossover event candidate
      .sameCTOnly(true)        // ignore pairs from different channel/time
      .includeSelfCrossovers(false) // whether crossover events within the same path should be detected
  List<CrossoverFinder.CrossoverEvent> events = CrossoverFinder.find(paths, cfg);
```


Methods
-------


Other Methods
~~~~~~~~~~~~~


.. py:method:: static find(Collection, CrossoverFinder$Config)

   Entry point: detect crossover events for a collection of paths using the given config.


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.CrossoverFinder>`_
* `CrossoverFinder JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/CrossoverFinder.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
