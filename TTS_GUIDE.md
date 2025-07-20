# Hướng dẫn sử dụng Text-to-Speech (TTS)

## Tính năng giọng đọc đã được thêm vào các trang:

### 1. **File List Page** (Đã có sẵn):

- Khi di chuyển giữa các file bằng `h` và `l`, tên file sẽ được đọc

### 2. **Word List Page** (MỚI):

- **Tự động đọc từ**: Khi di chuyển giữa các từ bằng `h` và `l`, từ hiện tại sẽ được đọc bằng giọng tiếng Anh
- **Ngôn ngữ**: Tiếng Anh (en) để phát âm chuẩn các từ

### 3. **Word Detail Page** (MỚI):

- **Đọc tên từ**: Khi vào trang chi tiết từ, sẽ đọc "Từ [tên từ]" bằng tiếng Việt
- **Đọc toàn bộ định nghĩa**: Nhấn phím `r` để nghe toàn bộ định nghĩa của từ

## Phím tắt mới:

### Word Detail Page:

- **`r`**: Đọc toàn bộ định nghĩa của từ (bao gồm mô tả, loại từ, nghĩa và ví dụ)
- **`k` hoặc `↑`**: Cuộn lên
- **`j` hoặc `↓`**: Cuộn xuống

## Cách hoạt động:

### Word List:

1. Mở một file text từ File List
2. Sử dụng `h` và `l` để di chuyển giữa các từ
3. Mỗi từ sẽ được đọc bằng giọng tiếng Anh tự động

### Word Detail:

1. Từ Word List, nhấn `j` để vào chi tiết một từ
2. Ngay khi vào, tên từ sẽ được đọc bằng tiếng Việt
3. Nhấn `r` để nghe toàn bộ định nghĩa chi tiết
4. Sử dụng `j`/`k` hoặc mũi tên để cuộn nội dung

## Ngôn ngữ TTS:

- **Word List**: Tiếng Anh (`en`) - để phát âm chuẩn từ vựng
- **Word Detail**: Tiếng Việt (`vi`) - để hiểu rõ định nghĩa và ví dụ

## Lưu ý:

- Tất cả TTS đều chạy trong background thread, không làm treo ứng dụng
- Có thể dừng giọng đọc hiện tại bằng cách di chuyển sang từ khác hoặc nhấn phím khác
- Giọng đọc sử dụng Google Text-to-Speech (gTTS) với chất lượng cao
