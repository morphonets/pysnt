
``BvvMultiSource`` Class Documentation
===================================


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


**Package:** ``sc.fiji.snt.viewer``

A group of BvvSource objects that are treated as a logical unit: display properties (color, range, active state) and manual transforms applied to the leader source are propagated to all follower sources.

This is particularly useful for:

Multichannel images where each channel is a separate BVV source but should move together during manual registration (press T in BVV to enter manual transform mode). Multi-image workflows where multiple volumes must be grouped and manipulated as one.

Transform synchronization is achieved by making all follower TransformedSources share the leader's fixedTransform and incrementalTransform field objects via reflection. This means any transform applied to the leader, including live T-mode (press T) dragging: It is immediately visible on all followers with no listener overhead. If reflection fails, a `renderTransformListeners` fallback is used.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getFollowers()

   


.. py:method:: getLeader()

   


.. py:method:: getLeaderTransform(AffineTransform3D)

   Returns a copy of the most recently cached leader fixed transform.


.. py:method:: getSources()

   


.. py:method:: isLiveSync()

   


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setActive(boolean)

   Sets the active/visible state for all sources in the group.


.. py:method:: setColor(ARGBType)

   Sets the color for all sources in the group.


.. py:method:: setDisplayRange(double, double)

   Sets the display range for all sources in the group.


.. py:method:: setLiveSync(boolean)

   Sets whether transforms are propagated to followers on every render frame (true) or only on explicit syncTransforms() calls (false).


Other Methods
~~~~~~~~~~~~~


.. py:method:: applyTransform(AffineTransform3D)

   Applies the given transform as the fixed transform to the leader and all followers. This is the primary entry point for loading a saved transform.


.. py:method:: removeFromBvv()

   Removes all sources in the group from the viewer.


.. py:method:: size()

   


.. py:method:: syncTransforms()

   Forces a repaint. With field-sharing active, followers already hold the same transform objects as the leader: this call just flushes the display. Called internally after transform commits in the fallback path.


See Also
--------

* `Package API <../api_auto/pysnt.viewer.html#pysnt.viewer.BvvMultiSource>`_
* `BvvMultiSource JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/BvvMultiSource.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
