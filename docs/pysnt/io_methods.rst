Filtered Method Index
====================

Methods filtered by: category 'I/O Operations'
Total matching methods: **43**

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
     - ``None``
     - Delete paths by position.
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
   * - :meth:`SNTService.loadGraph`
     - :class:`SNTService`
     - ``None``
     - No description available
   * - :meth:`Viewer3D.loadMesh`
     - :class:`Viewer3D`
     - ``Any``
     - Loads a Wavefront .OBJ file. Files should be loaded _before_ displaying the scene, otherwise, if the scene is already...
   * - :meth:`Viewer3D.loadRefBrain`
     - :class:`Viewer3D`
     - ``Any``
     - Loads the surface mesh of a supported reference brain/neuropil. Internet connection may be required.
   * - :meth:`SNTService.loadTracings`
     - :class:`SNTService`
     - ``None``
     - Loads the specified tracings file.
   * - :meth:`SNTService.loadTree`
     - :class:`SNTService`
     - ``None``
     - Loads the specified tree. Note that if SNT has not been properly initialized, spatial calibration mismatches may occur....
   * - :meth:`PathChangeListener.pathChanged`
     - :class:`PathChangeListener`
     - ``None``
     - No description available
   * - :meth:`TreeToRaster.rasterizePathLabels`
     - :class:`TreeToRaster`
     - ``Any``
     - Rasterizes the tree into a 16-bit label image where each voxel is assigned the 1-based index of the Path that owns it...
   * - :meth:`AStarRefiner.readPreferences`
     - :class:`AStarRefiner`
     - ``None``
     - No-op: kept for consistency with PathFitter/MultiSpectralRefiner, which read persisted preferences here. A* re-tracing...
   * - :meth:`PathFitter.readPreferences`
     - :class:`PathFitter`
     - ``None``
     - No description available
   * - :meth:`MouseLightLoader.saveAsJSON`
     - :class:`MouseLightLoader`
     - ``bool``
     - Convenience method to save JSON data to a local directory.
   * - :meth:`MouseLightLoader.saveAsSWC`
     - :class:`MouseLightLoader`
     - ``bool``
     - Convenience method to save SWC data to a local directory.
   * - :meth:`SpectralSimilarity.static averageColorFromPaths`
     - :class:`SpectralSimilarity`
     - ``Any``
     - As ``` averageColorFromPaths(RandomAccessibleInterval, java.util.List, double, double, double) ``` , but also adding a...
   * - :meth:`PathAndFillManager.static createFromFile`
     - :class:`PathAndFillManager`
     - ``Any``
     - Creates a PathAndFillManager instance from imported data
   * - :meth:`SNTUtils.static downloadToTempFile`
     - :class:`SNTUtils`
     - ``str``
     - Downloads a file from the specified URL to a temporary file
   * - :meth:`SNTUtils.static fileAvailable`
     - :class:`SNTUtils`
     - ``bool``
     - No description available
   * - :meth:`TreeUtils.static findPathsNeedingReversal`
     - :class:`TreeUtils`
     - ``List[Any]``
     - Determines which paths need to be reversed so that their start nodes point toward a given root location. A path should...
   * - :meth:`SNTTable.static fromFile`
     - :class:`SNTTable`
     - ``SNTTable``
     - Script-friendly method for loading tabular data from a file/URL.
   * - :meth:`Tree.static fromFile`
     - :class:`Tree`
     - ``Tree``
     - Script-friendly method for loading a Tree from a reconstruction file.
   * - :meth:`SNTUtils.static getReconstructionFiles`
     - :class:`SNTUtils`
     - ``Any``
     - Retrieves a list of reconstruction files stored in a common directory matching the specified criteria.
   * - :meth:`TreeUtils.static getRootPath`
     - :class:`TreeUtils`
     - ``Path``
     - Gets the root path of the tree containing the given path.
   * - :meth:`SNTUtils.static getUniquelySuffixedFile`
     - :class:`SNTUtils`
     - ``str``
     - No description available
   * - :meth:`SNTUtils.static getUniquelySuffixedTifFile`
     - :class:`SNTUtils`
     - ``str``
     - No description available
   * - :meth:`SNTUtils.static isReconstructionFile`
     - :class:`SNTUtils`
     - ``bool``
     - No description available
   * - :meth:`TreeUtils.static mergeContinuousPaths`
     - :class:`TreeUtils`
     - ``int``
     - Merges paths that continue along the same trajectory at branch points, reducing fragmentation in auto-traced...
   * - :meth:`TreeUtils.static mergePaths`
     - :class:`TreeUtils`
     - ``Path``
     - Merges a list of paths into a single path by appending nodes sequentially. The paths should be pre-ordered and oriented...
   * - :meth:`TreeUtils.static orientPathsForMerging`
     - :class:`TreeUtils`
     - ``None``
     - Orients paths in a chain so they can be merged end-to-start. After this operation, each path's end node will be near...
   * - :meth:`TreeUtils.static orientPathsTowardRoot`
     - :class:`TreeUtils`
     - ``int``
     - Orients paths so their start nodes point toward a given root location. Paths are reversed in-place if their end node is...
   * - :meth:`SNTUtils.static randomPaths`
     - :class:`SNTUtils`
     - ``List[Any]``
     - Generates a list of random paths. Only useful for debugging purposes
   * - :meth:`SNTUtils.static sanitizeFilename`
     - :class:`SNTUtils`
     - ``str``
     - Replaces characters that are unsafe/reserved in filenames with an underscore, leaving alphanumerics, dots, and hyphens...
   * - :meth:`TreeUtils.static splitByPrimaryPaths`
     - :class:`TreeUtils`
     - ``List[Any]``
     - Splits a tree with multiple primary paths into separate trees, one rooted at each primary path.
   * - :meth:`SciViewSNT.syncPathManagerList`
     - :class:`SciViewSNT`
     - ``bool``
     - (Re)loads the current list of Paths in the Path Manager list.
   * - :meth:`Fill.writeNodesXML`
     - :class:`Fill`
     - ``None``
     - No description available
   * - :meth:`Fill.writeXML`
     - :class:`Fill`
     - ``None``
     - No description available

----

*Filtered index generated on 2026-09-27 23:02:20*