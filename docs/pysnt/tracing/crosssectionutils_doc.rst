
``CrossSectionUtils`` Class Documentation
======================================


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


**Package:** ``sc.fiji.snt.tracing``

Static utilities for computing cross-sectional planes perpendicular to a path tangent. Extracted from ``PathFitter`` for reuse by other path-analysis tools (e.g., varicosity detection, torus mask generation).


Methods
-------


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: computeGridSize(double, double, int)

   Computes the grid size needed to cover a given physical radius at the specified scale, capped to a maximum.


.. py:method:: computeIsotropicScale(double[], double[], double, double, double)

   Computes the isotropic scale for a cross-section plane given the tangent plane basis vectors and voxel spacing.


.. py:method:: computeScaleAlongVector(double, double, double, double, double, double)

   Computes the effective physical scale along an arbitrary direction vector given anisotropic voxel spacing.


.. py:method:: computeTangentPlaneBasis(double, double, double)

   Computes an orthonormal basis for the plane perpendicular to the given normal (tangent) vector.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: sampleProfile(int, double, double, double, double[], double, double, double, double, RealRandomAccess)

   Samples a 1D intensity profile along a direction vector, centered on a given world position. Intended for 2D images where the cross-section perpendicular to a path tangent is a line, not a plane.


Other Methods
~~~~~~~~~~~~~


.. py:method:: applyAnnularMask(FloatProcessor, double, double)

   Applies an annular mask to a cross-section ``FloatProcessor``. Pixels outside the annulus (closer than ``innerRadius`` or farther than ``outerRadius`` from center) are set to ``Float.NaN``.


.. py:method:: applyAnnularMask1D(float[], double, double)

   Applies an annular mask to a 1D profile. Samples closer than ``innerRadius`` or farther than ``outerRadius`` from the center are set to ``Float.NaN``.


.. py:method:: backProject(int, int, int, double, double, double, double, double[], double[])

   Back-projects a 2D cross-section grid coordinate to 3D world coordinates.


.. py:method:: findMaxima1D(float[], double)

   Finds local maxima in a 1D profile using prominence-based filtering. A sample is a local maximum if it is strictly greater than both its neighbors (ignoring NaN) and its prominence exceeds the threshold. Prominence is defined as the peak value minus the highest saddle point connecting the peak to any higher peak (or the profile boundary).


.. py:method:: findMinima1D(float[], double)

   Finds local minima in a 1D profile using prominence-based filtering. Symmetric inversion of ``findMaxima1D(float[], double)``: a sample is a local minimum if it is strictly less than both its neighbors (ignoring NaN) and its prominence (the height it would need to climb to escape the basin and reach a deeper minimum, or the profile boundary) exceeds the threshold.

   Useful for detecting localized intensity valleys along a path's intensity profile -- the inverse of finding peaks.


.. py:method:: paintAnnulus(RandomAccessibleInterval, int, double, double, double, double, double[], double[], double, double, double, double, double, double, double, double, double)

   Paints an annular cross-section into a 3D output image. For each pixel in the annulus (between ``innerRadius`` and ``outerRadius`` in grid space), the corresponding voxel in the output image is set to ``fillValue``. Existing non-zero voxels are preserved (logical OR).


.. py:method:: sampleCrossSection(int, double, double, double, double, double, double[], double[], double, double, double, double, double, double, RealRandomAccess)

   Samples a square cross-section of an image on the plane perpendicular to a path tangent at a given node position. The section is centered on the node and oriented according to the precomputed basis vectors.


See Also
--------

* `Package API <../api_auto/pysnt.tracing.html#pysnt.tracing.CrossSectionUtils>`_
* `CrossSectionUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/CrossSectionUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
