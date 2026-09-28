
``SeedManager`` Class Documentation
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


**Package:** ``sc.fiji.snt``

Reusable JPanel that controls a SeedOverlay: visibility, LUT, confidence range, transparency, counters, CSV import/export/clear, plus an inline JTable for browsing and editing individual seeds. Used as the content of SNTUI's "Seeds" tab. Multiple instances can coexist on the same SeedOverlay; each registers its own listener and synchronizes via the overlay (the data model is the source of truth).

Caller must invoke dispose() when the panel is removed from its parent so the overlay and table-model listeners are unregistered.


Methods
-------


Utilities Methods
~~~~~~~~~~~~~~~~~


.. py:method:: checkImage(Image, ImageObserver)

   


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: computeVisibleRect(Rectangle)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: action(Event, Object)

   


.. py:method:: add(Component, Object, int)

   


.. py:method:: addAncestorListener(AncestorListener)

   


.. py:method:: addComponentListener(ComponentListener)

   


.. py:method:: addContainerListener(ContainerListener)

   


.. py:method:: addFocusListener(FocusListener)

   


.. py:method:: addHierarchyBoundsListener(HierarchyBoundsListener)

   


.. py:method:: addHierarchyListener(HierarchyListener)

   


.. py:method:: addInputMethodListener(InputMethodListener)

   


.. py:method:: addKeyListener(KeyListener)

   


.. py:method:: addMouseListener(MouseListener)

   


.. py:method:: addMouseMotionListener(MouseMotionListener)

   


.. py:method:: addMouseWheelListener(MouseWheelListener)

   


.. py:method:: addNotify()

   


.. py:method:: addPropertyChangeListener(String, PropertyChangeListener)

   


.. py:method:: addVetoableChangeListener(VetoableChangeListener)

   


.. py:method:: applyComponentOrientation(ComponentOrientation)

   


.. py:method:: areFocusTraversalKeysSet(int)

   


.. py:method:: bounds()

   


.. py:method:: contains(int, int)

   


.. py:method:: countComponents()

   


.. py:method:: createImage(int, int)

   


.. py:method:: createToolTip()

   


.. py:method:: createVolatileImage(int, int, ImageCapabilities)

   


.. py:method:: deliverEvent(Event)

   


.. py:method:: disable()

   


.. py:method:: dispatchEvent(AWTEvent)

   


.. py:method:: dispose()

   Unregisters the overlay listener and the table-model listener, and closes the detached-table dialog if it's open. Idempotent.

Must be called when this panel is removed from its parent: `overlay.addListener(overlayListener)` pins this panel to the overlay's lifetime, so skipping dispose() leaks the panel and its table model until SNT shuts down.


.. py:method:: doLayout()

   


.. py:method:: enable()

   


.. py:method:: findComponentAt(int, int)

   


.. py:method:: firePropertyChange(String, char, char)

   


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SeedManager>`_
* `SeedManager JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SeedManager.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
