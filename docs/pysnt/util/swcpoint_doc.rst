
``SWCPoint`` Class Documentation
=============================


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


**Package:** ``sc.fiji.snt.util``

Enhanced documentation for SWCPoint class.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clone())

   


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnnotation())

   


.. py:method:: getColor())

   Gets the color of this point.


.. py:method:: getCoordinateOnAxis(int))

   


.. py:method:: getHemisphere())

   


.. py:method:: getNextPoints())

   Returns the list holding the subsequent nodes in the reconstructed structure after this one.


.. py:method:: getPath())

   


.. py:method:: getTags())

   Gets the tags associated with this point.


.. py:method:: getUnscaledPoint())

   


.. py:method:: getX())

   


.. py:method:: getY())

   


.. py:method:: getZ())

   


.. py:method:: isReal())

   


.. py:method:: isSameLocation(PointInImage))

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAnnotation(BrainAnnotation))

   Description copied from interface: SNTPoint


.. py:method:: setColor(Color))

   Sets the color of this point.


.. py:method:: setHemisphere(char))

   


.. py:method:: setPath(Path))

   


.. py:method:: setPrevious(SWCPoint))

   Sets the preceding node in the reconstruction


.. py:method:: setTags(String))

   Sets the tags associated with this point.


Other Methods
~~~~~~~~~~~~~


.. py:method:: chebyshevDxTo(PointInImage))

   


.. py:method:: chebyshevXYdxTo(PointInImage))

   


.. py:method:: chebyshevZdxTo(PointInImage))

   


.. py:method:: static collectionAsReader(Collection))

   Converts a collection of SWC points into a Reader.


.. py:method:: compareTo(SWCPoint))

   


.. py:method:: distanceSquaredTo(double, double, double))

   


.. py:method:: distanceTo(PointInImage))

   


.. py:method:: euclideanDxTo(PointInImage))

   


.. py:method:: static flush(Collection, PrintWriter))

   Prints a list of points as space-separated values.


.. py:method:: previous())

   Returns the preceding node (if any)


.. py:method:: scale(double, double, double))

   


.. py:method:: transform(PathTransformer))

   


.. py:method:: xSeparationFromPreviousPoint())

   Returns the X-distance from previous point.


.. py:method:: ySeparationFromPreviousPoint())

   Returns the Y-distance from previous point.


.. py:method:: zSeparationFromPreviousPoint())

   Returns the Z-distance from previous point.


See Also
--------

* `Package API <../../api_auto/pysnt.util.html#pysnt.util.SWCPoint>`_
* `Main API Documentation <../../api_auto/pysnt.util#SWCPoint>`_
* `SWCPoint JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SWCPoint.html>`_
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Class Index </api_auto/class_index>`

