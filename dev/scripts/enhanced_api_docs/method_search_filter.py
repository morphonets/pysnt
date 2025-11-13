"""
Method search and filtering system for enhanced API documentation.
Provides text search and filtering capabilities for method indexes.
"""

import re
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any, Tuple

from .logging_setup import get_logger
from .method_index_entry import MethodIndexEntry

logger = get_logger('method_search_filter')


class SearchType(Enum):
    """Types of search operations."""
    EXACT = "exact"
    PARTIAL = "partial"
    REGEX = "regex"
    FUZZY = "fuzzy"


class FilterType(Enum):
    """Types of filter operations."""
    CLASS = "class"
    RETURN_TYPE = "return_type"
    CATEGORY = "category"
    PACKAGE = "package"
    PARAMETER_TYPE = "parameter_type"
    DEPRECATED = "deprecated"
    HAS_EXAMPLES = "has_examples"
    HAS_DESCRIPTION = "has_description"


@dataclass
class SearchQuery:
    """Represents a search query with options."""
    query: str
    search_type: SearchType = SearchType.PARTIAL
    case_sensitive: bool = False
    search_fields: List[str] = None  # Fields to search in
    
    def __post_init__(self):
        if self.search_fields is None:
            self.search_fields = ['method_name', 'description', 'class_name']


@dataclass
class FilterCriteria:
    """Represents filter criteria for method search."""
    filter_type: FilterType
    value: Any
    operator: str = "equals"  # equals, contains, starts_with, ends_with, not_equals
    
    def matches(self, method_entry: MethodIndexEntry) -> bool:
        """Check if method entry matches this filter criteria."""
        target_value = self._get_target_value(method_entry)
        
        if target_value is None:
            return False
        
        return self._apply_operator(target_value, self.value, self.operator)
    
    def _get_target_value(self, method_entry: MethodIndexEntry) -> Any:
        """Get the target value from method entry based on filter type."""
        if self.filter_type == FilterType.CLASS:
            return method_entry.class_name
        elif self.filter_type == FilterType.RETURN_TYPE:
            return method_entry.return_type
        elif self.filter_type == FilterType.CATEGORY:
            return method_entry.category
        elif self.filter_type == FilterType.PACKAGE:
            return method_entry.package
        elif self.filter_type == FilterType.PARAMETER_TYPE:
            return method_entry.parameter_types
        elif self.filter_type == FilterType.DEPRECATED:
            return method_entry.deprecated
        elif self.filter_type == FilterType.HAS_EXAMPLES:
            return len(method_entry.examples) > 0
        elif self.filter_type == FilterType.HAS_DESCRIPTION:
            return bool(method_entry.javadoc_description)
        else:
            return None
    
    def _apply_operator(self, target_value: Any, filter_value: Any, operator: str) -> bool:
        """Apply the operator to compare target and filter values."""
        if operator == "equals":
            return target_value == filter_value
        elif operator == "not_equals":
            return target_value != filter_value
        elif operator == "contains":
            if isinstance(target_value, (list, tuple)):
                return any(filter_value.lower() in str(item).lower() for item in target_value)
            return filter_value.lower() in str(target_value).lower()
        elif operator == "starts_with":
            return str(target_value).lower().startswith(str(filter_value).lower())
        elif operator == "ends_with":
            return str(target_value).lower().endswith(str(filter_value).lower())
        else:
            return False


@dataclass
class SearchResult:
    """Represents a search result with relevance scoring."""
    method_entry: MethodIndexEntry
    relevance_score: float
    matched_fields: List[str]
    match_positions: Dict[str, List[Tuple[int, int]]]  # field -> [(start, end), ...]
    
    def __lt__(self, other):
        """Compare search results by relevance score."""
        return self.relevance_score > other.relevance_score  # Higher score first


class MethodSearchFilter:
    """Provides search and filtering capabilities for method indexes."""
    
    def __init__(self):
        """Initialize the search and filter system."""
        self.logger = logger
        
        # Search field weights for relevance scoring
        self.field_weights = {
            'method_name': 3.0,
            'class_name': 2.0,
            'category': 1.5,
            'description': 1.0,
            'return_type': 0.8,
            'parameter_types': 0.6,
            'package': 0.4
        }
    
    def search_methods(self, method_entries: List[MethodIndexEntry], 
                      search_query: SearchQuery) -> List[SearchResult]:
        """
        Search methods based on query and return ranked results.
        
        Args:
            method_entries: List of method index entries to search
            search_query: Search query with options
            
        Returns:
            List of search results sorted by relevance
        """
        if not search_query.query.strip():
            # Return all methods with zero relevance if no query
            return [SearchResult(entry, 0.0, [], {}) for entry in method_entries]
        
        self.logger.debug(f"Searching {len(method_entries)} methods for '{search_query.query}'")
        
        results = []
        
        for entry in method_entries:
            result = self._search_single_method(entry, search_query)
            if result:
                results.append(result)
        
        # Sort by relevance score
        results.sort()
        
        self.logger.info(f"Found {len(results)} matching methods")
        return results
    
    def filter_methods(self, method_entries: List[MethodIndexEntry],
                      filters: List[FilterCriteria]) -> List[MethodIndexEntry]:
        """
        Filter methods based on criteria.
        
        Args:
            method_entries: List of method index entries to filter
            filters: List of filter criteria to apply
            
        Returns:
            List of filtered method entries
        """
        if not filters:
            return method_entries
        
        self.logger.debug(f"Filtering {len(method_entries)} methods with {len(filters)} criteria")
        
        filtered_entries = []
        
        for entry in method_entries:
            if all(filter_criteria.matches(entry) for filter_criteria in filters):
                filtered_entries.append(entry)
        
        self.logger.info(f"Filtered to {len(filtered_entries)} methods")
        return filtered_entries
    
    def search_and_filter(self, method_entries: List[MethodIndexEntry],
                         search_query: Optional[SearchQuery] = None,
                         filters: Optional[List[FilterCriteria]] = None) -> List[SearchResult]:
        """
        Combine search and filtering operations.
        
        Args:
            method_entries: List of method index entries
            search_query: Optional search query
            filters: Optional list of filter criteria
            
        Returns:
            List of search results that match both search and filters
        """
        # Apply filters first
        if filters:
            filtered_entries = self.filter_methods(method_entries, filters)
        else:
            filtered_entries = method_entries
        
        # Then apply search
        if search_query and search_query.query.strip():
            return self.search_methods(filtered_entries, search_query)
        else:
            # Return filtered results without search scoring
            return [SearchResult(entry, 0.0, [], {}) for entry in filtered_entries]
    
    def get_search_suggestions(self, method_entries: List[MethodIndexEntry],
                              partial_query: str, max_suggestions: int = 10) -> List[str]:
        """
        Get search suggestions based on partial query.
        
        Args:
            method_entries: List of method index entries
            partial_query: Partial search query
            max_suggestions: Maximum number of suggestions to return
            
        Returns:
            List of suggested search terms
        """
        if not partial_query.strip():
            return []
        
        suggestions = set()
        query_lower = partial_query.lower()
        
        for entry in method_entries:
            # Method name suggestions
            if entry.method_name.lower().startswith(query_lower):
                suggestions.add(entry.method_name)
            
            # Class name suggestions
            if entry.class_name.lower().startswith(query_lower):
                suggestions.add(entry.class_name)
            
            # Category suggestions
            if entry.category.lower().startswith(query_lower):
                suggestions.add(entry.category)
            
            # Return type suggestions
            if entry.return_type.lower().startswith(query_lower):
                suggestions.add(entry.return_type)
            
            # Word-based suggestions from descriptions
            if entry.javadoc_description:
                words = re.findall(r'\b\w+\b', entry.javadoc_description.lower())
                for word in words:
                    if word.startswith(query_lower) and len(word) > len(query_lower):
                        suggestions.add(word)
        
        # Sort suggestions by length and alphabetically
        sorted_suggestions = sorted(suggestions, key=lambda x: (len(x), x))
        return sorted_suggestions[:max_suggestions]
    
    def get_filter_options(self, method_entries: List[MethodIndexEntry]) -> Dict[str, List[str]]:
        """
        Get available filter options from method entries.
        
        Args:
            method_entries: List of method index entries
            
        Returns:
            Dictionary mapping filter types to available values
        """
        options = {
            'classes': set(),
            'categories': set(),
            'return_types': set(),
            'packages': set(),
            'parameter_types': set()
        }
        
        for entry in method_entries:
            options['classes'].add(entry.class_name)
            options['categories'].add(entry.category)
            options['return_types'].add(entry.return_type)
            if entry.package:
                options['packages'].add(entry.package)
            options['parameter_types'].update(entry.parameter_types)
        
        # Convert to sorted lists
        return {
            key: sorted(list(values)) for key, values in options.items()
        }
    
    def _search_single_method(self, method_entry: MethodIndexEntry, 
                             search_query: SearchQuery) -> Optional[SearchResult]:
        """Search a single method entry and return result if matches."""
        matched_fields = []
        match_positions = {}
        total_score = 0.0
        
        # Search in specified fields
        for field in search_query.search_fields:
            field_value = self._get_field_value(method_entry, field)
            if field_value is None:
                continue
            
            matches = self._find_matches(field_value, search_query)
            if matches:
                matched_fields.append(field)
                match_positions[field] = matches
                
                # Calculate field score
                field_score = self._calculate_field_score(field, matches, len(field_value))
                total_score += field_score * self.field_weights.get(field, 1.0)
        
        if matched_fields:
            return SearchResult(
                method_entry=method_entry,
                relevance_score=total_score,
                matched_fields=matched_fields,
                match_positions=match_positions
            )
        
        return None
    
    def _get_field_value(self, method_entry: MethodIndexEntry, field: str) -> Optional[str]:
        """Get field value from method entry."""
        if field == 'method_name':
            return method_entry.method_name
        elif field == 'class_name':
            return method_entry.class_name
        elif field == 'category':
            return method_entry.category
        elif field == 'description':
            return method_entry.javadoc_description
        elif field == 'return_type':
            return method_entry.return_type
        elif field == 'parameter_types':
            return ' '.join(method_entry.parameter_types)
        elif field == 'package':
            return method_entry.package
        elif field == 'signature':
            return method_entry.signature
        else:
            return None
    
    def _find_matches(self, text: str, search_query: SearchQuery) -> List[Tuple[int, int]]:
        """Find all matches of query in text."""
        if not text:
            return []
        
        query = search_query.query
        if not search_query.case_sensitive:
            text = text.lower()
            query = query.lower()
        
        matches = []
        
        if search_query.search_type == SearchType.EXACT:
            # Exact match
            if text == query:
                matches.append((0, len(text)))
        elif search_query.search_type == SearchType.PARTIAL:
            # Partial match - find all occurrences
            start = 0
            while True:
                pos = text.find(query, start)
                if pos == -1:
                    break
                matches.append((pos, pos + len(query)))
                start = pos + 1
        elif search_query.search_type == SearchType.REGEX:
            # Regular expression match
            try:
                flags = 0 if search_query.case_sensitive else re.IGNORECASE
                for match in re.finditer(query, text, flags):
                    matches.append((match.start(), match.end()))
            except re.error:
                # Invalid regex, fall back to partial match
                return self._find_matches(text, SearchQuery(query, SearchType.PARTIAL, search_query.case_sensitive))
        elif search_query.search_type == SearchType.FUZZY:
            # Fuzzy match - simple implementation
            matches = self._fuzzy_match(text, query)
        
        return matches
    
    def _fuzzy_match(self, text: str, query: str) -> List[Tuple[int, int]]:
        """Simple fuzzy matching implementation."""
        matches = []
        
        # Split query into words and find each word
        query_words = query.split()
        for word in query_words:
            if len(word) < 2:
                continue
            
            # Find approximate matches allowing for 1 character difference
            for i in range(len(text) - len(word) + 1):
                substring = text[i:i + len(word)]
                if self._levenshtein_distance(substring, word) <= 1:
                    matches.append((i, i + len(word)))
        
        return matches
    
    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def _calculate_field_score(self, field: str, matches: List[Tuple[int, int]], field_length: int) -> float:
        """Calculate relevance score for a field based on matches."""
        if not matches:
            return 0.0
        
        # Base score from number of matches
        base_score = len(matches)
        
        # Bonus for matches at the beginning of the field
        position_bonus = 0.0
        for start, end in matches:
            if start == 0:
                position_bonus += 2.0  # Match at beginning
            elif start < field_length * 0.1:
                position_bonus += 1.0  # Match near beginning
        
        # Bonus for coverage (how much of the field is matched)
        total_matched_chars = sum(end - start for start, end in matches)
        coverage_bonus = (total_matched_chars / field_length) * 2.0
        
        return base_score + position_bonus + coverage_bonus
    
    def create_search_index(self, method_entries: List[MethodIndexEntry]) -> Dict[str, Any]:
        """
        Create a search index for faster searching.
        
        Args:
            method_entries: List of method index entries
            
        Returns:
            Dictionary containing search index data
        """
        self.logger.info(f"Creating search index for {len(method_entries)} methods")
        
        # Word-based index
        word_index = {}
        
        # N-gram index for fuzzy search
        ngram_index = {}
        
        for i, entry in enumerate(method_entries):
            # Index words from all searchable fields
            searchable_text = ' '.join([
                entry.method_name,
                entry.class_name,
                entry.category,
                entry.javadoc_description or '',
                entry.return_type,
                ' '.join(entry.parameter_types),
                entry.package or ''
            ])
            
            # Extract words
            words = re.findall(r'\b\w+\b', searchable_text.lower())
            
            for word in words:
                if word not in word_index:
                    word_index[word] = []
                word_index[word].append(i)
                
                # Create n-grams for fuzzy search
                for n in range(2, min(len(word) + 1, 5)):  # 2-4 character n-grams
                    for j in range(len(word) - n + 1):
                        ngram = word[j:j + n]
                        if ngram not in ngram_index:
                            ngram_index[ngram] = set()
                        ngram_index[ngram].add(i)
        
        # Convert sets to lists for JSON serialization
        ngram_index = {k: list(v) for k, v in ngram_index.items()}
        
        search_index = {
            'word_index': word_index,
            'ngram_index': ngram_index,
            'method_count': len(method_entries),
            'created_at': str(datetime.now())
        }
        
        self.logger.info(f"Created search index with {len(word_index)} words and {len(ngram_index)} n-grams")
        return search_index


# Convenience functions for common search operations

def create_class_filter(class_name: str, operator: str = "contains") -> FilterCriteria:
    """Create a filter for class name."""
    return FilterCriteria(FilterType.CLASS, class_name, operator)


def create_return_type_filter(return_type: str, operator: str = "equals") -> FilterCriteria:
    """Create a filter for return type."""
    return FilterCriteria(FilterType.RETURN_TYPE, return_type, operator)


def create_category_filter(category: str) -> FilterCriteria:
    """Create a filter for method category."""
    return FilterCriteria(FilterType.CATEGORY, category, "equals")


def create_deprecated_filter(include_deprecated: bool = False) -> FilterCriteria:
    """Create a filter for deprecated methods."""
    return FilterCriteria(FilterType.DEPRECATED, not include_deprecated, "equals")


def create_documented_filter(require_documentation: bool = True) -> FilterCriteria:
    """Create a filter for methods with documentation."""
    return FilterCriteria(FilterType.HAS_DESCRIPTION, require_documentation, "equals")


def create_examples_filter(require_examples: bool = True) -> FilterCriteria:
    """Create a filter for methods with examples."""
    return FilterCriteria(FilterType.HAS_EXAMPLES, require_examples, "equals")