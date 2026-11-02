
``Bvv`` Class Documentation
========================


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

Support for Big Volume Viewer.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearAllTrees()

   Description copied from class: ``AbstractBigViewer``


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBoundingBox()

   


.. py:method:: getCalibration()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getCurrentTimepoint()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDefaultMarkerColor()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDefaultMarkerSize()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDefaultRenderingStyle()

   


.. py:method:: getDisplayRadii()

   Returns whether paths are currently rendered with per-node radii as tapered frusta (``true``) or as simple lines (``false``).


.. py:method:: getDisplayRange(int)

   


.. py:method:: getDownsamplingFactors(int, int)

   


.. py:method:: getGlobalMouseCoordinates(RealPoint)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getInstance()

   Returns the most recently created ``Bvv`` instance, or ``null`` if none has been created yet. Convenience accessor for scripts.


.. py:method:: getMarkerManager()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getMultiSources()

   Returns all ``BvvMultiSource`` groups currently managed by this viewer. This includes multichannel images and any grouped multi-image sources.


.. py:method:: getNumResolutionLevels(int)

   


.. py:method:: getOptions()

   


.. py:method:: getPhysicalUnit()

   Resolves the physical unit string for the currently loaded volume.


.. py:method:: getPrimarySourcePath()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getRenderSettleTime()

   


.. py:method:: getRenderedTrees()

   


.. py:method:: getRenderingOptions()

   Gets the path rendering options for controlling thickness, transparency, etc.


.. py:method:: getSNT()

   


.. py:method:: getSceneCenter()

   The world-space point currently at the center of this viewer's display: the intensity-peak result of ``findSceneCenterMaxima()`` when available, otherwise the same focal-plane fallback used by ``AbstractBigViewer.getSceneCenter()``.


.. py:method:: getSourceData(int, int)

   


.. py:method:: getSourceName(int)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getSourcePaths()

   


.. py:method:: getViewer()

   


.. py:method:: getViewerCanvas()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerFrame()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerHeight()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerPanel()

   


.. py:method:: getViewerTransform()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerWidth()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: hasMarkerManager()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: isDisposed()

   


.. py:method:: isEditModeEnabled()

   


.. py:method:: isOpen()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: isPathInProgress()

   


.. py:method:: isTracingEnabled()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setCalibration(double[], String)

   Overrides the voxel calibration (spacing and unit) for all loaded sources. This is useful when the image metadata does not carry the correct spatial calibration (e.g., ND2 files opened via SCIFIO/Bio-Formats where the unit string is lost). The change takes effect immediately: the scale bar, distance measurements, and slab-thickness controls will all use the new values.


.. py:method:: setChannelColors(Color[])

   Sets per-channel colors across all source groups, assigning colors sequentially by global channel order across all groups. For example, with two 3-channel images and colors [R, G, B, C, M, Y], image 1 gets R/G/B and image 2 gets C/M/Y. With a single multichannel image or a dataset where each setup is its own group (e.g. IMS), colors are assigned one-to-one in load order.

   To apply the same color pattern to every group independently, call ``setChannelColors(BvvMultiSource, Color...)`` per group.

   Typical script usage: 


   ::

       def bvv = Bvv.open(img)
       bvv.setChannelColors(Color.RED, Color.GREEN, Color.BLUE)





.. py:method:: setCurrentTimepoint(int)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: setDisplayRadii(boolean)

   Sets whether paths are rendered as tapered frusta with per-node radii (``true``) or as anti-aliased lines (``false``). Line rendering is significantly faster for datasets with many paths. Automatically invalidates the overlay cache and repaints.


.. py:method:: setDisplayRange(BvvMultiSource, double, double)

   Sets the display range (min/max intensity) for all channels of a specific source group.


.. py:method:: setPathOverlayOffset(double, double, double)

   Offsets all paths being rendered. This allows for 'dislodging' paths from their underlying signal without altering their coordinates.

   Rendering-only: stored purely in ``renderingOptions.pathOffset`` and read directly by ``OverlayRenderer#computeScreenData``. Does NOT touch ``Path``/``Tree`` state


.. py:method:: setRenderSettleTime(long)

   


.. py:method:: setTracingLockedByPause(boolean)

   


.. py:method:: setViewerTransform(AffineTransform3D, long)

   Description copied from class: ``AbstractBigViewer``


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: addMouseListenerToDisplay(MouseListener)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: renderFrames(List, String)

   


.. py:method:: resetView()

   Resets the viewer to a fit-to-viewport transform, centering the loaded volume in the canvas. Equivalent to the Reset button in Camera Controls. Does nothing if no volume has been loaded.


.. py:method:: show(AbstractSpimData)

   Displays the BVV viewer with the specified image.


.. py:method:: showCalibrationDialog(Component)

   


.. py:method:: showLoadedData()

   Displays the main tracing data from the associated SNT instance. This method is only available for BVV instances that are tethered to an SNT instance.


.. py:method:: showSecondaryData()

   Displays the secondary tracing data from the associated SNT instance. This method is only available for BVV instances that are tethered to an SNT instance.


.. py:method:: showViewerBanner(String)

   


.. py:method:: showViewerMessage(String)

   Description copied from class: ``AbstractBigViewer``


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: saveSnapshot(String)

   Saves a snapshot of current scene as a PNG image to the specified path.


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(File[])

   Loads reconstruction files and adds them to the viewer with live progress feedback. Files are loaded one at a time on a background thread; the viewer scene is updated after each file so the user sees trees appearing incrementally. The progress bar in the SNT Annotations card tracks progress.


.. py:method:: addTree(Tree)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: annotations()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: captureKeyframe()

   


.. py:method:: dispose()

   


.. py:method:: enableTracing(boolean)

   


.. py:method:: findCenterRay()

   Returns the world-space endpoints of the perspective ray through the center of the viewer's display (its optical axis). Unlike ``findClickRay()``, this does not depend on the mouse cursor.


.. py:method:: findClickRay()

   Returns the world-space endpoints of the perspective ray through the current mouse cursor position: result[0] = near-clip world point, result[1] = far-clip world point. Returns null if the mouse is outside the display or the viewer is not initialized.

   The ray correctly accounts for BVV's perspective projection (``pf = dCam/(dCam+viewerZ)``), giving a well-defined 3D ray for every screen pixel regardless of where the volume's focal plane sits. Use this instead of ``getGlobalMouseCoordinates(net.imglib2.RealPoint)`` when the Z coordinate of the picked point is important (e.g. landmark placement).


.. py:method:: findClickRayMaxima()

   Finds the world-space point of maximum intensity along the perspective ray through the current mouse cursor position.

   Casts a ray from the near clip plane to the far clip plane, samples the active source at 0.5-voxel intervals, and refines the peak location to sub-voxel accuracy via a 3-point parabola fit. Use this for landmark placement when the Z coordinate from the focal plane alone is unreliable.


.. py:method:: findSceneCenterMaxima()

   Finds the world-space point of maximum intensity along the perspective ray through the center of the viewer's display, i.e. whatever is actually visible at the middle of the screen right now, at whatever depth its signal peaks. Same search as ``findClickRayMaxima()``, but along the optical axis rather than through the mouse.


.. py:method:: flyTo(BoundingBox)

   


.. py:method:: hideSecondaryData()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: onSntActiveNodeChanged()

   


.. py:method:: onSntEditModeChanged(boolean)

   


.. py:method:: onSntEditedPathModified()

   


.. py:method:: onSntEditingPathChanged()

   


.. py:method:: open(AbstractSpimData)

   Convenience factory: opens one or more file paths into the same BVV viewer window, choosing the most appropriate loading strategy per file:

   - **.ims** Imaris HDF5: creates a BDV XML sidecar file next to the ``.ims`` file (using the same base name, e.g. ``dataset.xml`` ), then loads it via ``XmlIoSpimDataMinimal`` . BVV's pyramid-aware GPU cache manager is used, so the full volume is never loaded into RAM. If the directory is not writable, an ``IllegalArgumentException`` is thrown with instructions to create the XML manually using ``Plugins > BigDataViewer > Create XML for Imaris file`` .

   - **.xml** BDV XML/HDF5: loaded directly via ``XmlIoSpimDataMinimal`` and displayed using BVV's cache manager. This covers BDV HDF5 and BDV N5 datasets.

   - **.n5 / .zarr** directories: opened directly via ``n5-viewer_fiji`` (no XML sidecar) and displayed using BVV's cache manager. This covers plain N5 multiscale groups and OME-NGFF (OME-Zarr) containers.

   - **anything else** delegated to ``ImgUtils.open(String)`` and displayed via the standard ``ImgPlus`` path. Very large flat volumes will fail with a descriptive error rather than a GL crash.

   Typical Groovy/PySNT usage: ``def bvv = Bvv.open("/path/to/reference.xml", "/path/to/moving.ims")``


.. py:method:: playPaths(Collection, double, double)

   


.. py:method:: playback(List)

   


.. py:method:: promptGoTo()

   


.. py:method:: registerOmeZarrSource(String)

   


.. py:method:: removeTree(String)

   


.. py:method:: repaint()

   Forces a repaint of the viewer, updating volume renderings but not overlays.


.. py:method:: resyncCalibrationFromActiveSource()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: revealContextCommand(ContextMenuCommand)

   


.. py:method:: revealContextItem(JMenuItem)

   


.. py:method:: runContextCommand(ContextMenuCommand)

   


.. py:method:: runContextItem(JMenuItem)

   


.. py:method:: snapshot()

   Retrieves the specified scene view as an image. **Must be called from a non-EDT thread** (e.g. a script or SwingWorker), otherwise the render latch will time out.


.. py:method:: stopPlayback()

   


.. py:method:: syncOverlays()

   Updates the viewer display to reflect changes in rendered trees and paths. This method should be called after modifying the collection of rendered objects to ensure the display is synchronized.


.. py:method:: syncPathManagerList()

   


.. py:method:: toggleEditMode()

   


.. py:method:: updateSecondaryLayerIndicator()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: updateSelection()

   Lightweight alternative to ``AbstractBigViewer.syncPathManagerList()`` for pure selection changes. Patches color/thickness in place for already-rendered trees instead of rebuilding the Path Manager's tree grouping and recomputing screen-space geometry for the whole scene. Does nothing if paths haven't been rendered yet (e.g., before the first sync); The next ``AbstractBigViewer.syncPathManagerList()`` call renders and colors them correctly regardless.


.. py:method:: updateStatus(String, int, int)

   


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.Bvv>`_
* `Bvv JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Bvv.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
