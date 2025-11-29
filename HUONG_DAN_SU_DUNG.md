# Hướng Dẫn Sử Dụng Mahika - Ứng Dụng Học Từ Vựng Cho Người Khiếm Thị

## 📋 Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
3. [Cài Đặt](#cài-đặt)
4. [Cách Chạy Ứng Dụng](#cách-chạy-ứng-dụng)
5. [Hướng Dẫn Sử Dụng](#hướng-dẫn-sử-dụng)
6. [Phím Tắt](#phím-tắt)
7. [Tính Năng Chính](#tính-năng-chính)
8. [Xử Lý Sự Cố](#xử-lý-sự-cố)

---

## 🎯 Giới Thiệu

**Mahika** là ứng dụng học từ vựng tiếng Anh được thiết kế đặc biệt cho người khiếm thị, tích hợp:

- ✅ Text-to-Speech (TTS) - Đọc nội dung
- ✅ Speech-to-Text (STT) - Nhận diện giọng nói
- ✅ AI Chat hỗ trợ học tập
- ✅ OCR - Nhận diện chữ từ ảnh
- ✅ Tra cứu từ điển

---

## 💻 Yêu Cầu Hệ Thống

### Tối Thiểu:

- **OS**: Windows 10/11 (64-bit)
- **RAM**: 4GB
- **Ổ cứng**: 2GB khả dụng
- **Internet**: Kết nối ổn định (cho TTS, AI Chat, tra từ điển)

### Khuyến Nghị:

- **RAM**: 8GB trở lên
- **Microphone**: Để sử dụng tính năng Speech-to-Text
- **Speakers/Headphones**: Để nghe TTS

---

## 📦 Cài Đặt

### Cách 1: Sử Dụng File EXE (Khuyến nghị cho người dùng cuối)

1. **Download** file `Mahika.exe` từ thư mục `dist/`
2. **Copy toàn bộ thư mục** `dist/` (bao gồm các file DLL dependencies)
3. **Double-click** `Mahika.exe` để chạy

### Cách 2: Chạy Từ Source Code (Cho Developer)

#### Bước 1: Clone Repository

```bash
git clone https://github.com/khangttse182098/mahika.git
cd mahika
```

#### Bước 2: Tạo Virtual Environment

```bash
python -m venv venv
```

#### Bước 3: Kích Hoạt Virtual Environment

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

#### Bước 4: Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

#### Bước 5: Cấu Hình Database

Tạo file `.env` trong thư mục gốc với nội dung:

```env
# MySQL Database Configuration
DB_HOST=tramway.proxy.rlwy.net
DB_PORT=11636
DB_NAME=railway
DB_USER=root
DB_PASSWORD=your_password_here

# Google API Key (cho AI Chat)
GOOGLE_API_KEY=your_google_api_key_here
```

---

## 🚀 Cách Chạy Ứng Dụng

### Từ File EXE:

```bash
cd dist
Mahika.exe
```

### Từ Source Code:

```bash
# Đảm bảo đã activate virtual environment
venv\Scripts\python.exe main.py

# Hoặc nếu đã activate venv
python main.py
```

---

## 📖 Hướng Dẫn Sử Dụng

### 1️⃣ Đăng Nhập

**Bước 1**: Khởi động ứng dụng

- Nhập **Email** và **Password**
- Nhấn **Enter** hoặc click nút **Login**

**Tài khoản mẫu**:

- Email: `admin@gmail.com`
- Email: `phucphse181514@fpt.edu.vn`

**Lưu ý**:

- Tài khoản phải có `has_paid = 1` trong database
- Sau khi login thành công, hệ thống sẽ tự động load Whisper AI model (mất ~5-10 giây)

---

### 2️⃣ File List - Chọn File Để Học

**Mục đích**: Chọn file văn bản (.txt, .docx, .pdf) chứa từ vựng cần học

**Các thao tác**:

- **Số 1-9**: Chọn file nhanh theo số thứ tự
- **Enter**: Mở file đã chọn
- **Escape**: Quay lại trang trước
- **F5**: Làm mới danh sách file

**Hỗ trợ định dạng**:

- `.txt` - Text file
- `.docx` - Word document
- `.pdf` - PDF file

---

### 3️⃣ Word List - Danh Sách Từ Vựng

**Mục đích**: Hiển thị tất cả từ vựng trong file đã chọn

**Các thao tác**:

- **Mũi tên ↑/↓**: Di chuyển giữa các từ
- **Enter**: Xem chi tiết từ
- **Số 1-9**: Chọn từ nhanh theo số thứ tự
- **Ctrl+F**: Mở AI Chat để hỏi về từ vựng
- **Escape**: Quay lại File List

**Tính năng tự động**:

- TTS sẽ tự động đọc từ khi bạn di chuyển
- Hiển thị số thứ tự để dễ dàng chọn

---

### 4️⃣ Word Detail - Chi Tiết Từ Vựng

**Mục đích**: Xem định nghĩa, phiên âm, ví dụ của từ

**⚠️ QUAN TRỌNG - CÁCH THOÁT (CÓ 4 CÁCH)**:

- **Shift + K**: Thoát nhanh về trang trước ⚡ (khuyến nghị)
- **Escape (ESC)**: Thoát và quay lại Word List
- **Backspace**: Thoát và quay lại Word List
- **Alt + ←**: Quay lại trang trong lịch sử

**Thông tin hiển thị**:

- **Từ vựng** (Word)
- **Phiên âm** (Phonetic)
- **Định nghĩa** (Definition)
- **Ví dụ** (Examples)
- **Từ đồng nghĩa** (Synonyms)
- **Từ trái nghĩa** (Antonyms)

**Các thao tác điều khiển**:

- **k** (chữ thường): Cuộn lên ⬆️
- **j** (chữ thường): Cuộn xuống ⬇️
- **↑**: Cuộn lên (mũi tên)
- **↓**: Cuộn xuống (mũi tên)
- **R**: Đọc lại định nghĩa đầy đủ (TTS)
- **S**: Dừng giọng đọc hiện tại
- **I**: Nghe hướng dẫn sử dụng trang
- **Ctrl+C**: Copy toàn bộ thông tin
- **Ctrl+F**: Mở AI Chat để hỏi về từ này

**💡 Mẹo quan trọng**:

- **`k`** (chữ thường) = cuộn lên | **`Shift + K`** (Shift+k) = thoát
- Nhấn **Shift + K** là cách nhanh nhất để thoát
- Nếu phím tắt không hoạt động:
  1. Click chuột vào vùng nội dung Word Detail
  2. Sau đó nhấn **Shift + K** hoặc **Escape**

---

### 5️⃣ AI Chat - Trợ Lý Học Tập

**Mục đích**: Hỏi đáp với AI về từ vựng, ngữ pháp, cách dùng

**Cách mở AI Chat**:

- Nhấn **Ctrl+F** từ bất kỳ trang nào
- Hoặc click nút AI Chat (nếu có)

**Các thao tác**:

- **Gõ câu hỏi** vào ô text
- **Enter**: Gửi câu hỏi
- **Ctrl+V**: Gọi Speech-to-Text (nói câu hỏi)
- **Ctrl+R**: Đọc lại câu trả lời
- **Escape**: Đóng AI Chat

**Ví dụ câu hỏi**:

- "Explain the word 'example'"
- "Give me 5 sentences using 'beautiful'"
- "What's the difference between 'affect' and 'effect'?"
- "How to use 'would' in conditional sentences?"

---

## ⌨️ Phím Tắt

### Phím Điều Hướng Toàn Cục

| Phím       | Chức năng            |
| ---------- | -------------------- |
| `Alt + ←`  | Quay lại trang trước |
| `Alt + →`  | Tiến tới trang kế    |
| `Escape`   | Quay lại trang trước |
| `Ctrl + F` | Mở AI Chat           |

### Phím Tắt File List

| Phím    | Chức năng                |
| ------- | ------------------------ |
| `1-9`   | Chọn file theo số thứ tự |
| `Enter` | Mở file đã chọn          |
| `F5`    | Làm mới danh sách        |
| `↑/↓`   | Di chuyển giữa các file  |

### Phím Tắt Word List

| Phím       | Chức năng              |
| ---------- | ---------------------- |
| `1-9`      | Chọn từ theo số thứ tự |
| `Enter`    | Xem chi tiết từ        |
| `↑/↓`      | Di chuyển giữa các từ  |
| `Ctrl + F` | Mở AI Chat             |

### Phím Tắt Word Detail

| Phím        | Chức năng                           |
| ----------- | ----------------------------------- |
| `Shift + K` | ⭐ **THOÁT** về trang trước (nhanh) |
| `Escape`    | **THOÁT** về Word List              |
| `Backspace` | **THOÁT** về Word List              |
| `Alt + ←`   | **THOÁT** về lịch sử trang trước    |
| `k`         | Cuộn lên ⬆️                         |
| `j`         | Cuộn xuống ⬇️                       |
| `↑`         | Cuộn lên (mũi tên)                  |
| `↓`         | Cuộn xuống (mũi tên)                |
| `R`         | Đọc lại định nghĩa đầy đủ (TTS)     |
| `S`         | Dừng giọng đọc                      |
| `I`         | Nghe hướng dẫn sử dụng              |
| `Ctrl + C`  | Copy thông tin                      |
| `Ctrl + F`  | Mở AI Chat                          |

**📌 Lưu ý**:

- `k` (chữ thường) ≠ `Shift+K` (Shift + k)
- `k` = cuộn lên, `Shift+K` = thoát

### Phím Tắt AI Chat

| Phím       | Chức năng           |
| ---------- | ------------------- |
| `Enter`    | Gửi câu hỏi         |
| `Ctrl + V` | Speech-to-Text      |
| `Ctrl + R` | Đọc lại câu trả lời |
| `Escape`   | Đóng AI Chat        |

---

## 🎨 Tính Năng Chính

### 1. Text-to-Speech (TTS)

- **Công nghệ**: Google Text-to-Speech (gTTS)
- **Ngôn ngữ hỗ trợ**: Tiếng Việt, Tiếng Anh
- **Cache**: Tự động cache để tăng tốc độ
- **Background**: Chạy ngầm không block UI

### 2. Speech-to-Text (STT)

- **Công nghệ**: OpenAI Whisper (base model)
- **Độ chính xác**: Cao
- **Thời gian**: ~2-5 giây/câu
- **Cách dùng**: Nhấn `Ctrl+V` trong AI Chat

### 3. AI Chat

- **Công nghệ**: Google Gemini AI
- **Context-aware**: Hiểu ngữ cảnh từ vựng đang học
- **Realtime**: Phản hồi nhanh (~1-3 giây)

### 4. Dictionary

- **API**: Free Dictionary API
- **Thông tin đầy đủ**: Định nghĩa, phiên âm, ví dụ, từ đồng nghĩa

### 5. OCR (Nhận diện chữ từ ảnh)

- **Công nghệ**: Tesseract OCR
- **Hỗ trợ**: Ảnh chứa văn bản tiếng Anh
- **Format**: JPG, PNG, BMP

---

## 🔧 Xử Lý Sự Cố

### ❌ Lỗi: "Cannot connect to database"

**Nguyên nhân**: Không kết nối được MySQL

**Giải pháp**:

1. Kiểm tra file `.env`:
   ```env
   DB_HOST=tramway.proxy.rlwy.net
   DB_PORT=11636
   DB_NAME=railway
   DB_USER=root
   DB_PASSWORD=GMXWNbTkHFmPeXKqTornRrNLZJIEucYD
   ```
2. Kiểm tra kết nối internet
3. Kiểm tra MySQL server đang chạy
4. Test kết nối:
   ```bash
   python test_mysql_connection.py
   ```

---

### ❌ Lỗi: "Tài khoản chưa được kích hoạt"

**Nguyên nhân**: User chưa có `has_paid = 1`

**Giải pháp**:

```sql
UPDATE users SET has_paid = 1 WHERE email = 'your_email@example.com';
```

---

### ❌ TTS không phát âm thanh

**Nguyên nhân**: Volume tắt hoặc pygame mixer lỗi

**Giải pháp**:

1. Kiểm tra volume máy tính
2. Kiểm tra loa/tai nghe
3. Test TTS riêng:
   ```bash
   python test_tts.py
   ```
4. Kiểm tra cache:
   ```bash
   # Windows
   dir %TEMP%\mahika_tts_cache
   ```

---

### ❌ Whisper model load chậm

**Nguyên nhân**: Model lớn, máy yếu

**Giải pháp**:

1. Sử dụng model nhỏ hơn trong `login.py`:
   ```python
   Stt.load_model("tiny")  # Thay vì "base"
   ```
2. Hoặc bỏ qua load model nếu không dùng STT

---

### ❌ AI Chat không hoạt động

**Nguyên nhân**: Thiếu Google API Key hoặc hết quota

**Giải pháp**:

1. Kiểm tra `.env`:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```
2. Lấy API key mới tại: https://makersuite.google.com/app/apikey
3. Kiểm tra quota tại: https://console.cloud.google.com

---

### ❌ File không hiển thị trong File List

**Nguyên nhân**: File không đúng định dạng hoặc đường dẫn sai

**Giải pháp**:

1. Đảm bảo file có định dạng: `.txt`, `.docx`, `.pdf`
2. Đặt file trong thư mục dự án hoặc thư mục đã cấu hình
3. Nhấn `F5` để refresh danh sách

---

### ❌ Không thể thoát khỏi Word Detail

**Nguyên nhân**: Focus không đúng widget hoặc event handler chưa bind

**Giải pháp**:

1. **Thử các phím tắt sau theo thứ tự (từ nhanh → chậm)**:

   | Phím        | Tốc độ | Mô tả                    |
   | ----------- | ------ | ------------------------ |
   | `Shift + K` | ⚡⚡⚡ | Nhanh nhất (khuyến nghị) |
   | `Escape`    | ⚡⚡   | Nhanh                    |
   | `Backspace` | ⚡⚡   | Nhanh                    |
   | `Alt + ←`   | ⚡     | Trung bình (qua lịch sử) |

2. **Đảm bảo bạn nhấn đúng phím**:

   - ❌ SAI: Nhấn `k` (chữ thường) → Chỉ cuộn lên
   - ✅ ĐÚNG: Nhấn `Shift + K` (giữ Shift rồi nhấn K) → Thoát

3. **Nếu vẫn không thoát được**:

   - Click chuột vào vùng nội dung Word Detail
   - Sau đó nhấn `Shift + K` (giữ Shift + nhấn K cùng lúc)

4. **Kiểm tra code** (dành cho developer):

   ```python
   # Trong file word_detail.py - phải có đủ 3 bindings
   self.master.bind_all("<Shift-Key-K>", lambda e: self.go_back_to_previous_page())
   self.master.bind_all("<Escape>", lambda e: self.go_back_to_previous_page())
   self.master.bind_all("<BackSpace>", lambda e: self.go_back_to_previous_page())
   ```

5. **Khởi động lại ứng dụng** nếu vẫn bị stuck

**🔍 Debug Tips**:

- Test `k` → nếu cuộn lên được = bindings hoạt động
- Test `Shift+K` → nếu không thoát = cần check code

---

## 📞 Hỗ Trợ

### Liên hệ:

- **Email**: khangttse182098@fpt.edu.vn
- **GitHub**: https://github.com/khangttse182098/mahika
- **Issues**: https://github.com/khangttse182098/mahika/issues

### Báo lỗi:

1. Mở issue tại GitHub
2. Mô tả chi tiết lỗi
3. Attach screenshot/log nếu có
4. Nêu rõ:
   - Hệ điều hành
   - Python version
   - Cách tái hiện lỗi

---

## 📝 Ghi Chú

- **Phiên bản hiện tại**: 1.0.0
- **Ngày cập nhật**: 20/10/2025
- **Tác giả**: Team Mahika - FPTU
- **License**: MIT

---

## 🎓 Credits

- **CustomTkinter**: Modern UI framework
- **Google Gemini AI**: AI Chat
- **OpenAI Whisper**: Speech-to-Text
- **gTTS**: Text-to-Speech
- **Free Dictionary API**: Tra từ điển
- **Tesseract OCR**: Nhận diện chữ

---

**Chúc bạn học tập hiệu quả với Mahika! 🎉**
