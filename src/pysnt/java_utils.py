"""
Java utilities for PySNT.

This module handles Java/OpenJDK installation and configuration.
"""

import os
import sys
import subprocess
import logging
from pathlib import Path
from typing import Optional, Tuple, Dict, Any

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
        print("Please install Java manually:")
        print(f"  1. Download OpenJDK {version} from: https://adoptium.net/")
        print("  2. Set JAVA_HOME environment variable")
        print("  3. Add Java to PATH")
        return False
        
    except Exception as e:
        logger.error(f"Failed to install OpenJDK: {e}")
        print(f"❌ Failed to install OpenJDK {version}: {e}")
        print("Please install Java manually:")
        print(f"  1. Download OpenJDK {version} from: https://adoptium.net/")
        print("  2. Set JAVA_HOME environment variable")
        print("  3. Add Java to PATH")
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
        print("❌ Java not available")
        print("\n💡 To install Java:")
        print("  1. Automatic: Call ensure_java_available()")
        print("  2. Manual: Download from https://adoptium.net/")
        print("  3. Package manager: brew install openjdk@21 (macOS)")


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
    print("This will download and install Java automatically.")
    
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


if __name__ == "__main__":
    # Run Java setup if called directly
    setup_java_environment()