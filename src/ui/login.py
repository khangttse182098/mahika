import customtkinter as ctk
from src.core.user_service import UserService
from src.core.tts import Tts
from src.utils.enums.page_name import PageName

class LoginWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=400, height=300)
        self.app = master
        self.userService = UserService()
        
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
        Tts().play_sound(result['message'], "vi")
        if status == 200:
            self.app.show_page(PageName.FILE_LIST)
    
    def bind_keys(self):
        # No specific keys for login page, but global navigation will be handled by App
        pass
    
    def unbind_keys(self):
        # No specific keys to unbind for login page
        pass