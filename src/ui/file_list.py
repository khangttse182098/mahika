import os
import threading
from typing import List
import customtkinter as ctk
from src.core.stt import Stt

from src.core.tts import Tts
import test
class FileTile(ctk.CTkFrame):
    def __init__(self, master, fg="#FFFFFF", is_normal=True, name="", is_hovered=False):
        super().__init__(master, width=100, height=100, fg_color=fg)
        self.is_hovered = is_hovered
        self.name = name
        if is_normal == False:
            plusBtn = ctk.CTkLabel(self, text="+", font=ctk.CTkFont(size=50))
            plusBtn.place(relx=0.5, rely=0.5, anchor="center")
        else:
            nameLabel = ctk.CTkLabel(self, text=name, font=ctk.CTkFont(size=10, weight="bold"), text_color="#000000")
            nameLabel.place(relx=0.5, rely=0.5, anchor="center")
    
    def set_hovered(self):
        if self.is_hovered:
            self.configure(border_width=0)
            self.is_hovered = False
        else:
            self.configure(border_color="#2433BB", border_width=2) 
            self.is_hovered = True

class FileList(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#E5E5E5", width=1000, height=500)
        self.app = master
        self.file_list: List[FileTile] = []
        self.read_folder()
        self.total_file = len(self.file_list)
        self.hovered_position = -1
        self.max_col = 4
        self.after(100, self.focus_set)
        col = 1
        row = 0 

        # plus tile
        FileTile(self, fg="#0C34FA", is_normal=False).grid(row=0, column=0, padx=10, pady=10)

        # loop through
        for tile in self.file_list:
            if col == self.max_col:
                col = 0 
                row += 1
            tile.grid(row=row, column=col, padx=10, pady=10)
            col += 1    

    def change_hovered_tile(self, event, is_forward):
        if self.hovered_position > -1:
            self.file_list[self.hovered_position].set_hovered()
        match is_forward:
            case True:
                self.hovered_position = min(self.hovered_position + 1, self.total_file - 1)
            case False:
                self.hovered_position = max(self.hovered_position - 1, 0)
        hovered_tile = self.file_list[self.hovered_position]
        hovered_tile.set_hovered()

        # Play file name
        threading.Thread(target=lambda: Tts.play_sound(hovered_tile.name), daemon=True).start() 
    
    def navigate_word_list(self, event):
        file_name = self.file_list[self.hovered_position]
        full_path = os.path.join("D:/mahika", file_name.name)
        content: str
        if os.path.isfile(full_path):
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"content: {content}")
            except Exception as e:
                print(f"Error reading: {e}") 
    
    def read_folder(self):
        if not os.path.isdir('D:/mahika'):
            print("invalid directory")
        else:
            for entry in os.listdir('D:/mahika'):
                file_tile = FileTile(self, name=entry)
                self.file_list.append(file_tile)
    
    def bind_keys(self): 
        self.master.bind_all("<Key-l>", lambda event : self.change_hovered_tile(event, is_forward=True))
        self.master.bind_all("<Key-h>", lambda event : self.change_hovered_tile(event, is_forward=False))
        self.master.bind_all("<Key-j>", lambda event : self.navigate_word_list(event))
    
    def unbind_keys(self):
        self.master.unbind_all("<Key-l>")
        self.master.unbind_all("<Key-h>")
        self.master.unbind_all("<Key-j>")
