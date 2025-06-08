import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
class Gemini: 
    api_key = os.getenv("GEMINI_API_KEY")
    @staticmethod
    def get_response(prompt, system_content):
        genai.configure(api_key=Gemini.api_key)
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash", 
            generation_config=genai.types.GenerationConfig(response_mime_type="text/plain")
            )
        system_content += "Sử dụng plain text không cần định dạng Markdown."
        response = model.generate_content([system_content, prompt])
        return response.text.strip()