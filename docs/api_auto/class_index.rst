
Class Index
===========

This page provides an index of all classes available in the SNT API.

Total classes: **158**


A
-

* `AllenCompartment <../pysnt/annotation/allencompartment.html>`_ (``sc.fiji.snt.annotation``) - Defines an Allen Reference Atlas (ARA) [Allen Mouse Common Coordinate Framework] annotation.
* `AllenUtils <../pysnt/annotation/allenutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing/handling `AllenCompartment`s
* `AlongPathDetector <../pysnt/analysis.detection/alongpathdetector.html>`_ (``sc.fiji.snt.analysis.detection``) - Enhanced documentation for AlongPathDetector class.
* `Annotation3D <../pysnt/viewer/annotation3d.html>`_ (``sc.fiji.snt.viewer``) - An Annotation3D is a triangulated surface or a cloud of points (scatter) rendered in ``Viewer3D`` that can be used to highlight nodes in a ``Tree`` or locations in a ``mesh``.
* `AnnotationGraph <../pysnt/analysis.graph/annotationgraph.html>`_ (``sc.fiji.snt.analysis.graph``) - Enhanced documentation for AnnotationGraph class.
* `ArraySearchImage <../pysnt/tracing.image/arraysearchimage.html>`_ (``sc.fiji.snt.tracing.image``) - Enhanced documentation for ArraySearchImage class.
* `ArrayStorageBackend <../pysnt/tracing.auto.gwdt/arraystoragebackend.html>`_ (``sc.fiji.snt.tracing.auto.gwdt``) - Enhanced documentation for ArrayStorageBackend class.
* `AStarRefiner <../pysnt/astarrefiner.html>`_ (``sc.fiji.snt``) - Post-hoc A* re-tracing of a single, already-existing ``Path``: treats the path's current nodes as waypoints and re-derives the geometry between them via
* `AutoTraceConfig <../pysnt/tracing.auto/autotraceconfig.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for AutoTraceConfig class.
* `AutoTracer <../pysnt/tracing.auto/autotracer.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for AutoTracer class.

B
-

* `Bdv <../pysnt/viewer/bdv.html>`_ (``sc.fiji.snt.viewer``) - SNT's BigDataViewer-based 2D slice viewer.
* `BinaryTracer <../pysnt/tracing.auto/binarytracer.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for BinaryTracer class.
* `BiSearch <../pysnt/tracing/bisearch.html>`_ (``sc.fiji.snt.tracing``) - A flexible implementation of the bidirectional heuristic search algorithm described in Pijls, W.
* `BiSearchArtist <../pysnt/tracing.artist/bisearchartist.html>`_ (``sc.fiji.snt.tracing.artist``) - Enhanced documentation for BiSearchArtist class.
* `BiSearchNode <../pysnt/tracing/bisearchnode.html>`_ (``sc.fiji.snt.tracing``) - A ``SearchNode`` which can maintain both a from-start and from-goal search state.
* `BookmarkManager <../pysnt/bookmarkmanager.html>`_ (``sc.fiji.snt``) - Implements the *Bookmark Manager* pane.
* `BoundingBox <../pysnt/util/boundingbox.html>`_ (``sc.fiji.snt.util``) - A BoundingBox contains information (including spatial calibration) of a tracing canvas bounding box, i.
* `BundleDetector <../pysnt/util/bundledetector.html>`_ (``sc.fiji.snt.util``) - Detects regions where two paths run *parallel* to each other for a sustained distance, complementary to ``CrossoverFinder`` (which catches brief perpendicular near-crossings).
* `Bvv <../pysnt/viewer/bvv.html>`_ (``sc.fiji.snt.viewer``) - Support for Big Volume Viewer.
* `BvvMultiSource <../pysnt/viewer/bvvmultisource.html>`_ (``sc.fiji.snt.viewer``) - A group of ``BvvSource`` objects that are treated as a logical unit: display properties (color, range, active state) and manual transforms applied to the *leader* source are propagated to all *follower* sources.
* `BvvUtils <../pysnt/viewer/bvvutils.html>`_ (``sc.fiji.snt.viewer``) - Package-private utility methods shared across BVV-related classes (``Bvv``, ``ChannelUnmixingCard``, etc.

C
-

* `ColorMaps <../pysnt/util/colormaps.html>`_ (``sc.fiji.snt.util``) - Utilities for colormaps and IJ lookup tables
* `ConvexHull2D <../pysnt/analysis/convexhull2d.html>`_ (``sc.fiji.snt.analysis``) - Computes the convex hull of a set of 2D points.
* `ConvexHull3D <../pysnt/analysis/convexhull3d.html>`_ (``sc.fiji.snt.analysis``) - Convex hull analysis in 3D.
* `ConvexHullAnalyzer <../pysnt/analysis/convexhullanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class for Convex Hull measurements of a ``Tree``.
* `CrossoverFinder <../pysnt/util/crossoverfinder.html>`_ (``sc.fiji.snt.util``) - Utility to detect crossover locations between paths: spatially close locations between paths that look like intersections in the image but are not topological joins in the traced graph.
* `CrossSectionUtils <../pysnt/tracing/crosssectionutils.html>`_ (``sc.fiji.snt.tracing``) - Static utilities for computing cross-sectional planes perpendicular to a path tangent.
* `CurationManager <../pysnt/curationmanager.html>`_ (``sc.fiji.snt``) - Implements the *Curation Assistant* pane in SNT's UI.

D
-

* `DefaultSearchNode <../pysnt/tracing/defaultsearchnode.html>`_ (``sc.fiji.snt.tracing``) - A ``SearchNode`` which can maintain both a from-start and from-goal search state.
* `DelineationsManager <../pysnt/delineationsmanager.html>`_ (``sc.fiji.snt``) - Implements the *Delineation Analysis* pane.
* `Detection <../pysnt/analysis.detection/detection.html>`_ (``sc.fiji.snt.analysis.detection``) - Enhanced documentation for Detection class.
* `DetectorUtils <../pysnt/analysis.detection/detectorutils.html>`_ (``sc.fiji.snt.analysis.detection``) - Enhanced documentation for DetectorUtils class.
* `Difference <../pysnt/tracing.cost/difference.html>`_ (``sc.fiji.snt.tracing.cost``) - Enhanced documentation for Difference class.
* `DifferenceSq <../pysnt/tracing.cost/differencesq.html>`_ (``sc.fiji.snt.tracing.cost``) - Enhanced documentation for DifferenceSq class.
* `Dijkstra <../pysnt/tracing.heuristic/dijkstra.html>`_ (``sc.fiji.snt.tracing.heuristic``) - Enhanced documentation for Dijkstra class.
* `DirectedWeightedGraph <../pysnt/analysis.graph/directedweightedgraph.html>`_ (``sc.fiji.snt.analysis.graph``) - Enhanced documentation for DirectedWeightedGraph class.
* `DirectedWeightedSubgraph <../pysnt/analysis.graph/directedweightedsubgraph.html>`_ (``sc.fiji.snt.analysis.graph``) - Enhanced documentation for DirectedWeightedSubgraph class.
* `DiskBackedGWDTTracer <../pysnt/tracing.auto/diskbackedgwdttracer.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for DiskBackedGWDTTracer class.
* `DiskBackedStorageBackend <../pysnt/tracing.auto.gwdt/diskbackedstoragebackend.html>`_ (``sc.fiji.snt.tracing.auto.gwdt``) - Enhanced documentation for DiskBackedStorageBackend class.

E
-

* `Euclidean <../pysnt/tracing.heuristic/euclidean.html>`_ (``sc.fiji.snt.tracing.heuristic``) - Enhanced documentation for Euclidean class.

F
-

* `Fill <../pysnt/fill.html>`_ (``sc.fiji.snt``) - Defines a filled structure.
* `FillConverter <../pysnt/fillconverter.html>`_ (``sc.fiji.snt``) - Map filled nodes from a ``Collection`` of `FillerThread`s to and between `RandomAccessible`s.
* `FillerThread <../pysnt/tracing/fillerthread.html>`_ (``sc.fiji.snt.tracing``) - Seeded-volume segmentation via single-source shortest paths.
* `FillerThreadArtist <../pysnt/tracing.artist/fillerthreadartist.html>`_ (``sc.fiji.snt.tracing.artist``) - Enhanced documentation for FillerThreadArtist class.
* `FillManagerUI <../pysnt/fillmanagerui.html>`_ (``sc.fiji.snt``) - Implements the *Fill Manager* dialog.
* `FlyCircuitLoader <../pysnt/io/flycircuitloader.html>`_ (``sc.fiji.snt.io``) - Absurdly simple importer for retrieving SWC data from FlyCircuit.
* `Frangi <../pysnt/filter/frangi.html>`_ (``sc.fiji.snt.filter``) - A.

G
-

* `GroupedTreeStatistics <../pysnt/analysis/groupedtreestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes statistics from ``Tree`` groups.
* `GrowthAnalysisResults <../pysnt/analysis.growth/growthanalysisresults.html>`_ (``sc.fiji.snt.analysis.growth``) - Enhanced documentation for GrowthAnalysisResults class.
* `GrowthAnalyzer <../pysnt/analysis.growth/growthanalyzer.html>`_ (``sc.fiji.snt.analysis.growth``) - Enhanced documentation for GrowthAnalyzer class.
* `GWDTTracer <../pysnt/tracing.auto/gwdttracer.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for GWDTTracer class.
* `GWDTTracerFactory <../pysnt/tracing.auto/gwdttracerfactory.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for GWDTTracerFactory class.

H
-

* `Heuristic <../pysnt/tracing.heuristic/heuristic.html>`_ (``sc.fiji.snt.tracing.heuristic``) - Enhanced documentation for Heuristic class.

I
-

* `ImageParser2D <../pysnt/analysis.sholl.parsers/imageparser2d.html>`_ (``sc.fiji.snt.analysis.sholl.parsers``) - Enhanced documentation for ImageParser2D class.
* `ImageParser3D <../pysnt/analysis.sholl.parsers/imageparser3d.html>`_ (``sc.fiji.snt.analysis.sholl.parsers``) - Enhanced documentation for ImageParser3D class.
* `ImgUtils <../pysnt/util/imgutils.html>`_ (``sc.fiji.snt.util``) - Static utilities for handling and manipulation of `RandomAccessibleInterval`s
* `ImpUtils <../pysnt/util/imputils.html>`_ (``sc.fiji.snt.util``) - Static utilities for handling and manipulation of `ImagePlus`s
* `InsectBrainCompartment <../pysnt/annotation/insectbraincompartment.html>`_ (``sc.fiji.snt.annotation``) - Returns the compartment's acronym.
* `InsectBrainLoader <../pysnt/io/insectbrainloader.html>`_ (``sc.fiji.snt.io``) - Methods for retrieving reconstructions and annotations from the Insect Brain Database at insectbraindb.
* `InsectBrainUtils <../pysnt/annotation/insectbrainutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for retrieving species, brain, and neuron data from the Insect Brain Database
* `InteractiveTracerCanvas <../pysnt/interactivetracercanvas.html>`_ (``sc.fiji.snt``) - Enhanced documentation for InteractiveTracerCanvas class.
* `IOUtils <../pysnt/util/ioutils.html>`_ (``sc.fiji.snt.util``) - Static utilities for file I/O, namely the detection of reconstruction file formats.

L
-

* `LabelProximityDetector <../pysnt/analysis.detection/labelproximitydetector.html>`_ (``sc.fiji.snt.analysis.detection``) - Enhanced documentation for LabelProximityDetector class.
* `LabelsToSeeds <../pysnt/seed/labelstoseeds.html>`_ (``sc.fiji.snt.seed``) - Enhanced documentation for LabelsToSeeds class.
* `LinearProfileStats <../pysnt/analysis.sholl.math/linearprofilestats.html>`_ (``sc.fiji.snt.analysis.sholl.math``) - Enhanced documentation for LinearProfileStats class.
* `ListSearchImage <../pysnt/tracing.image/listsearchimage.html>`_ (``sc.fiji.snt.tracing.image``) - Enhanced documentation for ListSearchImage class.

M
-

* `MapSearchImage <../pysnt/tracing.image/mapsearchimage.html>`_ (``sc.fiji.snt.tracing.image``) - Enhanced documentation for MapSearchImage class.
* `MouseLightLoader <../pysnt/io/mouselightloader.html>`_ (``sc.fiji.snt.io``) - Methods for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.
* `MouseLightQuerier <../pysnt/io/mouselightquerier.html>`_ (``sc.fiji.snt.io``) - Importer for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.
* `MultiSpectralRefiner <../pysnt/analysis/multispectralrefiner.html>`_ (``sc.fiji.snt.analysis``) - Post-hoc refinement of traced paths in multispectral (e.
* `MultiTreeColorMapper <../pysnt/analysis/multitreecolormapper.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding groups of `Tree`s.
* `MultiTreeStatistics <../pysnt/analysis/multitreestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from univariate properties of ``Tree`` groups.
* `MultiViewer2D <../pysnt/viewer/multiviewer2d.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering montages of `Tree`s as 2D plots that can be exported as SVG, PNG or PDF.
* `MultiViewer3D <../pysnt/viewer/multiviewer3d.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering individual `Viewer3D`s as a multi-panel montage.

N
-

* `NeurolucidaImporter <../pysnt/io/neurolucidaimporter.html>`_ (``sc.fiji.snt.io``) - Importer for Neurolucida XML files (Neuromorphological File Specification / NMF format).
* `NeuroMorphoLoader <../pysnt/io/neuromorpholoader.html>`_ (``sc.fiji.snt.io``) - Importer for retrieving SWC data from neuromorpho.
* `NodeColorMapper <../pysnt/analysis/nodecolormapper.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding of ``NodeStatistics`` results.
* `NodeProfiler <../pysnt/analysis/nodeprofiler.html>`_ (``sc.fiji.snt.analysis``) - Command to retrieve node profiles (plots of voxel intensities sampled across Path nodes).
* `NodeStatistics <../pysnt/analysis/nodestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from a Collection of nodes, including convenience methods to plot distributions of such data.
* `NormalizedProfileStats <../pysnt/analysis.sholl.math/normalizedprofilestats.html>`_ (``sc.fiji.snt.analysis.sholl.math``) - Enhanced documentation for NormalizedProfileStats class.

O
-

* `OBJMesh <../pysnt/viewer/objmesh.html>`_ (``sc.fiji.snt.viewer``) - An OBJMesh stores information about a Wavefront .
* `OneMinusErf <../pysnt/tracing.cost/oneminuserf.html>`_ (``sc.fiji.snt.tracing.cost``) - Enhanced documentation for OneMinusErf class.

P
-

* `Path <../pysnt/path.html>`_ (``sc.fiji.snt``) - This class represents a traced segment (i.
* `PathAndFillManager <../pysnt/pathandfillmanager.html>`_ (``sc.fiji.snt``) - The PathAndFillManager is responsible for importing, handling and managing of Paths and Fills.
* `PathChangeListener <../pysnt/pathchangelistener.html>`_ (``sc.fiji.snt``) - Enhanced documentation for PathChangeListener class.
* `PathDownsampler <../pysnt/pathdownsampler.html>`_ (``sc.fiji.snt``) - This is an implementation of the Ramer-Douglas-Peucker algorithm for simplifying a curve represented by line-segments, as described here
* `PathFitter <../pysnt/pathfitter.html>`_ (``sc.fiji.snt``) - Class for fitting circular cross-sections around existing nodes of a ``Path`` in order to compute radii (node thickness) and midpoint refinement of existing coordinates.
* `PathManagerUI <../pysnt/pathmanagerui.html>`_ (``sc.fiji.snt``) - Implements the *Path Manager* Dialog.
* `PathProfiler <../pysnt/analysis/pathprofiler.html>`_ (``sc.fiji.snt.analysis``) - Command to retrieve Path profiles (plots of voxel intensities values along a Path)
* `PathResult <../pysnt/tracing/pathresult.html>`_ (``sc.fiji.snt.tracing``) - Enhanced documentation for PathResult class.
* `PathStatistics <../pysnt/analysis/pathstatistics.html>`_ (``sc.fiji.snt.analysis``) - A specialized version of ``TreeStatistics`` for analyzing individual paths without considering their connectivity relationships.
* `PathStraightener <../pysnt/analysis/pathstraightener.html>`_ (``sc.fiji.snt.analysis``) - Command to "straighten" an image using Path coordinates.
* `PCAnalyzer <../pysnt/analysis/pcanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Utility class for performing Principal Component Analysis (PCA) on various SNT data structures including Trees, Paths, and collections of SNTPoints.
* `PeripathDetector <../pysnt/analysis.detection/peripathdetector.html>`_ (``sc.fiji.snt.analysis.detection``) - Deprecated.
* `PersistenceAnalyzer <../pysnt/analysis/persistenceanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Performs persistent homology analysis on neuronal `Tree`s.
* `PlausibilityCalibrator <../pysnt/analysis.curation/plausibilitycalibrator.html>`_ (``sc.fiji.snt.analysis.curation``) - Enhanced documentation for PlausibilityCalibrator class.
* `PlausibilityCheck <../pysnt/analysis.curation/plausibilitycheck.html>`_ (``sc.fiji.snt.analysis.curation``) - Enhanced documentation for PlausibilityCheck class.
* `PlausibilityMonitor <../pysnt/analysis.curation/plausibilitymonitor.html>`_ (``sc.fiji.snt.analysis.curation``) - Enhanced documentation for PlausibilityMonitor class.
* `PointInImage <../pysnt/util/pointinimage.html>`_ (``sc.fiji.snt.util``) - Defines a Point in an image, a node of a traced ``Path``.
* `PolarProfileStats <../pysnt/analysis.sholl.math/polarprofilestats.html>`_ (``sc.fiji.snt.analysis.sholl.math``) - Enhanced documentation for PolarProfileStats class.
* `Profile <../pysnt/analysis.sholl/profile.html>`_ (``sc.fiji.snt.analysis.sholl``) - Enhanced documentation for Profile class.
* `ProfileEntry <../pysnt/analysis.sholl/profileentry.html>`_ (``sc.fiji.snt.analysis.sholl``) - Enhanced documentation for ProfileEntry class.
* `ProfileProperties <../pysnt/analysis.sholl/profileproperties.html>`_ (``sc.fiji.snt.analysis.sholl``) - Enhanced documentation for ProfileProperties class.

R
-

* `Reciprocal <../pysnt/tracing.cost/reciprocal.html>`_ (``sc.fiji.snt.tracing.cost``) - Enhanced documentation for Reciprocal class.
* `RemoteSWCLoader <../pysnt/io/remoteswcloader.html>`_ (``sc.fiji.snt.io``) - Importers downloading remote SWC files should extend this interface.
* `RootAngleAnalyzer <../pysnt/analysis/rootangleanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class to perform Root angle analysis on a ``Tree`` according to Bird and Cuntz 2019, PMID 31167149.
* `RootDetector <../pysnt/tracing.auto/rootdetector.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for RootDetector class.

S
-

* `SciViewSNT <../pysnt/sciviewsnt.html>`_ (``sc.fiji.snt``) - Bridges SNT to SciView, allowing Trees to be rendered as scenery objects
* `SearchArtistFactory <../pysnt/tracing.artist/searchartistfactory.html>`_ (``sc.fiji.snt.tracing.artist``) - Enhanced documentation for SearchArtistFactory class.
* `SearchImageStack <../pysnt/tracing.image/searchimagestack.html>`_ (``sc.fiji.snt.tracing.image``) - Enhanced documentation for SearchImageStack class.
* `SearchNode <../pysnt/tracing/searchnode.html>`_ (``sc.fiji.snt.tracing``) - Interface representing a node in 3D space that can be used in pathfinding and search algorithms.
* `SearchThread <../pysnt/tracing/searchthread.html>`_ (``sc.fiji.snt.tracing``) - Implements a common thread that explores the image using a variety of strategies, e.
* `SearchThreadArtist <../pysnt/tracing.artist/searchthreadartist.html>`_ (``sc.fiji.snt.tracing.artist``) - Enhanced documentation for SearchThreadArtist class.
* `SeedConfidence <../pysnt/seed/seedconfidence.html>`_ (``sc.fiji.snt.seed``) - Enhanced documentation for SeedConfidence class.
* `SeedManager <../pysnt/seedmanager.html>`_ (``sc.fiji.snt``) - Reusable JPanel that controls a ``SeedOverlay``: visibility, LUT, confidence range, transparency, counters, CSV import/export/clear, plus an inline JTable for browsing and editing individual seeds.
* `SeedOverlay <../pysnt/seed/seedoverlay.html>`_ (``sc.fiji.snt.seed``) - Enhanced documentation for SeedOverlay class.
* `SeedOverlayRenderer <../pysnt/seedoverlayrenderer.html>`_ (``sc.fiji.snt``) - Stateless renderer that draws a ``SeedOverlay``'s seeds onto a ``TracerCanvas``'s ``Graphics2D``.
* `SeedPoint <../pysnt/seed/seedpoint.html>`_ (``sc.fiji.snt.seed``) - Enhanced documentation for SeedPoint class.
* `SeedRois <../pysnt/seed/seedrois.html>`_ (``sc.fiji.snt.seed``) - Enhanced documentation for SeedRois class.
* `ShollAnalyzer <../pysnt/analysis/shollanalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class to retrieve Sholl metrics from a ``Tree``.
* `ShollOverlay <../pysnt/analysis.sholl.gui/sholloverlay.html>`_ (``sc.fiji.snt.analysis.sholl.gui``) - Enhanced documentation for ShollOverlay class.
* `ShollPlot <../pysnt/analysis.sholl.gui/shollplot.html>`_ (``sc.fiji.snt.analysis.sholl.gui``) - Enhanced documentation for ShollPlot class.
* `ShollStats <../pysnt/analysis.sholl.math/shollstats.html>`_ (``sc.fiji.snt.analysis.sholl.math``) - Enhanced documentation for ShollStats class.
* `ShollTable <../pysnt/analysis.sholl.gui/sholltable.html>`_ (``sc.fiji.snt.analysis.sholl.gui``) - Enhanced documentation for ShollTable class.
* `SkeletonConverter <../pysnt/analysis/skeletonconverter.html>`_ (``sc.fiji.snt.analysis``) - Enhanced documentation for SkeletonConverter class.
* `SNT <../pysnt/snt.html>`_ (``sc.fiji.snt``) - Implements the SNT plugin.
* `SNTChart <../pysnt/analysis/sntchart.html>`_ (``sc.fiji.snt.analysis``) - Extension of ``ChartPanel`` modified for scientific publications and convenience methods for plot annotations.
* `SNTColor <../pysnt/util/sntcolor.html>`_ (``sc.fiji.snt.util``) - A simple class for handling Colors including the ability to map an AWT Color to a SWC type integer tag.
* `SNTGraph <../pysnt/analysis.graph/sntgraph.html>`_ (``sc.fiji.snt.analysis.graph``) - Enhanced documentation for SNTGraph class.
* `SNTPoint <../pysnt/util/sntpoint.html>`_ (``sc.fiji.snt.util``) - Classes extend this interface implement a point in a 3D space, always using real world coordinates.
* `SNTPrefs <../pysnt/sntprefs.html>`_ (``sc.fiji.snt``) - Class handling SNT preferences.
* `SNTService <../pysnt/sntservice.html>`_ (``sc.fiji.snt``) - Service for accessing and scripting the active instance of ``SNT``.
* `SNTTable <../pysnt/analysis/snttable.html>`_ (``sc.fiji.snt.analysis``) - Extension of ``DefaultGenericTable`` with (minor) scripting conveniences.
* `SNTUI <../pysnt/sntui.html>`_ (``sc.fiji.snt``) - Implements SNT's main dialog.
* `SNTUtils <../pysnt/sntutils.html>`_ (``sc.fiji.snt``) - Static utilities for SNT
* `SomaUtils <../pysnt/tracing.auto/somautils.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for SomaUtils class.
* `SparseGWDTTracer <../pysnt/tracing.auto/sparsegwdttracer.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for SparseGWDTTracer class.
* `SparseStorageBackend <../pysnt/tracing.auto.gwdt/sparsestoragebackend.html>`_ (``sc.fiji.snt.tracing.auto.gwdt``) - Enhanced documentation for SparseStorageBackend class.
* `SpectralSimilarity <../pysnt/filter/spectralsimilarity.html>`_ (``sc.fiji.snt.filter``) - Computes a spectral similarity map from a multichannel (e.
* `StrahlerAnalyzer <../pysnt/analysis/strahleranalyzer.html>`_ (``sc.fiji.snt.analysis``) - Class to perform Horton-Strahler analysis on a ``Tree``.
* `SupplierUtil <../pysnt/tracing.image/supplierutil.html>`_ (``sc.fiji.snt.tracing.image``) - Enhanced documentation for SupplierUtil class.
* `SWCPoint <../pysnt/util/swcpoint.html>`_ (``sc.fiji.snt.util``) - Defines a node in an SWC reconstruction.

T
-

* `TracerCanvas <../pysnt/tracercanvas.html>`_ (``sc.fiji.snt``) - Provides rendering capabilities for visualizing paths, overlays, and additional interactive elements in an ImageJ canvas.
* `TracerThread <../pysnt/tracing/tracerthread.html>`_ (``sc.fiji.snt.tracing``) - SNT's default tracer thread: explores between two points in an image, doing an A* search with a choice of distance measures.
* `Tree <../pysnt/tree.html>`_ (``sc.fiji.snt``) - Utility class to access a Collection of Paths (typically a complete reconstruction).
* `TreeColorMapper <../pysnt/analysis/treecolormapper.html>`_ (``sc.fiji.snt.analysis``) - Class for color coding `Tree`s.
* `TreeParser <../pysnt/analysis.sholl.parsers/treeparser.html>`_ (``sc.fiji.snt.analysis.sholl.parsers``) - Enhanced documentation for TreeParser class.
* `TreeProperties <../pysnt/treeproperties.html>`_ (``sc.fiji.snt``) - Allows standardized metadata to be associated to a ``Tree``.
* `TreeStatistics <../pysnt/analysis/treestatistics.html>`_ (``sc.fiji.snt.analysis``) - Computes summary and descriptive statistics from properties of Paths and Nodes in a ``Tree``, including convenience methods to plot distributions of such data.
* `TreeToRaster <../pysnt/util/treetoraster.html>`_ (``sc.fiji.snt.util``) - Rasterizes a ``Tree`` into a 3D image using frustum (truncated-cone) geometry with partial-volume supersampling.
* `TreeUtils <../pysnt/util/treeutils.html>`_ (``sc.fiji.snt.util``) - Static utilities for Trees.
* `Tubeness <../pysnt/filter/tubeness.html>`_ (``sc.fiji.snt.filter``) - Computes a tubeness (vesselness) filter on a multi-dimensional image using multi-scale eigenvalue analysis of the Hessian matrix.
* `TuftDetector <../pysnt/tracing.auto/tuftdetector.html>`_ (``sc.fiji.snt.tracing.auto``) - Enhanced documentation for TuftDetector class.

V
-

* `VFBUtils <../pysnt/annotation/vfbutils.html>`_ (``sc.fiji.snt.annotation``) - Utility methods for accessing/handling Virtual Fly Brain (VFB) annotations
* `Viewer2D <../pysnt/viewer/viewer2d.html>`_ (``sc.fiji.snt.viewer``) - Class for rendering `Tree`s as 2D plots that can be exported as SVG, PNG or PDF.
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
