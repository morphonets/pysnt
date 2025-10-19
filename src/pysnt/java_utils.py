"""
Java utilities for PySNT.

This module handles Java/OpenJDK installation and configuration,
as well as Java class introspection utilities.
"""

import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, Dict, Any, Union

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
    # java version "1.8.0_391"
    # openjdk version "11.0.21" 2023-10-17 LTS
    
    import re
    
    # Try modern format (Java 9+): "21.0.1"
    match = re.search(r'"(\d+)\.(\d+)\.(\d+)', first_line)
    if match:
        major = int(match.group(1))
        result['version'] = major
    else:
        # Try legacy format (Java 8): "1.8.0_391"
        match = re.search(r'"1\.(\d+)\.', first_line)
        if match:
            result['version'] = int(match.group(1))
    
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
    
    This function uses Java reflection to introspect classes and display
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
        
        # Get the Java class
        java_class = _resolve_java_class(class_or_object)
        if java_class is None:
            return
        
        # Display header
        class_name = str(java_class.getSimpleName())
        full_name = str(java_class.getName())
        
        print(f"\n🔍 Inspecting: {class_name}")
        print(f"📦 Package: {java_class.getPackage().getName()}")
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
        
        # Show constructors
        if constructors:
            _show_constructors(java_class, keyword, case_sensitive, max_results)
        
        # Show methods
        if methods:
            _show_methods(java_class, keyword, case_sensitive, static_only, max_results)
        
        # Show fields
        if fields:
            _show_fields(java_class, keyword, case_sensitive, static_only, max_results)
        
        print()
        
    except ImportError:
        print("❌ scyjava not available. Make sure pysnt is properly installed.")
    except Exception as e:
        print(f"❌ Error during inspection: {e}")
        logger.debug(f"Inspection error details: {e}", exc_info=True)


def _resolve_java_class(class_or_object: Union[str, Any]) -> Optional[Any]:
    """Resolve a class name or object to a Java Class object."""
    
    if isinstance(class_or_object, str):
        # String class name - try to resolve it
        class_name = class_or_object
        
        # Try to import from common pysnt modules
        modules_to_try = [
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
        
        print(f"❌ Could not find class '{class_name}' in common pysnt modules")
        print("Try using the actual Java class object instead")
        return None
    
    else:
        # Assume it's already a Java class or object
        try:
            # Check if it's a jpype Java class
            class_name = str(type(class_or_object))
            if '_jpype._JClass' in class_name or 'java class' in str(class_or_object):
                # It's a jpype Java class, return it directly
                return class_or_object
            
            # If it's an instance, get its class
            if hasattr(class_or_object, 'getClass'):
                return class_or_object.getClass()
            else:
                # Assume it's already a Class object
                return class_or_object
        except:
            print(f"❌ Could not resolve Java class from: {type(class_or_object)}")
            return None


def _matches_keyword(name: str, keyword: str, case_sensitive: bool) -> bool:
    """Check if a name matches the keyword filter."""
    if not keyword:
        return True
    
    if case_sensitive:
        return keyword in name
    else:
        return keyword.lower() in name.lower()


def _show_constructors(java_class, keyword: str, case_sensitive: bool, max_results: int):
    """Show constructors matching the keyword."""
    try:
        constructors = java_class.getConstructors()
        class_name = str(java_class.getSimpleName())
        
        matching_constructors = []
        for constructor in constructors:
            if _matches_keyword(class_name, keyword, case_sensitive):
                param_types = [str(p.getSimpleName()) for p in constructor.getParameterTypes()]
                matching_constructors.append(param_types)
        
        if matching_constructors:
            print(f"\n🏗️  Constructors ({len(matching_constructors)}):")
            for i, params in enumerate(matching_constructors[:max_results]):
                params_str = ', '.join(params) if params else ''
                print(f"  {i+1}. {class_name}({params_str})")
            
            if len(matching_constructors) > max_results:
                print(f"  ... and {len(matching_constructors) - max_results} more")
        else:
            print(f"\n🏗️  Constructors: No matches for '{keyword}'")
            
    except Exception as e:
        print(f"❌ Error getting constructors: {e}")


def _show_methods(java_class, keyword: str, case_sensitive: bool, static_only: bool, max_results: int):
    """Show methods matching the keyword."""
    try:
        methods = java_class.getMethods()
        
        # Filter methods
        matching_methods = []
        for method in methods:
            method_name = str(method.getName())
            
            # Skip Object methods
            if method_name in ['equals', 'hashCode', 'toString', 'getClass', 'notify', 'notifyAll', 'wait']:
                continue
            
            # Check keyword match
            if not _matches_keyword(method_name, keyword, case_sensitive):
                continue
            
            # Check static filter
            modifiers = method.getModifiers()
            is_static = bool(modifiers & 0x0008)  # Modifier.STATIC
            
            if static_only and not is_static:
                continue
            
            # Get method info
            param_types = [str(p.getSimpleName()) for p in method.getParameterTypes()]
            return_type = str(method.getReturnType().getSimpleName())
            
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


def _show_fields(java_class, keyword: str, case_sensitive: bool, static_only: bool, max_results: int):
    """Show fields matching the keyword."""
    try:
        fields = java_class.getFields()
        
        # Filter fields
        matching_fields = []
        for field in fields:
            field_name = str(field.getName())
            
            # Check keyword match
            if not _matches_keyword(field_name, keyword, case_sensitive):
                continue
            
            # Check static filter
            modifiers = field.getModifiers()
            is_static = bool(modifiers & 0x0008)  # Modifier.STATIC
            is_final = bool(modifiers & 0x0010)   # Modifier.FINAL
            
            if static_only and not is_static:
                continue
            
            # Get field info
            field_type = str(field.getType().getSimpleName())
            
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


def get_methods(class_or_object: Union[str, Any], static_only: bool = False, include_inherited: bool = True) -> list:
    """
    Retrieve all public methods from a Java class or object.
    
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
        
        java_class = _resolve_java_class(class_or_object)
        if java_class is None:
            return []
        
        # Try different ways to get methods
        methods = None
        try:
            methods = java_class.getMethods()
        except AttributeError:
            # Try alternative approaches
            try:
                if hasattr(java_class, 'class_'):
                    methods = java_class.class_.getMethods()
                elif hasattr(java_class, '__javaclass__'):
                    methods = java_class.__javaclass__.getMethods()
                else:
                    # Last resort - use dir() and filter
                    all_attrs = dir(java_class)
                    methods = [attr for attr in all_attrs if not attr.startswith('_') and callable(getattr(java_class, attr, None))]
            except Exception as e:
                logger.error(f"Failed to get methods using alternative approaches: {e}")
                return []
        
        if not methods:
            logger.warning("No methods found for Java class")
            return []
        
        result = []
        
        for method in methods:
            try:
                if isinstance(method, str):
                    # Method name from dir() - create basic info
                    method_name = method
                    param_types = []
                    return_type = 'Any'
                    is_static = False
                else:
                    # Java Method object
                    method_name = str(method.getName())
                    
                    # Get method details
                    try:
                        param_types = [str(p.getSimpleName()) for p in method.getParameterTypes()]
                        return_type = str(method.getReturnType().getSimpleName())
                        
                        # Check static filter
                        modifiers = method.getModifiers()
                        is_static = bool(modifiers & 0x0008)  # Modifier.STATIC
                    except Exception:
                        # Fallback if we can't get detailed info
                        param_types = []
                        return_type = 'Any'
                        is_static = False
                
                # Skip Object methods unless explicitly requested
                if not include_inherited and method_name in [
                    'equals', 'hashCode', 'toString', 'getClass', 
                    'notify', 'notifyAll', 'wait'
                ]:
                    continue
                
                if static_only and not is_static:
                    continue
                
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
    Retrieve all public fields from a Java class or object.
    
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
        
        java_class = _resolve_java_class(class_or_object)
        if java_class is None:
            return []
        
        fields = java_class.getFields()
        result = []
        
        for field in fields:
            field_name = str(field.getName())
            
            # Check static filter
            modifiers = field.getModifiers()
            is_static = bool(modifiers & 0x0008)  # Modifier.STATIC
            is_final = bool(modifiers & 0x0010)   # Modifier.FINAL
            
            if static_only and not is_static:
                continue
            
            # Get field details
            field_type = str(field.getType().getSimpleName())
            
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
        
        # Sort by name for consistent output
        result.sort(key=lambda f: f['name'])
        return result
        
    except ImportError:
        logger.error("scyjava not available. Make sure pysnt is properly installed.")
        return []
    except Exception as e:
        logger.error(f"Error getting fields: {e}")
        return []


def find_members(class_or_object: Union[str, Any], 
                keyword: str,
                include_methods: bool = True,
                include_fields: bool = True,
                static_only: bool = False,
                case_sensitive: bool = False) -> Dict[str, list]:
    """
    Find methods and fields matching a keyword in a Java class or object.
    
    Parameters
    ----------
    class_or_object : str or Java object
        Either a string class name or a Java class/object
    keyword : str
        Keyword to search for in method and field names
    include_methods : bool, default True
        Whether to search methods
    include_fields : bool, default True
        Whether to search fields
    static_only : bool, default False
        Whether to search only static members
    case_sensitive : bool, default False
        Whether keyword matching should be case-sensitive
        
    Returns
    -------
    Dict[str, list]
        Dictionary with 'methods' and 'fields' keys containing matching members.
        Each member is a dictionary with detailed information.
        
    Examples
    --------
    >>> # Find all members containing 'length'
    >>> results = find_members('TreeStatistics', 'length')
    >>> print(f"Found {len(results['methods'])} methods and {len(results['fields'])} fields")
    
    >>> # Find only static methods containing 'get'
    >>> results = find_members('TreeStatistics', 'get', 
    ...                       include_fields=False, static_only=True)
    """
    result = {'methods': [], 'fields': []}
    
    if not keyword:
        logger.warning("No keyword provided for search")
        return result
    
    try:
        # Get methods if requested
        if include_methods:
            all_methods = get_methods(class_or_object, static_only=static_only)
            for method in all_methods:
                if _matches_keyword(method['name'], keyword, case_sensitive):
                    result['methods'].append(method)
        
        # Get fields if requested
        if include_fields:
            all_fields = get_fields(class_or_object, static_only=static_only)
            for field in all_fields:
                if _matches_keyword(field['name'], keyword, case_sensitive):
                    result['fields'].append(field)
        
        return result
        
    except Exception as e:
        logger.error(f"Error finding members: {e}")
        return result


if __name__ == "__main__":
    # Run Java setup if called directly
    setup_java_environment()