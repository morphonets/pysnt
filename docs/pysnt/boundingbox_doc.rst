
``BoundingBox`` Class Documentation
================================


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


**Package:** ``sc.fiji.snt.util``

A BoundingBox contains information (including spatial calibration) of a tracing canvas bounding box, i.e., the minimum bounding cuboid containing all nodes (SNTPoints) of a reconstructed structure.


Fields
------


**info** : ``str``
    No description available.


**xSpacing** : ``float``
    No description available.


**ySpacing** : ``float``
    No description available.


**zSpacing** : ``float``
    No description available.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: clone()

   Creates a copy of this BoundingBox.


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCalibration()

   Creates a Calibration object using information from this BoundingBox


.. py:method:: getCentroid()

   


.. py:method:: getDiagonal()

   Gets the box diagonal


.. py:method:: getDimensions()

   Gets this BoundingBox dimensions.


.. py:method:: getUnit()

   Gets the length unit of voxel spacing


.. py:method:: hasDimensions()

   


.. py:method:: isScaled()

   Checks whether this BoundingBox is spatially calibrated, i.e., if voxel spacing has been specified


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setDimensions(long, long, long)

   Sets the dimensions of this bounding box using uncalibrated (pixel) lengths.


.. py:method:: setOrigin(PointInImage)

   Sets the origin for this box, i.e., its (xMin, yMin, zMin) vertex.


.. py:method:: setOriginOpposite(PointInImage)

   Sets the origin opposite for this box, i.e., its (xMax, yMax, zMax) vertex.


.. py:method:: setSpacing(double, double, double, String)

   Sets the voxel spacing.


.. py:method:: setUnit(String)

   Sets the default length unit for voxel spacing (typically um, for SWC reconstructions)


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: compute(Iterator)

   Computes a new positioning so that this box encloses the specified point cloud.


Other Methods
~~~~~~~~~~~~~


.. py:method:: append(Iterator)

   Computes the bounding box of the specified point cloud and appends it to this bounding box, resizing it as needed.


.. py:method:: combine(BoundingBox)

   Combines this bounding box with another one. It is assumed both boxes share the same voxel spacing/Calibration.


.. py:method:: contains(BoundingBox)

   


.. py:method:: contains2D(SNTPoint)

   


.. py:method:: depth()

   


.. py:method:: height()

   


.. py:method:: inferSpacing(Collection)

   Infers the voxel spacing of this box from the inter-node distances of a Collection of SWCPoints.


.. py:method:: intersection(BoundingBox)

   Retrieves the intersection cuboid between this bounding with another bounding box. It is assumed both boxes share the same voxel spacing/Calibration.


.. py:method:: origin()

   Retrieves the origin of this box.


.. py:method:: originOpposite()

   Retrieves the origin opposite of this box.


.. py:method:: toBoundingBox3d()

   


.. py:method:: unscaledOrigin()

   Retrieves the origin of this box in unscaled ("pixel" units)


.. py:method:: unscaledOriginOpposite()

   Retrieves the origin opposite of this box in unscaled ("pixel" units)


.. py:method:: width()

   


See Also
--------

* `Package API <../api_auto/pysnt.util.html#pysnt.util.BoundingBox>`_
* `BoundingBox JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/BoundingBox.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
