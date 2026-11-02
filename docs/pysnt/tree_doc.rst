
``Tree`` Class Documentation
=========================


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

Utility class to access a Collection of Paths (typically a complete reconstruction). A Tree is the preferred way to group, access and manipulate `Path`s that share something in common, specially when scripting SNT. Note that a "Tree" here is literally a collection of `Path`s. Very few restrictions are imposed on its topology, although it is generally assumed that the Collection of paths describes a single-rooted structure with no loops.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clone()

   Creates a deep copy of this Tree.

   This method creates a complete copy of the tree including all paths and their relationships. Each path is cloned individually, and then the parent-child relationships are reconstructed in the cloned tree. This ensures that the cloned tree maintains the same structure as the original while being completely independent.


.. py:method:: transformedCopy(String)

   Retrieves a transformed duplicate of this tree.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: get(int)

   Returns the Path at the specified position.


.. py:method:: getApproximatedSurface()

   Retrieves an approximate estimate of Tree's surface are by approximating the surface area of each path, and summing to total. The surface of each path is computed assuming the lateral surface area of a conical frustum between nodes.


.. py:method:: getApproximatedVolume()

   Retrieves an approximate estimate of Tree's volume by approximating the volume of each path, and summing to total. The volume of each path is computed assuming the volume of each of inter-node segment to be that of a truncated cone (Frustum).


.. py:method:: getAssignedValue()

   Retrieves the numeric property assigned to this Tree.


.. py:method:: getBPs()

   Gets the branch points (junctions) of the graph. This is simply an alias for ``DirectedWeightedGraph.getBPs()``.


.. py:method:: getBoundingBox()

   Gets the bounding box associated with this tree.


.. py:method:: getCanvasOffset()

   Returns the canvas offset of this tree.


.. py:method:: getColor()

   Gets the color assigned to this Tree.


.. py:method:: getConvexHull()

   Retrieves the convex hull of this tree.


.. py:method:: getGraph()

   Assembles a DirectedGraph from this Tree.


.. py:method:: getImpContainer(int, int)

   Gets an empty image capable of holding the skeletonized version of this tree.


.. py:method:: getLabel()

   Returns the identifying label of this tree. When importing files, the label typically defaults to the imported filename,


.. py:method:: getNodes()

   Gets all the nodes (path points) forming this tree.


.. py:method:: getNodesAsSWCPoints()

   


.. py:method:: getNodesCount()

   Gets the total number of nodes across all paths in this Tree.


.. py:method:: getProperties()

   Returns the Properties instance holding the persistent set of properties. Useful to associate metadata to this tree. E.g.




   ::

       getProperties().setProperty(Tree.KEY_SPATIAL_UNIT, "um");
       String unit = getProperties().getProperty(Tree.KEY_SPATIAL_UNIT);
       getProperties().setProperty(Tree.KEY_COMPARTMENT, Tree.DENDRITIC);





.. py:method:: getRoot()

   Gets the first node of the main primary path of this tree


.. py:method:: getSWCTypeMap()

   Returns the SWC Type flags used by SNT.


.. py:method:: getSWCTypeNames(boolean)

   Gets the set of SWC type labels present in this tree with optional soma inclusion in a readable form.


.. py:method:: getSWCTypes()

   Gets the set of SWC types present in this tree with optional soma inclusion.


.. py:method:: getSkeleton()

   Retrieves the rasterized skeleton of this tree at 1:1 scaling.


.. py:method:: getSkeleton2D()

   Retrieves a 2D projection of the rasterized skeleton of this tree at 1:1 scaling.


.. py:method:: getSomaNodes()

   Gets the list of all nodes tagged as ``Path.SWC_SOMA``.


.. py:method:: getSparseGraph()

   Assembles a memory-efficient CSR-backed ``DirectedWeightedGraph`` from this Tree. Functionally equivalent to ``getGraph()`` (same vertex / edge content, same edge weights), but the underlying storage uses ~20x less heap per vertex than the default jgrapht specifics. Useful in batch workflows where many trees' graphs are held simultaneously, or where an analyzer is run across very large neuron collections.

   Trade-off: ``getEdge(v1, v2)`` is O(out-degree of v1) instead of O(1), and per-vertex edge iteration is in reverse insertion order. Both are negligible for permutation-invariant analyses such as Strahler ordering.


.. py:method:: getTips()

   Gets the end points (tips) of the graph. This is simply an alias for ``DirectedWeightedGraph.getTips()``.


.. py:method:: getTreeID()

   Returns the ID shared by every ``Path`` in this tree (see ``Path.getTreeID()``), i.e., the arbor's identity as tracked by the ``PathAndFillManager`` that assigned it.

   **Uniqueness is scoped to a single ``PathAndFillManager`` instance**, e.g., all the Trees of a running SNT session, or all the Trees parsed from one multi-tree reconstruction file. It is *not* guaranteed across independently-created Trees: each standalone parse (a call to ``fromFile(String)``, or each individual file visited by ``listFromFile(String)``/``listFromDir(String)``) gets its own manager with its own ID sequence starting from scratch, so two such Trees - even from the same ``listFromDir()`` call - may share the same ID. Once a Tree is merged into a live manager (e.g., via ``PathAndFillManager.addTree(Tree)``), its paths are assigned fresh, unique, collision-free IDs scoped to that manager; any IDs from the Tree's original source file are discarded.


.. py:method:: is3D()

   Assesses whether this Tree has depth.


.. py:method:: isAnnotated()

   Checks if the nodes of this Tree have been assigned `BrainAnnotation`s (neuropil labels).


.. py:method:: isEmpty()

   Checks if this Tree is empty.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setBoundingBox(BoundingBox)

   Associates a bounding box to this tree.


.. py:method:: setColor(ColorRGB)

   Assigns a color to all the paths in this tree. Note that assigning a non-null color will remove node colors from Paths.


.. py:method:: setLabel(String)

   Sets an identifying label for this Tree.


.. py:method:: setRadii(double)

   Assigns a fixed radius to all the nodes in this tree.


.. py:method:: setSWCType(String)

   Assigns an SWC type label to all the Paths in this Tree.


.. py:method:: setType(int)

   Assigns an SWC type label to all the Paths in this Tree.


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: show()

   Displays this Tree in an appropriate viewer (3D if the tree has depth, 2D otherwise).


.. py:method:: show2D()

   Displays this Tree in Viewer2D.


.. py:method:: show3D()

   Displays this Tree in Viewer3D.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: fromFile(String)

   Script-friendly method for loading a Tree from a reconstruction file.


.. py:method:: listFromDir(String)

   Retrieves a list of `Tree`s from reconstruction files stored in a common directory matching the specified criteria.


.. py:method:: listFromFile(String)

   Retrieves a list of `Tree`s from a single file.


.. py:method:: save(String)

   Saves this Tree to a .TRACES (XML, compressed) file.


.. py:method:: saveAsSWC(String)

   Saves this Tree to an SWC file.


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(Path)

   Adds a new Path to this Tree.


.. py:method:: applyCanvasOffset(double, double, double)

   Specifies the offset to be used when rendering this Tree in a ``TracerCanvas``. Path coordinates remain unaltered.


.. py:method:: applyProperties(Tree)

   Applies properties from another Tree to this Tree.


.. py:method:: applyZCorrection(double)

   Applies a Z-shrinkage correction to all nodes in this tree. This is typically used to compensate for tissue compression along the Z-axis during histological processing or mounting (e.g., paraffin embedding, cryosectioning). The correction factor is the ratio of the actual (cut) thickness to the measured (mounted) thickness.


.. py:method:: assignImage(Dataset)

   Assigns spatial calibration from an ImgPlus to this Tree.


.. py:method:: assignUniqueColors(Collection)

   


.. py:method:: assignValue(double)

   Assigns a numeric property to this Tree.


.. py:method:: downSample(double)

   


.. py:method:: downsample(double)

   Downsamples the tree, i.e., reduces the density of its nodes by increasing internode spacing.

   Note that 1) upsampling is not supported (cf. ``Path.upsample(double)``), and 2) the position of nodes at branch points and tips remains unaltered during downsampling, as per ``Path.downsample(double)``.


.. py:method:: fitRadii(ImagePlus)

   Fits radii to all paths in this Tree by fitting circular cross-sections to the image signal. Paths are fitted in parallel; results are applied sequentially. This is the scripting equivalent of the UI's "Fit Paths" action. Node positions are not modified; only radii and tangent vectors are computed.


.. py:method:: indexOf(Path)

   Returns the index of the specified Path in this Tree.


.. py:method:: list()

   Gets all the paths from this tree.


.. py:method:: merge(Tree)

   Appends all paths of a specified ``Tree`` to this one.


.. py:method:: rebuildGraph()

   Re-assembles the DirectedGraph object returned by ``getGraph()`` ensuring that no untracked changes exist. Usually, calling this method is not necessary since most changes to this Tree percolate to its graph representation.


.. py:method:: remove(Path)

   Removes a path from this tree.


.. py:method:: replaceAll(List)

   Replaces all Paths in this Tree.


.. py:method:: rotate(int, double)

   Rotates the tree.


.. py:method:: scale(double, double, double)

   Scales the tree by the specified factors.


.. py:method:: size()

   Retrieves the number of paths in this tree.


.. py:method:: skeletonize(ImagePlus, int)

   Skeletonizes (rasterizes) this tree on the specified image using Bresenham’s Algorithm (3D).


.. py:method:: subTree(String[])

   Extracts the subset of paths matching the specified criteria.


.. py:method:: swapAxes(int, int)

   Swaps the coordinates of two axes in this Tree.


.. py:method:: transform(String)

   Transforms a collection of trees using standardized flags.


.. py:method:: translate(double, double, double)

   Translates the tree by the specified offset.


.. py:method:: upsample(double)

   Downsamples the tree, i.e., increases the density of its nodes by decreasing internode spacing.

   The upscaling will include all the original nodes plus additional interpolated nodes placed at regular intervals between them, approximately equal to the specified distance. The original nodes are preserved in the upsampled tree. If the distance between two adjacent original nodes is less than the specified pacing, no additional nodes are added between them.


.. py:method:: validSoma()

   Checks whether this Tree has a valid soma annotation, i.e., a single primary path tagged with ``Path.SWC_SOMA``.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.Tree>`_
* `Tree JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/Tree.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
