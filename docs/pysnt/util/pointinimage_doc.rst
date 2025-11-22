
``PointInImage`` Class Documentation
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


**Package:** ``sc.fiji.snt.util``

Defines a Point in an image, a node of a traced Path. Coordinates are always expressed in real-world coordinates.


Fields
------


**onPath** : ``Path``
    No description available.


**radius** : ``float``
    No description available.


**v** : ``float``
    No description available.


**x** : ``float``
    No description available.


**y** : ``float``
    No description available.


**z** : ``float``
    No description available.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clone()

   Creates a copy of this PointInImage.

This method creates a copy of the point including all properties such as coordinates, value, annotation, and hemisphere information.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnnotation()

   


.. py:method:: getCoordinateOnAxis(int)

   Gets the coordinate along the specified axis.


.. py:method:: getHemisphere()

   


.. py:method:: getPath()

   Returns the Path associated with this node (if any)


.. py:method:: getUnscaledPoint(int)

   Converts the coordinates of this point into pixel units if this point is associated with a Path.


.. py:method:: getX()

   


.. py:method:: getY()

   


.. py:method:: getZ()

   


.. py:method:: isReal()

   


.. py:method:: isSameLocation(PointInImage)

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAnnotation(BrainAnnotation)

   Description copied from interface: SNTPoint


.. py:method:: setHemisphere(char)

   


.. py:method:: setPath(Path)

   Associates a Path with this node


Other Methods
~~~~~~~~~~~~~


.. py:method:: chebyshevDxTo(PointInImage)

   


.. py:method:: chebyshevXYdxTo(PointInImage)

   


.. py:method:: chebyshevZdxTo(PointInImage)

   


.. py:method:: distanceSquaredTo(PointInImage)

   


.. py:method:: distanceTo(PointInImage)

   


.. py:method:: euclideanDxTo(PointInImage)

   


.. py:method:: scale(double, double, double)

   Scales this point coordinates.


.. py:method:: transform(PathTransformer)

   


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.PointInImage>`_
* `PointInImage JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/PointInImage.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
