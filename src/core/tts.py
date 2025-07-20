from gtts import gTTS
import tempfile
import os
import pygame
import threading
import hashlib
from pathlib import Path

class Tts:
    _current_channel = None
    _lock = threading.Lock()
    _pygame_initialized = False
    _cache_dir = None
    
    @classmethod
    def _initialize_pygame(cls):
        """Initialize pygame mixer once"""
        if not cls._pygame_initialized:
            pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
            pygame.mixer.init()
            cls._pygame_initialized = True
    
    @classmethod
    def _get_cache_dir(cls):
        """Get or create cache directory"""
        if cls._cache_dir is None:
            cls._cache_dir = Path(tempfile.gettempdir()) / "mahika_tts_cache"
            cls._cache_dir.mkdir(exist_ok=True)
        return cls._cache_dir
    
    @classmethod
    def _get_cache_filename(cls, msg, lang):
        """Generate cache filename based on message and language"""
        text_hash = hashlib.md5(f"{msg}_{lang}".encode()).hexdigest()
        return cls._get_cache_dir() / f"{text_hash}.mp3"

    @staticmethod
    def play_sound(msg, lang="vi"):
        # Initialize pygame if not done
        Tts._initialize_pygame()
        
        # Check cache first
        cache_file = Tts._get_cache_filename(msg, lang)
        
        if not cache_file.exists():
            # Generate TTS and cache it
            try:
                tts = gTTS(msg, lang=lang)
                tts.save(str(cache_file))
            except Exception as e:
                print(f"TTS Error: {e}")
                return

        def _play():
            with Tts._lock:
                try:
                    # Stop current playback
                    if Tts._current_channel is not None:
                        pygame.mixer.music.stop()
                    
                    # Load and play
                    pygame.mixer.music.load(str(cache_file))
                    pygame.mixer.music.play()
                    Tts._current_channel = pygame.mixer.music
                except Exception as e:
                    print(f"Playback Error: {e}")

        threading.Thread(target=_play, daemon=True).start()
    
    @staticmethod
    def pre_cache_common_words():
        """Pre-cache common English words to speed up word list navigation"""
        common_words = [
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by",
            "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did",
            "will", "would", "could", "should", "can", "may", "might", "must", "shall",
            "this", "that", "these", "those", "here", "there", "where", "when", "how", "why",
            "good", "bad", "big", "small", "new", "old", "first", "last", "long", "short"
        ]
        
        def cache_words():
            for word in common_words:
                cache_file = Tts._get_cache_filename(word, "en")
                if not cache_file.exists():
                    try:
                        tts = gTTS(word, lang="en")
                        tts.save(str(cache_file))
                    except Exception as e:
                        print(f"Pre-cache error for '{word}': {e}")
        
        # Run pre-caching in background
        threading.Thread(target=cache_words, daemon=True).start()
    
    @staticmethod
    def stop_current_playback():
        """Stop current TTS playback"""
        with Tts._lock:
            if Tts._current_channel is not None:
                pygame.mixer.music.stop()