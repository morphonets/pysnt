
``SciViewSNT`` Class Documentation
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


**Package:** ``sc.fiji.snt``

Bridges SNT to SciView, allowing Trees to be rendered as scenery objects


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getSciView()

   Gets the SciView instance currently in use.


.. py:method:: getTreeAsSceneryNode(Tree)

   Gets the specified Tree as a Scenery Node.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setSciView(SciView)

   Sets the SciView to be used.


Other Methods
~~~~~~~~~~~~~


.. py:method:: addTree(Tree)

   Adds a tree to the associated SciView instance. A new SciView instance is automatically instantiated if setSciView(SciView) has not been called.


.. py:method:: static main(String;)

   


.. py:method:: removeTree(Tree)

   Removes the specified Tree.


.. py:method:: syncPathManagerList()

   (Re)loads the current list of Paths in the Path Manager list.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SciViewSNT>`_
* `SciViewSNT JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SciViewSNT.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
