
``StrahlerAnalyzer`` Class Documentation
=====================================


.. toctree::
   :maxdepth: 3
   :caption: Complete API Reference
   :hidden:

   ../../api_auto/index
   ../../api_auto/pysnt
   ../../api_auto/pysnt.analysis
   ../../api_auto/pysnt.analysis.graph
   ../../api_auto/pysnt.analysis.growth
   ../../api_auto/pysnt.analysis.sholl
   ../../api_auto/pysnt.analysis.sholl.gui
   ../../api_auto/pysnt.analysis.sholl.math
   ../../api_auto/pysnt.analysis.sholl.parsers
   ../../api_auto/pysnt.annotation
   ../../api_auto/pysnt.converters
   ../../api_auto/pysnt.converters.chart_converters
   ../../api_auto/pysnt.converters.core
   ../../api_auto/pysnt.converters.enhancement
   ../../api_auto/pysnt.converters.extractors
   ../../api_auto/pysnt.converters.graph_converters
   ../../api_auto/pysnt.converters.structured_data_converters
   ../../api_auto/pysnt.core
   ../../api_auto/pysnt.display
   ../../api_auto/pysnt.display.core
   ../../api_auto/pysnt.display.data_display
   ../../api_auto/pysnt.display.utils
   ../../api_auto/pysnt.display.visual_display
   ../../api_auto/pysnt.gui
   ../../api_auto/pysnt.gui.cmds
   ../../api_auto/pysnt.io
   ../../api_auto/pysnt.tracing
   ../../api_auto/pysnt.tracing.artist
   ../../api_auto/pysnt.tracing.cost
   ../../api_auto/pysnt.tracing.heuristic
   ../../api_auto/pysnt.tracing.image
   ../../api_auto/pysnt.util
   ../../api_auto/pysnt.viewer
   ../../api_auto/pysnt.common_module
   ../../api_auto/pysnt.config
   ../../api_auto/pysnt.gui_utils
   ../../api_auto/pysnt.java_utils
   ../../api_auto/pysnt.setup_utils
   ../../api_auto/method_index


**Package:** ``sc.fiji.snt.analysis``

Enhanced documentation for StrahlerAnalyzer class.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAvgBifurcationRatio())

   


.. py:method:: getAvgContractions())

   


.. py:method:: getAvgExtensionAngle(boolean, int))

   Gets the average relative extension angle for branches of a specific Strahler order.


.. py:method:: getAvgExtensionAngles(boolean))

   Gets a map of average relative extension angles for all Strahler orders.


.. py:method:: getAvgFragmentations())

   


.. py:method:: getBifurcationRatios())

   


.. py:method:: getBranchCounts())

   


.. py:method:: getBranchPointCounts())

   


.. py:method:: getBranches())

   


.. py:method:: getExtensionAngles(boolean))

   Gets a map of relative extension angles for all branches in each Strahler order.


.. py:method:: getGraph())

   


.. py:method:: getHighestBranchOrder())

   


.. py:method:: getLengths())

   


.. py:method:: getRelativeExtensionAngle(Path))

   Computes the relative extension angle for a StrahlerAnalyzer branch by finding the parent direction from the graph structure.


.. py:method:: getRootAssociatedBranches())

   


.. py:method:: getRootNumber())

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: static classify(DirectedWeightedGraph, boolean))

   


.. py:method:: dispose())

   Clears internal caches and mappings to free memory.


.. py:method:: static main(String;))

   


See Also
--------

* `Package API <../../api_auto/pysnt.analysis.html#pysnt.analysis.StrahlerAnalyzer>`_
* `Main API Documentation <../../api_auto/pysnt.analysis#StrahlerAnalyzer>`_
* `StrahlerAnalyzer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/StrahlerAnalyzer.html>`_
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Class Index </api_auto/class_index>`

