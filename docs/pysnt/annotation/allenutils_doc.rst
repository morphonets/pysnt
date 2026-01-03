
``AllenUtils`` Class Documentation
===============================


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

Utility methods for accessing/handling AllenCompartments


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getAnatomicalPlane(String)

   Retrieves the anatomical plane matching the specified cartesian plane.


.. py:method:: static getAxisDefiningSagittalPlane()

   Gets the axis defining the sagittal plane.


.. py:method:: static getCartesianPlane(String)

   Retrieves the Cartesian plane matching the specified anatomical plane.


.. py:method:: static getCompartment(String)

   Constructs a compartment from its CCF name or acronym


.. py:method:: static getHemisphere(Tree)

   Checks the hemisphere a neuron belongs to.


.. py:method:: static getHighestOntologyDepth()

   Gets the maximum number of ontology levels in the Allen CCF.


.. py:method:: static getOntologies()

   Gets a flat (non-hierarchical) list of all the compartments of the specified ontology depth.


.. py:method:: static getRootMesh(ColorRGB)

   Retrieves the surface contours for the Allen Mouse Brain Atlas (CCF), bundled with SNT.


.. py:method:: static getTreeModel(boolean)

   Retrieves the Allen CCF hierarchical tree data.


.. py:method:: static getXYZLabels()

   


.. py:method:: static isLeftHemisphere(double, double, double)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: static assignAnnotationsFromNodeValues(Tree)

   Assigns brain annotations (interpreted as CCF IDs) to node values for all paths in a Tree.

This method is the inverse operation of `transferAnnotationIdsToNodeValues(Tree)`.


.. py:method:: static assignHemisphereTags(DirectedWeightedGraph)

   


.. py:method:: static assignToLeftHemisphere(Tree)

   Assigns a tree to the left hemisphere by mirroring it if necessary.


.. py:method:: static assignToRightHemisphere(Tree)

   Assigns a tree to the right hemisphere by mirroring it if necessary.


.. py:method:: static brainCenter()

   Returns the spatial centroid of the Allen CCF.


.. py:method:: static main(String;)

   


.. py:method:: static splitByHemisphere(DirectedWeightedGraph)

   


.. py:method:: static transferAnnotationIdsToNodeValues(Tree)

   Transfers brain annotation IDs to node values for all paths in a Tree.

This is useful for preserving annotation information when saving data to TRACES files. Note that this method overwrites any existing node values. Nodes without annotations (null) are assigned BRAIN_ROOT_ID.


See Also
--------

* `Package API <../api_auto/pysnt.annotation.html#pysnt.annotation.AllenUtils>`_
* `AllenUtils JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/annotation/AllenUtils.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
