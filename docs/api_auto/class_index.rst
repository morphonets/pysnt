
Class Index
===========

This page provides an index of all classes available in the SNT API.

Total classes: **76**


A
-

* `AllenCompartment <../pysnt/annotation/allencompartment.html>`_ (``sc.fiji.snt.annotation``) - Defines an Allen Reference Atlas (ARA) [Allen Mouse Common Coordinate Framework] annotation.
* `AllenUtils <../pysnt/annotation/allenutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing/handling AllenCompartments
* `Annotation3D <../pysnt/viewer/annotation3d.html>`_ (``sc.fiji.snt.viewer``) - An Annotation3D is a triangulated surface or a cloud of points (scatter) rendered in Viewer3D that can be used to highlight nodes in a Tree or locations in a mesh.

B
-

* `BiSearch <../pysnt/tracing/bisearch.html>`_ (``sc.fiji.snt.tracing``) - A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.
* `BiSearchNode <../pysnt/tracing/bisearchnode.html>`_ (``sc.fiji.snt.tracing``) - A SearchNode which can maintain both a from-start and from-goal search state.
* `BoundingBox <../pysnt/util/boundingbox.html>`_ (``sc.fiji.snt.util``) - A BoundingBox contains information (including spatial calibration) of a tracing canvas bounding box, i.

C
-

* `ColorMaps <../pysnt/util/colormaps.html>`_ (``sc.fiji.snt.util``) - Utilities for colormaps and IJ lookup tables
* `ConvexHull2D <../pysnt/analysis/convexhull2d.html>`_ (``sc.fiji.snt.analysis``) - Computes the convex hull of a set of 2D points.
* `ConvexHull3D <../pysnt/analysis/convexhull3d.html>`_ (``sc.fiji.snt.analysis``) - Convex hull analysis in 3D.
* `ConvexHullAnalyzer <../pysnt/analysis/convexhullanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class for Convex Hull measurements of a Tree.
* `CrossoverFinder <../pysnt/util/crossoverfinder.html>`_ (``sc.fiji.snt.util``) - Utility to detect crossover locations between paths: spatially close locations between paths that look like intersections in the image but are not topological joins in the traced graph.

D
-

* `DefaultSearchNode <../pysnt/tracing/defaultsearchnode.html>`_ (``sc.fiji.snt.tracing``) - A SearchNode which can maintain both a from-start and from-goal search state.

F
-

* `Fill <../pysnt/fill.html>`_ (``sc.fiji.snt``) - Defines a filled structure.
* `FillConverter <../pysnt/fillconverter.html>`_ (``sc.fiji.snt``) - Map filled nodes from a Collection of FillerThreads to and between RandomAccessibles.
* `FillerThread <../pysnt/tracing/fillerthread.html>`_ (``sc.fiji.snt.tracing``) - Seeded-volume segmentation via single-source shortest paths.
* `FlyCircuitLoader <../pysnt/io/flycircuitloader.html>`_ (``sc.fiji.snt.io``) - Absurdly simple importer for retrieving SWC data from FlyCircuit.
* `Frangi <../pysnt/filter/frangi.html>`_ (``sc.fiji.snt.filter``) - A.

G
-

* `GroupedTreeStatistics <../pysnt/analysis/groupedtreestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes statistics from Tree groups.

I
-

* `ImgUtils <../pysnt/util/imgutils.html>`_ (``sc.fiji.snt.util``) - Static utilities for handling and manipulation of `RandomAccessibleInterval`s
* `ImpUtils <../pysnt/util/imputils.html>`_ (``sc.fiji.snt.util``) - Static utilities for handling and manipulation of ImagePluss
* `InsectBrainCompartment <../pysnt/annotation/insectbraincompartment.html>`_ (``sc.fiji.snt.annotation``) - Enhanced documentation for InsectBrainCompartment class.
* `InsectBrainLoader <../pysnt/io/insectbrainloader.html>`_ (``sc.fiji.snt.io``) - Methods for retrieving reconstructions and annotations from the Insect Brain Database at insectbraindb.
* `InsectBrainUtils <../pysnt/annotation/insectbrainutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for retrieving species, brain, and neuron data from the Insect Brain Database
* `InteractiveTracerCanvas <../pysnt/interactivetracercanvas.html>`_ (``sc.fiji.snt``) - Enhanced documentation for InteractiveTracerCanvas class.

M
-

* `MouseLightLoader <../pysnt/io/mouselightloader.html>`_ (``sc.fiji.snt.io``) - Methods for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.
* `MouseLightQuerier <../pysnt/io/mouselightquerier.html>`_ (``sc.fiji.snt.io``) - Importer for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.
* `MultiTreeColorMapper <../pysnt/analysis/multitreecolormapper.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding groups of Trees.
* `MultiTreeStatistics <../pysnt/analysis/multitreestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from univariate properties of Tree groups.
* `MultiViewer2D <../pysnt/viewer/multiviewer2d.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering montages of Trees as 2D plots that can be exported as SVG, PNG or PDF.
* `MultiViewer3D <../pysnt/viewer/multiviewer3d.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering individual Viewer3Ds as a multi-panel montage.

N
-

* `NeuroMorphoLoader <../pysnt/io/neuromorpholoader.html>`_ (``sc.fiji.snt.io``) - Importer for retrieving SWC data from neuromorpho.
* `NodeColorMapper <../pysnt/analysis/nodecolormapper.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding of NodeStatistics results.
* `NodeProfiler <../pysnt/analysis/nodeprofiler.html>`_ (``sc.fiji.snt.analysis``) - Command to retrieve node profiles (plots of voxel intensities sampled across Path nodes).
* `NodeStatistics <../pysnt/analysis/nodestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from a Collection of nodes, including convenience methods to plot distributions of such data.

P
-

* `Path <../pysnt/path.html>`_ (``sc.fiji.snt``) - This class represents a traced segment (i.
* `PathAndFillManager <../pysnt/pathandfillmanager.html>`_ (``sc.fiji.snt``) - The PathAndFillManager is responsible for importing, handling and managing of Paths and Fills.
* `PathChangeListener <../pysnt/pathchangelistener.html>`_ (``sc.fiji.snt``) - Enhanced documentation for PathChangeListener class.
* `PathDownsampler <../pysnt/pathdownsampler.html>`_ (``sc.fiji.snt``) - This is an implementation of the Ramer-Douglas-Peucker algorithm for simplifying a curve represented by line-segments, as described here
* `PathFitter <../pysnt/pathfitter.html>`_ (``sc.fiji.snt``) - Class for fitting circular cross-sections around existing nodes of a Path in order to compute radii (node thickness) and midpoint refinement of existing coordinates.
* `PathManagerUI <../pysnt/pathmanagerui.html>`_ (``sc.fiji.snt``) - Implements the Path Manager Dialog.
* `PathProfiler <../pysnt/analysis/pathprofiler.html>`_ (``sc.fiji.snt.analysis``) - Command to retrieve Path profiles (plots of voxel intensities values along a Path)
* `PathResult <../pysnt/tracing/pathresult.html>`_ (``sc.fiji.snt.tracing``) - Enhanced documentation for PathResult class.
* `PathStatistics <../pysnt/analysis/pathstatistics.html>`_ (``sc.fiji.snt.analysis``) - A specialized version of TreeStatistics for analyzing individual paths without considering their connectivity relationships.
* `PathStraightener <../pysnt/analysis/pathstraightener.html>`_ (``sc.fiji.snt.analysis``) - Command to "straighten" an image using Path coordinates.
* `PCAnalyzer <../pysnt/analysis/pcanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Utility class for performing Principal Component Analysis (PCA) on various SNT data structures including Trees, Paths, and collections of SNTPoints.
* `PersistenceAnalyzer <../pysnt/analysis/persistenceanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Performs persistent homology analysis on neuronal Trees.
* `PointInImage <../pysnt/util/pointinimage.html>`_ (``sc.fiji.snt.util``) - Defines a Point in an image, a node of a traced Path.

R
-

* `RemoteSWCLoader <../pysnt/io/remoteswcloader.html>`_ (``sc.fiji.snt.io``) - Importers downloading remote SWC files should extend this interface.
* `RootAngleAnalyzer <../pysnt/analysis/rootangleanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class to perform Root angle analysis on a Tree according to Bird and Cuntz 2019, PMID 31167149.

S
-

* `SciViewSNT <../pysnt/sciviewsnt.html>`_ (``sc.fiji.snt``) - Bridges SNT to SciView, allowing Trees to be rendered as scenery objects
* `SearchNode <../pysnt/tracing/searchnode.html>`_ (``sc.fiji.snt.tracing``) - Enhanced documentation for SearchNode class.
* `SearchThread <../pysnt/tracing/searchthread.html>`_ (``sc.fiji.snt.tracing``) - Implements a common thread that explores the image using a variety of strategies, e.
* `ShollAnalyzer <../pysnt/analysis/shollanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class to retrieve Sholl metrics from a Tree.
* `SkeletonConverter <../pysnt/analysis/skeletonconverter.html>`_ (``sc.fiji.snt.analysis``) - Class for generation of Trees from a skeletonized ImagePlus.
* `SNT <../pysnt/snt.html>`_ (``sc.fiji.snt``) - Implements the SNT plugin.
* `SNTChart <../pysnt/analysis/sntchart.html>`_ (``sc.fiji.snt.analysis``) - Extension of ChartPanel modified for scientific publications and convenience methods for plot annotations.
* `SNTColor <../pysnt/util/sntcolor.html>`_ (``sc.fiji.snt.util``) - A simple class for handling Colors including the ability to map an AWT Color to a SWC type integer tag.
* `SNTPoint <../pysnt/util/sntpoint.html>`_ (``sc.fiji.snt.util``) - Classes extend this interface implement a point in a 3D space, always using real world coordinates.
* `SNTService <../pysnt/sntservice.html>`_ (``sc.fiji.snt``) - Service for accessing and scripting the active instance of SNT.
* `SNTTable <../pysnt/analysis/snttable.html>`_ (``sc.fiji.snt.analysis``) - Extension of DefaultGenericTable with (minor) scripting conveniences.
* `SNTUI <../pysnt/sntui.html>`_ (``sc.fiji.snt``) - Implements SNT's main dialog.
* `SNTUtils <../pysnt/sntutils.html>`_ (``sc.fiji.snt``) - Static utilities for SNT
* `StrahlerAnalyzer <../pysnt/analysis/strahleranalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class to perform Horton-Strahler analysis on a Tree.
* `SWCPoint <../pysnt/util/swcpoint.html>`_ (``sc.fiji.snt.util``) - Defines a node in an SWC reconstruction.

T
-

* `TracerCanvas <../pysnt/tracercanvas.html>`_ (``sc.fiji.snt``) - Provides rendering capabilities for visualizing paths, overlays, and additional interactive elements in an ImageJ canvas.
* `TracerThread <../pysnt/tracing/tracerthread.html>`_ (``sc.fiji.snt.tracing``) - SNT's default tracer thread: explores between two points in an image, doing an A* search with a choice of distance measures.
* `Tree <../pysnt/tree.html>`_ (``sc.fiji.snt``) - Utility class to access a Collection of Paths (typically a complete reconstruction).
* `TreeColorMapper <../pysnt/analysis/treecolormapper.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding Trees.
* `TreeProperties <../pysnt/treeproperties.html>`_ (``sc.fiji.snt``) - Allows standardized metadata to be associated to a Tree.
* `TreeStatistics <../pysnt/analysis/treestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from properties of Paths and Nodes in a Tree, including convenience methods to plot distributions of such data.
* `Tubeness <../pysnt/filter/tubeness.html>`_ (``sc.fiji.snt.filter``) - Y.

V
-

* `VFBUtils <../pysnt/annotation/vfbutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing/handling Virtual Fly Brain (VFB) annotations
* `Viewer2D <../pysnt/viewer/viewer2d.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering Trees as 2D plots that can be exported as SVG, PNG or PDF.
* `Viewer3D <../pysnt/viewer/viewer3d.html>`_ (``sc.fiji.snt.viewer``) - Implements SNT's Reconstruction Viewer.

W
-

* `WekaModelLoader <../pysnt/io/wekamodelloader.html>`_ (``sc.fiji.snt.io``) - GUI command for Loading pre-trained models from Labkit/TWS as secondary image layer.

Z
-

* `ZBAtlasUtils <../pysnt/annotation/zbatlasutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing the Max Plank Zebrafish Brain Atlas (ZBA) at fishatlas.


See Also
--------

* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
* :doc:`API Documentation </api_auto/index>`
