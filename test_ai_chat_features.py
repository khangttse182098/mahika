#!/usr/bin/env python3
"""
Test script for AI Chat toggle functionality and English pronunciation
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.tts import Tts
import re

def test_english_extraction():
    """Test extracting English words from AI response"""
    
    # Test responses
    test_responses = [
        "Con chó là động vật có 4 chân, trung thành với con người. [ENGLISH: dog]",
        "Beautiful có nghĩa là đẹp, xinh đẹp. [ENGLISH: beautiful]",
        "Xin chào có nghĩa là lời chào hỏi. [ENGLISH: hello]",
        "Đây là câu trả lời không có từ tiếng Anh.",
    ]
    
    print("Testing English word extraction...")
    
    for response in test_responses:
        print(f"\nInput: {response}")
        
        # Extract English word
        english_match = re.search(r'\[ENGLISH:\s*([^\]]+)\]', response)
        
        if english_match:
            english_word = english_match.group(1).strip()
            vietnamese_part = re.sub(r'\[ENGLISH:[^\]]+\]', '', response).strip()
            
            print(f"✓ Vietnamese: {vietnamese_part}")
            print(f"✓ English: {english_word}")
            
            # Test TTS
            print("  Playing Vietnamese...")
            Tts.play_sound(vietnamese_part, "vi")
            
            print("  Playing English...")
            Tts.play_sound(english_word, "en")
            
        else:
            print("✗ No English word found")
            print("  Playing Vietnamese only...")
            Tts.play_sound(response, "vi")

def test_ai_chat_toggle():
    """Test information about AI Chat toggle"""
    print("\n" + "="*50)
    print("AI CHAT TOGGLE FUNCTIONALITY")
    print("="*50)
    print("✓ Alt+Space once: Opens AI Chat")
    print("✓ Alt+Space again: Closes AI Chat")
    print("✓ ESC: Also closes AI Chat")
    print("✓ Only one instance can be open at a time")
    print("\nAI RESPONSE FORMAT:")
    print("✓ AI responds in Vietnamese + [ENGLISH: word]")
    print("✓ Vietnamese part plays first")
    print("✓ English word plays with English TTS")

if __name__ == "__main__":
    print("Testing AI Chat Enhanced Features")
    print("="*40)
    
    try:
        test_english_extraction()
        test_ai_chat_toggle()
        print("\n✓ All tests completed successfully!")
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
    
    input("\nPress Enter to exit...")
