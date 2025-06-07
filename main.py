import threading
import customtkinter as ctk
from src.core.tts import Tts
from src.ui.login import LoginWindow
from src.utils.system_msg import SysMsg
from src.ui.file_list import FileList

def play_welcome_sound():
    Tts().play_sound(SysMsg.WELCOME_MSG.value)

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # app = LoginWindow()
    # app.after(0, lambda: threading.Thread(target=play_welcome_sound, daemon=True).start())
    # app.mainloop()

    app = FileList()
    app.mainloop()

if __name__ == "__main__":
    main()