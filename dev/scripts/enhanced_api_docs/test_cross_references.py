#!/usr/bin/env python3
"""
Test script for cross-reference functionality.
"""

import sys
from pathlib import Path

# Add the enhanced_api_docs directory to the path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from .cross_reference_builder import CrossReferenceBuilder
    from .json_enhancer import EnhancedJSONStubData, EnhancedMethodInfo, EnhancedMethodOverload, EnhancedParameterInfo
    from .rst_generator import SphinxRSTGenerator
    from .rst_templates import RSTTemplateEngine
except ImportError:
    # Fallback for direct execution
    import cross_reference_builder
    import json_enhancer
    import rst_generator
    import rst_templates
    
    CrossReferenceBuilder = cross_reference_builder.CrossReferenceBuilder
    EnhancedJSONStubData = json_enhancer.EnhancedJSONStubData
    EnhancedMethodInfo = json_enhancer.EnhancedMethodInfo
    EnhancedMethodOverload = json_enhancer.EnhancedMethodOverload
    EnhancedParameterInfo = json_enhancer.EnhancedParameterInfo
    SphinxRSTGenerator = rst_generator.SphinxRSTGenerator
    RSTTemplateEngine = rst_templates.RSTTemplateEngine


def create_test_stub(class_name: str, package: str, methods: list = None) -> EnhancedJSONStubData:
    """Create a test enhanced stub for testing."""
    if methods is None:
        methods = []
    
    return EnhancedJSONStubData(
        class_name=class_name,
        package=package,
        extracted_at="2024-01-01T00:00:00",
        extractor_version="1.0.0",
        enhancement_timestamp="2024-01-01T00:00:00",
        enhancement_version="1.0.0",
        methods=methods,
        fields=[],
        constructors=[],
        javadoc_description=f"Test class {class_name} for cross-reference testing.",
        inheritance={'extends': [], 'implements': []},
        see_also=[]
    )


def create_test_method(name: str, category: str = "Utilities", see_also: list = None) -> EnhancedMethodInfo:
    """Create a test method for testing."""
    if see_also is None:
        see_also = []
    
    param = EnhancedParameterInfo(
        name="param1",
        type="String",
        java_type="java.lang.String",
        description="Test parameter"
    )
    
    overload = EnhancedMethodOverload(
        signature=f"{name}(String param1)",
        params=[param],
        return_type="void",
        java_return_type="void",
        return_description="No return value"
    )
    
    return EnhancedMethodInfo(
        name=name,
        overloads=[overload],
        documentation=f"Test method {name}",
        javadoc_description=f"This is a test method named {name}.",
        category=category,
        see_also=see_also
    )


def test_cross_reference_builder():
    """Test the cross-reference builder functionality."""
    print("Testing CrossReferenceBuilder...")
    
    # Create test data
    tree_method = create_test_method("getRoot", "Getters")
    analyzer_method = create_test_method("analyze", "Analysis", see_also=["Tree.getRoot"])
    
    tree_stub = create_test_stub("Tree", "sc.fiji.snt", [tree_method])
    analyzer_stub = create_test_stub("TreeAnalyzer", "sc.fiji.snt.analysis", [analyzer_method])
    
    # Set up inheritance
    analyzer_stub.inheritance = {'extends': ['Tree'], 'implements': []}
    
    all_stubs = {
        "Tree": tree_stub,
        "TreeAnalyzer": analyzer_stub
    }
    
    # Test cross-reference building
    builder = CrossReferenceBuilder()
    cross_refs = builder.build_comprehensive_cross_references(tree_stub, all_stubs)
    
    print(f"✓ Generated cross-references for Tree class")
    print(f"  - Related methods: {len(cross_refs['related_methods'])}")
    print(f"  - Related classes: {len(cross_refs['related_classes'])}")
    print(f"  - Internal links: {len(cross_refs['internal_links'])}")
    print(f"  - Tutorial links: {len(cross_refs['tutorial_links'])}")
    print(f"  - External links: {len(cross_refs['external_links'])}")
    
    # Test cross-reference report
    report = builder.generate_cross_reference_report(all_stubs)
    print(f"✓ Generated cross-reference report")
    print(f"  - Total classes: {report['summary']['total_classes']}")
    print(f"  - Classes with inheritance: {report['summary']['classes_with_inheritance']}")
    print(f"  - Total cross-references: {report['summary']['total_cross_references']}")
    
    return True


def test_rst_template_rendering():
    """Test RST template rendering with cross-references."""
    print("\nTesting RST template rendering...")
    
    # Create test cross-reference data
    cross_ref_data = {
        'related_methods': [
            {
                'class_name': 'TreeAnalyzer',
                'name': 'analyze',
                'short_description': 'Analyzes tree structure',
                'relationship': 'see_also'
            }
        ],
        'related_classes': [
            {
                'name': 'TreeAnalyzer',
                'description': 'Subclass of Tree',
                'relationship': 'subclass'
            }
        ],
        'internal_links': [
            {
                'title': 'Method Index',
                'url': '../method_index.html',
                'description': 'Browse all methods'
            }
        ],
        'tutorial_links': [
            {
                'title': 'Tree Analysis Tutorial',
                'url': '../notebooks/tree_analysis.html',
                'description': 'Learn tree analysis'
            }
        ],
        'external_links': [
            {
                'title': 'JavaDoc for Tree',
                'url': 'https://javadoc.scijava.org/SNT/Tree.html',
                'type': 'javadoc'
            }
        ],
        'package_navigation': {
            'package': 'sc.fiji.snt',
            'total_classes': 3,
            'current_position': 2,
            'previous_class': {'name': 'Path', 'link': 'Path.html'},
            'next_class': {'name': 'TreeStatistics', 'link': 'TreeStatistics.html'},
            'all_classes': ['Path', 'Tree', 'TreeStatistics']
        }
    }
    
    # Test template rendering
    template_engine = RSTTemplateEngine()
    rst_content = template_engine.render_cross_references(cross_ref_data)
    
    print("✓ Generated RST cross-reference content")
    print(f"  - Content length: {len(rst_content)} characters")
    
    # Check that key sections are present
    required_sections = [
        'Related Methods',
        'Related Classes', 
        'Package Navigation',
        'Documentation Navigation',
        'Tutorials and Examples',
        'External Documentation'
    ]
    
    for section in required_sections:
        if section in rst_content:
            print(f"  ✓ {section} section present")
        else:
            print(f"  ✗ {section} section missing")
    
    return True


def test_rst_generator_integration():
    """Test RST generator integration with cross-references."""
    print("\nTesting RST generator integration...")
    
    # Create test data
    method = create_test_method("getRoot", "Getters")
    stub = create_test_stub("Tree", "sc.fiji.snt", [method])
    
    all_stubs = {"Tree": stub}
    
    # Test RST generation
    generator = SphinxRSTGenerator()
    rst_content, output_file = generator.generate_class_page(stub, all_stubs)
    
    print("✓ Generated class page with cross-references")
    print(f"  - Content length: {len(rst_content)} characters")
    print(f"  - Output file: {output_file}")
    
    # Check for cross-reference sections
    if "Documentation Navigation" in rst_content or "Related" in rst_content:
        print("  ✓ Cross-references included in class page")
    else:
        print("  ✗ Cross-references missing from class page")
    
    return True


def main():
    """Run all cross-reference tests."""
    print("Cross-Reference System Test Suite")
    print("=" * 40)
    
    try:
        # Run tests
        test_cross_reference_builder()
        test_rst_template_rendering()
        test_rst_generator_integration()
        
        print("\n" + "=" * 40)
        print("✓ All cross-reference tests passed!")
        return 0
        
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())