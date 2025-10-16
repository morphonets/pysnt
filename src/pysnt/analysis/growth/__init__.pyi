"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set

class GrowthAnalyzer:
    """
    SNT GrowthAnalyzer class with complete method signatures.
    Generated using Java reflection.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None: ...

    # Fields
    DEFAULT_BASE_THRESHOLD_FRACTION: float
    DEFAULT_RAPID_THRESHOLD_MULTIPLE: float
    DEFAULT_PHASE_SENSITIVITY: float
    DEFAULT_RETRACTION_THRESHOLD: float
    DEFAULT_MIN_PATH_LENGTH: float
    DEFAULT_MIN_TIME_POINTS: int
    DEFAULT_WINDOW_SIZE_FRACTION: float
    DEFAULT_ABSOLUTE_WINDOW_SIZE: int
    DEFAULT_USE_ABSOLUTE_WINDOW_SIZE: bool
    DEFAULT_USE_GLOBAL_THRESHOLDS: bool
    TAG_REGEX_PATTERN: str

    # Methods
    def analyze(self, arg0: List[Any], arg1: float, arg2: str) -> Any: ...
    def getAbsoluteWindowSize(self) -> int: ...
    def getBaseThresholdFraction(self) -> float: ...
    def getPhaseSensitivity(self) -> float: ...
    def getRapidThresholdMultiple(self) -> float: ...
    def getRetractionThreshold(self) -> float: ...
    def getWindowSizeFraction(self) -> float: ...
    def isUseAbsoluteWindowSize(self) -> bool: ...
    def isUseGlobalThresholds(self) -> bool: ...
    def setAbsoluteWindowSize(self, arg0: int) -> None: ...
    def setMinPathLength(self, arg0: float) -> None: ...
    def setMinTimePoints(self, arg0: int) -> None: ...
    def setPhaseSensitivity(self, arg0: float) -> None: ...
    def setPlateauThreshold(self, arg0: float) -> None: ...
    def setRapidThreshold(self, arg0: float) -> None: ...
    def setRetractionThreshold(self, arg0: float) -> None: ...
    def setUseAbsoluteWindowSize(self, arg0: bool) -> None: ...
    def setUseGlobalThresholds(self, arg0: bool) -> None: ...
    def setWindowSizeFraction(self, arg0: float) -> None: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

class GrowthChart:
    """
    SNT GrowthChart class.
    
    This class provides access to the Java GrowthChart functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the GrowthChart."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class GrowthStatistics:
    """
    SNT GrowthStatistics class.
    
    This class provides access to the Java GrowthStatistics functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the GrowthStatistics."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class GrowthUtils:
    """
    SNT GrowthUtils class.
    
    This class provides access to the Java GrowthUtils functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the GrowthUtils."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

# Module functions
def get_available_classes() -> List[str]: ...
def get_class(class_name: str) -> Any: ...
def list_classes() -> None: ...
def get_curated_classes() -> List[str]: ...
def get_extended_classes() -> List[str]: ...

CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]