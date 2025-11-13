"""
Configuration management for the enhanced API documentation system.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml


class Config:
    """Configuration manager for enhanced API documentation system."""
    
    def __init__(self, config_file: Optional[Path] = None):
        """Initialize configuration with default values."""
        self.script_dir = Path(__file__).parent.parent
        self.project_root = self.script_dir.parent.parent
        
        # Default configuration
        self.config = {
            'javadoc': {
                'source_zip': self.script_dir / 'SNT-v5.0.0-pre-release3_javadocs.zip',
                'extract_dir': self.script_dir / 'javadoc_extracted',
                'base_url': 'https://javadoc.scijava.org/SNT/'
            },
            'json_stubs': {
                'directory': self.script_dir / 'STUBS',
                'file_pattern': '*.json'
            },
            'output': {
                'docs_dir': self.project_root / 'docs' / 'pysnt',
                'class_pages_dir': self.project_root / 'docs' / 'pysnt',
                'index_file': self.project_root / 'docs' / 'api_auto' / 'method_index.rst'
            },
            'generation': {
                'categories': [
                    'Getters',
                    'Setters', 
                    'Analysis',
                    'I/O Operations',
                    'Visualization',
                    'Utilities',
                    'Static Methods'
                ],
                'include_examples': True,
                'include_deprecated': False,
                'cross_reference_depth': 2
            },
            'sphinx': {
                'integrate_with_existing': True,
                'toctree_maxdepth': 3,
                'add_to_main_index': True,
                'inject_toctree': True,
                'toctree_caption': 'Complete API Reference',
                'toctree_hidden': True
            },
            'caching': {
                'enable_cache': True,
                'cache_dir': self.script_dir / 'cache',
                'cache_ttl_days': 7
            },
            'logging': {
                'level': 'INFO',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        }
        
        # Load custom configuration if provided
        if config_file and config_file.exists():
            self.load_config(config_file)
    
    def load_config(self, config_file: Path):
        """Load configuration from YAML file."""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                custom_config = yaml.safe_load(f)
            
            # Merge custom config with defaults
            self._merge_config(self.config, custom_config)
        except Exception as e:
            print(f"Warning: Failed to load config file {config_file}: {e}")
    
    def _merge_config(self, base: Dict[str, Any], custom: Dict[str, Any]):
        """Recursively merge custom configuration with base configuration."""
        for key, value in custom.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value
    
    def get(self, key_path: str, default=None):
        """Get configuration value using dot notation (e.g., 'javadoc.source_zip')."""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def get_path(self, key_path: str) -> Path:
        """Get configuration value as Path object."""
        value = self.get(key_path)
        if value is None:
            raise ValueError(f"Configuration key '{key_path}' not found")
        return Path(value)
    
    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        dirs_to_create = [
            self.get_path('javadoc.extract_dir'),
            self.get_path('output.docs_dir'),
            self.get_path('output.class_pages_dir'),
            self.get_path('caching.cache_dir')
        ]
        
        for directory in dirs_to_create:
            directory.mkdir(parents=True, exist_ok=True)
    
    def validate(self) -> bool:
        """Validate configuration and required files."""
        errors = []
        
        # Check if JavaDoc ZIP exists
        javadoc_zip = self.get_path('javadoc.source_zip')
        if not javadoc_zip.exists():
            errors.append(f"JavaDoc ZIP file not found: {javadoc_zip}")
        
        # Check if JSON stubs directory exists
        stubs_dir = self.get_path('json_stubs.directory')
        if not stubs_dir.exists():
            errors.append(f"JSON stubs directory not found: {stubs_dir}")
        
        # Check if there are any JSON stub files
        json_files = list(stubs_dir.glob(self.get('json_stubs.file_pattern', '*.json')))
        if not json_files:
            errors.append(f"No JSON stub files found in: {stubs_dir}")
        
        if errors:
            print("Configuration validation errors:")
            for error in errors:
                print(f"  - {error}")
            return False
        
        return True


# Global configuration instance
config = Config()