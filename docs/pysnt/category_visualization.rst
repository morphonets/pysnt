Visualization Methods
=====================

Methods that create visual representations, plots, or graphical displays.

Total methods in this category: **26**

.. contents:: Classes in this Category
   :local:

AllenCompartment
----------------

.. method:: color()

   **Signature:** ``color() -> ColorRGB``

   **Returns:** (``Any``) the display color of this compartment (if known)


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

   **Signature:** ``color() -> ColorRGB``

   **Returns:** (``Any``) the display color of this compartment (if known)


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

.. method:: static colorToString(arg0)

   Returns the color encoded as hex string with the format #rrggbbaa.

   **Signature:** ``static colorToString(Object) -> String``

   **Parameters:**

   * **arg0** (``Any``): - the input AWT color

   **Returns:** (``str``) the converted string

.. method:: static contrastColor(arg0)

   Returns a suitable 'contrast' color.

   **Signature:** ``static contrastColor(Color) -> Color``

   **Parameters:**

   * **arg0** (``Any``): - the input color

   **Returns:** (``Any``) Either white or black, as per hue of input color.

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

.. method:: static getDistinctColorsHex(arg0, arg1)

   **Signature:** ``static getDistinctColorsHex(int, String) -> String;``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``Any``


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


Tree
----

.. method:: static assignUniqueColors(arg0)

   Assigns distinct colors to a collection of Trees.

   **Signature:** ``static assignUniqueColors(Collection) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - an optional string defining a hue to be excluded. Either 'red', 'green', or 'blue'.

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

*Category index generated on 2026-01-02 22:43:26*