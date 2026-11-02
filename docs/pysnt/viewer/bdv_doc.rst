
``Bdv`` Class Documentation
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

SNT's BigDataViewer-based 2D slice viewer.

Complements ``Bvv`` for images where orthographic 2D slice navigation is preferable over GPU volume rendering. Because BDV uses orthographic projection, cursor coordinates returned by ``AbstractViewerPanel.getGlobalMouseCoordinates(net.imglib2.RealPositionable)`` are unambiguous at the current slice depth, making marker placement more accurate than in BVV.

This class extends ``AbstractBigViewer`` and shares tree management, calibration, and bookmark infrastructure with ``Bvv``.

Path and annotation overlays reuse ``Bvv.PathOverlay`` and ``Bvv.AnnotationOverlay`` via the ``BigViewerPanel`` adapter, with ``dCam = Double.MAX_VALUE`` so the perspective factor evaluates to 1.0 (orthographic rendering, no foreshortening).

Usage (scripting) 


::

    bdv = new Bdv()
    bdv.show(imp)
    bdv.addTree(tree)
    bdv.getMarkerManager().toggleViewerPanel()




Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearAllTrees()

   Description copied from class: ``AbstractBigViewer``


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBdvHandle()

   Returns the underlying ``BdvHandle`` that manages sources and the viewer state.


.. py:method:: getBoundingBox()

   


.. py:method:: getCalibration()

   


.. py:method:: getCurrentTimepoint()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDefaultMarkerColor()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDefaultMarkerSize()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDefaultRenderingStyle()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getDisplayRadii()

   Returns whether paths are rendered as frusta (true) or centerlines (false).


.. py:method:: getDisplayRange(int)

   


.. py:method:: getDownsamplingFactors(int, int)

   


.. py:method:: getGlobalMouseCoordinates(RealPoint)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getInstance()

   Returns the most recently created ``Bdv`` instance, or ``null``. Convenience accessor for scripts.


.. py:method:: getMarkerManager()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getNumResolutionLevels(int)

   


.. py:method:: getPhysicalUnit()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getPrimarySourcePath()

   


.. py:method:: getRenderSettleTime()

   


.. py:method:: getRenderedTrees()

   


.. py:method:: getRenderingOptions()

   Returns the rendering options controlling path thickness, transparency, etc. For BDV, slab clipping options have no effect (slab mode is BVV-only).


.. py:method:: getSNT()

   


.. py:method:: getSceneCenter()

   


.. py:method:: getSourceData(int, int)

   


.. py:method:: getSourceName(int)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getSourcePaths()

   


.. py:method:: getViewerCanvas()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerFrame()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerHeight()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: getViewerPanel()

   Returns the BDV display panel. Unlike BVV, BDV uses a ``ViewerPanel`` (orthographic slice viewer).


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

   


.. py:method:: setCurrentTimepoint(int)

   Description copied from class: ``AbstractBigViewer``


.. py:method:: setDisplayRadii(boolean)

   Switches between frustum (radius-based) and centerline rendering. Invalidates the overlay cache and requests a repaint.


.. py:method:: setPathOverlayOffset(double, double, double)

   Shifts all rendered trees by (offsetX, offsetY, offsetZ) in world coordinates, for rendering purposes only.


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

   Description copied from class: ``AbstractBigViewer``


.. py:method:: show(AbstractSpimData)

   Opens sources loaded from an N5 or OME-Zarr container (see ``SpimDataUtils.resolvePathToSource(String)``). Unlike ``show(AbstractSpimData)``, there is no BDV-XML descriptor or ``AbstractSpimData`` involved: sources are built directly from the container's own N5/OME-NGFF metadata via ``n5-viewer_fiji``.


.. py:method:: showCalibrationDialog(Component)

   


.. py:method:: showLoadedData()

   Displays the main tracing data from the associated SNT instance. This method is only available for BDV instances that are tethered to an SNT instance.


.. py:method:: showSecondaryData()

   Displays the secondary tracing data from the associated SNT instance. This method is only available for BDV instances that are tethered to an SNT instance.


.. py:method:: showViewerBanner(String)

   


.. py:method:: showViewerMessage(String)

   Description copied from class: ``AbstractBigViewer``


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(File[])

   Description copied from class: ``AbstractBigViewer``


.. py:method:: addTree(Tree)

   


.. py:method:: annotations()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: captureKeyframe()

   


.. py:method:: dispose()

   


.. py:method:: enableTracing(boolean)

   


.. py:method:: flyTo(BoundingBox)

   


.. py:method:: hideSecondaryData()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: onSntActiveNodeChanged()

   


.. py:method:: onSntEditModeChanged(boolean)

   


.. py:method:: onSntEditedPathModified()

   


.. py:method:: onSntEditingPathChanged()

   


.. py:method:: playPaths(Collection, double, double)

   


.. py:method:: playback(List)

   


.. py:method:: promptGoTo()

   


.. py:method:: registerOmeZarrSource(String)

   


.. py:method:: removeTree(String)

   


.. py:method:: repaint()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: resyncCalibrationFromActiveSource()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: revealContextCommand(ContextMenuCommand)

   


.. py:method:: revealContextItem(JMenuItem)

   


.. py:method:: runContextCommand(ContextMenuCommand)

   


.. py:method:: runContextItem(JMenuItem)

   


.. py:method:: stopPlayback()

   


.. py:method:: syncOverlays()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: syncPathManagerList()

   


.. py:method:: toggleEditMode()

   


.. py:method:: updateSecondaryLayerIndicator()

   Description copied from class: ``AbstractBigViewer``


.. py:method:: updateSelection()

   Lightweight alternative to ``AbstractBigViewer.syncPathManagerList()`` for pure selection changes: patches color/thickness in place for already-rendered trees. Mirrors ``Bvv.updateSelection()``


.. py:method:: updateStatus(String, int, int)

   


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.Bdv>`_
* `Bdv JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Bdv.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
