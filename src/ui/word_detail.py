import customtkinter as ctk
from src.core.dictionary import Dictionary

class WordDetail(ctk.CTkFrame):
    def __init__(self, master, word="placeholder"):
        super().__init__(master, fg_color="#E5E5E5", width=1000, height=500)
        
        self.word = word
        self.widgets = []  # To track widgets for updating
        # self.create_layout()

    def create_layout(self):
        # Clear previous widgets
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

        # Word title
        word_label = ctk.CTkLabel(
            self,
            text=self.word.capitalize(),
            font=("Roboto", 36, "bold"),
            text_color="#2B2B2B"
        )
        word_label.pack(pady=(20, 10))
        self.widgets.append(word_label)

        # Scrollable frame for content
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="#FFFFFF",
            corner_radius=10,
            width=900,
            height=400
        )
        scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)
        self.widgets.append(scroll_frame)

        self.content_container = scroll_frame  # Store for adding content

    def update_content(self, new_word):
        self.word = new_word
        self.create_layout()  # Rebuild layout
        self.search_meaning()

    def search_meaning(self):
        content = Dictionary.enToVi(self.word)
        if not content:
            # Handle case where no content is found
            error_label = ctk.CTkLabel(
                self.content_container,
                text="No information found for this word.",
                font=("Roboto", 16),
                text_color="#FF5555"
            )
            error_label.pack(pady=20)
            self.widgets.append(error_label)
            return

        # General description
        description_label = ctk.CTkLabel(
            self.content_container,
            text=content.get("text", "No description available."),
            font=("Roboto", 16),
            text_color="#333333",
            wraplength=850,
            justify="left"
        )
        description_label.pack(pady=(10, 20), padx=20, anchor="w")
        self.widgets.append(description_label)

        # Meanings
        for idx, meaning in enumerate(content.get("meaningArray", [])):
            # Card-like frame for each meaning
            meaning_frame = ctk.CTkFrame(
                self.content_container,
                fg_color="#F5F5F5",
                corner_radius=8,
                border_width=1,
                border_color="#DDDDDD"
            )
            meaning_frame.pack(pady=5, padx=20, fill="x")
            self.widgets.append(meaning_frame)

            # Type
            type_label = ctk.CTkLabel(
                meaning_frame,
                text=meaning.get("type", "Unknown"),
                font=("Roboto", 16, "bold"),
                text_color="#1A73E8"
            )
            type_label.pack(pady=(10, 5), padx=15, anchor="w")

            # Meaning
            meaning_label = ctk.CTkLabel(
                meaning_frame,
                text=meaning.get("meaning", "No meaning provided."),
                font=("Roboto", 14),
                text_color="#2B2B2B"
            )
            meaning_label.pack(pady=5, padx=15, anchor="w")

            # Example
            example_label = ctk.CTkLabel(
                meaning_frame,
                text=f"Example: {meaning.get('example', 'No example available.')}",
                font=("Roboto", 14, "italic"),
                text_color="#555555"
            )
            example_label.pack(pady=(5, 10), padx=15, anchor="w")