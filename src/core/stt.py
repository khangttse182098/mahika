from faster_whisper import WhisperModel
# Singleton
class Stt:
    _instance = None
    _model = None
    _is_loaded = False
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) #Create new instance
        return cls._instance
    # Class method to make a function modify the attributes of a class
    @classmethod
    def load_model(cls, model_size="large-v3"):
        if cls._is_loaded == False:
            print(f"Loading Whisper Model with model size: {model_size}...")
            cls._model = WhisperModel(model_size, device="cpu", compute_type="int8")
            cls._is_loaded = True
            print("Loaded Whisper Model Successfuly")
    @classmethod
    def get_model(cls):
        if not cls._is_loaded:
            return cls.load_model()
        return cls._model
    @classmethod
    def transcribe(cls, audio_path):
        model = cls.get_model()
        segments, info = model.transcribe(audio_path, beam_size=1, language='vi')  # Unpack tuple
        full_text = ""
        for segment in segments:
            full_text += segment.text + " " 
        return full_text.strip()


