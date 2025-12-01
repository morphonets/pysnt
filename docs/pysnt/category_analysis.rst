Analysis Methods
================

Methods that perform calculations, measurements, or statistical analysis.

Total methods in this category: **18**

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

   **Signature:** ``compute() -> void``

   **Returns:** ``None``


ConvexHull3D
------------

.. method:: compute()

   **Signature:** ``compute() -> void``

   **Returns:** ``None``


ConvexHullAnalyzer
------------------

.. method:: static supportedMetrics()

   Gets the list of metrics supported by ConvexHullAnalyzer.

   **Signature:** ``static supportedMetrics() -> List``

   **Returns:** (``List[Any]``) the list of supported metric names that can be computed by this analyzer


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


ShollAnalyzer
-------------

.. method:: static getMetrics()

   **Signature:** ``static getMetrics() -> List``

   **Returns:** ``List[Any]``


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


Viewer2D
--------

.. method:: static getMetrics()

   **Signature:** ``static getMetrics() -> List``

   **Returns:** ``List[Any]``


----

*Category index generated on 2025-11-30 21:54:05*