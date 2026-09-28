
``TreeToRaster`` Class Documentation
=================================


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


**Package:** ``sc.fiji.snt.util``

Rasterizes a Tree into a 3D image using frustum (truncated-cone) geometry with partial-volume supersampling. Each segment between consecutive nodes is modeled as a frustum whose radii are linearly interpolated from the node radii. This produces a volumetric rendering that respects the thickness of each neurite, unlike the skeleton-based rasterization in Tree.getSkeleton().

Optionally, Poisson shot noise and Gaussian blur (to simulate spatially correlated noise) can be applied, producing realistic synthetic fluorescence microscopy images.

Optionally, voxel intensities can be modulated by local neurite thickness via `setThicknessModulation(double)`, producing brighter thick neurites and dimmer thin ones.

Pass 2 (partial-volume supersampling) and subsequent passes are parallelized across z-slices for improved performance. A spatial grid is used for frustum lookups to reduce computation costs.

Inspired by SWC2IMG (E. Meijering, imagescience.org).


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAxialRes()

   Gets the axial (z) voxel size.


.. py:method:: getLateralRes()

   Gets the lateral (x, y) voxel size.


.. py:method:: getRadiusScale()

   Gets the uniform radius multiplier applied to node radii.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAxialRes(double)

   Sets the axial (z) voxel size.

A value of 0 switches the rasterizer to 2D mode: the z coordinates of the tree are ignored (every node is projected onto the z = 0 plane) and the output image is a single slice. In-plane (x, y) thickness from node radii is preserved.


.. py:method:: setDefaultRadius(double)

   Sets the default radius used for nodes/trees that have no radii defined. If not set, defaults to half the lateral voxel size (i.e., a 1-voxel diameter).


.. py:method:: setGaussianBlur(double)

   Enables Gaussian blurring of the (optionally noisy) image, simulating spatially correlated noise and optical blur. Note that Gaussian blurring is ignored when using `rasterizePathLabels()`.


.. py:method:: setLateralRes(double)

   Sets the lateral (x, y) voxel size.


.. py:method:: setPoissonNoise(double, double)

   Enables Poisson shot noise on the rasterized image, simulating photon counting noise typical of fluorescence microscopy.

The peak intensity is derived from the SNR and background using the photon-counting model: `SNR = (peak - bg) / sqrt(peak)`. Note that Poisson shot noise is ignored when using `rasterizePathLabels()`


.. py:method:: setRadiusScale(double)

   Sets a uniform multiplier applied to every node radius (and to the default radius for nodes without radii) when rasterizing. Values above 1 dilate the rendered neurites, e.g. to make thin or sparse structures cover more voxels; values below 1 erode them. Because scaling is uniform, the relative thickness order (and thus thickest-wins label priority) is unchanged.

Note that larger radii increase the rasterized extent and the per-voxel supersampling cost.


.. py:method:: setReferenceBounds(int, int, int)

   Sets reference bounds explicitly, so the output image matches the specified dimensions. When set, the rasterized image will have exactly the given width, height, and depth, with the origin at (0, 0, 0) in pixel coordinates.


.. py:method:: setThicknessModulation(double)

   Enables intensity modulation based on local neurite thickness. When enabled, thicker neurites are rendered brighter and thinner neurites dimmer, proportional to the local radius.

The modulation factor defines what fraction of the intensity range is used for thickness variation. For example, a factor of 0.2 means the thickest frustum receives full intensity (1.0) while the thinnest receives 80% of the maximum (0.8).

Note: This option incurs additional computation since the local radius must be resolved for every sub-voxel hit during supersampling. Also, a factor of 1.0 maps the thinnest structure to zero intensity, effectively wiping it.


Other Methods
~~~~~~~~~~~~~


.. py:method:: rasterize()

   Rasterizes the tree into a 32-bit (float) image using partial-volume supersampling. Voxel values represent the fraction of the supersampled sub-voxels that fall inside the neuron structure (0.0 = background, 1.0 = fully inside), unless noise has been enabled via `setPoissonNoise(double, double)`, in which case values represent simulated photon counts.


.. py:method:: rasterizeLabels()

   Rasterizes the tree into a 16-bit label image where each voxel is assigned the 1-based index of the Path that owns it (as ordered by Tree.list()). Background voxels are 0.


.. py:method:: rasterizeNodeValueLabels()

   Rasterizes the tree into a 16-bit label image where each voxel is assigned the node value of the nearest path node (as stored via `Path.setNodeValue(double, int)`). This enables per-node labeling, e.g., from delineation assignments, atlas annotations, or other node-level classifications.

Node values are expected to be negative integers (as used by DelineationsManager); they are negated to produce positive labels in the output image. Nodes with NaN or non-negative values are treated as background (0).

Each frustum (segment between consecutive nodes) inherits the label of its start node. At intersection sites, the frustum with the largest local radius wins (thickest-wins), consistent with `rasterizePathLabels()`.

Note: The output is 16-bit unsigned (short), so label values above 65535 will overflow. In practice this is not a concern when the source is a label/segmentation image with a bounded class count, but callers should be aware of this limit.


.. py:method:: rasterizePathLabels()

   Rasterizes the tree into a 16-bit label image where each voxel is assigned the 1-based index of the Path that owns it (as ordered by Tree.list()). Background voxels are 0.

At intersection sites where multiple paths overlap, the path with the largest local radius wins (thickest-wins priority), ensuring that thin branches crossing a thick trunk do not overwrite it.

The returned image has the same dimensions and calibration as the density image produced by rasterize(), so the two can be used as overlays. Noise and blur settings are ignored for label images.


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.TreeToRaster>`_
* `TreeToRaster JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/TreeToRaster.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
