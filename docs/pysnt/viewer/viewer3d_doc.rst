
``Viewer3D`` Class Documentation
=============================


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

Implements SNT's Reconstruction Viewer. Relies heavily on the org.jzy3d package.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnnotation(String)

   Gets the annotation associated with the specified label.


.. py:method:: getAnnotations()

   Returns all annotations added to this viewer.


.. py:method:: getFrame()

   Gets the frame containing this viewer, optionally controlling its visibility.

Returns the AWT Frame that contains this viewer's 3D canvas and UI components. If no frame exists, one will be created with the specified visibility setting. This method is useful when you need to control whether the viewer window appears immediately or remains hidden for programmatic manipulation.


.. py:method:: getID()

   Returns this Viewer's id.


.. py:method:: getManagerPanel()

   Returns a reference to 'RV Controls' panel.


.. py:method:: getMesh(String)

   Gets the mesh associated with the specified label.


.. py:method:: getMeshes()

   Returns all meshes added to this viewer.


.. py:method:: getRecorder(boolean)

   Gets the script recorder for this viewer, optionally creating one if needed.


.. py:method:: getTree(String)

   Gets the tree associated with the specified label.


.. py:method:: getTrees()

   Returns all trees added to this viewer.


.. py:method:: isActive()

   Checks whether this instance is currently active


.. py:method:: isDarkModeOn()

   Checks if scene is being rendered under dark or light background.


.. py:method:: isSNTInstance()

   Checks whether this instance is SNT's Reconstruction Viewer.


.. py:method:: isSplitDendritesFromAxons()

   Checks whether axons and dendrites of imported Trees are set to be imported as separated objects.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: loadMesh(String, ColorRGB, double)

   Loads a Wavefront .OBJ file. Files should be loaded _before_ displaying the scene, otherwise, if the scene is already visible, validate() should be called to ensure all meshes are visible.


.. py:method:: loadRefBrain(String)

   Loads the surface mesh of a supported reference brain/neuropil. Internet connection may be required.


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(File;, String)

   Script friendly method to add a supported object (Tree, OBJMesh, AbstractDrawable, etc.) to this viewer. Note that collections of supported objects are also supported, which is an effective way of adding multiple items since the scene is only rebuilt once all items have been added.


.. py:method:: addColorBarLegend(ColorMapper)

   Adds a color bar legend (LUT ramp).


.. py:method:: addLabel(String)

   Adds an annotation label to the scene.


.. py:method:: addMesh(OBJMesh)

   Loads a Wavefront .OBJ file. Should be called before_ displaying the scene, otherwise, if the scene is already visible, validate() should be called to ensure all meshes are visible.


.. py:method:: addTree(Tree)

   Adds a tree to this viewer. Note that calling updateView() may be required to ensure that the current View's bounding box includes the added Tree.


.. py:method:: addTrees(Collection, String, String;)

   


.. py:method:: annotateLine(Collection, String)

   Adds a line annotation to this viewer.


.. py:method:: annotateMidPlane(BoundingBox, int, String)

   


.. py:method:: annotatePlane(SNTPoint, SNTPoint, String)

   


.. py:method:: annotatePoint(SNTPoint, String)

   Adds a highlighting point annotation to this viewer.


.. py:method:: annotatePoints(Collection, String)

   Adds a scatter (point cloud) annotation to this viewer.


.. py:method:: annotateSurface(Collection, String, boolean)

   Computes a convex hull from a collection of points and adds it to the scene as an annotation.


.. py:method:: assignUniqueColors(Collection)

   


.. py:method:: colorCode(Collection, String, ColorTable)

   Runs TreeColorMapper on the specified Tree.


.. py:method:: dispose()

   Closes and releases all the resources used by this viewer.


.. py:method:: duplicate()

   Creates a duplicate of this viewer containing only visible objects.

This method creates a new Viewer3D instance and copies all currently visible objects (trees, meshes, annotations) from this viewer to the new one. The duplicate viewer maintains the same visual settings and object properties but operates independently from the original.


.. py:method:: freeze()

   Does not allow scene to be interactive. Only static orthogonal views allowed.


.. py:method:: logSceneControls()

   Logs API calls controlling the scene (view point, bounds, etc.) to Script Recorder (or Console if Script Recorder is not running). Useful for programmatic control of animations.


.. py:method:: mergeAnnotations(Collection, String)

   Merges a collection of annotations into a single object.


.. py:method:: rebuild(Object)

   Rebuilds (repaints) a scene object (e.g., a Tree after being modified elsewhere)


.. py:method:: recordRotation(float, int, File)

   Records an animated rotation of the scene as a sequence of images.


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.Viewer3D>`_
* `Viewer3D JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Viewer3D.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
