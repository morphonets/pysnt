
``Annotation3D`` Class Documentation
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


**Package:** ``sc.fiji.snt.viewer``

An Annotation3D is a triangulated surface or a cloud of points (scatter) rendered in Viewer3D that can be used to highlight nodes in a Tree or locations in a mesh.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBarycentre()

   Returns the center of this annotation bounding box.


.. py:method:: getColor()

   


.. py:method:: getDrawable()

   Returns the AbstractDrawable associated with this annotation.


.. py:method:: getLabel()

   Gets the annotation label


.. py:method:: getType()

   Gets the type of this annotation.


.. py:method:: getVolume()

   


.. py:method:: isColorCodeAllowed()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setBoundingBoxColor(ColorRGB)

   Determines whether the mesh bounding box should be displayed.


.. py:method:: setColor(String, double)

   Script friendly method to assign a color to the annotation.


.. py:method:: setSize(Number)

   Sets the annotation width.


.. py:method:: setTransparency(double)

   Script friendly method to assign a transparency to the annotation.


.. py:method:: setWireframeColor(String)

   Assigns a wireframe color to the annotation.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static meshToDrawable(Mesh)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: colorCode(String, String)

   


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.Annotation3D>`_
* `Annotation3D JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Annotation3D.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
