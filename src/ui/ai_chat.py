import customtkinter as ctk
import threading
import re
from src.core.stt import Stt
from src.core.tts import Tts
from src.core.gemini import Gemini
from src.core.audio_recorder import AudioRecorder

class AiChatWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Window configuration
        self.title("AI Assistant")
        self.geometry("300x200")
        self.resizable(False, False)
        
        # Center the window on screen
        self.center_window()
        self.transient(master)
        self.grab_set()
        
        # Initialize components
        self.gemini = Gemini()
        self.audio_recorder = AudioRecorder()
        self.is_recording = False
        self.is_processing = False
        
        self.setup_ui()
        self.bind_keys()
        
    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (300 // 2)
        y = (self.winfo_screenheight() // 2) - (200 // 2)
        self.geometry(f"300x200+{x}+{y}")
        
    def setup_ui(self):
        # Main container
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Icon/Status display (large, centered)
        self.status_icon = ctk.CTkLabel(
            main_frame,
            text="🎤",
            font=ctk.CTkFont(size=80)
        )
        self.status_icon.pack(expand=True)
        
        # Status text
        self.status_text = ctk.CTkLabel(
            main_frame,
            text="Giữ SPACE để nói",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.status_text.pack(pady=(0, 20))
        
        # ESC to close instruction
        close_instruction = ctk.CTkLabel(
            main_frame,
            text="ESC để đóng",
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        close_instruction.pack()
        
    def bind_keys(self):
        # Bind keyboard events - Space to record
        self.bind("<KeyPress-space>", self.start_recording)
        self.bind("<KeyRelease-space>", self.stop_recording)
        self.bind("<Escape>", lambda e: self.close_chat())
        self.focus_set()
        
    def start_recording(self, event=None):
        """Start voice recording"""
        if not self.is_recording and not self.is_processing:
            self.is_recording = True
            self.status_icon.configure(text="🔴")
            self.status_text.configure(text="Đang nghe...")
            
            # Start recording in background thread
            threading.Thread(target=self._start_recording_thread, daemon=True).start()
            
    def stop_recording(self, event=None):
        """Stop voice recording and process"""
        if self.is_recording:
            self.is_recording = False
            self.is_processing = True
            self.status_icon.configure(text="...")
            self.status_text.configure(text="Đang xử lý...")
            
            # Stop recording and process in background
            threading.Thread(target=self._stop_recording_thread, daemon=True).start()
            
    def _start_recording_thread(self):
        """Background thread for starting recording"""
        try:
            self.audio_recorder.start_recording()
        except Exception as e:
            self.after(0, lambda: self.update_status("❌", "Lỗi ghi âm"))
            
    def _stop_recording_thread(self):
        """Background thread for stopping recording and processing"""
        try:
            # Stop recording
            audio_file = self.audio_recorder.stop_recording()
            
            if audio_file:
                # Convert speech to text
                self.after(0, lambda: self.update_status("🔄", "Đang xử lý giọng nói..."))                
                user_text = Stt.transcribe(audio_file)
                
                if user_text and user_text.strip():
                    # Log user input
                    print(f"[USER INPUT]: {user_text}")
                    
                    # Get AI response with special prompt
                    self.after(0, lambda: self.update_status("🤖", "AI đang suy nghĩ..."))
                    
                    # Create special prompt for vocabulary learning
                    enhanced_prompt = f"""
Người dùng hỏi: "{user_text}"

Nếu người dùng hỏi về từ tiếng Anh của một từ tiếng Việt, hãy trả lời theo định dạng:
"Từ [từ_tiếng_việt] trong tiếng Anh là [từ_tiếng_anh]"

Ví dụ:
- Hỏi: "từ xinh đẹp trong tiếng Anh là gì?" → Trả lời: "Từ xinh đẹp trong tiếng Anh là beautiful"
- Hỏi: "con chó tiếng Anh là gì?" → Trả lời: "Từ con chó trong tiếng Anh là dog"
- Hỏi: "từ học tiếng Anh là gì?" → Trả lời: "Từ học trong tiếng Anh là study"

Đối với các câu hỏi khác, trả lời bình thường bằng tiếng Việt và thêm [ENGLISH: từ_tiếng_anh] nếu có từ vựng liên quan.

QUAN TRỌNG: Chỉ trả lời ngắn gọn, không giải thích thêm.
"""
                    
                    ai_response = self.gemini.get_response(enhanced_prompt)
                    
                    if ai_response:
                        # Log AI response
                        print(f"[AI RESPONSE]: {ai_response}")
                        
                        # Process and play response
                        self.process_and_play_response(ai_response)
                    else:
                        print("[AI RESPONSE]: ERROR - No response from AI")
                        self.after(0, lambda: self.update_status("❌", "Lỗi AI"))
                        
                else:
                    self.after(0, lambda: self.update_status("❌", "Không nghe thấy"))
                    
            else:
                self.after(0, lambda: self.update_status("❌", "Lỗi ghi âm"))
                
        except Exception as e:
            self.after(0, lambda: self.update_status("❌", f"Lỗi: {str(e)[:20]}..."))
            
        finally:
            # Reset UI state after 2 seconds
            self.after(2000, self.reset_ui_state)
            
    def process_and_play_response(self, ai_response):
        """Process AI response and play only English pronunciation"""
        try:
            # Check if this is a vocabulary translation response
            vocab_match = re.search(r'Từ (.+?) trong tiếng Anh là (.+?)(?:\.|$)', ai_response, re.IGNORECASE)
            
            if vocab_match:
                vietnamese_word = vocab_match.group(1).strip()
                english_word = vocab_match.group(2).strip()
                
                # Log extracted words
                print(f"[EXTRACTED] Vietnamese: {vietnamese_word}, English: {english_word}")
                
                # Only pronounce the English word
                self.after(0, lambda: self.update_status("🗣️", "Phát âm tiếng Anh..."))
                
                def play_english_only():
                    # Directly pronounce the English word
                    Tts.play_sound(english_word, "en")
                
                threading.Thread(target=play_english_only, daemon=True).start()
                
            else:
                # Check for [ENGLISH: word] format (fallback)
                english_match = re.search(r'\[ENGLISH:\s*([^\]]+)\]', ai_response)
                
                if english_match:
                    english_word = english_match.group(1).strip()
                    
                    # Log extracted word
                    print(f"[EXTRACTED] English (fallback): {english_word}")
                    
                    # Only pronounce the English word
                    self.after(0, lambda: self.update_status("🗣️", "Phát âm tiếng Anh..."))
                    
                    def play_english_fallback():
                        Tts.play_sound(english_word, "en")
                    
                    threading.Thread(target=play_english_fallback, daemon=True).start()
                    
                else:
                    # No English word found, play Vietnamese (rare case)
                    print("[WARNING] No English word found in response")
                    self.after(0, lambda: self.update_status("🔊", "Đang trả lời..."))
                    threading.Thread(target=lambda: Tts.play_sound(ai_response, "vi"), daemon=True).start()
                
        except Exception as e:
            print(f"[ERROR] Error processing response: {e}")
            # Fallback: play original response
            self.after(0, lambda: self.update_status("🔊", "Đang trả lời..."))
            threading.Thread(target=lambda: Tts.play_sound(ai_response, "vi"), daemon=True).start()
    
    def update_status(self, icon, text):
        """Update status display"""
        self.status_icon.configure(text=icon)
        self.status_text.configure(text=text)
        
    def reset_ui_state(self):
        """Reset UI to ready state"""
        self.status_icon.configure(text="🎤")
        self.status_text.configure(text="Giữ SPACE để nói")
        self.is_recording = False
        self.is_processing = False
        
    def close_chat(self):
        """Close the chat window"""
        # Stop any ongoing recording
        if self.is_recording:
            self.stop_recording()
        
        # Notify parent app about close
        if hasattr(self.master, 'on_ai_chat_close'):
            self.master.on_ai_chat_close()
        
        self.grab_release()
        self.destroy()
        
    def on_closing(self):
        """Handle window closing"""
        self.close_chat()
