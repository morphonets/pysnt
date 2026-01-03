
``MouseLightQuerier`` Class Documentation
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

Importer for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.janelia.org


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getAllIDs()

   Gets all available neuron IDs from the database.


.. py:method:: static getIDs(String, boolean)

   Gets neuron IDs matching the specified collection of IDs or DOIs.


.. py:method:: static getNeuronCount()

   Gets the number of cells publicly available in the MouseLight database.


.. py:method:: static isDatabaseAvailable()

   Checks whether a connection to the MouseLight database can be established.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: static setCCFVersion(String)

   Sets the version of the Common Coordinate Framework to be used by the Querier.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.io.html#pysnt.io.MouseLightQuerier>`_
* `MouseLightQuerier JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/MouseLightQuerier.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
