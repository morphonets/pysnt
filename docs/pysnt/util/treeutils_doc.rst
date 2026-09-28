
``TreeUtils`` Class Documentation
==============================


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

Static utilities for Trees.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getConnectedTree(Path)

   Gets the connected tree (component) containing the given path. This traverses up to the root and then collects all descendants, ensuring we only get paths that are actually connected via parent-child relationships.

This is useful when paths may share a tree ID but are not actually connected (e.g., orphaned paths or paths awaiting relationship rebuild).


.. py:method:: static getMaxOrder(Path)

   Returns the maximum path order in the connected tree containing the given path. Higher values indicate deeper/more developed trees.


.. py:method:: static getRootPath(Path)

   Gets the root path of the tree containing the given path.


.. py:method:: static isAncestorOf(Path, Path)

   Checks if 'potentialAncestor' is an ancestor of 'potentialDescendant'. This traverses up the parent chain from potentialDescendant.


.. py:method:: static isDescendantOf(Path, Path)

   Checks if 'potentialDescendant' is a descendant of 'potentialAncestor'. This is equivalent to checking if potentialDescendant is in the subtree rooted at potentialAncestor (excluding potentialAncestor itself).


.. py:method:: static isInSubtree(Path, Path)

   Checks if 'target' is in the subtree rooted at 'root'. This traverses down through all descendants of root.


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: static analyzeEndpointClusters(Collection)

   Analyzes a collection of paths to determine which endpoint cluster (starts or ends) is more tightly grouped, suggesting the root location.

This is useful for auto-orienting paths toward a common root when the user hasn't specified an explicit root location.


.. py:method:: static computeUprightAngle(Tree, boolean)

   Computes the angle (in degrees) needed to make a tree appear upright in the XY viewing plane. The angle is derived from the extension angle of a reference path (the longest geodesic by default) using compass conventions where North is 0 degrees.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static assignUniqueColors(Tree)

   Assigns distinct colors to a collection of Trees.


.. py:method:: static assignUniqueColorsIfUncolored(Collection, String)

   Assigns distinct colors to trees that have no pre-existing color information, leaving trees with custom path/node colors untouched. Useful when importing files that may already carry authored colors (e.g., a traces file with per-path color attributes), where forcing a single flat color per tree would discard that information.


.. py:method:: static canFormContinuousChain(Collection, double)

   Checks if a collection of paths can form a spatially continuous chain within a given tolerance.


.. py:method:: static collectChildren(Path, Collection)

   Collects direct children of a path into the provided collection.


.. py:method:: static collectDescendants(Path, Collection)

   Collects all descendants (children, grandchildren, etc.) of a path into the provided collection.


.. py:method:: static countDescendants(Path)

   Counts all descendants (children, grandchildren, etc.) of a path.


.. py:method:: static filterByCableLength(Collection, double, double)

   Returns the subset of trees whose cable length falls within the specified range.


.. py:method:: static filterBySize(Collection, int, int)

   Returns the subset of trees whose path count falls within the specified range.


.. py:method:: static findClosestEndpoints(Path, Path)

   Finds the closest endpoint pairing between two paths. Checks all four combinations: start-start, start-end, end-start, end-end.


.. py:method:: static findPathsNeedingReversal(Collection, PointInImage)

   Determines which paths need to be reversed so that their start nodes point toward a given root location.

A path should be reversed if its end node is closer to the root than its start node.


.. py:method:: static merge(Collection)

   Combines all trees into a single Tree container.

Note that no effort is made to make the merge structure topographylically valid. This is simply a convenience method to collect paths in a single contained for operations that do not require an accurate graph structure, e.g., Sholl Analysis.


.. py:method:: static mergeContinuousPaths(Tree, double)

   Merges paths that continue along the same trajectory at branch points, reducing fragmentation in auto-traced reconstructions.

Problem: Auto-tracers like GWDTTracer often create separate paths at every branch point, even when the neurite continues straight through. This may fragment continuous paths into smaller segments.

Solution: At each junction where a parent path ends and children begin, this method checks if any child's trajectory aligns with the parent's. If the angle between their direction vectors is below the threshold, the most aligned child is merged into the parent, creating a longer continuous path.

Algorithm:

For each path with children, compute the parent's end tangent vector (direction at its terminal segment) For each child, compute its start tangent vector Find the child with the smallest angle to the parent direction If this angle ≤ threshold: append child's nodes to parent, reparent grandchildren to the extended parent, remove child from tree Repeat until no more merges are possible

Criteria for merging: Two paths are merged when:

The child starts at the parent's endpoint (branch point) The angle between their direction vectors ≤ angleThreshold The child is the most aligned among all siblings

Example: A traced axon might be split into 5 paths at 4 branch points: 
```
Before: P1 → P2 → P3 → P4 → P5  (with side branches B1, B2, B3, B4)
 After:  P1 (merged trunk) with children B1, B2, B3, B4
```



.. py:method:: static mergePaths(List, boolean)

   Merges a list of paths into a single path by appending nodes sequentially.

The paths should be pre-ordered and oriented using `orderByEndpointProximity(java.util.Collection<sc.fiji.snt.Path>)` and `orientPathsForMerging(java.util.List<sc.fiji.snt.Path>)`.

This method handles:

Appending nodes from each path to the result Optionally reparenting children of merged paths to the result Preserving the first path's parent connection (if any)

Note: This method does NOT delete the original paths from any manager. The caller is responsible for cleanup.


.. py:method:: static orderByEndpointProximity(Collection)

   Orders a collection of paths to form a spatially continuous chain based on endpoint proximity. The algorithm greedily connects paths by finding the closest endpoint pairs.

This method does NOT modify the paths (no reversal). Use `orientPathsForMerging(List)` on the result to fix orientations.


.. py:method:: static orientPathsForMerging(List)

   Orients paths in a chain so they can be merged end-to-start. After this operation, each path's end node will be near the next path's start node.

Paths are reversed in-place as needed.


.. py:method:: static orientPathsTowardRoot(Collection, PointInImage)

   Orients paths so their start nodes point toward a given root location. Paths are reversed in-place if their end node is closer to the root.

Note: This method does NOT update child branch points. Callers must handle child branch point updates separately if paths have children.


.. py:method:: static rasterize(Tree, double, double)

   Rasterizes a tree into a 3D image with the specified voxel sizes.


.. py:method:: static restoreNodeValues(Map)

   Restores per-path node values captured by `snapshotNodeValues(Tree)`.


.. py:method:: static snapshotNodeValues(Tree)

   Snapshots the per-node values (node.v) for each path in a Tree so they can be restored later.


.. py:method:: static splitByPrimaryPaths(Tree)

   Splits a tree with multiple primary paths into separate trees, one rooted at each primary path.


.. py:method:: static suggestRootLocation(Collection, PointInImage)

   Analyzes paths and suggests auto-orientation based on:

If a reference point (e.g., ROI centroid) is provided, orient toward it For 3+ paths: find the tighter endpoint cluster as the root For 2 paths: find the closest endpoint pair as the root


.. py:method:: static syncCanvasOffset(Path, Path)

   Applies the parent's canvas offset to the child path and all its descendants. This ensures paths are in the same coordinate space after connection. Node coordinates are transformed to maintain the same visual position.


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.TreeUtils>`_
* `TreeUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/TreeUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
