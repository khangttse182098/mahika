import customtkinter as ctk
class FileTile(ctk.CTkFrame):
    def __init__(self, master, fg="#FFFFFF", isNormal=True, name="", date="", isHovered=False):
        self.isHovered = isHovered
        super().__init__(master, width=100, height=100, fg_color=fg)
        if isNormal == False:
            plusBtn = ctk.CTkLabel(self, text="+", font=ctk.CTkFont(size=50))
            plusBtn.place(relx=0.5, rely=0.5, anchor="center")
        else:
            nameLabel = ctk.CTkLabel(self, text=name, font=ctk.CTkFont(size=10, weight="bold"), text_color="#000000")
            nameLabel.place(relx=0.5, rely=0.5, anchor="center")
            timeLabel = ctk.CTkLabel(self, text=date, font=ctk.CTkFont(size=8), text_color="#000000")
            timeLabel.place(relx=0.5, rely=0.7, anchor="center")
    
    def set_hovered(self):
        if self.isHovered:
            self.configure(border_width=0)
            self.isHovered = False
        else:
            self.configure(border_color="#2433BB", border_width=2) 
            self.isHovered = True

class FileList(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#E5E5E5")
        self.title("Trang tài liệu")
        self.tileList = []
        self.bind("<Key-l>", self.changeHoveredTile)
        self.geometry("1000x500")
        self.hoveredPosition = 0
        self.max_col = 4
        col = 1
        row = 0
        

        # plus tile
        FileTile(self, fg="#0C34FA", isNormal=False).grid(row=0, column=0, padx=10, pady=10)

        # loop through
        for i in range(10):
            if col == self.max_col:
                col = 0 
                row += 1

            fileTile = FileTile(self, name="Untitled", date="06/06/2025")

            # add to tileList
            self.tileList.append(fileTile)
            fileTile.grid(row=row, column=col, padx=10, pady=10)
            col += 1 
        
        self.tileList[0].set_hovered()
        
    
    def changeHoveredTile(self, event):
        self.tileList[self.hoveredPosition].set_hovered()
        self.hoveredPosition += 1
        print(f"pos: {self.hoveredPosition}")
        self.tileList[self.hoveredPosition].set_hovered()
