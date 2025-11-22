
``InsectBrainLoader`` Class Documentation
======================================


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


**Package:** ``sc.fiji.snt.io``

Methods for retrieving reconstructions and annotations from the Insect Brain Database at insectbraindb.org *


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getAnnotations()

   Gets the brain compartment annotations for this neuron.


.. py:method:: getMeshes()

   Gets the 3D meshes associated with this neuron's brain compartments.


.. py:method:: getNeuronInfo()

   


.. py:method:: getTree()

   Gets the collection of Paths for the specified cell ID


.. py:method:: static isDatabaseAvailable()

   Checks whether a connection to the Insect Brain Database can be established.


Other Methods
~~~~~~~~~~~~~


.. py:method:: idExists()

   Checks whether the neuron to be loaded was found in the database.


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.io.html#pysnt.io.InsectBrainLoader>`_
* `InsectBrainLoader JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/InsectBrainLoader.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
