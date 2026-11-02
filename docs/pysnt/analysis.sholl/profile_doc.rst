
``Profile`` Class Documentation
============================


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


**Package:** ``sc.fiji.snt.analysis.sholl``

Enhanced documentation for Profile class.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCountAtRadius(double)

   


.. py:method:: getExtraMeasurement()

   


.. py:method:: getProperties()

   


.. py:method:: getROIs()

   


.. py:method:: hasExtraMeasurement()

   


.. py:method:: hasPoints()

   


.. py:method:: hashCode()

   


.. py:method:: is2D()

   


.. py:method:: isEmpty()

   


.. py:method:: isIntDensityProfile()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setCenter(ShollPoint)

   


.. py:method:: setExtraMeasurement(String, String)

   


.. py:method:: setIdentifier(String)

   


.. py:method:: setIsIntDensityProfile(boolean)

   


.. py:method:: setNDimensions(int)

   


.. py:method:: setProperties(Properties)

   


.. py:method:: setSpatialCalibration(Calibration)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: plot()

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: add(ProfileEntry)

   


.. py:method:: assignImage(ImagePlus)

   


.. py:method:: center()

   


.. py:method:: counts()

   


.. py:method:: countsAsArray()

   


.. py:method:: duplicate()

   


.. py:method:: endRadius()

   


.. py:method:: entries()

   


.. py:method:: equals(Object)

   


.. py:method:: extras()

   


.. py:method:: identifier()

   


.. py:method:: lengths()

   


.. py:method:: lengthsAsArray()

   


.. py:method:: nDimensions()

   


.. py:method:: points()

   


.. py:method:: radii()

   


.. py:method:: radiiAsArray()

   


.. py:method:: radiiSquared()

   


.. py:method:: scale(double, double, double)

   


.. py:method:: scaled()

   


.. py:method:: size()

   


.. py:method:: source()

   


.. py:method:: spatialCalibration()

   


.. py:method:: startRadius()

   


.. py:method:: stepSize()

   


.. py:method:: toString()

   


.. py:method:: trimNaNCounts()

   


.. py:method:: trimZeroCounts()

   


.. py:method:: zeroCounts()

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.sholl.html#pysnt.analysis.sholl.Profile>`_
* `Profile JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/Profile.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
