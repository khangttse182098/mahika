import time
import customtkinter as ctk
from src.core.user_service import UserService
from src.core.tts import Tts
from src.utils.system_msg import SysMsg

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.userService = UserService()
        self.title("Login - English Learning Assistant")
        self.geometry("400x300") 
        
        # Giao diện đăng nhập
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)
        
        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = self.userService.login(username=username, password=password)
        status = result['status']
        Tts().playSound(result['message'], "vi")
        if status == 200:
            self.withdraw()