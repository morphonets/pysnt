Filtered Method Index
====================

Methods filtered by: category 'I/O Operations'
Total matching methods: **32**

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
     - ``bool``
     - Delete paths by position.
   * - :meth:`Path.drawPathAsPoints`
     - :class:`Path`
     - ``None``
     - No description available
   * - :meth:`PathAndFillManager.exportAllPathsAsSWC`
     - :class:`PathAndFillManager`
     - ``bool``
     - Exports all as Paths as SWC file(s). Multiple files are created if multiple Trees exist.
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
   * - :meth:`SNTUtils.static randomPaths`
     - :class:`SNTUtils`
     - ``List[Any]``
     - Generates a list of random paths. Only useful for debugging purposes
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

*Filtered index generated on 2025-11-13 22:40:29*