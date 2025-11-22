
``ConvexHullAnalyzer`` Class Documentation
=======================================


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

Class for Convex Hull measurements of a Tree.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: get(String)

   Gets the value of a specific convex hull metric.

Retrieves the computed value for the specified metric name. The metric must be one of the supported metrics returned by supportedMetrics().


.. py:method:: getAnalysis()

   Gets all computed convex hull analysis metrics.

Returns a map containing all the computed convex hull metrics and their values. The metrics are computed lazily and cached for subsequent calls. If the hull cannot be computed, all metrics return NaN.


.. py:method:: getBoundarySize()

   Gets the boundary size (perimeter for 2D hulls or surface area for 3D hulls) of the convex hull.


.. py:method:: getBoxivity()

   Gets the boxivity of the convex hull, which measures how box-like the convex hull is. Values closer to 1 indicate a more box-like shape.


.. py:method:: getCancelReason()

   


.. py:method:: getCentroid()

   


.. py:method:: getCompactness()

   


.. py:method:: getContext()

   


.. py:method:: getEccentricity()

   


.. py:method:: getElongation()

   Gets the elongation of the convex hull, which measures how elongated the convex hull is. Higher values indicate more elongated shapes.


.. py:method:: getHull()

   Gets the convex hull object being analyzed. The hull is initialized if needed.


.. py:method:: getRoundness()

   Gets the roundness of the convex hull, which measures how round or circular the convex hull is. Values closer to 1 indicate a more round shape.


.. py:method:: getSize()

   Gets the size (area or volume) of the convex hull, which is the area for 2D hulls or the volume for 3D hulls.


.. py:method:: getTree()

   Gets the tree being analyzed.


.. py:method:: getUnit(String)

   Returns the physical unit associated with the specified metric.


.. py:method:: isCanceled()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setContext(Context)

   


.. py:method:: setLabel(String)

   Sets the optional description for the analysis


Other Methods
~~~~~~~~~~~~~


.. py:method:: cancel(String)

   


.. py:method:: context()

   


.. py:method:: dump(SNTTable)

   


.. py:method:: static main(String;)

   Main method for testing and demonstration purposes.

Creates a ConvexHullAnalyzer instance using demo data and runs the analysis. This method is primarily used for development and debugging.


.. py:method:: run()

   


.. py:method:: static supportedMetrics()

   Gets the list of metrics supported by ConvexHullAnalyzer.


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.ConvexHullAnalyzer>`_
* `ConvexHullAnalyzer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/ConvexHullAnalyzer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
