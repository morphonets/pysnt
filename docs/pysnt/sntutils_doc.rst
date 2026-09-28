
``SNTUtils`` Class Documentation
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

Static utilities for SNT


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getBackupCopies(File, String)

   Returns all timestamped backup copies in the specified location. Convenience method that matches all traces files with timestamps.


.. py:method:: static getCacheDir()

   Returns SNT's own scratch/cache directory, used by disk-backed operations (e.g. `DiskBackedStorageBackend`, Lazy). Unlike the workspace directory (see `SNTPrefs#getWorkspaceDir()`), this directory holds only disposable, regenerable scratch data -- never anything a user created -- so it lives under the OS temp root.

Individual operations create their own uniquely-named subdirectory here and clean up after themselves once done. This parent directory itself is created lazily and left in place across sessions, so that (1) it is always at the same, discoverable path and (2) leftovers from a crashed session (which skipped its own cleanup) remain visible and removable.


.. py:method:: static getCacheDirSize()

   Computes the on-disk size of getCacheDir(). This walks the whole cache tree, so it can be slow once many files have accumulated; avoid calling this on the EDT


.. py:method:: static getContext()

   Convenience method to access the context of the running Fiji instance


.. py:method:: static getDecimalFormat(double, int)

   


.. py:method:: static getElapsedTime(long)

   


.. py:method:: static getHeapInfo()

   


.. py:method:: static getInstance()

   


.. py:method:: static getLastElement(String)

   Extracts the last path/URL element (typically a filename) from a file path, URL, or cloud-storage link, e.g., "/data/sample.n5" or `"https://host/a/b.zarr?x=1"` both yield "b.zarr"/"sample.n5". Handles Windows-style backslashes, trailing slashes, and URL query parameters/anchors.


.. py:method:: static getPluginInstance()

   


.. py:method:: static getReadableVersion()

   


.. py:method:: static getReconstructionFiles(File, String)

   Retrieves a list of reconstruction files stored in a common directory matching the specified criteria.


.. py:method:: static getSanitizedUnit(String)

   


.. py:method:: static getTimeStamp()

   


.. py:method:: static getUniquelySuffixedFile(File, String)

   


.. py:method:: static getUniquelySuffixedTifFile(File)

   


.. py:method:: static isContextSet()

   


.. py:method:: static isDebugMode()

   Assesses if SNT is running in debug mode


.. py:method:: static isReachable(String, int)

   Checks for whether url's host can be reached, meant to be called before a real download/stream attempt (e.g., `downloadToTempFile(java.lang.String)`) so that a missing network connection surfaces as one clear message. est-effort: only http(s) URLs are actually probed; any other scheme (e.g. a bare host-less URI) is assumed reachable, deferring to the real caller


.. py:method:: static isReconstructionFile(File)

   


.. py:method:: static isStandaloneContext()

   Returns whether the current context was self-initialized by SNT (i.e., no host application like ImageJ/Fiji provided one). This is useful for determining if it is safe to modify global UI state such as the Look and Feel.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: static setContext(Context)

   


.. py:method:: static setDebugMode(boolean)

   Enables/disables debug mode


.. py:method:: static setIsLoading(boolean, boolean)

   Shows or hides the loading splash screen. Calls nest safely: several independent call chains can be "loading" at once, so the splash only actually closes once every true has been balanced by a matching false, hence calls should be made in a try/finally block.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static addViewer(Viewer3D)

   


.. py:method:: static removeViewer(Viewer3D)

   


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static downloadToTempFile(String)

   Downloads a file from the specified URL to a temporary file


Other Methods
~~~~~~~~~~~~~


.. py:method:: static csvQuoteAndPrint(PrintWriter, Object)

   


.. py:method:: static downloadAndExtractZip(String)

   Downloads a zip archive from the specified URL and extracts it to a fresh temporary directory. Both the downloaded archive and the extracted contents are marked for deletion on JVM exit; the archive itself is also deleted immediately once extraction succeeds, since it is not needed afterward.


.. py:method:: static error(String, Throwable)

   As `error(String, Throwable)`, but allows suppressing the notification-center mirroring, e.g., when the caller has already surfaced the message to the user synchronously (a modal dialog)


.. py:method:: static extractReadableTimeStamp(File)

   


.. py:method:: static fileAvailable(File)

   


.. py:method:: static findClosestPair(File, String)

   


.. py:method:: static formatBytes(long)

   


.. py:method:: static formatDouble(double, int)

   


.. py:method:: static log(String)

   


.. py:method:: static nowTruncatedToSeconds()

   Returns the current date-time truncated to whole seconds, e.g., for stamping exported content with a generation time.


.. py:method:: static openRemoteStream(String)

   Opens an InputStream to url with explicit connect/read timeouts, so a stalled or unreachable remote host fails with a clear IOException instead of hanging indefinitely - the default behavior of URL.openStream(), whose underlying URLConnection has no timeout at all unless one is set explicitly. Used for remote reconstruction/marker/demo files (e.g. `https://.../autotracings.traces`), which are typically small enough that a single bounded connection (rather than `runWithTimeout(java.util.concurrent.Callable<T>, long, java.lang.String)`'s background-thread wrapper) is enough.


.. py:method:: static randomPaths()

   Generates a list of random paths. Only useful for debugging purposes


.. py:method:: static runWithTimeout(Callable, long, String)

   Runs task on a bounded background (daemon) thread, guarding against blocking I/O - typically remote N5/Zarr discovery, that can otherwise hang indefinitely on a stalled connection with no feedback to the user.

Unlike `openRemoteStream(String)` (a single bounded connection), this bounds the *entire* operation, however many network round-trips it internally makes.

On timeout, the background thread is best-effort interrupted via `ExecutorService.shutdownNow()`; if the underlying I/O call ignores interruption (common for plain socket reads), that thread may still leak until the stalled connection itself eventually times out or errors, but the calling thread is freed immediately to report the failure, rather than hanging alongside it.


.. py:method:: static sanitizeFilename(String)

   Replaces characters that are unsafe/reserved in filenames with an underscore, leaving alphanumerics, dots, and hyphens untouched.


.. py:method:: static startApp(boolean)

   Convenience method to start up SNT's GUI.


.. py:method:: static stripExtension(String)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SNTUtils>`_
* `SNTUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
