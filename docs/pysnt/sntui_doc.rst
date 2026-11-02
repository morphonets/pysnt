
``SNTUI`` Class Documentation
==========================


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

Implements SNT's main dialog.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: resetUI()

   Full reset: closes any tethered ``Bvv``/``Bdv`` viewer (via ``closeBigViewers()``) and the current image, and clears all paths, restoring the UI to its initial, blank-canvas state. Intended for callers that need a guaranteed-fresh session regardless of whatever was open before.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getActiveBigViewer()

   Returns the ``AbstractBigViewer`` (BVV or BDV) currently tethered to this UI, in particular, Stream mode's own viewer or ``null`` if neither is open.


.. py:method:: getBookmarkManager()

   Gets the Bookmark Manager pane.


.. py:method:: getCommandFinder()

   Returns the command palette instance, so that other components can register their own entries into it.


.. py:method:: getCurationManager()

   Returns the Curation Manager (Curation Assistant).


.. py:method:: getDelineationsManager()

   Gets the Delineations Manager pane.


.. py:method:: getFillManager()

   Gets the Fill Manager dialog.


.. py:method:: getNotesPane()

   Gets the Bookmark Manager pane.


.. py:method:: getOpenBigViewers()

   


.. py:method:: getOrPromptForWorkspace()

   Returns the workspace directory, prompting user to create it if it doesn't exist.


.. py:method:: getPathManager()

   Gets the Path Manager dialog.


.. py:method:: getPlausibilityMonitor()

   Returns the plausibility monitor used by the Curation Manager (Curation Assistant).


.. py:method:: getPrefs()

   


.. py:method:: getReconstructionViewer(boolean)

   Gets the Reconstruction Viewer.


.. py:method:: getRecorder(boolean)

   


.. py:method:: getSciViewSNT(boolean)

   Gets the SciViewSNT instance.


.. py:method:: getState()

   Gets the current UI state.


.. py:method:: getTable()

   


.. py:method:: getTracingCanvas()

   


.. py:method:: getTracingCanvasPopupMenu()

   


.. py:method:: isOtherBigViewerEditing(AbstractBigViewer)

   


.. py:method:: isReady()

   Assesses whether the UI is blocked.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setBdv(Bdv)

   Registers (or clears, if ``bdv`` is null) the ``Bdv`` instance tethered to this UI.


.. py:method:: setBvv(Bvv)

   Registers (or clears, if ``bvv`` is null) the ``Bvv`` instance tethered to this UI.


.. py:method:: setEnableDebugMode(boolean)

   Enables/disables debug mode


.. py:method:: setLookAndFeel(String)

   


.. py:method:: setRenderingScale(double)

   Sets rendering scale of Paths as per respective widget in dialog.


.. py:method:: setSigmaPaletteListener(SigmaPaletteListener)

   


.. py:method:: setVisibilityFilter(String, boolean)

   Sets filters for visibility of paths, as per respective widget in dialog.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: closeBigViewers()

   Closes any tethered ``Bvv``/``Bdv`` viewer(s), if open. Unlike ``resetUI()``, this does not touch the loaded image or paths: closing a big-viewer *window* isn't data loss the way clearing paths is (the underlying ``PathAndFillManager`` is untouched), so this needs no confirmation and is safe to call unconditionally - e.g. from ``DemoRunner`` before loading a new demo, so a viewer left over from a previous one is never silently orphaned (see ``AbstractBigViewer``/``setBvvOnEDT``'s ``windowClosing`` handler for what "orphaned" means here).


.. py:method:: showMessage(String, String)

   


.. py:method:: showStatus(String, boolean)

   Updates the status bar.


Other Methods
~~~~~~~~~~~~~


.. py:method:: changeState(int)

   Changes this UI to a new state. Does nothing if ``newState`` is the current UI state


.. py:method:: close()

   Closes this SNT session, asking for confirmation only if there are unsaved paths or measurements


.. py:method:: error(String)

   Displays an error message.


.. py:method:: launchSigmaPaletteAround(int, int, int)

   Crops a small region around the given point and launches the ``SigmaPalette`` preview grid, exactly as if the user had clicked at that position on the classic-mode tracing canvas (see ``InteractiveTracerCanvas#startSigmaWizard``). Public (rather than the previous ``protected``) so it can also be triggered from a Bdv/Bvv viewer action, since there is no classic canvas to click on in Stream mode (see ``AbstractBigViewer.Actions#pickSigmaPointAction()``).


.. py:method:: launchSigmaPaletteAroundStreamed(int, int, int)

   Crop-independent counterpart of ``launchSigmaPaletteAround(int, int, int)``: sources its bounds from ``SNT.getFullSourceData()`` instead of ``SNT.getLoadedData()``, so a BDV/BVV click that lands outside a materialized crop's (smaller) bounds still previews the region actually clicked, instead of silently clamping to the crop's edge. See ``AbstractBigViewer.Actions#pickSigmaPointAction()``, which pairs this with ``SNT.getDefaultCanvasPixelOffset()`` to convert the click.


.. py:method:: pause(boolean)

   Pauses/Resume SNT (equivalent to command in image contextual menu).


.. py:method:: pauseTracing(boolean)

   Pauses/Resume tracing functions (equivalent to command in image contextual menu).


.. py:method:: refresh()

   Updates the dialog, including status bar and 'computation settings' widget.


.. py:method:: registerActiveCmdWorker(SwingWorker)

   Registers (or clears, if ``worker`` is ``null``) the ``SwingWorker`` currently executing a long-running ``CommonDynamicCmd``. Unlike commands launched via ``DynamicCmdRunner``, these keep running on their own background thread long after the initiating dialog has closed and ``currentState`` has reverted to whatever it was before the dialog opened, so they cannot rely on the switch inside ``abortCurrentOperation()``. Cancellation is not forcible: the running code must itself poll ``Thread.isInterrupted()`` (see ``AbstractGWDTTracer``'s hot loops) for this to have any effect.


.. py:method:: runAutotracingWizard()

   Launches the autotracing wizard for the active image.

   The tracer implementation is selected based on image type:

   - **Binary images** : ``BinaryTracerCmd`` (topology-based skeletonization)

   - **Grayscale images** : ``GWDTTracerCmd`` (intensity-weighted distance transform)


.. py:method:: runCommand(String)

   Runs a Scijava command associated with SNT.


.. py:method:: runSecondaryLayerWizard()

   Runs the 'secondary layer wizard' in the background, without displaying prompt.


.. py:method:: selectTab(String)

   Activates the specified tab.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNTUI>`_
* `SNTUI JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTUI.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
