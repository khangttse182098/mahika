from src.core.gemini import Gemini
import json
class Dictionary:

    @staticmethod
    def enToVi(word):
        try:
            msg = f"Tra từ điển Anh - Việt cho từ '{word}'. Trả kết quả JSON với 2 key: 'text' (mô tả kết quả trả ra, tối đa 3 câu ngắn gọn, dễ hiểu cho người khiếm thị), 'meaningArray' (mảng các đối tượng, mỗi đối tượng có 3 key: 'type' - loại từ như Danh từ, Động từ; 'meaning' - nghĩa tiếng Việt ngắn gọn; 'example' - một ví dụ minh họa ngắn). Ví dụ: {{'text': 'Từ fish chỉ con cá, sống dưới nước. Nó có vây và mang. Thường dùng để chỉ thực phẩm.', 'meaningArray': [{{'type': 'Danh từ', 'meaning': 'Con cá', 'example': 'Con cá bơi trong hồ.'}}, {{'type': 'Động từ', 'meaning': 'Câu cá', 'example': 'Anh ấy đi câu cá.'}}]}}"
            response = Gemini.get_response(msg)
            
            if not response or response.strip() == "":
                print(f"Empty response from Gemini for word: {word}")
                # Return fallback data instead of None
                fallback_data = {
                    "text": f"Không thể tra từ '{word}' do lỗi kết nối API.",
                    "meaningArray": [
                        {
                            "type": "Từ tiếng Anh",
                            "meaning": f"Từ '{word}' - Chưa có thông tin",
                            "example": "Vui lòng kiểm tra kết nối mạng và thử lại"
                        }
                    ]
                }
                print("Returning fallback for empty response:", fallback_data)
                return fallback_data
            
            # Clean response - remove markdown formatting if present
            cleaned_response = response.strip()
            if cleaned_response.startswith("```json"):
                cleaned_response = cleaned_response[7:]  # Remove ```json
            if cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[:-3]  # Remove ```
            cleaned_response = cleaned_response.strip()
            
            response_object = json.loads(cleaned_response)
            text = response_object.get("text", "")
            meaning_array = response_object.get("meaningArray", [])
            print("Text:", text)
            for item in meaning_array:
                print(f" - Loại từ: {item.get('type', '')}, Nghĩa: {item.get('meaning', '')}")
            return response_object
            
        except json.JSONDecodeError as e:
            print(f"JSON decode error for word '{word}': {e}")
            print(f"Raw response: {response}")
            # Return fallback data
            fallback_data = {
                "text": f"Không thể tra từ '{word}' do lỗi định dạng dữ liệu. Vui lòng thử lại sau.",
                "meaningArray": [
                    {
                        "type": "Từ tiếng Anh",
                        "meaning": f"Từ '{word}' - Ý nghĩa không có sẵn",
                        "example": "Vui lòng kiểm tra kết nối mạng và thử lại"
                    }
                ]
            }
            print("Returning fallback data:", fallback_data)
            return fallback_data
        except Exception as e:
            print(f"General error for word '{word}': {e}")
            # Return basic fallback for any error
            fallback_data = {
                "text": f"Không thể tra từ '{word}' do lỗi hệ thống.",
                "meaningArray": [
                    {
                        "type": "Từ tiếng Anh",
                        "meaning": f"Từ '{word}' - Chưa có thông tin",
                        "example": "Vui lòng thử lại sau"
                    }
                ]
            }
            print("Returning general fallback data:", fallback_data)
            return fallback_data
    
    @staticmethod
    def viToEn(word):
        try:
            msg = f"Tra từ điển Việt - Anh cho từ '{word}'. Trả kết quả JSON với 2 key: 'text' (mô tả ngắn gọn bằng tiếng Việt, định dạng: 'Từ {word} trong tiếng Anh đọc là gì.', dễ hiểu cho người khiếm thị), 'meaningArray' (mảng các đối tượng, mỗi đối tượng có 4 key: 'type' - loại từ bằng tiếng Việt như Danh từ, Động từ; 'meaning' - từ tiếng Anh ngắn gọn; 'pronunciation' - cách đọc phiên âm quốc tế; 'example' - một ví dụ minh họa ngắn bằng tiếng Anh). Ví dụ: {{'text': 'Từ cá trong tiếng Anh đọc là fish.', 'meaningArray': [{{'type': 'Danh từ', 'meaning': 'Fish', 'pronunciation': '/fɪʃ/', 'example': 'The fish swims in the lake.'}}, {{'type': 'Động từ', 'meaning': 'To fish', 'pronunciation': '/fɪʃ/', 'example': 'He goes fishing on weekends.'}}]}}"
            response = Gemini.get_response(msg)
            
            if not response or response.strip() == "":
                print(f"Empty response from Gemini for word: {word}")
                # Return fallback data instead of None
                fallback_data = {
                    "text": f"Không thể tra từ '{word}' do lỗi kết nối API.",
                    "meaningArray": [
                        {
                            "type": "Từ tiếng Việt",
                            "meaning": f"Từ '{word}' - Chưa có thông tin",
                            "pronunciation": "N/A",
                            "example": "Vui lòng kiểm tra kết nối mạng và thử lại"
                        }
                    ]
                }
                print("Returning fallback for empty response:", fallback_data)
                return fallback_data
            
            # Clean response - remove markdown formatting if present
            cleaned_response = response.strip()
            if cleaned_response.startswith("```json"):
                cleaned_response = cleaned_response[7:]  # Remove ```json
            if cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[:-3]  # Remove ```
            cleaned_response = cleaned_response.strip()
            
            response_object = json.loads(cleaned_response)
            text = response_object.get("text", "")
            meaning_array = response_object.get("meaningArray", [])
            print("Text:", text)
            for item in meaning_array:
                print(f" - Loại từ: {item.get('type', '')}, Nghĩa: {item.get('meaning', '')}")
            return response_object
            
        except json.JSONDecodeError as e:
            print(f"JSON decode error for word '{word}': {e}")
            print(f"Raw response: {response}")
            # Return fallback data
            return {
                "text": f"Không thể tra từ '{word}' do lỗi định dạng dữ liệu.",
                "meaningArray": [
                    {
                        "type": "Từ tiếng Việt",
                        "meaning": f"Từ '{word}' - Ý nghĩa không có sẵn",
                        "pronunciation": "N/A",
                        "example": "Vui lòng kiểm tra kết nối mạng và thử lại"
                    }
                ]
            }
        except Exception as e:
            print(f"General error for word '{word}': {e}")
            # Return basic fallback for any error
            return {
                "text": f"Không thể tra từ '{word}' do lỗi hệ thống.",
                "meaningArray": [
                    {
                        "type": "Từ tiếng Việt",
                        "meaning": f"Từ '{word}' - Chưa có thông tin",
                        "pronunciation": "N/A", 
                        "example": "Vui lòng thử lại sau"
                    }
                ]
            }
