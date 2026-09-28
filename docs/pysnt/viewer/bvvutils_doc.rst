
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

Package-private utility methods shared across BVV-related classes (Bvv, ChannelUnmixingCard, etc.).


Methods
-------


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static prefetchForShow(Source, int)

   Fetches and locally caches whichever mipmap level BVV will actually render first for source, by touching every pixel on the calling thread. Call `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` first so the stack type is already decided when this runs

SimpleStack3D always uploads level 0 (full resolution) as a single texture on first paint (see `bvv.core.render.DefaultSimpleStackManager`) so that upload is what must be warmed for it. `MultiResolutionStack3D` streams blocks progressively and never blocks the EDT regardless of what is cached, so warming its coarsest level here is only a courtesy (a faster first frame).

Call this on a background thread before bvv.show(...) so the EDT only ever sees already-cached data


Other Methods
~~~~~~~~~~~~~


.. py:method:: static preferMultiResolutionIfSafe(Source, int)

   Forces BVV to render source with its pyramid-aware, block-streaming path (`bvv.core.multires.MultiResolutionStack3D`) instead of the naive single-texture path (`bvv.core.multires.SimpleStack3D`), when it is safe to do so.

BVV auto-detects which path to use (`bvv.core.multires.SourceStacks#inferSourceStackType`): it only picks the multi-resolution path when source's pixel type is TileAccess-supported AND `source.getSource(timepoint, 0)` is (or wraps, via VolatileView) an AbstractCellImg. Many BDV/N5 source builders wrap their levels in a plain Views-based interval (not an AbstractCellImg), which makes BVV fall back to SimpleStack3D even for a genuinely multi-resolution, remote source. SimpleStack3D uploads the entire full-resolution volume as one texture on first paint, fetching all of it synchronously

This mirrors BVV's own inferSourceStackType check before overriding it, so it never forces multi-resolution rendering on a source that would actually fail it (which would throw `UnsupportedOperationException` from TileAccess.create on the render thread). If the check fails, this method does nothing and BVV falls back to its own (slower) default


.. py:method:: static synthesizeMipmapPyramid(Source, int)

   Wraps a single-resolution Source in a synthetic mipmap pyramid, built by materializing it locally (see `ImgUtils.materialize(net.imglib2.RandomAccessibleInterval<T>)`) and lazily subsampling that local copy. BVV's VolumeRenderer requires multiple resolution levels to pick a LOD; without one it throws on every repaint. Use this for non-pyramidal N5/Zarr sources that cannot be re-exported with a real pyramid.

Level 0 is the full-resolution, now-local copy; each extra level doubles the previous step size along X/Y/Z, matching how a real N5/Zarr multiscale pyramid is laid out


.. py:method:: static warnIfLikelyRemoteImgPlus(ImgPlus, String)

   Diagnostic-only warning for the plain ImgPlus fallback path (see `SpimDataUtils.resolvePathToSource(String)`). Unlike `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`/ `warnIfLikelySimpleStack(bdv.viewer.Source<?>, int)`, an ImgPlus always has a single mipmap level, so BVV always renders it via the non-pyramid-aware SimpleStack3D path regardless of pixel type or backing storage - there is no "is it structurally eligible for MULTIRESOLUTION" question to ask here the way there is for AbstractSpimData/N5Sources.

resolvePathToSource already knows this at resolution time - a remote ImgPlus is only ever produced by its own URL fallback branch (ImgUtils.open(url)) - so this simply carries that signal forward rather than trying to re-derive it by introspecting the RAI (which, for a lazily-opened remote image, may not even be a recognizable cache type)


.. py:method:: static warnIfLikelySimpleStack(Source, int)

   Read-only counterpart to `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` for AbstractSpimData sources (BDV-XML/HDF5, IMS): logs a warning if source looks likely to fall back to BVV's non-pyramid-aware SimpleStack3D renderer, without attempting to prevent it.

Unlike the `SpimDataUtils.N5Sources` path, 
```
BvvFunctions.show(AbstractSpimData,
 BvvOptions)
```
 builds its own Source instances internally (via `BigDataViewer#initSetups`), so there is no hook to call `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)` on the actual instance before it first renders. inferSourceStackType's check is a pure function of the source's structural properties (pixel type, whether level 0 is an AbstractCellImg), not of instance identity or any per-instance cached state, so running the same check here - on the Source SNT already has a handle to after `show()` returns - still gives an accurate answer; it just can't change the outcome

This is diagnostic only: it neither prefetches nor forces a stack type, so it carries none of `preferMultiResolutionIfSafe(bdv.viewer.Source<?>, int)`/`prefetchForShow(bdv.viewer.Source<T>, int)`'s risk of misbehaving on a source shape this hasn't been exercised against - it only makes a slow first paint traceable in the log after the fact, for whichever AbstractSpimData backend produced it


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.BvvUtils>`_
* `BvvUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/BvvUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
