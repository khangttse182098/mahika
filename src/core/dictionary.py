from src.core.gemini import Gemini
import json
class Dictionary:

    @staticmethod
    def enToVi(word):
        msg = f"Tra từ điển Anh - Việt cho từ '{word}'. Trả kết quả JSON với 2 key: 'text' (mô tả kết quả trả ra, tối đa 3 câu ngắn gọn, dễ hiểu cho người khiếm thị), 'meaningArray' (mảng các đối tượng, mỗi đối tượng có 3 key: 'type' - loại từ như Danh từ, Động từ; 'meaning' - nghĩa tiếng Việt ngắn gọn; 'example' - một ví dụ minh họa ngắn). Ví dụ: {{'text': 'Từ fish chỉ con cá, sống dưới nước. Nó có vây và mang. Thường dùng để chỉ thực phẩm.', 'meaningArray': [{{'type': 'Danh từ', 'meaning': 'Con cá', 'example': 'Con cá bơi trong hồ.'}}, {{'type': 'Động từ', 'meaning': 'Câu cá', 'example': 'Anh ấy đi câu cá.'}}]}}"
        response = Gemini.get_response(msg)
        response_object = json.loads(response)
        text = response_object.get("text", "")
        meaning_array = response_object.get("meaningArray", [])
        print("Text:", text)
        for item in meaning_array:
            print(f" - Loại từ: {item.get('type', '')}, Nghĩa: {item.get('meaning', '')}")
        return response_object
    
    @staticmethod
    def viToEn(word):
        msg = f"Tra từ điển Việt - Anh cho từ '{word}'. Trả kết quả JSON với 2 key: 'text' (mô tả ngắn gọn bằng tiếng Việt, định dạng: 'Từ {word} trong tiếng Anh đọc là gì.', dễ hiểu cho người khiếm thị), 'meaningArray' (mảng các đối tượng, mỗi đối tượng có 4 key: 'type' - loại từ bằng tiếng Việt như Danh từ, Động từ; 'meaning' - từ tiếng Anh ngắn gọn; 'pronunciation' - cách đọc phiên âm quốc tế; 'example' - một ví dụ minh họa ngắn bằng tiếng Anh). Ví dụ: {{'text': 'Từ cá trong tiếng Anh đọc là fish.', 'meaningArray': [{{'type': 'Danh từ', 'meaning': 'Fish', 'pronunciation': '/fɪʃ/', 'example': 'The fish swims in the lake.'}}, {{'type': 'Động từ', 'meaning': 'To fish', 'pronunciation': '/fɪʃ/', 'example': 'He goes fishing on weekends.'}}]}}"
        response = Gemini.get_response(msg)
        response_object = json.loads(response)
        text = response_object.get("text", "")
        meaning_array = response_object.get("meaningArray", [])
        print("Text:", text)
        for item in meaning_array:
            print(f" - Loại từ: {item.get('type', '')}, Nghĩa: {item.get('meaning', '')}")
        return response_object
