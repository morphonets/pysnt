
``DelineationsManager`` Class Documentation
========================================


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

Implements the *Delineation Analysis* pane.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: reset()

   Deletes all delineations.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getDelineationROIs()

   


.. py:method:: hasDelineationLabels(Collection)

   Checks if the given tree has any delineation labels.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: importFromLabelImage(ImagePlus)

   Convenience overload accepting an ``ImagePlus``, which is converted to an ``ImgPlus`` via ``ImpUtils.toImgPlus3D(ImagePlus, int, int)``.


.. py:method:: load(List)

   Loads delineations from a list of area ROIs. Each ROI is mapped to a delineation entry, and path nodes whose XY coordinates fall within the ROI are assigned to the corresponding delineation. If an ROI has been renamed or colored (stroke or fill), those properties are transferred to the delineation.


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.DelineationsManager>`_
* `DelineationsManager JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/DelineationsManager.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
