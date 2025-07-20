#!/usr/bin/env python3
"""
Test script để kiểm tra tính năng TTS giọng tiếng Anh cho từ vựng
"""

import sys
import os
import time

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core.tts import Tts

def test_english_pronunciation():
    print("🔊 Testing English pronunciation for words...")
    print("Initializing TTS system...")
    
    # Initialize TTS
    Tts._initialize_pygame()
    
    # Test words với giọng tiếng Anh
    test_words = ["apple", "banana", "computer", "language", "pronunciation"]
    
    for word in test_words:
        print(f"📢 Playing pronunciation of: {word}")
        Tts.play_sound(word, "en")  # Sử dụng giọng tiếng Anh
        time.sleep(3)  # Đợi 3 giây giữa các từ
    
    print("✅ English pronunciation test completed!")
    print("🎯 Nếu bạn nghe được phát âm tiếng Anh chuẩn, tính năng đã hoạt động!")

def test_vietnamese_instruction():
    print("\n🔊 Testing Vietnamese instructions...")
    instruction = "Bạn vừa nghe phát âm tiếng Anh. Nhấn R để nghe định nghĩa, P để nghe lại phát âm"
    print("📢 Playing Vietnamese instruction...")
    Tts.play_sound(instruction, "vi")  # Hướng dẫn bằng tiếng Việt
    time.sleep(5)
    print("✅ Vietnamese instruction test completed!")

if __name__ == "__main__":
    print("=" * 50)
    print("🎵 TTS English Pronunciation Test")
    print("=" * 50)
    
    try:
        test_english_pronunciation()
        test_vietnamese_instruction()
        
        print("\n✨ All tests completed successfully!")
        print("🎧 Recommendation: Test in the actual app by:")
        print("  1. Login → File List → Word List → Word Detail")
        print("  2. Listen for English pronunciation when entering word detail")
        print("  3. Press P to repeat English pronunciation")
        print("  4. Press R to hear Vietnamese definition")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
