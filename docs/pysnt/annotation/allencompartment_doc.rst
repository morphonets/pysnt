
``AllenCompartment`` Class Documentation
=====================================


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


**Package:** ``sc.fiji.snt.annotation``

Defines an Allen Reference Atlas (ARA) [Allen Mouse Common Coordinate Framework] annotation. A Compartment is defined by either a UUID (as per MouseLight's database) or its unique integer identifier. To improve performance, a compartment's metadata (reference to its mesh, its aliases, etc.) are not loaded at initialization, but retrieved only when such getters are called.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAncestor(int)

   Gets the nth ancestor of this compartment.


.. py:method:: getAncestors()

   Gets the ancestor ontologies of this compartment as a flat (non-hierarchical) list.


.. py:method:: getChildren(int)

   Gets the child ontologies of this compartment as a flat (non-hierarchical) list.


.. py:method:: getMesh()

   


.. py:method:: getOntologyDepth()

   Gets the ontology depth of this compartment.


.. py:method:: getParent()

   Gets the parent of this compartment.


.. py:method:: getTreePath()

   Gets the tree path of this compartment. The TreePath is the list of parent compartments that uniquely identify this compartment in the ontologies hierarchical tree. The elements of the list are ordered with the root ('Whole Brain') as the first element of the list. In practice, this is equivalent to appending this compartment to the list returned by getAncestors().


.. py:method:: getUUID()

   


.. py:method:: isChildOf(BrainAnnotation)

   Assesses if this annotation is a child of a specified compartment.


.. py:method:: isMeshAvailable()

   Checks whether a mesh is known to be available for this compartment.


.. py:method:: isParentOf(BrainAnnotation)

   Assesses if this annotation is the parent of the specified compartment.


Other Methods
~~~~~~~~~~~~~


.. py:method:: acronym()

   


.. py:method:: aliases()

   


.. py:method:: color()

   


.. py:method:: id()

   


.. py:method:: includes(BrainAnnotation)

   


.. py:method:: static main(String;)

   


.. py:method:: name()

   


See Also
--------

* `Package API <../api_auto/pysnt.annotation.html#pysnt.annotation.AllenCompartment>`_
* `AllenCompartment JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/annotation/AllenCompartment.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
