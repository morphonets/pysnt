I/O Operations Methods
======================

Methods that handle input/output operations, file loading, and data import/export.

Total methods in this category: **92**

.. contents:: Classes in this Category
   :local:

AStarRefiner
------------

.. method:: readPreferences()

   No-op: kept for consistency with `PathFitter`/`MultiSpectralRefiner`, which read persisted preferences here. A* re-tracing simply reuses whichever search parameters are already configured on the live `SNT` instance.

   **Signature:** ``readPreferences() -> void``

   **Returns:** ``None``


AutoTraceConfig
---------------

.. method:: fromPaths(paths, source, spacing)

   **Signature:** ``fromPaths(List, RandomAccessibleInterval, double[]) -> AutoTraceConfig``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **source** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``AutoTraceConfig``


Bdv
---

.. method:: onSntEditedPathModified()

   **Signature:** ``onSntEditedPathModified() -> void``

   **Returns:** ``None``

.. method:: onSntEditingPathChanged()

   **Signature:** ``onSntEditingPathChanged() -> void``

   **Returns:** ``None``

.. method:: playPaths(paths, speed, fov)

   **Signature:** ``playPaths(Collection, double, double) -> PathPlayer``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **speed** (``float``)
   * **fov** (``float``)

   **Returns:** ``Any``

.. method:: syncPathManagerList()

   **Signature:** ``syncPathManagerList() -> boolean``

   **Returns:** ``bool``


Bvv
---

.. method:: onSntEditedPathModified()

   **Signature:** ``onSntEditedPathModified() -> void``

   **Returns:** ``None``

.. method:: onSntEditingPathChanged()

   **Signature:** ``onSntEditingPathChanged() -> void``

   **Returns:** ``None``

.. method:: playPaths(paths, speed, fov)

   **Signature:** ``playPaths(Collection, double, double) -> PathPlayer``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **speed** (``float``)
   * **fov** (``float``)

   **Returns:** ``Any``

.. method:: saveSnapshot(filePath)

   Saves a snapshot of current scene as a PNG image to the specified path.

   **Signature:** ``saveSnapshot(String) -> boolean``

   **Parameters:**

   * **filePath** (``str``): - the absolute path of the destination file

   **Returns:** (``bool``) true, if file was successfully saved

.. method:: syncPathManagerList()

   **Signature:** ``syncPathManagerList() -> boolean``

   **Returns:** ``bool``


CrossSectionUtils
-----------------

.. method:: sampleProfile(nSamples, scale, ox, oy, direction, xSpacing, ySpacing, offsetX, offsetY, realAccess)

   Samples a 1D intensity profile along a direction vector, centered on a given world position. Intended for 2D images where the cross-section perpendicular to a path tangent is a line, not a plane.

   **Signature:** ``sampleProfile(int, double, double, double, double[], double, double, double, double, RealRandomAccess) -> float[]``

   **Parameters:**

   * **nSamples** (``int``): - number of samples (should be odd so center is well-defined)
   * **scale** (``float``)
   * **ox** (``float``)
   * **oy** (``float``)
   * **direction** (``List[float]``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **offsetX** (``float``)
   * **offsetY** (``float``)
   * **realAccess** (``Any``)

   **Returns:** (``List[float]``) the sampled profile as a float array


DefaultSearchNode
-----------------

.. method:: asPath(x_spacing, y_spacing, z_spacing, spacing_units)

   **Signature:** ``asPath(double, double, double, String) -> Path``

   **Parameters:**

   * **x_spacing** (``float``)
   * **y_spacing** (``float``)
   * **z_spacing** (``float``)
   * **spacing_units** (``str``)

   **Returns:** ``Path``

.. method:: asPathReversed(x_spacing, y_spacing, z_spacing, spacing_units)

   **Signature:** ``asPathReversed(double, double, double, String) -> Path``

   **Parameters:**

   * **x_spacing** (``float``)
   * **y_spacing** (``float``)
   * **z_spacing** (``float``)
   * **spacing_units** (``str``)

   **Returns:** ``Path``


DelineationsManager
-------------------

.. method:: importFromLabelImage(labelImp)

   Convenience overload accepting an `ImagePlus`, which is converted to an `ImgPlus` via `ImpUtils.toImgPlus3D(ImagePlus, int, int)`.

   **Signature:** ``importFromLabelImage(ImagePlus) -> int``

   **Parameters:**

   * **labelImp** (``Any``): - the labels ImagePlus

   **Returns:** (``int``) the number of unique labels imported


DetectorUtils
-------------

.. method:: assignToNearestPaths(detections, allPaths)

   **Signature:** ``assignToNearestPaths(List, Collection) -> List``

   **Parameters:**

   * **detections** (``List[Any]``)
   * **allPaths** (``List[Any]``)

   **Returns:** ``List[Any]``


Fill
----

.. method:: writeNodesXML(pw)

   **Signature:** ``writeNodesXML(PrintWriter) -> void``

   **Parameters:**

   * **pw** (``Any``)

   **Returns:** ``None``

.. method:: writeXML(pw, fillIndex)

   **Signature:** ``writeXML(PrintWriter, int) -> void``

   **Parameters:**

   * **pw** (``Any``)
   * **fillIndex** (``int``)

   **Returns:** ``None``


ImgUtils
--------

.. method:: saveAsOmeZarr(img, zarrDir, nThreads, progress)

   Writes an image as a multiscale OME-Zarr (OME-NGFF v0.5, Zarr v3) directory. Level 0 is streamed from `img` one slab of Z planes at a time (so every plane is read once), and each coarser level is computed from the previous one, one block at a time, by averaging 2x2x2 neighborhoods. Peak memory is therefore a single slab plus the blocks in flight, regardless of image size. Chunks are zstd-compressed and, for larger levels, grouped into shards (one file per shard)

Levels are halved along X, Y and Z until a level fits a 3D texture (2048 voxels per side, and `BvvUtils.MAX_SINGLE_TEXTURE_VOXELS`), with a minimum of 3 levels

   **Signature:** ``saveAsOmeZarr(ImgPlus, File, int, Consumer) -> void``

   **Parameters:**

   * **img** (``Any``): - image with X, Y, Z leading, followed by an optional channel axis and an optional time axis (see normalizeToXYZ(net.imagej.ImgPlus<T>))
   * **zarrDir** (``str``)
   * **nThreads** (``int``)
   * **progress** (``Any``)

   **Returns:** ``None``


MouseLightLoader
----------------

.. method:: saveAsJSON(outputDirectory)

   Convenience method to save JSON data to a local directory.

   **Signature:** ``saveAsJSON(String) -> boolean``

   **Parameters:**

   * **outputDirectory** (``str``): - the output directory

   **Returns:** (``bool``) true, if successful

.. method:: saveAsSWC(outputDirectory)

   Convenience method to save SWC data to a local directory.

   **Signature:** ``saveAsSWC(String) -> boolean``

   **Parameters:**

   * **outputDirectory** (``str``): - the output directory

   **Returns:** (``bool``) true, if successful


MultiSpectralRefiner
--------------------

.. method:: readPreferences()

   Reads stored preferences from `MultiSpectralRefinerCmd` and applies them to this refiner. If auto-intensity is enabled in the preferences, the auto-calibrated values from the constructor are preserved.

   **Signature:** ``readPreferences() -> void``

   **Returns:** ``None``


Path
----

.. method:: createPath()

   Returns a new Path with this Path's attributes (e.g. spatial scale), but no nodes.

   **Signature:** ``createPath() -> Path``

   **Returns:** (``Path``) the empty path

.. method:: drawPathAsPoints(canvas, g, c, plane, highContrast, drawDiameter)

   **Signature:** ``drawPathAsPoints(TracerCanvas, Graphics2D, Color, int, boolean, boolean) -> void``

   **Parameters:**

   * **canvas** (``TracerCanvas``)
   * **g** (``Any``)
   * **c** (``Any``)
   * **plane** (``int``)
   * **highContrast** (``bool``)
   * **drawDiameter** (``bool``)

   **Returns:** ``None``


PathAndFillManager
------------------

.. method:: createFromFile(filePath, swcTypes)

   Creates a PathAndFillManager instance from imported data

   **Signature:** ``createFromFile(String, int[]) -> PathAndFillManager``

   **Parameters:**

   * **filePath** (``str``): - the absolute path of the file to be imported as per load(String, int...)
   * **swcTypes** (``List[int]``)

   **Returns:** (``PathAndFillManager``) the PathAndFillManager instance, or null if file could not be imported

.. method:: deletePath(p)

   Deletes a path.

   **Signature:** ``deletePath(Path) -> boolean``

   **Parameters:**

   * **p** (``Path``): - the path to be deleted

   **Returns:** (``bool``) true, if path was found and successfully deleted

.. method:: deletePaths(paths)

   Delete paths by position.

   **Signature:** ``deletePaths(Collection) -> boolean``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``bool``

.. method:: exportAllPathsAsSWC(baseFilename)

   **Signature:** ``exportAllPathsAsSWC(String) -> boolean``

   **Parameters:**

   * **baseFilename** (``str``)

   **Returns:** ``bool``

.. method:: exportFillsAsCSV(outputFile)

   Export fills as CSV.

   **Signature:** ``exportFillsAsCSV(File) -> void``

   **Parameters:**

   * **outputFile** (``str``): - the output file

   **Returns:** ``None``

.. method:: exportToCSV(outputFile)

   Output some potentially useful information about all the Paths managed by this instance as a CSV (comma separated values) file.

   **Signature:** ``exportToCSV(File) -> void``

   **Parameters:**

   * **outputFile** (``str``): - the output file

   **Returns:** ``None``

.. method:: exportTree(treeIndex, file)

   **Signature:** ``exportTree(int, File) -> boolean``

   **Parameters:**

   * **treeIndex** (``int``)
   * **file** (``str``)

   **Returns:** ``bool``

.. method:: importNeurons(map, color, spatialUnit)

   Import neuron(s) as a collection of reconstruction nodes (SWC points)

   **Signature:** ``importNeurons(Map, ColorRGB, String) -> Map``

   **Parameters:**

   * **map** (``Dict[str, Any]``): - the input map of reconstruction nodes
   * **color** (``Any``)
   * **spatialUnit** (``str``)

   **Returns:** (``Dict[str, Any]``) the map mapping imported ids to imported Trees. A null Tree will be assigned if a morphology could not be imported

.. method:: importSWC(descriptor, urlOrFilePath)

   Imports an SWC file using advanced options.

   **Signature:** ``importSWC(String, String) -> boolean``

   **Parameters:**

   * **descriptor** (``str``): - the absolute file path to the imported file
   * **urlOrFilePath** (``str``)

   **Returns:** (``bool``) true, if import was successful

.. method:: importSWCs(swcs, color)

   Imports a group of SWC files (Remote URLs supported).

   **Signature:** ``importSWCs(Map, ColorRGB) -> List``

   **Parameters:**

   * **swcs** (``Dict[str, Any]``): - the HashMap containing the absolute file paths (or URLs) of files to be imported as values and a file descriptor as keys.
   * **color** (``Any``)

   **Returns:** (``List[Any]``) the List of imported `Tree`s labeled after the file descriptor. The returned list will not contain null elements: If a file was not successfully imported an empty Tree will be generated

.. method:: loadGuessingType(filePathOrURL)

   **Signature:** ``loadGuessingType(String) -> boolean``

   **Parameters:**

   * **filePathOrURL** (``str``)

   **Returns:** ``bool``

.. method:: nearestNodeOnPaths(paths, x, y, z)

   Finds the node nearest to a position, across the given paths as they are (no fitted/unfitted resolution: see `nearestNodeInUse(Collection, double, double, double)`).

   **Signature:** ``nearestNodeOnPaths(Collection, double, double, double) -> NodeRef``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to be searched. Empty paths are skipped
   * **x** (``float``)
   * **y** (``float``)
   * **z** (``float``)

   **Returns:** (``Any``) the nearest node, or null if the paths hold no nodes

.. method:: nearestPointOnAnyPath(paths, pic, distanceLimit)

   **Signature:** ``nearestPointOnAnyPath(Collection, PointInCanvas, double) -> NearPoint``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **pic** (``Any``)
   * **distanceLimit** (``float``)

   **Returns:** ``Any``

.. method:: pathChanged(event)

   **Signature:** ``pathChanged(PathChangeEvent) -> void``

   **Parameters:**

   * **event** (``Any``)

   **Returns:** ``None``

.. method:: repairPhantomFittedPaths()

   Repairs the paths returned by `getPhantomFittedPaths()` into ordinary, standalone paths: assigns each a fresh, valid (positive, collision-free) ID and a default name, since the fit-time name/ID are meaningless once the original they were fitted from is gone.

   **Signature:** ``repairPhantomFittedPaths() -> int``

   **Returns:** (``int``) the number of paths repaired

.. method:: transformPaths(transformation, templateImage, modelImage)

   **Signature:** ``transformPaths(PathTransformer, ImagePlus, ImagePlus) -> PathAndFillManager``

   **Parameters:**

   * **transformation** (``Any``)
   * **templateImage** (``Any``)
   * **modelImage** (``Any``)

   **Returns:** ``PathAndFillManager``


PathFitter
----------

.. method:: readPreferences()

   **Signature:** ``readPreferences() -> void``

   **Returns:** ``None``


PathManagerUI
-------------

.. method:: extractTagsFromPath(p)

   **Signature:** ``extractTagsFromPath(Path) -> String``

   **Parameters:**

   * **p** (``Path``)

   **Returns:** ``str``

.. method:: extractTagsFromPaths(paths)

   **Signature:** ``extractTagsFromPaths(Collection) -> Set``

   **Parameters:**

   * **paths** (``List[Any]``)

   **Returns:** ``Set[Any]``

.. method:: geSelectedPathsAsTree()

   Gets the collection of paths listed in the Path Manager as a `Tree` object. All paths are retrieved if none are currently selected.

   **Signature:** ``geSelectedPathsAsTree() -> Tree``

   **Returns:** (``Tree``) the Tree holding the Path collection

.. method:: refreshForPaths(paths)

   Repaints the Path Manager view for the given paths. Public hook used by external mutators (e.g. the Curation Assistant's review-tag actions in `CurationManager`) that change path names directly and need the table to pick the change up; bypasses the heavier viewer-update pass because path mutations like tag-suffix edits don't affect 3D viewers.

   **Signature:** ``refreshForPaths(Collection) -> void``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths whose representation in the manager needs to refresh;

   **Returns:** ``None``


PlausibilityCalibrator
----------------------

.. method:: listCurationFiles(workspaceDir)

   **Signature:** ``listCurationFiles(File) -> File[]``

   **Parameters:**

   * **workspaceDir** (``str``)

   **Returns:** ``List[str]``

.. method:: loadBuiltIn(presetName, monitor)

   **Signature:** ``loadBuiltIn(String, PlausibilityMonitor) -> void``

   **Parameters:**

   * **presetName** (``str``)
   * **monitor** (``PlausibilityMonitor``)

   **Returns:** ``None``


PlausibilityMonitor
-------------------

.. method:: onPathFinalized(completedChild)

   **Signature:** ``onPathFinalized(Path) -> List``

   **Parameters:**

   * **completedChild** (``Path``)

   **Returns:** ``List[Any]``


SNT
---

.. method:: deselectLastPath()

   Removes the most recently selected path from the current selection (so nothing remains selected if only one path was selected). Does nothing in edit mode, in which a single path is always selected

   **Signature:** ``deselectLastPath() -> Path``

   **Returns:** (``Path``) the path that was deselected, or null if there was nothing to deselect

.. method:: initPathsToFill(fromPaths, splitFillerThreads)

   **Signature:** ``initPathsToFill(Set, boolean) -> void``

   **Parameters:**

   * **fromPaths** (``Set[Any]``)
   * **splitFillerThreads** (``bool``)

   **Returns:** ``None``

.. method:: loadLabelsFile(path)

   **Signature:** ``loadLabelsFile(String) -> void``

   **Parameters:**

   * **path** (``str``)

   **Returns:** ``None``

.. method:: loadSecondaryImage(file)

   **Signature:** ``loadSecondaryImage(File) -> void``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``None``

.. method:: loadTracings(file)

   **Signature:** ``loadTracings(File) -> boolean``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``bool``

.. method:: makePathVolume(paths, labelsImage)

   Rasterizes centerline of paths into an ImagePlus

   **Signature:** ``makePathVolume(Collection, boolean) -> ImagePlus``

   **Parameters:**

   * **paths** (``List[Any]``): - If true, each path has a unique intensity; otherwise all nodes are set to 255 (8-bit Binary)
   * **labelsImage** (``bool``)

   **Returns:** (``Any``) the ImagePlus with embedded centerlines

.. method:: notifyEditingPathChanged()

   Refreshes the Bdv/Bvv rendering of the path being edited after it was modified by the tracing canvas. Throttled so that continuous gestures (e.g., dragging a node) do not flood the viewers

   **Signature:** ``notifyEditingPathChanged() -> void``

   **Returns:** ``None``

.. method:: selectPath(p, addToExistingSelection)

   **Signature:** ``selectPath(Path, boolean) -> void``

   **Parameters:**

   * **p** (``Path``)
   * **addToExistingSelection** (``bool``)

   **Returns:** ``None``


SNTChart
--------

.. method:: saveAsPDF(filePath)

   **Signature:** ``saveAsPDF(String) -> void``

   **Parameters:**

   * **filePath** (``str``)

   **Returns:** ``None``

.. method:: saveAsPNG(file)

   **Signature:** ``saveAsPNG(File) -> void``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``None``

.. method:: saveAsSVG(filePath)

   **Signature:** ``saveAsSVG(String) -> void``

   **Parameters:**

   * **filePath** (``str``)

   **Returns:** ``None``


SNTPrefs
--------

.. method:: deselectedPathColor()

   **Signature:** ``deselectedPathColor() -> Color``

   **Returns:** ``Any``

.. method:: selectedPathColor()

   **Signature:** ``selectedPathColor() -> Color``

   **Returns:** ``Any``


SNTService
----------

.. method:: loadGraph(graph)

   **Signature:** ``loadGraph(DirectedWeightedGraph) -> void``

   **Parameters:**

   * **graph** (``DirectedWeightedGraph``)

   **Returns:** ``None``

.. method:: loadTracings(filePathOrURL)

   Loads the specified tracings file.

   **Signature:** ``loadTracings(String) -> void``

   **Parameters:**

   * **filePathOrURL** (``str``): - either a "SWC", "TRACES" or "JSON" file path or URL

   **Returns:** ``None``

.. method:: loadTree(tree)

   Loads the specified tree. Note that if SNT has not been properly initialized, spatial calibration mismatches may occur. In that case, assign the spatial calibration of the image to {#@code Tree} using `Tree.assignImage(ImagePlus)`, before loading it.

   **Signature:** ``loadTree(Tree) -> void``

   **Parameters:**

   * **tree** (``Tree``): - the Tree to be loaded (null not allowed).

   **Returns:** ``None``

.. method:: loadTrees(trees)

   Loads the specified collection of trees.

   **Signature:** ``loadTrees(Collection) -> void``

   **Parameters:**

   * **trees** (``List[Any]``): - the collection of Tree to be loaded (null not allowed).

   **Returns:** ``None``


SNTTable
--------

.. method:: fromFile(filePathOrURL)

   Script-friendly method for loading tabular data from a file/URL.

   **Signature:** ``fromFile(String) -> SNTTable``

   **Parameters:**

   * **filePathOrURL** (``str``): - the absolute path or URL to the tabular file to be imported

   **Returns:** (``SNTTable``) the SNTTable or null if file could not be imported


SNTUtils
--------

.. method:: downloadToTempFile(fileUrl)

   Downloads a file from the specified URL to a temporary file

   **Signature:** ``downloadToTempFile(String) -> File``

   **Parameters:**

   * **fileUrl** (``str``): - the URL of the file to download

   **Returns:** (``str``) the downloaded file

.. method:: fileAvailable(file)

   **Signature:** ``fileAvailable(File) -> boolean``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``bool``

.. method:: randomPaths()

   Generates a list of random paths. Only useful for debugging purposes

   **Signature:** ``randomPaths() -> List``

   **Returns:** (``List[Any]``) the list of random Paths

.. method:: sanitizeFilename(filename)

   Replaces characters that are unsafe/reserved in filenames with an underscore, leaving alphanumerics, dots, and hyphens untouched.

   **Signature:** ``sanitizeFilename(String) -> String``

   **Parameters:**

   * **filename** (``str``): - the candidate filename (or a full path -- only used for e.g. a whole path rather than a bare filename component; separators are not treated specially and will themselves be replaced)

   **Returns:** (``str``) the sanitized filename, or null if `filename` is null


SeedOverlay
-----------

.. method:: loadCsv(file, replace)

   **Signature:** ``loadCsv(File, boolean) -> CsvImportResult``

   **Parameters:**

   * **file** (``str``)
   * **replace** (``bool``)

   **Returns:** ``Any``

.. method:: saveAs(file)

   **Signature:** ``saveAs(File) -> void``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``None``


ShollTable
----------

.. method:: fromFile(filePathOrURL)

   **Signature:** ``fromFile(String) -> SNTTable``

   **Parameters:**

   * **filePathOrURL** (``str``)

   **Returns:** ``SNTTable``

.. method:: listProfileEntries()

   **Signature:** ``listProfileEntries() -> void``

   **Returns:** ``None``

.. method:: saveSilently(file)

   **Signature:** ``saveSilently(File) -> boolean``

   **Parameters:**

   * **file** (``str``)

   **Returns:** ``bool``


SomaUtils
---------

.. method:: roiToSomaPath(roi, referencePath)

   **Signature:** ``roiToSomaPath(Roi, Path) -> Path``

   **Parameters:**

   * **roi** (``Any``)
   * **referencePath** (``Path``)

   **Returns:** ``Path``


SpectralSimilarity
------------------

.. method:: averageColorFromPaths(input, paths, xSpacing, ySpacing, zSpacing)

   As 
```
averageColorFromPaths(RandomAccessibleInterval, java.util.List, double, double, double)
```
, but also adding a pixel-space offset after scaling (see 
```
nodeToPixelCoords(sc.fiji.snt.util.PointInImage, double, double, double, double, double, double)
```
) - needed whenever `input` is the crop-local grid of a materialized crop, or the raw streamed source's own voxel grid under a non-zero `SNT#getWorldOriginOffset()`.

   **Signature:** ``averageColorFromPaths(RandomAccessibleInterval, List, double, double, double) -> double[]``

   **Parameters:**

   * **input** (``Any``): - pixel-space offset added after scaling, x axis
   * **paths** (``List[Any]``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)

   **Returns:** ``List[float]``


Tree
----

.. method:: fromFile(filePath)

   Script-friendly method for loading a Tree from a reconstruction file.

   **Signature:** ``fromFile(String) -> Tree``

   **Parameters:**

   * **filePath** (``str``): - the absolute path to the file (.Traces, (e)SWC or JSON) to be imported

   **Returns:** (``Tree``) the Tree instance, or null if file could not be imported

.. method:: listFromFile(tracesOrJsonFile)

   Retrieves a list of `Tree`s from a single file.

   **Signature:** ``listFromFile(String) -> Collection``

   **Parameters:**

   * **tracesOrJsonFile** (``str``): - the file containing the reconstructions (typically a .traces or .json extension). A directory is also supported, as is a remote URL: a single reconstruction file (SWC/.traces/.json/.ndf/Neurolucida) is streamed directly, while a

   **Returns:** (``List[Any]``) the collection of imported `Tree`s. An empty list is retrieved if `tracesOrJsonFile` is not a valid, readable file.

.. method:: saveAsSWC(filePath)

   Saves this Tree to an SWC file.

   **Signature:** ``saveAsSWC(String) -> boolean``

   **Parameters:**

   * **filePath** (``str``): - the absolute path of the output file.

   **Returns:** (``bool``) true, if file successfully saved.


TreeToRaster
------------

.. method:: rasterizePathLabels()

   Rasterizes the tree into a 16-bit label image where each voxel is assigned the 1-based index of the `Path` that owns it (as ordered by `Tree.list()`). Background voxels are 0.

At intersection sites where multiple paths overlap, the path with the largest local radius wins (thickest-wins priority), ensuring that thin branches crossing a thick trunk do not overwrite it.

The returned image has the same dimensions and calibration as the density image produced by `rasterize()`, so the two can be used as overlays. Noise and blur settings are ignored for label images.

   **Signature:** ``rasterizePathLabels() -> ImagePlus``

   **Returns:** (``Any``) a 16-bit `ImagePlus` of path labels


TreeUtils
---------

.. method:: findPathsNeedingReversal(paths, rootLocation)

   Determines which paths need to be reversed so that their start nodes point toward a given root location.

A path should be reversed if its end node is closer to the root than its start node.

   **Signature:** ``findPathsNeedingReversal(Collection, PointInImage) -> List``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to analyze
   * **rootLocation** (``PointInImage``)

   **Returns:** (``List[Any]``) list of paths that should be reversed (subset of input)

.. method:: mergeContinuousPaths(tree, angleThreshold)

   Merges paths that continue along the same trajectory at branch points, reducing fragmentation in auto-traced reconstructions.

**Problem:** Auto-tracers like `GWDTTracer` often create separate paths at every branch point, even when the neurite continues straight through. This may fragment continuous paths into smaller segments.

**Solution:** At each junction where a parent path ends and children begin, this method checks if any child's trajectory aligns with the parent's. If the angle between their direction vectors is below the threshold, the most aligned child is merged into the parent, creating a longer continuous path.

**Algorithm:**

#. For each path with children, compute the parent's end tangent vector (direction at its terminal segment)

#. For each child, compute its start tangent vector

#. Find the child with the smallest angle to the parent direction

#. If this angle ≤ threshold: append child's nodes to parent, reparent grandchildren to the extended parent, remove child from tree

#. Repeat until no more merges are possible

**Criteria for merging:** Two paths are merged when:

- The child starts at the parent's endpoint (branch point)

- The angle between their direction vectors ≤ `angleThreshold`

- The child is the *most aligned* among all siblings

**Example:** A traced axon might be split into 5 paths at 4 branch points: 
```
Before: P1 → P2 → P3 → P4 → P5  (with side branches B1, B2, B3, B4)
 After:  P1 (merged trunk) with children B1, B2, B3, B4
```


   **Signature:** ``mergeContinuousPaths(Tree, double) -> int``

   **Parameters:**

   * **tree** (``Tree``): - maximum angle (in degrees) between parent end tangent and child start tangent for paths to be considered continuous. Suggested values:

15-20°: strict, only nearly straight continuations 30°: moderate (default), allows gentle curves 45°: permissive, may merge actual branches

Use 0 or negative to disable merging.
   * **angleThreshold** (``float``)

   **Returns:** (``int``) the number of paths that were merged (and removed from the tree)

   **Example:**

   .. code-block:: java

      Before: P1 → P2 → P3 → P4 → P5  (with side branches B1, B2, B3, B4)
       After:  P1 (merged trunk) with children B1, B2, B3, B4

.. method:: mergePaths(orderedPaths, reparentChildren)

   Merges a list of paths into a single path by appending nodes sequentially.

The paths should be pre-ordered and oriented using `orderByEndpointProximity(java.util.Collection<sc.fiji.snt.Path>)` and `orientPathsForMerging(java.util.List<sc.fiji.snt.Path>)`.

This method handles:

- Appending nodes from each path to the result

- Optionally reparenting children of merged paths to the result

- Preserving the first path's parent connection (if any)

**Note:** This method does NOT delete the original paths from any manager. The caller is responsible for cleanup.

   **Signature:** ``mergePaths(List, boolean) -> Path``

   **Parameters:**

   * **orderedPaths** (``List[Any]``): - paths to merge, in order (should be oriented for merging)
   * **reparentChildren** (``bool``)

   **Returns:** (``Path``) the merged path, or null if input is empty

.. method:: orientPathsForMerging(orderedPaths)

   Orients paths in a chain so they can be merged end-to-start. After this operation, each path's end node will be near the next path's start node.

Paths are reversed in-place as needed.

   **Signature:** ``orientPathsForMerging(List) -> void``

   **Parameters:**

   * **orderedPaths** (``List[Any]``): - list of paths previously ordered by orderByEndpointProximity(java.util.Collection<sc.fiji.snt.Path>)

   **Returns:** ``None``

.. method:: orientPathsTowardRoot(paths, rootLocation)

   Orients paths so their start nodes point toward a given root location. Paths are reversed in-place if their end node is closer to the root.

**Note:** This method does NOT update child branch points. Callers must handle child branch point updates separately if paths have children.

   **Signature:** ``orientPathsTowardRoot(Collection, PointInImage) -> int``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to orient
   * **rootLocation** (``PointInImage``)

   **Returns:** (``int``) the number of paths that were reversed

.. method:: splitByPrimaryPaths(tree)

   Splits a tree with multiple primary paths into separate trees, one rooted at each primary path.

   **Signature:** ``splitByPrimaryPaths(Tree) -> List``

   **Parameters:**

   * **tree** (``Tree``)

   **Returns:** ``List[Any]``


Viewer3D
--------

.. method:: loadMesh(filePath, color, transparencyPercent)

   Loads a Wavefront .OBJ file. Files should be loaded _before_ displaying the scene, otherwise, if the scene is already visible, `validate()` should be called to ensure all meshes are visible.

   **Signature:** ``loadMesh(String, ColorRGB, double) -> OBJMesh``

   **Parameters:**

   * **filePath** (``str``): - the absolute file path (or URL) of the file to be imported. The filename is used as unique identifier of the object (see setVisible(String, boolean))
   * **color** (``Any``)
   * **transparencyPercent** (``float``)

   **Returns:** (``OBJMesh``) the loaded OBJ mesh

.. method:: loadRefBrain(template)

   Loads the surface mesh of a supported reference brain/neuropil. Internet connection may be required.

   **Signature:** ``loadRefBrain(String) -> OBJMesh``

   **Parameters:**

   * **template** (``str``): - the reference brain to be loaded (case-insensitive). E.g., "zebrafish" (MP ZBA); "mouse" (Allen CCF); "JFRC2", "JFRC3" "JFRC2018", "FCWB"(adult), "L1", "L3", "VNC" (Drosophila)

   **Returns:** (``OBJMesh``) a reference to the loaded mesh

.. method:: saveScene(directory, visibleOnly)

   Saves the contents of the scene to a directory: reconstructions as `.traces` files and meshes as `.obj` files (with a companion `.mtl` file storing their color). Annotations are currently not saved.

   **Signature:** ``saveScene(File, boolean) -> int``

   **Parameters:**

   * **directory** (``str``): - the destination directory (created if needed)
   * **visibleOnly** (``bool``)

   **Returns:** (``int``) the number of files written

.. method:: saveSnapshot()

   **Signature:** ``saveSnapshot() -> boolean``

   **Returns:** ``bool``

.. method:: syncPathManagerList()

   (Re)loads the current list of Paths in the Path Manager list.

   **Signature:** ``syncPathManagerList() -> boolean``

   **Returns:** (``bool``) true, if synchronization was apparently successful, false otherwise


----

*Category index generated on 2026-11-02 07:57:40*