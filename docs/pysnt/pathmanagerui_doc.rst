
``PathManagerUI`` Class Documentation
==================================


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

Implements the *Path Manager* Dialog.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearSelection()

   Clears the current path selection.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getFilteringToolBar()

   


.. py:method:: getJTree()

   Gets the JTree component used to display paths.


.. py:method:: getNavigationToolBar()

   


.. py:method:: getPathAndFillManager()

   Gets the PathAndFillManager instance.


.. py:method:: getProofReadingToolBar()

   


.. py:method:: getSNT()

   Gets the SNT instance associated with this Path Manager.


.. py:method:: getSearchable()

   Gets the Searchable interface for the JTree.


.. py:method:: getSelectedPaths(boolean)

   Gets the paths currently selected in the Manager's ``JTree`` list.


.. py:method:: getSelectedPathsOrganizedByTrees(boolean)

   Gets the paths currently selected in the Manager's ``JTree`` list as `Tree`s.


.. py:method:: hasTags(Path)

   return true if the path name contains any tag delimiters ({ or [).


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setCombinedSelectionFilters(boolean)

   Sets whether selection filters should be combined. This is equivalent to toggling the 'filter' button in Path Manager's UI


.. py:method:: setFillList(List)

   


.. py:method:: setPathList(Path, boolean)

   


.. py:method:: setSelectedPaths(Collection, Object)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: applyDefaultTags(String[])

   Applies a default (built-in) tag to selected Path(s).


.. py:method:: applySelectionFilter(String)

   Selects paths matching a morphometric criteria.


.. py:method:: applyTag(String)

   Applies a custom tag/ color to selected Path(s).


.. py:method:: dispose()

   


.. py:method:: extractTagsFromPath(Path)

   


.. py:method:: extractTagsFromPaths(Collection)

   


.. py:method:: geSelectedPathsAsTree()

   Gets the collection of paths listed in the Path Manager as a ``Tree`` object. All paths are retrieved if none are currently selected.


.. py:method:: refreshForPaths(Collection)

   Repaints the Path Manager view for the given paths. Public hook used by external mutators (e.g. the Curation Assistant's review-tag actions in ``CurationManager``) that change path names directly and need the table to pick the change up; bypasses the heavier viewer-update pass because path mutations like tag-suffix edits don't affect 3D viewers.


.. py:method:: reload()

   Reloads the contents of ``PathAndFillManager``


.. py:method:: removeTags(Path)

   


.. py:method:: runCommand(String)

   Runs a menu command with options.


.. py:method:: select(Path)

   Selects a specific path in the Path Manager.


.. py:method:: selectAll()

   Selects all paths.


.. py:method:: update()

   Refreshes (Repaints) the Path Manager JTree.


.. py:method:: valueChanged(TreeSelectionEvent)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.PathManagerUI>`_
* `PathManagerUI JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathManagerUI.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
