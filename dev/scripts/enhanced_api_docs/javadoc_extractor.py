"""
Javadoc ZIP extraction and management.
"""

import zipfile
import shutil
from pathlib import Path
from typing import Optional, List

from .config import config
from .logging_setup import get_logger

logger = get_logger('javadoc_extractor')


class JavaDocExtractor:
    """Handles extraction and management of JavaDoc ZIP files."""
    
    def __init__(self):
        self.zip_path = config.get_path('javadoc.source_zip')
        self.extract_dir = config.get_path('javadoc.extract_dir')
        self.extracted = self._is_extracted()
    
    def extract_javadoc(self, force: bool = False) -> bool:
        """
        Extract JavaDoc ZIP file to the configured directory.
        
        Args:
            force: If True, re-extract even if already extracted
            
        Returns:
            True if extraction successful, False otherwise
        """
        if not self.zip_path.exists():
            logger.error(f"JavaDoc ZIP file not found: {self.zip_path}")
            return False
        
        # Check if already extracted
        if not force and self.extract_dir.exists() and self._is_extracted():
            logger.info(f"JavaDoc already extracted to: {self.extract_dir}")
            self.extracted = True
            return True
        
        # Clean extract directory if it exists
        if self.extract_dir.exists():
            logger.info(f"Cleaning existing extract directory: {self.extract_dir}")
            shutil.rmtree(self.extract_dir)
        
        # Create extract directory
        self.extract_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            logger.info(f"Extracting JavaDoc ZIP: {self.zip_path}")
            logger.info(f"Extract destination: {self.extract_dir}")
            
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                # Get list of files to extract
                file_list = zip_ref.namelist()
                logger.info(f"Found {len(file_list)} files in ZIP")
                
                # Extract all files
                zip_ref.extractall(self.extract_dir)
                
                # Log some sample extracted files
                html_files = [f for f in file_list if f.endswith('.html')]
                logger.info(f"Extracted {len(html_files)} HTML files")
                
                if html_files:
                    logger.debug("Sample HTML files:")
                    for html_file in html_files[:5]:  # Show first 5
                        logger.debug(f"  - {html_file}")
                    if len(html_files) > 5:
                        logger.debug(f"  ... and {len(html_files) - 5} more")
            
            self.extracted = True
            logger.info("JavaDoc extraction completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to extract JavaDoc ZIP: {e}")
            return False
    
    def _is_extracted(self) -> bool:
        """Check if JavaDoc has been properly extracted."""
        # Look for common JavaDoc files/directories
        # Handle nested directory structure from ZIP
        javadoc_root = self._find_javadoc_root()
        if not javadoc_root:
            return False
            
        expected_items = [
            'index.html',
            'allclasses-index.html',
            'sc'  # Main package directory
        ]
        
        for item in expected_items:
            if not (javadoc_root / item).exists():
                return False
        
        return True
    
    def _find_javadoc_root(self) -> Optional[Path]:
        """Find the actual JavaDoc root directory (handles nested ZIP structure)."""
        if not self.extract_dir.exists():
            return None
        
        # Check if files are directly in extract_dir
        if (self.extract_dir / 'index.html').exists():
            return self.extract_dir
        
        # Look for nested directories that contain index.html
        for item in self.extract_dir.iterdir():
            if item.is_dir():
                if (item / 'index.html').exists():
                    return item
        
        return None
    
    def find_class_html_files(self) -> List[Path]:
        """
        Find all class HTML files in the extracted JavaDoc.
        
        Returns:
            List of paths to class HTML files
        """
        if not self.extracted:
            logger.warning("JavaDoc not extracted yet")
            return []
        
        # Find the actual JavaDoc root directory
        javadoc_root = self._find_javadoc_root()
        if not javadoc_root:
            logger.warning("Could not find JavaDoc root directory")
            return []
        
        # Look for HTML files in the sc/fiji/snt directory structure
        html_files = []
        snt_dir = javadoc_root / 'sc' / 'fiji' / 'snt'
        
        if snt_dir.exists():
            # Find all HTML files recursively
            html_files = list(snt_dir.rglob('*.html'))
            
            # Filter out non-class files (package-summary, etc.)
            class_files = []
            for html_file in html_files:
                filename = html_file.name
                if (not filename.startswith('package-') and 
                    not filename.startswith('class-use') and
                    filename != 'index.html'):
                    class_files.append(html_file)
            
            logger.info(f"Found {len(class_files)} class HTML files")
            return class_files
        else:
            logger.warning(f"SNT package directory not found: {snt_dir}")
            return []
    
    def get_class_html_path(self, class_name: str, package: str = 'sc.fiji.snt') -> Optional[Path]:
        """
        Get the path to a specific class HTML file.
        
        Args:
            class_name: Name of the Java class
            package: Java package name (default: sc.fiji.snt)
            
        Returns:
            Path to class HTML file if found, None otherwise
        """
        if not self.extracted:
            logger.warning("JavaDoc not extracted yet")
            return None
        
        # Find the actual JavaDoc root directory
        javadoc_root = self._find_javadoc_root()
        if not javadoc_root:
            logger.warning("Could not find JavaDoc root directory")
            return None
        
        # Convert package name to directory path
        package_path = package.replace('.', '/')
        class_html_path = javadoc_root / package_path / f'{class_name}.html'
        
        if class_html_path.exists():
            return class_html_path
        else:
            logger.debug(f"Class HTML file not found: {class_html_path}")
            return None
    
    def cleanup(self):
        """Clean up extracted JavaDoc files."""
        if self.extract_dir.exists():
            logger.info(f"Cleaning up extracted JavaDoc: {self.extract_dir}")
            shutil.rmtree(self.extract_dir)
            self.extracted = False
    
    def get_extraction_info(self) -> dict:
        """Get information about the extracted JavaDoc."""
        info = {
            'zip_path': str(self.zip_path),
            'extract_dir': str(self.extract_dir),
            'extracted': self.extracted,
            'zip_exists': self.zip_path.exists(),
            'extract_dir_exists': self.extract_dir.exists()
        }
        
        if self.extracted:
            class_files = self.find_class_html_files()
            info['class_files_count'] = len(class_files)
            info['sample_classes'] = [f.stem for f in class_files[:10]]
        
        return info