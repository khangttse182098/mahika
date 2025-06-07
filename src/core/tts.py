from gtts import gTTS
from playsound import playsound
import tempfile
import os

class Tts():
    @staticmethod
    def play_sound(msg, lang="vi"):
        tts = gTTS(msg, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file: 
            temp_file_path = temp_file.name
            tts.save(temp_file_path)
        
        playsound(temp_file_path)

        os.remove(temp_file_path)