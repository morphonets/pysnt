
``Fill`` Class Documentation
=========================


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

Defines a filled structure.


Fields
------


**distanceThreshold** : ``float``
    No description available.


**metric** : ``Any``
    No description available.


**spacing_units** : ``str``
    No description available.


**x_spacing** : ``float``
    No description available.


**y_spacing** : ``float``
    No description available.


**z_spacing** : ``float``
    No description available.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getEstimatedMeanRadius()

   Returns the estimated mean radius of the fill, assuming a cylindric shape


.. py:method:: getMetric()

   


.. py:method:: getNodeList()

   Returns the list of nodes in the filled structure.


.. py:method:: getSourcePaths()

   Returns the set of source paths for the filled structure.


.. py:method:: getSourcePathsStringHuman()

   


.. py:method:: getSourcePathsStringMachine()

   


.. py:method:: getThreshold()

   


.. py:method:: getVolume()

   Returns the Fill volume. It assumes that the volume is just the number of sub-threshold nodes multiplied by x_spacing * y_spacing * z_spacing.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setMetric(SNT$CostType)

   Sets the cost metric for the filled structure.


.. py:method:: setSourcePaths(Path;)

   Sets the source paths for the filled structure using a set of paths.


.. py:method:: setSpacing(double, double, double, String)

   


.. py:method:: setThreshold(double)

   Sets the distance threshold for the filled structure.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: writeNodesXML(PrintWriter)

   


.. py:method:: writeXML(PrintWriter, int)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(int, int, int, double, int, boolean)

   Adds a node to the filled structure.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.Fill>`_
* `Fill JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/Fill.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
