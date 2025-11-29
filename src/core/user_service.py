import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from werkzeug.security import check_password_hash

load_dotenv()

class UserService():
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.database = os.getenv("DB_NAME", "railway")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.conn.is_connected():
                print("MySQL connection success")
        except Error as e:
            print(f"MySQL connection error: {e}")
            self.conn = None

    def login(self, email, password):
        if not self.conn or not self.conn.is_connected():
            print("Cannot connect to database")
            return {"status": 500, "message": "Không thể kết nối tới cơ sở dữ liệu"}
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            cursor.close()
            print(f"Fetched user: {user}")
            if user:
                # Check if user has paid (has_paid = 1)
                has_paid = user.get("has_paid", 0)
                if has_paid != 1:
                    return {"status": 403, "message": "Tài khoản của bạn chưa được kích hoạt. Vui lòng thanh toán để sử dụng dịch vụ."}
                
                # Try different possible column names for password
                stored_password = None
                if "password_hash" in user:
                    stored_password = user["password_hash"]
                elif "password" in user:
                    stored_password = user["password"]
                elif "pass" in user:
                    stored_password = user["pass"]
                
                if stored_password is None:
                    return {"status": 500, "message": f"Không tìm thấy cột password trong database. Columns available: {list(user.keys())}"}
                
                # Check if password is hashed (starts with hash algorithm name) or plain text
                if stored_password.startswith(('pbkdf2:', 'scrypt:', 'argon2:', '$2b$', '$2a$', '$2y$')):
                    # Password is hashed, use check_password_hash
                    if check_password_hash(stored_password, password):
                        return {"status": 200, "message": "Bạn đã đăng nhập thành công!"}
                    else:
                        return {"status": 401, "message": "Bạn đang nhập sai mật khẩu!"}
                else:
                    # Password is plain text, compare directly
                    if stored_password == password:
                        return {"status": 200, "message": "Bạn đã đăng nhập thành công!"}
                    else:
                        return {"status": 401, "message": "Bạn đang nhập sai mật khẩu!"}
            else:
                return {"status": 401, "message": "Không tìm thấy email của bạn"}
        except Exception as e:
            return {"status": 500, "message": f"Lỗi từ hệ thống: {e}"}
