Visualization Methods
=====================

Methods that create visual representations, plots, or graphical displays.

Total methods in this category: **37**

.. contents:: Classes in this Category
   :local:

AllenCompartment
----------------

.. method:: color()

   Description copied from interface: BrainAnnotation

   **Signature:** ``color() -> ColorRGB``

   **Returns:** ``Any``


Annotation3D
------------

.. method:: colorCode(arg0, arg1)

   **Signature:** ``colorCode(String, String) -> void``

   **Parameters:**

   * **arg0** (``str``): - one of COLORMAPS, i.e., "grayscale", "hotcold", "rgb", "redgreen", "whiteblue", etc.
   * **arg1** (``str``)

   **Returns:** ``None``


ColorMaps
---------

.. method:: static discreteColors(arg0, arg1)

   **Signature:** ``static discreteColors(ColorTable, int) -> ColorRGB;``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: static discreteColorsAWT(arg0, arg1)

   **Signature:** ``static discreteColorsAWT(ColorTable, int) -> Color;``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``Any``

.. method:: static glasbeyColorsAWT(arg0)

   **Signature:** ``static glasbeyColorsAWT(int) -> Color;``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Any``


ImpUtils
--------

.. method:: static applyColorTable(arg0, arg1)

   **Signature:** ``static applyColorTable(ImagePlus, ColorTable) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``


InsectBrainCompartment
----------------------

.. method:: color()

   Description copied from interface: BrainAnnotation

   **Signature:** ``color() -> ColorRGB``

   **Returns:** ``Any``


MultiViewer3D
-------------

.. method:: viewers()

   **Signature:** ``viewers() -> List``

   **Returns:** ``List[Any]``


NodeProfiler
------------

.. method:: preview()

   **Signature:** ``preview() -> void``

   **Returns:** ``None``


PathProfiler
------------

.. method:: preview()

   **Signature:** ``preview() -> void``

   **Returns:** ``None``


SNT
---

.. method:: captureView(arg0, arg1)

   Retrieves a WYSIWYG 'snapshot' of a tracing canvas without voxel data.

   **Signature:** ``captureView(String, ColorRGB) -> ImagePlus``

   **Parameters:**

   * **arg0** (``str``): - A case-insensitive string specifying the canvas to be captured. Either "xy" (or "main"), "xz", "zy" or "3d" (for legacy's 3D Viewer).
   * **arg1** (``Any``)

   **Returns:** (``Any``) the snapshot capture of the canvas as an RGB image


SNTColor
--------

.. method:: color()

   Retrieves the AWT color

   **Signature:** ``color() -> Color``

   **Returns:** (``Any``) the AWT color

.. method:: static alphaColor(arg0, arg1)

   Adds an alpha component to an AWT color.

   **Signature:** ``static alphaColor(Color, double) -> Color``

   **Parameters:**

   * **arg0** (``Any``): - the input color
   * **arg1** (``float``)

   **Returns:** (``Any``) the color with an alpha component

.. method:: static colorBlindSafeBlue()

   Returns the blue of the Okabe-Ito palette, safe against the most common forms of color blindness

   **Signature:** ``static colorBlindSafeBlue() -> Color``

   **Returns:** (``Any``) the colorblind-safe blue

.. method:: static colorBlindSafeYellow()

   Returns the yellow of the Okabe-Ito palette, safe against the most common forms of color blindness

   **Signature:** ``static colorBlindSafeYellow() -> Color``

   **Returns:** (``Any``) the colorblind-safe yellow

.. method:: static colorToString(arg0)

   Returns the color encoded as hex string with the format #rrggbbaa.

   **Signature:** ``static colorToString(Object) -> String``

   **Parameters:**

   * **arg0** (``Any``): - the input AWT color

   **Returns:** (``str``) the converted string

.. method:: static contrastColor(arg0)

   Returns a BW 'contrast' color

   **Signature:** ``static contrastColor(Color) -> Color``

   **Parameters:**

   * **arg0** (``Any``): - the input color

   **Returns:** (``Any``) Either white or black, as per hue of input color.

.. method:: static contrastHueColor(arg0, arg1)

   Returns a 'contrasting' color using warm/cool contrast adjustments relatively to a second color reference.

   **Signature:** ``static contrastHueColor(Color, Color) -> Color``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``Any``

.. method:: static getDistinctColors(arg0)

   Returns distinct colors based on Kenneth Kelly's 22 colors of maximum contrast (black and white excluded). More details on this SO discussion

   **Signature:** ``static getDistinctColors(int) -> ColorRGB;``

   **Parameters:**

   * **arg0** (``int``): - the number of colors to be retrieved

   **Returns:** (``Any``) the maximum contrast colors

.. method:: static getDistinctColorsAWT(arg0)

   **Signature:** ``static getDistinctColorsAWT(int) -> Color;``

   **Parameters:**

   * **arg0** (``int``)

   **Returns:** ``Any``

.. method:: static getDistinctColorsColorblindSafe(arg0)

   Returns distinct colors from the Okabe-Ito colorblind-safe palette, cycling through its 6 hues once nColors exceeds that count

   **Signature:** ``static getDistinctColorsColorblindSafe(int) -> ColorRGB;``

   **Parameters:**

   * **arg0** (``int``): - the number of colors to be retrieved

   **Returns:** (``Any``) the colorblind-safe colors

.. method:: static getDistinctColorsColorblindSafeAWT(arg0)

   AWT variant of `getDistinctColorsColorblindSafe(int)`

   **Signature:** ``static getDistinctColorsColorblindSafeAWT(int) -> Color;``

   **Parameters:**

   * **arg0** (``int``): - the number of colors to be retrieved

   **Returns:** (``Any``) the colorblind-safe colors, as AWT colors

.. method:: static getDistinctColorsHex(arg0)

   Returns distinct colors based on Kenneth Kelly's 22 colors of maximum contrast (black and white excluded) as Hex values. More details on this SO discussion

   **Signature:** ``static getDistinctColorsHex(int) -> String;``

   **Parameters:**

   * **arg0** (``int``): - the number of colors to be retrieved

   **Returns:** (``Any``) the maximum contrast colors as hex color strings

.. method:: static okabeIto4Colors()

   Returns a 4-color subset of the Okabe-Ito colorblind-safe palette

   **Signature:** ``static okabeIto4Colors() -> List``

   **Returns:** (``List[Any]``) the 4 Okabe-Ito colors

.. method:: static okabeIto6Colors()

   Returns the 6-color Okabe-Ito colorblind-safe palette

   **Signature:** ``static okabeIto6Colors() -> List``

   **Returns:** (``List[Any]``) the 6 Okabe-Ito colors

.. method:: static oppositeColor(arg0)

   Returns a suitable 'opposite' color.

   **Signature:** ``static oppositeColor(Color) -> Color``

   **Parameters:**

   * **arg0** (``Any``): - the input color

   **Returns:** (``Any``) The opposite color


SNTService
----------

.. method:: newRecViewer(arg0)

   Instantiates a new standalone Reconstruction Viewer.

   **Signature:** ``newRecViewer(boolean) -> Viewer3D``

   **Parameters:**

   * **arg0** (``bool``)

   **Returns:** (``Viewer3D``) The standalone Viewer3D instance

.. method:: updateViewers()

   Script-friendly method for updating (refreshing) all viewers currently in use by SNT. Does nothing if no SNT instance exists.

   **Signature:** ``updateViewers() -> void``

   **Returns:** ``None``


SNTUtils
--------

.. method:: static addViewer(arg0)

   **Signature:** ``static addViewer(Viewer3D) -> void``

   **Parameters:**

   * **arg0** (``Viewer3D``)

   **Returns:** ``None``

.. method:: static removeViewer(arg0)

   **Signature:** ``static removeViewer(Viewer3D) -> void``

   **Parameters:**

   * **arg0** (``Viewer3D``)

   **Returns:** ``None``


SeedOverlayRenderer
-------------------

.. method:: static colorForSeed(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

   Dispatches to the per-mode color computation. CONFIDENCE keeps the legacy confidence-position behaviour (alpha rides on confidence); INDEX / TYPE / SOURCE use a categorical key and full opacity so every seed contributes equal visual weight.

Public so that non-canvas consumers (e.g. the Seeds table's swatch column) can compute the exact same color a seed would receive on the canvas, ensuring row⇄canvas correspondence is visually identical. Stateless: pass depthFalloff = 1.0 when there's no slice-distance concept (table rows have no Z).

   **Signature:** ``static colorForSeed(ColorTable, Color, SeedOverlay$ColorMode, SeedPoint, double, double, double, Map, Map) -> Color``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``Any``)
   * **arg4** (``float``)
   * **arg5** (``float``)
   * **arg6** (``float``)
   * **arg7** (``Dict[str, Any]``)
   * **arg8** (``Dict[str, Any]``)

   **Returns:** ``Any``


SpectralSimilarity
------------------

.. method:: static averageColorAtPositions(arg0, arg1)

   Computes the average color vector from a set of 3D positions in a multichannel image represented as per-channel ImageStacks.

   **Signature:** ``static averageColorAtPositions(RandomAccessibleInterval, [[I) -> [D``

   **Parameters:**

   * **arg0** (``Any``): - one ImageStack per channel
   * **arg1** (``Any``)

   **Returns:** (``Any``) the average color vector (one value per channel)


TreeUtils
---------

.. method:: static assignUniqueColors(arg0)

   Assigns distinct colors to a collection of Trees.

   **Signature:** ``static assignUniqueColors(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - an optional string defining a hue to be excluded. Either 'red', 'green', 'blue', or 'dim'.

   **Returns:** ``None``

.. method:: static assignUniqueColorsIfUncolored(arg0, arg1)

   Assigns distinct colors to trees that have no pre-existing color information, leaving trees with custom path/node colors untouched. Useful when importing files that may already carry authored colors (e.g., a traces file with per-path color attributes), where forcing a single flat color per tree would discard that information.

   **Signature:** ``static assignUniqueColorsIfUncolored(Collection, String) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)
   * **arg1** (``str``)

   **Returns:** ``None``


Viewer3D
--------

.. method:: assignUniqueColors(arg0)

   **Signature:** ``assignUniqueColors(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``None``

.. method:: colorCode(arg0, arg1, arg2)

   Runs TreeColorMapper on the specified Tree.

   **Signature:** ``colorCode(Collection, String, ColorTable) -> [D``

   **Parameters:**

   * **arg0** (``List[Any]``): - the identifier of the Tree (as per addTree(Tree))to be color mapped
   * **arg1** (``str``)
   * **arg2** (``Any``)

   **Returns:** (``Any``) the double[] the limits (min and max) of the mapped values


WekaModelLoader
---------------

.. method:: preview()

   **Signature:** ``preview() -> void``

   **Returns:** ``None``


----

*Category index generated on 2026-09-27 23:02:20*