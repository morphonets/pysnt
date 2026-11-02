
``SNTChart`` Class Documentation
=============================


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


**Package:** ``sc.fiji.snt.analysis``

Extension of ``ChartPanel`` modified for scientific publications and convenience methods for plot annotations.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getDefaultDirectoryForSaveAs()

   


.. py:method:: getFrame()

   


.. py:method:: getHistogram(SNTTable, boolean)

   Builds a single-series histogram from an array of values. The number of bins is chosen automatically (Freedman-Diaconis rule).


.. py:method:: getImage()

   Gets an ImagePlus representation of the chart.

   Creates an ImagePlus object containing a rasterized version of the chart at default scaling (1.0x).


.. py:method:: getImages(float)

   


.. py:method:: getPaintScaleLegend(String, ColorTable, double, double, int)

   


.. py:method:: getPolarHistogram(double[], String, String)

   Builds a single-series polar histogram from an array of values. The number of bins is chosen automatically (Freedman-Diaconis rule).


.. py:method:: getTitle()

   


.. py:method:: isCombined()

   Checks if this chart is part of a multi-panel montage


.. py:method:: isEqualized()

   Checks if the axes of the underlying XY plot are equalized.

   Returns true if both X and Y axes use the same scale.


.. py:method:: isGMMDistributionVisible()

   Gets whether the GMM distribution curve is being overlaid over histogram frequencies


.. py:method:: isGridlinesVisible()

   


.. py:method:: isLegendVisible()

   


.. py:method:: isNormDistributionVisible()

   Gets whether a normal distribution curve is being overlaid over histogram frequencies


.. py:method:: isOutlineVisible()

   Checks if the plot outline is visible.

   Returns true if the plot's border outline is currently visible.


.. py:method:: isQuartilesVisible()

   Gets whether quartile markers (Q1, Median, Q3) are being overlaid over histogram frequencies


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAxesVisible(boolean)

   Sets the visibility of chart axes.

   Controls whether the domain (X) and range (Y) axes are visible in the chart. This affects both XY plots and category plots.


.. py:method:: setChartTitle(String)

   


.. py:method:: setColors(ColorTable)

   (Re)colors existing dataset series. Unlike ``setColors(String...)``, only the series fill is touched: outline/item-label paint is left alone, since e.g. histogram bars rely on a fixed black/white outline (set independently of series color, see ``AnalysisUtils``) for the margin between adjacent bars


.. py:method:: setDefaultFontScale(double)

   


.. py:method:: setEqualizeAxes(boolean)

   Sets whether the axes of the underlying XY plot should be equalized (same scale).

   When enabled, both X and Y axes will use the same scale to maintain equal aspect ratio. When disabled, each axis maximizes its range.


.. py:method:: setFontSize(float)

   Sets the font size for this chart.


.. py:method:: setGMMFitVisible(boolean)

   Sets whether a GMM distribution curve should be overlaid over histogram frequencies.


.. py:method:: setGaussianFitVisible(boolean)

   Sets whether a normal distribution curve should be overlaid over histogram frequencies.


.. py:method:: setGridlinesVisible(boolean)

   


.. py:method:: setLegendVisible(boolean)

   


.. py:method:: setLineWidth(int)

   Changes the line width of all series in a XY plot


.. py:method:: setOutlineVisible(boolean)

   Sets the visibility of the plot outline.

   Controls whether the border outline around the plot area is visible.


.. py:method:: setQuartilesVisible(boolean)

   Sets whether quartile markers (Q1, Median, Q3) should be overlaid over histogram frequencies.


.. py:method:: setTitle(String)

   


.. py:method:: setVisible(boolean)

   


Visualization Methods
~~~~~~~~~~~~~~~~~~~~~


.. py:method:: show()

   


.. py:method:: showHeatmap(double[][], ColorTable, String[])

   Shows a two-dimensional heatmap from a two-dimensional data matrix, with rows/columns labeled categorically (e.g. class/check names) instead of by numeric coordinate. Cannot be called from event dispatcher thread.


.. py:method:: showHistogram3D(Collection, Collection, ColorTable, String[])

   Shows a bivariate histogram (two-dimensional histogram) from two DescriptiveStatistics objects. The number of bins is automatically determined using the Freedman-Diaconis rule.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: save(File)

   Saves this chart.


.. py:method:: saveAsPDF(String)

   


.. py:method:: saveAsPNG(File)

   


.. py:method:: saveAsSVG(String)

   


Other Methods
~~~~~~~~~~~~~


.. py:method:: addColorBarLegend(String, ColorTable, double, double, int)

   Adds a color bar legend (LUT ramp).


.. py:method:: addPolygon(Polygon2D, ColorRGB, ColorRGB)

   


.. py:method:: annotate(String)

   Adds a subtitle to the chart.


.. py:method:: annotateCategory(String, String)

   Annotates the specified category (Category plots only).


.. py:method:: annotatePoint(double, double, String)

   Highlights a point in a histogram/XY plot by drawing a labeled arrow at the specified location.


.. py:method:: annotateXline(double, String)

   Annotates the specified X-value (XY plots and histograms).


.. py:method:: annotateYline(double, String)

   Annotates the specified Y-value (XY plots and histograms).


.. py:method:: applyStyle(SNTChart)

   


.. py:method:: closeAll()

   Closes all open charts


.. py:method:: combine(Collection)

   Combines a collection of charts into a multipanel montage.


.. py:method:: combineAsImagePlus(Collection)

   Combines a collection of charts into a ImageJ1 stack.


.. py:method:: containsValidData()

   Checks if the chart contains valid data.

   Returns true if the chart object exists and presumably contains data that can be displayed.


.. py:method:: dispose()

   Disposes of this chart and releases its resources.

   Closes the chart window and removes it from the list of open instances. This method should be called when the chart is no longer needed to prevent memory leaks.


.. py:method:: openCharts()

   


.. py:method:: replace(SNTChart)

   Replaces the current chart with the specified instance


.. py:method:: shadeXRegion(double, double, String)

   Shades a region of the domain (X) axis as a background band.


.. py:method:: tile(Collection)

   Tiles specified charts displaying them on a grid. Charts's windows are made visible if not displayed.


.. py:method:: tileAll()

   Tiles all open charts displaying them on a grid. Charts's windows are made visible if not displayed.


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.SNTChart>`_
* `SNTChart JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SNTChart.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
