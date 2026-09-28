Analysis Methods
================

Methods that perform calculations, measurements, or statistical analysis.

Total methods in this category: **25**

.. contents:: Classes in this Category
   :local:

BoundingBox
-----------

.. method:: compute(arg0)

   Computes a new positioning so that this box encloses the specified point cloud.

   **Signature:** ``compute(Iterator) -> void``

   **Parameters:**

   * **arg0** (``Any``): - the iterator of the points Collection

   **Returns:** ``None``


ConvexHull2D
------------

.. method:: compute()

   Description copied from class: AbstractConvexHull

   **Signature:** ``compute() -> void``

   **Returns:** ``None``


ConvexHull3D
------------

.. method:: compute()

   Description copied from class: AbstractConvexHull

   **Signature:** ``compute() -> void``

   **Returns:** ``None``


ConvexHullAnalyzer
------------------

.. method:: static supportedMetrics()

   Gets the list of metrics supported by ConvexHullAnalyzer.

   **Signature:** ``static supportedMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metric names that can be computed by this analyzer


Frangi
------

.. method:: compute(arg0, arg1)

   **Signature:** ``compute(Object, Object) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``


MultiTreeColorMapper
--------------------

.. method:: static getMetrics(arg0)

   Gets the list of supported mapping metrics.

   **Signature:** ``static getMetrics(String) -> List``

   **Parameters:**

   * **arg0** (``str``): - Either 'all' (MultiTreeColorMapper and TreeColorMapper metrics) or 'default' (MultiTreeColorMapper only)

   **Returns:** (``List[Any]``) the list of mapping metrics.

.. method:: static getSingleValueMetrics()

   Gets the list of single-value mapping metrics.

   **Signature:** ``static getSingleValueMetrics() -> List``

   **Returns:** (``List[Any]``) the list of single-value mapping metrics.


MultiTreeStatistics
-------------------

.. method:: static getAllMetrics()

   Description copied from class: TreeStatistics

   **Signature:** ``static getAllMetrics() -> List``

   **Returns:** (``List[Any]``) the terminal branches. Note that as per `Path.getSection(int, int)`, these branches will not carry any connectivity information.

.. method:: static getMetrics()

   Gets the list of metrics supported by MultiTreeStatistics.

Returns all the metrics that can be computed for groups of trees, including aggregate measures and group-specific statistics.

   **Signature:** ``static getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metric names


NodeColorMapper
---------------

.. method:: static getMetrics()

   Gets the list of supported mapping metrics.

   **Signature:** ``static getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of mapping metrics.


NodeStatistics
--------------

.. method:: static computeNearestNeighborDistances(arg0)

   Computes nearest neighbor distances. Assigns the computed value to the v value of each point

   **Signature:** ``static computeNearestNeighborDistances(List) -> void``

   **Parameters:**

   * **arg0** (``List[Any]``): - the list of points

   **Returns:** ``None``

.. method:: static getMetrics()

   Gets the list of supported metrics.

   **Signature:** ``static getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metrics


OBJMesh
-------

.. method:: computePrincipalAxes(arg0)

   Computes the principal axes of this mesh using the new PCAnalyzer. This method replaces the deprecated `getPrincipalAxes(String)` method.

   **Signature:** ``computePrincipalAxes(String) -> PCAnalyzer$PrincipalAxis;``

   **Parameters:**

   * **arg0** (``str``): - either "left", "l", "right", "r", otherwise principal axes are computed for both hemi-halves, i.e., the full mesh

   **Returns:** (``Any``) array of three PrincipalAxis objects ordered by decreasing variance (primary, secondary, tertiary), or null if computation fails


PathStatistics
--------------

.. method:: static getAllMetrics()

   Gets the terminal branches from the analyzed paths.

Returns paths that have children, representing non-terminal segments. Note: This implementation differs from typical terminal branch definition as it returns paths with children rather than leaf paths.

   **Signature:** ``static getAllMetrics() -> List``

   **Returns:** (``List[Any]``) the list of paths with children

.. method:: static getMetrics()

   **Signature:** ``static getMetrics() -> List``

   **Returns:** ``List[Any]``


RootAngleAnalyzer
-----------------

.. method:: static supportedMetrics()

   **Signature:** ``static supportedMetrics() -> List``

   **Returns:** ``List[Any]``


SeedManager
-----------

.. method:: computeVisibleRect(arg0)

   **Signature:** ``computeVisibleRect(Rectangle) -> void``

   **Parameters:**

   * **arg0** (``Any``)

   **Returns:** ``None``


ShollAnalyzer
-------------

.. method:: static getMetrics()

   **Signature:** ``static getMetrics() -> List``

   **Returns:** ``List[Any]``


SpectralSimilarity
------------------

.. method:: compute(arg0, arg1)

   Computes the spectral similarity map.

   **Signature:** ``compute(RandomAccessibleInterval, RandomAccessibleInterval) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``


TreeColorMapper
---------------

.. method:: static getMetrics()

   Gets the list of supported mapping metrics.

   **Signature:** ``static getMetrics() -> List``

   **Returns:** (``List[Any]``) the list of mapping metrics.


TreeStatistics
--------------

.. method:: static getAllMetrics()

   Gets the list of supported metrics.

   **Signature:** ``static getAllMetrics() -> List``

   **Returns:** (``List[Any]``) the list of available metrics


TreeUtils
---------

.. method:: static analyzeEndpointClusters(arg0)

   Analyzes a collection of paths to determine which endpoint cluster (starts or ends) is more tightly grouped, suggesting the root location.

This is useful for auto-orienting paths toward a common root when the user hasn't specified an explicit root location.

   **Signature:** ``static analyzeEndpointClusters(Collection) -> TreeUtils$EndpointClusterAnalysis``

   **Parameters:**

   * **arg0** (``List[Any]``): - the paths to analyze (must have at least 2)

   **Returns:** (``Any``) analysis result, or null if paths is null or has fewer than 2 paths

.. method:: static computeUprightAngle(arg0, arg1)

   Computes the angle (in degrees) needed to make a tree appear upright in the XY viewing plane. The angle is derived from the extension angle of a reference path (the longest geodesic by default) using compass conventions where North is 0 degrees.

   **Signature:** ``static computeUprightAngle(Tree, boolean) -> double``

   **Parameters:**

   * **arg0** (``Tree``): - the tree to analyze
   * **arg1** (``bool``)

   **Returns:** (``float``) the rotation angle in degrees, or Double.NaN if it cannot be computed (e.g., single-node tree)


Tubeness
--------

.. method:: compute(arg0, arg1)

   **Signature:** ``compute(RandomAccessibleInterval, RandomAccessibleInterval) -> void``

   **Parameters:**

   * **arg0** (``Any``)
   * **arg1** (``Any``)

   **Returns:** ``None``


Viewer2D
--------

.. method:: static getMetrics()

   **Signature:** ``static getMetrics() -> List``

   **Returns:** ``List[Any]``


----

*Category index generated on 2026-09-27 23:02:20*