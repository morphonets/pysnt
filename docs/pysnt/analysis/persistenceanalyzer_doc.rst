
``PersistenceAnalyzer`` Class Documentation
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


**Package:** ``sc.fiji.snt.analysis``

Performs persistent homology analysis on neuronal Trees.

This class implements the algorithm described in Kanari, L. et al. "A Topological Representation of Branching Neuronal Morphologies" (Neuroinformatics 16, 3–13, 2018) to extract topological features from neuronal morphologies.

Core Concepts

Filter Functions: Mathematical functions that assign scalar values to each node in the tree based on various morphological properties (distance from root, branch order, spatial coordinates, etc.).

Persistence Diagram: A collection of 2D points (birth, death) representing when topological features (branches) appear and disappear during a filtration process. Each point corresponds to a branch in the neuronal tree.

Persistence: The "lifespan" of a topological feature, calculated as death - birth. High persistence indicates morphologically significant branches, while low persistence may represent noise or minor branches.

Supported Filter Functions

Geodesic: Path distance from node to root along the tree structure Radial: Euclidean (straight-line) distance from node to root Centrifugal: Reverse Strahler number (branch order from tips) Path Order: SNT path order hierarchy X, Y, Z: Spatial coordinates for directional analysis

Usage Example 
```
// Create analyzer for a neuronal tree
PersistenceAnalyzer analyzer = new PersistenceAnalyzer(tree);

// Get persistence diagram using geodesic distance
List<List<Double>> diagram = analyzer.getDiagram("geodesic");

// Each inner list contains [birth, death] values
for (List<Double> pair : diagram) {
    double birth = pair.get(0);
    double death = pair.get(1);
    double persistence = death - birth;
    System.out.println("Branch: birth=" + birth + ", death=" + death + ", persistence=" + persistence);
}

// Get persistence landscape
double[] landscape = analyzer.getLandscape("geodesic", 5, 100);
```


Methods
-------


Getters Methods
~~~~~~~~~~~~~~~


.. py:method:: getBarcode(String)

   Gets the persistence barcode for the specified filter function.

The barcode is a simplified representation of the persistence diagram that contains only the persistence values (death - birth) for each topological feature, akin to a one-dimensional summary of branch significance.

Interpretation:

High values: Morphologically significant branches Low values: Minor branches or potential noise Distribution: The spread of values indicates branching complexity

Special Properties:

All values are non-negative (|death - birth|) For geodesic descriptor: sum of all values equals total cable length Number of values equals number of tips in the tree

Example Usage: 
```
List<Double> barcode = analyzer.getBarcode("geodesic");

// Find most significant branches
barcode.sort(Collections.reverseOrder());
System.out.println("Top 5 most persistent branches:");
for (int i = 0; i < Math.min(5, barcode.size()); i++) {
    System.out.println("Branch " + (i+1) + ": " + barcode.get(i));
}
```



.. py:method:: static getDescriptors()

   Gets a list of supported descriptor functions for persistence analysis.

Returns the string identifiers for all available filter functions that can be used with getDiagram(String), getBarcode(String), and other analysis methods. These descriptors are case-insensitive when used in method calls.


.. py:method:: getDiagram(String)

   Gets the persistence diagram for the specified filter function.

The persistence diagram is the core output of the analysis, consisting of birth-death pairs that represent the "lifespan" of topological features (branches) during the filtration process. Each point in the diagram corresponds to a branch in the neuronal tree.

Structure: Returns a list where each inner list contains exactly two values:

Birth [0]: The filter value where the branch appears (branch point) Death [1]: The filter value where the branch disappears (tip)

Properties:

Number of points = Number of tips in the tree All values are non-negative For geodesic descriptor: sum of all (death-birth) = total cable length High persistence (death-birth) indicates morphologically significant branches

Example usage: 
```
List<List<Double>> diagram = analyzer.getDiagram("geodesic");
for (List<Double> point : diagram) {
    double birth = point.get(0);
    double death = point.get(1);
    double persistence = death - birth;
    System.out.println("Branch: persistence = " + persistence);
}
```



.. py:method:: getDiagramNodes(String)

   Gets the tree nodes associated with each point in the persistence diagram.

This method returns the actual SWCPoint nodes from the neuronal tree that correspond to each birth-death pair in the persistence diagram. This allows you to map topological features back to specific locations in the original morphology.

Structure: Returns a list where each inner list contains exactly two nodes:

Birth Node [0]: The branch point where the topological feature appears Death Node [1]: The tip node where the topological feature disappears

Correspondence: The order of node pairs matches the order of birth-death pairs returned by getDiagram(String), allowing direct correlation between topological features and their spatial locations.

Example Usage: 
```
List<List<Double>> diagram = analyzer.getDiagram("geodesic");
List<List<SWCPoint>> nodes = analyzer.getDiagramNodes("geodesic");

for (int i = 0; i < diagram.size(); i++) {
    List<Double> birthDeath = diagram.get(i);
    List<SWCPoint> nodesPair = nodes.get(i);
    
    double persistence = birthDeath.get(1) - birthDeath.get(0);
    SWCPoint branchPoint = nodesPair.get(0);
    SWCPoint tipPoint = nodesPair.get(1);
    
    System.out.printf("Branch with persistence %.2f: from (%.1f,%.1f,%.1f) to (%.1f,%.1f,%.1f)%n",
                      persistence, 
                      branchPoint.getX(), branchPoint.getY(), branchPoint.getZ(),
                      tipPoint.getX(), tipPoint.getY(), tipPoint.getZ());
}
```



.. py:method:: getLandscape(String, int, int)

   Gets the persistence landscape as a vectorized representation.

Persistence landscapes transform persistence diagrams into a vector space representation that The landscape is a collection of piecewise-linear functions that capture the "shape" of the persistence diagram in a stable, vectorized format.

Mathematical Background: Each point (birth, death) in the persistence diagram contributes a "tent" function to the landscape. The k-th landscape function at any point is the k-th largest value among all tent functions at that point. This creates a stable, multi-resolution representation of the topological features.

Output Structure: Returns a 1D array of length `numLandscapes × resolution` where the first resolution values represent the first landscape function, the next resolution values represent the second landscape function, and so on.


Other Methods
~~~~~~~~~~~~~


.. py:method:: static main(String;)

   


See Also
--------

* `Package API <../api_auto/pysnt.analysis.html#pysnt.analysis.PersistenceAnalyzer>`_
* `PersistenceAnalyzer JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/PersistenceAnalyzer.html>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
