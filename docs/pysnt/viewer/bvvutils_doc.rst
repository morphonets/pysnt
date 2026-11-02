
``BvvUtils`` Class Documentation
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


**Package:** ``sc.fiji.snt.viewer``

Package-private utility methods shared across BVV-related classes (``Bvv``, ``ChannelUnmixingCard``, etc.).


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clearCaches()

   Releases the in-memory cell caches of all streamed (N5/Zarr/IMS) sources shown in BVV. Open viewers keep working: tiles are simply reloaded on demand. The GPU tile cache is not affected (it is freed when its window closes)


.. py:method:: estimateLocalCopyBytes(Source)

   Estimates the heap needed to copy level 0 of ``source`` into memory (see ``synthesizeMipmapPyramid(bdv.viewer.Source<T>, int, boolean)``)


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCachePrefMB()

   


.. py:method:: getFetchersPref()

   


.. py:method:: getRenderQuality()

   


.. py:method:: isCachePromptSuppressed()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setCachePrefMB(int)

   Persists the GPU tile cache preference (MB). 0 means automatic. Applies next time a BVV window is opened


.. py:method:: setCachePromptSuppressed(boolean)

   


.. py:method:: setFetchersPref(int)

   Persists the tile fetcher thread preference. 0 means automatic. Applies when a dataset is next opened


.. py:method:: setRenderQuality(RenderQuality)

   


.. py:method:: setSessionCacheMB(int)

   Overrides the preference for the current session only (0 clears the override)


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: prefetchForShow(Source, int)

   As ``prefetchForShow(Source, int)``, reporting progress as the data is fetched


.. py:method:: syncQueuesWithViewer(BvvHandle)

   Registers all tracked fetch queues with the cache controls of ``handle``, so that BVV advances them on every new frame (see ``CacheControl.prepareNextFrame()``). Idempotent. Opt out with ``-Dsnt.bvv.noQueueSync=true``


Other Methods
~~~~~~~~~~~~~


.. py:method:: buildTiledPyramid(ImgPlus, int)

   Builds one pyramid-backed ``Source`` per channel of an in-memory image, such that BVV renders it with its tile-streaming path (``MultiResolutionStack3D``) instead of uploading the whole volume as a single 3D texture, which is capped by ``GL_MAX_3D_TEXTURE_SIZE``. Level 0 and every coarser level is copied into its own ``CellImg``, because BVV only streams sources backed by cell images. Level 0 is copied in memory (see ``ImgUtils.materializeTiled(net.imglib2.RandomAccessibleInterval<T>, int)``), which costs the full volume in heap (see ``estimateTiledPyramidBytes(net.imagej.ImgPlus<?>)``). Coarser levels (step 2, 4, 8...) are averaged from the previous level (see ``averagedLevel(net.imglib2.RandomAccessibleInterval<T>)``) and computed lazily, on demand

   Meant for view-only sessions: the returned sources are independent copies, so an image also held for tracing would be stored twice


.. py:method:: effectiveCacheMB(int, boolean)

   


.. py:method:: ensureCellBacked(SourceAndConverter)

   As ``ensureCellBacked(SourceAndConverter)``, sizing the cells after the chunks of the underlying data


.. py:method:: estimateTiledPyramidBytes(ImgPlus)

   Estimates the heap needed by ``buildTiledPyramid(net.imagej.ImgPlus<T>, int)``: the full XYZ volume of every channel, plus ~15% for the coarser levels. Doubled if ``img`` is not lazily loaded, since it stays in memory during the copy


.. py:method:: fetcherThreads(boolean)

   


.. py:method:: maxCacheMB()

   


.. py:method:: preferMultiResolutionIfSafe(Source, int)

   Forces BVV to render ``source`` with its pyramid-aware, block-streaming path (``bvv.core.multires.MultiResolutionStack3D``) instead of the naive single-texture path (``bvv.core.multires.SimpleStack3D``), when it is safe to do so.

   BVV auto-detects which path to use (``bvv.core.multires.SourceStacks#inferSourceStackType``): it only picks the multi-resolution path when ``source``'s pixel type is ``TileAccess``-supported AND ``source.getSource(timepoint, 0)`` is (or wraps, via ``VolatileView``) an ``AbstractCellImg``. Many BDV/N5 source builders wrap their levels in a plain ``Views``-based interval (not an ``AbstractCellImg``), which makes BVV fall back to ``SimpleStack3D`` even for a genuinely multi-resolution, remote source. ``SimpleStack3D`` uploads the entire full-resolution volume as one texture on first paint, fetching all of it synchronously

   This mirrors BVV's own ``inferSourceStackType`` check before overriding it, so it never forces multi-resolution rendering on a source that would actually fail it (which would throw ``UnsupportedOperationException`` from ``TileAccess.create`` on the render thread). If the check fails, this method does nothing and BVV falls back to its own (slower) default


.. py:method:: recommendedCacheMB(int)

   


.. py:method:: releaseSources(Collection)

   Releases the in-memory cell caches of the given sources (those not backed by ``BvvUtils.CellBackedSource`` are ignored) and forgets them. Meant for when the viewer showing them is disposed. The pinned-heap budget they hold is returned right away. That of levels not owned by a source (synthesized or tiled pyramids) is returned once they are garbage-collected


.. py:method:: reportChunking(String, int[])

   Logs how the cells streamed to BVV relate to the source chunks and, if the chunk layout is poorly suited to interactive 3D viewing, queues a notice for the notification center. Does nothing if the chunk shape is unknown


.. py:method:: synthesizeMipmapPyramid(Source, int, boolean)

   Wraps a single-resolution ``Source`` in a synthetic mipmap pyramid. BVV's ``VolumeRenderer`` requires multiple resolution levels to pick a LOD; without one it throws on every repaint. Use this for non-pyramidal N5/Zarr sources that cannot be re-exported with a real pyramid.

   Level 0 is either a local, cell-based copy of the source (see ``ImgUtils.materializeTiled(net.imglib2.RandomAccessibleInterval<T>, int)``), or, if ``copyLocally`` is false, the source itself (as a zero-min view: a non-zero min of the source is moved into the returned source's transform, so its position in world space is unchanged). Each extra level doubles the previous step size along X/Y/Z, matching how a real N5/Zarr multiscale pyramid is laid out. Extra levels are averaged (2x2x2) from the previous level (see ``averagedLevel(net.imglib2.RandomAccessibleInterval<T>)``) and computed lazily, on demand, so they cost no heap up front


.. py:method:: trackQueue(CacheControl)

   Makes ``syncQueuesWithViewer(bvv.vistools.BvvHandle)`` aware of a fetch queue that feeds BVV


.. py:method:: warnIfLikelyRemoteImgPlus(ImgPlus, String)

   Diagnostic-only warning for the plain ``ImgPlus`` fallback path (see ``SpimDataUtils.resolvePathToSource(String)``). Unlike ``preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)``/ ``warnIfLikelySimpleStack(bdv.viewer.Source<?>, int)``, an ``ImgPlus`` always has a single mipmap level, so BVV always renders it via the non-pyramid-aware ``SimpleStack3D`` path regardless of pixel type or backing storage - there is no "is it structurally eligible for MULTIRESOLUTION" question to ask here the way there is for ``AbstractSpimData``/``N5Sources``.

   ``resolvePathToSource`` already knows this at resolution time - a remote ``ImgPlus`` is only ever produced by its own URL fallback branch (``ImgUtils.open(url)``) - so this simply carries that signal forward rather than trying to re-derive it by introspecting the RAI (which, for a lazily-opened remote image, may not even be a recognizable cache type)


.. py:method:: warnIfLikelySimpleStack(Source, int)

   Read-only counterpart to ``preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`` for ``AbstractSpimData`` sources (BDV-XML/HDF5, IMS): logs a warning if ``source`` looks likely to fall back to BVV's non-pyramid-aware ``SimpleStack3D`` renderer, without attempting to prevent it.

   Unlike the ``SpimDataUtils.N5Sources`` path, 


   ::

       BvvFunctions.show(AbstractSpimData,
       BvvOptions)


    builds its own ``Source`` instances internally (via ``BigDataViewer#initSetups``), so there is no hook to call ``preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`` on the actual instance before it first renders. ``inferSourceStackType``'s check is a pure function of the source's structural properties (pixel type, whether level 0 is an ``AbstractCellImg``), not of instance identity or any per-instance cached state, so running the same check here - on the ``Source`` SNT already has a handle to after ``show()`` returns - still gives an accurate answer; it just can't change the outcome

   This is diagnostic only: it neither prefetches nor forces a stack type, so it carries none of ``preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)``/``prefetchForShow(bdv.viewer.Source<T>, int)``'s risk of misbehaving on a source shape this hasn't been exercised against - it only makes a slow first paint traceable in the log after the fact, for whichever ``AbstractSpimData`` backend produced it


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.BvvUtils>`_
* `BvvUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/BvvUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
