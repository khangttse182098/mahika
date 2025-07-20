#!/usr/bin/env python3
"""
Test script for word_detail functionality
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core.dictionary import Dictionary

def test_dictionary():
    print("Testing Dictionary.enToVi...")
    
    # Test with a simple word
    result = Dictionary.enToVi("apple")
    print(f"Result for 'apple': {result}")
    
    if result:
        print("✓ Dictionary returned data")
        print(f"Text: {result.get('text', 'N/A')}")
        print(f"MeaningArray length: {len(result.get('meaningArray', []))}")
    else:
        print("✗ Dictionary returned None")

if __name__ == "__main__":
    test_dictionary()
