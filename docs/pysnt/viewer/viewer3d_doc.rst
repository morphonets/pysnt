
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

Implements SNT's Reconstruction Viewer. Relies heavily on the ``org.jzy3d`` package.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: validate()

   Checks if all drawables in the 3D scene are being rendered properly, rebuilding the entire scene if not. Useful to "hard-reset" the viewer, e.g., to ensure all meshes are redrawn.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnimationAxis()

   Gets the current rotation axis for the live animation.


.. py:method:: getAnimationMode()

   Gets the current animation mode.


.. py:method:: getAnnotation(String)

   Gets the annotation associated with the specified label.


.. py:method:: getAnnotations()

   Returns all annotations added to this viewer.


.. py:method:: getColorCodeLabel()

   Gets the label (measurement and unit, e.g., "Path length (µm)") of the last color coding performed through ``colorCode()``. Useful as legend title.


.. py:method:: getFrame()

   Gets the frame containing this viewer, optionally controlling its visibility.

   Returns the AWT Frame that contains this viewer's 3D canvas and UI components. If no frame exists, one will be created with the specified visibility setting. This method is useful when you need to control whether the viewer window appears immediately or remains hidden for programmatic manipulation.


.. py:method:: getID()

   Returns this Viewer's id.


.. py:method:: getManagerPanel()

   Returns a reference to control panel.


.. py:method:: getMesh(String)

   Gets the mesh associated with the specified label.


.. py:method:: getMeshShadingMode()

   Returns the current mesh shading mode.


.. py:method:: getMeshes()

   Returns all meshes added to this viewer.


.. py:method:: getRecorder(boolean)

   Gets the script recorder for this viewer, optionally creating one if needed.


.. py:method:: getTree(String)

   Gets the tree associated with the specified label.


.. py:method:: getTrees()

   Returns all trees added to this viewer.


.. py:method:: hashCode()

   


.. py:method:: isActive()

   Checks whether this instance is currently active


.. py:method:: isAutoDetectAnimationAxis()

   Returns whether automatic rotation axis detection is enabled.


.. py:method:: isDarkModeOn()

   Checks if scene is being rendered under dark or light background.


.. py:method:: isMeshBackfaceCull()

   Returns whether backface culling is enabled for OBJ meshes.


.. py:method:: isSNTInstance()

   Checks whether this instance is SNT's Reconstruction Viewer.


.. py:method:: isScaleBarDisplayed()

   Checks whether the scale bar is being displayed.


.. py:method:: isSplitDendritesFromAxons()

   Checks whether axons and dendrites of imported Trees are set to be imported as separated objects.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAnatomicalMapping(String)

   Applies a custom anatomical axis mapping to the scene, setting axis labels and the scene's up vector (dorsal direction). This is useful for custom atlases or coordinate systems not covered by the predefined templates.


.. py:method:: setAnimationAxis(RotationAxis)

   Sets the rotation axis for the live animation (double-click spin). Calling this method disables automatic axis detection.


.. py:method:: setAnimationEnabled(boolean)

   Toggles the Viewer's animation.


.. py:method:: setAnimationMode(AnimationMode)

   Sets the animation mode for both live (double-click) and recorded rotations.


.. py:method:: setAutoDetectAnimationAxis(boolean)

   Enables or disables automatic detection of the best rotation axis based on the current viewpoint. When enabled (the default), double-clicking to start a live animation will infer the most natural axis by picking the world axis most aligned with the camera's viewing direction. Calling ``setAnimationAxis(RotationAxis)`` disables auto-detection.


.. py:method:: setAxesLabels(String[])

   Sets custom labels for the 3D coordinate axes.


.. py:method:: setBounds(float, float, float, float, float, float)

   Sets a manual bounding box for the scene. The bounding box determines the zoom and framing of the scene. Current view point is logged to the Console when interacting with the Reconstruction Viewer in debug mode.


.. py:method:: setDefaultColor(ColorRGB)

   Sets the default color for rendering `Tree`s.


.. py:method:: setDefaultThickness(float)

   Sets the line thickness for rendering `Tree`s that have no specified radius. Must be called *before* adding paths to the scene.


.. py:method:: setDepthFog(boolean)

   Enables or disables depth fog for all trees (current and future). The preference is persisted across sessions.


.. py:method:: setEnableAxes(boolean)

   Enables/disables the display of X,Y,Z axis grid.


.. py:method:: setEnableDarkMode(boolean)

   Enables/disables "Dark Mode" mode


.. py:method:: setEnableDebugMode(boolean)

   Enables/disables debug mode


.. py:method:: setFogIntensity(float)

   Sets the fog intensity for all trees and persists the preference.


.. py:method:: setFont(Font, float, ColorRGB)

   Sets the font for label annotations


.. py:method:: setFrameSize(int, int)

   Resizes the viewer to the specified dimensions. Useful when generating scene animations programmatically. Does nothing if viewer's frame does not exist.


.. py:method:: setLabelLocation(float, float)

   Sets the location for annotation labels


.. py:method:: setLookAndFeel(String)

   


.. py:method:: setMeshBackfaceCull(boolean)

   Enables or disables backface culling for all OBJ meshes (current and future). Backface culling skips rendering of back-facing triangles, improving performance for closed meshes. The preference is persisted across sessions.


.. py:method:: setMeshShadingMode(int)

   Sets the shading mode for all OBJ meshes (current and future). The preference is persisted across sessions.


.. py:method:: setPseudoLighting(boolean)

   Enables or disables pseudo-lighting for all trees (current and future). Mutually exclusive with depth fog. Enabling this disables fog.


.. py:method:: setRadiusScale(float)

   Applies a tube radius scale to a subset of rendered trees.


.. py:method:: setScaleBarDisplayed(boolean)

   Toggles the display of a scale bar in the bottom-left corner of the scene. The scale bar assumes that scene coordinates are in micrometers, unless a different unit has been specified through ``setScaleBarUnit(String)``.


.. py:method:: setScaleBarUnit(String)

   Sets the base unit of the scene coordinates, used to compute the scale bar length. The unit is parsed by ``BoundingBox.sanitizedUnit(String)``, so common aliases (e.g., "um", "micron") are accepted.


.. py:method:: setSceneUpdatesEnabled(boolean)

   Sets whether the scene should update (refresh) every time a new reconstruction (or mesh) is added/removed from the scene.


.. py:method:: setSnapshotDir(String)

   Sets the directory for storing snapshots.


.. py:method:: setSomaRadius(float)

   Applies a constant radius to the somas of a subset of rendered trees.


.. py:method:: setSomasDisplayed(boolean)

   Toggles the visibility of somas for all trees in the scene.


.. py:method:: setSplitDendritesFromAxons(boolean)

   Sets whether axons and dendrites should be imported as separated objects.


.. py:method:: setTitle(String)

   Sets the title of the Viewer's frame.


.. py:method:: setTreeColor(Collection, ColorRGB, String)

   Recolors a subset of rendered trees.


.. py:method:: setTreeThickness(float)

   Applies a constant thickness (line width) to all rendered trees.Note that by default, trees are rendered using their nodes' diameter.


.. py:method:: setTubeMode(boolean)

   Enables or disables tube rendering for all trees (current and future). The preference is persisted across sessions.


.. py:method:: setTubeSides(int)

   Sets the number of sides for tube cross-sections for all trees. Only has a visual effect when tube rendering is active. The preference is persisted across sessions.


.. py:method:: setTubeWireframe(boolean)

   Enables or disables the wireframe overlay on tube rendering for all trees. The preference is persisted across sessions.


.. py:method:: setUpsamplingFactor(int)

   Sets the Catmull-Rom upsampling factor for all trees and rebuilds them. 1 = no smoothing, higher = smoother paths at vertex joints.


.. py:method:: setViewMode(String)

   Renders the scene from a specified camera angle (script-friendly).


.. py:method:: setViewPoint(double, double)

   Renders the scene from a specified camera angle using polar coordinates relative to the center of the scene. Only X and Y dimensions are required, as the distance to center is automatically computed. Current view point is logged to the Console by calling ``logSceneControls()``.


.. py:method:: setViewPointCC(double, double)

   Calls ``setViewPoint(double, double)`` using Cartesian coordinates.


.. py:method:: setVisible(String, boolean)

   Toggles the visibility of a rendered Tree, a loaded OBJ mesh, or an annotation.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: resetView()

   Resets the view to its default position and orientation.

   This method restores the camera to its initial position, orientation, and zoom level, providing a consistent starting point for viewing the scene.


.. py:method:: show()

   Displays the viewer under specified dimensions. Useful when generating scene animations programmatically.


.. py:method:: showMessage(String, boolean)

   Displays a short message in the viewer's canvas.


.. py:method:: updateView()

   Updates the scene bounds to ensure all visible objects are displayed.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: loadMesh(String, ColorRGB, double)

   Loads a Wavefront .OBJ file. Files should be loaded _before_ displaying the scene, otherwise, if the scene is already visible, ``validate()`` should be called to ensure all meshes are visible.


.. py:method:: loadRefBrain(String)

   Loads the surface mesh of a supported reference brain/neuropil. Internet connection may be required.


.. py:method:: saveScene(File, boolean)

   Saves the contents of the scene to a directory: reconstructions as ``.traces`` files and meshes as ``.obj`` files (with a companion ``.mtl`` file storing their color). Annotations are currently not saved.


.. py:method:: saveSnapshot()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(Object)

   Script friendly method to add a supported object (``Tree``, ``OBJMesh``, AbstractDrawable, etc.) to this viewer. Note that collections of supported objects are also supported, which is an effective way of adding multiple items since the scene is only rebuilt once all items have been added.


.. py:method:: addColorBarLegend(ColorMapper)

   Adds a color bar legend (LUT ramp) with a title.


.. py:method:: addLabel(String)

   Adds an annotation label to the scene.


.. py:method:: addMesh(OBJMesh)

   Loads a Wavefront .OBJ file. Should be called before_ displaying the scene, otherwise, if the scene is already visible, ``validate()`` should be called to ensure all meshes are visible.


.. py:method:: addTree(Tree)

   Adds a tree to this viewer. Note that calling ``updateView()`` may be required to ensure that the current View's bounding box includes the added Tree.


.. py:method:: addTrees(Collection, String)

   


.. py:method:: annotateLine(Collection, String)

   Adds a line annotation to this viewer.


.. py:method:: annotateMidPlane(BoundingBox, int, String)

   


.. py:method:: annotatePlane(SNTPoint, SNTPoint, String)

   


.. py:method:: annotatePoint(SNTPoint, String)

   Adds a highlighting point annotation to this viewer.


.. py:method:: annotatePoints(Collection, String)

   Adds a scatter (point cloud) annotation to this viewer.


.. py:method:: annotateSurface(Collection, String)

   Computes a convex hull from a collection of points and adds it to the scene as an annotation.


.. py:method:: assignUniqueColors(Collection)

   


.. py:method:: colorCode(Collection, String, ColorTable)

   Runs ``TreeColorMapper`` on the specified ``Tree``.


.. py:method:: dispose()

   Closes and releases all the resources used by this viewer.


.. py:method:: duplicate()

   Creates a duplicate of this viewer containing only visible objects.

   This method creates a new Viewer3D instance and copies all currently visible objects (trees, meshes, annotations) from this viewer to the new one. The duplicate viewer maintains the same visual settings and object properties but operates independently from the original.


.. py:method:: equals(Object)

   


.. py:method:: freeze()

   Does not allow scene to be interactive. Only static orthogonal views allowed.


.. py:method:: logSceneControls()

   Logs API calls controlling the scene (view point, bounds, etc.) to Script Recorder (or Console if Script Recorder is not running). Useful for programmatic control of animations.


.. py:method:: mergeAnnotations(Collection, String)

   Merges a collection of annotations into a single object.


.. py:method:: rebuild(Object)

   Rebuilds (repaints) a scene object (e.g., a Tree after being modified elsewhere)


.. py:method:: recordRotation(float, int, File)

   Records an animated rotation of the scene around the specified axis as a sequence of images.


.. py:method:: remove(Object)

   Script friendly method to remove an object (``Tree``, ``OBJMesh``, AbstractDrawable, ``String`` (object label), etc.) from this viewer's scene.


.. py:method:: removeAllMeshes()

   Removes all loaded OBJ meshes from current viewer


.. py:method:: removeAllTrees()

   Removes all the Trees from current viewer


.. py:method:: removeAnnotation(Annotation3D)

   Removes the specified annotation from the viewer.


.. py:method:: removeMesh(OBJMesh)

   Removes the specified OBJ mesh.


.. py:method:: removeTree(String)

   Removes the specified Tree.


.. py:method:: rotate(float)

   Rotates the scene.


.. py:method:: runCommand(String)

   


.. py:method:: snapshot()

   Retrieves the specified scene view as an image.


.. py:method:: snapshotWYSIWYG()

   Retrieves the current scene as an image using a screen capture that matches the on-screen rendering exactly (WYSIWYG). This bypasses the OpenGL framebuffer readback, avoiding color discrepancies from premultiplied alpha and display color management. Falls back to ``snapshot()`` when the viewer is not visible (e.g., offscreen rendering or headless environments).


.. py:method:: syncPathManagerList()

   (Re)loads the current list of Paths in the Path Manager list.


.. py:method:: translate(Collection, SNTPoint)

   Translates the specified collection of `Tree`s.


.. py:method:: unfreeze()

   Allows scene to be interactive.


.. py:method:: updateColorBarLegend(double, double)

   Updates all the properties of the existing color bar legend. Does nothing if no legend exists.


.. py:method:: zoomTo(Object[])

   Zooms the scene into the bounding box enclosing the specified objects.


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.Viewer3D>`_
* `Viewer3D JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Viewer3D.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
