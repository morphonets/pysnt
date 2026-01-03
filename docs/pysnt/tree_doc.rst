
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

Utility class to access a Collection of Paths (typically a complete reconstruction). A Tree is the preferred way to group, access and manipulate Paths that share something in common, specially when scripting SNT. Note that a "Tree" here is literally a collection of Paths. Very few restrictions are imposed on its topology, although it is generally assumed that the Collection of paths describes a single-rooted structure with no loops.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clone()

   Creates a deep copy of this Tree.

This method creates a complete copy of the tree including all paths and their relationships. Each path is cloned individually, and then the parent-child relationships are reconstructed in the cloned tree. This ensures that the cloned tree maintains the same structure as the original while being completely independent.


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

   Gets the branch points (junctions) of the graph. This is simply an alias for `DirectedWeightedGraph.getBPs()`.


.. py:method:: getBoundingBox(boolean)

   Gets the bounding box associated with this tree.


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


```
getProperties().setProperty(Tree.KEY_SPATIAL_UNIT, "um");
String unit = getProperties().getProperty(Tree.KEY_SPATIAL_UNIT);
getProperties().setProperty(Tree.KEY_COMPARTMENT, Tree.DENDRITIC);
```



.. py:method:: getRoot()

   Gets the first node of the main primary path of this tree


.. py:method:: static getSWCTypeMap()

   Returns the SWC Type flags used by SNT.


.. py:method:: getSWCTypeNames(boolean)

   Gets the set of SWC type labels present in this tree with optional soma inclusion in a readable form.


.. py:method:: getSWCTypes(boolean)

   Gets the set of SWC types present in this tree with optional soma inclusion.


.. py:method:: getSkeleton()

   Retrieves the rasterized skeleton of this tree at 1:1 scaling.


.. py:method:: getSkeleton2D(int)

   Retrieves a 2D projection of the rasterized skeleton of this tree at 1:1 scaling.


.. py:method:: getSomaNodes()

   Gets the list of all nodes tagged as Path.SWC_SOMA.


.. py:method:: getTips()

   Gets the end points (tips) of the graph. This is simply an alias for `DirectedWeightedGraph.getTips()`.


.. py:method:: is3D()

   Assesses whether this Tree has depth.


.. py:method:: isAnnotated()

   Checks if the nodes of this Tree have been assigned BrainAnnotations (neuropil labels).


.. py:method:: isEmpty()

   Checks if this Tree is empty.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: static fromFile(String)

   Script-friendly method for loading a Tree from a reconstruction file.


.. py:method:: static listFromDir(String, String, String;)

   Retrieves a list of Trees from reconstruction files stored in a common directory matching the specified criteria.


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(Path)

   Adds a new Path to this Tree.


.. py:method:: applyCanvasOffset(double, double, double)

   Specifies the offset to be used when rendering this Tree in a TracerCanvas. Path coordinates remain unaltered.


.. py:method:: applyProperties(Tree)

   Applies properties from another Tree to this Tree.


.. py:method:: assignImage(Dataset)

   Assigns spatial calibration from a Dataset to this Tree.


.. py:method:: static assignUniqueColors(Collection)

   Assigns distinct colors to a collection of Trees.


.. py:method:: assignValue(double)

   Assigns a numeric property to this Tree.


.. py:method:: downSample(double)

   


.. py:method:: downsample(double)

   Downsamples the tree, i.e., reduces the density of its nodes by increasing internode spacing.

Note that 1) upsampling is not supported (cf. {upsample(double)}, and 2) the position of nodes at branch points and tips remains unaltered during downsampling, as per `Path.downsample(double)`.


.. py:method:: indexOf(Path)

   Returns the index of the specified Path in this Tree.


.. py:method:: list()

   Gets all the paths from this tree.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.Tree>`_
* `Tree JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/Tree.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
