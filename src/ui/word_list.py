import customtkinter as ctk

class WordList(ctk.CTkFrame):
    def __init__(self, master, content="Test phát"):
        super().__init__(master, fg_color="#E5E5E5", width=1000, height=500)
        self.content = ctk.CTkLabel(self, text=content, font=ctk.CTkFont(size=10, weight="bold"), text_color="#000000")
        self.content.pack()