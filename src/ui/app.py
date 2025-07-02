from typing import Dict
import customtkinter as ctk

from src.ui.file_list import FileList
from src.ui.login import LoginWindow
from src.ui.word_list import WordList
from src.utils.enums.page_name import PageName
from src.ui.word_detail import WordDetail

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.focus_set()
        self.pages: Dict[str, ctk.CTkBaseClass] = {
            PageName.LOGIN: LoginWindow(self),
            PageName.FILE_LIST: FileList(self),
            PageName.WORD_LIST: WordList(self),
            PageName.WORD_DETAIL: WordDetail(self)
        }
        self.current_page: ctk.CTkBaseClass = None

        # show login as first page
        self.show_page(PageName.LOGIN)
 
    def show_page(self, name: str, content=""):
        if self.current_page:
            # unbind previous page bind key
            if hasattr(self.current_page, "unbind_keys"):
                self.current_page.unbind_keys()
            
            # hide the current page
            self.current_page.pack_forget()
        
        new_page = self.pages[name]
        
        # Update content if the page supports it and content is provided
        if content and hasattr(new_page, "update_content"):
            new_page.update_content(content)

        # Bind new page with key if had
        if hasattr(new_page, "bind_keys"):
            new_page.bind_keys()
        
        # show the page to screen
        new_page.pack(fill="both", expand=True)

        self.title(name.value)
        self.current_page = new_page
