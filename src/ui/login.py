import customtkinter as ctk
import threading
from src.core.user_service import UserService
from src.core.tts import Tts
from src.core.stt import Stt
from src.utils.enums.page_name import PageName

class LoginWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=400, height=300)
        self.app = master
        self.userService = UserService()
          # Giao diện đăng nhập
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)
        
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="Email")
        self.email_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        
        # Status label for model loading
        self.status_label = ctk.CTkLabel(self.frame, text="", font=ctk.CTkFont(size=10))
        self.status_label.pack(pady=5)
        
        # Bind Enter key to login function
        self.email_entry.bind("<Return>", lambda event: self.login())
        self.password_entry.bind("<Return>", lambda event: self.login())
        self.bind("<Return>", lambda event: self.login())
        
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        result = self.userService.login(email=email, password=password)
        status = result['status']
        
        if status == 200:
            # Show page first before TTS to avoid UI blocking
            self.app.show_page(PageName.FILE_LIST.value)
            # Load Whisper model in background after successful login
            self.load_whisper_model()
            # Play TTS in background thread
            threading.Thread(target=lambda: Tts().play_sound(result['message'], "vi"), daemon=True).start()
        else:
            # For error messages, play TTS immediately (blocking is acceptable for errors)
            threading.Thread(target=lambda: Tts().play_sound(result['message'], "vi"), daemon=True).start()
    
    def load_whisper_model(self):
        """Load Whisper model in background thread to improve AI chat performance"""
        def load_model_thread():
            try:
                # Update status on UI thread safely
                self.after(0, lambda: self.status_label.configure(text="Đang tải model AI..."))
                
                Stt.load_model("base")  # Use smaller model for faster loading, can change to "large-v3" if needed
                
                # Update status on UI thread safely
                self.after(0, lambda: self.status_label.configure(text="Model AI đã sẵn sàng!"))
                print("Whisper model loaded successfully in background")
                
                # Clear status after 3 seconds
                self.after(3000, lambda: self.status_label.configure(text=""))
                
            except Exception as e:
                print(f"Error loading Whisper model: {e}")
                self.after(0, lambda: self.status_label.configure(text="Lỗi tải model AI"))
        
        # Start loading in background thread so it doesn't block UI
        threading.Thread(target=load_model_thread, daemon=True).start()
    
    def bind_keys(self):
        # No specific keys for login page, but global navigation will be handled by App
        pass
    
    def unbind_keys(self):
        # No specific keys to unbind for login page
        pass