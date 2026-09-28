I/O Operations Methods
======================

Methods that handle input/output operations, file loading, and data import/export.

Total methods in this category: **43**

.. contents:: Classes in this Category
   :local:

AStarRefiner
------------

.. method:: readPreferences()

   No-op: kept for consistency with PathFitter/MultiSpectralRefiner, which read persisted preferences here. A* re-tracing simply reuses whichever search parameters are already configured on the live SNT instance.

   **Signature:** ``readPreferences() -> void``

   **Returns:** ``None``


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

   **Signature:** ``deletePaths([I) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the indices to be deleted

   **Returns:** ``None``

.. method:: exportAllPathsAsSWC(arg0)

   **Signature:** ``exportAllPathsAsSWC(String) -> boolean``

   **Parameters:**

   * **arg0** (``str``)

   **Returns:** ``bool``

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

.. method:: static getUniquelySuffixedFile(arg0, arg1)

   **Signature:** ``static getUniquelySuffixedFile(File, String) -> File``

   **Parameters:**

   * **arg0** (``str``)
   * **arg1** (``str``)

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

.. method:: static sanitizeFilename(arg0)

   Replaces characters that are unsafe/reserved in filenames with an underscore, leaving alphanumerics, dots, and hyphens untouched.

   **Signature:** ``static sanitizeFilename(String) -> String``

   **Parameters:**

   * **arg0** (``str``): - the candidate filename (or a full path -- only used for e.g. a whole path rather than a bare filename component; separators are not treated specially and will themselves be replaced)

   **Returns:** (``str``) the sanitized filename, or null if filename is null


SciViewSNT
----------

.. method:: syncPathManagerList()

   (Re)loads the current list of Paths in the Path Manager list.

   **Signature:** ``syncPathManagerList() -> boolean``

   **Returns:** (``bool``) true, if Path Manager list is not empty and synchronization was successful


SpectralSimilarity
------------------

.. method:: static averageColorFromPaths(arg0, arg1, arg2, arg3, arg4)

   As 
```
averageColorFromPaths(RandomAccessibleInterval, java.util.List, double, double, double)
```
, but also adding a pixel-space offset after scaling (see 
```
nodeToPixelCoords(sc.fiji.snt.util.PointInImage, double, double, double, double, double, double)
```
) - needed whenever input is the crop-local grid of a materialized crop, or the raw streamed source's own voxel grid under a non-zero `SNT#getWorldOriginOffset()`.

   **Signature:** ``static averageColorFromPaths(RandomAccessibleInterval, List, double, double, double) -> [D``

   **Parameters:**

   * **arg0** (``Any``): - pixel-space offset added after scaling, x axis
   * **arg1** (``List[Any]``)
   * **arg2** (``float``)
   * **arg3** (``float``)
   * **arg4** (``float``)

   **Returns:** ``Any``


Tree
----

.. method:: static fromFile(arg0)

   Script-friendly method for loading a Tree from a reconstruction file.

   **Signature:** ``static fromFile(String) -> Tree``

   **Parameters:**

   * **arg0** (``str``): - the absolute path to the file (.Traces, (e)SWC or JSON) to be imported

   **Returns:** (``Tree``) the Tree instance, or null if file could not be imported


TreeToRaster
------------

.. method:: rasterizePathLabels()

   Rasterizes the tree into a 16-bit label image where each voxel is assigned the 1-based index of the Path that owns it (as ordered by Tree.list()). Background voxels are 0.

At intersection sites where multiple paths overlap, the path with the largest local radius wins (thickest-wins priority), ensuring that thin branches crossing a thick trunk do not overwrite it.

The returned image has the same dimensions and calibration as the density image produced by rasterize(), so the two can be used as overlays. Noise and blur settings are ignored for label images.

   **Signature:** ``rasterizePathLabels() -> ImagePlus``

   **Returns:** (``Any``) a 16-bit ImagePlus of path labels


TreeUtils
---------

.. method:: static findPathsNeedingReversal(arg0, arg1)

   Determines which paths need to be reversed so that their start nodes point toward a given root location.

A path should be reversed if its end node is closer to the root than its start node.

   **Signature:** ``static findPathsNeedingReversal(Collection, PointInImage) -> List``

   **Parameters:**

   * **arg0** (``List[Any]``): - the paths to analyze
   * **arg1** (``PointInImage``)

   **Returns:** (``List[Any]``) list of paths that should be reversed (subset of input)

.. method:: static getRootPath(arg0)

   Gets the root path of the tree containing the given path.

   **Signature:** ``static getRootPath(Path) -> Path``

   **Parameters:**

   * **arg0** (``Path``)

   **Returns:** ``Path``

.. method:: static mergeContinuousPaths(arg0, arg1)

   Merges paths that continue along the same trajectory at branch points, reducing fragmentation in auto-traced reconstructions.

Problem: Auto-tracers like GWDTTracer often create separate paths at every branch point, even when the neurite continues straight through. This may fragment continuous paths into smaller segments.

Solution: At each junction where a parent path ends and children begin, this method checks if any child's trajectory aligns with the parent's. If the angle between their direction vectors is below the threshold, the most aligned child is merged into the parent, creating a longer continuous path.

Algorithm:

For each path with children, compute the parent's end tangent vector (direction at its terminal segment) For each child, compute its start tangent vector Find the child with the smallest angle to the parent direction If this angle ≤ threshold: append child's nodes to parent, reparent grandchildren to the extended parent, remove child from tree Repeat until no more merges are possible

Criteria for merging: Two paths are merged when:

The child starts at the parent's endpoint (branch point) The angle between their direction vectors ≤ angleThreshold The child is the most aligned among all siblings

Example: A traced axon might be split into 5 paths at 4 branch points: 
```
Before: P1 → P2 → P3 → P4 → P5  (with side branches B1, B2, B3, B4)
 After:  P1 (merged trunk) with children B1, B2, B3, B4
```


   **Signature:** ``static mergeContinuousPaths(Tree, double) -> int``

   **Parameters:**

   * **arg0** (``Tree``): - maximum angle (in degrees) between parent end tangent and child start tangent for paths to be considered continuous. Suggested values:

15-20°: strict, only nearly straight continuations 30°: moderate (default), allows gentle curves 45°: permissive, may merge actual branches

Use 0 or negative to disable merging.
   * **arg1** (``float``)

   **Returns:** (``int``) the number of paths that were merged (and removed from the tree)

   **Example:**

   .. code-block:: java

      Before: P1 → P2 → P3 → P4 → P5  (with side branches B1, B2, B3, B4)
       After:  P1 (merged trunk) with children B1, B2, B3, B4

.. method:: static mergePaths(arg0, arg1)

   Merges a list of paths into a single path by appending nodes sequentially.

The paths should be pre-ordered and oriented using `orderByEndpointProximity(java.util.Collection<sc.fiji.snt.Path>)` and `orientPathsForMerging(java.util.List<sc.fiji.snt.Path>)`.

This method handles:

Appending nodes from each path to the result Optionally reparenting children of merged paths to the result Preserving the first path's parent connection (if any)

Note: This method does NOT delete the original paths from any manager. The caller is responsible for cleanup.

   **Signature:** ``static mergePaths(List, boolean) -> Path``

   **Parameters:**

   * **arg0** (``List[Any]``): - paths to merge, in order (should be oriented for merging)
   * **arg1** (``bool``)

   **Returns:** (``Path``) the merged path, or null if input is empty

.. method:: static orientPathsForMerging(arg0)

   Orients paths in a chain so they can be merged end-to-start. After this operation, each path's end node will be near the next path's start node.

Paths are reversed in-place as needed.

   **Signature:** ``static orientPathsForMerging(List) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - list of paths previously ordered by orderByEndpointProximity(java.util.Collection<sc.fiji.snt.Path>)

   **Returns:** ``None``

.. method:: static orientPathsTowardRoot(arg0, arg1)

   Orients paths so their start nodes point toward a given root location. Paths are reversed in-place if their end node is closer to the root.

Note: This method does NOT update child branch points. Callers must handle child branch point updates separately if paths have children.

   **Signature:** ``static orientPathsTowardRoot(Collection, PointInImage) -> int``

   **Parameters:**

   * **arg0** (``List[Any]``): - the paths to orient
   * **arg1** (``PointInImage``)

   **Returns:** (``int``) the number of paths that were reversed

.. method:: static splitByPrimaryPaths(arg0)

   Splits a tree with multiple primary paths into separate trees, one rooted at each primary path.

   **Signature:** ``static splitByPrimaryPaths(Tree) -> List``

   **Parameters:**

   * **arg0** (``Tree``)

   **Returns:** ``List[Any]``


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

*Category index generated on 2026-09-27 23:02:20*