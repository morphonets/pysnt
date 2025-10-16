#!/usr/bin/env python3
"""
Test that autocompletion for SNT Java classes is working
"""

import sys
from pathlib import Path

try:
    import pytest
except ImportError:
    pytest = None

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))


def test_tree_class_import():
    """Test that Tree class can be imported."""
    import pysnt
    
    # Test Tree class import
    tree = pysnt.Tree
    assert tree is not None, "Tree class should be importable"


def test_tree_methods_accessible():
    """Test that Tree class methods are accessible (for IDE autocompletion)."""
    import pysnt
    
    tree = pysnt.Tree
    
    # Test that methods exist (for autocompletion)
    # Note: We're not calling them since SNT isn't initialized,
    # just checking they're accessible for IDE autocompletion
    assert hasattr(tree, 'getColor'), "Tree.getColor method should be accessible"
    assert hasattr(tree, 'getRoot'), "Tree.getRoot method should be accessible"
    assert hasattr(tree, 'getPaths'), "Tree.getPaths method should be accessible"
    assert hasattr(tree, 'size'), "Tree.size method should be accessible"


def test_analysis_class_import():
    """Test that an analysis class can be imported."""
    from pysnt.analysis import TreeStatistics
    assert TreeStatistics is not None, "TreeStatistics class should be importable"


def test_analysis_methods_accessible():
    """Test that an analysis class methods are accessible."""
    from pysnt.analysis import TreeStatistics
    
    # Test that methods exist for autocompletion
    assert hasattr(TreeStatistics, 'getSummaryStats'), "TreeStatistics.getSummaryStats should be accessible"


def test_path_class_methods():
    """Test that Path class methods are accessible."""
    import pysnt
    
    path = pysnt.Path
    
    # Test common Path methods
    assert hasattr(path, 'getLength'), "Path.getLength method should be accessible"
    assert hasattr(path, 'getNodes'), "Path.getNodes method should be accessible"
    assert hasattr(path, 'getSWCType'), "Path.getSWCType method should be accessible"


def test_snt_utils_methods():
    """Test that SNTUtils methods are accessible."""
    import pysnt
    
    snt_utils = pysnt.SNTUtils
    
    # Test SNTUtils methods
    assert hasattr(snt_utils, 'getVersion'), "SNTUtils.getVersion should be accessible"
    assert hasattr(snt_utils, 'isDebugMode'), "SNTUtils.isDebugMode should be accessible"


if __name__ == "__main__":
    # Run tests when called directly
    print("Testing Java autocompletion...")
    
    try:
        test_tree_class_import()
        print("✓ Tree class import test passed")
        
        test_tree_methods_accessible()
        print("✓ Tree methods accessibility test passed")
        
        test_analysis_class_import()
        print("✓ Analysis class import test passed")
        
        test_analysis_methods_accessible()
        print("✓ Analysis methods accessibility test passed")
        
        test_path_class_methods()
        print("✓ Path class methods test passed")
        
        test_snt_utils_methods()
        print("✓ SNTUtils methods test passed")
        
        print("\n All autocompletion tests passed!")
        
    except Exception as e:
        print(f"\n✘ Test failed: {e}")
        sys.exit(1)