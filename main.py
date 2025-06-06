import customtkinter as ctk
from src.ui.login import LoginWindow

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = LoginWindow()
    app.mainloop()

if __name__ == "__main__":
    main()