
``SNTPrefs`` Class Documentation
=============================


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

Class handling SNT preferences.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearAll()

   


.. py:method:: clearBvvPrefs()

   Restores the defaults of all BVV preferences


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: get(String, String)

   Gets a string preference value.


.. py:method:: getAutoLoadToolbarButton()

   Gets whether the SNT button is auto-installed in the IJ toolbar at Fiji startup.


.. py:method:: getAutoSelectionOfFinishedPath()

   


.. py:method:: getAutosaveFile()

   


.. py:method:: getBackupDir()

   Returns the backup directory, or null if workspace doesn't exist. Does NOT create directories.


.. py:method:: getBigViewerPickRadius()

   


.. py:method:: getBoolean(String, boolean)

   Gets a boolean preference value.


.. py:method:: getBvvCacheMB()

   


.. py:method:: getBvvFetchers()

   


.. py:method:: getBvvMaxStep()

   


.. py:method:: getBvvRenderQuality()

   


.. py:method:: getDefaultLookAndFeel()

   


.. py:method:: getDisplayCustomPathColors()

   


.. py:method:: getLookAndFeel()

   Gets the current look and feel preference.


.. py:method:: getNextImgExtensions()

   Returns the list of filename suffixes used to identify images when navigating to the next/previous image in a folder (see ``SNTUI``). Matching is case-insensitive and applied to the end of the filename (i.e., ``endsWith``). Suffixes may include a leading dot (e.g., ``".tif"``) or a partial filename suffix (e.g., ``"_max.tif"``).


.. py:method:: getPref(int)

   


.. py:method:: getRecentDir()

   


.. py:method:: getRequireShiftToFork()

   


.. py:method:: getSessionsDir()

   Returns the sessions directory, or null if workspace doesn't exist. Does NOT create directories.


.. py:method:: getTemp(String, String)

   Gets a temporary string preference value that will be cleared at session end.


.. py:method:: getThreads()

   Gets the current number of threads setting.


.. py:method:: getUseNativeFileChooser()

   Gets whether SNT's open/save dialogs should use the OS native file dialogs (FlatLaf's ``SystemFileChooser``) instead of SNT's own ``FileChooser``.


.. py:method:: getWorkspaceDir()

   


.. py:method:: is2DDisplayCanvas()

   Checks if 2D display canvas is forced.


.. py:method:: isBvvCachePromptSuppressed()

   


.. py:method:: isCanvasAutoActivationEnabled()

   


.. py:method:: isFastCropMaterializationEnabled()

   


.. py:method:: isSaveCompressedTraces()

   Checks if traces should be saved in compressed format.


.. py:method:: isSaveWinLocations()

   Checks if window locations should be saved and restored.


.. py:method:: isScrollDiameterEnabled()

   


.. py:method:: isSomaDisplayTriangle()

   Sets whether single-node paths tagged as are rendered w/ triangular shape.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: set(String, String)

   Sets a boolean preference value.


.. py:method:: set2DDisplayCanvas(boolean)

   Sets whether to force 2D display canvas.


.. py:method:: setAutoLoadToolbarButton(boolean)

   Sets whether the SNT button should be auto-installed in the IJ toolbar at Fiji startup.


.. py:method:: setAutoSelectionOfFinishedPath(boolean)

   


.. py:method:: setAutosaveFile(File)

   


.. py:method:: setBvvCacheMB(int)

   


.. py:method:: setBvvCachePromptSuppressed(boolean)

   


.. py:method:: setBvvFetchers(int)

   


.. py:method:: setBvvMaxStep(double)

   


.. py:method:: setBvvRenderQuality(String)

   


.. py:method:: setCanvasAutoActivation(boolean)

   


.. py:method:: setDeselectedPathColor(Color)

   


.. py:method:: setDisplayCustomPathColors(boolean)

   


.. py:method:: setFastCropMaterialization(boolean)

   


.. py:method:: setLastKnownDir(File)

   


.. py:method:: setLookAndFeel(String)

   Sets the look and feel preference.


.. py:method:: setNextImgExtensions(List)

   Convenience method for setting filename suffixes from a comma-separated string. Whitespace around entries is trimmed and blank entries are ignored. Delegates to ``setNextImgExtensions(List)``.


.. py:method:: setRecentDir(File)

   


.. py:method:: setRequireShiftToFork(boolean)

   


.. py:method:: setSaveCompressedTraces(boolean)

   Sets whether to save traces in compressed format.


.. py:method:: setSaveWinLocations(boolean)

   Sets whether window locations should be saved and restored.


.. py:method:: setScrollDiameterEnabled(boolean)

   


.. py:method:: setSelectedPathColor(Color)

   


.. py:method:: setSomaDisplayTriangle(boolean)

   Sets whether single-node paths tagged as soma should render w/ triangular shape.


.. py:method:: setTemp(String, String)

   Sets a temporary string preference value that will be cleared at session end.


.. py:method:: setThreads(int)

   Sets the number of threads to use for multi-threaded operations.


.. py:method:: setUseNativeFileChooser(boolean)

   Sets whether SNT's simple open/save dialogs should use native OS file dialogs.


.. py:method:: setWorkspaceDir(File)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: deselectedPathColor()

   


.. py:method:: ensureWorkspaceExists()

   Creates workspace directory if it doesn't exist.


.. py:method:: firstRun()

   Checks if SNT has ever been run before on this system, consuming the check in the process: the very first call ever made to this method returns ``true``; every call after that returns ``false``.


.. py:method:: firstRunAfterUpdate()

   Checks if this is the first run after an SNT update.


.. py:method:: lastKnownDir()

   


.. py:method:: selectedPathColor()

   


.. py:method:: workspaceIsValid()

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNTPrefs>`_
* `SNTPrefs JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTPrefs.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
