from src.core.tts import Tts
import time

print("Testing TTS...")
print("1. Testing Vietnamese...")
Tts.play_sound("Xin chào, đây là test tiếng Việt", "vi")
time.sleep(3)

print("2. Testing English...")
Tts.play_sound("Hello, this is an English test", "en")
time.sleep(3)

print("3. Testing login success message...")
Tts.play_sound("Bạn đã đăng nhập thành công!", "vi")
time.sleep(3)

print("Test completed!")
