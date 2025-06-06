import customtkinter as ctk
from src.core.tts import Tts
from src.ui.login import LoginWindow
from src.utils.system_msg import SysMsg

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = LoginWindow()
    app.update()
    Tts().playSound(SysMsg.WELCOME_MSG.value) 
    app.mainloop()

if __name__ == "__main__":
    main()