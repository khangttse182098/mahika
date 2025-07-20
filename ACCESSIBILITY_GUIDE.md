# Hướng dẫn sử dụng tính năng giọng đọc (TTS) - Mahika Dictionary

## Dành cho người khiếm thị

Ứng dụng Mahika Dictionary được thiết kế đặc biệt để hỗ trợ người khiếm thị tra cứu từ điển tiếng Anh - tiếng Việt thông qua các tính năng giọng đọc tiên tiến.

## Tính năng TTS trong trang Word Detail (Chi tiết từ)

### 🎵 Tự động phát âm khi vào trang

- Khi bạn chọn một từ và vào trang chi tiết, ứng dụng sẽ tự động:
  1. Đọc tên từ bằng giọng tiếng Anh chuẩn (phát âm từ)
  2. Sau 2 giây, đưa ra hướng dẫn ngắn gọn về các phím tắt bằng tiếng Việt

### ⌨️ Phím tắt TTS trong trang Word Detail

| Phím          | Chức năng                                  |
| ------------- | ------------------------------------------ |
| **R**         | Đọc toàn bộ định nghĩa của từ (tiếng Việt) |
| **P**         | Phát âm từ bằng tiếng Anh                  |
| **I**         | Nghe hướng dẫn đầy đủ về tất cả phím tắt   |
| **S**         | Dừng giọng đọc hiện tại                    |
| **J** / **↓** | Cuộn xuống nội dung                        |
| **K** / **↑** | Cuộn lên nội dung                          |
| **Shift+H**   | Quay lại trang trước                       |
| **Shift+L**   | Tiến tới trang sau                         |

### 🔊 Các tình huống TTS đặc biệt

#### Khi chưa chọn từ (Placeholder):

- Ứng dụng sẽ thông báo: "Chưa chọn từ nào. Quay lại trang danh sách từ để chọn một từ cần tra cứu."

#### Khi có lỗi tra từ:

- Ứng dụng sẽ đọc thông báo lỗi và hướng dẫn khắc phục

#### Khi tra từ thành công:

- Đọc tên từ bằng giọng tiếng Anh chuẩn (phát âm tự nhiên)
- Hướng dẫn ngắn gọn bằng tiếng Việt
- Sẵn sàng cho các lệnh TTS khác

### 🚀 Tính năng tối ưu hóa

#### Cache âm thanh:

- Các từ đã được phát âm sẽ được lưu cache để phát lại nhanh hơn
- Tự động pre-cache các từ phổ biến để cải thiện tốc độ

#### Luồng xử lý nền (Threading):

- TTS chạy trên luồng riêng, không làm đơ giao diện
- Có thể dừng giọng đọc bất cứ lúc nào

#### Điều khiển thông minh:

- Tự động dừng giọng đọc cũ khi bắt đầu giọng đọc mới
- Throttling để tránh spam âm thanh

### 💡 Mẹo sử dụng hiệu quả

1. **Nghe hướng dẫn đầy đủ**: Nhấn **I** khi lần đầu sử dụng trang
2. **Phát âm chuẩn tự động**: Khi vào trang, từ sẽ được phát âm tiếng Anh chuẩn tự động
3. **Phát âm lặp lại**: Nhấn **P** để nghe lại phát âm tiếng Anh bất cứ lúc nào
4. **Đọc định nghĩa đầy đủ**: Nhấn **R** để nghe toàn bộ thông tin của từ bằng tiếng Việt
5. **Dừng khi cần**: Nhấn **S** để dừng giọng đọc khi muốn chuyển sang tác vụ khác
6. **Điều hướng mượt mà**: Sử dụng Shift+H/L để chuyển trang nhanh chóng

### 🔧 Cấu hình âm thanh

- **Ngôn ngữ**: Tự động chuyển đổi giữa tiếng Việt (hướng dẫn, định nghĩa) và tiếng Anh (phát âm từ)
- **Chất lượng**: Sử dụng Google Text-to-Speech với chất lượng cao
- **Tốc độ**: Được tối ưu hóa cho việc nghe hiểu dễ dàng

### ⚠️ Lưu ý quan trọng

- Đảm bảo có kết nối internet để TTS hoạt động
- Âm lượng hệ thống cần được bật
- Có thể mất vài giây để tải âm thanh lần đầu tiên

### 🆘 Xử lý sự cố

- **Không có âm thanh**: Kiểm tra kết nối internet và âm lượng
- **Âm thanh bị cắt**: Nhấn **S** để dừng và thử lại
- **Phát âm sai**: Đây là giọng máy, có thể không hoàn hảo 100%

---

**Phát triển bởi**: Mahika Team  
**Mục đích**: Hỗ trợ người khiếm thị học tiếng Anh hiệu quả
