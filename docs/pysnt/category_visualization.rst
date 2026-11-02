Visualization Methods
=====================

Methods that create visual representations, plots, or graphical displays.

Total methods in this category: **62**

.. contents:: Classes in this Category
   :local:

AllenCompartment
----------------

.. method:: color()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``color() -> ColorRGB``

   **Returns:** ``Any``


Annotation3D
------------

.. method:: colorCode(colormap, axis)

   **Signature:** ``colorCode(String, String) -> void``

   **Parameters:**

   * **colormap** (``str``): - one of COLORMAPS, i.e., "grayscale", "hotcold", "rgb", "redgreen", "whiteblue", etc.
   * **axis** (``str``)

   **Returns:** ``None``


Bdv
---

.. method:: renderFrames(keyframes, outputDir)

   **Signature:** ``renderFrames(List, String) -> void``

   **Parameters:**

   * **keyframes** (``List[Any]``)
   * **outputDir** (``str``)

   **Returns:** ``None``

.. method:: resetView()

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``resetView() -> void``

   **Returns:** ``None``

.. method:: showCalibrationDialog(parent)

   **Signature:** ``showCalibrationDialog(Component) -> void``

   **Parameters:**

   * **parent** (``Any``)

   **Returns:** ``None``

.. method:: showLoadedData()

   Displays the main tracing data from the associated SNT instance. This method is only available for BDV instances that are tethered to an SNT instance.

   **Signature:** ``showLoadedData() -> void``

   **Returns:** ``None``

.. method:: showSecondaryData()

   Displays the secondary tracing data from the associated SNT instance. This method is only available for BDV instances that are tethered to an SNT instance.

   **Signature:** ``showSecondaryData() -> void``

   **Returns:** ``None``

.. method:: showViewerBanner(msg)

   **Signature:** ``showViewerBanner(String) -> void``

   **Parameters:**

   * **msg** (``str``)

   **Returns:** ``None``

.. method:: showViewerMessage(msg)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``showViewerMessage(String) -> void``

   **Parameters:**

   * **msg** (``str``): - the message to show

   **Returns:** ``None``


BiSearchArtist
--------------

.. method:: drawProgressOnSlice(plane, currentSliceInPlane, canvas, g)

   **Signature:** ``drawProgressOnSlice(int, int, TracerCanvas, Graphics) -> void``

   **Parameters:**

   * **plane** (``int``)
   * **currentSliceInPlane** (``int``)
   * **canvas** (``TracerCanvas``)
   * **g** (``Any``)

   **Returns:** ``None``


BookmarkManager
---------------

.. method:: showPanel()

   Shows the marker panel, bringing it to front if already visible.

   **Signature:** ``showPanel() -> void``

   **Returns:** ``None``


Bvv
---

.. method:: renderFrames(keyframes, outputDir)

   **Signature:** ``renderFrames(List, String) -> void``

   **Parameters:**

   * **keyframes** (``List[Any]``)
   * **outputDir** (``str``)

   **Returns:** ``None``

.. method:: resetView()

   Resets the viewer to a fit-to-viewport transform, centering the loaded volume in the canvas. Equivalent to the Reset button in Camera Controls. Does nothing if no volume has been loaded.

   **Signature:** ``resetView() -> void``

   **Returns:** ``None``

.. method:: showCalibrationDialog(parent)

   **Signature:** ``showCalibrationDialog(Component) -> void``

   **Parameters:**

   * **parent** (``Any``)

   **Returns:** ``None``

.. method:: showLoadedData()

   Displays the main tracing data from the associated SNT instance. This method is only available for BVV instances that are tethered to an SNT instance.

   **Signature:** ``showLoadedData() -> void``

   **Returns:** ``None``

.. method:: showSecondaryData()

   Displays the secondary tracing data from the associated SNT instance. This method is only available for BVV instances that are tethered to an SNT instance.

   **Signature:** ``showSecondaryData() -> void``

   **Returns:** ``None``

.. method:: showViewerBanner(msg)

   **Signature:** ``showViewerBanner(String) -> void``

   **Parameters:**

   * **msg** (``str``)

   **Returns:** ``None``

.. method:: showViewerMessage(msg)

   Description copied from class: `AbstractBigViewer`

   **Signature:** ``showViewerMessage(String) -> void``

   **Parameters:**

   * **msg** (``str``): - the message to show

   **Returns:** ``None``


BvvUtils
--------

.. method:: syncQueuesWithViewer(handle)

   Registers all tracked fetch queues with the cache controls of `handle`, so that BVV advances them on every new frame (see `CacheControl.prepareNextFrame()`). Idempotent. Opt out with `-Dsnt.bvv.noQueueSync=true`

   **Signature:** ``syncQueuesWithViewer(BvvHandle) -> void``

   **Parameters:**

   * **handle** (``Any``)

   **Returns:** ``None``


ColorMaps
---------

.. method:: discreteColors(colorTable, n)

   **Signature:** ``discreteColors(ColorTable, int) -> ColorRGB[]``

   **Parameters:**

   * **colorTable** (``Any``)
   * **n** (``int``)

   **Returns:** ``List[Any]``

.. method:: discreteColorsAWT(colorTable, n)

   **Signature:** ``discreteColorsAWT(ColorTable, int) -> Color[]``

   **Parameters:**

   * **colorTable** (``Any``)
   * **n** (``int``)

   **Returns:** ``List[Any]``

.. method:: glasbeyColorsAWT(n)

   **Signature:** ``glasbeyColorsAWT(int) -> Color[]``

   **Parameters:**

   * **n** (``int``)

   **Returns:** ``List[Any]``


CrossSectionUtils
-----------------

.. method:: paintAnnulus(output, side, scaleIso, ox, oy, oz, aBasis, bBasis, xSpacing, ySpacing, zSpacing, offsetX, offsetY, offsetZ, innerRadius, outerRadius, fillValue)

   Paints an annular cross-section into a 3D output image. For each pixel in the annulus (between `innerRadius` and `outerRadius` in grid space), the corresponding voxel in the output image is set to `fillValue`. Existing non-zero voxels are preserved (logical OR).

   **Signature:** ``paintAnnulus(RandomAccessibleInterval, int, double, double, double, double, double[], double[], double, double, double, double, double, double, double, double, double) -> void``

   **Parameters:**

   * **output** (``Any``): - the 3D output image (modified in place); dimensions correspond to pixel coordinates
   * **side** (``int``)
   * **scaleIso** (``float``)
   * **ox** (``float``)
   * **oy** (``float``)
   * **oz** (``float``)
   * **aBasis** (``List[float]``)
   * **bBasis** (``List[float]``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)
   * **offsetX** (``float``)
   * **offsetY** (``float``)
   * **offsetZ** (``float``)
   * **innerRadius** (``float``)
   * **outerRadius** (``float``)
   * **fillValue** (``float``)

   **Returns:** ``None``


CurationManager
---------------

.. method:: severityColor(severity)

   **Signature:** ``severityColor(Severity) -> Color``

   **Parameters:**

   * **severity** (``Any``)

   **Returns:** (``Any``) the per-severity accent color used in the Assistant tab's table, filter menu, and severity icons.


FillerThreadArtist
------------------

.. method:: drawProgressOnSlice(plane, currentSliceInPlane, canvas, g)

   **Signature:** ``drawProgressOnSlice(int, int, TracerCanvas, Graphics) -> void``

   **Parameters:**

   * **plane** (``int``)
   * **currentSliceInPlane** (``int``)
   * **canvas** (``TracerCanvas``)
   * **g** (``Any``)

   **Returns:** ``None``


ImpUtils
--------

.. method:: applyColorTable(imp, cTable)

   **Signature:** ``applyColorTable(ImagePlus, ColorTable) -> void``

   **Parameters:**

   * **imp** (``Any``)
   * **cTable** (``Any``)

   **Returns:** ``None``


InsectBrainCompartment
----------------------

.. method:: color()

   Description copied from interface: `BrainAnnotation`

   **Signature:** ``color() -> ColorRGB``

   **Returns:** ``Any``


MultiViewer3D
-------------

.. method:: viewers()

   **Signature:** ``viewers() -> List``

   **Returns:** ``List[Any]``


Path
----

.. method:: resetColor()

   Resets this path color, forcing SNT to render it under default settings.

   **Signature:** ``resetColor() -> void``

   **Returns:** ``None``


SNT
---

.. method:: captureView(view, backgroundColor)

   Retrieves a WYSIWYG 'snapshot' of a tracing canvas without voxel data.

   **Signature:** ``captureView(String, ColorRGB) -> ImagePlus``

   **Parameters:**

   * **view** (``str``): - A case-insensitive string specifying the canvas to be captured. Either "xy" (or "main"), "xz", "zy" or "3d" (for legacy's 3D Viewer).
   * **backgroundColor** (``Any``)

   **Returns:** (``Any``) the snapshot capture of the canvas as an RGB image

.. method:: showMIPOverlays(opacity)

   **Signature:** ``showMIPOverlays(double) -> void``

   **Parameters:**

   * **opacity** (``float``)

   **Returns:** ``None``

.. method:: showStatus(progress, maximum, status)

   Description copied from interface: `PaneOwner`

   **Signature:** ``showStatus(int, int, String) -> void``

   **Parameters:**

   * **progress** (``int``): - the current progress value
   * **maximum** (``int``)
   * **status** (``str``)

   **Returns:** ``None``

.. method:: updateAllViewers()

   **Signature:** ``updateAllViewers() -> void``

   **Returns:** ``None``


SNTChart
--------

.. method:: showHeatmap(data, colorTable, axisLabels)

   Shows a two-dimensional heatmap from a two-dimensional data matrix, with rows/columns labeled categorically (e.g. class/check names) instead of by numeric coordinate. Cannot be called from event dispatcher thread.

   **Signature:** ``showHeatmap(double[][], ColorTable, String[]) -> JFrame``

   **Parameters:**

   * **data** (``List[List[float]]``): - the heatmap title (null allowed)
   * **colorTable** (``Any``)
   * **axisLabels** (``List[str]``)

   **Returns:** (``Any``) the frame holding the heatmap

.. method:: showHistogram3D(values1, values2, colorTable, axisLabels)

   Shows a bivariate histogram (two-dimensional histogram) from two DescriptiveStatistics objects. The number of bins is automatically determined using the Freedman-Diaconis rule.

   **Signature:** ``showHistogram3D(Collection, Collection, ColorTable, String[]) -> JFrame``

   **Parameters:**

   * **values1** (``List[Any]``): - DescriptiveStatistics for the first distribution
   * **values2** (``List[Any]``)
   * **colorTable** (``Any``)
   * **axisLabels** (``List[str]``)

   **Returns:** (``Any``) the frame holding the histogram


SNTColor
--------

.. method:: alphaColor(c, percent)

   Adds an alpha component to an AWT color.

   **Signature:** ``alphaColor(Color, double) -> Color``

   **Parameters:**

   * **c** (``Any``): - the input color
   * **percent** (``float``)

   **Returns:** (``Any``) the color with an alpha component

.. method:: color()

   Retrieves the AWT color

   **Signature:** ``color() -> Color``

   **Returns:** (``Any``) the AWT color

.. method:: colorBlindSafeBlue()

   Returns the blue of the Okabe-Ito palette, safe against the most common forms of color blindness

   **Signature:** ``colorBlindSafeBlue() -> Color``

   **Returns:** (``Any``) the colorblind-safe blue

.. method:: colorBlindSafeYellow()

   Returns the yellow of the Okabe-Ito palette, safe against the most common forms of color blindness

   **Signature:** ``colorBlindSafeYellow() -> Color``

   **Returns:** (``Any``) the colorblind-safe yellow

.. method:: colorToString(color)

   Returns the color encoded as hex string with the format #rrggbbaa.

   **Signature:** ``colorToString(Object) -> String``

   **Parameters:**

   * **color** (``Any``): - the input AWT color

   **Returns:** (``str``) the converted string

.. method:: contrastColor(c)

   Returns a BW 'contrast' color

   **Signature:** ``contrastColor(Color) -> Color``

   **Parameters:**

   * **c** (``Any``): - the input color

   **Returns:** (``Any``) Either white or black, as per hue of input color.

.. method:: contrastHueColor(c)

   Returns a 'contrasting' color using warm/cool contrast adjustments relatively to a second color reference.

   **Signature:** ``contrastHueColor(Color) -> Color``

   **Parameters:**

   * **c** (``Any``): - the input color

   **Returns:** (``Any``) The contrasting color

.. method:: okabeIto4Colors()

   Returns a 4-color subset of the Okabe-Ito colorblind-safe palette

   **Signature:** ``okabeIto4Colors() -> List``

   **Returns:** (``List[Any]``) the 4 Okabe-Ito colors

.. method:: okabeIto6Colors()

   Returns the 6-color Okabe-Ito colorblind-safe palette

   **Signature:** ``okabeIto6Colors() -> List``

   **Returns:** (``List[Any]``) the 6 Okabe-Ito colors

.. method:: oppositeColor(c)

   Returns a suitable 'opposite' color.

   **Signature:** ``oppositeColor(Color) -> Color``

   **Parameters:**

   * **c** (``Any``): - the input color

   **Returns:** (``Any``) The opposite color


SNTService
----------

.. method:: newRecViewer(guiControls)

   Instantiates a new standalone Reconstruction Viewer.

   **Signature:** ``newRecViewer(boolean) -> Viewer3D``

   **Parameters:**

   * **guiControls** (``bool``)

   **Returns:** (``Viewer3D``) The standalone `Viewer3D` instance

.. method:: updateViewers()

   Script-friendly method for updating (refreshing) all viewers currently in use by SNT. Does nothing if no SNT instance exists.

   **Signature:** ``updateViewers() -> void``

   **Returns:** ``None``


SNTUI
-----

.. method:: closeBigViewers()

   Closes any tethered `Bvv`/`Bdv` viewer(s), if open. Unlike `resetUI()`, this does not touch the loaded image or paths: closing a big-viewer *window* isn't data loss the way clearing paths is (the underlying `PathAndFillManager` is untouched), so this needs no confirmation and is safe to call unconditionally - e.g. from `DemoRunner` before loading a new demo, so a viewer left over from a previous one is never silently orphaned (see `AbstractBigViewer`/`setBvvOnEDT`'s `windowClosing` handler for what "orphaned" means here).

   **Signature:** ``closeBigViewers() -> void``

   **Returns:** ``None``

.. method:: showMessage(msg, title)

   **Signature:** ``showMessage(String, String) -> void``

   **Parameters:**

   * **msg** (``str``)
   * **title** (``str``)

   **Returns:** ``None``

.. method:: showStatus(msg, temporary)

   Updates the status bar.

   **Signature:** ``showStatus(String, boolean) -> void``

   **Parameters:**

   * **msg** (``str``): - the text to displayed. Set it to null (or empty String) to reset the status bar.
   * **temporary** (``bool``)

   **Returns:** ``None``


SearchThreadArtist
------------------

.. method:: drawProgressOnSlice(plane, currentSliceInPlane, canvas, g)

   **Signature:** ``drawProgressOnSlice(int, int, TracerCanvas, Graphics) -> void``

   **Parameters:**

   * **plane** (``int``)
   * **currentSliceInPlane** (``int``)
   * **canvas** (``TracerCanvas``)
   * **g** (``Any``)

   **Returns:** ``None``


SeedOverlayRenderer
-------------------

.. method:: colorForSeed(table, unknownConfidenceColor, mode, s, low, high, depthFalloff, seedIndexMap, categoryOrdinals)

   Dispatches to the per-mode color computation. CONFIDENCE keeps the legacy confidence-position behaviour (alpha rides on confidence); INDEX / TYPE / SOURCE use a categorical key and full opacity so every seed contributes equal visual weight.

Public so that non-canvas consumers (e.g. the Seeds table's swatch column) can compute the exact same color a seed would receive on the canvas, ensuring row⇄canvas correspondence is visually identical. Stateless: pass `depthFalloff = 1.0` when there's no slice-distance concept (table rows have no Z).

   **Signature:** ``colorForSeed(ColorTable, Color, ColorMode, SeedPoint, double, double, double, Map, Map) -> Color``

   **Parameters:**

   * **table** (``Any``)
   * **unknownConfidenceColor** (``Any``)
   * **mode** (``Any``)
   * **s** (``SeedPoint``)
   * **low** (``float``)
   * **high** (``float``)
   * **depthFalloff** (``float``)
   * **seedIndexMap** (``Dict[str, Any]``)
   * **categoryOrdinals** (``Dict[str, Any]``)

   **Returns:** ``Any``


ShollPlot
---------

.. method:: drawLabel(label, color)

   **Signature:** ``drawLabel(String, Color) -> void``

   **Parameters:**

   * **label** (``str``)
   * **color** (``Any``)

   **Returns:** ``None``


SpectralSimilarity
------------------

.. method:: averageColorAtPositions(channelStacks, positions)

   Computes the average color vector from a set of 3D positions in a multichannel image represented as per-channel `ImageStack`s.

   **Signature:** ``averageColorAtPositions(ImageStack[], int[][]) -> double[]``

   **Parameters:**

   * **channelStacks** (``List[Any]``): - one ImageStack per channel
   * **positions** (``List[List[int]]``)

   **Returns:** (``List[float]``) the average color vector (one value per channel)


TreeUtils
---------

.. method:: assignUniqueColors(trees)

   Assigns distinct colors to a collection of Trees.

   **Signature:** ``assignUniqueColors(Collection) -> void``

   **Parameters:**

   * **trees** (``List[Any]``): - an optional string defining a hue to be excluded. Either 'red', 'green', 'blue', or 'dim'.

   **Returns:** ``None``

.. method:: assignUniqueColorsIfUncolored(trees)

   Assigns distinct colors to trees that have no pre-existing color information, leaving trees with custom path/node colors untouched. Useful when importing files that may already carry authored colors (e.g., a traces file with per-path color attributes), where forcing a single flat color per tree would discard that information.

   **Signature:** ``assignUniqueColorsIfUncolored(Collection) -> void``

   **Parameters:**

   * **trees** (``List[Any]``): - the trees to (conditionally) color

   **Returns:** ``None``


Viewer3D
--------

.. method:: assignUniqueColors(treeLabels)

   **Signature:** ``assignUniqueColors(Collection) -> void``

   **Parameters:**

   * **treeLabels** (``List[Any]``)

   **Returns:** ``None``

.. method:: colorCode(treeLabels, measurement, colorTable)

   Runs `TreeColorMapper` on the specified `Tree`.

   **Signature:** ``colorCode(Collection, String, ColorTable) -> double[]``

   **Parameters:**

   * **treeLabels** (``List[Any]``): - the identifier of the Tree (as per addTree(Tree))to be color mapped
   * **measurement** (``str``)
   * **colorTable** (``Any``)

   **Returns:** (``List[float]``) the double[] the limits (min and max) of the mapped values

.. method:: resetView()

   Resets the view to its default position and orientation.

This method restores the camera to its initial position, orientation, and zoom level, providing a consistent starting point for viewing the scene.

   **Signature:** ``resetView() -> void``

   **Returns:** ``None``

.. method:: showMessage(msg, asBanner)

   Displays a short message in the viewer's canvas.

   **Signature:** ``showMessage(String, boolean) -> void``

   **Parameters:**

   * **msg** (``str``): - the message to show
   * **asBanner** (``bool``)

   **Returns:** ``None``

.. method:: updateColorBarLegend(min, max)

   Updates all the properties of the existing color bar legend. Does nothing if no legend exists.

   **Signature:** ``updateColorBarLegend(double, double) -> void``

   **Parameters:**

   * **min** (``float``): - the minimum value in the color table
   * **max** (``float``)

   **Returns:** ``None``

.. method:: updateView()

   Updates the scene bounds to ensure all visible objects are displayed.

   **Signature:** ``updateView() -> void``

   **Returns:** ``None``


----

*Category index generated on 2026-11-02 07:57:40*