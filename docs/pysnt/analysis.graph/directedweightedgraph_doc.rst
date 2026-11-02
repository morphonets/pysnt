
``DirectedWeightedGraph`` Class Documentation
==========================================


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


**Package:** ``sc.fiji.snt.analysis.graph``

Enhanced documentation for DirectedWeightedGraph class.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBPs()

   


.. py:method:: getBreadthFirstIterator()

   


.. py:method:: getComponents()

   


.. py:method:: getDepthFirstIterator()

   


.. py:method:: getEdgeColor(DefaultWeightedEdge)

   


.. py:method:: getEdgeColorRGBMap()

   


.. py:method:: getLongestPath(boolean)

   


.. py:method:: getLongestPathVertices(boolean)

   


.. py:method:: getNodeStatistics()

   


.. py:method:: getNodesFromLeavesToRoot()

   


.. py:method:: getNodesFromRootToLeaves()

   


.. py:method:: getRoot()

   


.. py:method:: getShortestPath(SWCPoint, SWCPoint)

   


.. py:method:: getShortestPathVertices(SWCPoint, SWCPoint)

   


.. py:method:: getSimplifiedGraph()

   


.. py:method:: getSubgraph(Set)

   


.. py:method:: getTips()

   


.. py:method:: getTopologicalOrderIterator()

   


.. py:method:: getTree()

   


.. py:method:: getTreeWithSamePathStructure()

   


.. py:method:: getTrees()

   


.. py:method:: getVertexColor(Object)

   


.. py:method:: getVertexColorRGBMap()

   


.. py:method:: getVertexValue(Object)

   


.. py:method:: getVertexValueMap()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setEdgeColor(DefaultWeightedEdge, ColorRGB)

   


.. py:method:: setRoot(SWCPoint)

   


.. py:method:: setVertexColor(Object, ColorRGB)

   


.. py:method:: setVertexValue(Object, double)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: show()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addVertex(double, double, double)

   


.. py:method:: applyEdges(UnaryOperator)

   


.. py:method:: applyVertices(UnaryOperator)

   


.. py:method:: assignEdgeWeightsEuclidean()

   


.. py:method:: filterEdges(Predicate)

   


.. py:method:: filterVertices(Predicate)

   


.. py:method:: scale(double, double, double, boolean)

   


.. py:method:: sumEdgeWeights()

   


.. py:method:: updateVertexProperties()

   


.. py:method:: vertexSet(char)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.graph.html#pysnt.analysis.graph.DirectedWeightedGraph>`_
* `DirectedWeightedGraph JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/graph/DirectedWeightedGraph.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
