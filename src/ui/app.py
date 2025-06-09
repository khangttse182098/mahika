from typing import Dict
import customtkinter as ctk

from src.ui.file_list import FileList
from src.ui.login import LoginWindow
from src.ui.word_list import WordList
from src.utils.enums.page_name import PageName

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.focus_set()
        self.pages: Dict[str, ctk.CTkBaseClass] = {
            PageName.LOGIN: LoginWindow(self),
            PageName.FILE_LIST: FileList(self),
            PageName.WORD_LIST: WordList(self)
        }
        self.current_page: ctk.CTkBaseClass  = None

        self.show_page(PageName.LOGIN)
 
    def show_page(self, name: str):
        if self.current_page:
            self.current_page.pack_forget()
        
        page = self.pages[name]
        page.pack(fill="both", expand=True)
        self.current_page = page
