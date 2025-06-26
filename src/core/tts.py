from gtts import gTTS
import tempfile
import os
import pygame
import threading

class Tts:
    _current_channel = None
    _lock = threading.Lock()

    @staticmethod
    def play_sound(msg, lang="vi"):
        tts = gTTS(msg, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_path = temp_file.name
            tts.save(temp_path)

        def _play():
            pygame.mixer.init()
            with Tts._lock:
                if Tts._current_channel is not None:
                    Tts._current_channel.stop()
                pygame.mixer.music.load(temp_path)
                pygame.mixer.music.play()
                Tts._current_channel = pygame.mixer.music

            while pygame.mixer.music.get_busy():
                continue

            # os.remove(temp_path)

        threading.Thread(target=_play, daemon=True).start()
