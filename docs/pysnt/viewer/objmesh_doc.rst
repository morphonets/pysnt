
``OBJMesh`` Class Documentation
============================


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

An OBJMesh stores information about a Wavefront .obj mesh loaded into Viewer3D, with access points to its OBJFile and DrawableVBO


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAngleWithLocalDirection(SNTPoint, [D, String, int)

   Computes the angle between a direction vector and the local mesh direction at a point. This is useful for e.g., analyzing how neuronal processes align with the local curvature of surfaces (neuropil meshes).


.. py:method:: getBoundingBox(String)

   Gets the minimum bounding box of this mesh.


.. py:method:: getCentroid(String)

   Returns the spatial centroid of the specified (hemi)mesh.


.. py:method:: getDisplayedHemisphere()

   Returns the currently displayed hemisphere: "left", "right", or "both".


.. py:method:: getDrawable()

   Returns the DrawableVBO associated with this mesh


.. py:method:: getLabel()

   


.. py:method:: getLocalDirection(SNTPoint, String, int)

   Computes the local direction of the mesh at a specific point using nearest neighbor analysis. This method finds the dominant direction of mesh curvature in the local neighborhood of the specified point, which is useful for analyzing how structures align with curved anatomical surfaces.


.. py:method:: getObj()

   Returns the OBJFile associated with this mesh


.. py:method:: getPrincipalAxes(String)

   Computes the principal axes of the mesh using Principal Component Analysis (PCA). The principal axes represent the directions of maximum, medium, and minimum variance in the mesh geometry, providing insight into the overall shape orientation of this mesh.


.. py:method:: getSourceAnnotation()

   Returns the BrainAnnotation (atlas compartment) from which this mesh was retrieved, or null if this mesh was loaded from a standalone file.


.. py:method:: getSymmetryAxis()

   


.. py:method:: getVertices()

   Returns the mesh vertices.


.. py:method:: getVolume()

   Gets the volume of this mesh.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setBoundingBoxColor(String)

   Determines whether the mesh bounding box should be displayed.


.. py:method:: setColor(ColorRGB, double)

   Assigns a color to the mesh.


.. py:method:: setDisplayedHemisphere(String)

   Sets which hemisphere of this mesh is displayed.


.. py:method:: setLabel(String)

   Sets the label for this mesh.


.. py:method:: setSourceAnnotation(BrainAnnotation)

   Associates this mesh with the BrainAnnotation (atlas compartment) it was retrieved from.


.. py:method:: setSymmetryAxis(int)

   Sets the axis defining the symmetry plane of this mesh (e.g., the sagittal plane for most bilateria models), where X=0; Y=1; Z=2;


.. py:method:: setTransparency(double)

   Changes the transparency of this mesh.


.. py:method:: setVolume(double)

   Sets the volume of this mesh.


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: computePrincipalAxes(String)

   Computes the principal axes of this mesh using the new PCAnalyzer. This method replaces the deprecated `getPrincipalAxes(String)` method.


Other Methods
~~~~~~~~~~~~~


.. py:method:: duplicate()

   


.. py:method:: label()

   Gets this mesh label.


.. py:method:: translate(SNTPoint)

   Translates the vertices of this mesh by the specified offset. If mesh is displayed, changes may only occur once scene is rebuilt.


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.OBJMesh>`_
* `OBJMesh JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/OBJMesh.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
