Analysis Methods
================

Methods that perform calculations, measurements, or statistical analysis.

Total methods in this category: **36**

.. contents:: Classes in this Category
   :local:

ArrayStorageBackend
-------------------

.. method:: computeGWDT(source, threshold, spacing, minIntensity, maxIntensity)

   **Signature:** ``computeGWDT(RandomAccessibleInterval, double, double[], double, double) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)
   * **minIntensity** (``float``)
   * **maxIntensity** (``float``)

   **Returns:** ``None``


BoundingBox
-----------

.. method:: compute(iterator)

   Computes a new positioning so that this box encloses the specified point cloud.

   **Signature:** ``compute(Iterator) -> void``

   **Parameters:**

   * **iterator** (``Any``): - the iterator of the points Collection

   **Returns:** ``None``


ConvexHull2D
------------

.. method:: compute()

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``compute() -> void``

   **Returns:** ``None``


ConvexHull3D
------------

.. method:: compute()

   Description copied from class: `AbstractConvexHull`

   **Signature:** ``compute() -> void``

   **Returns:** ``None``


ConvexHullAnalyzer
------------------

.. method:: supportedMetrics()

   Gets the list of metrics supported by ConvexHullAnalyzer.

   **Signature:** ``supportedMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metric names that can be computed by this analyzer


CrossSectionUtils
-----------------

.. method:: computeIsotropicScale(aBasis, bBasis, xSpacing, ySpacing, zSpacing)

   Computes the isotropic scale for a cross-section plane given the tangent plane basis vectors and voxel spacing.

   **Signature:** ``computeIsotropicScale(double[], double[], double, double, double) -> double``

   **Parameters:**

   * **aBasis** (``List[float]``): - first basis vector
   * **bBasis** (``List[float]``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)

   **Returns:** (``float``) the isotropic scale (geometric mean of scales along both basis vectors)

.. method:: computeScaleAlongVector(vx, vy, vz, xSpacing, ySpacing, zSpacing)

   Computes the effective physical scale along an arbitrary direction vector given anisotropic voxel spacing.

   **Signature:** ``computeScaleAlongVector(double, double, double, double, double, double) -> double``

   **Parameters:**

   * **vx** (``float``): - X component of direction vector
   * **vy** (``float``)
   * **vz** (``float``)
   * **xSpacing** (``float``)
   * **ySpacing** (``float``)
   * **zSpacing** (``float``)

   **Returns:** (``float``) effective scale (physical distance per unit in the given direction)

.. method:: computeTangentPlaneBasis(nx, ny, nz)

   Computes an orthonormal basis for the plane perpendicular to the given normal (tangent) vector.

   **Signature:** ``computeTangentPlaneBasis(double, double, double) -> double[][]``

   **Parameters:**

   * **nx** (``float``): - X component of the normal vector
   * **ny** (``float``)
   * **nz** (``float``)

   **Returns:** (``List[List[float]]``) `double[2][3]`: `[0]` is the first basis vector, `[1]` is the second basis vector


DetectorUtils
-------------

.. method:: computeEDT(labelRAI, labelVal, spacing)

   **Signature:** ``computeEDT(RandomAccessibleInterval, int, double[]) -> Img``

   **Parameters:**

   * **labelRAI** (``Any``)
   * **labelVal** (``int``)
   * **spacing** (``List[float]``)

   **Returns:** ``Any``


DiskBackedStorageBackend
------------------------

.. method:: computeGWDT(source, threshold, spacing, minIntensity, maxIntensity)

   **Signature:** ``computeGWDT(RandomAccessibleInterval, double, double[], double, double) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)
   * **minIntensity** (``float``)
   * **maxIntensity** (``float``)

   **Returns:** ``None``


Frangi
------

.. method:: compute(input, output)

   **Signature:** ``compute(RandomAccessibleInterval, RandomAccessibleInterval) -> void``

   **Parameters:**

   * **input** (``Any``)
   * **output** (``Any``)

   **Returns:** ``None``


GrowthAnalyzer
--------------

.. method:: analyze(paths, frameInterval, timeUnits)

   **Signature:** ``analyze(Collection, double, String) -> GrowthAnalysisResults``

   **Parameters:**

   * **paths** (``List[Any]``)
   * **frameInterval** (``float``)
   * **timeUnits** (``str``)

   **Returns:** ``GrowthAnalysisResults``


ImgUtils
--------

.. method:: computeIntensityStats(source)

   Computes basic intensity statistics of an image.

   **Signature:** ``computeIntensityStats(RandomAccessibleInterval) -> double[]``

   **Parameters:**

   * **source** (``Any``): - the input image

   **Returns:** (``List[float]``) array of [min, max, mean]

.. method:: computeMeanIntensity(source)

   Computes the mean intensity of an image.

   **Signature:** ``computeMeanIntensity(RandomAccessibleInterval) -> double``

   **Parameters:**

   * **source** (``Any``): - the input image

   **Returns:** (``float``) the mean intensity value

.. method:: computePercentile(source, percentile)

   Computes an approximate percentile by random sampling.

   **Signature:** ``computePercentile(RandomAccessibleInterval, double) -> double``

   **Parameters:**

   * **source** (``Any``): - the input image
   * **percentile** (``float``)

   **Returns:** (``float``) the approximate percentile value


LabelsToSeeds
-------------

.. method:: compute(imp, minConfidence, type, source)

   **Signature:** ``compute(ImagePlus, double, String, String) -> List``

   **Parameters:**

   * **imp** (``Any``)
   * **minConfidence** (``float``)
   * **type** (``str``)
   * **source** (``str``)

   **Returns:** ``List[Any]``


MultiSpectralRefiner
--------------------

.. method:: computeNodeCosts(imp, path)

   Computes the cost at each node of a path without modifying it, where the path's node coordinates and imp's own pixel grid are related by a fixed offset. See `MultiSpectralRefiner(ImagePlus, Path, double, double, double)`.

   **Signature:** ``computeNodeCosts(ImagePlus, Path) -> double[]``

   **Parameters:**

   * **imp** (``Any``): - the multichannel image
   * **path** (``Path``)

   **Returns:** (``List[float]``) per-node cost values (same length as path.size())


MultiTreeStatistics
-------------------

.. method:: measure(metrics, groupByType)

   **Signature:** ``measure(Collection, boolean) -> void``

   **Parameters:**

   * **metrics** (``List[Any]``)
   * **groupByType** (``bool``)

   **Returns:** ``None``


NodeStatistics
--------------

.. method:: computeNearestNeighborDistances(points)

   Computes nearest neighbor distances. Assigns the computed value to the `v` value of each point

   **Signature:** ``computeNearestNeighborDistances(List) -> void``

   **Parameters:**

   * **points** (``List[Any]``): - the list of points

   **Returns:** ``None``


OBJMesh
-------

.. method:: computePrincipalAxes(hemiHalf)

   Computes the principal axes of this mesh using the new PCAnalyzer. This method replaces the deprecated `getPrincipalAxes(String)` method.

   **Signature:** ``computePrincipalAxes(String) -> PrincipalAxis[]``

   **Parameters:**

   * **hemiHalf** (``str``): - either "left", "l", "right", "r", otherwise principal axes are computed for both hemi-halves, i.e., the full mesh

   **Returns:** (``List[Any]``) array of three PrincipalAxis objects ordered by decreasing variance (primary, secondary, tertiary), or null if computation fails


PathStatistics
--------------

.. method:: measure(metrics, groupByType)

   **Signature:** ``measure(Collection, boolean) -> void``

   **Parameters:**

   * **metrics** (``List[Any]``)
   * **groupByType** (``bool``)

   **Returns:** ``None``

.. method:: measureIndividualPaths(metrics, summarize)

   Measures specified metrics for each individual path and creates a detailed table.

This method generates a comprehensive measurement table where each row represents an individual path and columns contain the requested morphometric measurements. This is particularly useful for comparative analysis of path properties or for exporting detailed morphometric data.

The generated table includes:

- Path identification information (name, SWC type)

- All requested morphometric measurements

- Optional summary statistics (if summarize is true)

   **Signature:** ``measureIndividualPaths(Collection, boolean) -> void``

   **Parameters:**

   * **metrics** (``List[Any]``): - the collection of metric names to measure for each path. If null or empty, a default "safe" set of metrics is used
   * **summarize** (``bool``)

   **Returns:** ``None``


PlausibilityMonitor
-------------------

.. method:: measure(deepCheck, paths)

   **Signature:** ``measure(DeepCheck, Collection) -> Measurements``

   **Parameters:**

   * **deepCheck** (``Any``)
   * **paths** (``List[Any]``)

   **Returns:** ``Any``


RootAngleAnalyzer
-----------------

.. method:: supportedMetrics()

   **Signature:** ``supportedMetrics() -> List``

   **Returns:** ``List[Any]``


SNT
---

.. method:: computeImgStats(in, imgStats, costType)

   **Signature:** ``computeImgStats(Iterable, ImageStatistics, CostType) -> ImageStatistics``

   **Parameters:**

   * **in** (``List[Any]``)
   * **imgStats** (``Any``)
   * **costType** (``Any``)

   **Returns:** ``Any``


SomaUtils
---------

.. method:: computeIntegratedDensity(mask, source)

   **Signature:** ``computeIntegratedDensity(Img, RandomAccessibleInterval) -> double``

   **Parameters:**

   * **mask** (``Any``)
   * **source** (``Any``)

   **Returns:** ``float``

.. method:: computeMaskArea(mask, spacing)

   **Signature:** ``computeMaskArea(Img, double[]) -> double``

   **Parameters:**

   * **mask** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``float``

.. method:: computeMaskCentroid(mask, spacing)

   **Signature:** ``computeMaskCentroid(Img, double[]) -> double[]``

   **Parameters:**

   * **mask** (``Any``)
   * **spacing** (``List[float]``)

   **Returns:** ``List[float]``

.. method:: computeMinimumThreshold(source)

   **Signature:** ``computeMinimumThreshold(RandomAccessibleInterval) -> double``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``float``

.. method:: computeOtsuThreshold(source)

   **Signature:** ``computeOtsuThreshold(RandomAccessibleInterval) -> double``

   **Parameters:**

   * **source** (``Any``)

   **Returns:** ``float``


SparseStorageBackend
--------------------

.. method:: computeGWDT(source, threshold, spacing, minIntensity, maxIntensity)

   **Signature:** ``computeGWDT(RandomAccessibleInterval, double, double[], double, double) -> void``

   **Parameters:**

   * **source** (``Any``)
   * **threshold** (``float``)
   * **spacing** (``List[float]``)
   * **minIntensity** (``float``)
   * **maxIntensity** (``float``)

   **Returns:** ``None``


SpectralSimilarity
------------------

.. method:: compute(input, output)

   Computes the spectral similarity map.

   **Signature:** ``compute(RandomAccessibleInterval, RandomAccessibleInterval) -> void``

   **Parameters:**

   * **input** (``Any``): - 4D input image (X, Y, Z, C) where the last dimension is channels
   * **output** (``Any``)

   **Returns:** ``None``


TreeStatistics
--------------

.. method:: measure(metrics, groupByType)

   Measures this Tree, outputting the result to the measurements table. If a Context has been specified, the table is updated. Otherwise, table contents are printed to Console.

   **Signature:** ``measure(Collection, boolean) -> void``

   **Parameters:**

   * **metrics** (``List[Any]``): - the row header label
   * **groupByType** (``bool``)

   **Returns:** ``None``


TreeUtils
---------

.. method:: analyzeEndpointClusters(paths)

   Analyzes a collection of paths to determine which endpoint cluster (starts or ends) is more tightly grouped, suggesting the root location.

This is useful for auto-orienting paths toward a common root when the user hasn't specified an explicit root location.

   **Signature:** ``analyzeEndpointClusters(Collection) -> EndpointClusterAnalysis``

   **Parameters:**

   * **paths** (``List[Any]``): - the paths to analyze (must have at least 2)

   **Returns:** (``Any``) analysis result, or null if paths is null or has fewer than 2 paths

.. method:: computeUprightAngle(tree, useCentroid)

   Computes the angle (in degrees) needed to make a tree appear upright in the XY viewing plane. The angle is derived from the extension angle of a reference path (the longest geodesic by default) using compass conventions where North is 0 degrees.

   **Signature:** ``computeUprightAngle(Tree, boolean) -> double``

   **Parameters:**

   * **tree** (``Tree``): - the tree to analyze
   * **useCentroid** (``bool``)

   **Returns:** (``float``) the rotation angle in degrees, or `Double.NaN` if it cannot be computed (e.g., single-node tree, or tree with multiple roots)


Tubeness
--------

.. method:: compute(input, output)

   **Signature:** ``compute(RandomAccessibleInterval, RandomAccessibleInterval) -> void``

   **Parameters:**

   * **input** (``Any``)
   * **output** (``Any``)

   **Returns:** ``None``


----

*Category index generated on 2026-11-02 07:57:40*