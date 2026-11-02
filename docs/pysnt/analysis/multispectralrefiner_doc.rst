
``MultiSpectralRefiner`` Class Documentation
=========================================


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

Post-hoc refinement of traced paths in multispectral (e.g., Brainbow) images.

For each path, the algorithm computes a reference color vector (the average intensity across all channels at each node), then iteratively adjusts node positions and radii to minimize a cost function combining:

#. **Intensity penalty** fraction of voxels in the node's sphere whose total intensity falls outside the expected range

#. **Color penalty** fraction of voxels whose spectral angle (cosine similarity) to the reference color vector is below threshold

#. **Radius penalty** ``1/r²`` , favoring compact cross-sections

This is an SNT-native re-implementation of the nCorrect algorithm described in:

Azzouz, S et al., "Optimized Neuron Tracing Using Post Hoc Reanalysis." doi:10.1101/2022.10.10.511642

The minimum path-length quality gate is informed by:

Leiwe et al., "Automated neuronal reconstruction with super-multicolour Tetbow labelling and threshold-based clustering of colour hues", *Nat Commun* 15, 5279 (2024). doi:10.1038/s41467-024-49455-y

Like ``PathFitter``, each instance operates on a single ``Path``. ``call()`` is thread-safe for parallel execution; ``apply()`` must be called sequentially to commit results back to the original path.


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getFinalNodeCosts()

   Returns the per-node cost values after refinement. Only valid after ``call()`` has been invoked.


.. py:method:: getFinalPenalty()

   Returns the total penalty of the path after refinement. Only valid after ``call()`` has been invoked.


.. py:method:: getInitialNodeCosts()

   Returns the per-node cost values before refinement. Only valid after ``call()`` has been invoked.


.. py:method:: getInitialPenalty()

   Returns the total penalty of the path before refinement. Only valid after ``call()`` has been invoked.


Setters Methods
~~~~~~~~~~~~~~~


.. py:method:: setAutoTune(boolean)

   Enables automatic parameter tuning from path and image statistics. When enabled, ``call()`` will adjust ``maxRadius``, ``cosSimilarityThreshold``, and intensity thresholds based on the actual data before running the optimization loop.


.. py:method:: setBackgroundThreshold(double)

   Sets the background fraction threshold. If more than this fraction of voxels in a node's sphere fail the intensity test, the node is considered to be in the background.


.. py:method:: setColorWeight(double)

   Sets the weight for the color (cosine similarity) penalty term.


.. py:method:: setConvergenceThreshold(double)

   Sets the convergence threshold for the refinement loop. The loop stops when the relative improvement per iteration falls below this fraction (e.g., 0.001 = stop when improvement is less than 0.1% of total penalty).


.. py:method:: setCosSimilarityThreshold(double)

   Sets the cosine similarity threshold below which a voxel is considered spectrally dissimilar to the reference color.


.. py:method:: setIntensityRange(double, double)

   Sets the intensity range for adaptive percent-C computation.


.. py:method:: setIntensityWeight(double)

   Sets the weight for the intensity background penalty term.


.. py:method:: setMaxIterations(int)

   Sets the maximum number of iterations for the refinement loop. The loop also stops early if convergence is reached.


.. py:method:: setMaxRadius(int)

   Sets the maximum radius (in pixels) to test during radius optimization.


.. py:method:: setPercentCRange(double, double)

   Sets the percent-C range for adaptive intensity tolerance.


.. py:method:: setRadiusWeight(double)

   Sets the weight for the radius expansion penalty term.


.. py:method:: setReferenceWindowRadius(int)

   Sets the sliding-window radius for per-node reference color computation. When enabled, each node's reference color is the average of the ±N neighboring nodes along the path, rather than a single global average. This handles color drift along long axons in Brainbow images.


Analysis Methods
~~~~~~~~~~~~~~~~


.. py:method:: computeNodeCosts(ImagePlus, Path)

   Computes the cost at each node of a path without modifying it, where the path's node coordinates and imp's own pixel grid are related by a fixed offset. See ``MultiSpectralRefiner(ImagePlus, Path, double, double, double)``.


I/O Operations Methods
~~~~~~~~~~~~~~~~~~~~~~


.. py:method:: readPreferences()

   Reads stored preferences from ``MultiSpectralRefinerCmd`` and applies them to this refiner. If auto-intensity is enabled in the preferences, the auto-calibrated values from the constructor are preserved.


Other Methods
~~~~~~~~~~~~~


.. py:method:: apply()

   Applies the refinement result to the original path by replacing all its nodes with the refined geometry. This preserves hierarchical relationships (parent, children, connections) via ``Path.replaceNodes(Path)``. Must be called sequentially (not thread-safe).


.. py:method:: applySettings(MultiSpectralRefiner)

   Applies all settings from another refiner to this one. Useful for batch operations where a reference refiner holds the user-configured parameters.


.. py:method:: call()

   Runs the multispectral refinement on this path. Thread-safe: does not modify the original path. Call ``apply()`` afterward (sequentially) to commit results.


.. py:method:: refineTree(ImagePlus, Tree)

   Refines all paths in a tree with custom parameters, where the tree's node coordinates and imp's own pixel grid are related by a fixed offset. See ``MultiSpectralRefiner(ImagePlus, Path, double, double, double)``.


.. py:method:: succeeded()

   Whether the refinement succeeded (penalty decreased or path was already optimal).


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.MultiSpectralRefiner>`_
* `MultiSpectralRefiner JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/MultiSpectralRefiner.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
