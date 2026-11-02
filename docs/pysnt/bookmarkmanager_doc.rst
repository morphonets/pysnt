
``BookmarkManager`` Class Documentation
====================================


.. toctree::
   :maxdepth: 3
   :caption: Complete API Reference
   :hidden:

   ../api_auto/index
   ../api_auto/pysnt
   ../api_auto/pysnt.analysis
   ../api_auto/pysnt.analysis.graph
   ../api_auto/pysnt.analysis.growth
   ../api_auto/pysnt.analysis.sholl
   ../api_auto/pysnt.analysis.sholl.gui
   ../api_auto/pysnt.analysis.sholl.math
   ../api_auto/pysnt.analysis.sholl.parsers
   ../api_auto/pysnt.annotation
   ../api_auto/pysnt.converters
   ../api_auto/pysnt.converters.chart_converters
   ../api_auto/pysnt.converters.core
   ../api_auto/pysnt.converters.enhancement
   ../api_auto/pysnt.converters.extractors
   ../api_auto/pysnt.converters.graph_converters
   ../api_auto/pysnt.converters.structured_data_converters
   ../api_auto/pysnt.core
   ../api_auto/pysnt.display
   ../api_auto/pysnt.display.core
   ../api_auto/pysnt.display.data_display
   ../api_auto/pysnt.display.utils
   ../api_auto/pysnt.display.visual_display
   ../api_auto/pysnt.gui
   ../api_auto/pysnt.gui.cmds
   ../api_auto/pysnt.io
   ../api_auto/pysnt.tracing
   ../api_auto/pysnt.tracing.artist
   ../api_auto/pysnt.tracing.cost
   ../api_auto/pysnt.tracing.heuristic
   ../api_auto/pysnt.tracing.image
   ../api_auto/pysnt.util
   ../api_auto/pysnt.viewer
   ../api_auto/pysnt.common_module
   ../api_auto/pysnt.config
   ../api_auto/pysnt.gui_utils
   ../api_auto/pysnt.java_utils
   ../api_auto/pysnt.setup_utils
   ../api_auto/method_index
   ../api_auto/class_index
   ../api_auto/constants_index


**Package:** ``sc.fiji.snt``

Implements the *Bookmark Manager* pane.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearSelection()

   Clears the selection of bookmarks in the table. Does nothing if no selection exists.


.. py:method:: reset()

   Clears all bookmarks.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCount()

   Returns the number of bookmarks.


.. py:method:: getLastPosition()

   Returns the position of the most recently added bookmark/marker, in spatially calibrated ("world") coordinates (canonical storage format).

   In viewer mode (BVV/BDV), this is the last marker placed with the ``M`` key (or added programmatically). In SNT-UI mode, this is the last entry added to the Bookmark Manager pane. Since new entries are always appended, this reflects placement order in the common case; it can become stale relative to placement order after an explicit list-reordering operation (e.g. the table's "Sort by Distance..." menu, or a Merge/Colocalize operation, both of which re-write the backing list).


.. py:method:: getPixelPositions(boolean)

   Returns bookmark/marker positions in **pixel/voxel** coordinates, converted from this manager's canonical world/calibrated storage via ``worldToPixel(Bookmark)``.


.. py:method:: getPositions(boolean)

   Returns bookmark/marker positions in spatially calibrated (**"world"**) coordinates, i.e., this manager's canonical storage format, returned as-is (fresh copies) in both modes.


.. py:method:: getROIs(boolean)

   Returns a list of ROIs representing the bookmarks.


.. py:method:: getRois(String, List)

   Creates a list of `PointRoi`s from XYZCT locations with a color tag.


.. py:method:: getViewerDialogPanel()

   Returns the floating dialog for viewer mode, creating it on first call.


.. py:method:: hasBookmarks()

   Returns whether any bookmarks exist.


.. py:method:: isVisible()

   Returns whether this manager's markers are currently rendered in the big-viewer's shared ``AbstractBigViewer.AnnotationOverlay``, independently of the paths and seed-annotation layers.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setVisible(boolean)

   Shows or hides this manager's markers in the big-viewer overlay without touching the model itself (bookmarks are neither added nor removed), leaving every other owner's layer (paths, seed annotations) untouched. Mirrors ``SeedOverlay.isVisible()``'s role for ``SeedOverlayBigViewerHandler``.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: addViewerToolbarButton(JComponent)

   Adds a component to the viewer toolbar section of this panel. The component is appended after a separator the first time this method is called. Viewer subclasses use this to inject context-specific controls (e.g. a slab-clip toggle).


.. py:method:: showPanel()

   Shows the marker panel, bringing it to front if already visible.


.. py:method:: toggleViewerPanel()

   Shows or hides this marker manager's UI: redirects to SNTUI's "Bookmarks" tab whenever when SNTUI is present (e.g., in stream mode, see ``insideSNTUI()``), otherwise toggles the floating viewer dialog.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: load(File)

   


.. py:method:: save(File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(Map, String)

   Adds multiple bookmarks from selected path nodes


.. py:method:: dispose()

   Should be called when the panel is removed from the UI.


.. py:method:: remove(Path, int)

   


.. py:method:: resyncOverlay()

   Re-pushes all markers onto the viewer's shared ``AbstractBigViewer.AnnotationOverlay``. A no-op in SNT-UI mode (``viewer == null``). Meant to be called by ``Bvv``/``Bdv`` right after (re)creating that overlay, so markers added while ``syncViewerOverlay()`` was still no-op-ing on a null ``AbstractBigViewer.annotations()`` (i.e. before the viewer window existed) get rendered instead of silently staying buffered in the model.


.. py:method:: toOverlay(Overlay)

   Adds the bookmark ROIs to the specified overlay. If no bookmarks are selected, all bookmarks are added, otherwise only the selected bookmarks are added.


.. py:method:: toRoiManager()

   Adds the bookmarks to the ROI Manager. If no bookmarks are selected, all bookmarks are added, otherwise only the selected bookmarks are added.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.BookmarkManager>`_
* `BookmarkManager JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/BookmarkManager.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
