#!/usr/bin/env python3
"""
Command-line interface for PySNT.

This module provides command-line access to PySNT functionality,
including version information and system diagnostics.
"""

import sys
import argparse
from . import version, print_version, info


def main():
    """Main command-line interface."""
    parser = argparse.ArgumentParser(
        prog='pysnt',
        description='pySNT: Python interface for SNT',
        epilog='For more information, visit: https://github.com/morphonets/pysnt'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='store_true',
        help='Show PySNT version'
    )
    
    parser.add_argument(
        '--info', '-i',
        action='store_true', 
        help='Show detailed system and dependency information'
    )
    
    parser.add_argument(
        '--check-java',
        action='store_true',
        help='Check Java installation status'
    )
    
    parser.add_argument(
        '--check-fiji',
        action='store_true',
        help='Check Fiji installation status'
    )
    
    parser.add_argument(
        '--setup-java',
        action='store_true',
        help='Run interactive Java setup wizard'
    )
    
    parser.add_argument(
        '--setup-fiji',
        action='store_true',
        help='Run interactive Fiji setup wizard'
    )
    
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    # Handle version request
    if args.version:
        print_version()
        return
    
    # Handle info request
    if args.info:
        info()
        return
    
    # Handle Java check
    if args.check_java:
        try:
            from .java_utils import print_java_status
            print_java_status()
        except ImportError as e:
            print(f"❌ Java utilities not available: {e}")
        return
    
    # Handle Fiji check
    if args.check_fiji:
        try:
            from .setup_utils import find_fiji_installations, print_fiji_status
            
            print("🔍 Searching for Fiji installations...")
            installations = find_fiji_installations()
            
            if installations:
                print(f"Found {len(installations)} Fiji installation(s):")
                for i, path in enumerate(installations, 1):
                    print(f"\n{i}. {path}")
                    print_fiji_status(path)
            else:
                print("❌ No Fiji installations found")
                
        except ImportError as e:
            print(f"❌ Fiji utilities not available: {e}")
        return
    
    # Handle Java setup
    if args.setup_java:
        try:
            from .java_utils import setup_java_environment
            setup_java_environment()
        except ImportError as e:
            print(f"❌ Java setup utilities not available: {e}")
        return
    
    # Handle Fiji setup
    if args.setup_fiji:
        try:
            from .setup_utils import interactive_fiji_setup, setup_fiji_environment
            
            fiji_path = interactive_fiji_setup()
            if fiji_path:
                print(f"\n🎯 Selected Fiji path: {fiji_path}")
                
                # Offer to set up environment
                try:
                    setup_env = input("Set up FIJI_PATH environment variable? (y/N): ").strip().lower()
                    if setup_env in ['y', 'yes']:
                        permanent = input("Make permanent (add to shell profile)? (y/N): ").strip().lower()
                        setup_fiji_environment(fiji_path, permanent=(permanent in ['y', 'yes']))
                except KeyboardInterrupt:
                    print("\nSetup cancelled.")
            else:
                print("❌ Fiji setup cancelled.")
                
        except ImportError as e:
            print(f"❌ Fiji setup utilities not available: {e}")
        return


if __name__ == '__main__':
    main()