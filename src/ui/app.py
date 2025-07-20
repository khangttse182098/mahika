from typing import Dict
import customtkinter as ctk

from src.ui.file_list import FileList
from src.ui.login import LoginWindow
from src.ui.word_list import WordList
from src.utils.enums.page_name import PageName
from src.ui.word_detail import WordDetail
from src.core.tts import Tts

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.focus_set()
        
        # Initialize TTS and start pre-caching common words
        Tts._initialize_pygame()
        Tts.pre_cache_common_words()
        
        self.pages: Dict[str, ctk.CTkBaseClass] = {
            PageName.LOGIN: LoginWindow(self),
            PageName.FILE_LIST: FileList(self),
            PageName.WORD_LIST: WordList(self),
            PageName.WORD_DETAIL: WordDetail(self)
        }
        self.current_page: ctk.CTkBaseClass = None
        self.current_page_name: str = None
        self.page_history = []  # Stack để lưu lịch sử trang
        self.page_forward_stack = []  # Stack cho forward navigation

        # show login as first page
        self.show_page(PageName.LOGIN)
 
    def show_page(self, name: str, content="", add_to_history=True):
        # Add current page to history before switching (if not already navigating back/forward)
        if add_to_history and self.current_page_name and self.current_page_name != name:
            self.page_history.append(self.current_page_name)
            # Clear forward stack when navigating to a new page
            self.page_forward_stack.clear()
            print(f"Added {self.current_page_name.value} to history. History: {[page.value for page in self.page_history]}")
        
        print(f"Showing page: {name.value}")
        
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
        
        # Bind global navigation keys
        self.bind_global_navigation_keys()
        
        # show the page to screen
        new_page.pack(fill="both", expand=True)

        self.title(name.value)
        self.current_page = new_page
        self.current_page_name = name
    
    def bind_global_navigation_keys(self):
        # Unbind existing global navigation keys first to avoid duplicates
        self.unbind_all("<Shift-Key-H>")
        self.unbind_all("<Shift-Key-L>")
        
        # Bind global navigation keys for all pages
        self.bind_all("<Shift-Key-H>", lambda event: self.navigate_back())
        self.bind_all("<Shift-Key-L>", lambda event: self.navigate_forward())
    
    def navigate_back(self):
        if self.page_history:
            print(f"Navigating back from {self.current_page_name} to previous page")
            print(f"History before: {[page.value for page in self.page_history]}")
            
            # Add current page to forward stack
            if self.current_page_name:
                self.page_forward_stack.append(self.current_page_name)
            
            # Get previous page from history
            previous_page = self.page_history.pop()
            print(f"Going back to: {previous_page.value}")
            self.show_page(previous_page, add_to_history=False)
        else:
            print("No page history available for back navigation")
    
    def navigate_forward(self):
        if self.page_forward_stack:
            print(f"Navigating forward from {self.current_page_name}")
            print(f"Forward stack before: {[page.value for page in self.page_forward_stack]}")
            
            # Add current page to history
            if self.current_page_name:
                self.page_history.append(self.current_page_name)
            
            # Get next page from forward stack
            next_page = self.page_forward_stack.pop()
            print(f"Going forward to: {next_page.value}")
            self.show_page(next_page, add_to_history=False)
        else:
            print("No forward pages available")
    
    def get_navigation_status(self):
        """Get current navigation status for debugging"""
        return {
            "current_page": self.current_page_name.value if self.current_page_name else "None",
            "history": [page.value for page in self.page_history],
            "forward_stack": [page.value for page in self.page_forward_stack],
            "can_go_back": len(self.page_history) > 0,
            "can_go_forward": len(self.page_forward_stack) > 0
        }
