# SNT inventory: 5.0.24-SNAPSHOT-736f024779a9b422e04cb45087f01d8994a338ca

Generated 2026-10-31T22:28:04 from `org.morphonets:SNT:5.0.24-SNAPSHOT`

## Coverage by package

| package | public | curated | extended | missing | skipped | unloadable |
|---|---|---|---|---|---|---|
| . | 50 | 15 | 11 | 24 | 0 | 1 |
| ..analysis | 45 | 21 | 7 | 17 | 0 | 0 |
| ..analysis.curation | 35 | 0 | 0 | 35 | 0 | 0 |
| ..analysis.detection | 8 | 0 | 0 | 8 | 0 | 0 |
| ..analysis.graph | 11 | 4 | 6 | 1 | 0 | 0 |
| ..analysis.growth | 10 | 2 | 1 | 7 | 0 | 0 |
| ..analysis.sholl | 4 | 3 | 1 | 0 | 0 | 0 |
| ..analysis.sholl.gui | 3 | 3 | 0 | 0 | 0 | 0 |
| ..analysis.sholl.math | 8 | 4 | 1 | 3 | 0 | 0 |
| ..analysis.sholl.parsers | 6 | 3 | 3 | 0 | 0 | 0 |
| ..annotation | 9 | 6 | 0 | 3 | 0 | 0 |
| ..event | 2 | 0 | 0 | 2 | 0 | 0 |
| ..filter | 5 | 2 | 2 | 1 | 0 | 0 |
| ..gui | 73 | 0 | 0 | 73 | 0 | 0 |
| ..gui.cmds | 66 | 0 | 0 | 0 | 66 | 0 |
| ..hyperpanes | 3 | 0 | 0 | 3 | 0 | 0 |
| ..io | 16 | 7 | 3 | 6 | 0 | 0 |
| ..plugin | 48 | 0 | 0 | 0 | 48 | 0 |
| ..plugin.ij1 | 2 | 0 | 0 | 0 | 2 | 0 |
| ..seed | 13 | 0 | 0 | 13 | 0 | 0 |
| ..tracing | 13 | 7 | 4 | 2 | 0 | 0 |
| ..tracing.artist | 5 | 4 | 1 | 0 | 0 | 0 |
| ..tracing.auto | 17 | 0 | 0 | 17 | 0 | 0 |
| ..tracing.auto.gwdt | 4 | 0 | 0 | 4 | 0 | 0 |
| ..tracing.cost | 6 | 4 | 1 | 1 | 0 | 0 |
| ..tracing.heuristic | 3 | 3 | 0 | 0 | 0 | 0 |
| ..tracing.image | 9 | 5 | 1 | 3 | 0 | 0 |
| ..util | 37 | 9 | 9 | 19 | 0 | 0 |
| ..viewer | 27 | 5 | 2 | 20 | 0 | 0 |
| ..viewer.geditor | 12 | 0 | 0 | 12 | 0 | 0 |
| **total** | 550 | 107 | 53 | 274 | 116 | 1 |

## Missing from PySNT (public, not skipped)

- `.`: AStarRefiner, CurationManager, FillConverter_ResultType, FillManagerUI_State, Fill_Node, MultiPathTracerCanvas, MultiPathTracerCanvas_Entry, PathAndFillManager_AllPointsIterator, PathAndFillManager_NodeRef, PathNodeEditor, PathNodeEditor_Result, Path_PathNode, SNTUtils_BackgroundTask, SNTUtils_HeapInfo, SNT_CostType, SNT_FilterType, SNT_HeuristicType, SNT_MaterializedCrop, SNT_SearchImageType, SNT_SearchSettingsSnapshot, SNT_SearchType, SNT_VoxelBounds, SeedManager, SeedOverlayRenderer
- `..analysis`: CandidatePathMetrics, CandidatePathMetrics_Metric, CandidatePathMetrics_Metric_Kind, CircularModels_Domain, CircularModels_VonMisesFit, MultiSpectralRefiner, MultiSpectralRefiner_Parameters, NodeCollector, NodeCollector_Projection, PCAnalyzer_PrincipalAxis, PeripathDetector, PeripathDetector_Config, PeripathDetector_Detection, ProfileProcessor_Metric, ProfileProcessor_Shape, TreeAnalyzer, UnknownMetricException
- `..analysis.curation`: CurationHistograms, CurationHistograms_Side, CurationTags, CurationTags_Partition, PlausibilityCalibrator, PlausibilityCalibrator_CalibrationResult, PlausibilityCalibrator_CheckSummary, PlausibilityCheck, PlausibilityCheck_BoundaryProximity, PlausibilityCheck_BranchAngle, PlausibilityCheck_BundledPaths, PlausibilityCheck_ConstantRadii, PlausibilityCheck_Crossovers, PlausibilityCheck_DeepCheck, PlausibilityCheck_DirectionContinuity, PlausibilityCheck_ImpactKind, PlausibilityCheck_IntensityValley, PlausibilityCheck_InterForkDistance, PlausibilityCheck_InvalidRadius, PlausibilityCheck_LiveCheck, PlausibilityCheck_Measurements, PlausibilityCheck_RadiusContinuity, PlausibilityCheck_RadiusJumps, PlausibilityCheck_RadiusMonotonicity, PlausibilityCheck_Severity, PlausibilityCheck_SignalQuality, PlausibilityCheck_SomaDistance, PlausibilityCheck_TerminalBranchLength, PlausibilityCheck_TerminalNearAncestor, PlausibilityCheck_TortuosityConsistency, PlausibilityCheck_UncertainTerminal, PlausibilityCheck_Warning, PlausibilityCheck_ZExtentRatio, PlausibilityMonitor, PlausibilityMonitor_WarningListener
- `..analysis.detection`: AlongPathDetector, AlongPathDetector_Config, Detection, DetectorUtils, LabelProximityDetector, LabelProximityDetector_Config, PeripathDetector, PeripathDetector_Config
- `..analysis.graph`: SparseDirectedWeightedGraph
- `..analysis.growth`: GrowthAnalysisResults_GrowthSummaryStatistics, GrowthAnalysisResults_NeuriteSelectionCriterion, GrowthAnalyzer_ElongationEvent, GrowthAnalyzer_GrowthPhase, GrowthAnalyzer_GrowthPhaseType, GrowthAnalyzer_RetractionEvent, GrowthAnalyzer_TimePoint
- `..analysis.sholl.math`: PolarProfileStats_PolarPeak, PolarProfileStats_Report, ShollStats_DataMode
- `..annotation`: BrainAnnotation, DrosophilaCompartment, DrosophilaUtils
- `..event`: SNTEvent, SNTListener
- `..filter`: SpectralSimilarity
- `..gui`: CalloutManager, CheckboxSpinner, CollapsiblePanel, ColorChangedListener, ColorChooserButton, ColorMenu, ComponentMover, ContextMenuCommand, ContextMenuCommand_Labels, CostPalette, CostPalette_Listener, DemoRunner, DemoRunner_Demo, EnhancedGenericDialog, FileChooser, FileDrop, FileDrop_Listener, FileDrop_TransferableObject_Fetcher, FilePicker, GuiUtils, GuiUtils_Buttons, GuiUtils_Buttons_OptionsButton, GuiUtils_Buttons_StackedButton, GuiUtils_ChoiceAction, GuiUtils_Colors, GuiUtils_Fields, GuiUtils_LAF, GuiUtils_MenuItems, GuiUtils_Notices, GuiUtils_Notices_PendingNotice, GuiUtils_Panels, GuiUtils_ScrollPanes, GuiUtils_SplitPanes, GuiUtils_Tables, GuiUtils_Tables_BarCellRenderer, GuiUtils_Tables_BestCellRenderer, GuiUtils_Tables_DetachableTable, GuiUtils_Text, GuiUtils_Toolbars, GuiUtils_Trees, GuiUtils_VisitingZoom, GuiUtils_Windows, GuidedTutorial, GuidedTutorial_Step, IconActionableMenuItem, IconFactory, IconFactory_GLYPH, MaterializeRegionDialog, MeasureUI, NodeEditCommand, NodeEditCommand_MenuState, OntologyBrowser, OntologyBrowser_AllenCCFRenderer, OntologyBrowser_OntologyTab, PaletteOptions, PathManagerUISearchableBar, SNTCommandFinder, SNTEditorPane, SNTInterpreterPane, SNTInterpreterWindow, SNTPromptPane, SNTREPL, SNTSearchableBar, SWCExportDialog, SWCImportDialog, ScriptInstaller, ScriptRecorder, SearchField, SigmaPalette, SigmaPaletteListener, TagChips, TagUtils, XYZFieldsPanel
- `..hyperpanes`: MultiDThreePanes, MultiDThreePanesCanvas, PaneOwner
- `..io`: InsectBrainLoader_NeuronInfo, NeurolucidaImporter, SpimDataUtils, SpimDataUtils_CalibratedSource, SpimDataUtils_ChannelData, SpimDataUtils_N5Sources
- `..seed`: LabelsToSeeds, SeedConfidence, SeedOverlay, SeedOverlayBigViewerHandler, SeedOverlayCanvasHandler, SeedOverlay_ColorMode, SeedOverlay_CsvHeaderException, SeedOverlay_CsvImportResult, SeedOverlay_SeedOverlayListener, SeedPoint, SeedPointEditDialog, SeedRois, SeedTableModel
- `..tracing`: BiSearchNode_State, CrossSectionUtils
- `..tracing.auto`: AbstractAutoTracer, AbstractGWDTTracer, AbstractGWDTTracer_WaypointBiasSource, AutoTraceConfig, AutoTracer, AutoTracer_SeedRole, BinaryTracer, ComponentReconnector, DiskBackedGWDTTracer, GWDTTracer, GWDTTracerFactory, RootDetector, SomaUtils, SomaUtils_SomaResult, SparseGWDTTracer, TuftDetector, TuftDetector_Type
- `..tracing.auto.gwdt`: ArrayStorageBackend, DiskBackedStorageBackend, SparseStorageBackend, StorageBackend
- `..tracing.cost`: OneMinusErfFloor
- `..tracing.image`: SupplierUtil_ArraySearchImageSupplier, SupplierUtil_ListSearchImageSupplier, SupplierUtil_MapSearchImageSupplier
- `..util`: BundleDetector, BundleDetector_Config, CrossoverFinder_Config, CrossoverFinder_CrossoverEvent, GLUtils, GLUtils_Info, IOUtils, IOUtils_ReconstructionFormat, ImgUtils_MaxProjection, ImgUtils_OmeZarrCalibration, ImgUtils_SliceResult, Integration, MeshUtils, MeshUtils_Material, PointDeduplicator, TreeToRaster, TreeUtils, TreeUtils_EndpointClusterAnalysis, TreeUtils_EndpointMatch
- `..viewer`: AbstractBigViewer, AbstractBigViewer_AnnotationOverlay, AbstractBigViewer_PathRenderingOptions, AbstractBigViewer_PathRenderingOptions_Style, AbstractBigViewer_RecenterStrategy, Bdv, BvvMultiSource, BvvProfiler, BvvUtils, BvvUtils_RenderQuality, Bvv_AnnotationOverlay, Keyframe, Keyframe_SourceDisplay, OBJMesh, PathPlayer, UnmixEngine_Host, Viewer3D_AnimationMode, Viewer3D_ManagerPanel, Viewer3D_RotationAxis, Viewer3D_ViewMode
- `..viewer.geditor`: AnnotationGraphAdapter, AnnotationGraphComponent, GraphEditor, SNTGraphAdapter, SNTGraphComponent, SNTPseudographAdapter, SNTPseudographComponent, TreeGraphAdapter, TreeGraphComponent, mxCircleLayoutGrouped, mxCircleLayoutScaled, mxCircleLayoutSorted

## Stale PySNT entries

- `..InteractiveTracerCanvas` (curated): not_public
- `..PathChangeListener` (curated): not_public
- `..ClarifyingKeyListener` (extended): not_public
- `..FittingProgress` (extended): not_public
- `..MultiTaskProgress` (extended): not_public
- `..NormalPlaneCanvas` (extended): not_public
- `..PathAndFillListener` (extended): not_public
- `..PathChangeEvent` (extended): not_public
- `..PathChangeListener` (extended): not_public
- `..QueueJumpingKeyListener` (extended): not_public
- `..analysis.SkeletonConverter` (curated): absent
- `..analysis.sholl.math.CommonStats` (extended): not_public
- `..gui.FigCreatorCmd` (curated): absent
- `..tracing.PathResult` (curated): not_public
- `..viewer.ColorTableMapper` (extended): not_public
- `..test.example.BranchAnalyzer` (curated): no_such_java_package
- `..test.example.ExampleAnalyzer` (curated): no_such_java_package
- `..test.example.MorphologyAnalyzer` (curated): no_such_java_package
- `..test.example.ShapeMetrics` (curated): no_such_java_package
- `..test.example.TestClass` (curated): no_such_java_package
- `..test.example.AdvancedMorphology` (extended): no_such_java_package
- `..test.example.AdvancedTest` (extended): no_such_java_package
- `..test.example.DetailedMetrics` (extended): no_such_java_package
- `..test.example.InternalUtils` (extended): no_such_java_package

## Deprecated types

- `..analysis.PeripathDetector_Config` 
- `..analysis.PeripathDetector_Detection` 
- `..analysis.PeripathDetector` Use {@link sc.fiji.snt.analysis.detection.PeripathDetector} instead. This class is retained for backward compatibility and delegates all calls to the new package.
- `..analysis.TreeAnalyzer` Use {@link TreeStatistics} instead
- `..gui.EnhancedGenericDialog` 
- `..plugin.AnalyzerCmd` replaced by {@link sc.fiji.snt.gui.MeasureUI }

## Deprecated methods

### `..Path`
- `addDiscsTo3DViewer(Image3DUniverse univ, Color3f c, ImagePlus colorImage)` 
- `addDiscsTo3DViewer(Image3DUniverse univ, Color c, ImagePlus colorImage)` 
- `getStartJoinsPoint()` Use {@link #getBranchPoint()} instead. * <p> NB: Earlier versions of Simple Neurite Tracer allowed paths to connect at either the start point (getStartJoinsPoint()) or end-point (getStartJoinsPoint()). Useful for some applications but a huge headache to handle. </p>
- `getJunctionNodes()` use {@link #getBranchPoints()} instead
- `removeFrom3DViewer(Image3DUniverse univ)` This method is deprecated. Use newer 3D visualization methods instead.
- `addAsLinesTo3DViewer(Image3DUniverse univ, Color c, ImagePlus colorImage)` 
- `getPoint3fList()` 
- `getStartJoins()` use {@link #getParentPath()} instead
- `createCircles()` No longer needed - radii and tangents are now stored per-node
- `setStartJoin(Path parentPath, PointInImage branchPoint)` use {@link #setBranchFrom(Path, PointInImage)} instead
- `unsetStartJoin()` 
- `versionInUse()` Use {@link #isActiveVersion()} instead
- `addTo3DViewer(Image3DUniverse univ, Color3f c, ImagePlus colorImage)` This method is deprecated. Use newer 3D visualization methods instead.
- `addTo3DViewer(Image3DUniverse univ, Color c, ImagePlus colorImage)` This method is deprecated. Use newer 3D visualization methods instead.
- `interpolateMissingRadii(DoublePredicate predicate, boolean apply)` Use {@link #sanitizeRadii(DoublePredicate, boolean)} instead

### `..PathAndFillManager`
- `contentSelected(Content c)` 
- `universeClosed()` 
- `contentAdded(Content c)` 
- `contentChanged(Content c)` 
- `contentRemoved(Content c)` 
- `canvasResized()` 

### `..SNT`
- `showCorrespondencesTo(File tracesFile, Color c, double maxDistance)` 
- `startHessian(String image, double sigma, double max, boolean wait)` 

### `..SNTService`
- `getAnalyzer(boolean selectedPathsOnly)` Use {@link #getStatistics(boolean)} instead
- `demoTreeImage()` 
- `demoTree()` 
- `getPlugin()` use {@link #getInstance()} instead

### `..SNTUtils`
- `getPluginInstance()` use {@link #getInstance()} instead

### `..Tree`
- `assignUniqueColors(Collection trees, String excludedHue)` use {@link TreeUtils#assignUniqueColors(Collection)}
- `assignUniqueColors(Collection trees)` use {@link TreeUtils#assignUniqueColors(Collection)}
- `downSample(double internodeSpacing)` Use {@link #downsample(double)} instead.

### `..analysis.PeripathDetector`
- `createTorusMask(Collection paths, ImagePlus output, Config cfg, double fillValue)` Use {@link sc.fiji.snt.analysis.detection.PeripathDetector#createTorusMask} instead.
- `createTorusMask(Collection paths, RandomAccessibleInterval output, Config cfg, double fillValue)` Use {@link sc.fiji.snt.analysis.detection.PeripathDetector#createTorusMask} instead.
- `detect(Collection paths, RandomAccessibleInterval img, Config cfg)` Use {@link sc.fiji.snt.analysis.detection.PeripathDetector#detect} instead.

### `..analysis.SNTChart`
- `setVisible(boolean b)` 

### `..analysis.TreeStatistics`
- `getMetrics()` 

### `..analysis.graph.GraphUtils`
- `getSimplifiedGraph(DirectedWeightedGraph graph)` 
- `createTree(Graph graph)` 
- `createGraph(Collection nodes, boolean assignDistancesToWeights)` 
- `createGraph(Tree tree)` 

### `..hyperpanes.MultiDThreePanesCanvas`
- `setCrosshairs(double x, double y, double z, boolean display)` 

### `..plugin.StrahlerCmd`
- `getTable()` Use {@link #getSummaryTable()} instead

### `..tracing.auto.AbstractGWDTTracer`
- `setMinSegmentLength(double lengthInPhysicalUnits)` Use {@link #setMinBranchIntensityLength(double)} instead. Note: the physical-to-voxel conversion is not meaningful for this parameter since it is an intensity sum, not a distance.
- `setMinSegmentLengthVoxels(double lengthInVoxels)` Use {@link #setMinBranchIntensityLength(double)} instead.

### `..util.ImgUtils`
- `imgPlusToCalibration(ImgPlus imgPlus)` Use {@link #getCalibration(ImgPlus)} instead

### `..util.TreeToRaster`
- `rasterizeLabels()` Use {@link #rasterizePathLabels()} instead

### `..viewer.MultiViewer2D`
- `setLabel(String label)` 

### `..viewer.OBJMesh`
- `getLabel()` use {@link #label} instead

### `..viewer.Viewer2D`
- `addTrees(Collection trees)` use {@link #add(Object)} instead
- `addTree(Tree tree)` Use {@link #add(Object)} instead
- `showPlot()` Use {@link #show()} instead.

### `..viewer.Viewer3D`
- `addTrees(Collection trees, boolean assignUniqueColors)` use {@link #addTrees(Collection, String)} instead

## Classes that failed to load

- `..SciViewSNT_ShapeTree`: java.lang.NoClassDefFoundError: java.lang.NoClassDefFoundError: graphics/scenery/Mesh

## Classes whose methods could not be reflected

- `..SciViewSNT`: java.lang.NoClassDefFoundError: java.lang.NoClassDefFoundError: graphics/scenery/Node
- `..gui.DemoRunner`: java.lang.NoClassDefFoundError: java.lang.NoClassDefFoundError: bvv/core/VolumeViewerFrame
- `..gui.EnhancedGenericDialog`: java.lang.VerifyError: java.lang.VerifyError: Bad type on operand stack
- `..viewer.Bvv`: java.lang.NoClassDefFoundError: java.lang.NoClassDefFoundError: bvv/vistools/BvvSource
- `..viewer.BvvMultiSource`: java.lang.NoClassDefFoundError: java.lang.NoClassDefFoundError: bvv/vistools/BvvStackSource
- `..viewer.BvvUtils`: java.lang.NoClassDefFoundError: java.lang.NoClassDefFoundError: bvv/core/VolumeViewerPanel
