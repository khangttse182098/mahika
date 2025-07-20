# Hướng dẫn sử dụng Navigation Keys

## Phím tắt điều hướng mới đã được thêm vào tất cả các trang:

### Phím tắt Global (hoạt động trên tất cả trang):

- **Shift + H**: Quay lại trang trước đó
- **Shift + L**: Tiến tới trang tiếp theo (nếu có)

### Phím tắt riêng cho từng trang:

#### File List Page:

- **h**: Di chuyển sang trái
- **l**: Di chuyển sang phải
- **j**: Mở file được chọn

#### Word List Page:

- **h**: Di chuyển về từ trước
- **l**: Di chuyển tới từ tiếp theo
- **j**: Xem chi tiết từ được chọn

#### Login Page:

- Không có phím tắt riêng

#### Word Detail Page:

- Không có phím tắt riêng

## Luồng điều hướng tiêu biểu:

1. **Login** → (đăng nhập) → **File List**
2. **File List** → (nhấn j trên file) → **Word List**
3. **Word List** → (nhấn j trên từ) → **Word Detail**
4. **Word Detail** → (nhấn Shift+H) → **Word List**
5. **Word List** → (nhấn Shift+H) → **File List**

## Lưu ý:

- Lịch sử trang được lưu trữ tự động
- Khi điều hướng tới trang mới (không phải back/forward), lịch sử forward sẽ bị xóa
- Debug info sẽ được in ra console để theo dõi hoạt động điều hướng
