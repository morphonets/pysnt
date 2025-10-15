"""
Setup utilities for PySNT.

This module provides helper functions for setting up PySNT,
including Fiji path configuration and environment setup.
"""

import os
import platform
from pathlib import Path
from typing import List


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
            # Basic validation
            path_obj = Path(path)
            if any((path_obj / indicator).exists() for indicator in ["fiji", "config", "jars"]):
                found_installations.append(path)
    
    return found_installations


def check_fiji_installation(fiji_path: str) -> dict:
    """
    Check and validate a Fiji installation.
    
    Parameters
    ----------
    fiji_path : str
        Path to check
        
    Returns
    -------
    dict
        Dictionary with validation results
    """
    result = {
        "path": fiji_path,
        "exists": False,
        "is_fiji": False,
        "executables": [],
        "has_plugins": False,
        "has_jars": False,
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
    else:
        result["issues"].append("No jars directory found")
    
    # Overall assessment
    result["is_fiji"] = (len(result["executables"]) > 0 and result["has_plugins"])
    
    return result


def print_fiji_status(fiji_path: str):
    """
    Print detailed status of a Fiji installation.
    
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
    
    if status["issues"]:
        print("\n⚠️  Issues found:")
        for issue in status["issues"]:
            print(f"   • {issue}")
    
    if status["is_fiji"]:
        print("\n✅ This appears to be a valid Fiji installation!")
    else:
        print("\n❌ This does not appear to be a valid Fiji installation.")


def interactive_fiji_setup():
    """
    Interactive setup wizard for Fiji configuration.
    """
    print("🧙 PySNT Fiji Setup Wizard")
    print("=" * 30)
    
    # Check current status
    current_fiji = os.environ.get("FIJI_PATH")
    if current_fiji:
        print(f"Current FIJI_PATH: {current_fiji}")
        status = check_fiji_installation(current_fiji)
        if status["is_fiji"]:
            print("✅ Current Fiji installation appears valid.")
            return current_fiji
        else:
            print("⚠️  Current FIJI_PATH may not be valid.")
    
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
                return custom_path
                
        except KeyboardInterrupt:
            return None
    
    return None


if __name__ == "__main__":
    # Run interactive setup if called directly
    fiji_path = interactive_fiji_setup()
    
    if fiji_path:
        print(f"\n🎯 Selected Fiji path: {fiji_path}")
        
        # Offer to set up environment
        setup_env = input("Set up FIJI_PATH environment variable? (y/N): ").strip().lower()
        if setup_env in ['y', 'yes']:
            permanent = input("Make permanent (add to shell profile)? (y/N): ").strip().lower()
            setup_fiji_environment(fiji_path, permanent=(permanent in ['y', 'yes']))
        
        print("\n✅ Setup complete! You can now use:")
        print("   import pysnt")
        print("   pysnt.initialize_snt()")
    else:
        print("\n❌ Setup cancelled.")