"""
Javadoc-JSON matching system for the enhanced API documentation systems
Matches Javadoc methods with JSON stub method signatures.
"""

import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Dict, List, Optional, Tuple, Any

from .javadoc_parser import MethodDocumentation, ClassDocumentation
from .json_stub_reader import JSONStubData, MethodInfo, MethodOverload
from .logging_setup import get_logger

logger = get_logger('javadoc_json_matcher')


@dataclass
class MethodMatch:
    """Represents a match between JavaDoc method and JSON stub method."""
    javadoc_method: MethodDocumentation
    json_method: MethodInfo
    json_overload: MethodOverload
    confidence: float
    match_type: str  # 'exact', 'fuzzy', 'signature_only', 'name_only'
    parameter_mapping: Dict[str, str]  # json_param_name -> javadoc_param_name
    issues: List[str]  # Any issues found during matching


@dataclass
class ClassMatchResult:
    """Results of matching JavaDoc and JSON stub data for a class."""
    class_name: str
    javadoc_class: Optional[ClassDocumentation]
    json_stub: Optional[JSONStubData]
    method_matches: List[MethodMatch]
    unmatched_javadoc_methods: List[MethodDocumentation]
    unmatched_json_methods: List[MethodInfo]
    match_statistics: Dict[str, int]


class JavaDocJSONMatcher:
    """Matches JavaDoc documentation with JSON stub method signatures."""
    
    def __init__(self, fuzzy_threshold: float = 0.8):
        """
        Initialize the matcher.
        
        Args:
            fuzzy_threshold: Minimum similarity score for fuzzy matching (0.0-1.0)
        """
        self.fuzzy_threshold = fuzzy_threshold
        self.logger = logger
    
    def match_class(self, javadoc_class: ClassDocumentation, json_stub: JSONStubData) -> ClassMatchResult:
        """
        Match JavaDoc class documentation with JSON stub data.
        
        Args:
            javadoc_class: JavaDoc class documentation
            json_stub: JSON stub data
            
        Returns:
            ClassMatchResult with matching information
        """
        self.logger.debug(f"Matching class {javadoc_class.class_name} with JSON stub")
        
        method_matches = []
        unmatched_javadoc = javadoc_class.methods.copy()
        unmatched_json = json_stub.methods.copy()
        
        # First pass: Exact matches
        exact_matches = self._find_exact_matches(unmatched_javadoc, unmatched_json)
        method_matches.extend(exact_matches)
        
        # Remove matched methods from unmatched lists
        for match in exact_matches:
            if match.javadoc_method in unmatched_javadoc:
                unmatched_javadoc.remove(match.javadoc_method)
            if match.json_method in unmatched_json:
                unmatched_json.remove(match.json_method)
        
        # Second pass: Signature-based matches
        signature_matches = self._find_signature_matches(unmatched_javadoc, unmatched_json)
        method_matches.extend(signature_matches)
        
        # Remove matched methods
        for match in signature_matches:
            if match.javadoc_method in unmatched_javadoc:
                unmatched_javadoc.remove(match.javadoc_method)
            if match.json_method in unmatched_json:
                unmatched_json.remove(match.json_method)
        
        # Third pass: Fuzzy matches
        fuzzy_matches = self._find_fuzzy_matches(unmatched_javadoc, unmatched_json)
        method_matches.extend(fuzzy_matches)
        
        # Remove matched methods
        for match in fuzzy_matches:
            if match.javadoc_method in unmatched_javadoc:
                unmatched_javadoc.remove(match.javadoc_method)
            if match.json_method in unmatched_json:
                unmatched_json.remove(match.json_method)
        
        # Calculate statistics
        match_stats = self._calculate_match_statistics(method_matches, javadoc_class.methods, json_stub.methods)
        
        return ClassMatchResult(
            class_name=javadoc_class.class_name,
            javadoc_class=javadoc_class,
            json_stub=json_stub,
            method_matches=method_matches,
            unmatched_javadoc_methods=unmatched_javadoc,
            unmatched_json_methods=unmatched_json,
            match_statistics=match_stats
        )
    
    def _find_exact_matches(self, javadoc_methods: List[MethodDocumentation], 
                           json_methods: List[MethodInfo]) -> List[MethodMatch]:
        """Find exact method name matches."""
        matches = []
        
        for javadoc_method in javadoc_methods:
            # Clean method name (remove static prefix, etc.)
            clean_javadoc_name = self._clean_method_name(javadoc_method.name)
            
            for json_method in json_methods:
                clean_json_name = self._clean_method_name(json_method.name)
                
                if clean_javadoc_name == clean_json_name:
                    # Find best overload match
                    best_overload, param_mapping = self._match_overloads(javadoc_method, json_method)
                    if best_overload:
                        matches.append(MethodMatch(
                            javadoc_method=javadoc_method,
                            json_method=json_method,
                            json_overload=best_overload,
                            confidence=1.0,
                            match_type='exact',
                            parameter_mapping=param_mapping,
                            issues=[]
                        ))
                        break
        
        self.logger.debug(f"Found {len(matches)} exact matches")
        return matches
    
    def _find_signature_matches(self, javadoc_methods: List[MethodDocumentation], 
                               json_methods: List[MethodInfo]) -> List[MethodMatch]:
        """Find matches based on method signatures (parameter types and return types)."""
        matches = []
        
        for javadoc_method in javadoc_methods:
            best_match = None
            best_confidence = 0.0
            
            for json_method in json_methods:
                # Compare signatures across all overloads
                for overload in json_method.overloads:
                    confidence = self._calculate_signature_similarity(javadoc_method, overload)
                    
                    if confidence > best_confidence and confidence >= 0.7:  # Threshold for signature match
                        param_mapping = self._map_parameters(javadoc_method, overload)
                        best_match = MethodMatch(
                            javadoc_method=javadoc_method,
                            json_method=json_method,
                            json_overload=overload,
                            confidence=confidence,
                            match_type='signature_only',
                            parameter_mapping=param_mapping,
                            issues=self._identify_signature_issues(javadoc_method, overload)
                        )
                        best_confidence = confidence
            
            if best_match:
                matches.append(best_match)
        
        self.logger.debug(f"Found {len(matches)} signature-based matches")
        return matches
    
    def _find_fuzzy_matches(self, javadoc_methods: List[MethodDocumentation], 
                           json_methods: List[MethodInfo]) -> List[MethodMatch]:
        """Find fuzzy matches based on method name similarity."""
        matches = []
        
        for javadoc_method in javadoc_methods:
            clean_javadoc_name = self._clean_method_name(javadoc_method.name)
            best_match = None
            best_similarity = 0.0
            
            for json_method in json_methods:
                clean_json_name = self._clean_method_name(json_method.name)
                
                # Calculate string similarity
                similarity = SequenceMatcher(None, clean_javadoc_name, clean_json_name).ratio()
                
                if similarity > best_similarity and similarity >= self.fuzzy_threshold:
                    # Find best overload match
                    best_overload, param_mapping = self._match_overloads(javadoc_method, json_method)
                    if best_overload:
                        best_match = MethodMatch(
                            javadoc_method=javadoc_method,
                            json_method=json_method,
                            json_overload=best_overload,
                            confidence=similarity,
                            match_type='fuzzy',
                            parameter_mapping=param_mapping,
                            issues=[f"Fuzzy name match: '{javadoc_method.name}' -> '{json_method.name}'"]
                        )
                        best_similarity = similarity
            
            if best_match:
                matches.append(best_match)
        
        self.logger.debug(f"Found {len(matches)} fuzzy matches")
        return matches
    
    def _clean_method_name(self, method_name: str) -> str:
        """Clean method name for comparison."""
        # Remove 'static' prefix
        name = re.sub(r'^static\s+', '', method_name)
        
        # Remove generic type parameters
        name = re.sub(r'<[^>]*>', '', name)
        
        # Remove whitespace
        name = name.strip()
        
        return name
    
    def _match_overloads(self, javadoc_method: MethodDocumentation, 
                        json_method: MethodInfo) -> Tuple[Optional[MethodOverload], Dict[str, str]]:
        """Find the best matching overload for a JavaDoc method."""
        best_overload = None
        best_score = 0.0
        best_param_mapping = {}
        
        for overload in json_method.overloads:
            score = self._calculate_overload_similarity(javadoc_method, overload)
            if score > best_score:
                best_score = score
                best_overload = overload
                best_param_mapping = self._map_parameters(javadoc_method, overload)
        
        return best_overload, best_param_mapping
    
    def _calculate_overload_similarity(self, javadoc_method: MethodDocumentation, 
                                     json_overload: MethodOverload) -> float:
        """Calculate similarity between JavaDoc method and JSON overload."""
        score = 0.0
        
        # Parameter count match (40% weight)
        javadoc_param_count = len(javadoc_method.parameters)
        json_param_count = len(json_overload.params)
        
        if javadoc_param_count == json_param_count:
            score += 0.4
        elif abs(javadoc_param_count - json_param_count) <= 1:
            score += 0.2  # Close parameter count
        
        # Return type similarity (30% weight)
        return_similarity = self._calculate_type_similarity(
            javadoc_method.return_type, 
            json_overload.java_return_type
        )
        score += return_similarity * 0.3
        
        # Parameter type similarity (30% weight)
        if javadoc_param_count > 0 and json_param_count > 0:
            param_similarities = []
            min_params = min(javadoc_param_count, json_param_count)
            
            for i in range(min_params):
                if i < len(javadoc_method.parameters):
                    # JavaDoc parameters don't have explicit types in our current structure
                    # We'll use a heuristic based on parameter names
                    param_similarities.append(0.5)  # Neutral score
            
            if param_similarities:
                avg_param_similarity = sum(param_similarities) / len(param_similarities)
                score += avg_param_similarity * 0.3
        
        return score
    
    def _calculate_signature_similarity(self, javadoc_method: MethodDocumentation, 
                                      json_overload: MethodOverload) -> float:
        """Calculate signature similarity between JavaDoc method and JSON overload."""
        # This is similar to overload similarity but focuses more on types
        return self._calculate_overload_similarity(javadoc_method, json_overload)
    
    def _calculate_type_similarity(self, type1: str, type2: str) -> float:
        """Calculate similarity between two type names."""
        if not type1 or not type2:
            return 0.0
        
        # Clean type names
        clean_type1 = self._clean_type_name(type1)
        clean_type2 = self._clean_type_name(type2)
        
        if clean_type1 == clean_type2:
            return 1.0
        
        # Check for common type mappings
        type_mappings = {
            'void': 'void',
            'boolean': 'boolean',
            'int': 'int',
            'long': 'long',
            'double': 'double',
            'float': 'float',
            'String': 'String',
            'Object': 'Object'
        }
        
        mapped_type1 = type_mappings.get(clean_type1, clean_type1)
        mapped_type2 = type_mappings.get(clean_type2, clean_type2)
        
        if mapped_type1 == mapped_type2:
            return 0.9
        
        # Use string similarity as fallback
        return SequenceMatcher(None, clean_type1, clean_type2).ratio()
    
    def _clean_type_name(self, type_name: str) -> str:
        """Clean type name for comparison."""
        # Remove package prefixes
        type_name = re.sub(r'^[a-z.]+\.', '', type_name)
        
        # Remove generic parameters
        type_name = re.sub(r'<[^>]*>', '', type_name)
        
        # Remove array indicators
        type_name = re.sub(r'\[\]', '', type_name)
        
        return type_name.strip()
    
    def _map_parameters(self, javadoc_method: MethodDocumentation, 
                       json_overload: MethodOverload) -> Dict[str, str]:
        """Map JSON parameter names to JavaDoc parameter names."""
        mapping = {}
        
        javadoc_params = javadoc_method.parameters
        json_params = json_overload.params
        
        # Simple positional mapping
        for i, json_param in enumerate(json_params):
            if i < len(javadoc_params):
                mapping[json_param.name] = javadoc_params[i].name
            else:
                mapping[json_param.name] = f"param_{i}"
        
        return mapping
    
    def _identify_signature_issues(self, javadoc_method: MethodDocumentation, 
                                  json_overload: MethodOverload) -> List[str]:
        """Identify potential issues with signature matching."""
        issues = []
        
        javadoc_param_count = len(javadoc_method.parameters)
        json_param_count = len(json_overload.params)
        
        if javadoc_param_count != json_param_count:
            issues.append(f"Parameter count mismatch: JavaDoc={javadoc_param_count}, JSON={json_param_count}")
        
        # Check for generic parameter names in JSON
        generic_params = [p.name for p in json_overload.params if p.name.startswith('arg')]
        if generic_params:
            issues.append(f"Generic parameter names in JSON: {generic_params}")
        
        return issues
    
    def _calculate_match_statistics(self, matches: List[MethodMatch], 
                                   javadoc_methods: List[MethodDocumentation],
                                   json_methods: List[MethodInfo]) -> Dict[str, int]:
        """Calculate matching statistics."""
        stats = {
            'total_javadoc_methods': len(javadoc_methods),
            'total_json_methods': len(json_methods),
            'total_matches': len(matches),
            'exact_matches': 0,
            'signature_matches': 0,
            'fuzzy_matches': 0,
            'name_only_matches': 0,
            'unmatched_javadoc': 0,
            'unmatched_json': 0
        }
        
        for match in matches:
            if match.match_type == 'exact':
                stats['exact_matches'] += 1
            elif match.match_type == 'signature_only':
                stats['signature_matches'] += 1
            elif match.match_type == 'fuzzy':
                stats['fuzzy_matches'] += 1
            elif match.match_type == 'name_only':
                stats['name_only_matches'] += 1
        
        stats['unmatched_javadoc'] = stats['total_javadoc_methods'] - stats['total_matches']
        stats['unmatched_json'] = stats['total_json_methods'] - stats['total_matches']
        
        # Calculate match percentage
        if stats['total_javadoc_methods'] > 0:
            stats['match_percentage'] = round(
                (stats['total_matches'] / stats['total_javadoc_methods']) * 100, 1
            )
        else:
            stats['match_percentage'] = 0.0
        
        return stats
    
    def match_multiple_classes(self, javadoc_classes: Dict[str, ClassDocumentation],
                              json_stubs: Dict[str, JSONStubData]) -> Dict[str, ClassMatchResult]:
        """
        Match multiple JavaDoc classes with JSON stubs.
        
        Args:
            javadoc_classes: Dictionary of class names to JavaDoc documentation
            json_stubs: Dictionary of class names to JSON stub data
            
        Returns:
            Dictionary of class names to match results
        """
        results = {}
        
        # Find classes that exist in both datasets
        common_classes = set(javadoc_classes.keys()) & set(json_stubs.keys())
        self.logger.info(f"Matching {len(common_classes)} common classes")
        
        for class_name in common_classes:
            javadoc_class = javadoc_classes[class_name]
            json_stub = json_stubs[class_name]
            
            result = self.match_class(javadoc_class, json_stub)
            results[class_name] = result
        
        # Handle classes that exist only in one dataset
        javadoc_only = set(javadoc_classes.keys()) - set(json_stubs.keys())
        json_only = set(json_stubs.keys()) - set(javadoc_classes.keys())
        
        for class_name in javadoc_only:
            results[class_name] = ClassMatchResult(
                class_name=class_name,
                javadoc_class=javadoc_classes[class_name],
                json_stub=None,
                method_matches=[],
                unmatched_javadoc_methods=javadoc_classes[class_name].methods,
                unmatched_json_methods=[],
                match_statistics={'total_javadoc_methods': len(javadoc_classes[class_name].methods),
                                'total_json_methods': 0, 'total_matches': 0, 'match_percentage': 0.0}
            )
        
        for class_name in json_only:
            results[class_name] = ClassMatchResult(
                class_name=class_name,
                javadoc_class=None,
                json_stub=json_stubs[class_name],
                method_matches=[],
                unmatched_javadoc_methods=[],
                unmatched_json_methods=json_stubs[class_name].methods,
                match_statistics={'total_javadoc_methods': 0,
                                'total_json_methods': len(json_stubs[class_name].methods),
                                'total_matches': 0, 'match_percentage': 0.0}
            )
        
        return results
    
    def generate_matching_report(self, results: Dict[str, ClassMatchResult]) -> Dict[str, Any]:
        """Generate a comprehensive matching report."""
        report = {
            'summary': {
                'total_classes': len(results),
                'classes_with_both_data': 0,
                'classes_javadoc_only': 0,
                'classes_json_only': 0,
                'total_method_matches': 0,
                'total_javadoc_methods': 0,
                'total_json_methods': 0,
                'overall_match_percentage': 0.0
            },
            'match_type_distribution': {
                'exact': 0,
                'signature_only': 0,
                'fuzzy': 0,
                'name_only': 0
            },
            'class_results': {},
            'issues_summary': {
                'classes_with_issues': 0,
                'common_issues': {}
            }
        }
        
        for class_name, result in results.items():
            # Update summary statistics
            if result.javadoc_class and result.json_stub:
                report['summary']['classes_with_both_data'] += 1
            elif result.javadoc_class:
                report['summary']['classes_javadoc_only'] += 1
            elif result.json_stub:
                report['summary']['classes_json_only'] += 1
            
            report['summary']['total_method_matches'] += len(result.method_matches)
            report['summary']['total_javadoc_methods'] += result.match_statistics.get('total_javadoc_methods', 0)
            report['summary']['total_json_methods'] += result.match_statistics.get('total_json_methods', 0)
            
            # Update match type distribution
            for match in result.method_matches:
                report['match_type_distribution'][match.match_type] += 1
            
            # Store class-specific results
            report['class_results'][class_name] = {
                'match_percentage': result.match_statistics.get('match_percentage', 0.0),
                'total_matches': len(result.method_matches),
                'unmatched_javadoc': len(result.unmatched_javadoc_methods),
                'unmatched_json': len(result.unmatched_json_methods),
                'issues': []
            }
            
            # Collect issues
            class_issues = []
            for match in result.method_matches:
                class_issues.extend(match.issues)
            
            if class_issues:
                report['issues_summary']['classes_with_issues'] += 1
                report['class_results'][class_name]['issues'] = class_issues
                
                for issue in class_issues:
                    report['issues_summary']['common_issues'][issue] = \
                        report['issues_summary']['common_issues'].get(issue, 0) + 1
        
        # Calculate overall match percentage
        if report['summary']['total_javadoc_methods'] > 0:
            report['summary']['overall_match_percentage'] = round(
                (report['summary']['total_method_matches'] / report['summary']['total_javadoc_methods']) * 100, 1
            )
        
        return report