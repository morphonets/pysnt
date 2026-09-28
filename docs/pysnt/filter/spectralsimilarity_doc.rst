
``SpectralSimilarity`` Class Documentation
=======================================


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


**Package:** ``sc.fiji.snt.filter``

Computes a spectral similarity map from a multichannel (e.g., Brainbow) image. For each voxel, the output encodes how well the voxel's channel-intensity vector matches a reference color vector. The output is a scalar image suitable for use as a secondary tracing layer.

The per-voxel score combines two terms:

Cosine similarity: dot product of unit-normalized voxel and reference color vectors (1 = identical direction, 0 = orthogonal) Intensity factor: sigmoid falloff based on how much the voxel's total intensity deviates from the reference intensity. This prevents bright background or dim noise from producing high scores

The final output is `cosineSimilarity × intensityFactor`, scaled to [0, 1]. High values indicate voxels that match the target neuron's color and brightness.

The input image is a 4D (X, Y, Z, C) `RandomAccessibleInterval` where the last dimension is channels. The output is a 3D (X, Y, Z) scalar image.

This filter is designed for integration with SNT's secondary layer tracing infrastructure, where any standard cost function (e.g., Reciprocal) applied to the output produces spectrally-aware path searches.

The color-vector approach to neurite identification in multichannel images is also validated in:

Leiwe et al., "Automated neuronal reconstruction with super-multicolour Tetbow labelling and threshold-based clustering of colour hues", Nat Commun 15, 5279 (2024). doi:10.1038/s41467-024-49455-y


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getArity()

   


.. py:method:: getIndependentInstance()

   


.. py:method:: getReferenceColor()

   Returns the reference color vector used by this filter.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setEnvironment(OpEnvironment)

   


.. py:method:: setInput(Object)

   


.. py:method:: setOutput(Object)

   


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: compute(RandomAccessibleInterval, RandomAccessibleInterval)

   Computes the spectral similarity map.


Other Methods
~~~~~~~~~~~~~


.. py:method:: accept(Object)

   


.. py:method:: andThen(Consumer)

   


.. py:method:: static averageColorAtPositions(RandomAccessibleInterval, [[I)

   Computes the average color vector from a set of 3D positions in a multichannel image represented as per-channel ImageStacks.


.. py:method:: static averageColorFromPaths(RandomAccessibleInterval, List, double, double, double)

   As 
```
averageColorFromPaths(RandomAccessibleInterval, java.util.List, double, double, double)
```
, but also adding a pixel-space offset after scaling (see 
```
nodeToPixelCoords(sc.fiji.snt.util.PointInImage, double, double, double, double, double, double)
```
) - needed whenever input is the crop-local grid of a materialized crop, or the raw streamed source's own voxel grid under a non-zero `SNT#getWorldOriginOffset()`.


.. py:method:: static channelSum([D)

   Sums all elements of a vector. Typically used to compute the total intensity across channels of a color vector.


.. py:method:: in()

   


.. py:method:: initialize()

   


.. py:method:: static nodeToPixelCoords(PointInImage, double, double, double, double, double, double)

   As `nodeToPixelCoords(sc.fiji.snt.util.PointInImage, double, double, double)`, but also adding a pixel-space offset after scaling - typically `SNT#getActiveCanvasPixelOffset()`, needed whenever the target image is the crop-local grid of a materialized crop, or the raw streamed source's own voxel grid under a non-zero `SNT#getWorldOriginOffset()` (see `SNT#createSearch(double, double, double, double, double, double)` for the same conversion, applied to A* search endpoints instead of Path nodes).


.. py:method:: static normalizeVector([D)

   Normalizes a vector to unit length in place. If the vector has zero magnitude, it is left unchanged.


.. py:method:: ops()

   


.. py:method:: out()

   


.. py:method:: run()

   


See Also
--------

* `Package API <../api_auto/pysnt.filter.html#pysnt.filter.SpectralSimilarity>`_
* `SpectralSimilarity JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/filter/SpectralSimilarity.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
