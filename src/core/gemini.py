import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
class Gemini: 
    api_key = os.getenv("GOOGLE_API_KEY")  # Changed from GEMINI_API_KEY to GOOGLE_API_KEY
    @staticmethod
    def get_response(prompt, system_content=""):
        try:
            if not Gemini.api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
            genai.configure(api_key=Gemini.api_key)
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash", 
                generation_config=genai.types.GenerationConfig(response_mime_type="text/plain")
                )
            system_content += "Sử dụng plain text không cần định dạng Markdown, tránh các dấu **"
            response = model.generate_content([system_content, prompt])
            
            if not response or not response.text:
                print("Empty response from Gemini API")
                return ""
            
            return response.text.strip()
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return ""