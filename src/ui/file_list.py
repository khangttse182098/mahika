import threading
from typing import List
import customtkinter as ctk
from src.core.stt import Stt

from src.core.tts import Tts
class FileTile(ctk.CTkFrame):
    def __init__(self, master, fg="#FFFFFF", is_normal=True, name="", date="", is_hovered=False):
        self.is_hovered = is_hovered
        self.name = name
        self.date = date
        super().__init__(master, width=100, height=100, fg_color=fg)
        if is_normal == False:
            plusBtn = ctk.CTkLabel(self, text="+", font=ctk.CTkFont(size=50))
            plusBtn.place(relx=0.5, rely=0.5, anchor="center")
        else:
            nameLabel = ctk.CTkLabel(self, text=name, font=ctk.CTkFont(size=10, weight="bold"), text_color="#000000")
            nameLabel.place(relx=0.5, rely=0.5, anchor="center")
            timeLabel = ctk.CTkLabel(self, text=date, font=ctk.CTkFont(size=8), text_color="#000000")
            timeLabel.place(relx=0.5, rely=0.7, anchor="center")
    
    def set_hovered(self):
        if self.is_hovered:
            self.configure(border_width=0)
            self.is_hovered = False
        else:
            self.configure(border_color="#2433BB", border_width=2) 
            self.is_hovered = True

class FileList(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#E5E5E5")
        self.title("Trang tài liệu")
        self.tile_list: List[FileTile] = []
        self.bind("<Key-l>", lambda event : self.changeHoveredTile(event, is_forward=True))
        self.bind("<Key-h>", lambda event : self.changeHoveredTile(event, is_forward=False))
        self.geometry("1000x500")
        self.hovered_position = 0
        self.max_col = 4
        col = 1
        row = 0 

        # plus tile
        FileTile(self, fg="#0C34FA", is_normal=False).grid(row=0, column=0, padx=10, pady=10)

        # loop through
        for i in range(10):
            if col == self.max_col:
                col = 0 
                row += 1

            file_tile = FileTile(self, name="Untitled", date="06/06/2025")

            # add to tileList
            self.tile_list.append(file_tile)
            file_tile.grid(row=row, column=col, padx=10, pady=10)
            col += 1 
        
        self.tile_list[0].set_hovered()
        
    
    def changeHoveredTile(self, event, is_forward):
        self.tile_list[self.hovered_position].set_hovered()
        match is_forward:
            case True:
                self.hovered_position += 1
            case False:
                self.hovered_position -= 1 if self.hovered_position > 0 else 0
        hovered_tile = self.tile_list[self.hovered_position]
        hovered_tile.set_hovered()
        # Play file name
        threading.Thread(target=lambda: Tts.play_sound(hovered_tile.name, lang="en"), daemon=True).start()

