I/O Operations Methods
======================

Methods that handle input/output operations, file loading, and data import/export.

Total methods in this category: **32**

.. contents:: Classes in this Category
   :local:

DefaultSearchNode
-----------------

.. method:: asPath(arg0, arg1, arg2, arg3)

   **Signature:** ``asPath(double, double, double, String) -> Path``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)
   * **arg3** (``str``)

   **Returns:** ``Path``

.. method:: asPathReversed(arg0, arg1, arg2, arg3)

   **Signature:** ``asPathReversed(double, double, double, String) -> Path``

   **Parameters:**

   * **arg0** (``float``)
   * **arg1** (``float``)
   * **arg2** (``float``)
   * **arg3** (``str``)

   **Returns:** ``Path``


Fill
----

.. method:: writeNodesXML(arg0)

   **Signature:** ``writeNodesXML(PrintWriter) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``

.. method:: writeXML(arg0, arg1)

   **Signature:** ``writeXML(PrintWriter, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``int``)

   **Returns:** ``None``


MouseLightLoader
----------------

.. method:: saveAsJSON(arg0)

   Convenience method to save JSON data to a local directory.

   **Signature:** ``saveAsJSON(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``): - the output directory

   **Returns:** (``bool``) true, if successful

.. method:: saveAsSWC(arg0)

   Convenience method to save SWC data to a local directory.

   **Signature:** ``saveAsSWC(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``): - the output directory

   **Returns:** (``bool``) true, if successful


Path
----

.. method:: createPath()

   Returns a new Path with this Path's attributes (e.g. spatial scale), but no nodes.

   **Signature:** ``createPath() -> Path``

   **Returns:** (``Path``) the empty path

.. method:: drawPathAsPoints(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

   **Signature:** ``drawPathAsPoints(TracerCanvas, Graphics2D, Color, boolean, boolean, int, int) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)
   * **arg2** (``Any``)
   * **arg3** (``bool``)
   * **arg4** (``bool``)
   * **arg5** (``int``)
   * **arg6** (``int``)

   **Returns:** ``None``


PathAndFillManager
------------------

.. method:: deletePath(arg0)

   Deletes a path.

   **Signature:** ``deletePath(int) -> boolean``

   **Parameters:**

   * **arg0** (``int``): - the path to be deleted

   **Returns:** (``bool``) true, if path was found and successfully deleted

.. method:: deletePaths(arg0)

   Delete paths by position.

   **Signature:** ``deletePaths(Collection) -> boolean``

   **Parameters:**

   * **arg0** (``List[Any]``)

   **Returns:** ``bool``

.. method:: exportAllPathsAsSWC(arg0)

   Exports all as Paths as SWC file(s). Multiple files are created if multiple Trees exist.

   **Signature:** ``exportAllPathsAsSWC(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``): - the file path (including common basename) for exported files. The

   **Returns:** (``bool``) true, if successful

.. method:: exportFillsAsCSV(arg0)

   Export fills as CSV.

   **Signature:** ``exportFillsAsCSV(File) -> void``

   **Parameters:**

   * **arg0** (``str``): - the output file

   **Returns:** ``None``

.. method:: exportToCSV(arg0)

   Output some potentially useful information about all the Paths managed by this instance as a CSV (comma separated values) file.

   **Signature:** ``exportToCSV(File) -> void``

   **Parameters:**

   * **arg0** (``str``): - the output file

   **Returns:** ``None``

.. method:: exportTree(arg0, arg1)

   **Signature:** ``exportTree(int, File) -> boolean``

   **Parameters:**

   * **arg0** (``int``)
   * **arg1** (``str``)

   **Returns:** ``bool``

.. method:: static createFromFile(arg0, arg1)

   Creates a PathAndFillManager instance from imported data

   **Signature:** ``static createFromFile(String, [I) -> PathAndFillManager``

   **Parameters:**

   * **arg0** (``str``): - the absolute path of the file to be imported as per load(String, int...)
   * **arg1** (``Any``)

   **Returns:** (``Any``) the PathAndFillManager instance, or null if file could not be imported


PathChangeListener
------------------

.. method:: pathChanged(arg0)

   **Signature:** ``pathChanged(PathChangeEvent) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


PathFitter
----------

.. method:: readPreferences()

   **Signature:** ``readPreferences() -> void``

   **Returns:** ``None``


SNTService
----------

.. method:: loadGraph(arg0)

   **Signature:** ``loadGraph(DirectedWeightedGraph) -> void``

   **Parameters:**

   * **arg0** (``DirectedWeightedGraph``)

   **Returns:** ``None``

.. method:: loadTracings(arg0)

   Loads the specified tracings file.

   **Signature:** ``loadTracings(String) -> void``

   **Parameters:**

   * **arg0** (``str``): - either a "SWC", "TRACES" or "JSON" file path. URLs defining remote files also supported. Null not allowed.

   **Returns:** ``None``

.. method:: loadTree(arg0)

   Loads the specified tree. Note that if SNT has not been properly initialized, spatial calibration mismatches may occur. In that case, assign the spatial calibration of the image to {#@code Tree} using `Tree.assignImage(ImagePlus)`, before loading it.

   **Signature:** ``loadTree(Tree) -> void``

   **Parameters:**

   * **arg0** (``Tree``): - the Tree to be loaded (null not allowed).

   **Returns:** ``None``


SNTTable
--------

.. method:: static fromFile(arg0, arg1)

   Script-friendly method for loading tabular data from a file/URL.

   **Signature:** ``static fromFile(String, String) -> SNTTable``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)

   **Returns:** ``SNTTable``


SNTUtils
--------

.. method:: static downloadToTempFile(arg0)

   Downloads a file from the specified URL to a temporary file

   **Signature:** ``static downloadToTempFile(String) -> File``

   **Parameters:**

   * **arg0** (``str``): - the URL of the file to download

   **Returns:** (``str``) the downloaded file

.. method:: static fileAvailable(arg0)

   **Signature:** ``static fileAvailable(File) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: static getReconstructionFiles(arg0, arg1)

   Retrieves a list of reconstruction files stored in a common directory matching the specified criteria.

   **Signature:** ``static getReconstructionFiles(File, String) -> File;``

   **Parameters:**

   * **arg0** (``str``): - the directory containing the reconstruction files (.(e)swc, .traces, .json extension)
   * **arg1** (``str``)

   **Returns:** (``Any``) the array of files. An empty list is retrieved if dir is not a valid, readable directory.

.. method:: static getUniquelySuffixedFile(arg0)

   **Signature:** ``static getUniquelySuffixedFile(File) -> File``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``

.. method:: static getUniquelySuffixedTifFile(arg0)

   **Signature:** ``static getUniquelySuffixedTifFile(File) -> File``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``str``

.. method:: static isReconstructionFile(arg0)

   **Signature:** ``static isReconstructionFile(File) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

.. method:: static randomPaths()

   Generates a list of random paths. Only useful for debugging purposes

   **Signature:** ``static randomPaths() -> List``

   **Returns:** (``List[Any]``) the list of random Paths


SciViewSNT
----------

.. method:: syncPathManagerList()

   (Re)loads the current list of Paths in the Path Manager list.

   **Signature:** ``syncPathManagerList() -> boolean``

   **Returns:** (``bool``) true, if Path Manager list is not empty and synchronization was successful


Tree
----

.. method:: static fromFile(arg0)

   Script-friendly method for loading a Tree from a reconstruction file.

   **Signature:** ``static fromFile(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - the absolute path to the file (.Traces, (e)SWC or JSON) to be imported

   **Returns:** (``Tree``) the Tree instance, or null if file could not be imported


Viewer3D
--------

.. method:: loadMesh(arg0, arg1, arg2)

   Loads a Wavefront .OBJ file. Files should be loaded _before_ displaying the scene, otherwise, if the scene is already visible, validate() should be called to ensure all meshes are visible.

   **Signature:** ``loadMesh(String, ColorRGB, double) -> OBJMesh``

   **Parameters:**

   * **arg0** (``str``): - the absolute file path (or URL) of the file to be imported. The filename is used as unique identifier of the object (see setVisible(String, boolean))
   * **arg1** (``Any``)
   * **arg2** (``float``)

   **Returns:** (``Any``) the loaded OBJ mesh

.. method:: loadRefBrain(arg0)

   Loads the surface mesh of a supported reference brain/neuropil. Internet connection may be required.

   **Signature:** ``loadRefBrain(String) -> OBJMesh``

   **Parameters:**

   * **arg0** (``str``): - the reference brain to be loaded (case-insensitive). E.g., "zebrafish" (MP ZBA); "mouse" (Allen CCF); "JFRC2", "JFRC3" "JFRC2018", "FCWB"(adult), "L1", "L3", "VNC" (Drosophila)

   **Returns:** (``Any``) a reference to the loaded mesh


----

*Category index generated on 2025-11-23 00:28:41*