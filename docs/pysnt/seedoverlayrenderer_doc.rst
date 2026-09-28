
``SeedOverlayRenderer`` Class Documentation
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

Stateless renderer that draws a SeedOverlay's seeds onto a TracerCanvas's Graphics2D. Invoked from `TracerCanvas.drawOverlay(Graphics2D)` after paths are drawn so seeds appear on top.

Visual conventions:

Color is looked up from the overlay's active ColorTable using the seed's confidence normalized to [low, high]. Seeds outside that range are not drawn. Radius on screen is the seed's physical radius converted to voxels (using the active image's in-plane spacing) and then to canvas pixels via the current magnification. A small floor is applied so high-zoom-out seeds remain clickable. Alpha falls off with distance from the current depth slice (per-plane); seeds outside the canvas's eitherSide band (when just_near_slices is on) are skipped. Seeds whose 2D projection falls outside the visible canvas rectangle are skipped (the dominant performance optimization when the user is zoomed in). When the visible post-cull set exceeds SUBSAMPLE_RENDER_CAP, only the top-K seeds by confidence are drawn (full set remains available for queries).


Methods
-------


Other Methods
~~~~~~~~~~~~~


.. py:method:: static colorForSeed(ColorTable, Color, SeedOverlay$ColorMode, SeedPoint, double, double, double, Map, Map)

   Dispatches to the per-mode color computation. CONFIDENCE keeps the legacy confidence-position behaviour (alpha rides on confidence); INDEX / TYPE / SOURCE use a categorical key and full opacity so every seed contributes equal visual weight.

Public so that non-canvas consumers (e.g. the Seeds table's swatch column) can compute the exact same color a seed would receive on the canvas, ensuring row⇄canvas correspondence is visually identical. Stateless: pass depthFalloff = 1.0 when there's no slice-distance concept (table rows have no Z).


See Also
--------

* `Package API <../api_auto/pysnt.html#pysnt.SeedOverlayRenderer>`_
* `SeedOverlayRenderer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SeedOverlayRenderer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
