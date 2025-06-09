# GEMINI VS STT
# from src.core.gemini import Gemini
# from src.core.stt import Stt

# stt = Stt()
# stt.load_model()
# full_text = stt.transcribe("./src/utils/audio/qn_audio.m4a")
# print(f"Nội dung file âm thanh: {full_text}" )
# print(Gemini.get_response(full_text, "Bạn là người Quảng Nam chuyên nói giọng địa phương, hãy dịch câu nói của người này giúp tôi"))

from src.core.audio_recorder import AudioRecorder
from src.core.stt import Stt
import time

stt = Stt()
stt.load_model()

while True:
    record_text = AudioRecorder.get_record_text()
    print(record_text)
    if(record_text == "Tạm dừng"):
        break
    print("--------------------------------")
    time.sleep(1)
