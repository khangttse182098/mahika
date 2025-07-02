import customtkinter as ctk
import textwrap

from src.utils.enums.page_name import PageName

class WordList(ctk.CTkFrame):
    def __init__(self, master, content="Test phát"):
        super().__init__(master, fg_color="#E5E5E5", width=1000, height=500)
        self.app = master
        
        # Use CTkTextbox for better text wrapping capabilities
        self.content_textbox = ctk.CTkTextbox(
            self, 
            width=900, 
            height=400,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#000000",
            fg_color="#FFFFFF",
            wrap="word"  # Enable word wrapping
        )
        self.content_textbox.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Configure text tags for highlighting
        self.setup_text_tags()
        
        # Choosen text for highlighting
        self.choosen_word_pos = ""
        self.word_list = []
        
        # Insert initial content
        self.content_textbox.insert("0.0", content)
        self.content_textbox.configure(state="disabled")  # Make it read-only
    
    def bind_keys(self): 
        self.master.bind_all("<Key-l>", lambda event : self.change_choosen_word(event, is_forward=True))
        self.master.bind_all("<Key-h>", lambda event : self.change_choosen_word(event, is_forward=False))
        self.master.bind_all("<Key-j>", lambda event : self.navigate_word_detail(event))
    
    def unbind_keys(self):
        self.master.unbind_all("<Key-l>")
        self.master.unbind_all("<Key-h>")
        self.master.unbind_all("<Key-j>")

    def update_content(self, new_content):
        self.content_textbox.configure(state="normal")  # Enable editing temporarily
        self.content_textbox.delete("0.0", "end")  # Clear existing content

        # turn new_content string into array of words
        self.word_list = new_content.split()
        self.choosen_word_pos = 0
        
        # Optional: Add manual line breaks for very long lines (alternative approach)
        # wrapped_content = self.wrap_text(new_content, width=80)

        print("content type: ",type(new_content))
        
        self.content_textbox.insert("0.0", new_content)
        self.content_textbox.configure(state="disabled")  # Make it read-only again
        
        # Highlight the first word by default
        if self.word_list:
            self.highlight_word_at_position(0)
     

    def wrap_text(self, text, width=80):
        lines = text.split('\n')
        wrapped_lines = []
        
        for line in lines:
            if len(line) <= width:
                wrapped_lines.append(line)
            else:
                # Use textwrap to break long lines
                wrapped = textwrap.fill(line, width=width)
                wrapped_lines.append(wrapped)
        
        return '\n'.join(wrapped_lines)

    def change_choosen_word(self, event, is_forward: bool):
        if (is_forward):
            if (self.choosen_word_pos < len(self.word_list) - 1):
                self.choosen_word_pos += 1
        else:
            if(self.choosen_word_pos > 0):
                self.choosen_word_pos -= 1
        
        # Highlight the currently selected word
        self.highlight_word_at_position(self.choosen_word_pos)
        
        print("choosen word position: ", self.choosen_word_pos)
        print("choosen word: ", self.word_list[self.choosen_word_pos] if self.word_list else "None")
    
    def setup_text_tags(self):
        # Enable text editing to configure tags
        self.content_textbox.configure(state="normal")
        
        # Create tags for different highlight styles
        self.content_textbox.tag_config("highlight", 
                                       background="#FFFF00",  # Yellow background
                                       foreground="#000000")   # Black text
        
        self.content_textbox.tag_config("selected", 
                                       background="#0078D4",  # Blue background
                                       foreground="#FFFFFF")   # White text
        
        self.content_textbox.tag_config("error", 
                                       background="#FF0000",  # Red background
                                       foreground="#FFFFFF")   # White text
        
        # Disable editing again
        self.content_textbox.configure(state="disabled")
    
    def highlight_word_at_position(self, word_position):
        # Highlight a specific word at the given position in the word list
        if not self.word_list or word_position >= len(self.word_list):
            return
            
        self.content_textbox.configure(state="normal")
        
        # Clear all previous highlights
        self.content_textbox.tag_remove("selected", "1.0", "end")
        
        # Calculate the character position of the word
        char_position = 0
        for i in range(word_position):
            char_position += len(self.word_list[i]) + 1  # +1 for space
        
        # Calculate start and end positions
        start_pos = f"1.{char_position}"
        end_pos = f"1.{char_position + len(self.word_list[word_position])}"
        
        # Apply highlight tag to the specific word
        self.content_textbox.tag_add("selected", start_pos, end_pos)
        
        self.content_textbox.configure(state="disabled")
    
    def highlight_specific_word(self, word_text, tag_name="highlight"):
        # Highlight all occurrences of a specific word
        self.content_textbox.configure(state="normal")
        
        # Clear previous highlights of this tag
        self.content_textbox.tag_remove(tag_name, "1.0", "end")
        
        # Get all text content
        content = self.content_textbox.get("1.0", "end-1c")
        
        # Find all occurrences of the word
        start_index = 0
        while True:
            pos = content.find(word_text, start_index)
            if pos == -1:
                break
                
            # Calculate line and character position
            lines_before = content[:pos].count('\n')
            line_start = content.rfind('\n', 0, pos) + 1
            char_pos = pos - line_start
            
            start_pos = f"{lines_before + 1}.{char_pos}"
            end_pos = f"{lines_before + 1}.{char_pos + len(word_text)}"
            
            # Apply highlight tag
            self.content_textbox.tag_add(tag_name, start_pos, end_pos)
            
            start_index = pos + 1
        
        self.content_textbox.configure(state="disabled")
    
    def navigate_word_detail(self, event):
        self.app.show_page(PageName.WORD_DETAIL, self.word_list[self.choosen_word_pos])