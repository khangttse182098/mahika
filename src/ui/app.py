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
        
        print("Starting App initialization...")
        
        # Initialize TTS and start pre-caching common words
        try:
            print("Initializing TTS...")
            Tts._initialize_pygame()
            Tts.pre_cache_common_words()
            print("TTS initialized successfully")
        except Exception as e:
            print(f"TTS initialization error: {e}")
        
        # Initialize pages with error handling
        self.pages: Dict[str, ctk.CTkBaseClass] = {}
        
        try:
            print("Creating LoginWindow...")
            login_page = LoginWindow(self)
            if login_page is None:
                print("ERROR: LoginWindow constructor returned None!")
            else:
                self.pages[PageName.LOGIN.value] = login_page
                print(f"LoginWindow created successfully, key: '{PageName.LOGIN.value}'")
        except Exception as e:
            print(f"Error creating LoginWindow: {e}")
            raise
            
        try:
            print("Creating FileList...")
            file_list_page = FileList(self)
            if file_list_page is None:
                print("ERROR: FileList constructor returned None!")
            else:
                self.pages[PageName.FILE_LIST.value] = file_list_page
                print(f"FileList created successfully, key: '{PageName.FILE_LIST.value}'")
        except Exception as e:
            print(f"Error creating FileList: {e}")
            raise
            
        try:
            print("Creating WordList...")
            word_list_page = WordList(self)
            if word_list_page is None:
                print("ERROR: WordList constructor returned None!")
            else:
                self.pages[PageName.WORD_LIST.value] = word_list_page
                print(f"WordList created successfully, key: '{PageName.WORD_LIST.value}'")
        except Exception as e:
            print(f"Error creating WordList: {e}")
            raise
            
        try:
            print("Creating WordDetail...")
            word_detail_page = WordDetail(self)
            if word_detail_page is None:
                print("ERROR: WordDetail constructor returned None!")
            else:
                self.pages[PageName.WORD_DETAIL.value] = word_detail_page
                print(f"WordDetail created successfully, key: '{PageName.WORD_DETAIL.value}'")
        except Exception as e:
            print(f"Error creating WordDetail: {e}")
            raise
            
        print(f"All pages created. Page keys: {list(self.pages.keys())}")
        
        self.current_page: ctk.CTkBaseClass = None
        self.current_page_name: str = None
        self.page_history = []  # Stack để lưu lịch sử trang
        self.page_forward_stack = []  # Stack cho forward navigation
          # show login as first page
        try:
            print(f"Showing initial page: '{PageName.LOGIN.value}'")
            print(f"PageName.LOGIN.value type: {type(PageName.LOGIN.value)}")
            print(f"Available page keys: {list(self.pages.keys())}")
            self.show_page(PageName.LOGIN.value)
            print("Initial page shown successfully")
        except Exception as e:
            print(f"Error showing initial page: {e}")
            import traceback
            traceback.print_exc()
            raise

    def show_page(self, name: str, content="", add_to_history=True):
        # Debug output to file
        debug_file = "e:/mahika_debug.txt"
        try:
            with open(debug_file, "a") as f:
                f.write(f"show_page called with name={repr(name)}, type={type(name)}\n")
        except:
            pass
            
        # Convert enum to string value if needed
        if hasattr(name, 'value'):
            name = name.value
        elif name is None:
            print("Error: name parameter is None")
            try:
                with open(debug_file, "a") as f:
                    f.write("ERROR: name parameter is None, returning\n")
            except:
                pass
            return
        elif not isinstance(name, str):
            name = str(name)
            
        try:
            with open(debug_file, "a") as f:
                f.write(f"After processing: name={repr(name)}\n")
        except:
            pass
            
        # Check if the page exists
        if name not in self.pages:
            try:
                with open(debug_file, "a") as f:
                    f.write(f"ERROR: Page '{name}' not found in pages. Available: {list(self.pages.keys())}\n")
            except:
                pass
            print(f"Error: Page '{name}' not found")
            return
            
        # Add current page to history before switching (if not already navigating back/forward)
        if add_to_history and self.current_page_name and self.current_page_name != name:
            # Only add valid (non-None) page names to history
            if self.current_page_name is not None:
                self.page_history.append(self.current_page_name)
                # Clear forward stack when navigating to a new page
                self.page_forward_stack.clear()
                try:
                    print(f"Added {str(self.current_page_name)} to history. History: {[str(page) for page in self.page_history]}")
                except:
                    print("Added page to history")
        
        try:
            print(f"Showing page: {str(name)}")
        except:
            print("Showing page")
        
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

        # Set title safely - this might be causing the issue
        try:
            if name and isinstance(name, str):
                self.title(name)
            else:
                self.title("Mahika Dictionary")
        except Exception as e:
            try:
                with open(debug_file, "a") as f:
                    f.write(f"Error setting title: {e}\n")
            except:
                pass
            try:
                self.title("Mahika Dictionary")
            except:
                pass
            
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
            try:
                print(f"Navigating back from {str(self.current_page_name)} to previous page")
                print(f"History before: {[str(page) for page in self.page_history]}")
            except:
                print("Navigating back to previous page")
            
            # Add current page to forward stack
            if self.current_page_name:
                self.page_forward_stack.append(self.current_page_name)
            
            # Get previous page from history
            previous_page = self.page_history.pop()
            if previous_page is None:
                print("Error: previous_page is None, cannot navigate back")
                return
            try:
                print(f"Going back to: {str(previous_page)}")
            except:
                print("Going back")
            self.show_page(previous_page, add_to_history=False)
        else:
            print("No page history available for back navigation")
    
    def navigate_forward(self):
        if self.page_forward_stack:
            try:
                print(f"Navigating forward from {str(self.current_page_name)}")
                print(f"Forward stack before: {[str(page) for page in self.page_forward_stack]}")
            except:
                print("Navigating forward")
            
            # Add current page to history
            if self.current_page_name:
                self.page_history.append(self.current_page_name)
            
            # Get next page from forward stack
            next_page = self.page_forward_stack.pop()
            if next_page is None:
                print("Error: next_page is None, cannot navigate forward")
                return
            try:
                print(f"Going forward to: {str(next_page)}")
            except:
                print("Going forward")
            self.show_page(next_page, add_to_history=False)
        else:
            print("No forward pages available")
    def get_navigation_status(self):
        """Get current navigation status for debugging"""
        try:
            return {
                "current_page": str(self.current_page_name) if self.current_page_name else "None",
                "history": [str(page) for page in self.page_history],
                "forward_stack": [str(page) for page in self.page_forward_stack],
                "can_go_back": len(self.page_history) > 0,
                "can_go_forward": len(self.page_forward_stack) > 0
            }
        except:
            return {
                "current_page": "Unknown",
                "history": [],
                "forward_stack": [],
                "can_go_back": False,
                "can_go_forward": False
            }
