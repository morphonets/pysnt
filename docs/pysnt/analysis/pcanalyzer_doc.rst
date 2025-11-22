
``PCAnalyzer`` Class Documentation
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


**Package:** ``sc.fiji.snt.analysis``

Utility class for performing Principal Component Analysis (PCA) on various SNT data structures including Trees, Paths, and collections of SNTPoints.

This class provides methods to compute the principal axes of 3D point data, which represent the directions of maximum variance in the data. This is useful for analyzing the overall orientation and shape characteristics of neuronal structures, meshes, and other 3D geometries.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getPrincipalAxes(Collection)

   Computes the principal axes for a collection of SNTPoints.


.. py:method:: static getVariancePercentages(PCAnalyzer$PrincipalAxis;)

   Computes the variance percentages for an array of principal axes. This is a convenience method that returns the percentage of total variance explained by each principal axis.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static orientTowardDirection(PCAnalyzer$PrincipalAxis;, [D)

   Orients principal axes so the primary axis points toward a reference direction, i.e., the primary axis is oriented to minimize the angle with the reference direction. If the primary axis points away from the reference (dot product < 0), it's flipped.\


.. py:method:: static orientTowardTips(PCAnalyzer$PrincipalAxis;, Tree)

   Convenience method to orient existing principal axes toward a tree's tips centroid. For several topologies, this orients the primary axis is so it aligns with the general growth direction of the arbor.


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.PCAnalyzer>`_
* `PCAnalyzer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/PCAnalyzer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
