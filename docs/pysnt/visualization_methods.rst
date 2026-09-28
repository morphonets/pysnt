Filtered Method Index
====================

Methods filtered by: category 'Visualization'
Total matching methods: **37**

Matching Methods
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 15 35

   * - Method
     - Class
     - Return Type
     - Description
   * - :meth:`Viewer3D.assignUniqueColors`
     - :class:`Viewer3D`
     - ``None``
     - No description available
   * - :meth:`SNT.captureView`
     - :class:`SNT`
     - ``Any``
     - Retrieves a WYSIWYG 'snapshot' of a tracing canvas without voxel data.
   * - :meth:`AllenCompartment.color`
     - :class:`AllenCompartment`
     - ``Any``
     - Description copied from interface: BrainAnnotation
   * - :meth:`InsectBrainCompartment.color`
     - :class:`InsectBrainCompartment`
     - ``Any``
     - Description copied from interface: BrainAnnotation
   * - :meth:`SNTColor.color`
     - :class:`SNTColor`
     - ``Any``
     - Retrieves the AWT color
   * - :meth:`Annotation3D.colorCode`
     - :class:`Annotation3D`
     - ``None``
     - No description available
   * - :meth:`Viewer3D.colorCode`
     - :class:`Viewer3D`
     - ``Any``
     - Runs TreeColorMapper on the specified Tree.
   * - :meth:`SNTService.newRecViewer`
     - :class:`SNTService`
     - ``Viewer3D``
     - Instantiates a new standalone Reconstruction Viewer.
   * - :meth:`NodeProfiler.preview`
     - :class:`NodeProfiler`
     - ``None``
     - No description available
   * - :meth:`PathProfiler.preview`
     - :class:`PathProfiler`
     - ``None``
     - No description available
   * - :meth:`WekaModelLoader.preview`
     - :class:`WekaModelLoader`
     - ``None``
     - No description available
   * - :meth:`SNTUtils.static addViewer`
     - :class:`SNTUtils`
     - ``None``
     - No description available
   * - :meth:`SNTColor.static alphaColor`
     - :class:`SNTColor`
     - ``Any``
     - Adds an alpha component to an AWT color.
   * - :meth:`ImpUtils.static applyColorTable`
     - :class:`ImpUtils`
     - ``None``
     - No description available
   * - :meth:`TreeUtils.static assignUniqueColors`
     - :class:`TreeUtils`
     - ``None``
     - Assigns distinct colors to a collection of Trees.
   * - :meth:`TreeUtils.static assignUniqueColorsIfUncolored`
     - :class:`TreeUtils`
     - ``None``
     - Assigns distinct colors to trees that have no pre-existing color information, leaving trees with custom path/node...
   * - :meth:`SpectralSimilarity.static averageColorAtPositions`
     - :class:`SpectralSimilarity`
     - ``Any``
     - Computes the average color vector from a set of 3D positions in a multichannel image represented as per-channel...
   * - :meth:`SNTColor.static colorBlindSafeBlue`
     - :class:`SNTColor`
     - ``Any``
     - Returns the blue of the Okabe-Ito palette, safe against the most common forms of color blindness
   * - :meth:`SNTColor.static colorBlindSafeYellow`
     - :class:`SNTColor`
     - ``Any``
     - Returns the yellow of the Okabe-Ito palette, safe against the most common forms of color blindness
   * - :meth:`SeedOverlayRenderer.static colorForSeed`
     - :class:`SeedOverlayRenderer`
     - ``Any``
     - Dispatches to the per-mode color computation. CONFIDENCE keeps the legacy confidence-position behaviour (alpha rides on...
   * - :meth:`SNTColor.static colorToString`
     - :class:`SNTColor`
     - ``str``
     - Returns the color encoded as hex string with the format #rrggbbaa.
   * - :meth:`SNTColor.static contrastColor`
     - :class:`SNTColor`
     - ``Any``
     - Returns a BW 'contrast' color
   * - :meth:`SNTColor.static contrastHueColor`
     - :class:`SNTColor`
     - ``Any``
     - Returns a 'contrasting' color using warm/cool contrast adjustments relatively to a second color reference.
   * - :meth:`ColorMaps.static discreteColors`
     - :class:`ColorMaps`
     - ``Any``
     - No description available
   * - :meth:`ColorMaps.static discreteColorsAWT`
     - :class:`ColorMaps`
     - ``Any``
     - No description available
   * - :meth:`SNTColor.static getDistinctColors`
     - :class:`SNTColor`
     - ``Any``
     - Returns distinct colors based on Kenneth Kelly's 22 colors of maximum contrast (black and white excluded). More details...
   * - :meth:`SNTColor.static getDistinctColorsAWT`
     - :class:`SNTColor`
     - ``Any``
     - No description available
   * - :meth:`SNTColor.static getDistinctColorsColorblindSafe`
     - :class:`SNTColor`
     - ``Any``
     - Returns distinct colors from the Okabe-Ito colorblind-safe palette, cycling through its 6 hues once nColors exceeds...
   * - :meth:`SNTColor.static getDistinctColorsColorblindSafeAWT`
     - :class:`SNTColor`
     - ``Any``
     - AWT variant of `getDistinctColorsColorblindSafe(int)`
   * - :meth:`SNTColor.static getDistinctColorsHex`
     - :class:`SNTColor`
     - ``Any``
     - Returns distinct colors based on Kenneth Kelly's 22 colors of maximum contrast (black and white excluded) as Hex...
   * - :meth:`ColorMaps.static glasbeyColorsAWT`
     - :class:`ColorMaps`
     - ``Any``
     - No description available
   * - :meth:`SNTColor.static okabeIto4Colors`
     - :class:`SNTColor`
     - ``List[Any]``
     - Returns a 4-color subset of the Okabe-Ito colorblind-safe palette
   * - :meth:`SNTColor.static okabeIto6Colors`
     - :class:`SNTColor`
     - ``List[Any]``
     - Returns the 6-color Okabe-Ito colorblind-safe palette
   * - :meth:`SNTColor.static oppositeColor`
     - :class:`SNTColor`
     - ``Any``
     - Returns a suitable 'opposite' color.
   * - :meth:`SNTUtils.static removeViewer`
     - :class:`SNTUtils`
     - ``None``
     - No description available
   * - :meth:`SNTService.updateViewers`
     - :class:`SNTService`
     - ``None``
     - Script-friendly method for updating (refreshing) all viewers currently in use by SNT. Does nothing if no SNT instance...
   * - :meth:`MultiViewer3D.viewers`
     - :class:`MultiViewer3D`
     - ``List[Any]``
     - No description available

----

*Filtered index generated on 2026-09-27 23:02:20*