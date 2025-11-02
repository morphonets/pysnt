#!/usr/bin/env python3
"""
PySNT Development Utilities

Provides utility functions for PySNT development and maintenance:
1. Quality control validation (detects duplicate classes, naming issues, etc.)
2. Import depth fixing for common_module imports
3. Cleaning up unused typing imports in .pyi files
4. Module configuration analysis

Usage:
    python scripts/pysnt_utils.py --qc                    # Run quality control validation
    python scripts/pysnt_utils.py --fix-imports           # Fix import depths
    python scripts/pysnt_utils.py --clean-pyi-imports     # Clean unused typing imports
    python scripts/pysnt_utils.py --analyze               # Analyze module configurations
"""

import ast
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class QualityControlError(Exception):
    """Exception raised when QC validation fails."""
    pass


class PySNTUtils:
    """Utility functions for PySNT development and maintenance."""
    
    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.src_root = self.project_root / "src" / "pysnt"
        
        # Quality control validation rules
        self.validation_rules = [
            self._validate_no_duplicate_classes,
            self._validate_inner_class_naming,
        ]
    
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
        
        Args:
            init_file: Path to the __init__.py file
        
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
    
    def validate_module(self, init_file: Path, curated_classes: List[str], 
                       extended_classes: List[str], package_path: str) -> None:
        """
        Run all QC validation rules on a module.
        
        Args:
            init_file: Path to the __init__.py file
            curated_classes: List of curated class names
            extended_classes: List of extended class names  
            package_path: Java package path
            
        Raises:
            QualityControlError: If any validation rule fails
        """
        for rule in self.validation_rules:
            rule(init_file, curated_classes, extended_classes, package_path)
    
    def _validate_no_duplicate_classes(self, init_file: Path, curated_classes: List[str],
                                     extended_classes: List[str], package_path: str) -> None:
        """Validate that CURATED_CLASSES and EXTENDED_CLASSES don't share common entries."""
        curated_set = set(curated_classes)
        extended_set = set(extended_classes)
        duplicates = curated_set.intersection(extended_set)
        
        if duplicates:
            relative_path = init_file.relative_to(Path.cwd()) if init_file.is_absolute() else init_file
            raise QualityControlError(
                f"QC FAILURE in {relative_path}: "
                f"Classes appear in both CURATED_CLASSES and EXTENDED_CLASSES: {sorted(duplicates)}\\n"
                f"Each class should only appear in one list. Move duplicates to either CURATED_CLASSES "
                f"(for commonly used classes) or EXTENDED_CLASSES (for less common classes)."
            )
    
    def _validate_inner_class_naming(self, init_file: Path, curated_classes: List[str],
                                   extended_classes: List[str], package_path: str) -> None:
        """Validate that inner class names use underscore notation, not dollar signs."""
        all_classes = curated_classes + extended_classes
        dollar_classes = [cls for cls in all_classes if '$' in cls]
        
        if dollar_classes:
            relative_path = init_file.relative_to(Path.cwd()) if init_file.is_absolute() else init_file
            raise QualityControlError(
                f"QC FAILURE in {relative_path}: "
                f"Inner class names should use underscore notation, not dollar signs: {dollar_classes}\\n"
                f"Example: Use 'OuterClass_InnerClass' instead of 'OuterClass$InnerClass'"
            )
    
    def run_quality_control(self) -> Dict[str, int]:
        """Run quality control validation on all modules."""
        init_files = self.find_init_files()
        stats = {
            'total_files': len(init_files),
            'total_curated_classes': 0,
            'total_extended_classes': 0,
        }
        
        logger.info(f"Running quality control validation on {len(init_files)} modules...")
        
        for init_file in init_files:
            logger.info(f"Validating {init_file.relative_to(self.project_root)}...")
            
            try:
                curated, extended, package_path = self.parse_class_lists(init_file)
                stats['total_curated_classes'] += len(curated)
                stats['total_extended_classes'] += len(extended)
                
                # Run validation
                self.validate_module(init_file, curated, extended, package_path)
                logger.info(f"  ✅ {len(curated)} curated, {len(extended)} extended classes")
                
            except QualityControlError as e:
                logger.error(f"❌ Quality Control validation failed: {e}")
                raise
        
        return stats
    
    def fix_import_depths(self, dry_run: bool = False) -> Dict[str, int]:
        """Fix import depths for common_module imports in all __init__.py files."""
        init_files = self.find_init_files()
        stats = {
            'total_files': len(init_files),
            'modified_files': 0,
        }
        
        logger.info(f"Fixing import depths in {len(init_files)} __init__.py files")
        
        for init_file in init_files:
            try:
                content = init_file.read_text(encoding='utf-8')
                original_content = content
                
                # Calculate correct import depth
                import_depth = self._get_import_depth(init_file)
                dots = "." * import_depth
                
                # Fix the import statement
                pattern = r'from \\.+common_module import setup_module_classes'
                replacement = f'from {dots}common_module import setup_module_classes'
                
                if re.search(pattern, content):
                    new_content = re.sub(pattern, replacement, content)
                    
                    if new_content != original_content:
                        if not dry_run:
                            init_file.write_text(new_content, encoding='utf-8')
                            logger.info(f"Fixed import depth in {init_file.relative_to(self.project_root)} (depth: {import_depth})")
                        else:
                            logger.info(f"Would fix import depth in {init_file.relative_to(self.project_root)} (depth: {import_depth})")
                        stats['modified_files'] += 1
                    else:
                        logger.debug(f"Import depth already correct in {init_file.relative_to(self.project_root)}")
                else:
                    logger.debug(f"No common_module import found in {init_file.relative_to(self.project_root)}")
                    
            except Exception as e:
                logger.error(f"Failed to fix import depth in {init_file}: {e}")
        
        return stats
    
    def _get_import_depth(self, init_file: Path) -> int:
        """Calculate the correct import depth for common_module import."""
        relative_path = init_file.relative_to(self.src_root)
        parts = relative_path.parts[:-1]  # Remove __init__.py
        return len(parts) + 1  # +1 because we need to go up to pysnt level
    
    def clean_unused_typing_imports(self, dry_run: bool = False) -> Dict[str, int]:
        """Clean up unused typing imports in .pyi files."""
        pyi_files = list(self.src_root.rglob("*.pyi"))
        pyi_files = [f for f in pyi_files if "__pycache__" not in str(f)]
        
        stats = {
            'total_files': len(pyi_files),
            'modified_files': 0,
            'imports_removed': 0,
        }
        
        logger.info(f"Cleaning unused typing imports in {len(pyi_files)} .pyi files")
        
        # Common typing imports to check
        typing_imports = [
            'Any', 'List', 'Dict', 'Optional', 'Union', 'overload', 'Set', 
            'Tuple', 'Callable', 'Iterator', 'Iterable', 'Sequence', 'Mapping'
        ]
        
        for pyi_file in pyi_files:
            try:
                content = pyi_file.read_text(encoding='utf-8')
                original_content = content
                
                # Find the typing import line
                typing_import_pattern = r'^from typing import (.+)$'
                
                lines = content.split('\\n')
                modified = False
                
                for i, line in enumerate(lines):
                    match = re.match(typing_import_pattern, line.strip())
                    if match:
                        imports_str = match.group(1)
                        
                        # Parse the imports (handle both comma-separated and multi-line)
                        current_imports = []
                        if imports_str.strip():
                            # Split by comma and clean up
                            for imp in imports_str.split(','):
                                imp = imp.strip()
                                if imp:
                                    current_imports.append(imp)
                        
                        # Check which imports are actually used in the file
                        # Exclude the import line itself from the search
                        content_without_import = content.replace(line, "")
                        used_imports = []
                        
                        for imp in current_imports:
                            # Check if the import is used in the file (excluding the import line)
                            # Look for the import name as a standalone word
                            if re.search(rf'\\b{re.escape(imp)}\\b', content_without_import):
                                used_imports.append(imp)
                        
                        # If we have unused imports, update the line
                        if len(used_imports) != len(current_imports):
                            removed_count = len(current_imports) - len(used_imports)
                            stats['imports_removed'] += removed_count
                            
                            if used_imports:
                                # Create new import line with only used imports
                                new_import_line = f"from typing import {', '.join(sorted(used_imports))}"
                                lines[i] = new_import_line
                                logger.debug(f"Updated typing imports in {pyi_file.relative_to(self.project_root)}: {', '.join(sorted(used_imports))}")
                            else:
                                # Remove the entire import line if no imports are used
                                lines[i] = ""
                                logger.debug(f"Removed unused typing import line from {pyi_file.relative_to(self.project_root)}")
                            
                            modified = True
                        else:
                            logger.debug(f"All typing imports used in {pyi_file.relative_to(self.project_root)}")
                        
                        break  # Only process the first typing import line
                
                if modified:
                    new_content = '\\n'.join(lines)
                    # Clean up multiple consecutive empty lines
                    new_content = re.sub(r'\\n\\n\\n+', '\\n\\n', new_content)
                    
                    if not dry_run:
                        pyi_file.write_text(new_content, encoding='utf-8')
                        logger.info(f"Cleaned typing imports in {pyi_file.relative_to(self.project_root)}")
                    else:
                        logger.info(f"Would clean typing imports in {pyi_file.relative_to(self.project_root)}")
                    stats['modified_files'] += 1
                else:
                    logger.debug(f"No unused typing imports in {pyi_file.relative_to(self.project_root)}")
                    
            except Exception as e:
                logger.error(f"Failed to clean typing imports in {pyi_file}: {e}")
        
        return stats
    
    def analyze_modules(self) -> Dict[str, any]:
        """Analyze all modules and provide a summary."""
        init_files = self.find_init_files()
        analysis = {
            'total_modules': len(init_files),
            'modules': {},
            'total_curated': 0,
            'total_extended': 0,
        }
        
        logger.info(f"Analyzing {len(init_files)} modules...")
        
        for init_file in init_files:
            try:
                curated, extended, package_path = self.parse_class_lists(init_file)
                
                module_name = package_path if package_path else "pysnt"
                analysis['modules'][module_name] = {
                    'curated_classes': curated,
                    'extended_classes': extended,
                    'curated_count': len(curated),
                    'extended_count': len(extended),
                    'total_count': len(curated) + len(extended),
                }
                
                analysis['total_curated'] += len(curated)
                analysis['total_extended'] += len(extended)
                
            except Exception as e:
                logger.error(f"Failed to analyze {init_file}: {e}")
        
        return analysis


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="PySNT Development Utilities",
        epilog="Provides utility functions for PySNT development and maintenance."
    )
    parser.add_argument('--qc', action='store_true',
                       help='Run quality control validation')
    parser.add_argument('--fix-imports', action='store_true',
                       help='Fix import depths for common_module imports')
    parser.add_argument('--clean-pyi-imports', action='store_true',
                       help='Clean up unused typing imports in .pyi files')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze module configurations')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview changes without modifying files')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent  # dev/scripts -> dev -> project_root
    
    if not (project_root / "src" / "pysnt").exists():
        logger.error("Could not find src/pysnt directory. Run from project root.")
        return 1
    
    utils = PySNTUtils(project_root)
    
    if args.qc:
        logger.info("Running quality control validation...")
        try:
            stats = utils.run_quality_control()
            
            logger.info("=" * 50)
            logger.info("QUALITY CONTROL SUMMARY:")
            logger.info(f"  Files validated: {stats['total_files']}")
            logger.info(f"  Total curated classes: {stats['total_curated_classes']}")
            logger.info(f"  Total extended classes: {stats['total_extended_classes']}")
            logger.info("✅ All quality control checks passed!")
            
        except QualityControlError:
            return 1
    
    elif args.fix_imports:
        logger.info("Fixing import depths for common_module imports...")
        if args.dry_run:
            logger.info("DRY RUN MODE - No files will be modified")
        
        stats = utils.fix_import_depths(dry_run=args.dry_run)
        
        logger.info("=" * 50)
        logger.info("IMPORT DEPTH FIX SUMMARY:")
        logger.info(f"  Files processed: {stats['total_files']}")
        logger.info(f"  Files modified: {stats['modified_files']}")
        
        if args.dry_run:
            logger.info("\\nRun without --dry-run to apply changes")
        else:
            logger.info("\\n✅ Import depth fixing complete!")
    
    elif args.clean_pyi_imports:
        logger.info("Cleaning unused typing imports in .pyi files...")
        if args.dry_run:
            logger.info("DRY RUN MODE - No files will be modified")
        
        stats = utils.clean_unused_typing_imports(dry_run=args.dry_run)
        
        logger.info("=" * 50)
        logger.info("TYPING IMPORT CLEANUP SUMMARY:")
        logger.info(f"  Files processed: {stats['total_files']}")
        logger.info(f"  Files modified: {stats['modified_files']}")
        logger.info(f"  Imports removed: {stats['imports_removed']}")
        
        if args.dry_run:
            logger.info("\\nRun without --dry-run to apply changes")
        else:
            logger.info("\\n✅ Typing import cleanup complete!")
    
    elif args.analyze:
        logger.info("Analyzing module configurations...")
        
        analysis = utils.analyze_modules()
        
        logger.info("=" * 50)
        logger.info("MODULE ANALYSIS SUMMARY:")
        logger.info(f"  Total modules: {analysis['total_modules']}")
        logger.info(f"  Total curated classes: {analysis['total_curated']}")
        logger.info(f"  Total extended classes: {analysis['total_extended']}")
        logger.info("")
        
        # Show per-module breakdown
        for module_name, data in sorted(analysis['modules'].items()):
            logger.info(f"  📦 {module_name}:")
            logger.info(f"    Curated: {data['curated_count']}, Extended: {data['extended_count']}")
            if args.verbose and data['curated_classes']:
                logger.info(f"    Classes: {', '.join(data['curated_classes'][:5])}{'...' if len(data['curated_classes']) > 5 else ''}")
    
    else:
        # Show help if no action specified
        parser.print_help()
        return 0
    
    return 0


if __name__ == "__main__":
    exit(main())