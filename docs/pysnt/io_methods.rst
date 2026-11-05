Filtered Method Index
====================

Methods filtered by: category 'I/O Operations'
Total matching methods: **92**

Matching Methods
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 15 35

   * - Method
     - Class
     - Return Type
     - Description
   * - :meth:`DefaultSearchNode.asPath`
     - :class:`DefaultSearchNode`
     - ``Path``
     - No description available
   * - :meth:`DefaultSearchNode.asPathReversed`
     - :class:`DefaultSearchNode`
     - ``Path``
     - No description available
   * - :meth:`DetectorUtils.assignToNearestPaths`
     - :class:`DetectorUtils`
     - ``List[Any]``
     - No description available
   * - :meth:`SpectralSimilarity.averageColorFromPaths`
     - :class:`SpectralSimilarity`
     - ``List[float]``
     - As ``` averageColorFromPaths(RandomAccessibleInterval, java.util.List, double, double, double) ``` , but also adding a...
   * - :meth:`PathAndFillManager.createFromFile`
     - :class:`PathAndFillManager`
     - ``PathAndFillManager``
     - Creates a PathAndFillManager instance from imported data
   * - :meth:`Path.createPath`
     - :class:`Path`
     - ``Path``
     - Returns a new Path with this Path's attributes (e.g. spatial scale), but no nodes.
   * - :meth:`PathAndFillManager.deletePath`
     - :class:`PathAndFillManager`
     - ``bool``
     - Deletes a path.
   * - :meth:`PathAndFillManager.deletePaths`
     - :class:`PathAndFillManager`
     - ``bool``
     - Delete paths by position.
   * - :meth:`SNT.deselectLastPath`
     - :class:`SNT`
     - ``Path``
     - Removes the most recently selected path from the current selection (so nothing remains selected if only one path was...
   * - :meth:`SNTPrefs.deselectedPathColor`
     - :class:`SNTPrefs`
     - ``Any``
     - No description available
   * - :meth:`SNTUtils.downloadToTempFile`
     - :class:`SNTUtils`
     - ``str``
     - Downloads a file from the specified URL to a temporary file
   * - :meth:`Path.drawPathAsPoints`
     - :class:`Path`
     - ``None``
     - No description available
   * - :meth:`PathAndFillManager.exportAllPathsAsSWC`
     - :class:`PathAndFillManager`
     - ``bool``
     - No description available
   * - :meth:`PathAndFillManager.exportFillsAsCSV`
     - :class:`PathAndFillManager`
     - ``None``
     - Export fills as CSV.
   * - :meth:`PathAndFillManager.exportToCSV`
     - :class:`PathAndFillManager`
     - ``None``
     - Output some potentially useful information about all the Paths managed by this instance as a CSV (comma separated...
   * - :meth:`PathAndFillManager.exportTree`
     - :class:`PathAndFillManager`
     - ``bool``
     - No description available
   * - :meth:`PathManagerUI.extractTagsFromPath`
     - :class:`PathManagerUI`
     - ``str``
     - No description available
   * - :meth:`PathManagerUI.extractTagsFromPaths`
     - :class:`PathManagerUI`
     - ``Set[Any]``
     - No description available
   * - :meth:`SNTUtils.fileAvailable`
     - :class:`SNTUtils`
     - ``bool``
     - No description available
   * - :meth:`TreeUtils.findPathsNeedingReversal`
     - :class:`TreeUtils`
     - ``List[Any]``
     - Determines which paths need to be reversed so that their start nodes point toward a given root location. A path should...
   * - :meth:`SNTTable.fromFile`
     - :class:`SNTTable`
     - ``SNTTable``
     - Script-friendly method for loading tabular data from a file/URL.
   * - :meth:`ShollTable.fromFile`
     - :class:`ShollTable`
     - ``SNTTable``
     - No description available
   * - :meth:`Tree.fromFile`
     - :class:`Tree`
     - ``Tree``
     - Script-friendly method for loading a Tree from a reconstruction file.
   * - :meth:`AutoTraceConfig.fromPaths`
     - :class:`AutoTraceConfig`
     - ``AutoTraceConfig``
     - No description available
   * - :meth:`PathManagerUI.geSelectedPathsAsTree`
     - :class:`PathManagerUI`
     - ``Tree``
     - Gets the collection of paths listed in the Path Manager as a `Tree` object. All paths are retrieved if none are...
   * - :meth:`DelineationsManager.importFromLabelImage`
     - :class:`DelineationsManager`
     - ``int``
     - Convenience overload accepting an `ImagePlus`, which is converted to an `ImgPlus` via `ImpUtils.toImgPlus3D(ImagePlus,...
   * - :meth:`PathAndFillManager.importNeurons`
     - :class:`PathAndFillManager`
     - ``Dict[str, Any]``
     - Import neuron(s) as a collection of reconstruction nodes (SWC points)
   * - :meth:`PathAndFillManager.importSWC`
     - :class:`PathAndFillManager`
     - ``bool``
     - Imports an SWC file using advanced options.
   * - :meth:`PathAndFillManager.importSWCs`
     - :class:`PathAndFillManager`
     - ``List[Any]``
     - Imports a group of SWC files (Remote URLs supported).
   * - :meth:`SNT.initPathsToFill`
     - :class:`SNT`
     - ``None``
     - No description available
   * - :meth:`PlausibilityCalibrator.listCurationFiles`
     - :class:`PlausibilityCalibrator`
     - ``List[str]``
     - No description available
   * - :meth:`Tree.listFromFile`
     - :class:`Tree`
     - ``List[Any]``
     - Retrieves a list of `Tree`s from a single file.
   * - :meth:`ShollTable.listProfileEntries`
     - :class:`ShollTable`
     - ``None``
     - No description available
   * - :meth:`PlausibilityCalibrator.loadBuiltIn`
     - :class:`PlausibilityCalibrator`
     - ``None``
     - No description available
   * - :meth:`SeedOverlay.loadCsv`
     - :class:`SeedOverlay`
     - ``Any``
     - No description available
   * - :meth:`SNTService.loadGraph`
     - :class:`SNTService`
     - ``None``
     - No description available
   * - :meth:`PathAndFillManager.loadGuessingType`
     - :class:`PathAndFillManager`
     - ``bool``
     - No description available
   * - :meth:`SNT.loadLabelsFile`
     - :class:`SNT`
     - ``None``
     - No description available
   * - :meth:`Viewer3D.loadMesh`
     - :class:`Viewer3D`
     - ``OBJMesh``
     - Loads a Wavefront .OBJ file. Files should be loaded _before_ displaying the scene, otherwise, if the scene is already...
   * - :meth:`Viewer3D.loadRefBrain`
     - :class:`Viewer3D`
     - ``OBJMesh``
     - Loads the surface mesh of a supported reference brain/neuropil. Internet connection may be required.
   * - :meth:`SNT.loadSecondaryImage`
     - :class:`SNT`
     - ``None``
     - No description available
   * - :meth:`SNT.loadTracings`
     - :class:`SNT`
     - ``bool``
     - No description available
   * - :meth:`SNTService.loadTracings`
     - :class:`SNTService`
     - ``None``
     - Loads the specified tracings file.
   * - :meth:`SNTService.loadTree`
     - :class:`SNTService`
     - ``None``
     - Loads the specified tree. Note that if SNT has not been properly initialized, spatial calibration mismatches may occur....
   * - :meth:`SNTService.loadTrees`
     - :class:`SNTService`
     - ``None``
     - Loads the specified collection of trees.
   * - :meth:`SNT.makePathVolume`
     - :class:`SNT`
     - ``Any``
     - Rasterizes centerline of paths into an ImagePlus
   * - :meth:`TreeUtils.mergeContinuousPaths`
     - :class:`TreeUtils`
     - ``int``
     - Merges paths that continue along the same trajectory at branch points, reducing fragmentation in auto-traced...
   * - :meth:`TreeUtils.mergePaths`
     - :class:`TreeUtils`
     - ``Path``
     - Merges a list of paths into a single path by appending nodes sequentially. The paths should be pre-ordered and oriented...
   * - :meth:`PathAndFillManager.nearestNodeOnPaths`
     - :class:`PathAndFillManager`
     - ``Any``
     - Finds the node nearest to a position, across the given paths as they are (no fitted/unfitted resolution: see...
   * - :meth:`PathAndFillManager.nearestPointOnAnyPath`
     - :class:`PathAndFillManager`
     - ``Any``
     - No description available
   * - :meth:`SNT.notifyEditingPathChanged`
     - :class:`SNT`
     - ``None``
     - Refreshes the Bdv/Bvv rendering of the path being edited after it was modified by the tracing canvas. Throttled so that...
   * - :meth:`PlausibilityMonitor.onPathFinalized`
     - :class:`PlausibilityMonitor`
     - ``List[Any]``
     - No description available
   * - :meth:`Bdv.onSntEditedPathModified`
     - :class:`Bdv`
     - ``None``
     - No description available
   * - :meth:`Bvv.onSntEditedPathModified`
     - :class:`Bvv`
     - ``None``
     - No description available
   * - :meth:`Bdv.onSntEditingPathChanged`
     - :class:`Bdv`
     - ``None``
     - No description available
   * - :meth:`Bvv.onSntEditingPathChanged`
     - :class:`Bvv`
     - ``None``
     - No description available
   * - :meth:`TreeUtils.orientPathsForMerging`
     - :class:`TreeUtils`
     - ``None``
     - Orients paths in a chain so they can be merged end-to-start. After this operation, each path's end node will be near...
   * - :meth:`TreeUtils.orientPathsTowardRoot`
     - :class:`TreeUtils`
     - ``int``
     - Orients paths so their start nodes point toward a given root location. Paths are reversed in-place if their end node is...
   * - :meth:`PathAndFillManager.pathChanged`
     - :class:`PathAndFillManager`
     - ``None``
     - No description available
   * - :meth:`Bdv.playPaths`
     - :class:`Bdv`
     - ``Any``
     - No description available
   * - :meth:`Bvv.playPaths`
     - :class:`Bvv`
     - ``Any``
     - No description available
   * - :meth:`SNTUtils.randomPaths`
     - :class:`SNTUtils`
     - ``List[Any]``
     - Generates a list of random paths. Only useful for debugging purposes
   * - :meth:`TreeToRaster.rasterizePathLabels`
     - :class:`TreeToRaster`
     - ``Any``
     - Rasterizes the tree into a 16-bit label image where each voxel is assigned the 1-based index of the `Path` that owns it...
   * - :meth:`AStarRefiner.readPreferences`
     - :class:`AStarRefiner`
     - ``None``
     - No-op: kept for consistency with `PathFitter`/`MultiSpectralRefiner`, which read persisted preferences here. A*...
   * - :meth:`MultiSpectralRefiner.readPreferences`
     - :class:`MultiSpectralRefiner`
     - ``None``
     - Reads stored preferences from `MultiSpectralRefinerCmd` and applies them to this refiner. If auto-intensity is enabled...
   * - :meth:`PathFitter.readPreferences`
     - :class:`PathFitter`
     - ``None``
     - No description available
   * - :meth:`PathManagerUI.refreshForPaths`
     - :class:`PathManagerUI`
     - ``None``
     - Repaints the Path Manager view for the given paths. Public hook used by external mutators (e.g. the Curation...
   * - :meth:`PathAndFillManager.repairPhantomFittedPaths`
     - :class:`PathAndFillManager`
     - ``int``
     - Repairs the paths returned by `getPhantomFittedPaths()` into ordinary, standalone paths: assigns each a fresh, valid...
   * - :meth:`SomaUtils.roiToSomaPath`
     - :class:`SomaUtils`
     - ``Path``
     - No description available
   * - :meth:`CrossSectionUtils.sampleProfile`
     - :class:`CrossSectionUtils`
     - ``List[float]``
     - Samples a 1D intensity profile along a direction vector, centered on a given world position. Intended for 2D images...
   * - :meth:`SNTUtils.sanitizeFilename`
     - :class:`SNTUtils`
     - ``str``
     - Replaces characters that are unsafe/reserved in filenames with an underscore, leaving alphanumerics, dots, and hyphens...
   * - :meth:`SeedOverlay.saveAs`
     - :class:`SeedOverlay`
     - ``None``
     - No description available
   * - :meth:`MouseLightLoader.saveAsJSON`
     - :class:`MouseLightLoader`
     - ``bool``
     - Convenience method to save JSON data to a local directory.
   * - :meth:`ImgUtils.saveAsOmeZarr`
     - :class:`ImgUtils`
     - ``None``
     - Writes an image as a multiscale OME-Zarr (OME-NGFF v0.5, Zarr v3) directory. Level 0 is streamed from `img` one slab of...
   * - :meth:`SNTChart.saveAsPDF`
     - :class:`SNTChart`
     - ``None``
     - No description available
   * - :meth:`SNTChart.saveAsPNG`
     - :class:`SNTChart`
     - ``None``
     - No description available
   * - :meth:`SNTChart.saveAsSVG`
     - :class:`SNTChart`
     - ``None``
     - No description available
   * - :meth:`MouseLightLoader.saveAsSWC`
     - :class:`MouseLightLoader`
     - ``bool``
     - Convenience method to save SWC data to a local directory.
   * - :meth:`Tree.saveAsSWC`
     - :class:`Tree`
     - ``bool``
     - Saves this Tree to an SWC file.
   * - :meth:`Viewer3D.saveScene`
     - :class:`Viewer3D`
     - ``int``
     - Saves the contents of the scene to a directory: reconstructions as `.traces` files and meshes as `.obj` files (with a...
   * - :meth:`ShollTable.saveSilently`
     - :class:`ShollTable`
     - ``bool``
     - No description available
   * - :meth:`Bvv.saveSnapshot`
     - :class:`Bvv`
     - ``bool``
     - Saves a snapshot of current scene as a PNG image to the specified path.
   * - :meth:`Viewer3D.saveSnapshot`
     - :class:`Viewer3D`
     - ``bool``
     - No description available
   * - :meth:`SNT.selectPath`
     - :class:`SNT`
     - ``None``
     - No description available
   * - :meth:`SNTPrefs.selectedPathColor`
     - :class:`SNTPrefs`
     - ``Any``
     - No description available
   * - :meth:`TreeUtils.splitByPrimaryPaths`
     - :class:`TreeUtils`
     - ``List[Any]``
     - Splits a tree with multiple primary paths into separate trees, one rooted at each primary path.
   * - :meth:`Bdv.syncPathManagerList`
     - :class:`Bdv`
     - ``bool``
     - No description available
   * - :meth:`Bvv.syncPathManagerList`
     - :class:`Bvv`
     - ``bool``
     - No description available
   * - :meth:`Viewer3D.syncPathManagerList`
     - :class:`Viewer3D`
     - ``bool``
     - (Re)loads the current list of Paths in the Path Manager list.
   * - :meth:`PathAndFillManager.transformPaths`
     - :class:`PathAndFillManager`
     - ``PathAndFillManager``
     - No description available
   * - :meth:`Fill.writeNodesXML`
     - :class:`Fill`
     - ``None``
     - No description available
   * - :meth:`Fill.writeXML`
     - :class:`Fill`
     - ``None``
     - No description available

----

*Filtered index generated on 2026-11-05 07:43:37*