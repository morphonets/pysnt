
``CurationManager`` Class Documentation
====================================


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

Implements the *Curation Assistant* pane in SNT's UI. Provides morphological plausibility feedback during tracing and editing operations.

The panel is organized into:

- **Live Monitoring Parameters** configures checks that run inline during interactive tracing (fork, segment, finalization hooks).

- **On-demand Monitoring Parameters** configures heavier checks that scan the full reconstruction.

- **Action buttons** toggle live monitoring on/off, or trigger a full on-demand scan (which runs *both* parameter sets across all paths).

- **Warnings table** displays current issues; double-click to navigate to the issue location.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getPanel()

   Builds and returns the panel to be added as a tab in SNTUI.


.. py:method:: getStatusSummary()

   Generates a summary string for the status bar: shows the most severe warning, suitable for display in the QUERY_KEEP status text.


Other Methods
~~~~~~~~~~~~~


.. py:method:: addWarnings(List)

   Appends warnings to the table without replacing existing ones. Used by external producers that want to inject items into the warnings log alongside the ones already produced by the live/deep checks. The severity filter is re-applied automatically; entries whose severity is currently hidden are accepted into the underlying list but stay invisible until the user re-enables their severity in the toolbar.


.. py:method:: calibrateFromTrees(List)

   Calibrates thresholds from the given in-memory trees, enables live monitoring, runs a full scan, and switches SNTUI to the Assistant tab. Intended to be called programmatically after autotracing completes.


.. py:method:: dispose()

   Unregisters this panel from the monitor. Should be called when the panel is removed from the UI to avoid listener leaks.


.. py:method:: refreshFromMonitor()

   Refreshes all UI controls (spinners, checkboxes, toggle) from the monitor's current state. Called after loading a preset or restoring a session.


.. py:method:: severityColor(Severity)

   


.. py:method:: warningsUpdated(List)

   Description copied from interface: ``PlausibilityMonitor.WarningListener``


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.CurationManager>`_
* `CurationManager JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/CurationManager.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
