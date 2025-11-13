"""
JSON stub file reader and validator for enhanced API documentation system.
"""

import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

from .config import config
from .logging_setup import get_logger

logger = get_logger('json_stub_reader')


@dataclass
class ParameterInfo:
    """Parameter information from JSON stub."""
    name: str
    type: str
    java_type: str


@dataclass
class MethodOverload:
    """Method overload information from JSON stub."""
    signature: str
    params: List[ParameterInfo]
    return_type: str
    java_return_type: str


@dataclass
class MethodInfo:
    """Method information from JSON stub."""
    name: str
    overloads: List[MethodOverload]
    documentation: str


@dataclass
class ConstructorOverload:
    """Constructor overload information from JSON stub."""
    signature: str
    params: List[ParameterInfo]
    return_type: str
    java_return_type: str


@dataclass
class ConstructorInfo:
    """Constructor information from JSON stub."""
    name: str
    overloads: List[ConstructorOverload]
    documentation: str


@dataclass
class FieldInfo:
    """Field information from JSON stub."""
    name: str
    type: str
    java_type: str
    documentation: str


@dataclass
class JSONStubData:
    """Complete JSON stub data for a class."""
    class_name: str
    package: str
    extracted_at: str
    extractor_version: str
    methods: List[MethodInfo]
    fields: List[FieldInfo]
    constructors: List[ConstructorInfo]
    
    # Additional metadata
    file_path: Optional[Path] = None
    is_valid: bool = True
    validation_errors: List[str] = None
    
    def __post_init__(self):
        if self.validation_errors is None:
            self.validation_errors = []


class JSONStubReader:
    """Reads and validates JSON stub files from the STUBS directory."""
    
    def __init__(self):
        """Initialize with configuration from config system."""
        self.stubs_dir = config.get_path('json_stubs.directory')
        self.file_pattern = config.get('json_stubs.file_pattern', '*.json')
        self.backup_enabled = config.get('caching.enable_cache', True)
        self.backup_dir = config.get_path('caching.cache_dir') / 'json_backups'
        self.logger = logger
        
        # Ensure backup directory exists if backup is enabled
        if self.backup_enabled:
            self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def find_json_stub_files(self) -> List[Path]:
        """
        Find all JSON stub files in the STUBS directory.
        
        Returns:
            List of paths to JSON stub files
        """
        if not self.stubs_dir.exists():
            self.logger.error(f"STUBS directory not found: {self.stubs_dir}")
            return []
        
        json_files = list(self.stubs_dir.glob(self.file_pattern))
        self.logger.info(f"Found {len(json_files)} JSON stub files in {self.stubs_dir}")
        
        return json_files
    
    def load_json_stub(self, file_path: Path) -> Optional[JSONStubData]:
        """
        Load and validate a single JSON stub file.
        
        Args:
            file_path: Path to the JSON stub file
            
        Returns:
            JSONStubData object if successful, None otherwise
        """
        if not file_path.exists():
            self.logger.error(f"JSON stub file not found: {file_path}")
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            # Parse and validate the JSON data
            stub_data = self._parse_json_data(raw_data, file_path)
            
            if stub_data and stub_data.is_valid:
                self.logger.debug(f"Successfully loaded JSON stub: {file_path.name}")
                return stub_data
            else:
                self.logger.warning(f"Invalid JSON stub file: {file_path.name}")
                if stub_data:
                    for error in stub_data.validation_errors:
                        self.logger.warning(f"  - {error}")
                return stub_data  # Return even if invalid for error reporting
                
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decode error in {file_path.name}: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Failed to load JSON stub {file_path.name}: {e}")
            return None
    
    def load_all_json_stubs(self) -> Dict[str, JSONStubData]:
        """
        Load all JSON stub files from the STUBS directory.
        
        Returns:
            Dictionary mapping class names to JSONStubData objects
        """
        json_files = self.find_json_stub_files()
        stub_data = {}
        
        for file_path in json_files:
            stub = self.load_json_stub(file_path)
            if stub:
                # Use class name as key, but handle duplicates
                key = stub.class_name
                if key in stub_data:
                    # Handle duplicate class names by including package
                    key = f"{stub.package}.{stub.class_name}"
                    self.logger.warning(f"Duplicate class name {stub.class_name}, using full name: {key}")
                
                stub_data[key] = stub
        
        self.logger.info(f"Loaded {len(stub_data)} JSON stub files successfully")
        return stub_data
    
    def _parse_json_data(self, raw_data: Dict[str, Any], file_path: Path) -> Optional[JSONStubData]:
        """Parse raw JSON data into JSONStubData object with validation."""
        validation_errors = []
        
        # Validate required top-level fields
        required_fields = ['class_name', 'package', 'extracted_at', 'extractor_version', 'methods']
        for field in required_fields:
            if field not in raw_data:
                validation_errors.append(f"Missing required field: {field}")
        
        if validation_errors:
            return JSONStubData(
                class_name=raw_data.get('class_name', 'Unknown'),
                package=raw_data.get('package', 'unknown'),
                extracted_at=raw_data.get('extracted_at', ''),
                extractor_version=raw_data.get('extractor_version', ''),
                methods=[],
                fields=[],
                constructors=[],
                file_path=file_path,
                is_valid=False,
                validation_errors=validation_errors
            )
        
        # Parse methods
        methods = []
        for method_data in raw_data.get('methods', []):
            method = self._parse_method_data(method_data, validation_errors)
            if method:
                methods.append(method)
        
        # Parse fields
        fields = []
        for field_data in raw_data.get('fields', []):
            field = self._parse_field_data(field_data, validation_errors)
            if field:
                fields.append(field)
        
        # Parse constructors
        constructors = []
        for constructor_data in raw_data.get('constructors', []):
            constructor = self._parse_constructor_data(constructor_data, validation_errors)
            if constructor:
                constructors.append(constructor)
        
        return JSONStubData(
            class_name=raw_data['class_name'],
            package=raw_data['package'],
            extracted_at=raw_data['extracted_at'],
            extractor_version=raw_data['extractor_version'],
            methods=methods,
            fields=fields,
            constructors=constructors,
            file_path=file_path,
            is_valid=len(validation_errors) == 0,
            validation_errors=validation_errors
        )
    
    def _parse_method_data(self, method_data: Dict[str, Any], validation_errors: List[str]) -> Optional[MethodInfo]:
        """Parse method data from JSON."""
        if 'name' not in method_data:
            validation_errors.append("Method missing 'name' field")
            return None
        
        if 'overloads' not in method_data:
            validation_errors.append(f"Method {method_data['name']} missing 'overloads' field")
            return None
        
        overloads = []
        for overload_data in method_data['overloads']:
            overload = self._parse_method_overload(overload_data, method_data['name'], validation_errors)
            if overload:
                overloads.append(overload)
        
        return MethodInfo(
            name=method_data['name'],
            overloads=overloads,
            documentation=method_data.get('documentation', '')
        )
    
    def _parse_method_overload(self, overload_data: Dict[str, Any], method_name: str, validation_errors: List[str]) -> Optional[MethodOverload]:
        """Parse method overload data from JSON."""
        required_fields = ['signature', 'params', 'return_type', 'java_return_type']
        for field in required_fields:
            if field not in overload_data:
                validation_errors.append(f"Method {method_name} overload missing '{field}' field")
                return None
        
        # Parse parameters
        params = []
        for param_data in overload_data['params']:
            param = self._parse_parameter_data(param_data, method_name, validation_errors)
            if param:
                params.append(param)
        
        return MethodOverload(
            signature=overload_data['signature'],
            params=params,
            return_type=overload_data['return_type'],
            java_return_type=overload_data['java_return_type']
        )
    
    def _parse_parameter_data(self, param_data: Dict[str, Any], method_name: str, validation_errors: List[str]) -> Optional[ParameterInfo]:
        """Parse parameter data from JSON."""
        required_fields = ['name', 'type', 'java_type']
        for field in required_fields:
            if field not in param_data:
                validation_errors.append(f"Method {method_name} parameter missing '{field}' field")
                return None
        
        return ParameterInfo(
            name=param_data['name'],
            type=param_data['type'],
            java_type=param_data['java_type']
        )
    
    def _parse_field_data(self, field_data: Dict[str, Any], validation_errors: List[str]) -> Optional[FieldInfo]:
        """Parse field data from JSON."""
        required_fields = ['name', 'type', 'java_type']
        for field in required_fields:
            if field not in field_data:
                validation_errors.append(f"Field missing '{field}' field")
                return None
        
        return FieldInfo(
            name=field_data['name'],
            type=field_data['type'],
            java_type=field_data['java_type'],
            documentation=field_data.get('documentation', '')
        )
    
    def _parse_constructor_data(self, constructor_data: Dict[str, Any], validation_errors: List[str]) -> Optional[ConstructorInfo]:
        """Parse constructor data from JSON."""
        if 'name' not in constructor_data:
            validation_errors.append("Constructor missing 'name' field")
            return None
        
        if 'overloads' not in constructor_data:
            validation_errors.append(f"Constructor {constructor_data['name']} missing 'overloads' field")
            return None
        
        overloads = []
        for overload_data in constructor_data['overloads']:
            overload = self._parse_constructor_overload(overload_data, constructor_data['name'], validation_errors)
            if overload:
                overloads.append(overload)
        
        return ConstructorInfo(
            name=constructor_data['name'],
            overloads=overloads,
            documentation=constructor_data.get('documentation', '')
        )
    
    def _parse_constructor_overload(self, overload_data: Dict[str, Any], constructor_name: str, validation_errors: List[str]) -> Optional[ConstructorOverload]:
        """Parse constructor overload data from JSON."""
        required_fields = ['signature', 'params', 'return_type', 'java_return_type']
        for field in required_fields:
            if field not in overload_data:
                validation_errors.append(f"Constructor {constructor_name} overload missing '{field}' field")
                return None
        
        # Parse parameters
        params = []
        for param_data in overload_data['params']:
            param = self._parse_parameter_data(param_data, constructor_name, validation_errors)
            if param:
                params.append(param)
        
        return ConstructorOverload(
            signature=overload_data['signature'],
            params=params,
            return_type=overload_data['return_type'],
            java_return_type=overload_data['java_return_type']
        )
    
    def create_backup(self, file_path: Path) -> bool:
        """
        Create a backup of a JSON stub file before modification.
        
        Args:
            file_path: Path to the JSON file to backup
            
        Returns:
            True if backup successful, False otherwise
        """
        if not self.backup_enabled:
            return True
        
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"{file_path.stem}_{timestamp}.json"
            backup_path = self.backup_dir / backup_name
            
            shutil.copy2(file_path, backup_path)
            self.logger.debug(f"Created backup: {backup_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create backup for {file_path.name}: {e}")
            return False
    
    def validate_json_structure(self, stub_data: JSONStubData) -> Dict[str, Any]:
        """
        Perform comprehensive validation of JSON stub data.
        
        Args:
            stub_data: JSONStubData object to validate
            
        Returns:
            Dictionary with validation results and statistics
        """
        validation = {
            'valid': stub_data.is_valid,
            'errors': stub_data.validation_errors.copy(),
            'warnings': [],
            'statistics': {
                'total_methods': len(stub_data.methods),
                'total_constructors': len(stub_data.constructors),
                'total_fields': len(stub_data.fields),
                'methods_with_overloads': 0,
                'constructors_with_overloads': 0,
                'methods_with_documentation': 0,
                'unique_method_names': set(),
                'parameter_count_distribution': {}
            }
        }
        
        # Validate methods
        for method in stub_data.methods:
            validation['statistics']['unique_method_names'].add(method.name)
            
            if len(method.overloads) > 1:
                validation['statistics']['methods_with_overloads'] += 1
            
            if method.documentation and method.documentation != f"Java method: {method.name}":
                validation['statistics']['methods_with_documentation'] += 1
            
            # Check for parameter naming issues
            for overload in method.overloads:
                param_count = len(overload.params)
                validation['statistics']['parameter_count_distribution'][param_count] = \
                    validation['statistics']['parameter_count_distribution'].get(param_count, 0) + 1
                
                # Check for generic parameter names (arg0, arg1, etc.)
                generic_params = [p for p in overload.params if p.name.startswith('arg')]
                if generic_params and len(overload.params) > 0:
                    validation['warnings'].append(
                        f"Method {method.name} has generic parameter names: {[p.name for p in generic_params]}"
                    )
        
        # Validate constructors
        for constructor in stub_data.constructors:
            if len(constructor.overloads) > 1:
                validation['statistics']['constructors_with_overloads'] += 1
        
        # Check for missing documentation
        if validation['statistics']['methods_with_documentation'] == 0 and validation['statistics']['total_methods'] > 0:
            validation['warnings'].append("No methods have meaningful documentation")
        
        # Check for duplicate method names (should be handled by overloads)
        method_names = [m.name for m in stub_data.methods]
        if len(method_names) != len(set(method_names)):
            validation['errors'].append("Duplicate method names found (should use overloads)")
        
        return validation
    
    def get_stub_statistics(self, stub_data_dict: Dict[str, JSONStubData]) -> Dict[str, Any]:
        """
        Generate statistics for all loaded JSON stub data.
        
        Args:
            stub_data_dict: Dictionary of class names to JSONStubData
            
        Returns:
            Dictionary with comprehensive statistics
        """
        stats = {
            'total_classes': len(stub_data_dict),
            'valid_classes': 0,
            'invalid_classes': 0,
            'total_methods': 0,
            'total_constructors': 0,
            'total_fields': 0,
            'packages': set(),
            'extractor_versions': set(),
            'classes_by_package': {},
            'validation_summary': {
                'classes_with_errors': 0,
                'classes_with_warnings': 0,
                'common_errors': {},
                'common_warnings': {}
            }
        }
        
        for class_name, stub_data in stub_data_dict.items():
            if stub_data.is_valid:
                stats['valid_classes'] += 1
            else:
                stats['invalid_classes'] += 1
            
            stats['total_methods'] += len(stub_data.methods)
            stats['total_constructors'] += len(stub_data.constructors)
            stats['total_fields'] += len(stub_data.fields)
            
            stats['packages'].add(stub_data.package)
            stats['extractor_versions'].add(stub_data.extractor_version)
            
            # Group by package
            if stub_data.package not in stats['classes_by_package']:
                stats['classes_by_package'][stub_data.package] = []
            stats['classes_by_package'][stub_data.package].append(class_name)
            
            # Validation statistics
            validation = self.validate_json_structure(stub_data)
            if validation['errors']:
                stats['validation_summary']['classes_with_errors'] += 1
                for error in validation['errors']:
                    stats['validation_summary']['common_errors'][error] = \
                        stats['validation_summary']['common_errors'].get(error, 0) + 1
            
            if validation['warnings']:
                stats['validation_summary']['classes_with_warnings'] += 1
                for warning in validation['warnings']:
                    stats['validation_summary']['common_warnings'][warning] = \
                        stats['validation_summary']['common_warnings'].get(warning, 0) + 1
        
        # Convert sets to lists for JSON serialization
        stats['packages'] = list(stats['packages'])
        stats['extractor_versions'] = list(stats['extractor_versions'])
        
        return stats