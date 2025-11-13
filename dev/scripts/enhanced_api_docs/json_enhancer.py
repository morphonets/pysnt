"""
JSON stub enhancement engine for enhanced API documentation system.
Adds Javadoc documentation layer to existing JSON structure.
"""

import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime

from .javadoc_parser import MethodDocumentation, ClassDocumentation
from .json_stub_reader import JSONStubData, MethodInfo, MethodOverload
from .javadoc_json_matcher import JavaDocJSONMatcher, MethodMatch, ClassMatchResult
from .logging_setup import get_logger

logger = get_logger('json_enhancer')


@dataclass
class EnhancedParameterInfo:
    """Enhanced parameter information with JavaDoc documentation."""
    name: str
    type: str
    java_type: str
    description: str = ""
    javadoc_name: Optional[str] = None


@dataclass
class EnhancedMethodOverload:
    """Enhanced method overload with JavaDoc documentation."""
    signature: str
    params: List[EnhancedParameterInfo]
    return_type: str
    java_return_type: str
    return_description: str = ""
    throws: Dict[str, str] = None
    
    def __post_init__(self):
        if self.throws is None:
            self.throws = {}


@dataclass
class EnhancedMethodInfo:
    """Enhanced method information with JavaDoc documentation."""
    name: str
    overloads: List[EnhancedMethodOverload]
    documentation: str
    javadoc_description: str = ""
    category: str = "Utilities"
    deprecated: bool = False
    since_version: Optional[str] = None
    see_also: List[str] = None
    examples: List[str] = None
    
    def __post_init__(self):
        if self.see_also is None:
            self.see_also = []
        if self.examples is None:
            self.examples = []


@dataclass
class EnhancedJSONStubData:
    """Enhanced JSON stub data with JavaDoc documentation."""
    class_name: str
    package: str
    extracted_at: str
    extractor_version: str
    enhancement_timestamp: str
    enhancement_version: str
    
    # Original data
    methods: List[EnhancedMethodInfo]
    fields: List[Dict[str, Any]]  # Keep original field structure for now
    constructors: List[Dict[str, Any]]  # Keep original constructor structure for now
    
    # Enhanced data
    javadoc_description: str = ""
    inheritance: Dict[str, List[str]] = None
    nested_classes: List[str] = None
    deprecated: bool = False
    since_version: Optional[str] = None
    see_also: List[str] = None
    
    # Metadata
    enhancement_metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.inheritance is None:
            self.inheritance = {'extends': [], 'implements': []}
        if self.nested_classes is None:
            self.nested_classes = []
        if self.see_also is None:
            self.see_also = []
        if self.enhancement_metadata is None:
            self.enhancement_metadata = {}


class JSONStubEnhancer:
    """Enhances JSON stub files with JavaDoc documentation."""
    
    def __init__(self):
        """Initialize the enhancer."""
        self.logger = logger
        self.matcher = JavaDocJSONMatcher()
        self.enhancement_version = "1.0.0"
        
        # Method categorization patterns
        self.category_patterns = {
            'Getters': [
                r'^get[A-Z]', r'^is[A-Z]', r'^has[A-Z]', r'^can[A-Z]',
                r'.*[Cc]ount$', r'.*[Ss]ize$', r'.*[Ll]ength$'
            ],
            'Setters': [
                r'^set[A-Z]', r'^add[A-Z]', r'^remove[A-Z]', r'^clear[A-Z]',
                r'^enable[A-Z]', r'^disable[A-Z]', r'^toggle[A-Z]'
            ],
            'Analysis': [
                r'.*[Aa]nalyz', r'.*[Cc]alculat', r'.*[Mm]easur', r'.*[Cc]omput',
                r'.*[Ss]tatistic', r'.*[Mm]etric', r'.*[Ee]valuat'
            ],
            'I/O Operations': [
                r'^load[A-Z]', r'^save[A-Z]', r'^read[A-Z]', r'^write[A-Z]',
                r'^import[A-Z]', r'^export[A-Z]', r'.*[Ff]ile', r'.*[Pp]ath'
            ],
            'Visualization': [
                r'^draw[A-Z]', r'^render[A-Z]', r'^display[A-Z]', r'^show[A-Z]',
                r'^plot[A-Z]', r'^paint[A-Z]', r'.*[Cc]olor', r'.*[Vv]iew'
            ],
            'Static Methods': [
                r'^static\s+'
            ]
        }
    
    def enhance_json_stub(self, json_stub: JSONStubData, 
                         javadoc_class: Optional[ClassDocumentation] = None) -> EnhancedJSONStubData:
        """
        Enhance a JSON stub with JavaDoc documentation.
        
        Args:
            json_stub: Original JSON stub data
            javadoc_class: Optional JavaDoc class documentation
            
        Returns:
            Enhanced JSON stub data
        """
        self.logger.debug(f"Enhancing JSON stub for {json_stub.class_name}")
        
        # Create enhanced stub with basic information
        enhanced_stub = EnhancedJSONStubData(
            class_name=json_stub.class_name,
            package=json_stub.package,
            extracted_at=json_stub.extracted_at,
            extractor_version=json_stub.extractor_version,
            enhancement_timestamp=datetime.now().isoformat(),
            enhancement_version=self.enhancement_version,
            methods=[],
            fields=json_stub.fields,  # Keep original for now
            constructors=json_stub.constructors  # Keep original for now
        )
        
        if javadoc_class:
            # Add class-level JavaDoc information
            enhanced_stub.javadoc_description = javadoc_class.description
            enhanced_stub.inheritance = javadoc_class.inheritance
            enhanced_stub.nested_classes = javadoc_class.nested_classes
            enhanced_stub.deprecated = javadoc_class.deprecated
            enhanced_stub.since_version = javadoc_class.since_version
            enhanced_stub.see_also = javadoc_class.see_also
            
            # Match methods and enhance them
            match_result = self.matcher.match_class(javadoc_class, json_stub)
            enhanced_stub.methods = self._enhance_methods(json_stub.methods, match_result)
            
            # Store enhancement metadata
            enhanced_stub.enhancement_metadata = {
                'matching_statistics': match_result.match_statistics,
                'unmatched_javadoc_methods': len(match_result.unmatched_javadoc_methods),
                'unmatched_json_methods': len(match_result.unmatched_json_methods),
                'enhancement_quality_score': self._calculate_enhancement_quality(match_result)
            }
        else:
            # No JavaDoc available, enhance with categorization only
            enhanced_stub.methods = self._enhance_methods_without_javadoc(json_stub.methods)
            enhanced_stub.enhancement_metadata = {
                'javadoc_available': False,
                'categorization_only': True
            }
        
        self.logger.info(f"Enhanced {json_stub.class_name}: {len(enhanced_stub.methods)} methods")
        return enhanced_stub
    
    def _enhance_methods(self, json_methods: List[MethodInfo], 
                        match_result: ClassMatchResult) -> List[EnhancedMethodInfo]:
        """Enhance methods using JavaDoc matching results."""
        enhanced_methods = []
        
        # Create a mapping of JSON method names to their matches
        method_matches = {match.json_method.name: match for match in match_result.method_matches}
        
        for json_method in json_methods:
            if json_method.name in method_matches:
                # Method has JavaDoc match
                match = method_matches[json_method.name]
                # Verify it's the same method object or has same signature
                if match.json_method.name == json_method.name:
                    enhanced_method = self._create_enhanced_method_from_match(json_method, match)
                else:
                    enhanced_method = self._create_enhanced_method_without_javadoc(json_method)
            else:
                # Method has no JavaDoc match
                enhanced_method = self._create_enhanced_method_without_javadoc(json_method)
            
            enhanced_methods.append(enhanced_method)
        
        return enhanced_methods
    
    def _enhance_methods_without_javadoc(self, json_methods: List[MethodInfo]) -> List[EnhancedMethodInfo]:
        """Enhance methods without JavaDoc documentation (categorization only)."""
        enhanced_methods = []
        
        for json_method in json_methods:
            enhanced_method = self._create_enhanced_method_without_javadoc(json_method)
            enhanced_methods.append(enhanced_method)
        
        return enhanced_methods
    
    def _create_enhanced_method_from_match(self, json_method: MethodInfo, 
                                         match: MethodMatch) -> EnhancedMethodInfo:
        """Create enhanced method from JavaDoc match."""
        javadoc_method = match.javadoc_method
        
        # Enhance overloads
        enhanced_overloads = []
        for overload in json_method.overloads:
            if overload == match.json_overload:
                # This is the matched overload, enhance with JavaDoc
                enhanced_overload = self._enhance_overload_with_javadoc(overload, javadoc_method, match)
            else:
                # Other overload, enhance without specific JavaDoc
                enhanced_overload = self._enhance_overload_without_javadoc(overload)
            enhanced_overloads.append(enhanced_overload)
        
        return EnhancedMethodInfo(
            name=json_method.name,
            overloads=enhanced_overloads,
            documentation=json_method.documentation,
            javadoc_description=javadoc_method.description,
            category=self._categorize_method(json_method.name),
            deprecated=javadoc_method.deprecated,
            since_version=javadoc_method.since_version,
            see_also=javadoc_method.see_also,
            examples=javadoc_method.examples
        )
    
    def _create_enhanced_method_without_javadoc(self, json_method: MethodInfo) -> EnhancedMethodInfo:
        """Create enhanced method without JavaDoc documentation."""
        enhanced_overloads = []
        for overload in json_method.overloads:
            enhanced_overload = self._enhance_overload_without_javadoc(overload)
            enhanced_overloads.append(enhanced_overload)
        
        return EnhancedMethodInfo(
            name=json_method.name,
            overloads=enhanced_overloads,
            documentation=json_method.documentation,
            javadoc_description="",
            category=self._categorize_method(json_method.name)
        )
    
    def _enhance_overload_with_javadoc(self, json_overload: MethodOverload,
                                     javadoc_method: MethodDocumentation,
                                     match: MethodMatch) -> EnhancedMethodOverload:
        """Enhance method overload with JavaDoc information."""
        enhanced_params = []
        
        for json_param in json_overload.params:
            # Find corresponding JavaDoc parameter
            javadoc_param_name = match.parameter_mapping.get(json_param.name)
            javadoc_param = None
            
            if javadoc_param_name:
                javadoc_param = next(
                    (p for p in javadoc_method.parameters if p.name == javadoc_param_name),
                    None
                )
            
            enhanced_param = EnhancedParameterInfo(
                name=json_param.name,
                type=json_param.type,
                java_type=json_param.java_type,
                description=javadoc_param.description if javadoc_param else "",
                javadoc_name=javadoc_param_name
            )
            enhanced_params.append(enhanced_param)
        
        return EnhancedMethodOverload(
            signature=json_overload.signature,
            params=enhanced_params,
            return_type=json_overload.return_type,
            java_return_type=json_overload.java_return_type,
            return_description=javadoc_method.return_description,
            throws=javadoc_method.throws
        )
    
    def _enhance_overload_without_javadoc(self, json_overload: MethodOverload) -> EnhancedMethodOverload:
        """Enhance method overload without JavaDoc information."""
        enhanced_params = []
        
        for json_param in json_overload.params:
            enhanced_param = EnhancedParameterInfo(
                name=json_param.name,
                type=json_param.type,
                java_type=json_param.java_type,
                description="",
                javadoc_name=None
            )
            enhanced_params.append(enhanced_param)
        
        return EnhancedMethodOverload(
            signature=json_overload.signature,
            params=enhanced_params,
            return_type=json_overload.return_type,
            java_return_type=json_overload.java_return_type,
            return_description="",
            throws={}
        )
    
    def _categorize_method(self, method_name: str) -> str:
        """Categorize method based on name patterns."""
        # Clean method name for pattern matching
        clean_name = re.sub(r'^static\s+', '', method_name)
        
        # Check each category pattern
        for category, patterns in self.category_patterns.items():
            for pattern in patterns:
                if re.search(pattern, method_name, re.IGNORECASE):
                    return category
        
        # Default category
        return "Utilities"
    
    def _calculate_enhancement_quality(self, match_result: ClassMatchResult) -> float:
        """Calculate enhancement quality score based on matching results."""
        if not match_result.method_matches:
            return 0.0
        
        total_methods = match_result.match_statistics.get('total_javadoc_methods', 0)
        if total_methods == 0:
            return 0.0
        
        # Base score from match percentage
        match_percentage = match_result.match_statistics.get('match_percentage', 0.0)
        base_score = match_percentage / 100.0
        
        # Bonus for exact matches
        exact_matches = match_result.match_statistics.get('exact_matches', 0)
        exact_bonus = (exact_matches / total_methods) * 0.2
        
        # Penalty for issues
        total_issues = sum(len(match.issues) for match in match_result.method_matches)
        issue_penalty = min(total_issues * 0.05, 0.3)
        
        quality_score = min(base_score + exact_bonus - issue_penalty, 1.0)
        return round(quality_score, 3)
    
    def enhance_multiple_stubs(self, json_stubs: Dict[str, JSONStubData],
                              javadoc_classes: Dict[str, ClassDocumentation]) -> Dict[str, EnhancedJSONStubData]:
        """
        Enhance multiple JSON stubs with JavaDoc documentation.
        
        Args:
            json_stubs: Dictionary of class names to JSON stub data
            javadoc_classes: Dictionary of class names to JavaDoc documentation
            
        Returns:
            Dictionary of class names to enhanced JSON stub data
        """
        enhanced_stubs = {}
        
        for class_name, json_stub in json_stubs.items():
            javadoc_class = javadoc_classes.get(class_name)
            enhanced_stub = self.enhance_json_stub(json_stub, javadoc_class)
            enhanced_stubs[class_name] = enhanced_stub
        
        self.logger.info(f"Enhanced {len(enhanced_stubs)} JSON stubs")
        return enhanced_stubs
    
    def generate_enhancement_report(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """Generate comprehensive enhancement report."""
        report = {
            'summary': {
                'total_classes': len(enhanced_stubs),
                'classes_with_javadoc': 0,
                'classes_without_javadoc': 0,
                'total_enhanced_methods': 0,
                'methods_with_javadoc_descriptions': 0,
                'methods_with_examples': 0,
                'average_enhancement_quality': 0.0
            },
            'categorization': {
                'Getters': 0,
                'Setters': 0,
                'Analysis': 0,
                'I/O Operations': 0,
                'Visualization': 0,
                'Static Methods': 0,
                'Utilities': 0
            },
            'quality_distribution': {
                'high_quality': 0,  # > 0.8
                'medium_quality': 0,  # 0.5 - 0.8
                'low_quality': 0,  # < 0.5
                'no_javadoc': 0
            },
            'class_details': {}
        }
        
        quality_scores = []
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            has_javadoc = bool(enhanced_stub.javadoc_description)
            
            if has_javadoc:
                report['summary']['classes_with_javadoc'] += 1
            else:
                report['summary']['classes_without_javadoc'] += 1
            
            # Count methods and categorization
            methods_with_descriptions = 0
            methods_with_examples = 0
            
            for method in enhanced_stub.methods:
                report['summary']['total_enhanced_methods'] += 1
                
                if method.javadoc_description:
                    methods_with_descriptions += 1
                
                if method.examples:
                    methods_with_examples += 1
                
                # Count by category
                category = method.category
                if category in report['categorization']:
                    report['categorization'][category] += 1
            
            report['summary']['methods_with_javadoc_descriptions'] += methods_with_descriptions
            report['summary']['methods_with_examples'] += methods_with_examples
            
            # Quality assessment
            quality_score = enhanced_stub.enhancement_metadata.get('enhancement_quality_score', 0.0)
            if quality_score > 0:
                quality_scores.append(quality_score)
                
                if quality_score > 0.8:
                    report['quality_distribution']['high_quality'] += 1
                elif quality_score >= 0.5:
                    report['quality_distribution']['medium_quality'] += 1
                else:
                    report['quality_distribution']['low_quality'] += 1
            else:
                report['quality_distribution']['no_javadoc'] += 1
            
            # Store class details
            report['class_details'][class_name] = {
                'has_javadoc': has_javadoc,
                'method_count': len(enhanced_stub.methods),
                'methods_with_descriptions': methods_with_descriptions,
                'quality_score': quality_score,
                'categories': {}
            }
            
            # Count categories for this class
            for method in enhanced_stub.methods:
                category = method.category
                report['class_details'][class_name]['categories'][category] = \
                    report['class_details'][class_name]['categories'].get(category, 0) + 1
        
        # Calculate average quality
        if quality_scores:
            report['summary']['average_enhancement_quality'] = round(
                sum(quality_scores) / len(quality_scores), 3
            )
        
        return report
    
    def to_dict(self, enhanced_stub: EnhancedJSONStubData) -> Dict[str, Any]:
        """Convert enhanced stub to dictionary for JSON serialization."""
        # Convert dataclass to dict, handling nested structures
        result = asdict(enhanced_stub)
        
        # Ensure all datetime objects are strings
        if isinstance(result.get('enhancement_timestamp'), datetime):
            result['enhancement_timestamp'] = result['enhancement_timestamp'].isoformat()
        
        return result