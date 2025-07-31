#!/usr/bin/env python3
"""
Test script to verify Whisper model loading
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.stt import Stt

def test_whisper_loading():
    print("Testing Whisper model loading...")
    
    try:
        # Test loading the model
        print("Loading Whisper model...")
        Stt.load_model("base")  # Use base model for faster loading
        print("✓ Whisper model loaded successfully!")
        
        # Test getting the model
        model = Stt.get_model()
        if model:
            print("✓ Model retrieved successfully!")
        else:
            print("✗ Failed to retrieve model")
            
        return True
        
    except Exception as e:
        print(f"✗ Error loading Whisper model: {e}")
        return False

if __name__ == "__main__":
    success = test_whisper_loading()
    if success:
        print("\nWhisper model test completed successfully!")
    else:
        print("\nWhisper model test failed!")
    
    input("Press Enter to exit...")
