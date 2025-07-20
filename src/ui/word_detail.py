import customtkinter as ctk
import threading
from src.core.dictionary import Dictionary
from src.core.tts import Tts

class WordDetail(ctk.CTkFrame):
    def __init__(self, master, word="placeholder"):
        super().__init__(master, fg_color="#E5E5E5", width=1000, height=500)
        
        self.word = word
        self.widgets = []  # To track widgets for updating
        self.content_container = None  # Initialize content container
        self.word_content = None  # Store word content for TTS
        self.create_layout()  # Create initial layout

    def create_layout(self):
        # Clear previous widgets - destroy all children first
        for widget in self.winfo_children():
            widget.destroy()
        self.widgets = []

        # Word title - fixed at top
        word_label = ctk.CTkLabel(
            self,
            text=self.word.capitalize() if self.word != "placeholder" else "Word Detail",
            font=("Roboto", 36, "bold"),
            text_color="#2B2B2B"
        )
        word_label.pack(pady=(20, 10), anchor="n")
        self.widgets.append(word_label)

        # Container frame for scrollable content
        content_frame = ctk.CTkFrame(
            self,
            fg_color="#FFFFFF",
            corner_radius=10,
            border_width=2,
            border_color="#CCCCCC"
        )
        content_frame.pack(pady=10, padx=20, fill="both", expand=True)
        self.widgets.append(content_frame)

        # Scrollable frame for content with visible scrollbar
        scroll_frame = ctk.CTkScrollableFrame(
            content_frame,
            fg_color="transparent",
            corner_radius=0,
            scrollbar_button_color="#888888",
            scrollbar_button_hover_color="#666666",
            width=650  # Set fixed width to prevent overflow
        )
        scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        self.widgets.append(scroll_frame)

        self.content_container = scroll_frame  # Store for adding content
        
        # Show placeholder if no word is set
        if self.word == "placeholder":
            self.show_placeholder()

    def update_content(self, new_word):
        if self.word != new_word:  # Only update if word is different
            self.word = new_word
            self.create_layout()  # Rebuild layout
            if self.word and self.word != "placeholder":
                self.search_meaning()
                # Stop any current playback for faster response
                Tts.stop_current_playback()
                # Play word pronunciation in English when entering word detail page
                threading.Thread(target=lambda: Tts.play_sound(self.word, "en"), daemon=True).start()
                # Give a brief instruction after word pronunciation
                threading.Thread(target=self.delayed_instructions, daemon=True).start()
            else:
                self.show_placeholder()
    
    def delayed_instructions(self):
        """Play instructions after a short delay"""
        import time
        time.sleep(2)  # Wait 2 seconds for word pronunciation to finish
        brief_instruction = "Bạn vừa nghe phát âm tiếng Anh. Nhấn R để nghe định nghĩa, P để nghe lại phát âm, I để nghe hướng dẫn đầy đủ"
        Tts.play_sound(brief_instruction, "vi")

    def search_meaning(self):
        content = None
        try:
            print(f"Searching meaning for word: {self.word}")
            content = Dictionary.enToVi(self.word)
            print(f"Dictionary returned: {content}")
            self.word_content = content  # Store content for TTS
            
            if not content:
                # Handle case where no content is found
                print("No content returned from Dictionary")
                self.show_error("Không thể tìm thấy thông tin cho từ này.")
                return
            
            print("Content is valid, proceeding to display...")
            # Continue to display the content (even if it's fallback data)
                
        except Exception as e:
            print(f"Error in search_meaning: {e}")
            self.show_error("Có lỗi xảy ra khi tra từ. Vui lòng thử lại.")
            return

        # If we reach here, content is valid - display it normally
        # General description with better text wrapping
        description_label = ctk.CTkLabel(
            self.content_container,
            text=content.get("text", "No description available."),
            font=("Roboto", 16),
            text_color="#333333",
            wraplength=650,  # Reduced wraplength to fit better
            justify="left",
            anchor="w"
        )
        description_label.pack(pady=(15, 20), padx=20, fill="x")

        # Meanings
        for idx, meaning in enumerate(content.get("meaningArray", [])):
            # Card-like frame for each meaning
            meaning_frame = ctk.CTkFrame(
                self.content_container,
                fg_color="#F8F9FA",
                corner_radius=8,
                border_width=1,
                border_color="#E0E0E0"
            )
            meaning_frame.pack(pady=8, padx=20, fill="x")

            # Type header
            type_label = ctk.CTkLabel(
                meaning_frame,
                text=meaning.get("type", "Unknown"),
                font=("Roboto", 16, "bold"),
                text_color="#1A73E8"
            )
            type_label.pack(pady=(15, 8), padx=20, anchor="w")

            # Meaning text
            meaning_label = ctk.CTkLabel(
                meaning_frame,
                text=meaning.get("meaning", "No meaning provided."),
                font=("Roboto", 14),
                text_color="#2B2B2B",
                wraplength=600,  # Reduced wraplength
                justify="left",
                anchor="w"
            )
            meaning_label.pack(pady=5, padx=20, fill="x")

            # Example text
            example_text = meaning.get('example', 'No example available.')
            example_label = ctk.CTkLabel(
                meaning_frame,
                text=f"Example: {example_text}",
                font=("Roboto", 13, "italic"),
                text_color="#666666",
                wraplength=600,  # Reduced wraplength
                justify="left",
                anchor="w"
            )
            example_label.pack(pady=(5, 15), padx=20, fill="x")
    
    def show_placeholder(self):
        # Show placeholder message when no word is selected
        placeholder_label = ctk.CTkLabel(
            self.content_container,
            text="Select a word to see its definition and details.",
            font=("Roboto", 18),
            text_color="#666666"
        )
        placeholder_label.pack(pady=50)
        
        # Play audio instruction for placeholder
        placeholder_instruction = "Chưa chọn từ nào. Quay lại trang danh sách từ để chọn một từ cần tra cứu."
        threading.Thread(target=lambda: Tts.play_sound(placeholder_instruction, "vi"), daemon=True).start()
    
    def show_error(self, error_message):
        """Show error message when dictionary lookup fails"""
        error_label = ctk.CTkLabel(
            self.content_container,
            text=error_message,
            font=("Roboto", 16),
            text_color="#FF5555",
            wraplength=600,
            justify="left"
        )
        error_label.pack(pady=20, padx=20)
        
        # Add retry suggestion
        retry_label = ctk.CTkLabel(
            self.content_container,
            text="Nhấn Shift+H để quay lại hoặc thử từ khác.",
            font=("Roboto", 12),
            text_color="#888888"
        )
        retry_label.pack(pady=10)
        
        # Play audio error message
        audio_error = f"{error_message} Nhấn Shift H để quay lại trang trước hoặc thử từ khác."
        threading.Thread(target=lambda: Tts.play_sound(audio_error, "vi"), daemon=True).start()
    
    def bind_keys(self):
        # Bind scrolling keys for word detail page
        self.master.bind_all("<Key-k>", lambda event: self.scroll_up())
        self.master.bind_all("<Key-j>", lambda event: self.scroll_down())
        # Alternative arrow keys
        self.master.bind_all("<Up>", lambda event: self.scroll_up())
        self.master.bind_all("<Down>", lambda event: self.scroll_down())
        # Bind key to read word definition
        self.master.bind_all("<Key-r>", lambda event: self.read_word_definition())
        # Bind key to read word pronunciation (English)
        self.master.bind_all("<Key-p>", lambda event: self.read_word_pronunciation())
        # Bind key to read navigation instructions
        self.master.bind_all("<Key-i>", lambda event: self.read_instructions())
        # Bind key to stop current TTS playback
        self.master.bind_all("<Key-s>", lambda event: self.stop_tts())
    
    def unbind_keys(self):
        # Unbind scrolling keys
        self.master.unbind_all("<Key-k>")
        self.master.unbind_all("<Key-j>")
        self.master.unbind_all("<Up>")
        self.master.unbind_all("<Down>")
        self.master.unbind_all("<Key-r>")
        # Unbind new TTS keys
        self.master.unbind_all("<Key-p>")
        self.master.unbind_all("<Key-i>")
        self.master.unbind_all("<Key-s>")
    
    def scroll_up(self):
        if self.content_container:
            self.content_container._parent_canvas.yview_scroll(-1, "units")
    
    def scroll_down(self):
        if self.content_container:
            self.content_container._parent_canvas.yview_scroll(1, "units")
    
    def read_word_definition(self):
        """Read the complete word definition using TTS"""
        if not self.word_content or self.word == "placeholder":
            return
        
        # Stop current playback first
        Tts.stop_current_playback()
        
        # Create a complete text from the word content
        complete_text = self.word_content.get("text", "")
        
        # Add meanings
        for meaning in self.word_content.get("meaningArray", []):
            meaning_type = meaning.get("type", "")
            meaning_text = meaning.get("meaning", "")
            example_text = meaning.get("example", "")
            
            complete_text += f" Loại từ: {meaning_type}. Nghĩa: {meaning_text}."
            if example_text:
                complete_text += f" Ví dụ: {example_text}."
        
        # Play the complete definition
        threading.Thread(target=lambda: Tts.play_sound(complete_text, "vi"), daemon=True).start()
    
    def read_word_pronunciation(self):
        """Read the word pronunciation in English"""
        if self.word == "placeholder":
            return
        
        # Stop current playback first
        Tts.stop_current_playback()
        
        # Play word pronunciation in English
        threading.Thread(target=lambda: Tts.play_sound(self.word, "en"), daemon=True).start()
    
    def read_instructions(self):
        """Read navigation instructions for the word detail page"""
        # Stop current playback first
        Tts.stop_current_playback()
        
        instructions = """Trang chi tiết từ vựng. 
        Nhấn R để đọc định nghĩa đầy đủ. 
        Nhấn P để phát âm từ tiếng Anh. 
        Nhấn J hoặc mũi tên xuống để cuộn xuống. 
        Nhấn K hoặc mũi tên lên để cuộn lên. 
        Nhấn S để dừng giọng đọc. 
        Nhấn Shift H để quay lại trang trước. 
        Nhấn Shift L để tiến tới trang sau."""
        
        threading.Thread(target=lambda: Tts.play_sound(instructions, "vi"), daemon=True).start()
    
    def stop_tts(self):
        """Stop current TTS playback"""
        Tts.stop_current_playback()
        # Optional: Play a short confirmation sound
        threading.Thread(target=lambda: Tts.play_sound("Đã dừng giọng đọc", "vi"), daemon=True).start()