
Class Index
===========

This page provides an index of all classes available in the SNT API.

Total classes: **73**


A
-

* `AllenCompartment <../pysnt/allencompartment_doc.html>`_ (``sc.fiji.snt.annotation``) - Defines an Allen Reference Atlas (ARA) [Allen Mouse Common Coordinate Framework] annotation.
* `AllenUtils <../pysnt/allenutils_doc.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing/handling AllenCompartments

B
-

* `BiSearch <../pysnt/bisearch_doc.html>`_ (``sc.fiji.snt.tracing``) - A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.
* `BiSearchNode <../pysnt/bisearchnode_doc.html>`_ (``sc.fiji.snt.tracing``) - A SearchNode which can maintain both a from-start and from-goal search state.
* `BoundingBox <../pysnt/boundingbox_doc.html>`_ (``sc.fiji.snt.util``) - A BoundingBox contains information (including spatial calibration) of a tracing canvas bounding box, i.

C
-

* `ColorMaps <../pysnt/colormaps_doc.html>`_ (``sc.fiji.snt.util``) - Utilities for colormaps and IJ lookup tables
* `ConvexHull2D <../pysnt/convexhull2d_doc.html>`_ (``sc.fiji.snt.analysis``) - Computes the convex hull of a set of 2D points.
* `ConvexHull3D <../pysnt/convexhull3d_doc.html>`_ (``sc.fiji.snt.analysis``) - Convex hull analysis in 3D.
* `ConvexHullAnalyzer <../pysnt/convexhullanalyzer_doc.html>`_ (``sc.fiji.snt.analysis``) - Class for Convex Hull measurements of a Tree.
* `CrossoverFinder <../pysnt/crossoverfinder_doc.html>`_ (``sc.fiji.snt.util``) - Utility to detect crossover locations between paths: spatially close locations between paths that look like intersections in the image but are not topological joins in the traced graph.

D
-

* `DefaultSearchNode <../pysnt/defaultsearchnode_doc.html>`_ (``sc.fiji.snt.tracing``) - A SearchNode which can maintain both a from-start and from-goal search state.

F
-

* `Fill <../pysnt/fill_doc.html>`_ (``sc.fiji.snt``) - Defines a filled structure.
* `FillConverter <../pysnt/fillconverter_doc.html>`_ (``sc.fiji.snt``) - Map filled nodes from a Collection of FillerThreads to and between RandomAccessibles.
* `FillerThread <../pysnt/fillerthread_doc.html>`_ (``sc.fiji.snt.tracing``) - Seeded-volume segmentation via single-source shortest paths.
* `FlyCircuitLoader <../pysnt/flycircuitloader_doc.html>`_ (``sc.fiji.snt.io``) - Absurdly simple importer for retrieving SWC data from FlyCircuit.

G
-

* `GroupedTreeStatistics <../pysnt/groupedtreestatistics_doc.html>`_ (``sc.fiji.snt.analysis``) - Computes statistics from Tree groups.

I
-

* `ImgUtils <../pysnt/imgutils_doc.html>`_ (``sc.fiji.snt.util``) - Static utilities for handling and manipulation of `RandomAccessibleInterval`s
* `ImpUtils <../pysnt/imputils_doc.html>`_ (``sc.fiji.snt.util``) - Static utilities for handling and manipulation of ImagePluss
* `InsectBrainCompartment <../pysnt/insectbraincompartment_doc.html>`_ (``sc.fiji.snt.annotation``) - Enhanced documentation for InsectBrainCompartment class.
* `InsectBrainLoader <../pysnt/insectbrainloader_doc.html>`_ (``sc.fiji.snt.io``) - Methods for retrieving reconstructions and annotations from the Insect Brain Database at insectbraindb.
* `InsectBrainUtils <../pysnt/insectbrainutils_doc.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for retrieving species, brain, and neuron data from the Insect Brain Database
* `InteractiveTracerCanvas <../pysnt/interactivetracercanvas_doc.html>`_ (``sc.fiji.snt``) - Enhanced documentation for InteractiveTracerCanvas class.

M
-

* `MouseLightLoader <../pysnt/mouselightloader_doc.html>`_ (``sc.fiji.snt.io``) - Methods for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.
* `MouseLightQuerier <../pysnt/mouselightquerier_doc.html>`_ (``sc.fiji.snt.io``) - Importer for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.
* `MultiTreeColorMapper <../pysnt/multitreecolormapper_doc.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding groups of Trees.
* `MultiTreeStatistics <../pysnt/multitreestatistics_doc.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from univariate properties of Tree groups.
* `MultiViewer2D <../pysnt/multiviewer2d_doc.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering montages of Trees as 2D plots that can be exported as SVG, PNG or PDF.
* `MultiViewer3D <../pysnt/multiviewer3d_doc.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering individual Viewer3Ds as a multi-panel montage.

N
-

* `NeuroMorphoLoader <../pysnt/neuromorpholoader_doc.html>`_ (``sc.fiji.snt.io``) - Importer for retrieving SWC data from neuromorpho.
* `NodeColorMapper <../pysnt/nodecolormapper_doc.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding of NodeStatistics results.
* `NodeProfiler <../pysnt/nodeprofiler_doc.html>`_ (``sc.fiji.snt.analysis``) - Command to retrieve node profiles (plots of voxel intensities sampled across Path nodes).
* `NodeStatistics <../pysnt/nodestatistics_doc.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from a Collection of nodes, including convenience methods to plot distributions of such data.

P
-

* `Path <../pysnt/path_doc.html>`_ (``sc.fiji.snt``) - This class represents a traced segment (i.
* `PathAndFillManager <../pysnt/pathandfillmanager_doc.html>`_ (``sc.fiji.snt``) - The PathAndFillManager is responsible for importing, handling and managing of Paths and Fills.
* `PathChangeListener <../pysnt/pathchangelistener_doc.html>`_ (``sc.fiji.snt``) - Enhanced documentation for PathChangeListener class.
* `PathDownsampler <../pysnt/pathdownsampler_doc.html>`_ (``sc.fiji.snt``) - This is an implementation of the Ramer-Douglas-Peucker algorithm for simplifying a curve represented by line-segments, as described here
* `PathFitter <../pysnt/pathfitter_doc.html>`_ (``sc.fiji.snt``) - Class for fitting circular cross-sections around existing nodes of a Path in order to compute radii (node thickness) and midpoint refinement of existing coordinates.
* `PathManagerUI <../pysnt/pathmanagerui_doc.html>`_ (``sc.fiji.snt``) - Implements the Path Manager Dialog.
* `PathProfiler <../pysnt/pathprofiler_doc.html>`_ (``sc.fiji.snt.analysis``) - Command to retrieve Path profiles (plots of voxel intensities values along a Path)
* `PathResult <../pysnt/pathresult_doc.html>`_ (``sc.fiji.snt.tracing``) - Enhanced documentation for PathResult class.
* `PathStatistics <../pysnt/pathstatistics_doc.html>`_ (``sc.fiji.snt.analysis``) - A specialized version of TreeStatistics for analyzing individual paths without considering their connectivity relationships.
* `PathStraightener <../pysnt/pathstraightener_doc.html>`_ (``sc.fiji.snt.analysis``) - Command to "straighten" an image using Path coordinates.
* `PCAnalyzer <../pysnt/pcanalyzer_doc.html>`_ (``sc.fiji.snt.analysis``) - Utility class for performing Principal Component Analysis (PCA) on various SNT data structures including Trees, Paths, and collections of SNTPoints.
* `PersistenceAnalyzer <../pysnt/persistenceanalyzer_doc.html>`_ (``sc.fiji.snt.analysis``) - Performs persistent homology analysis on neuronal Trees.
* `PointInImage <../pysnt/pointinimage_doc.html>`_ (``sc.fiji.snt.util``) - Defines a Point in an image, a node of a traced Path.

R
-

* `RemoteSWCLoader <../pysnt/remoteswcloader_doc.html>`_ (``sc.fiji.snt.io``) - Importers downloading remote SWC files should extend this interface.
* `RootAngleAnalyzer <../pysnt/rootangleanalyzer_doc.html>`_ (``sc.fiji.snt.analysis``) - Class to perform Root angle analysis on a Tree according to Bird and Cuntz 2019, PMID 31167149.

S
-

* `SciViewSNT <../pysnt/sciviewsnt_doc.html>`_ (``sc.fiji.snt``) - Bridges SNT to SciView, allowing Trees to be rendered as scenery objects
* `SearchNode <../pysnt/searchnode_doc.html>`_ (``sc.fiji.snt.tracing``) - Enhanced documentation for SearchNode class.
* `SearchThread <../pysnt/searchthread_doc.html>`_ (``sc.fiji.snt.tracing``) - Implements a common thread that explores the image using a variety of strategies, e.
* `ShollAnalyzer <../pysnt/shollanalyzer_doc.html>`_ (``sc.fiji.snt.analysis``) - Class to retrieve Sholl metrics from a Tree.
* `SkeletonConverter <../pysnt/skeletonconverter_doc.html>`_ (``sc.fiji.snt.analysis``) - Class for generation of Trees from a skeletonized ImagePlus.
* `SNT <../pysnt/snt_doc.html>`_ (``sc.fiji.snt``) - Implements the SNT plugin.
* `SNTChart <../pysnt/sntchart_doc.html>`_ (``sc.fiji.snt.analysis``) - Extension of ChartPanel modified for scientific publications and convenience methods for plot annotations.
* `SNTColor <../pysnt/sntcolor_doc.html>`_ (``sc.fiji.snt.util``) - A simple class for handling Colors including the ability to map an AWT Color to a SWC type integer tag.
* `SNTPoint <../pysnt/sntpoint_doc.html>`_ (``sc.fiji.snt.util``) - Classes extend this interface implement a point in a 3D space, always using real world coordinates.
* `SNTService <../pysnt/sntservice_doc.html>`_ (``sc.fiji.snt``) - Service for accessing and scripting the active instance of SNT.
* `SNTTable <../pysnt/snttable_doc.html>`_ (``sc.fiji.snt.analysis``) - Extension of DefaultGenericTable with (minor) scripting conveniences.
* `SNTUI <../pysnt/sntui_doc.html>`_ (``sc.fiji.snt``) - Implements SNT's main dialog.
* `SNTUtils <../pysnt/sntutils_doc.html>`_ (``sc.fiji.snt``) - Static utilities for SNT
* `StrahlerAnalyzer <../pysnt/strahleranalyzer_doc.html>`_ (``sc.fiji.snt.analysis``) - Class to perform Horton-Strahler analysis on a Tree.
* `SWCPoint <../pysnt/swcpoint_doc.html>`_ (``sc.fiji.snt.util``) - Defines a node in an SWC reconstruction.

T
-

* `TracerCanvas <../pysnt/tracercanvas_doc.html>`_ (``sc.fiji.snt``) - Provides rendering capabilities for visualizing paths, overlays, and additional interactive elements in an ImageJ canvas.
* `TracerThread <../pysnt/tracerthread_doc.html>`_ (``sc.fiji.snt.tracing``) - SNT's default tracer thread: explores between two points in an image, doing an A* search with a choice of distance measures.
* `Tree <../pysnt/tree_doc.html>`_ (``sc.fiji.snt``) - Utility class to access a Collection of Paths (typically a complete reconstruction).
* `TreeColorMapper <../pysnt/treecolormapper_doc.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding Trees.
* `TreeProperties <../pysnt/treeproperties_doc.html>`_ (``sc.fiji.snt``) - Allows standardized metadata to be associated to a Tree.
* `TreeStatistics <../pysnt/treestatistics_doc.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from properties of Paths and Nodes in a Tree, including convenience methods to plot distributions of such data.

V
-

* `VFBUtils <../pysnt/vfbutils_doc.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing/handling Virtual Fly Brain (VFB) annotations
* `Viewer2D <../pysnt/viewer2d_doc.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering Trees as 2D plots that can be exported as SVG, PNG or PDF.
* `Viewer3D <../pysnt/viewer3d_doc.html>`_ (``sc.fiji.snt.viewer``) - Implements SNT's Reconstruction Viewer.

W
-

* `WekaModelLoader <../pysnt/wekamodelloader_doc.html>`_ (``sc.fiji.snt.io``) - GUI command for Loading pre-trained models from Labkit/TWS as secondary image layer.

Z
-

* `ZBAtlasUtils <../pysnt/zbatlasutils_doc.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing the Max Plank Zebrafish Brain Atlas (ZBA) at fishatlas.


See Also
--------

* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
* :doc:`API Documentation </api_auto/index>`
