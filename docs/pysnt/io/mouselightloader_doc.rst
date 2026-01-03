
``MouseLightLoader`` Class Documentation
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


**Package:** ``sc.fiji.snt.io``

Methods for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.janelia.org *


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: static getAllLoaders()

   Gets the loaders for all the cells publicly available in the MouseLight database.


.. py:method:: getDOI()

   Gets the DOI for this neuron.


.. py:method:: getID()

   Gets the neuron ID for this loader.


.. py:method:: getJSON()

   Gets all the data associated with this reconstruction as a JSON object.


.. py:method:: static getNeuronCount()

   Gets the number of cells publicly available in the MouseLight database.


.. py:method:: getNodes()

   Script-friendly method to extract the nodes of a cellular compartment.


.. py:method:: getSWC()

   Gets all the data associated with this reconstruction in the SWC format.


.. py:method:: getSampleInfo()

   Gets sample information for this neuron.


.. py:method:: getSomaCompartment()

   Gets the brain compartment containing the soma.


.. py:method:: getSomaLocation()

   Gets the soma location for this neuron.


.. py:method:: getTree()

   Script-friendly method to extract the entire neuron as a collection of Paths.


.. py:method:: static isDatabaseAvailable()

   Checks whether a connection to the MouseLight database can be established.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: save(String)

   Convenience method to save JSON data.


.. py:method:: saveAsJSON(String)

   Convenience method to save JSON data to a local directory.


.. py:method:: saveAsSWC(String)

   Convenience method to save SWC data to a local directory.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static demoTrees()

   Returns a collection of four demo reconstructions NB: Data is cached locally. No internet connection required.


.. py:method:: static extractNodes(File, String)

   Extracts reconstruction(s) from a JSON file.


.. py:method:: static extractTrees(InputStream, String)

   


.. py:method:: idExists()

   Checks if the neuron ID exists in the database.


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.io.html#pysnt.io.MouseLightLoader>`_
* `MouseLightLoader JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/MouseLightLoader.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
