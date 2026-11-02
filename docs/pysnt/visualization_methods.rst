Filtered Method Index
====================

Methods filtered by: category 'Visualization'
Total matching methods: **62**

Matching Methods
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 15 35

   * - Method
     - Class
     - Return Type
     - Description
   * - :meth:`SNTColor.alphaColor`
     - :class:`SNTColor`
     - ``Any``
     - Adds an alpha component to an AWT color.
   * - :meth:`ImpUtils.applyColorTable`
     - :class:`ImpUtils`
     - ``None``
     - No description available
   * - :meth:`TreeUtils.assignUniqueColors`
     - :class:`TreeUtils`
     - ``None``
     - Assigns distinct colors to a collection of Trees.
   * - :meth:`Viewer3D.assignUniqueColors`
     - :class:`Viewer3D`
     - ``None``
     - No description available
   * - :meth:`TreeUtils.assignUniqueColorsIfUncolored`
     - :class:`TreeUtils`
     - ``None``
     - Assigns distinct colors to trees that have no pre-existing color information, leaving trees with custom path/node...
   * - :meth:`SpectralSimilarity.averageColorAtPositions`
     - :class:`SpectralSimilarity`
     - ``List[float]``
     - Computes the average color vector from a set of 3D positions in a multichannel image represented as per-channel...
   * - :meth:`SNT.captureView`
     - :class:`SNT`
     - ``Any``
     - Retrieves a WYSIWYG 'snapshot' of a tracing canvas without voxel data.
   * - :meth:`SNTUI.closeBigViewers`
     - :class:`SNTUI`
     - ``None``
     - Closes any tethered `Bvv`/`Bdv` viewer(s), if open. Unlike `resetUI()`, this does not touch the loaded image or paths:...
   * - :meth:`AllenCompartment.color`
     - :class:`AllenCompartment`
     - ``Any``
     - Description copied from interface: `BrainAnnotation`
   * - :meth:`InsectBrainCompartment.color`
     - :class:`InsectBrainCompartment`
     - ``Any``
     - Description copied from interface: `BrainAnnotation`
   * - :meth:`SNTColor.color`
     - :class:`SNTColor`
     - ``Any``
     - Retrieves the AWT color
   * - :meth:`SNTColor.colorBlindSafeBlue`
     - :class:`SNTColor`
     - ``Any``
     - Returns the blue of the Okabe-Ito palette, safe against the most common forms of color blindness
   * - :meth:`SNTColor.colorBlindSafeYellow`
     - :class:`SNTColor`
     - ``Any``
     - Returns the yellow of the Okabe-Ito palette, safe against the most common forms of color blindness
   * - :meth:`Annotation3D.colorCode`
     - :class:`Annotation3D`
     - ``None``
     - No description available
   * - :meth:`Viewer3D.colorCode`
     - :class:`Viewer3D`
     - ``List[float]``
     - Runs `TreeColorMapper` on the specified `Tree`.
   * - :meth:`SeedOverlayRenderer.colorForSeed`
     - :class:`SeedOverlayRenderer`
     - ``Any``
     - Dispatches to the per-mode color computation. CONFIDENCE keeps the legacy confidence-position behaviour (alpha rides on...
   * - :meth:`SNTColor.colorToString`
     - :class:`SNTColor`
     - ``str``
     - Returns the color encoded as hex string with the format #rrggbbaa.
   * - :meth:`SNTColor.contrastColor`
     - :class:`SNTColor`
     - ``Any``
     - Returns a BW 'contrast' color
   * - :meth:`SNTColor.contrastHueColor`
     - :class:`SNTColor`
     - ``Any``
     - Returns a 'contrasting' color using warm/cool contrast adjustments relatively to a second color reference.
   * - :meth:`ColorMaps.discreteColors`
     - :class:`ColorMaps`
     - ``List[Any]``
     - No description available
   * - :meth:`ColorMaps.discreteColorsAWT`
     - :class:`ColorMaps`
     - ``List[Any]``
     - No description available
   * - :meth:`ShollPlot.drawLabel`
     - :class:`ShollPlot`
     - ``None``
     - No description available
   * - :meth:`BiSearchArtist.drawProgressOnSlice`
     - :class:`BiSearchArtist`
     - ``None``
     - No description available
   * - :meth:`FillerThreadArtist.drawProgressOnSlice`
     - :class:`FillerThreadArtist`
     - ``None``
     - No description available
   * - :meth:`SearchThreadArtist.drawProgressOnSlice`
     - :class:`SearchThreadArtist`
     - ``None``
     - No description available
   * - :meth:`ColorMaps.glasbeyColorsAWT`
     - :class:`ColorMaps`
     - ``List[Any]``
     - No description available
   * - :meth:`SNTService.newRecViewer`
     - :class:`SNTService`
     - ``Viewer3D``
     - Instantiates a new standalone Reconstruction Viewer.
   * - :meth:`SNTColor.okabeIto4Colors`
     - :class:`SNTColor`
     - ``List[Any]``
     - Returns a 4-color subset of the Okabe-Ito colorblind-safe palette
   * - :meth:`SNTColor.okabeIto6Colors`
     - :class:`SNTColor`
     - ``List[Any]``
     - Returns the 6-color Okabe-Ito colorblind-safe palette
   * - :meth:`SNTColor.oppositeColor`
     - :class:`SNTColor`
     - ``Any``
     - Returns a suitable 'opposite' color.
   * - :meth:`CrossSectionUtils.paintAnnulus`
     - :class:`CrossSectionUtils`
     - ``None``
     - Paints an annular cross-section into a 3D output image. For each pixel in the annulus (between `innerRadius` and...
   * - :meth:`Bdv.renderFrames`
     - :class:`Bdv`
     - ``None``
     - No description available
   * - :meth:`Bvv.renderFrames`
     - :class:`Bvv`
     - ``None``
     - No description available
   * - :meth:`Path.resetColor`
     - :class:`Path`
     - ``None``
     - Resets this path color, forcing SNT to render it under default settings.
   * - :meth:`Bdv.resetView`
     - :class:`Bdv`
     - ``None``
     - Description copied from class: `AbstractBigViewer`
   * - :meth:`Bvv.resetView`
     - :class:`Bvv`
     - ``None``
     - Resets the viewer to a fit-to-viewport transform, centering the loaded volume in the canvas. Equivalent to the Reset...
   * - :meth:`Viewer3D.resetView`
     - :class:`Viewer3D`
     - ``None``
     - Resets the view to its default position and orientation. This method restores the camera to its initial position,...
   * - :meth:`CurationManager.severityColor`
     - :class:`CurationManager`
     - ``Any``
     - No description available
   * - :meth:`Bdv.showCalibrationDialog`
     - :class:`Bdv`
     - ``None``
     - No description available
   * - :meth:`Bvv.showCalibrationDialog`
     - :class:`Bvv`
     - ``None``
     - No description available
   * - :meth:`SNTChart.showHeatmap`
     - :class:`SNTChart`
     - ``Any``
     - Shows a two-dimensional heatmap from a two-dimensional data matrix, with rows/columns labeled categorically (e.g....
   * - :meth:`SNTChart.showHistogram3D`
     - :class:`SNTChart`
     - ``Any``
     - Shows a bivariate histogram (two-dimensional histogram) from two DescriptiveStatistics objects. The number of bins is...
   * - :meth:`Bdv.showLoadedData`
     - :class:`Bdv`
     - ``None``
     - Displays the main tracing data from the associated SNT instance. This method is only available for BDV instances that...
   * - :meth:`Bvv.showLoadedData`
     - :class:`Bvv`
     - ``None``
     - Displays the main tracing data from the associated SNT instance. This method is only available for BVV instances that...
   * - :meth:`SNT.showMIPOverlays`
     - :class:`SNT`
     - ``None``
     - No description available
   * - :meth:`SNTUI.showMessage`
     - :class:`SNTUI`
     - ``None``
     - No description available
   * - :meth:`Viewer3D.showMessage`
     - :class:`Viewer3D`
     - ``None``
     - Displays a short message in the viewer's canvas.
   * - :meth:`BookmarkManager.showPanel`
     - :class:`BookmarkManager`
     - ``None``
     - Shows the marker panel, bringing it to front if already visible.
   * - :meth:`Bdv.showSecondaryData`
     - :class:`Bdv`
     - ``None``
     - Displays the secondary tracing data from the associated SNT instance. This method is only available for BDV instances...
   * - :meth:`Bvv.showSecondaryData`
     - :class:`Bvv`
     - ``None``
     - Displays the secondary tracing data from the associated SNT instance. This method is only available for BVV instances...
   * - :meth:`SNT.showStatus`
     - :class:`SNT`
     - ``None``
     - Description copied from interface: `PaneOwner`
   * - :meth:`SNTUI.showStatus`
     - :class:`SNTUI`
     - ``None``
     - Updates the status bar.
   * - :meth:`Bdv.showViewerBanner`
     - :class:`Bdv`
     - ``None``
     - No description available
   * - :meth:`Bvv.showViewerBanner`
     - :class:`Bvv`
     - ``None``
     - No description available
   * - :meth:`Bdv.showViewerMessage`
     - :class:`Bdv`
     - ``None``
     - Description copied from class: `AbstractBigViewer`
   * - :meth:`Bvv.showViewerMessage`
     - :class:`Bvv`
     - ``None``
     - Description copied from class: `AbstractBigViewer`
   * - :meth:`BvvUtils.syncQueuesWithViewer`
     - :class:`BvvUtils`
     - ``None``
     - Registers all tracked fetch queues with the cache controls of `handle`, so that BVV advances them on every new frame...
   * - :meth:`SNT.updateAllViewers`
     - :class:`SNT`
     - ``None``
     - No description available
   * - :meth:`Viewer3D.updateColorBarLegend`
     - :class:`Viewer3D`
     - ``None``
     - Updates all the properties of the existing color bar legend. Does nothing if no legend exists.
   * - :meth:`Viewer3D.updateView`
     - :class:`Viewer3D`
     - ``None``
     - Updates the scene bounds to ensure all visible objects are displayed.
   * - :meth:`SNTService.updateViewers`
     - :class:`SNTService`
     - ``None``
     - Script-friendly method for updating (refreshing) all viewers currently in use by SNT. Does nothing if no SNT instance...
   * - :meth:`MultiViewer3D.viewers`
     - :class:`MultiViewer3D`
     - ``List[Any]``
     - No description available

----

*Filtered index generated on 2026-11-02 07:57:40*