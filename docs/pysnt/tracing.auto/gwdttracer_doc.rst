
``GWDTTracer`` Class Documentation
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


**Package:** ``sc.fiji.snt.tracing.auto``

Enhanced documentation for GWDTTracer class.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getCaliperFraction()

   


.. py:method:: getMaxGapVoxels()

   


.. py:method:: getMinSomaDistance()

   


.. py:method:: getNSomas()

   


.. py:method:: getRootStrategy()

   


.. py:method:: getScoreMap()

   


.. py:method:: getSomaRoi()

   


.. py:method:: getTipExtensionDistance()

   


.. py:method:: getTracedRegionBuffer()

   


.. py:method:: isAllowVoxelGap()

   


.. py:method:: isAutoFilter()

   


.. py:method:: isParallelBranchPruneEnabled()

   


.. py:method:: isPathFittingEnabled()

   


.. py:method:: isVerbose()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAllowVoxelGap(boolean)

   


.. py:method:: setAutoFilter(boolean)

   


.. py:method:: setBackgroundThreshold(double)

   


.. py:method:: setBranchTuneMaxAngle(double)

   


.. py:method:: setCaliperFraction(double)

   


.. py:method:: setConnectivityType(int)

   


.. py:method:: setJointLeafPruneEnabled(boolean)

   


.. py:method:: setLeafPruneOverlap(double)

   


.. py:method:: setMaxGapVoxels(int)

   


.. py:method:: setMinBranchIntensityLength(double)

   


.. py:method:: setMinSegmentLength(double)

   


.. py:method:: setMinSegmentLengthVoxels(double)

   


.. py:method:: setMinSomaDistance(double)

   


.. py:method:: setNSomas(int)

   


.. py:method:: setOvershootRemovalEnabled(boolean)

   


.. py:method:: setParallelBranchPruneEnabled(boolean)

   


.. py:method:: setPathFittingEnabled(boolean)

   


.. py:method:: setResampleStep(double)

   


.. py:method:: setRoots(Collection)

   


.. py:method:: setScoreMap(RandomAccessibleInterval)

   


.. py:method:: setScoreMapEnabled(boolean)

   


.. py:method:: setScoreMapFilterType(FilterType)

   


.. py:method:: setScoreMapPruneThreshold(double)

   


.. py:method:: setScoreMapScales(double[])

   


.. py:method:: setSeed(long[])

   


.. py:method:: setSeedPhysical(double[])

   


.. py:method:: setSmoothWindowSize(int)

   


.. py:method:: setSomaRoi(Roi)

   


.. py:method:: setSomaRoiZPosition(int)

   


.. py:method:: setSphereOverlapThreshold(double)

   


.. py:method:: setSrRatio(double)

   


.. py:method:: setStatusListener(Consumer)

   


.. py:method:: setTipExtensionDistance(double)

   


.. py:method:: setTips(Collection)

   


.. py:method:: setTracedRegionBuffer(int)

   


.. py:method:: setVerbose(boolean)

   


.. py:method:: setWaypointBiasFixedFactor(double)

   


.. py:method:: setWaypointBiasRadiusVoxels(double)

   


.. py:method:: setWaypointBiasSource(WaypointBiasSource)

   


.. py:method:: setWaypointBiasStrength(double)

   


.. py:method:: setWaypoints(Collection)

   


.. py:method:: setZigzagRemovalEnabled(boolean)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: create(ImagePlus)

   


.. py:method:: findRoot(RandomAccessibleInterval, double[])

   


.. py:method:: findRootPhysical(RandomAccessibleInterval, double[])

   


.. py:method:: findThickestPoint(RandomAccessibleInterval, double, double[])

   


.. py:method:: findThickestPointPhysical(RandomAccessibleInterval, double, double[])

   


.. py:method:: honoredSeedRoles()

   


.. py:method:: iterateNeighbors(int[], int, int, Runnable)

   


.. py:method:: main(String[])

   


.. py:method:: posToIndex(long[], long[])

   


.. py:method:: trace()

   


.. py:method:: traceMultiSoma(List)

   


.. py:method:: traceToGraph()

   


.. py:method:: traceTrees()

   


See Also
--------

* `Package API <../api_auto/pysnt.tracing.auto.html#pysnt.tracing.auto.GWDTTracer>`_
* `GWDTTracer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/auto/GWDTTracer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
