"""
Enhanced JSON file writer for enhanced API documentation system.
Writes enriched JSON files with both reflection and Javadoc data.
"""

import json
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

from .json_enhancer import EnhancedJSONStubData
from .config import config
from .logging_setup import get_logger

logger = get_logger('json_writer')


class EnhancedJSONWriter:
    """Writes enhanced JSON stub files with atomic updates and backup support."""
    
    def __init__(self):
        """Initialize the writer with configuration."""
        self.output_dir = config.get_path('json_stubs.directory')
        self.backup_enabled = config.get('caching.enable_cache', True)
        self.backup_dir = config.get_path('caching.cache_dir') / 'json_backups'
        self.logger = logger
        
        # Ensure directories exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if self.backup_enabled:
            self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def write_enhanced_json(self, enhanced_stub: EnhancedJSONStubData, 
                           output_path: Optional[Path] = None) -> bool:
        """
        Write enhanced JSON stub to file with atomic update.
        
        Args:
            enhanced_stub: Enhanced JSON stub data to write
            output_path: Optional custom output path, defaults to standard location
            
        Returns:
            True if write successful, False otherwise
        """
        if output_path is None:
            output_path = self.output_dir / f"{enhanced_stub.class_name}.json"
        
        self.logger.debug(f"Writing enhanced JSON for {enhanced_stub.class_name} to {output_path}")
        
        try:
            # Create backup if file exists
            if output_path.exists() and self.backup_enabled:
                if not self._create_backup(output_path):
                    self.logger.warning(f"Failed to create backup for {output_path}")
            
            # Convert to dictionary for JSON serialization
            enhanced_dict = self._prepare_for_serialization(enhanced_stub)
            
            # Write atomically using temporary file
            return self._atomic_write(enhanced_dict, output_path)
            
        except Exception as e:
            self.logger.error(f"Failed to write enhanced JSON for {enhanced_stub.class_name}: {e}")
            return False
    
    def write_multiple_enhanced_jsons(self, enhanced_stubs: Dict[str, EnhancedJSONStubData],
                                    output_dir: Optional[Path] = None) -> Dict[str, bool]:
        """
        Write multiple enhanced JSON stubs to files.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced JSON stub data
            output_dir: Optional custom output directory
            
        Returns:
            Dictionary mapping class names to write success status
        """
        if output_dir is None:
            output_dir = self.output_dir
        
        results = {}
        successful_writes = 0
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            output_path = output_dir / f"{class_name}.json"
            success = self.write_enhanced_json(enhanced_stub, output_path)
            results[class_name] = success
            
            if success:
                successful_writes += 1
            else:
                self.logger.error(f"Failed to write {class_name}.json")
        
        self.logger.info(f"Successfully wrote {successful_writes}/{len(enhanced_stubs)} enhanced JSON files")
        return results
    
    def _prepare_for_serialization(self, enhanced_stub: EnhancedJSONStubData) -> Dict[str, Any]:
        """Prepare enhanced stub data for JSON serialization."""
        # Convert dataclass to dictionary
        enhanced_dict = {
            'class_name': enhanced_stub.class_name,
            'package': enhanced_stub.package,
            'extracted_at': enhanced_stub.extracted_at,
            'extractor_version': enhanced_stub.extractor_version,
            'enhancement_timestamp': enhanced_stub.enhancement_timestamp,
            'enhancement_version': enhanced_stub.enhancement_version,
            
            # Enhanced class-level information
            'javadoc_description': enhanced_stub.javadoc_description,
            'inheritance': enhanced_stub.inheritance,
            'nested_classes': enhanced_stub.nested_classes,
            'deprecated': enhanced_stub.deprecated,
            'since_version': enhanced_stub.since_version,
            'see_also': enhanced_stub.see_also,
            
            # Methods (enhanced)
            'methods': self._serialize_methods(enhanced_stub.methods),
            
            # Fields and constructors (preserve original structure for backward compatibility)
            'fields': self._serialize_fields(enhanced_stub.fields),
            'constructors': self._serialize_constructors(enhanced_stub.constructors),
            
            # Enhancement metadata
            'enhancement_metadata': enhanced_stub.enhancement_metadata
        }
        
        return enhanced_dict
    
    def _serialize_methods(self, methods: List) -> List[Dict[str, Any]]:
        """Serialize enhanced methods to dictionary format."""
        serialized_methods = []
        
        for method in methods:
            method_dict = {
                'name': method.name,
                'documentation': method.documentation,
                'javadoc_description': method.javadoc_description,
                'category': method.category,
                'deprecated': method.deprecated,
                'since_version': method.since_version,
                'see_also': method.see_also,
                'examples': method.examples,
                'overloads': []
            }
            
            # Serialize overloads
            for overload in method.overloads:
                overload_dict = {
                    'signature': overload.signature,
                    'return_type': overload.return_type,
                    'java_return_type': overload.java_return_type,
                    'return_description': overload.return_description,
                    'throws': overload.throws,
                    'params': []
                }
                
                # Serialize parameters
                for param in overload.params:
                    param_dict = {
                        'name': param.name,
                        'type': param.type,
                        'java_type': param.java_type,
                        'description': param.description,
                        'javadoc_name': param.javadoc_name
                    }
                    overload_dict['params'].append(param_dict)
                
                method_dict['overloads'].append(overload_dict)
            
            serialized_methods.append(method_dict)
        
        return serialized_methods
    
    def _serialize_fields(self, fields: List) -> List[Dict[str, Any]]:
        """Serialize fields to dictionary format."""
        if not fields:
            return []
        
        # If fields are already dictionaries, return as-is
        if isinstance(fields[0], dict):
            return fields
        
        # If fields are dataclass objects, convert them
        serialized_fields = []
        for field in fields:
            if hasattr(field, '__dict__'):
                serialized_fields.append(field.__dict__)
            else:
                serialized_fields.append(field)
        
        return serialized_fields
    
    def _serialize_constructors(self, constructors: List) -> List[Dict[str, Any]]:
        """Serialize constructors to dictionary format."""
        if not constructors:
            return []
        
        # If constructors are already dictionaries, return as-is
        if isinstance(constructors[0], dict):
            return constructors
        
        # If constructors are dataclass objects, convert them recursively
        serialized_constructors = []
        for constructor in constructors:
            serialized_constructors.append(self._serialize_object_recursively(constructor))
        
        return serialized_constructors
    
    def _serialize_object_recursively(self, obj) -> Any:
        """Recursively serialize objects to JSON-compatible format."""
        if obj is None:
            return None
        elif isinstance(obj, (str, int, float, bool)):
            return obj
        elif isinstance(obj, (list, tuple)):
            return [self._serialize_object_recursively(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self._serialize_object_recursively(value) for key, value in obj.items()}
        elif hasattr(obj, '__dict__'):
            # Dataclass or object with __dict__
            return {key: self._serialize_object_recursively(value) for key, value in obj.__dict__.items()}
        else:
            # Fallback: convert to string
            return str(obj)
    
    def _atomic_write(self, data: Dict[str, Any], output_path: Path) -> bool:
        """Write data to file atomically using temporary file."""
        try:
            # Create temporary file in the same directory as the target
            temp_dir = output_path.parent
            with tempfile.NamedTemporaryFile(
                mode='w', 
                dir=temp_dir, 
                suffix='.tmp', 
                prefix=f"{output_path.stem}_",
                delete=False,
                encoding='utf-8'
            ) as temp_file:
                
                # Write JSON data with proper formatting
                json.dump(data, temp_file, indent=2, ensure_ascii=False, sort_keys=True)
                temp_path = Path(temp_file.name)
            
            # Atomic move from temporary file to final location
            shutil.move(str(temp_path), str(output_path))
            
            self.logger.debug(f"Successfully wrote {output_path}")
            return True
            
        except Exception as e:
            # Clean up temporary file if it exists
            if 'temp_path' in locals() and temp_path.exists():
                temp_path.unlink()
            
            self.logger.error(f"Atomic write failed for {output_path}: {e}")
            return False
    
    def _create_backup(self, file_path: Path) -> bool:
        """Create a backup of an existing file."""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"{file_path.stem}_{timestamp}.json"
            backup_path = self.backup_dir / backup_name
            
            shutil.copy2(file_path, backup_path)
            self.logger.debug(f"Created backup: {backup_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create backup for {file_path}: {e}")
            return False
    
    def validate_enhanced_json(self, file_path: Path) -> Dict[str, Any]:
        """
        Validate an enhanced JSON file for structure and completeness.
        
        Args:
            file_path: Path to the enhanced JSON file
            
        Returns:
            Dictionary with validation results
        """
        validation = {
            'valid': False,
            'errors': [],
            'warnings': [],
            'statistics': {
                'file_size': 0,
                'methods_count': 0,
                'enhanced_methods_count': 0,
                'methods_with_javadoc': 0,
                'methods_with_examples': 0,
                'categories': {}
            }
        }
        
        try:
            if not file_path.exists():
                validation['errors'].append(f"File does not exist: {file_path}")
                return validation
            
            validation['statistics']['file_size'] = file_path.stat().st_size
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validate required fields
            required_fields = [
                'class_name', 'package', 'extracted_at', 'extractor_version',
                'enhancement_timestamp', 'enhancement_version', 'methods'
            ]
            
            for field in required_fields:
                if field not in data:
                    validation['errors'].append(f"Missing required field: {field}")
            
            # Validate methods structure
            if 'methods' in data:
                methods = data['methods']
                validation['statistics']['methods_count'] = len(methods)
                
                for method in methods:
                    # Check for enhanced fields
                    if method.get('javadoc_description'):
                        validation['statistics']['methods_with_javadoc'] += 1
                    
                    if method.get('examples'):
                        validation['statistics']['methods_with_examples'] += 1
                    
                    # Count categories
                    category = method.get('category', 'Unknown')
                    validation['statistics']['categories'][category] = \
                        validation['statistics']['categories'].get(category, 0) + 1
                    
                    # Check for enhanced overloads
                    if 'overloads' in method:
                        for overload in method['overloads']:
                            if overload.get('return_description') or overload.get('throws'):
                                validation['statistics']['enhanced_methods_count'] += 1
                                break
            
            # Check for enhancement metadata
            if 'enhancement_metadata' not in data:
                validation['warnings'].append("Missing enhancement metadata")
            
            # Check for JavaDoc integration
            if not data.get('javadoc_description'):
                validation['warnings'].append("No class-level JavaDoc description")
            
            # Validate JSON structure integrity
            try:
                json.dumps(data)  # Test serialization
                validation['valid'] = len(validation['errors']) == 0
            except Exception as e:
                validation['errors'].append(f"JSON serialization error: {e}")
            
        except json.JSONDecodeError as e:
            validation['errors'].append(f"JSON decode error: {e}")
        except Exception as e:
            validation['errors'].append(f"Validation error: {e}")
        
        return validation
    
    def generate_write_report(self, write_results: Dict[str, bool],
                             enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """Generate comprehensive write operation report."""
        report = {
            'summary': {
                'total_files': len(write_results),
                'successful_writes': sum(write_results.values()),
                'failed_writes': len(write_results) - sum(write_results.values()),
                'total_methods_written': 0,
                'total_file_size': 0,
                'enhancement_coverage': {
                    'classes_with_javadoc': 0,
                    'methods_with_javadoc': 0,
                    'methods_with_examples': 0
                }
            },
            'file_details': {},
            'errors': []
        }
        
        for class_name, success in write_results.items():
            if success and class_name in enhanced_stubs:
                enhanced_stub = enhanced_stubs[class_name]
                
                # Calculate file statistics
                output_path = self.output_dir / f"{class_name}.json"
                file_size = output_path.stat().st_size if output_path.exists() else 0
                
                report['summary']['total_file_size'] += file_size
                report['summary']['total_methods_written'] += len(enhanced_stub.methods)
                
                # Enhancement coverage
                if enhanced_stub.javadoc_description:
                    report['summary']['enhancement_coverage']['classes_with_javadoc'] += 1
                
                methods_with_javadoc = sum(1 for m in enhanced_stub.methods if m.javadoc_description)
                methods_with_examples = sum(1 for m in enhanced_stub.methods if m.examples)
                
                report['summary']['enhancement_coverage']['methods_with_javadoc'] += methods_with_javadoc
                report['summary']['enhancement_coverage']['methods_with_examples'] += methods_with_examples
                
                # Store file details
                report['file_details'][class_name] = {
                    'success': success,
                    'file_size': file_size,
                    'method_count': len(enhanced_stub.methods),
                    'methods_with_javadoc': methods_with_javadoc,
                    'methods_with_examples': methods_with_examples,
                    'enhancement_quality': enhanced_stub.enhancement_metadata.get('enhancement_quality_score', 0.0)
                }
            else:
                report['file_details'][class_name] = {
                    'success': success,
                    'error': 'Write operation failed'
                }
                if not success:
                    report['errors'].append(f"Failed to write {class_name}.json")
        
        # Calculate percentages
        if report['summary']['total_files'] > 0:
            report['summary']['success_rate'] = round(
                (report['summary']['successful_writes'] / report['summary']['total_files']) * 100, 1
            )
        
        return report
    
    def cleanup_backups(self, days_to_keep: int = 7) -> int:
        """
        Clean up old backup files.
        
        Args:
            days_to_keep: Number of days to keep backup files
            
        Returns:
            Number of backup files deleted
        """
        if not self.backup_enabled or not self.backup_dir.exists():
            return 0
        
        deleted_count = 0
        cutoff_time = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
        
        try:
            for backup_file in self.backup_dir.glob('*.json'):
                if backup_file.stat().st_mtime < cutoff_time:
                    backup_file.unlink()
                    deleted_count += 1
                    self.logger.debug(f"Deleted old backup: {backup_file}")
            
            self.logger.info(f"Cleaned up {deleted_count} old backup files")
            
        except Exception as e:
            self.logger.error(f"Failed to cleanup backups: {e}")
        
        return deleted_count