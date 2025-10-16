"""
Setup utilities for PySNT.

This module provides helper functions for setting up PySNT,
including Fiji path configuration and environment setup with
persistent configuration storage.
"""

import json
import os
import platform
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional


def get_config_dir() -> Path:
    """
    Get platform-specific config directory.
    
    Returns
    -------
    Path
        Platform-specific configuration directory for pysnt (following XDG base directory specification)
    """
    system = platform.system()
    if system == "Windows":
        return Path(os.getenv('APPDATA', '~')).expanduser() / 'pysnt'
    elif system == "Darwin":  # macOS
        return Path.home() / 'Library' / 'Application Support' / 'pysnt'
    else:  # Linux and others
        xdg_config = os.getenv('XDG_CONFIG_HOME', '~/.config')
        return Path(xdg_config).expanduser() / 'pysnt'


def load_config() -> Dict[str, Any]:
    """
    Load configuration from platform-specific config file.
    
    Returns
    -------
    Dict[str, Any]
        Configuration dictionary, empty if file doesn't exist or is invalid
    """
    config_file = get_config_dir() / 'config.json'
    if not config_file.exists():
        return {}
    
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_config(config: Dict[str, Any]) -> bool:
    """
    Save configuration to platform-specific config file.
    
    Parameters
    ----------
    config : Dict[str, Any]
        Configuration dictionary to save
        
    Returns
    -------
    bool
        True if saved successfully, False otherwise
    """
    config_dir = get_config_dir()
    config_file = config_dir / 'config.json'
    
    try:
        # Create config directory if it doesn't exist
        config_dir.mkdir(parents=True, exist_ok=True)
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except (IOError, OSError):
        return False


def set_fiji_path(fiji_path: str, validate: bool = True) -> bool:
    """
    Set and persist the Fiji installation path.
    
    Parameters
    ----------
    fiji_path : str
        Path to Fiji installation
    validate : bool, default True
        Whether to validate the path before saving
        
    Returns
    -------
    bool
        True if path was set successfully, False otherwise
        
    Examples
    --------
    >>> # Set Fiji path
    >>> pysnt.setup_utils.set_fiji_path("/Applications/Fiji.app")
    >>> 
    >>> # Set without validation (use with caution)
    >>> pysnt.setup_utils.set_fiji_path("/custom/fiji/path", validate=False)
    """
    if validate:
        if not Path(fiji_path).exists():
            return False
        
        status = check_fiji_installation(fiji_path)
        if not status["is_fiji"]:
            # Continue anyway, but it's not ideal
            pass
    
    # Load current config and update
    config = load_config()
    config["fiji_path"] = fiji_path
    
    return save_config(config)


def get_fiji_path() -> Optional[str]:
    """
    Get the currently configured Fiji path.
    
    Returns the path from the first available source in priority order:
    1. FIJI_PATH environment variable
    2. Config file
    3. None if not found
    
    Returns
    -------
    str or None
        Current Fiji path if configured, None otherwise
        
    Examples
    --------
    >>> # Check current Fiji path
    >>> path = pysnt.setup_utils.get_fiji_path()
    >>> if path:
    ...     print(f"Fiji configured at: {path}")
    ... else:
    ...     print("Fiji path not configured")
    """
    # Check environment variable first
    fiji_env = os.environ.get("FIJI_PATH")
    if fiji_env:
        return fiji_env
    
    # Check config file
    config = load_config()
    return config.get("fiji_path")


def clear_fiji_path(reset_env: bool = False) -> bool:
    """
    Clear the saved Fiji path from configuration.
    
    Parameters
    ----------
    reset_env : bool, default False
        If True, also clears the FIJI_PATH environment variable for the current session.
        If False, only clears the saved configuration file.
    
    Returns
    -------
    bool
        True if cleared successfully, False otherwise
        
    Examples
    --------
    >>> # Clear saved Fiji path only
    >>> pysnt.setup_utils.clear_fiji_path()
    >>> 
    >>> # Clear both saved path and environment variable
    >>> pysnt.setup_utils.clear_fiji_path(reset_env=True)
    """
    success = True
    
    # Clear from config file
    config = load_config()
    if "fiji_path" in config:
        config.pop("fiji_path")
        success = save_config(config)
    
    # Clear environment variable if requested
    if reset_env and "FIJI_PATH" in os.environ:
        try:
            del os.environ["FIJI_PATH"]
        except Exception:
            success = False
    
    return success


def reset_fiji_path() -> bool:
    """
    Completely reset Fiji path configuration.
    
    This clears both the saved configuration file and the FIJI_PATH 
    environment variable for the current session.
    
    Returns
    -------
    bool
        True if reset successfully, False otherwise
        
    Examples
    --------
    >>> # Completely reset Fiji configuration
    >>> pysnt.setup_utils.reset_fiji_path()
    """
    return clear_fiji_path(reset_env=True)


def get_config_info() -> Dict[str, Any]:
    """
    Get information about the current configuration.
    
    Returns
    -------
    Dict[str, Any]
        Dictionary containing configuration information
        
    Examples
    --------
    >>> # Get config info
    >>> info = pysnt.setup_utils.get_config_info()
    >>> print(f"Config directory: {info['config_dir']}")
    >>> print(f"Config file exists: {info['config_exists']}")
    >>> print(f"Fiji path: {info['fiji_path']}")
    """
    config_dir = get_config_dir()
    config_file = config_dir / 'config.json'
    config = load_config()
    
    return {
        "config_dir": str(config_dir),
        "config_file": str(config_file),
        "config_exists": config_file.exists(),
        "fiji_path": config.get("fiji_path"),
        "fiji_path_env": os.environ.get("FIJI_PATH"),
        "platform": platform.system(),
        "common_paths": find_fiji_installations()
    }


def is_fiji_valid() -> bool:
    """
    Quick check if the current Fiji configuration is valid with SNT plugin.
    
    Returns
    -------
    bool
        True if Fiji is configured with SNT plugin, False otherwise
        
    Examples
    --------
    >>> # Quick validation check
    >>> if not pysnt.setup_utils.is_fiji_valid():
    ...     print("Fiji with SNT not configured properly!")
    ...     exit(1)
    >>> 
    >>> # Use in scripts
    >>> import sys
    >>> import pysnt.setup_utils as setup
    >>> if not setup.is_fiji_valid():
    ...     print("Error: Fiji installation not found or SNT plugin missing")
    ...     print("Run: python -m pysnt.setup_utils --auto-detect")
    ...     sys.exit(1)
    """
    # Get current effective path
    fiji_path = get_fiji_path()
    if not fiji_path:
        return False
    
    # Check if path exists
    if not Path(fiji_path).exists():
        return False
    
    # Check if it's a valid Fiji installation
    status = check_fiji_installation(fiji_path)
    return status["is_fiji"]


def get_fiji_status() -> Dict[str, Any]:
    """
    Get detailed status of the current Fiji configuration/
    
    Returns
    -------
    Dict[str, Any]
        Dictionary with detailed status information including:
        - configured: bool - Whether any Fiji path is configured
        - path: str or None - The effective Fiji path
        - exists: bool - Whether the path exists
        - valid: bool - Whether it's a valid Fiji installation with SNT
        - issues: List[str] - List of any issues found (including SNT-specific)
        
    Examples
    --------
    >>> # Get detailed status
    >>> status = pysnt.setup_utils.get_fiji_status()
    >>> if not status['valid']:
    ...     print(f"Fiji/SNT issues: {', '.join(status['issues'])}")
    """
    fiji_path = get_fiji_path()
    
    result = {
        "configured": fiji_path is not None,
        "path": fiji_path,
        "exists": False,
        "valid": False,
        "issues": []
    }
    
    if not fiji_path:
        result["issues"].append("No Fiji path configured")
        return result
    
    if not Path(fiji_path).exists():
        result["issues"].append(f"Configured path does not exist: {fiji_path}")
        return result
    
    result["exists"] = True
    
    # Check if it's a valid Fiji installation
    status = check_fiji_installation(fiji_path)
    result["valid"] = status["is_fiji"]
    
    if not status["is_fiji"]:
        result["issues"].extend(status["issues"])
    
    return result


def show_config_status():
    """
    Display current Fiji configuration status in a user-friendly format.
    
    Examples
    --------
    >>> # Show current configuration
    >>> pysnt.setup_utils.show_config_status()
    """
    print("PySNT Fiji Configuration Status")
    print("=" * 40)
    
    info = get_config_info()
    
    print(f"Platform: {info['platform']}")
    print(f"Config directory: {info['config_dir']}")
    print(f"Config file exists: {info['config_exists']}")
    print()
    
    # Current paths
    env_path = info['fiji_path_env']
    config_path = info['fiji_path']
    
    print("Current Configuration:")
    if env_path:
        print(f"  FIJI_PATH (env var): {env_path}")
        exists = "✓" if Path(env_path).exists() else "✗ (not found)"
        print(f"    Status: {exists}")
    else:
        print("  FIJI_PATH (env var): Not set")
    
    if config_path:
        print(f"  Config file path: {config_path}")
        exists = "✓" if Path(config_path).exists() else "✗ (not found)"
        print(f"    Status: {exists}")
    else:
        print("  Config file path: Not set")
    
    # Effective path
    effective_path = get_fiji_path()
    if effective_path:
        print(f"\nEffective Fiji path: {effective_path}")
    else:
        print("\nNo Fiji path configured")
    
    # Available installations
    available = find_fiji_installations()
    if available:
        print(f"\nAvailable Fiji installations found:")
        for path in available:
            exists = "✓" if Path(path).exists() else " "
            print(f"  {exists} {path}")
    else:
        print(f"\nNo Fiji installations found in common locations")


def auto_detect_and_configure() -> Optional[str]:
    """
    Try to auto-detect a valid Fiji installation and save to config if found.
    
    Returns
    -------
    str or None
        Path to detected Fiji installation if found and configured, None otherwise
        
    Examples
    --------
    >>> # Auto-detect and configure Fiji
    >>> path = pysnt.setup_utils.auto_detect_and_configure()
    >>> if path:
    ...     print(f"Fiji configured at: {path}")
    ... else:
    ...     print("No Fiji installation detected")
    """
    print("Attempting to auto-detect Fiji installation...")
    
    # Check if already configured
    current_path = get_fiji_path()
    if current_path and Path(current_path).exists():
        status = check_fiji_installation(current_path)
        if status["is_fiji"]:
            print(f"✓ Fiji already configured at: {current_path}")
            return current_path
    
    # Try to find installations
    found = find_fiji_installations()
    if found:
        # Use the first valid installation
        for path in found:
            status = check_fiji_installation(path)
            if status["is_fiji"]:
                print(f"✓ Found Fiji at: {path}")
                
                if set_fiji_path(path):
                    print("✓ Path saved to config")
                    return path
                else:
                    print("✗ Failed to save path to config")
    
    print("✗ Could not auto-detect Fiji installation")
    return None


def setup_fiji_environment(fiji_path: str, permanent: bool = False) -> bool:
    """
    Set up Fiji environment variable.
    
    Parameters
    ----------
    fiji_path : str
        Path to Fiji installation
    permanent : bool, default False
        Whether to attempt permanent setup (adds to shell profile)
        
    Returns
    -------
    bool
        True if setup was successful
    """
    if not os.path.exists(fiji_path):
        print(f"❌ Fiji path does not exist: {fiji_path}")
        return False
    
    # Set for current session
    os.environ['FIJI_PATH'] = fiji_path
    print(f"✅ FIJI_PATH set for current session: {fiji_path}")
    
    if permanent:
        return _setup_permanent_fiji_path(fiji_path)
    
    return True


def _setup_permanent_fiji_path(fiji_path: str) -> bool:
    """
    Attempt to set up permanent FIJI_PATH in shell profile.
    
    Parameters
    ----------
    fiji_path : str
        Path to Fiji installation
        
    Returns
    -------
    bool
        True if setup was successful
    """
    system = platform.system().lower()
    home = Path.home()
    
    # Determine shell profile file
    profile_files = []
    if system == "darwin":  # macOS
        profile_files = [".zshrc", ".bash_profile", ".bashrc"]
    elif system == "linux":
        profile_files = [".bashrc", ".bash_profile", ".zshrc"]
    elif system == "windows":
        print("⚠️  Permanent environment setup on Windows requires manual configuration.")
        print("Please add FIJI_PATH to your system environment variables.")
        return False
    
    # Find existing profile file or use default
    profile_file = None
    for pf in profile_files:
        if (home / pf).exists():
            profile_file = home / pf
            break
    
    if not profile_file:
        # Use default for the system
        profile_file = home / profile_files[0]
    
    try:
        # Check if FIJI_PATH is already set in the file
        export_line = f'export FIJI_PATH="{fiji_path}"'
        
        if profile_file.exists():
            content = profile_file.read_text()
            if "FIJI_PATH" in content:
                print(f"⚠️  FIJI_PATH already exists in {profile_file}")
                print("Please update it manually if needed.")
                return True
        
        # Append to profile file
        with open(profile_file, "a") as f:
            f.write(f"\n# Added by PySNT\n{export_line}\n")
        
        print(f"✅ Added FIJI_PATH to {profile_file}")
        print("Please restart your terminal or run:")
        print(f"   source {profile_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to set up permanent FIJI_PATH: {e}")
        print("Please add this line to your shell profile manually:")
        print(f'   export FIJI_PATH="{fiji_path}"')
        return False


def find_fiji_installations() -> List[str]:
    """
    Search for Fiji installations on the system.
    
    Returns
    -------
    List[str]
        List of found Fiji installation paths
    """
    potential_paths = [
        # macOS
        "/Applications/Fiji.app",
        os.path.expanduser("~/Applications/Fiji.app"),
        os.path.expanduser("~/Desktop/Fiji.app"),
        os.path.expanduser("~/Downloads/Fiji.app"),
        
        # Windows
        "C:/Fiji.app",
        "C:/Program Files/Fiji.app",
        "C:/Program Files (x86)/Fiji.app",
        os.path.expanduser("~/Desktop/Fiji.app"),
        os.path.expanduser("~/Downloads/Fiji.app"),
        
        # Linux
        "/opt/Fiji.app",
        "/usr/local/Fiji.app",
        os.path.expanduser("~/Fiji.app"),
        os.path.expanduser("~/Desktop/Fiji.app"),
        os.path.expanduser("~/Downloads/Fiji.app"),
        
        # Common user locations
        os.path.expanduser("~/Software/Fiji.app"),
        os.path.expanduser("~/Programs/Fiji.app"),
    ]
    
    found_installations = []
    for path in potential_paths:
        if os.path.exists(path):
            # Enhanced validation - check if it's actually a Fiji installation
            status = check_fiji_installation(path)
            # Include if it has basic Fiji structure (even without SNT for broader compatibility)
            if status["has_jars"] and (status["executables"] or status["has_plugins"]):
                found_installations.append(path)
    
    return found_installations


def check_fiji_installation(fiji_path: str) -> dict:
    """
    Check and validate a Fiji installation serving SNT.
    
    Parameters
    ----------
    fiji_path : str
        Path to check
        
    Returns
    -------
    dict
        Dictionary with validation results including:
        - path: str - The path that was checked
        - exists: bool - Whether the path exists
        - is_fiji: bool - Whether it appears to be a Fiji installation
        - has_snt: bool - Whether SNT plugin is found
        - executables: List[str] - Found executables
        - has_plugins: bool - Whether plugins directory exists
        - has_jars: bool - Whether jars directory exists
        - snt_jars: List[str] - Found SNT jar files
        - issues: List[str] - List of issues found
    """
    result = {
        "path": fiji_path,
        "exists": False,
        "is_fiji": False,
        "has_snt": False,
        "executables": [],
        "has_plugins": False,
        "has_jars": False,
        "snt_jars": [],
        "issues": []
    }
    
    if not os.path.exists(fiji_path):
        result["issues"].append("Path does not exist")
        return result
    
    result["exists"] = True
    path_obj = Path(fiji_path)
    
    # Check for executables
    executables = ["fiji"]
    
    for exe in executables:
        if (path_obj / exe).exists():
            result["executables"].append(exe)
    
    if not result["executables"]:
        result["issues"].append("No Fiji executable found")
    
    # Check for key directories
    if (path_obj / "plugins").exists():
        result["has_plugins"] = True
    else:
        result["issues"].append("No plugins directory found")
    
    if (path_obj / "jars").exists():
        result["has_jars"] = True
        
        # Check for the SNT jar in the jars directory
        jars_dir = path_obj / "jars"
        try:
            for jar_file in jars_dir.glob("*.jar"):
                if jar_file.name.startswith("SNT-"):
                    result["snt_jars"].append(jar_file.name)
                    result["has_snt"] = True
                    break  # Short-circuit: only one SNT jar expected
            
            if not result["has_snt"]:
                result["issues"].append("The SNT jar file was not found")
                
        except Exception as e:
            result["issues"].append(f"Could not scan jars directory: {e}")
    else:
        result["issues"].append("No jars directory found")
    
    # Enhanced assessment: requires Fiji basics AND SNT plugin
    result["is_fiji"] = (len(result["executables"]) > 0 and 
                        result["has_plugins"] and 
                        result["has_jars"] and 
                        result["has_snt"])
    
    return result


def print_fiji_status(fiji_path: str):
    """
    Print detailed status of a Fiji installation with SNT plugin check.
    
    Parameters
    ----------
    fiji_path : str
        Path to check
    """
    status = check_fiji_installation(fiji_path)
    
    print(f"\n🔍 Fiji Installation Check: {fiji_path}")
    print("=" * 50)
    
    if not status["exists"]:
        print("❌ Path does not exist")
        return
    
    print(f"📁 Path exists: ✅")
    print(f"🎯 Is Fiji installation: {'✅' if status['is_fiji'] else '❌'}")
    
    if status["executables"]:
        print(f"⚙️  Executables found: {', '.join(status['executables'])}")
    else:
        print("⚙️  Executables found: ❌ None")
    
    print(f"🔌 Has plugins directory: {'✅' if status['has_plugins'] else '❌'}")
    print(f"📚 Has jars directory: {'✅' if status['has_jars'] else '❌'}")
    
    # SNT-specific checks
    print(f"🧠 Has SNT plugin: {'✅' if status['has_snt'] else '❌'}")
    
    if status["snt_jars"]:
        print(f"📦 SNT jar files found:")
        for jar in status["snt_jars"]:
            print(f"   • {jar}")
    elif status["has_jars"]:
        print("📦 SNT jar files: ❌ None found (looking for SNT-*.jar)")
    
    if status["issues"]:
        print("\n⚠️  Issues found:")
        for issue in status["issues"]:
            print(f"   • {issue}")
    
    if status["is_fiji"]:
        print("\n✅ This appears to be a valid Fiji installation with SNT!")
    else:
        print("\n❌ This does not appear to be a valid Fiji installation with SNT.")
        if status["has_plugins"] and status["has_jars"] and not status["has_snt"]:
            print("   Note: Fiji installation found, but SNT plugin is missing.")


def interactive_fiji_setup():
    """
    Interactive setup wizard for Fiji configuration with persistent storage.
    """
    print("🧙 PySNT Fiji Setup Wizard")
    print("=" * 30)
    
    # Check current status using new config system
    current_fiji = get_fiji_path()
    if current_fiji:
        print(f"Current configured path: {current_fiji}")
        status = check_fiji_installation(current_fiji)
        if status["is_fiji"]:
            print("✅ Current Fiji installation appears valid.")
            return current_fiji
        else:
            print("⚠️  Current configured path may not be valid.")
    
    # Search for installations
    print("\n🔍 Searching for Fiji installations...")
    found = find_fiji_installations()
    
    if found:
        print(f"Found {len(found)} potential Fiji installation(s):")
        for i, path in enumerate(found, 1):
            print(f"  {i}. {path}")
        
        while True:
            try:
                choice = input(f"\nSelect installation (1-{len(found)}) or 'other' for custom path: ").strip()
                
                if choice.lower() == 'other':
                    break
                
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(found):
                    selected_path = found[choice_idx]
                    print_fiji_status(selected_path)
                    
                    confirm = input("\nUse this installation? (y/N): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        # Save to persistent config
                        if set_fiji_path(selected_path):
                            print("✅ Path saved to configuration")
                        else:
                            print("⚠️  Could not save to configuration, but will use for this session")
                        return selected_path
                else:
                    print("Invalid selection.")
                    
            except (ValueError, KeyboardInterrupt):
                break
    
    # Custom path input
    print("\n📁 Enter custom Fiji path:")
    while True:
        try:
            custom_path = input("Fiji path (or 'quit' to exit): ").strip()
            
            if custom_path.lower() in ['quit', 'exit', 'cancel']:
                return None
            
            custom_path = os.path.expanduser(custom_path)
            print_fiji_status(custom_path)
            
            confirm = input("\nUse this path? (y/N): ").strip().lower()
            if confirm in ['y', 'yes']:
                # Save to persistent config
                if set_fiji_path(custom_path, validate=False):
                    print("✅ Path saved to configuration")
                else:
                    print("⚠️  Could not save to configuration, but will use for this session")
                return custom_path
                
        except KeyboardInterrupt:
            return None
    
    return None


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="PySNT Fiji Configuration Utility",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m pysnt.setup_utils                    # Interactive setup
  python -m pysnt.setup_utils --status           # Show configuration status
  python -m pysnt.setup_utils --auto-detect      # Auto-detect Fiji
  python -m pysnt.setup_utils --set /path/to/Fiji.app  # Set Fiji path
  python -m pysnt.setup_utils --clear            # Clear saved path
  python -m pysnt.setup_utils --reset            # Reset everything (config + env var)
  python -m pysnt.setup_utils --check            # Check if configuration is valid
        """
    )
    
    parser.add_argument('--status', action='store_true', help='Show configuration status')
    parser.add_argument('--auto-detect', action='store_true', help='Auto-detect Fiji installation')
    parser.add_argument('--set', metavar='PATH', help='Set Fiji path')
    parser.add_argument('--clear', action='store_true', help='Clear saved Fiji path')
    parser.add_argument('--reset', action='store_true', help='Reset Fiji path (clear config and env var)')
    parser.add_argument('--check', action='store_true', help='Check if Fiji configuration is valid (exit code 0=valid, 1=invalid)')
    parser.add_argument('--no-validate', action='store_true', help='Skip path validation when setting')
    
    args = parser.parse_args()
    
    if args.status:
        show_config_status()
    elif args.auto_detect:
        path = auto_detect_and_configure()
        if not path:
            print("\nTry:")
            print("  1. Installing Fiji to a common location")
            print("  2. Setting FIJI_PATH environment variable")
            print("  3. Using --set to specify the path manually")
    elif args.set:
        success = set_fiji_path(args.set, validate=not args.no_validate)
        if success:
            print(f"✓ Fiji path set to: {args.set}")
        else:
            print(f"✗ Failed to set Fiji path: {args.set}")
    elif args.clear:
        success = clear_fiji_path()
        if success:
            print("✓ Fiji path cleared from configuration")
        else:
            print("✗ Failed to clear Fiji path")
    elif args.reset:
        success = reset_fiji_path()
        if success:
            print("✓ Fiji configuration completely reset (config file and environment variable)")
        else:
            print("✗ Failed to reset Fiji configuration")
    elif args.check:
        is_valid = is_fiji_valid()
        if is_valid:
            print("✓ Fiji configuration is valid")
            sys.exit(0)
        else:
            status = get_fiji_status()
            print("✗ Fiji configuration is invalid")
            if status['issues']:
                print("Issues found:")
                for issue in status['issues']:
                    print(f"  • {issue}")
            print("\nTo fix, try:")
            print("  python -m pysnt.setup_utils --auto-detect")
            print("  python -m pysnt.setup_utils --set /path/to/Fiji.app")
            sys.exit(1)
    else:
        # Run interactive setup if no arguments provided
        fiji_path = interactive_fiji_setup()
        
        if fiji_path:
            print(f"\n🎯 Selected Fiji path: {fiji_path}")
            
            # Offer to set up environment variable as well
            setup_env = input("Also set up FIJI_PATH environment variable? (y/N): ").strip().lower()
            if setup_env in ['y', 'yes']:
                permanent = input("Make permanent (add to shell profile)? (y/N): ").strip().lower()
                setup_fiji_environment(fiji_path, permanent=(permanent in ['y', 'yes']))
            
            print("\n✅ Setup complete! You can now use:")
            print("   import pysnt")
            print("   pysnt.initialize()")
        else:
            print("\n❌ Setup cancelled.")