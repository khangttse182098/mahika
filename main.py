import threading
import customtkinter as ctk
from src.core.tts import Tts
from src.ui.app import App
from src.utils.enums.system_msg import SysMsg
from src.core.stt import Stt
from src.core.audio_recorder import AudioRecorder
from src.core.dictionary import Dictionary

# def load_stt_model():
#    Stt.load_model()

def play_welcome_sound():
    Tts().play_sound(SysMsg.WELCOME_MSG.value)


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # app = LoginWindow()
    # app.after(0, lambda: threading.Thread(target=play_welcome_sound, daemon=True).start())
    # app.mainloop()

    # app = FileList()
    # # Load the Whisper Model after the app run
    # app.after(0, lambda: threading.Thread(target=load_stt_model, daemon=True).start())

    # app = WordList(content="This is a test")
    app = App()
    Dictionary.viToEn("Cá")
    app.mainloop()

if __name__ == "__main__":
    main()