import threading
import sys
import os
import customtkinter as ctk

# Add error handling for executable distribution
if hasattr(sys, '_MEIPASS'):
    # Running as exe - add the bundled directory to path
    os.chdir(sys._MEIPASS)
else:
    # Running as script - use current directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    from src.core.tts import Tts
    from src.ui.app import App
    from src.utils.enums.system_msg import SysMsg
    from src.core.stt import Stt
    from src.core.audio_recorder import AudioRecorder
    from src.core.dictionary import Dictionary
except ImportError as e:
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Import Error", f"Failed to import required modules: {e}")
    sys.exit(1)

# def load_stt_model():
#    Stt.load_model()

# def play_welcome_sound():
#     Tts().play_sound(SysMsg.WELCOME_MSG.value)


def main():
    try:
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
        app.mainloop()
        
    except Exception as e:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Application Error", f"Application failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()