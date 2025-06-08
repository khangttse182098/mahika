from src.core.gemini import Gemini
from src.core.stt import Stt

stt = Stt()
stt.load_model()
full_text = stt.transcribe("./src/utils/audio/qn_audio.m4a")
print(f"Nội dung file âm thanh: {full_text}" )
print(Gemini.get_response(full_text, "Bạn là người Quảng Nam chuyên nói giọng địa phương, hãy dịch câu nói của người này giúp tôi"))