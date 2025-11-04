"""
Java utilities for PySNT.

This module handles Java/OpenJDK installation and configuration,
as well as Java class introspection utilities.

The reflection functions use scyjava's reflection tools:
- inspect(): Uses jreflect for detailed class inspection
- get_methods(): Uses jreflect to retrieve method information  
- get_fields(): Uses jreflect to retrieve field information
- is_instance_of(): Uses jinstance for type checking
- reflect_java_object(): Direct wrapper around jreflect
"""

import logging
import os
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Optional, Dict, Any, Union, List

import scyjava # noqa
import jpype # noqa

logger = logging.getLogger(__name__)

# Required Java version
REQUIRED_JAVA_VERSION = 21
MIN_JAVA_VERSION = 21  # Minimum for basic functionality


def check_java_installation() -> Dict[str, Any]:
    """
    Check current Java installation status.
    
    Returns
    -------
    Dict[str, Any]
        Dictionary with Java installation information:
        - 'available': bool - Whether Java is available
        - 'version': int or None - Java version number
        - 'version_string': str or None - Full version string
        - 'java_home': str or None - JAVA_HOME path
        - 'executable': str or None - Java executable path
        - 'vendor': str or None - Java vendor
        - 'meets_requirements': bool - Whether version meets requirements
    """
    result = {
        'available': False,
        'version': None,
        'version_string': None,
        'java_home': os.environ.get('JAVA_HOME'),
        'executable': None,
        'vendor': None,
        'meets_requirements': False
    }
    
    # Try to find Java executable
    java_executable = _find_java_executable()
    if not java_executable:
        return result
    
    result['executable'] = java_executable
    result['available'] = True
    
    # Get Java version information
    try:
        cmd = [java_executable, '-version']
        process = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        # Java version info goes to stderr
        version_output = process.stderr
        
        # Parse version information
        version_info = _parse_java_version(version_output)
        result.update(version_info)
        
        # Check if version meets requirements
        if result['version']:
            result['meets_requirements'] = result['version'] >= MIN_JAVA_VERSION
        
        logger.debug(f"Java check result: {result}")
        
    except Exception as e:
        logger.warning(f"Failed to check Java version: {e}")
    
    return result


def _find_java_executable() -> Optional[str]:
    """
    Find Java executable in system.
    
    Returns
    -------
    str or None
        Path to Java executable if found
    """
    # Check JAVA_HOME first
    java_home = os.environ.get('JAVA_HOME')
    if java_home:
        java_exe = Path(java_home) / 'bin' / 'java'
        if java_exe.exists():
            return str(java_exe)
    
    # Check PATH
    try:
        result = subprocess.run(['which', 'java'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    
    # Windows-specific check
    if sys.platform == 'win32':
        try:
            result = subprocess.run(['where', 'java'], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip().split('\n')[0]
        except:
            pass
    
    return None


def _parse_java_version(version_output: str) -> Dict[str, Any]:
    """
    Parse Java version output.
    
    Parameters
    ----------
    version_output : str
        Output from 'java -version' command
        
    Returns
    -------
    Dict[str, Any]
        Parsed version information
    """
    result = {
        'version': None,
        'version_string': None,
        'vendor': None
    }
    
    if not version_output:
        return result
    
    lines = version_output.strip().split('\n')
    if not lines:
        return result
    
    # First line usually contains version
    first_line = lines[0]
    result['version_string'] = first_line
    
    # Extract version number
    # Examples:
    # openjdk version "21.0.1" 2023-10-17
    # openjdk version "11.0.21" 2023-10-17 LTS
    
    import re
    
    # Try legacy format first (Java 8): "1.8.0_391"
    match = re.search(r'"1\.(\d+)\.', first_line)
    if match:
        result['version'] = int(match.group(1))
    else:
        # Try modern format (Java 9+): "21.0.1"
        match = re.search(r'"(\d+)\.(\d+)\.(\d+)', first_line)
        if match:
            major = int(match.group(1))
            result['version'] = major
    
    # Extract vendor information
    if 'openjdk' in first_line.lower():
        result['vendor'] = 'OpenJDK'
    elif 'oracle' in first_line.lower():
        result['vendor'] = 'Oracle'
    elif 'adoptopenjdk' in first_line.lower():
        result['vendor'] = 'AdoptOpenJDK'
    elif 'eclipse' in first_line.lower():
        result['vendor'] = 'Eclipse Temurin'
    
    return result


def ensure_java_available(required_version: int = REQUIRED_JAVA_VERSION, 
                         auto_install: bool = True) -> bool:
    """
    Ensure Java is available with required version.
    
    Parameters
    ----------
    required_version : int, default 21
        Required Java version
    auto_install : bool, default True
        Whether to automatically install Java if not available
        
    Returns
    -------
    bool
        True if Java is available with required version
    """
    logger.info(f"Checking Java availability (required version: {required_version})")
    
    # Check current installation
    java_info = check_java_installation()
    
    if java_info['available'] and java_info['version']:
        if java_info['version'] >= required_version:
            logger.info(f"✅ Java {java_info['version']} available ({java_info['vendor']})")
            return True
        elif java_info['version'] >= MIN_JAVA_VERSION:
            logger.warning(f"⚠️  Java {java_info['version']} available but {required_version} recommended")
            return True
        else:
            logger.warning(f"❌ Java {java_info['version']} too old (minimum: {MIN_JAVA_VERSION})")
    else:
        logger.warning("❌ Java not found")
    
    if not auto_install:
        return False
    
    # Try to install Java
    return install_openjdk(required_version)


def install_openjdk(version: int = REQUIRED_JAVA_VERSION) -> bool:
    """
    Install OpenJDK using install-jdk package.
    
    Parameters
    ----------
    version : int, default 21
        Java version to install
        
    Returns
    -------
    bool
        True if installation was successful
    """
    logger.info(f"Attempting to install OpenJDK {version}")
    
    try:
        # Import install-jdk (should be available from requirements.txt)
        import jdk
        
        print(f"📥 Installing OpenJDK {version}...")
        print("This may take a few minutes on first run.")
        
        # Install JDK
        java_home = jdk.install(version)
        
        if java_home and Path(java_home).exists():
            logger.info(f"✅ OpenJDK {version} installed at: {java_home}")
            
            # Set JAVA_HOME for current session
            os.environ['JAVA_HOME'] = java_home
            
            # Add to PATH
            java_bin = Path(java_home) / 'bin'
            if str(java_bin) not in os.environ.get('PATH', ''):
                os.environ['PATH'] = f"{java_bin}{os.pathsep}{os.environ.get('PATH', '')}"
            
            print(f"✅ OpenJDK {version} installed and configured!")
            print(f"JAVA_HOME: {java_home}")
            
            # Verify installation
            java_info = check_java_installation()
            if java_info['available'] and java_info['version'] >= version:
                return True
            else:
                logger.error("Installation verification failed")
                return False
        else:
            logger.error("Installation failed - no JAVA_HOME returned")
            return False
            
    except ImportError:
        logger.error("install-jdk package not available. Install with: pip install install-jdk")
        print("❌ Automatic Java installation not available.")
        print(f"Please install OpenJDK {version} manually")
        return False
        
    except Exception as e:
        logger.error(f"Failed to install OpenJDK: {e}")
        print(f"❌ Failed to install OpenJDK {version}: {e}")
        print(f"Please install OpenJDK {version} manually")
        return False


def print_java_status():
    """Print detailed Java installation status."""
    print("\n☕ Java Installation Status")
    print("=" * 30)
    
    java_info = check_java_installation()
    
    if java_info['available']:
        print(f"✅ Java available: {java_info['version_string']}")
        print(f"📍 Executable: {java_info['executable']}")
        
        if java_info['java_home']:
            print(f"🏠 JAVA_HOME: {java_info['java_home']}")
        else:
            print("🏠 JAVA_HOME: Not set")
        
        if java_info['vendor']:
            print(f"🏢 Vendor: {java_info['vendor']}")
        
        if java_info['version']:
            if java_info['version'] >= REQUIRED_JAVA_VERSION:
                print(f"✅ Version check: {java_info['version']} >= {REQUIRED_JAVA_VERSION} (recommended)")
            elif java_info['version'] >= MIN_JAVA_VERSION:
                print(f"⚠️  Version check: {java_info['version']} >= {MIN_JAVA_VERSION} (minimum, but {REQUIRED_JAVA_VERSION} recommended)")
            else:
                print(f"❌ Version check: {java_info['version']} < {MIN_JAVA_VERSION} (too old)")
    else:
        print("❌ Java not available. Call ensure_java_available()")


def setup_java_environment() -> bool:
    """
    Interactive Java environment setup.
    
    Returns
    -------
    bool
        True if Java is properly set up
    """
    print("☕ Java Environment Setup")
    print("=" * 25)
    
    # Check current status
    java_info = check_java_installation()
    
    if java_info['available'] and java_info['meets_requirements']:
        print("✅ Java is already properly configured!")
        print_java_status()
        return True
    
    if java_info['available']:
        print(f"⚠️  Java {java_info['version']} found but OpenJDK {REQUIRED_JAVA_VERSION} recommended")
    else:
        print("❌ Java not found")
    
    # Offer installation
    print(f"\nWould you like to install OpenJDK {REQUIRED_JAVA_VERSION}?")
    print("This will download and install OpenJDK automatically.")
    
    try:
        choice = input("Install OpenJDK? (Y/n): ").strip().lower()
        
        if choice in ['', 'y', 'yes']:
            success = install_openjdk(REQUIRED_JAVA_VERSION)
            if success:
                print("\n✅ Java setup complete!")
                print_java_status()
                return True
            else:
                print("\n❌ Automatic installation failed.")
                return False
        else:
            print("Skipping Java installation.")
            print("You can install Java manually or call ensure_java_available() later.")
            return java_info['meets_requirements']
            
    except KeyboardInterrupt:
        print("\nSetup cancelled.")
        return False


def inspect(class_or_object: Union[str, Any], 
           keyword: str = "", 
           methods: bool = True, 
           fields: bool = True,
           constructors: bool = False,
           static_only: bool = False,
           case_sensitive: bool = False,
           max_results: int = 50) -> None:
    """
    Inspect a Java class or object, listing methods and fields matching a keyword.
    
    This function uses scyjava's jreflect to introspect classes and display
    their public methods and fields. Useful for exploring SNT classes
    and discovering available functionality.
    
    Parameters
    ----------
    class_or_object : str or Java object
        Either a string class name (e.g., 'TreeStatistics') or a Java class/object
    keyword : str, default ""
        Filter results to only show items containing this keyword (case-insensitive by default)
    methods : bool, default True
        Whether to show methods
    fields : bool, default True
        Whether to show fields
    constructors : bool, default False
        Whether to show constructors
    static_only : bool, default False
        Whether to show only static members
    case_sensitive : bool, default False
        Whether keyword matching should be case-sensitive
    max_results : int, default 50
        Maximum number of results to display per category
        
    Examples
    --------
    >>> # Inspect TreeStatistics class
    >>> inspect('TreeStatistics')
    
    >>> # Look for methods containing 'length'
    >>> inspect('TreeStatistics', 'length', fields=False)
    
    >>> # Inspect an instance
    >>> from pysnt.analysis import TreeStatistics
    >>> stats = TreeStatistics()
    >>> inspect(stats, 'get')
    
    >>> # Show only static methods
    >>> inspect('TreeStatistics', static_only=True, fields=False)
    """
    
    try:
        import scyjava
        
        if not scyjava.jvm_started():
            print("❌ JVM not started. Call pysnt.initialize() first.")
            return
        
        # Resolve the Java class or object
        resolved_object = _resolve_java_object(class_or_object)
        if resolved_object is None:
            return
        
        # Get class information using scyjava.jreflect
        try:
            all_info = scyjava.jreflect(resolved_object, "all")
            class_name = _get_class_name(resolved_object)
            full_name = _get_full_class_name(resolved_object)
            package_name = _get_package_name(resolved_object)
        except Exception as e:
            print(f"❌ Error using jreflect: {e}")
            logger.debug(f"jreflect error details: {e}", exc_info=True)
            return
        
        # Display header
        print(f"\n🔍 Inspecting: {class_name}")
        if package_name:
            print(f"📦 Package: {package_name}")
        print(f"Full name: {full_name}")
        
        if keyword:
            keyword_display = f" matching '{keyword}'"
            if not case_sensitive:
                keyword_display += " (case-insensitive)"
        else:
            keyword_display = ""
        
        print(f"Showing: ", end="")
        shown = []
        if constructors:
            shown.append("constructors")
        if methods:
            shown.append("methods")
        if fields:
            shown.append("fields")
        print(", ".join(shown) + keyword_display)
        
        if static_only:
            print("Static members only")
        
        print("=" * 60)
        
        # Filter and show results using jreflect data
        if constructors:
            _show_constructors_from_jreflect(resolved_object, keyword, case_sensitive, max_results)
        
        if methods:
            _show_methods_from_jreflect(resolved_object, keyword, case_sensitive, static_only, max_results)
        
        if fields:
            _show_fields_from_jreflect(resolved_object, keyword, case_sensitive, static_only, max_results)
        
        print()
        
    except ImportError:
        print("❌ scyjava not available. Make sure pysnt is properly installed.")
    except Exception as e:
        print(f"❌ Error during inspection: {e}")
        logger.debug(f"Inspection error details: {e}", exc_info=True)


def _resolve_java_object(class_or_object: Union[str, Any]) -> Optional[Any]:
    """Resolve a class name or object to a Java object suitable for jreflect."""
    
    if isinstance(class_or_object, str):
        # String class name - try to resolve it
        class_name = class_or_object
        
        # Try to import from common pysnt modules
        modules_to_try = [
            'pysnt',  # Main module first
            'pysnt.analysis',
            'pysnt.analysis.graph', 
            'pysnt.analysis.growth',
            'pysnt.analysis.sholl',
            'pysnt.analysis.sholl.gui',
            'pysnt.analysis.sholl.math',
            'pysnt.analysis.sholl.parsers',
            'pysnt.tracing',
            'pysnt.viewer'
        ]
        
        for module_name in modules_to_try:
            try:
                module = __import__(module_name, fromlist=[class_name])
                java_class = getattr(module, class_name, None)
                if java_class is not None:
                    return java_class
            except:
                continue
        
        # Try direct jimport as fallback
        try:
            import scyjava
            return scyjava.jimport(class_name)
        except:
            pass
        
        print(f"❌ Could not find class '{class_name}' in common pysnt modules")
        print("Try using the actual Java class object instead")
        return None
    
    else:
        # Return the object as-is for jreflect to handle
        return class_or_object


def _get_class_name(java_object: Any) -> str:
    """Get simple class name from a Java object."""
    try:
        import scyjava
        # Try to get class info using jreflect
        info = scyjava.jreflect(java_object, "all")
        if info and len(info) > 0:
            # Look for class information in the reflection data
            for item in info:
                if 'name' in item and '.' in item['name']:
                    return item['name'].split('.')[-1]
        
        # Fallback to string representation
        class_str = str(type(java_object))
        if 'class ' in class_str:
            return class_str.split('class ')[-1].split('.')[-1].rstrip("'>")
        return str(java_object).split('.')[-1]
    except:
        return str(type(java_object).__name__)


def _get_full_class_name(java_object: Any) -> str:
    """Get full class name from a Java object."""
    try:
        import scyjava
        # Try to get class info using jreflect
        info = scyjava.jreflect(java_object, "all")
        if info and len(info) > 0:
            # Look for class information in the reflection data
            for item in info:
                if 'name' in item and '.' in item['name']:
                    return item['name']
        
        # Fallback to string representation
        return str(java_object)
    except:
        return str(java_object)


def _get_package_name(java_object: Any) -> str:
    """Get package name from a Java object."""
    try:
        full_name = _get_full_class_name(java_object)
        if '.' in full_name:
            return '.'.join(full_name.split('.')[:-1])
        return ""
    except:
        return ""


def _show_constructors_from_jreflect(java_object: Any, keyword: str, case_sensitive: bool, max_results: int):
    """Show constructors using scyjava.jreflect."""
    try:
        import scyjava
        constructors_info = scyjava.jreflect(java_object, "constructors")
        class_name = _get_class_name(java_object)
        
        matching_constructors = []
        for constructor in constructors_info:
            # Extract parameter types from arguments
            params = constructor.get('arguments', [])
            param_types = []
            for param in params:
                if isinstance(param, dict) and 'type' in param:
                    param_type = str(param['type'])
                    param_types.append(param_type.split('.')[-1])  # Simple name
                else:
                    param_type = str(param)
                    param_types.append(param_type.split('.')[-1])
            
            # Apply keyword filter to constructor signature if keyword is provided
            constructor_sig = f"{class_name}({', '.join(param_types)})"
            if not keyword or _matches_keyword(constructor_sig, keyword, case_sensitive):
                matching_constructors.append(param_types)
        
        if matching_constructors:
            print(f"\n🏗️  Constructors ({len(matching_constructors)}):")
            for i, params in enumerate(matching_constructors[:max_results]):
                params_str = ', '.join(params) if params else ''
                print(f"  {i+1}. {class_name}({params_str})")
            
            if len(matching_constructors) > max_results:
                print(f"  ... and {len(matching_constructors) - max_results} more")
        elif keyword:
            print(f"\n🏗️  Constructors: No matches for '{keyword}'")
        else:
            print(f"\n🏗️  Constructors: None found")
            
    except Exception as e:
        print(f"❌ Error getting constructors: {e}")


def _show_methods_from_jreflect(java_object: Any, keyword: str, case_sensitive: bool, static_only: bool, max_results: int):
    """Show methods using scyjava.jreflect."""
    try:
        import scyjava
        methods_info = scyjava.jreflect(java_object, "methods")
        
        matching_methods = []
        for method in methods_info:
            method_name = str(method.get('name', ''))
            
            # Skip Object methods
            if method_name in ['equals', 'hashCode', 'toString', 'getClass', 'notify', 'notifyAll', 'wait']:
                continue
            
            # Check keyword match
            if not _matches_keyword(method_name, keyword, case_sensitive):
                continue
            
            # Check static filter
            modifiers = method.get('mods', [])
            is_static = 'static' in modifiers
            
            if static_only and not is_static:
                continue
            
            # Extract parameter and return types
            params = method.get('arguments', [])
            param_types = []
            for param in params:
                if isinstance(param, dict) and 'type' in param:
                    param_type = str(param['type'])
                    param_types.append(param_type.split('.')[-1])  # Simple name
                else:
                    param_type = str(param)
                    param_types.append(param_type.split('.')[-1])
            
            return_type = method.get('returns', 'void')
            return_type = str(return_type)
            if '.' in return_type:
                return_type = return_type.split('.')[-1]  # Simple name
            
            matching_methods.append({
                'name': method_name,
                'params': param_types,
                'return_type': return_type,
                'is_static': is_static
            })
        
        if matching_methods:
            # Sort by name
            matching_methods.sort(key=lambda m: m['name'])
            
            static_suffix = " (static only)" if static_only else ""
            print(f"\n⚙️  Methods ({len(matching_methods)}){static_suffix}:")
            
            for i, method in enumerate(matching_methods[:max_results]):
                params_str = ', '.join(method['params']) if method['params'] else ''
                static_marker = "static " if method['is_static'] else ""
                print(f"  • {static_marker}{method['name']}({params_str}) -> {method['return_type']}")
            
            if len(matching_methods) > max_results:
                print(f"  ... and {len(matching_methods) - max_results} more")
        else:
            filter_desc = f"'{keyword}'" if keyword else "criteria"
            print(f"\n⚙️  Methods: No matches for {filter_desc}")
            
    except Exception as e:
        print(f"❌ Error getting methods: {e}")


def _show_fields_from_jreflect(java_object: Any, keyword: str, case_sensitive: bool, static_only: bool, max_results: int):
    """Show fields using scyjava.jreflect."""
    try:
        import scyjava
        fields_info = scyjava.jreflect(java_object, "fields")
        
        matching_fields = []
        for field in fields_info:
            field_name = str(field.get('name', ''))
            
            # Check keyword match
            if not _matches_keyword(field_name, keyword, case_sensitive):
                continue
            
            # Check static filter
            modifiers = field.get('mods', [])
            is_static = 'static' in modifiers
            is_final = 'final' in modifiers
            
            if static_only and not is_static:
                continue
            
            # Extract field type
            field_type = field.get('returns', 'Object')  # fields use 'returns' for type
            field_type = str(field_type)
            if '.' in field_type:
                field_type = field_type.split('.')[-1]  # Simple name
            
            matching_fields.append({
                'name': field_name,
                'type': field_type,
                'is_static': is_static,
                'is_final': is_final
            })
        
        if matching_fields:
            # Sort by name
            matching_fields.sort(key=lambda f: f['name'])
            
            static_suffix = " (static only)" if static_only else ""
            print(f"\n📊 Fields ({len(matching_fields)}){static_suffix}:")
            
            for i, field in enumerate(matching_fields[:max_results]):
                modifiers = []
                if field['is_static']:
                    modifiers.append('static')
                if field['is_final']:
                    modifiers.append('final')
                
                mod_str = ' '.join(modifiers)
                if mod_str:
                    mod_str += ' '
                
                print(f"  • {mod_str}{field['name']}: {field['type']}")
            
            if len(matching_fields) > max_results:
                print(f"  ... and {len(matching_fields) - max_results} more")
        else:
            filter_desc = f"'{keyword}'" if keyword else "criteria"
            print(f"\n📊 Fields: No matches for {filter_desc}")
            
    except Exception as e:
        print(f"❌ Error getting fields: {e}")


def _matches_keyword(name: str, keyword: str, case_sensitive: bool) -> bool:
    """Check if a name matches the keyword filter."""
    if not keyword:
        return True
    
    # Ensure name is a string (convert Java strings if needed)
    name_str = str(name)
    
    if case_sensitive:
        return keyword in name_str
    else:
        return keyword.lower() in name_str.lower()


def get_methods(class_or_object: Union[str, Any], static_only: bool = False, include_inherited: bool = True) -> list:
    """
    Retrieve all public methods from a Java class or object using scyjava.jreflect.
    
    Parameters
    ----------
    class_or_object : str or Java object
        Either a string class name or a Java class/object
    static_only : bool, default False
        Whether to return only static methods
    include_inherited : bool, default True
        Whether to include inherited methods (from Object class excluded)
        
    Returns
    -------
    list
        List of dictionaries containing method information:
        - 'name': method name
        - 'params': list of parameter type names
        - 'return_type': return type name
        - 'is_static': whether method is static
        - 'signature': full method signature string
        
    Examples
    --------
    >>> methods = get_methods('TreeStatistics')
    >>> for method in methods:
    ...     print(f"{method['name']}({', '.join(method['params'])}) -> {method['return_type']}")
    """
    try:
        import scyjava
        
        if not scyjava.jvm_started():
            logger.warning("JVM not started. Call pysnt.initialize() first.")
            return []
        
        java_object = _resolve_java_object(class_or_object)
        if java_object is None:
            return []
        
        # Use scyjava.jreflect to get method information
        try:
            methods_info = scyjava.jreflect(java_object, "methods")
        except Exception as e:
            logger.error(f"Failed to get methods using jreflect: {e}")
            return []
        
        result = []
        
        for method in methods_info:
            try:
                method_name = str(method.get('name', ''))
                
                # Skip Object methods unless explicitly requested
                if not include_inherited and method_name in [
                    'equals', 'hashCode', 'toString', 'getClass', 
                    'notify', 'notifyAll', 'wait'
                ]:
                    continue
                
                # Check static filter
                modifiers = method.get('mods', [])
                is_static = 'static' in modifiers
                
                if static_only and not is_static:
                    continue
                
                # Extract parameter types
                params = method.get('arguments', [])
                param_types = []
                for param in params:
                    if isinstance(param, dict) and 'type' in param:
                        param_type = str(param['type'])
                        param_types.append(param_type.split('.')[-1])  # Simple name
                    else:
                        param_type = str(param)
                        param_types.append(param_type.split('.')[-1])
                
                # Extract return type
                return_type = method.get('returns', 'void')
                return_type = str(return_type)
                if '.' in return_type:
                    return_type = return_type.split('.')[-1]  # Simple name
                
                # Create signature
                params_str = ', '.join(param_types) if param_types else ''
                static_prefix = 'static ' if is_static else ''
                signature = f"{static_prefix}{method_name}({params_str}) -> {return_type}"
                
                result.append({
                    'name': method_name,
                    'params': param_types,
                    'return_type': return_type,
                    'is_static': is_static,
                    'signature': signature
                })
                
            except Exception as e:
                logger.debug(f"Error processing method {method}: {e}")
                continue
        
        # Sort by name for consistent output
        result.sort(key=lambda m: m['name'])
        return result
        
    except ImportError:
        logger.error("scyjava not available. Make sure pysnt is properly installed.")
        return []
    except Exception as e:
        logger.error(f"Error getting methods: {e}")
        return []


def get_fields(class_or_object: Union[str, Any], static_only: bool = False) -> list:
    """
    Retrieve all public fields from a Java class or object using scyjava.jreflect.
    
    Parameters
    ----------
    class_or_object : str or Java object
        Either a string class name or a Java class/object
    static_only : bool, default False
        Whether to return only static fields
        
    Returns
    -------
    list
        List of dictionaries containing field information:
        - 'name': field name
        - 'type': field type name
        - 'is_static': whether field is static
        - 'is_final': whether field is final
        - 'signature': full field signature string
        
    Examples
    --------
    >>> fields = get_fields('TreeStatistics')
    >>> for field in fields:
    ...     print(f"{field['name']}: {field['type']}")
    """
    try:
        import scyjava
        
        if not scyjava.jvm_started():
            logger.warning("JVM not started. Call pysnt.initialize() first.")
            return []
        
        java_object = _resolve_java_object(class_or_object)
        if java_object is None:
            return []
        
        # Use scyjava.jreflect to get field information
        try:
            fields_info = scyjava.jreflect(java_object, "fields")
        except Exception as e:
            logger.error(f"Failed to get fields using jreflect: {e}")
            return []
        
        result = []
        
        for field in fields_info:
            try:
                field_name = str(field.get('name', ''))
                
                # Check static filter
                modifiers = field.get('mods', [])
                is_static = 'static' in modifiers
                is_final = 'final' in modifiers
                
                if static_only and not is_static:
                    continue
                
                # Extract field type
                field_type = field.get('returns', 'Object')  # fields use 'returns' for type
                field_type = str(field_type)
                if '.' in field_type:
                    field_type = field_type.split('.')[-1]  # Simple name
                
                # Create signature
                modifiers_list = []
                if is_static:
                    modifiers_list.append('static')
                if is_final:
                    modifiers_list.append('final')
                
                mod_str = ' '.join(modifiers_list)
                if mod_str:
                    mod_str += ' '
                
                signature = f"{mod_str}{field_name}: {field_type}"
                
                result.append({
                    'name': field_name,
                    'type': field_type,
                    'is_static': is_static,
                    'is_final': is_final,
                    'signature': signature
                })
                
            except Exception as e:
                logger.debug(f"Error processing field {field}: {e}")
                continue
        
        # Sort by name for consistent output
        result.sort(key=lambda f: f['name'])
        return result
        
    except ImportError:
        logger.error("scyjava not available. Make sure pysnt is properly installed.")
        return []
    except Exception as e:
        logger.error(f"Error getting fields: {e}")
        return []


def get_inner_classes(class_or_object: Union[str, Any]) -> list:
    """
    Retrieve all public inner classes from a Java class.
    
    Note: This function uses traditional Java reflection as scyjava.jreflect 
    doesn't currently provide inner class information.
    
    Parameters
    ----------
    class_or_object : str or Java object
        Either a string class name or a Java class/object
        
    Returns
    -------
    list
        List of dictionaries containing inner class information:
        - 'name': simple class name
        - 'full_name': full qualified class name
        - 'is_static': whether the inner class is static
        - 'is_interface': whether it's an interface
        - 'is_enum': whether it's an enum
        - 'signature': descriptive signature string
        
    Examples
    --------
    >>> inner_classes = get_inner_classes('CircularModels')
    >>> for cls in inner_classes:
    ...     print(f"{cls['name']}: {cls['full_name']}")
    """
    try:
        import scyjava
        
        if not scyjava.jvm_started():
            logger.warning("JVM not started. Call pysnt.initialize() first.")
            return []
        
        java_object = _resolve_java_object(class_or_object)
        if java_object is None:
            return []
        
        # Get the Java Class object for reflection
        # Since jreflect doesn't provide inner classes, we use traditional reflection
        try:
            if hasattr(java_object, 'getClass'):
                java_class = java_object.getClass()
            elif hasattr(java_object, 'class_'):
                java_class = java_object.class_
            else:
                java_class = java_object
            
            # Get declared classes (inner classes)
            inner_classes = java_class.getDeclaredClasses()
        except Exception as e:
            logger.debug(f"Could not get inner classes using traditional reflection: {e}")
            return []
        
        result = []
        
        for inner_class in inner_classes:
            try:
                class_name = str(inner_class.getSimpleName())
                full_name = str(inner_class.getName())
                
                # Get modifiers
                modifiers = inner_class.getModifiers()
                is_static = bool(modifiers & 0x0008)  # Modifier.STATIC
                is_interface = inner_class.isInterface()
                is_enum = inner_class.isEnum()
                
                # Create signature
                modifiers_list = []
                if is_static:
                    modifiers_list.append('static')
                
                if is_interface:
                    type_str = 'interface'
                elif is_enum:
                    type_str = 'enum'
                else:
                    type_str = 'class'
                
                mod_str = ' '.join(modifiers_list)
                if mod_str:
                    mod_str += ' '
                
                signature = f"{mod_str}{type_str} {class_name}"
                
                result.append({
                    'name': class_name,
                    'full_name': full_name,
                    'is_static': is_static,
                    'is_interface': is_interface,
                    'is_enum': is_enum,
                    'signature': signature
                })
                
            except Exception as e:
                logger.debug(f"Error processing inner class {inner_class}: {e}")
                continue
        
        # Sort by name for consistent output
        result.sort(key=lambda c: c['name'])
        return result
        
    except ImportError:
        logger.error("scyjava not available. Make sure pysnt is properly installed.")
        return []
    except Exception as e:
        logger.error(f"Error getting inner classes: {e}")
        return []


def is_instance_of(obj: Any, jtype: Union[str, Any]) -> bool:
    """
    Test if the given object is an instance of a particular Java type using scyjava.jinstance.
    
    This is a wrapper around scyjava's jinstance function that provides better error handling
    and logging for the PySNT context.
    
    Parameters
    ----------
    obj : Any
        The object to check
    jtype : str or Java class
        The Java type, as either a jimported class or as a string
        
    Returns
    -------
    bool
        True if the object is an instance of that Java type, False otherwise
        
    Examples
    --------
    >>> from pysnt.analysis import TreeStatistics
    >>> stats = TreeStatistics()
    >>> is_instance_of(stats, 'sc.fiji.snt.analysis.TreeStatistics')
    True
    
    >>> # Using jimported class
    >>> TreeStats = scyjava.jimport('sc.fiji.snt.analysis.TreeStatistics')
    >>> is_instance_of(stats, TreeStats)
    True
    """
    try:
        import scyjava
        
        if not scyjava.jvm_started():
            logger.warning("JVM not started. Call pysnt.initialize() first.")
            return False
        
        return scyjava.jinstance(obj, jtype)
        
    except ImportError:
        logger.error("scyjava not available. Make sure pysnt is properly installed.")
        return False
    except Exception as e:
        logger.debug(f"Error checking instance type: {e}")
        return False


def reflect_java_object(data: Any, aspect: str = "all") -> List[Dict[str, Any]]:
    """
    Use Java reflection to introspect the given Java object using scyjava.jreflect.
    
    This is a wrapper around scyjava's jreflect function that provides better error handling
    and logging for the PySNT context.
    
    Parameters
    ----------
    data : Any
        The object or class or fully qualified class name to inspect
    aspect : str, default "all"
        One of: "all", "constructors", "fields", or "methods"
        
    Returns
    -------
    List[Dict[str, Any]]
        List of dicts with keys: "name", "mods", "arguments", and "returns"
        
    Examples
    --------
    >>> from pysnt.analysis import TreeStatistics
    >>> methods = reflect_java_object(TreeStatistics, "methods")
    >>> for method in methods:
    ...     print(f"{method['name']}: {method.get('returns', 'void')}")
    
    >>> # Get all reflection info
    >>> all_info = reflect_java_object('sc.fiji.snt.analysis.TreeStatistics')
    """
    try:
        import scyjava
        
        if not scyjava.jvm_started():
            logger.warning("JVM not started. Call pysnt.initialize() first.")
            return []
        
        return scyjava.jreflect(data, aspect)
        
    except ImportError:
        logger.error("scyjava not available. Make sure pysnt is properly installed.")
        return []
    except Exception as e:
        logger.error(f"Error during reflection: {e}")
        return []


def find_members(class_or_object: Union[str, Any], 
                keyword: str,
                include_methods: bool = True,
                include_fields: bool = True,
                include_inner_classes: bool = True,
                static_only: bool = False,
                case_sensitive: bool = False) -> Dict[str, list]:
    """
    Find methods, fields, and inner classes matching a keyword in a Java class or object.
    
    This function now uses scyjava.jreflect for improved performance and consistency.
    
    Parameters
    ----------
    class_or_object : str or Java object
        Either a string class name or a Java class/object
    keyword : str
        Keyword to search for in method, field, and inner class names
    include_methods : bool, default True
        Whether to search methods
    include_fields : bool, default True
        Whether to search fields
    include_inner_classes : bool, default True
        Whether to search inner classes
    static_only : bool, default False
        Whether to search only static members
    case_sensitive : bool, default False
        Whether keyword matching should be case-sensitive
        
    Returns
    -------
    Dict[str, list]
        Dictionary with 'methods', 'fields', and 'inner_classes' keys containing matching members.
        Each member is a dictionary with detailed information.
        
    Examples
    --------
    >>> # Find all members containing 'length'
    >>> results = find_members('TreeStatistics', 'length')
    >>> print(f"Found {len(results['methods'])} methods and {len(results['fields'])} fields")
    
    >>> # Find inner classes containing 'Fit'
    >>> results = find_members('CircularModels', 'Fit')
    >>> print(f"Found {len(results['inner_classes'])} inner classes")
    
    >>> # Find only static methods containing 'get'
    >>> results = find_members('TreeStatistics', 'get', 
    ...                       include_fields=False, static_only=True)
    """
    result = {'methods': [], 'fields': [], 'inner_classes': []}
    
    if not keyword:
        logger.debug("No keyword provided for search - will return all members")
        # Don't return early - let it proceed to get all members
    
    try:
        # Get methods if requested - now using jreflect-based implementation
        if include_methods:
            all_methods = get_methods(class_or_object, static_only=static_only)
            for method in all_methods:
                if _matches_keyword(method['name'], keyword, case_sensitive):
                    result['methods'].append(method)
        
        # Get fields if requested - now using jreflect-based implementation
        if include_fields:
            all_fields = get_fields(class_or_object, static_only=static_only)
            for field in all_fields:
                if _matches_keyword(field['name'], keyword, case_sensitive):
                    result['fields'].append(field)
        
        # Get inner classes if requested - still uses traditional reflection
        # as jreflect doesn't provide inner class information
        if include_inner_classes:
            inner_classes = get_inner_classes(class_or_object)
            for inner_class in inner_classes:
                if _matches_keyword(inner_class['name'], keyword, case_sensitive):
                    result['inner_classes'].append(inner_class)
        
        return result
        
    except Exception as e:
        logger.error(f"Error finding members: {e}")
        return result


def discover_java_classes(
    package_name: str, 
    known_classes: Optional[List[str]] = None,
    include_abstract: bool = False,
    include_interfaces: bool = False
) -> List[str]:
    """
    Discover all public classes in a Java package.
    
    This utility function dynamically discovers classes from Java packages using
    a multi-step approach:
    
    1. First attempts JAR file scanning for .class files
    2. If no known_classes provided, scans pysnt module __init__.py files for 
       CURATED_CLASSES and EXTENDED_CLASSES lists
    3. Tests each candidate class for existence and visibility
    
    The dynamic scanning approach finds significantly more classes than hardcoded
    lists and automatically stays up-to-date with module definitions.
    
    Parameters
    ----------
    package_name : str
        Full Java package name (e.g., 'sc.fiji.snt.analysis')
    known_classes : List[str], optional
        List of known class names to test. If None, scans pysnt modules dynamically.
    include_abstract : bool, default False
        Whether to include abstract classes
    include_interfaces : bool, default False
        Whether to include interfaces
        
    Returns
    -------
    List[str]
        List of discovered public class names
        
    Examples
    --------
    >>> # Discover analysis classes (scans pysnt.analysis modules)
    >>> classes = discover_java_classes('sc.fiji.snt.analysis')
    >>> 
    >>> # Discover with explicit class list
    >>> known = ['TreeStatistics', 'ConvexHull']
    >>> classes = discover_java_classes('sc.fiji.snt.analysis', known)
    
    Notes
    -----
    The dynamic scanning finds classes from:
    - CURATED_CLASSES lists in matching pysnt modules
    - EXTENDED_CLASSES lists in matching pysnt modules  
    - All submodules of the matching package
    
    For 'sc.fiji.snt.analysis', this scans:
    - src/pysnt/analysis/__init__.py
    - src/pysnt/analysis/graph/__init__.py
    - src/pysnt/analysis/sholl/__init__.py
    - And other analysis submodules
    """
    if scyjava is None:
        logger.warning("ScyJava not available. Cannot discover classes.")
        return []
        
    if not scyjava.jvm_started():
        logger.warning("JVM not started. Cannot discover classes.")
        return []
    
    try:
        # Import Java reflection classes
        Class = scyjava.jimport("java.lang.Class")
        Modifier = scyjava.jimport("java.lang.reflect.Modifier")
        
        classes = []
        
        # Method 1: Advanced package scanning from JAR files
        if known_classes is None:
            try:
                classes = _scan_package_from_jars(package_name, logger)
            except Exception as e:
                logger.debug(f"JAR scanning failed: {e}")
        
        # Method 2: Use provided known classes or scan pysnt modules
        if not classes and known_classes:
            test_classes = known_classes
        elif not classes:
            # Scan pysnt modules for CURATED_CLASSES and EXTENDED_CLASSES
            test_classes = _scan_pysnt_modules_for_classes(package_name)
        else:
            test_classes = []
        
        # Test each class for existence and visibility
        for class_name in test_classes:
            try:
                full_class_name = f"{package_name}.{class_name}"
                java_class = Class.forName(full_class_name)
                
                # Check class modifiers
                modifiers = java_class.getModifiers()
                
                # Filter based on visibility and type
                if not Modifier.isPublic(modifiers):
                    logger.debug(f"Skipping non-public class: {class_name}")
                    continue
                    
                if Modifier.isAbstract(modifiers) and not include_abstract:
                    logger.debug(f"Skipping abstract class: {class_name}")
                    continue
                    
                if Modifier.isInterface(modifiers) and not include_interfaces:
                    logger.debug(f"Skipping interface: {class_name}")
                    continue

                # Inner classes will also be included
                # The public modifier check above will filter out private inner classes

                classes.append(class_name)
                logger.debug(f"Found public class: {class_name}")
                
            except Exception as e:
                logger.debug(f"Class not found or not accessible: {class_name} - {e}")
                continue
        
        # Remove duplicates and sort
        classes = sorted(list(set(classes)))
        logger.info(f"Discovered {len(classes)} public classes in {package_name}")
        return classes
        
    except Exception as e:
        logger.error(f"Failed to discover classes in {package_name}: {e}")
        return []


def _scan_package_from_jars(package_name: str, logger) -> List[str]:
    """
    Scan JAR files in classpath for classes in the specified package.
    
    Parameters
    ----------
    package_name : str
        Java package name (e.g., 'sc.fiji.snt.analysis')
    logger : Logger
        Logger instance for debug messages
        
    Returns
    -------
    List[str]
        List of class names found in JAR files
    """
    classes = []
    package_path = package_name.replace('.', '/')
    
    # Get classpath
    classpath = os.environ.get('CLASSPATH', '')
    
    # Look for relevant JAR files
    potential_jars = []
    if classpath:
        for path in classpath.split(os.pathsep):
            if any(keyword in path.lower() for keyword in ['snt']): # snt jar only for now
                potential_jars.append(path)
    
    # Scan JAR files
    for jar_path in potential_jars:
        if os.path.exists(jar_path) and jar_path.endswith('.jar'):
            try:
                with zipfile.ZipFile(jar_path, 'r') as jar:
                    for entry in jar.namelist():
                        if (entry.startswith(f'{package_path}/') and 
                            entry.endswith('.class')):
                            
                            # Extract class name
                            relative_path = entry[len(f'{package_path}/'):]
                            if '/' not in relative_path:  # Top-level class only
                                class_name = relative_path[:-6]  # Remove .class
                                # Include inner classes - public/private filtering happens later
                                classes.append(class_name)
                                logger.debug(f"Found class in JAR: {class_name}")
                                    
            except Exception as e:
                logger.debug(f"Could not scan JAR {jar_path}: {e}")
    
    return classes


def _scan_pysnt_modules_for_classes(package_name: str) -> List[str]:
    """
    Scan pysnt module __init__.py files to collect CURATED_CLASSES and EXTENDED_CLASSES
    that match the given Java package name.
    
    This dynamically discovers class names from the actual module definitions
    instead of using hardcoded lists.
    
    Parameters
    ----------
    package_name : str
        Java package name (e.g., 'sc.fiji.snt.analysis')
        
    Returns
    -------
    List[str]
        List of class names found in matching pysnt modules
    """
    import os
    import importlib.util
    from pathlib import Path
    
    # Get the pysnt source directory
    pysnt_dir = Path(__file__).parent
    
    # Map Java package names to pysnt module paths
    package_mappings = {
        'sc.fiji.snt.analysis': ['analysis'],
        'sc.fiji.snt.analysis.graph': ['analysis/graph'],
        'sc.fiji.snt.analysis.growth': ['analysis/growth'],  
        'sc.fiji.snt.analysis.sholl': ['analysis/sholl'],
        'sc.fiji.snt.analysis.sholl.gui': ['analysis/sholl/gui'],
        'sc.fiji.snt.analysis.sholl.math': ['analysis/sholl/math'],
        'sc.fiji.snt.analysis.sholl.parsers': ['analysis/sholl/parsers'],
        'sc.fiji.snt.util': ['util'],
        'sc.fiji.snt.viewer': ['viewer'],
        'sc.fiji.snt.tracing': ['tracing'],
        'sc.fiji.snt.tracing.artist': ['tracing/artist'],
        'sc.fiji.snt.tracing.cost': ['tracing/cost'],
        'sc.fiji.snt.tracing.heuristic': ['tracing/heuristic'],
        'sc.fiji.snt.tracing.image': ['tracing/image'],
        'sc.fiji.snt.io': ['io'],
        'sc.fiji.snt': [''],  # Main package
    }
    
    # Get module paths to scan for this package
    module_paths = package_mappings.get(package_name, [])
    
    # If no direct mapping, try to infer from package name
    if not module_paths:
        # Extract the last part of the package name
        parts = package_name.split('.')
        if len(parts) >= 3 and parts[0] == 'sc' and parts[1] == 'fiji' and parts[2] == 'snt':
            # Build path from remaining parts
            if len(parts) > 3:
                module_path = '/'.join(parts[3:])
                module_paths = [module_path]
    
    collected_classes = []
    
    # Scan each relevant module path
    for module_path in module_paths:
        init_file = pysnt_dir / module_path / '__init__.py' if module_path else pysnt_dir / '__init__.py'
        
        if init_file.exists():
            try:
                # Read and parse the __init__.py file
                with open(init_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract CURATED_CLASSES and EXTENDED_CLASSES using simple parsing
                classes = _extract_class_lists_from_content(content)
                collected_classes.extend(classes)
                
                logger.debug(f"Found {len(classes)} classes in {init_file}")
                
            except Exception as e:
                logger.debug(f"Error reading {init_file}: {e}")
                continue
    
    # Also scan all subdirectories for additional classes
    if module_paths:
        for module_path in module_paths:
            base_dir = pysnt_dir / module_path if module_path else pysnt_dir
            if base_dir.is_dir():
                for subdir in base_dir.iterdir():
                    if subdir.is_dir() and (subdir / '__init__.py').exists():
                        try:
                            with open(subdir / '__init__.py', 'r', encoding='utf-8') as f:
                                content = f.read()
                            
                            classes = _extract_class_lists_from_content(content)
                            collected_classes.extend(classes)
                            
                            logger.debug(f"Found {len(classes)} classes in {subdir / '__init__.py'}")
                            
                        except Exception as e:
                            logger.debug(f"Error reading {subdir / '__init__.py'}: {e}")
                            continue
    
    # Remove duplicates and return
    unique_classes = list(set(collected_classes))
    logger.debug(f"Total unique classes found for {package_name}: {len(unique_classes)}")
    
    return unique_classes


def _extract_class_lists_from_content(content: str) -> List[str]:
    """
    Extract CURATED_CLASSES and EXTENDED_CLASSES from Python file content.
    
    Uses simple string parsing to avoid importing modules.
    
    Parameters
    ----------
    content : str
        Content of the Python file
        
    Returns
    -------
    List[str]
        List of class names found
    """
    import re
    
    classes = []
    
    # Pattern to match CURATED_CLASSES = [...]
    curated_pattern = r'CURATED_CLASSES\s*=\s*\[(.*?)\]'
    extended_pattern = r'EXTENDED_CLASSES\s*=\s*\[(.*?)\]'
    
    # Find CURATED_CLASSES
    curated_match = re.search(curated_pattern, content, re.DOTALL)
    if curated_match:
        curated_content = curated_match.group(1)
        # Extract quoted strings
        class_names = re.findall(r'["\']([^"\']+)["\']', curated_content)
        classes.extend(class_names)
    
    # Find EXTENDED_CLASSES  
    extended_match = re.search(extended_pattern, content, re.DOTALL)
    if extended_match:
        extended_content = extended_match.group(1)
        # Extract quoted strings
        class_names = re.findall(r'["\']([^"\']+)["\']', extended_content)
        classes.extend(class_names)
    
    return classes


# Java Logging Control Functions

def configure_java_logging() -> bool:
    """
    Configure Java-side logging based on current PySNT configuration options.
    
    This function reads the current configuration settings and applies them
    to various Java logging frameworks to control verbosity.
    
    The configuration is controlled via pysnt.set_option():
    - 'java.logging.level': Logging level (OFF, ERROR, WARN, INFO, DEBUG, TRACE)
    - 'java.logging.jpype.silence': Whether to silence JPype logging
    - 'java.logging.log4j.silence': Whether to silence Log4j logging
    - 'java.logging.slf4j.silence': Whether to silence SLF4J logging
    - 'java.logging.jul.silence': Whether to silence java.util.logging
        
    Returns
    -------
    bool
        True if configuration was successful, False otherwise
        
    Examples
    --------
    >>> # Configure logging via options
    >>> pysnt.set_option('java.logging.level', 'ERROR')
    >>> pysnt.set_option('java.logging.jpype.silence', True)
    >>> pysnt.configure_java_logging()
    >>> 
    >>> # Set to INFO level for debugging
    >>> pysnt.set_option('java.logging.level', 'INFO')
    >>> pysnt.configure_java_logging()
    >>> 
    >>> # Only silence JPype, keep other logging
    >>> pysnt.set_option('java.logging.jpype.silence', True)
    >>> pysnt.set_option('java.logging.log4j.silence', False)
    >>> pysnt.set_option('java.logging.slf4j.silence', False)
    >>> pysnt.configure_java_logging()
    """
    success = True
    
    try:
        # Import config functions
        from .config import get_option
        
        # Read configuration options
        level = get_option('java.logging.level')
        silence_jpype = get_option('java.logging.jpype.silence')
        silence_log4j = get_option('java.logging.log4j.silence')
        silence_slf4j = get_option('java.logging.slf4j.silence')
        silence_java_util_logging = get_option('java.logging.jul.silence')
        
        # 1. Configure JPype logging (Python side)
        if silence_jpype and jpype is not None:
            try:
                import logging
                jpype_logger = logging.getLogger('jpype')
                if level == "OFF":
                    jpype_logger.setLevel(logging.CRITICAL + 1)  # Effectively OFF
                elif level == "ERROR":
                    jpype_logger.setLevel(logging.ERROR)
                elif level == "WARN":
                    jpype_logger.setLevel(logging.WARNING)
                elif level == "INFO":
                    jpype_logger.setLevel(logging.INFO)
                elif level == "DEBUG":
                    jpype_logger.setLevel(logging.DEBUG)
                
                logger.debug(f"Configured JPype logging to {level}")
            except Exception as e:
                logger.warning(f"Failed to configure JPype logging: {e}")
                success = False
        
        # 2. Configure Java-side logging (requires JVM to be started)
        if scyjava is not None and scyjava.jvm_started():
            try:
                # Configure Log4j if available
                if silence_log4j:
                    success &= _configure_log4j_logging(level)
                
                # Configure SLF4J if available  
                if silence_slf4j:
                    success &= _configure_slf4j_logging(level)
                
                # Configure java.util.logging
                if silence_java_util_logging:
                    success &= _configure_jul_logging(level)
                    
            except Exception as e:
                logger.warning(f"Failed to configure Java logging: {e}")
                success = False
        else:
            logger.debug("JVM not started - Java logging configuration will be applied when JVM starts")
    
    except Exception as e:
        logger.error(f"Error configuring Java logging: {e}")
        success = False
    
    return success


def _configure_log4j_logging(level: str) -> bool:
    """Configure Log4j logging if available."""
    try:
        # Try Log4j 2.x first
        try:
            LogManager = scyjava.jimport('org.apache.logging.log4j.LogManager')
            Level = scyjava.jimport('org.apache.logging.log4j.Level')
            Configurator = scyjava.jimport('org.apache.logging.log4j.core.config.Configurator')
            
            # Map our levels to Log4j levels
            level_map = {
                "OFF": Level.OFF,
                "ERROR": Level.ERROR, 
                "WARN": Level.WARN,
                "INFO": Level.INFO,
                "DEBUG": Level.DEBUG,
                "TRACE": Level.TRACE
            }
            
            log4j_level = level_map.get(level, Level.ERROR)
            
            # Set root logger level
            Configurator.setRootLevel(log4j_level)
            
            # Also set specific loggers that tend to be verbose
            verbose_loggers = [
                "org.scijava",
                "net.imagej", 
                "org.apache.commons",
                "com.github.haifengl",
            ]
            
            for logger_name in verbose_loggers:
                try:
                    Configurator.setLevel(logger_name, log4j_level)
                except:
                    pass  # Logger might not exist
            
            logger.debug(f"Configured Log4j 2.x logging to {level}")
            return True
            
        except ImportError:
            # Try Log4j 1.x
            try:
                Logger = scyjava.jimport('org.apache.log4j.Logger')
                Level = scyjava.jimport('org.apache.log4j.Level')
                
                level_map = {
                    "OFF": Level.OFF,
                    "ERROR": Level.ERROR,
                    "WARN": Level.WARN, 
                    "INFO": Level.INFO,
                    "DEBUG": Level.DEBUG
                }
                
                log4j_level = level_map.get(level, Level.ERROR)
                
                # Set root logger
                root_logger = Logger.getRootLogger()
                root_logger.setLevel(log4j_level)
                
                logger.debug(f"Configured Log4j 1.x logging to {level}")
                return True
                
            except ImportError:
                logger.debug("Log4j not available")
                return True  # Not an error if Log4j isn't present
                
    except Exception as e:
        logger.warning(f"Failed to configure Log4j: {e}")
        return False


def _configure_slf4j_logging(level: str) -> bool:
    """Configure SLF4J logging if available."""
    try:
        # Try to configure SLF4J
        try:
            LoggerFactory = scyjava.jimport('org.slf4j.LoggerFactory')
            
            # Try to get Logback configuration (common SLF4J implementation)
            try:
                LoggerContext = scyjava.jimport('ch.qos.logback.classic.LoggerContext')
                Level = scyjava.jimport('ch.qos.logback.classic.Level')
                
                level_map = {
                    "OFF": Level.OFF,
                    "ERROR": Level.ERROR,
                    "WARN": Level.WARN,
                    "INFO": Level.INFO, 
                    "DEBUG": Level.DEBUG,
                    "TRACE": Level.TRACE
                }
                
                logback_level = level_map.get(level, Level.ERROR)
                
                # Get logger context and set root level
                context = LoggerFactory.getILoggerFactory()
                if hasattr(context, 'getLogger'):
                    root_logger = context.getLogger('ROOT')
                    if hasattr(root_logger, 'setLevel'):
                        root_logger.setLevel(logback_level)
                        
                        # Set specific verbose loggers
                        verbose_loggers = [
                            "org.scijava",
                            "net.imagej",
                            "com.github.haifengl",
                            "org.apache.commons"
                        ]
                        
                        for logger_name in verbose_loggers:
                            try:
                                specific_logger = context.getLogger(logger_name)
                                specific_logger.setLevel(logback_level)
                            except:
                                pass
                
                logger.debug(f"Configured SLF4J/Logback logging to {level}")
                return True
                
            except ImportError:
                logger.debug("Logback not available for SLF4J configuration")
                return True
                
        except ImportError:
            logger.debug("SLF4J not available")
            return True
            
    except Exception as e:
        logger.warning(f"Failed to configure SLF4J: {e}")
        return False


def _configure_jul_logging(level: str) -> bool:
    """Configure java.util.logging."""
    try:
        Logger = scyjava.jimport('java.util.logging.Logger')
        Level = scyjava.jimport('java.util.logging.Level')
        
        level_map = {
            "OFF": Level.OFF,
            "ERROR": Level.SEVERE,
            "WARN": Level.WARNING,
            "INFO": Level.INFO,
            "DEBUG": Level.FINE,
            "TRACE": Level.FINEST
        }
        
        jul_level = level_map.get(level, Level.SEVERE)
        
        # Set root logger
        root_logger = Logger.getLogger("")
        root_logger.setLevel(jul_level)
        
        # Set specific verbose loggers
        verbose_loggers = [
            "org.scijava",
            "net.imagej",
            "com.github.haifengl",
        ]
        
        for logger_name in verbose_loggers:
            try:
                specific_logger = Logger.getLogger(logger_name)
                specific_logger.setLevel(jul_level)
            except:
                pass
        
        logger.debug(f"Configured java.util.logging to {level}")
        return True
        
    except Exception as e:
        logger.warning(f"Failed to configure java.util.logging: {e}")
        return False

if __name__ == "__main__":
    # Run Java setup if called directly
    setup_java_environment()