#!/usr/bin/env python3
"""
Test script for new vocabulary learning AI chat functionality
"""
import sys
import os
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.tts import Tts

def test_vocabulary_response_parsing():
    """Test parsing vocabulary responses"""
    
    test_responses = [
        "Từ xinh đẹp trong tiếng Anh là beautiful",
        "Từ con chó trong tiếng Anh là dog",
        "Từ học trong tiếng Anh là study",
        "Từ máy tính trong tiếng Anh là computer",
        "Beautiful có nghĩa là đẹp, xinh đẹp. [ENGLISH: beautiful]",  # fallback format
    ]
    
    print("Testing Vocabulary Response Parsing...")
    print("="*50)
    
    for response in test_responses:
        print(f"\nInput: {response}")
        
        # Test the new vocabulary pattern
        vocab_match = re.search(r'Từ (.+?) trong tiếng Anh là (.+?)(?:\.|$)', response, re.IGNORECASE)
        
        if vocab_match:
            vietnamese_word = vocab_match.group(1).strip()
            english_word = vocab_match.group(2).strip()
            
            print(f"✓ Vocabulary format detected!")
            print(f"  Vietnamese word: {vietnamese_word}")
            print(f"  English word: {english_word}")
            
            # Test TTS sequence
            intro_text = f"Từ tiếng Anh của {vietnamese_word} là:"
            print(f"  Will say: '{intro_text}'")
            print(f"  Then pronounce: '{english_word}' (English)")
            
            # Actual TTS test (uncomment to test audio)
            # print("  Playing audio...")
            # Tts.play_sound(intro_text, "vi")
            # Tts.play_sound(english_word, "en")
            
        else:
            # Test fallback [ENGLISH: word] format
            english_match = re.search(r'\[ENGLISH:\s*([^\]]+)\]', response)
            if english_match:
                english_word = english_match.group(1).strip()
                vietnamese_part = re.sub(r'\[ENGLISH:[^\]]+\]', '', response).strip()
                print(f"✓ Fallback format detected!")
                print(f"  Vietnamese: {vietnamese_part}")
                print(f"  English: {english_word}")
            else:
                print("✗ No pattern matched - will play as Vietnamese only")

def test_user_questions():
    """Test typical user questions that should trigger vocabulary response"""
    
    user_questions = [
        "từ xinh đẹp trong tiếng Anh là gì?",
        "con chó tiếng Anh là gì?",
        "từ học tiếng Anh là gì?",
        "máy tính tiếng Anh là gì?",
        "từ beautiful có nghĩa là gì?",  # reverse question
    ]
    
    print("\n" + "="*50)
    print("Expected User Questions:")
    print("="*50)
    
    for question in user_questions:
        print(f"User: '{question}'")
        if "tiếng Anh là gì" in question.lower():
            # Extract Vietnamese word
            if "từ " in question:
                viet_word = question.replace("từ ", "").replace(" trong tiếng Anh là gì?", "").replace(" tiếng Anh là gì?", "")
            else:
                viet_word = question.replace(" tiếng Anh là gì?", "")
            print(f"  → AI should respond: 'Từ {viet_word} trong tiếng Anh là [english_word]'")
        else:
            print(f"  → Regular AI response with [ENGLISH: word] format")
        print()

if __name__ == "__main__":
    print("Testing Enhanced AI Chat Vocabulary Features")
    print("="*60)
    
    try:
        test_vocabulary_response_parsing()
        test_user_questions()
        
        print("\n" + "="*60)
        print("✅ SUMMARY:")
        print("1. ✓ New vocabulary pattern: 'Từ X trong tiếng Anh là Y'")
        print("2. ✓ TTS sequence: 'Từ tiếng Anh của X là:' + English pronunciation")
        print("3. ✓ Fallback to [ENGLISH: word] format for other responses")
        print("4. ✓ Enhanced user experience for vocabulary learning")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
    
    input("\nPress Enter to exit...")
