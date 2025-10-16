#!/usr/bin/env python3
"""
Utility script to generate placeholder classes for PySNT modules.

1. Parses all __init__.py files to extract CURATED_CLASSES and EXTENDED_CLASSES
2. Generates placeholder classes with proper docstrings and Javadoc links
3. Updates the __init__.py files with the generated placeholders

Usage:
    python scripts/generate_placeholders.py                    # Generate placeholders
    python scripts/generate_placeholders.py --dry-run          # Preview changes only
    python scripts/generate_placeholders.py --extended         # Include extended classes too
    python scripts/generate_placeholders.py --reset            # Remove existing placeholders
    python scripts/generate_placeholders.py --reset --dry-run  # Preview placeholder removal
"""

import ast
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Base Javadoc URL
JAVADOC_BASE_URL = "https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt"

class PlaceholderGenerator:
    """Generates placeholder classes for PySNT modules."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.src_root = project_root / "src" / "pysnt"
        
    def find_init_files(self) -> List[Path]:
        """Find all __init__.py files in the pysnt package."""
        init_files = []
        for init_file in self.src_root.rglob("__init__.py"):
            # Skip __pycache__ and other non-source directories
            if "__pycache__" not in str(init_file):
                init_files.append(init_file)
        return sorted(init_files)
    
    def parse_class_lists(self, init_file: Path) -> Tuple[List[str], List[str], str]:
        """
        Parse CURATED_CLASSES and EXTENDED_CLASSES from an __init__.py file.
        
        Returns:
            Tuple of (curated_classes, extended_classes, package_path)
        """
        try:
            content = init_file.read_text(encoding='utf-8')
            tree = ast.parse(content)
            
            curated_classes = []
            extended_classes = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            if target.id == "CURATED_CLASSES" and isinstance(node.value, ast.List):
                                curated_classes = self._extract_string_list(node.value)
                            elif target.id == "EXTENDED_CLASSES" and isinstance(node.value, ast.List):
                                extended_classes = self._extract_string_list(node.value)
                            elif target.id == "CURATED_ROOT_CLASSES" and isinstance(node.value, ast.List):
                                # Handle main module's root classes
                                curated_classes = self._extract_string_list(node.value)
            
            # Determine package path from file location
            package_path = self._get_package_path(init_file)
            
            return curated_classes, extended_classes, package_path
            
        except Exception as e:
            logger.error(f"Failed to parse {init_file}: {e}")
            return [], [], ""
    
    def _extract_string_list(self, list_node: ast.List) -> List[str]:
        """Extract string values from an AST List node."""
        strings = []
        for item in list_node.elts:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                strings.append(item.value)
            elif isinstance(item, ast.Str):  # Python < 3.8 compatibility
                strings.append(item.s)
        return strings
    
    def _get_package_path(self, init_file: Path) -> str:
        """
        Convert file path to Java package path.
        
        Examples:
            src/pysnt/__init__.py -> ""
            src/pysnt/analysis/__init__.py -> "analysis"
            src/pysnt/analysis/growth/__init__.py -> "analysis/growth"
        """
        relative_path = init_file.relative_to(self.src_root)
        parts = relative_path.parts[:-1]  # Remove __init__.py
        return "/".join(parts) if parts else ""
    
    def generate_javadoc_url(self, class_name: str, package_path: str) -> str:
        """Generate Javadoc URL for a class."""
        if package_path:
            full_path = f"{JAVADOC_BASE_URL}/{package_path}/{class_name}.html"
        else:
            full_path = f"{JAVADOC_BASE_URL}/{class_name}.html"
        return full_path
    
    def generate_placeholder_class(self, class_name: str, package_path: str, is_extended: bool = False) -> str:
        """
        Generate placeholder class code with docstring and Javadoc link.
        
        Args:
            class_name: Name of the class
            package_path: Package path (e.g., "analysis", "analysis/growth")
            is_extended: Whether this is an extended class
        """
        javadoc_url = self.generate_javadoc_url(class_name, package_path)
        
        # Determine class type description
        if is_extended:
            class_type = "Extended SNT class"
            availability = "Available via get_class() after JVM initialization"
        else:
            class_type = "Curated SNT class"
            availability = "Available for direct import after JVM initialization"
        
        # Generate package description for docstring
        if package_path:
            package_desc = f" from {package_path} package"
        else:
            package_desc = " from root package"
        
        placeholder_code = f'''class {class_name}:
    """
    {class_type}{package_desc} with method signatures.
    
    {availability}.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: {javadoc_url}
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")'''
        
        return placeholder_code
    
    def find_placeholder_section(self, content: str) -> Tuple[Optional[int], Optional[int]]:
        """
        Find the placeholder classes section in the file content.
        
        Returns:
            Tuple of (start_line_index, end_line_index) or (None, None) if not found
        """
        lines = content.split('\n')
        start_idx = None
        end_idx = None
        
        # Look for placeholder section markers
        for i, line in enumerate(lines):
            if "# Placeholder classes for IDE support" in line:
                start_idx = i
            elif start_idx is not None and (
                line.startswith("# Import submodules") or 
                line.startswith("# Setup common module") or
                line.startswith("from . import") or
                line.startswith("_module_funcs = setup_module_classes") or
                line.startswith("__all__ = [")
            ):
                end_idx = i
                break
        
        # If we found a start but no clear end, look for the next non-placeholder content
        if start_idx is not None and end_idx is None:
            # Look for patterns that indicate end of placeholder section
            in_class = False
            in_docstring = False
            
            for i in range(start_idx + 1, len(lines)):
                line = lines[i].strip()
                
                # Track if we're inside a class definition
                if line.startswith("class "):
                    in_class = True
                    continue
                
                # Track docstring state
                if '"""' in line:
                    # Count quotes in this line
                    quote_count = line.count('"""')
                    if quote_count % 2 == 1:  # Odd number toggles state
                        in_docstring = not in_docstring
                    continue
                
                # Skip placeholder class content
                if (line == "" or 
                    in_docstring or
                    line.startswith("def __") or
                    line.startswith("raise RuntimeError") or
                    line.startswith(".. _Javadoc") or
                    line.startswith("See `Javadoc") or
                    "Available for direct import" in line or
                    "Call pysnt.initialize()" in line or
                    "Dynamic attribute access" in line or
                    "Placeholder constructor" in line or
                    "Curated SNT class" in line or
                    "Extended SNT class" in line):
                    continue
                
                # If we're in a class and hit a non-placeholder line, we might be done
                if in_class and not (line.startswith("def ") or line.startswith("class ")):
                    # Check if this looks like the end of placeholder section
                    if (line.startswith("# ") or 
                        line.startswith("from ") or
                        line.startswith("import ") or
                        line.startswith("_module_funcs") or
                        line.startswith("__all__")):
                        end_idx = i
                        break
                
                # If we hit a new section that's clearly not placeholder content
                if (line.startswith("# Import") or 
                    line.startswith("# Setup") or
                    line.startswith("from . import") or
                    line.startswith("_module_funcs") or
                    line.startswith("__all__")):
                    end_idx = i
                    break
        
        return start_idx, end_idx
    
    def remove_placeholders_from_file(self, init_file: Path, dry_run: bool = False) -> bool:
        """
        Remove existing placeholder classes from an __init__.py file.
        
        Args:
            init_file: Path to the __init__.py file
            dry_run: If True, don't actually modify the file
            
        Returns:
            True if file was modified, False otherwise
        """
        try:
            content = init_file.read_text(encoding='utf-8')
            original_content = content
            
            # Find existing placeholder section
            start_idx, end_idx = self.find_placeholder_section(content)
            
            if start_idx is not None and end_idx is not None:
                lines = content.split('\n')
                
                # Remove the placeholder section (including empty lines before/after)
                # Clean up extra empty lines
                new_lines = lines[:start_idx]
                
                # Skip empty lines before the next section
                remaining_lines = lines[end_idx:]
                while remaining_lines and remaining_lines[0].strip() == "":
                    remaining_lines = remaining_lines[1:]
                
                new_lines.extend(remaining_lines)
                new_content = '\n'.join(new_lines)
                
                if new_content != original_content:
                    if not dry_run:
                        init_file.write_text(new_content, encoding='utf-8')
                        logger.info(f"Removed placeholders from {init_file.relative_to(self.project_root)}")
                    else:
                        logger.info(f"Would remove placeholders from {init_file.relative_to(self.project_root)}")
                    return True
                else:
                    logger.info(f"No placeholder changes needed for {init_file.relative_to(self.project_root)}")
                    return False
            else:
                logger.info(f"No placeholders found in {init_file.relative_to(self.project_root)}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to remove placeholders from {init_file}: {e}")
            return False
    
    def generate_placeholders_for_file(self, init_file: Path, include_extended: bool = False) -> str:
        """Generate all placeholder classes for a single __init__.py file."""
        curated_classes, extended_classes, package_path = self.parse_class_lists(init_file)
        
        if not curated_classes and not extended_classes:
            return ""
        
        placeholders = []
        placeholders.append("# Placeholder classes for IDE support - will be replaced with Java classes")
        
        # Generate curated class placeholders
        for class_name in curated_classes:
            placeholder = self.generate_placeholder_class(class_name, package_path, is_extended=False)
            placeholders.append(placeholder)
            placeholders.append("")  # Empty line between classes
        
        # Generate extended class placeholders if requested
        if include_extended:
            if extended_classes:
                placeholders.append("# Extended class placeholders (for enhanced IDE support)")
            for class_name in extended_classes:
                placeholder = self.generate_placeholder_class(class_name, package_path, is_extended=True)
                placeholders.append(placeholder)
                placeholders.append("")  # Empty line between classes
        
        return "\n".join(placeholders)
    
    def update_init_file(self, init_file: Path, include_extended: bool = False, dry_run: bool = False) -> bool:
        """
        Update an __init__.py file with generated placeholder classes.
        
        Returns:
            True if file was modified, False otherwise
        """
        try:
            content = init_file.read_text(encoding='utf-8')
            original_content = content
            
            # Generate new placeholders
            new_placeholders = self.generate_placeholders_for_file(init_file, include_extended)
            
            if not new_placeholders:
                logger.info(f"No classes found in {init_file.relative_to(self.project_root)}")
                return False
            
            # Find existing placeholder section
            start_idx, end_idx = self.find_placeholder_section(content)
            
            lines = content.split('\n')
            
            if start_idx is not None and end_idx is not None:
                # Replace existing placeholder section
                new_lines = lines[:start_idx] + new_placeholders.split('\n') + lines[end_idx:]
                new_content = '\n'.join(new_lines)
            else:
                # Insert placeholders before imports/setup section
                insert_idx = self._find_insertion_point(lines)
                new_lines = lines[:insert_idx] + [''] + new_placeholders.split('\n') + [''] + lines[insert_idx:]
                new_content = '\n'.join(new_lines)
            
            if new_content != original_content:
                if not dry_run:
                    init_file.write_text(new_content, encoding='utf-8')
                    logger.info(f"Updated {init_file.relative_to(self.project_root)}")
                else:
                    logger.info(f"Would update {init_file.relative_to(self.project_root)}")
                return True
            else:
                logger.info(f"No changes needed for {init_file.relative_to(self.project_root)}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to update {init_file}: {e}")
            return False
    
    def _find_insertion_point(self, lines: List[str]) -> int:
        """Find the best place to insert placeholder classes."""
        # Look for common patterns where placeholders should be inserted
        for i, line in enumerate(lines):
            if any(pattern in line for pattern in [
                "# Import submodules",
                "# Setup common module", 
                "from . import",
                "_module_funcs = setup_module_classes"
            ]):
                return i
        
        # Default to end of file
        return len(lines)
    
    def process_all_files(self, include_extended: bool = False, dry_run: bool = False, reset_only: bool = False) -> Dict[str, int]:
        """
        Process all __init__.py files and generate placeholders or reset them.
        
        Args:
            include_extended: Include extended classes in placeholders
            dry_run: Preview changes without modifying files
            reset_only: Only remove existing placeholders, don't generate new ones
            
        Returns:
            Dictionary with statistics
        """
        init_files = self.find_init_files()
        stats = {
            'total_files': len(init_files),
            'modified_files': 0,
            'total_curated_classes': 0,
            'total_extended_classes': 0
        }
        
        logger.info(f"Found {len(init_files)} __init__.py files")
        
        for init_file in init_files:
            logger.info(f"Processing {init_file.relative_to(self.project_root)}...")
            
            # Count classes
            curated, extended, _ = self.parse_class_lists(init_file)
            stats['total_curated_classes'] += len(curated)
            stats['total_extended_classes'] += len(extended)
            
            # Process file based on mode
            if reset_only:
                # Only remove existing placeholders
                if self.remove_placeholders_from_file(init_file, dry_run):
                    stats['modified_files'] += 1
            else:
                # Generate/update placeholders
                if self.update_init_file(init_file, include_extended, dry_run):
                    stats['modified_files'] += 1
        
        return stats


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate placeholder classes for PySNT modules")
    parser.add_argument('--dry-run', action='store_true', 
                       help='Preview changes without modifying files')
    parser.add_argument('--extended', action='store_true',
                       help='Include extended classes in placeholders')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--reset', action='store_true',
                       help='Remove existing placeholders without generating new ones (useful for debugging)')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    if not (project_root / "src" / "pysnt").exists():
        logger.error("Could not find src/pysnt directory. Run from project root.")
        return 1
    
    # Generate or reset placeholders
    generator = PlaceholderGenerator(project_root)
    
    if args.reset:
        logger.info("Removing existing placeholder classes from PySNT modules...")
        if args.dry_run:
            logger.info("DRY RUN MODE - No files will be modified")
        
        stats = generator.process_all_files(
            include_extended=False,  # Not relevant for reset
            dry_run=args.dry_run,
            reset_only=True
        )
        
        # Print summary
        logger.info("=" * 50)
        logger.info("RESET SUMMARY:")
        logger.info(f"  Files processed: {stats['total_files']}")
        logger.info(f"  Files modified: {stats['modified_files']}")
        logger.info(f"  Curated classes found: {stats['total_curated_classes']}")
        logger.info(f"  Extended classes found: {stats['total_extended_classes']}")
        
        if args.dry_run:
            logger.info("\nRun without --dry-run to apply changes")
        else:
            logger.info("\n✅ Placeholder removal complete!")
            logger.info("💡 Run without --reset to regenerate placeholders")
    
    else:
        logger.info("Generating placeholder classes for PySNT modules...")
        if args.dry_run:
            logger.info("DRY RUN MODE - No files will be modified")
        if args.extended:
            logger.info("Including extended classes in placeholders")
        
        stats = generator.process_all_files(
            include_extended=args.extended,
            dry_run=args.dry_run,
            reset_only=False
        )
        
        # Print summary
        logger.info("=" * 50)
        logger.info("GENERATION SUMMARY:")
        logger.info(f"  Files processed: {stats['total_files']}")
        logger.info(f"  Files modified: {stats['modified_files']}")
        logger.info(f"  Curated classes: {stats['total_curated_classes']}")
        logger.info(f"  Extended classes: {stats['total_extended_classes']}")
        
        if args.dry_run:
            logger.info("\nRun without --dry-run to apply changes")
        else:
            logger.info("\n✅ Placeholder generation complete!")
            logger.info("💡 Use --reset to remove placeholders for debugging")
    
    return 0


if __name__ == "__main__":
    exit(main())