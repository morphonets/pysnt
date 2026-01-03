"""
Runtime docstring enhancement for PySNT classes.

This module provides enhanced docstrings with JavaDoc descriptions and links
to detailed documentation for all PySNT classes.
"""

def enhance_class_docstrings():
    """Enhance docstrings for all PySNT classes with JavaDoc information."""
    import sys
    
    # Enhanced docstrings for all classes
    enhanced_docstrings = {
        "MouseLightQuerier": '"""\n    Importer for retrieving reconstructions from MouseLight\'s online database at ml-neuronbrowser.janelia.org\n    \n    **All Methods and Attributes:** See `MouseLightQuerier detailed documentation <../pysnt/io/mouselightquerier_doc.html>`_.\n    """',
        "InteractiveTracerCanvas": '"""\n    SNT class with method signatures.\n    \n    Available for direct import after JVM initialization.\n    Call pysnt.initialize() before using this class.\n    \n    **All Methods and Attributes:** See `InteractiveTracerCanvas detailed documentation <../pysnt/interactivetracercanvas_doc.html>`_.\n    \n    See `InteractiveTracerCanvas JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/InteractiveTracerCanvas.html>`_.\n    """',
        "SNTUI": '"""\n    Implements SNT\'s main dialog.\n    \n    **All Methods and Attributes:** See `SNTUI detailed documentation <../pysnt/sntui_doc.html>`_.\n    """',
        "ZBAtlasUtils": '"""\n    Utility methods for accessing the Max Plank Zebrafish Brain Atlas (ZBA) at fishatlas.neuro.mpg.de.\n    \n    **All Methods and Attributes:** See `ZBAtlasUtils detailed documentation <../pysnt/annotation/zbatlasutils_doc.html>`_.\n    """',
        "TracerCanvas": '"""\n    Provides rendering capabilities for visualizing paths, overlays, and additional interactive elements in an ImageJ canvas.\n    \n    **All Methods and Attributes:** See `TracerCanvas detailed documentation <../pysnt/tracercanvas_doc.html>`_.\n    """',
        "SkeletonConverter": '"""\n    Class for generation of Trees from a skeletonized ImagePlus.\n    \n    **All Methods and Attributes:** See `SkeletonConverter detailed documentation <../pysnt/analysis/skeletonconverter_doc.html>`_.\n    """',
        "InsectBrainLoader": '"""\n    Methods for retrieving reconstructions and annotations from the Insect Brain Database at insectbraindb.org *\n    \n    **All Methods and Attributes:** See `InsectBrainLoader detailed documentation <../pysnt/io/insectbrainloader_doc.html>`_.\n    """',
        "NodeProfiler": '"""\n    Command to retrieve node profiles (plots of voxel intensities sampled across Path nodes).\n    \n    **All Methods and Attributes:** See `NodeProfiler detailed documentation <../pysnt/analysis/nodeprofiler_doc.html>`_.\n    """',
        "SNTTable": '"""\n    Extension of DefaultGenericTable with (minor) scripting conveniences.\n    \n    **All Methods and Attributes:** See `SNTTable detailed documentation <../pysnt/analysis/snttable_doc.html>`_.\n    """',
        "Tubeness": '"""\n    Y. Sato, S. Nakajima, N. Shiraga, H. Atsumi, S. Yoshida, T. Koller, G. Gerig, and R. Kikinis, “Three-dimensional multi-scale line filter for segmentation and visualization of curvilinear structures in medical images,” Med Image Anal., vol. 2, no. 2, pp. 143-168, June 1998.\n    \n    **All Methods and Attributes:** See `Tubeness detailed documentation <../pysnt/filter/tubeness_doc.html>`_.\n    """',
        "PathChangeListener": '"""\n    SNT class with method signatures.\n    \n    Available for direct import after JVM initialization.\n    Call pysnt.initialize() before using this class.\n    \n    **All Methods and Attributes:** See `PathChangeListener detailed documentation <../pysnt/pathchangelistener_doc.html>`_.\n    \n    See `PathChangeListener JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathChangeListener.html>`_.\n    """',
        "ImpUtils": '"""\n    Static utilities for handling and manipulation of ImagePluss\n    \n    **All Methods and Attributes:** See `ImpUtils detailed documentation <../pysnt/util/imputils_doc.html>`_.\n    """',
        "ImgUtils": '"""\n    Static utilities for handling and manipulation of `RandomAccessibleInterval`s\n    \n    **All Methods and Attributes:** See `ImgUtils detailed documentation <../pysnt/util/imgutils_doc.html>`_.\n    """',
        "FillerThread": '"""\n    Seeded-volume segmentation via single-source shortest paths. Path nodes are used as seed points in an open-ended variant of Dijkstra\'s algorithm. The threshold sets the maximum allowable distance for a node to be included in the Fill. This distance is represented in the g-score of a node, which is the length of the shortest path from a seed point to that node. The magnitudes of these distances are heavily dependent on the supplied cost function Cost, so the threshold should be set with a particular cost function in mind. It often helps to adjust the threshold interactively.\n    \n    **All Methods and Attributes:** See `FillerThread detailed documentation <../pysnt/tracing/fillerthread_doc.html>`_.\n    """',
        "Frangi": '"""\n    A.F. Frangi, W.J. Niessen, K.L. Vincken, M.A. Viergever (1998). Multiscale vessel enhancement filtering. In Medical Image Computing and Computer-Assisted Intervention - MICCAI\'98, W.M. Wells, A. Colchester and S.L. Delp (Eds.), Lecture Notes in Computer Science, vol. 1496 - Springer Verlag, Berlin, Germany, pp. 130-137.\n    \n    **All Methods and Attributes:** See `Frangi detailed documentation <../pysnt/filter/frangi_doc.html>`_.\n    """',
        "PathProfiler": '"""\n    Command to retrieve Path profiles (plots of voxel intensities values along a Path)\n    \n    **All Methods and Attributes:** See `PathProfiler detailed documentation <../pysnt/analysis/pathprofiler_doc.html>`_.\n    """',
        "AllenUtils": '"""\n    Utility methods for accessing/handling AllenCompartments\n    \n    **All Methods and Attributes:** See `AllenUtils detailed documentation <../pysnt/annotation/allenutils_doc.html>`_.\n    """',
        "Tree": '"""\n    Utility class to access a Collection of Paths (typically a complete reconstruction). A Tree is the preferred way to group, access and manipulate Paths that share something in common, specially when scripting SNT. Note that a "Tree" here is literally a collection of Paths. Very few restrictions are imposed on its topology, although it is generally assumed that the Collection of paths describes a single-rooted structure with no loops.\n    \n    **All Methods and Attributes:** See `Tree detailed documentation <../pysnt/tree_doc.html>`_.\n    """',
        "SNTColor": '"""\n    A simple class for handling Colors including the ability to map an AWT Color to a SWC type integer tag.\n    \n    **All Methods and Attributes:** See `SNTColor detailed documentation <../pysnt/util/sntcolor_doc.html>`_.\n    """',
        "PathFitter": '"""\n    Class for fitting circular cross-sections around existing nodes of a Path in order to compute radii (node thickness) and midpoint refinement of existing coordinates.\n    \n    **All Methods and Attributes:** See `PathFitter detailed documentation <../pysnt/pathfitter_doc.html>`_.\n    """',
        "TreeProperties": '"""\n    Allows standardized metadata to be associated to a Tree.\n    \n    **All Methods and Attributes:** See `TreeProperties detailed documentation <../pysnt/treeproperties_doc.html>`_.\n    """',
        "WekaModelLoader": '"""\n    GUI command for Loading pre-trained models from Labkit/TWS as secondary image layer.\n    \n    **All Methods and Attributes:** See `WekaModelLoader detailed documentation <../pysnt/io/wekamodelloader_doc.html>`_.\n    """',
        "VFBUtils": '"""\n    Utility methods for accessing/handling Virtual Fly Brain (VFB) annotations\n    \n    **All Methods and Attributes:** See `VFBUtils detailed documentation <../pysnt/annotation/vfbutils_doc.html>`_.\n    """',
        "SearchThread": '"""\n    Implements a common thread that explores the image using a variety of strategies, e.g., to trace tubular structures or surfaces.\n    \n    **All Methods and Attributes:** See `SearchThread detailed documentation <../pysnt/tracing/searchthread_doc.html>`_.\n    """',
        "PointInImage": '"""\n    Defines a Point in an image, a node of a traced Path. Coordinates are always expressed in real-world coordinates.\n    \n    **All Methods and Attributes:** See `PointInImage detailed documentation <../pysnt/util/pointinimage_doc.html>`_.\n    """',
        "NodeStatistics": '"""\n    Computes summary and descriptive statistics from a Collection of nodes, including convenience methods to plot distributions of such data.\n    \n    **All Methods and Attributes:** See `NodeStatistics detailed documentation <../pysnt/analysis/nodestatistics_doc.html>`_.\n    """',
        "ColorMaps": '"""\n    Utilities for colormaps and IJ lookup tables\n    \n    **All Methods and Attributes:** See `ColorMaps detailed documentation <../pysnt/util/colormaps_doc.html>`_.\n    """',
        "MultiTreeStatistics": '"""\n    Computes summary and descriptive statistics from univariate properties of Tree groups. For analysis of individual Trees use TreeStatistics.\n    \n    **All Methods and Attributes:** See `MultiTreeStatistics detailed documentation <../pysnt/analysis/multitreestatistics_doc.html>`_.\n    """',
        "FlyCircuitLoader": '"""\n    Absurdly simple importer for retrieving SWC data from FlyCircuit.\n    \n    **All Methods and Attributes:** See `FlyCircuitLoader detailed documentation <../pysnt/io/flycircuitloader_doc.html>`_.\n    """',
        "FillConverter": '"""\n    Map filled nodes from a Collection of FillerThreads to and between RandomAccessibles.\n    \n    **All Methods and Attributes:** See `FillConverter detailed documentation <../pysnt/fillconverter_doc.html>`_.\n    """',
        "PCAnalyzer": '"""\n    Utility class for performing Principal Component Analysis (PCA) on various SNT data structures including Trees, Paths, and collections of SNTPoints.\n\nThis class provides methods to compute the principal axes of 3D point data, which represent the directions of maximum variance in the data. This is useful for analyzing the overall orientation and shape characteristics of neuronal structures, meshes, and other 3D geometries.\n    \n    **All Methods and Attributes:** See `PCAnalyzer detailed documentation <../pysnt/analysis/pcanalyzer_doc.html>`_.\n    """',
        "SNTChart": '"""\n    Extension of ChartPanel modified for scientific publications and convenience methods for plot annotations.\n    \n    **All Methods and Attributes:** See `SNTChart detailed documentation <../pysnt/analysis/sntchart_doc.html>`_.\n    """',
        "InsectBrainUtils": '"""\n    Utility methods for retrieving species, brain, and neuron data from the Insect Brain Database\n    \n    **All Methods and Attributes:** See `InsectBrainUtils detailed documentation <../pysnt/annotation/insectbrainutils_doc.html>`_.\n    """',
        "PathDownsampler": '"""\n    This is an implementation of the Ramer-Douglas-Peucker algorithm for simplifying a curve represented by line-segments, as described here\n    \n    **All Methods and Attributes:** See `PathDownsampler detailed documentation <../pysnt/pathdownsampler_doc.html>`_.\n    """',
        "PersistenceAnalyzer": '"""\n    Performs persistent homology analysis on neuronal Trees.\n\nThis class implements the algorithm described in Kanari, L. et al. "A Topological Representation of Branching Neuronal Morphologies" (Neuroinformatics 16, 3–13, 2018) to extract topological features from neuronal morphologies.\n\nCore Concepts\n\nFilter Functions: Mathematical functions that assign scalar values to each node in the tree based on various morphological properties (distance from root, branch order, spatial coordinates, etc.).\n\nPersistence Diagram: A collection of 2D points (birth, death) representing when topological features (branches) appear and disappear during a filtration process. Each point corresponds to a branch in the neuronal tree.\n\nPersistence: The "lifespan" of a topological feature, calculated as death - birth. High persistence indicates morphologically significant branches, while low persistence may represent noise or minor branches.\n\nSupported Filter Functions\n\nGeodesic: Path distance from node to root along the tree structure Radial: Euclidean (straight-line) distance from node to root Centrifugal: Reverse Strahler number (branch order from tips) Path Order: SNT path order hierarchy X, Y, Z: Spatial coordinates for directional analysis\n\nUsage Example \n```\n// Create analyzer for a neuronal tree\nPersistenceAnalyzer analyzer = new PersistenceAnalyzer(tree);\n\n// Get persistence diagram using geodesic distance\nList<List<Double>> diagram = analyzer.getDiagram("geodesic");\n\n// Each inner list contains [birth, death] values\nfor (List<Double> pair : diagram) {\n    double birth = pair.get(0);\n    double death = pair.get(1);\n    double persistence = death - birth;\n    System.out.println("Branch: birth=" + birth + ", death=" + death + ", persistence=" + persistence);\n}\n\n// Get persistence landscape\ndouble[] landscape = analyzer.getLandscape("geodesic", 5, 100);\n```\n    \n    **All Methods and Attributes:** See `PersistenceAnalyzer detailed documentation <../pysnt/analysis/persistenceanalyzer_doc.html>`_.\n    """',
        "BiSearch": '"""\n    A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.H.L.M., Post, H., 2009. "Yet another bidirectional algorithm for shortest paths," Econometric Institute Research Papers EI 2009-10, Erasmus University Rotterdam, Erasmus School of Economics (ESE), Econometric Institute.\n\nThe search distance function (Cost) and heuristic estimate (Heuristic) are supplied by the caller.\n    \n    **All Methods and Attributes:** See `BiSearch detailed documentation <../pysnt/tracing/bisearch_doc.html>`_.\n    """',
        "Path": '"""\n    This class represents a traced segment (i.e., a Path) in a reconstruction. It has methods to manipulate its points (nodes) with sup-pixel accuracy, including drawing them onto threePane-style canvases, etc.\n\nPaths are non-branching sequences of adjacent points (including diagonals) in the image. Branches and joins are supported by attributes of paths that specify that they begin on (or end on) other paths.\n\nIn SNT, a Path can exist in two versions or flavors: itself and a fitted version generated by PathFitter. Because fitting may fail around certain nodes, the fitted version may have a different number of nodes relatively to its non-fitted version\n    \n    **All Methods and Attributes:** See `Path detailed documentation <../pysnt/path_doc.html>`_.\n    """',
        "BoundingBox": '"""\n    A BoundingBox contains information (including spatial calibration) of a tracing canvas bounding box, i.e., the minimum bounding cuboid containing all nodes (SNTPoints) of a reconstructed structure.\n    \n    **All Methods and Attributes:** See `BoundingBox detailed documentation <../pysnt/util/boundingbox_doc.html>`_.\n    """',
        "BiSearchNode": '"""\n    A SearchNode which can maintain both a from-start and from-goal search state.\n    \n    **All Methods and Attributes:** See `BiSearchNode detailed documentation <../pysnt/tracing/bisearchnode_doc.html>`_.\n    """',
        "ShollAnalyzer": '"""\n    Class to retrieve Sholl metrics from a Tree.\n    \n    **All Methods and Attributes:** See `ShollAnalyzer detailed documentation <../pysnt/analysis/shollanalyzer_doc.html>`_.\n    """',
        "MouseLightLoader": '"""\n    Methods for retrieving reconstructions from MouseLight\'s online database at ml-neuronbrowser.janelia.org *\n    \n    **All Methods and Attributes:** See `MouseLightLoader detailed documentation <../pysnt/io/mouselightloader_doc.html>`_.\n    """',
        "PathAndFillManager": '"""\n    The PathAndFillManager is responsible for importing, handling and managing of Paths and Fills. Typically, a PathAndFillManager is accessed from a SNT instance, but accessing a PathAndFillManager directly is useful for batch/headless operations.\n    \n    **All Methods and Attributes:** See `PathAndFillManager detailed documentation <../pysnt/pathandfillmanager_doc.html>`_.\n    """',
        "Fill": '"""\n    Defines a filled structure.\n    \n    **All Methods and Attributes:** See `Fill detailed documentation <../pysnt/fill_doc.html>`_.\n    """',
        "TreeStatistics": '"""\n    Computes summary and descriptive statistics from properties of Paths and Nodes in a Tree, including convenience methods to plot distributions of such data. For analysis of groups of Trees have a look at MultiTreeStatistics and `GroupedTreeStatistics`.\n    \n    **All Methods and Attributes:** See `TreeStatistics detailed documentation <../pysnt/analysis/treestatistics_doc.html>`_.\n    """',
        "SearchNode": '"""\n    SNT class with method signatures.\n    \n    Available for direct import after JVM initialization.\n    Call pysnt.initialize() before using this class.\n    \n    **All Methods and Attributes:** See `SearchNode detailed documentation <../pysnt/tracing/searchnode_doc.html>`_.\n    \n    See `SearchNode JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/SearchNode.html>`_.\n    """',
        "Viewer3D": '"""\n    Implements SNT\'s Reconstruction Viewer. Relies heavily on the org.jzy3d package.\n    \n    **All Methods and Attributes:** See `Viewer3D detailed documentation <../pysnt/viewer/viewer3d_doc.html>`_.\n    """',
        "SNTPoint": '"""\n    Classes extend this interface implement a point in a 3D space, always using real world coordinates.\n    \n    **All Methods and Attributes:** See `SNTPoint detailed documentation <../pysnt/util/sntpoint_doc.html>`_.\n    """',
        "PathStatistics": '"""\n    A specialized version of TreeStatistics for analyzing individual paths without considering their connectivity relationships.\n\nPathStatistics provides morphometric analysis of neuronal paths while treating each path as an independent entity, rather than as part of a connected tree structure.\n\nKey differences from TreeStatistics:\n\nNo graph conversion - paths are analyzed independently Branch-related metrics are redefined to work with individual paths Supports path-specific measurements like Path ID and number of children Provides individual path measurement capabilities\n\nExample usage: \n```\n// Analyze a single path\nPathStatistics stats = new PathStatistics(path);\ndouble length = stats.getMetric("Path length").doubleValue();\n\n// Analyze multiple paths independently\nCollection<Path> paths = getPaths();\nPathStatistics multiStats = new PathStatistics(paths, "My Analysis");\nmultiStats.measureIndividualPaths(Arrays.asList("Path length", "N. nodes"), true);\n```\n    \n    **All Methods and Attributes:** See `PathStatistics detailed documentation <../pysnt/analysis/pathstatistics_doc.html>`_.\n    """',
        "GroupedTreeStatistics": '"""\n    Computes statistics from Tree groups.\n    \n    **All Methods and Attributes:** See `GroupedTreeStatistics detailed documentation <../pysnt/analysis/groupedtreestatistics_doc.html>`_.\n    """',
        "StrahlerAnalyzer": '"""\n    Class to perform Horton-Strahler analysis on a Tree.\n    \n    **All Methods and Attributes:** See `StrahlerAnalyzer detailed documentation <../pysnt/analysis/strahleranalyzer_doc.html>`_.\n    """',
        "Viewer2D": '"""\n    Class for rendering Trees as 2D plots that can be exported as SVG, PNG or PDF.\n    \n    **All Methods and Attributes:** See `Viewer2D detailed documentation <../pysnt/viewer/viewer2d_doc.html>`_.\n    """',
        "RootAngleAnalyzer": '"""\n    Class to perform Root angle analysis on a Tree according to Bird and Cuntz 2019, PMID 31167149.\n    \n    **All Methods and Attributes:** See `RootAngleAnalyzer detailed documentation <../pysnt/analysis/rootangleanalyzer_doc.html>`_.\n    """',
        "TracerThread": '"""\n    SNT\'s default tracer thread: explores between two points in an image, doing an A* search with a choice of distance measures.\n    \n    **All Methods and Attributes:** See `TracerThread detailed documentation <../pysnt/tracing/tracerthread_doc.html>`_.\n    """',
        "AllenCompartment": '"""\n    Defines an Allen Reference Atlas (ARA) [Allen Mouse Common Coordinate Framework] annotation. A Compartment is defined by either a UUID (as per MouseLight\'s database) or its unique integer identifier. To improve performance, a compartment\'s metadata (reference to its mesh, its aliases, etc.) are not loaded at initialization, but retrieved only when such getters are called.\n    \n    **All Methods and Attributes:** See `AllenCompartment detailed documentation <../pysnt/annotation/allencompartment_doc.html>`_.\n    """',
        "SNTService": '"""\n    Service for accessing and scripting the active instance of SNT.\n    \n    **All Methods and Attributes:** See `SNTService detailed documentation <../pysnt/sntservice_doc.html>`_.\n    """',
        "SciViewSNT": '"""\n    Bridges SNT to SciView, allowing Trees to be rendered as scenery objects\n    \n    **All Methods and Attributes:** See `SciViewSNT detailed documentation <../pysnt/sciviewsnt_doc.html>`_.\n    """',
        "RemoteSWCLoader": '"""\n    Importers downloading remote SWC files should extend this interface.\n    \n    **All Methods and Attributes:** See `RemoteSWCLoader detailed documentation <../pysnt/io/remoteswcloader_doc.html>`_.\n    """',
        "ConvexHull3D": '"""\n    Convex hull analysis in 3D.\n    \n    **All Methods and Attributes:** See `ConvexHull3D detailed documentation <../pysnt/analysis/convexhull3d_doc.html>`_.\n    """',
        "NodeColorMapper": '"""\n    Class for color coding of NodeStatistics results.\n    \n    **All Methods and Attributes:** See `NodeColorMapper detailed documentation <../pysnt/analysis/nodecolormapper_doc.html>`_.\n    """',
        "InsectBrainCompartment": '"""\n    SNT class with method signatures.\n    \n    Available for direct import after JVM initialization.\n    Call pysnt.initialize() before using this class.\n    \n    **All Methods and Attributes:** See `InsectBrainCompartment detailed documentation <../pysnt/annotation/insectbraincompartment_doc.html>`_.\n    \n    See `InsectBrainCompartment JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/annotation/InsectBrainCompartment.html>`_.\n    """',
        "PathStraightener": '"""\n    Command to "straighten" an image using Path coordinates.\n    \n    **All Methods and Attributes:** See `PathStraightener detailed documentation <../pysnt/analysis/pathstraightener_doc.html>`_.\n    """',
        "MultiViewer3D": '"""\n    Class for rendering individual Viewer3Ds as a multi-panel montage.\n    \n    **All Methods and Attributes:** See `MultiViewer3D detailed documentation <../pysnt/viewer/multiviewer3d_doc.html>`_.\n    """',
        "SWCPoint": '"""\n    Defines a node in an SWC reconstruction. The SWC file format is detailed here.\n    \n    **All Methods and Attributes:** See `SWCPoint detailed documentation <../pysnt/util/swcpoint_doc.html>`_.\n    """',
        "CrossoverFinder": '"""\n    Utility to detect crossover locations between paths: spatially close locations between paths that look like intersections in the image but are not topological joins in the traced graph.\n\nHere, a crossover is defined as a spatial location where two distinct paths approach within a distance threshold (in real units) for at least minRunNodes consecutive node pairs, but do not share an actual tracing node at that location. Optional geometric filtering by crossing angle is supported.\n\nUsage: \n```\nCrossoverFinder.Config cfg = new CrossoverFinder.Config()\n      .proximity(2.0)          // spatial threshold in spatially calibrated units (e.g., microns)\n      .thetaMinDeg(25)         // optional minimum crossing angle (0 to disable)\n      .minRunNodes(2)          // consecutive near-node pairs to accept a crossover event candidate\n      .sameCTOnly(true)        // ignore pairs from different channel/time\n      .includeSelfCrossovers(false) // whether crossover events within the same path should be detected\n  List<CrossoverFinder.CrossoverEvent> events = CrossoverFinder.find(paths, cfg);\n```\n    \n    **All Methods and Attributes:** See `CrossoverFinder detailed documentation <../pysnt/util/crossoverfinder_doc.html>`_.\n    """',
        "NeuroMorphoLoader": '"""\n    Importer for retrieving SWC data from neuromorpho.org.\n    \n    **All Methods and Attributes:** See `NeuroMorphoLoader detailed documentation <../pysnt/io/neuromorpholoader_doc.html>`_.\n    """',
        "MultiTreeColorMapper": '"""\n    Class for color coding groups of Trees.\n\nAfter a mapping property and a color table (LUT) are specified, the mapping proceeds as follows: 1) Each Tree in the group is measured for the mapping property; 2) each measurement is mapped to a LUT entry that is used to color each Tree. Mapping limits can be optionally specified\n    \n    **All Methods and Attributes:** See `MultiTreeColorMapper detailed documentation <../pysnt/analysis/multitreecolormapper_doc.html>`_.\n    """',
        "SNT": '"""\n    Implements the SNT plugin.\n    \n    **All Methods and Attributes:** See `SNT detailed documentation <../pysnt/snt_doc.html>`_.\n    """',
        "DefaultSearchNode": '"""\n    A SearchNode which can maintain both a from-start and from-goal search state.\n    \n    **All Methods and Attributes:** See `DefaultSearchNode detailed documentation <../pysnt/tracing/defaultsearchnode_doc.html>`_.\n    """',
        "PathManagerUI": '"""\n    Implements the Path Manager Dialog.\n    \n    **All Methods and Attributes:** See `PathManagerUI detailed documentation <../pysnt/pathmanagerui_doc.html>`_.\n    """',
        "Annotation3D": '"""\n    An Annotation3D is a triangulated surface or a cloud of points (scatter) rendered in Viewer3D that can be used to highlight nodes in a Tree or locations in a mesh.\n    \n    **All Methods and Attributes:** See `Annotation3D detailed documentation <../pysnt/viewer/annotation3d_doc.html>`_.\n    """',
        "ConvexHullAnalyzer": '"""\n    Class for Convex Hull measurements of a Tree.\n    \n    **All Methods and Attributes:** See `ConvexHullAnalyzer detailed documentation <../pysnt/analysis/convexhullanalyzer_doc.html>`_.\n    """',
        "SNTUtils": '"""\n    Static utilities for SNT\n    \n    **All Methods and Attributes:** See `SNTUtils detailed documentation <../pysnt/sntutils_doc.html>`_.\n    """',
        "MultiViewer2D": '"""\n    Class for rendering montages of Trees as 2D plots that can be exported as SVG, PNG or PDF.\n    \n    **All Methods and Attributes:** See `MultiViewer2D detailed documentation <../pysnt/viewer/multiviewer2d_doc.html>`_.\n    """',
        "ConvexHull2D": '"""\n    Computes the convex hull of a set of 2D points.\n    \n    **All Methods and Attributes:** See `ConvexHull2D detailed documentation <../pysnt/analysis/convexhull2d_doc.html>`_.\n    """',
        "TreeColorMapper": '"""\n    Class for color coding Trees.\n    \n    **All Methods and Attributes:** See `TreeColorMapper detailed documentation <../pysnt/analysis/treecolormapper_doc.html>`_.\n    """',
        "PathResult": '"""\n    SNT class with method signatures.\n    \n    Available for direct import after JVM initialization.\n    Call pysnt.initialize() before using this class.\n    \n    **All Methods and Attributes:** See `PathResult detailed documentation <../pysnt/tracing/pathresult_doc.html>`_.\n    \n    See `PathResult JavaDoc <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/PathResult.html>`_.\n    """',
    }
    
    # Apply enhanced docstrings to classes in pysnt modules
    _apply_enhanced_docstrings(enhanced_docstrings)

def _apply_enhanced_docstrings(enhanced_docstrings):
    """Apply enhanced docstrings to classes in loaded modules."""
    import sys
    import os
    from pathlib import Path
    
    # Automatically discover all pysnt submodules
    module_names = ['pysnt']  # Start with main module
    
    # Find the pysnt package directory
    try:
        # Try to find pysnt in sys.path or relative to this file
        pysnt_dir = None
        for path in sys.path:
            potential_dir = Path(path) / 'pysnt'
            if potential_dir.is_dir() and (potential_dir / '__init__.py').exists():
                pysnt_dir = potential_dir
                break
        
        # If not found in sys.path, try relative to common locations
        if not pysnt_dir:
            # Try relative to this file (for when generating docs)
            script_dir = Path(__file__).parent.parent.parent.parent  # Go up to project root
            potential_dir = script_dir / 'src' / 'pysnt'
            if potential_dir.is_dir() and (potential_dir / '__init__.py').exists():
                pysnt_dir = potential_dir
        
        # Discover submodules
        if pysnt_dir:
            for item in sorted(pysnt_dir.iterdir()):
                if item.is_dir() and not item.name.startswith('_') and not item.name.startswith('.'):
                    # Check if it's a Python package (has __init__.py)
                    if (item / '__init__.py').exists():
                        module_names.append(f'pysnt.{item.name}')
    except Exception:
        # If discovery fails, fall back to known modules
        module_names = [
            'pysnt',
            'pysnt.analysis',
            'pysnt.annotation',
            'pysnt.converters',
            'pysnt.display',
            'pysnt.gui',
            'pysnt.io',
            'pysnt.tracing',
            'pysnt.util',
            'pysnt.viewer'
        ]
    
    for module_name in module_names:
        # Try to get the module from sys.modules, or import it
        module = None
        if module_name in sys.modules:
            module = sys.modules[module_name]
        else:
            # Try to import the module
            try:
                module = __import__(module_name, fromlist=[''])
            except (ImportError, Exception):
                # Module not available, skip it
                continue
        
        if module:
            for class_name, enhanced_docstring in enhanced_docstrings.items():
                if hasattr(module, class_name):
                    class_obj = getattr(module, class_name)
                    if hasattr(class_obj, '__doc__'):
                        class_obj.__doc__ = enhanced_docstring
                        #print(f"Enhanced docstring for {module_name}.{class_name}")

# Auto-enhance when this module is imported
enhance_class_docstrings()
