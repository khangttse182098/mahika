import sys
import os
sys.path.append('e:\\FPTU\\SU25\\EXE202\\Project\\mahika')

from src.core.user_service import UserService
from werkzeug.security import generate_password_hash, check_password_hash

def test_mysql_connection():
    print("Testing MySQL connection...")
    user_service = UserService()
    
    # Test connection
    print(f"Connection status: {'Connected' if user_service.conn and user_service.conn.is_connected() else 'Failed'}")
    
    # Test login with non-existent email (should return 401)
    print("\n--- Test 1: Non-existent email ---")
    result = user_service.login("test@example.com", "test123")
    print(f"Login test result: {result}")
    
    # Test password hash functionality
    print("\n--- Test 2: Password hash verification ---")
    test_password = "Admin@123"
    password_hash = "scrypt:32768:8:1$sRw4q7MSC6dV4GmL$50ac6dcb2e42c26381ad0f8be61844f66b9ba5b5ced35c937762a28d1f92eff90bb55e4f42ddb43feb141e4d24b7779720478d0938e608d71073e156442fa9d180"
    
    is_valid = check_password_hash(password_hash, test_password)
    print(f"Password verification for 'Admin@123': {is_valid}")
    
    # Show what the expected database record would look like
    print("\n--- Expected Database Record ---")
    print("Email: admin@gmail.com")
    print("Password Hash:", password_hash)
    print("\nTo test the full login flow, you would need to:")
    print("1. Create a 'users' table in your MySQL database")
    print("2. Insert a record with email='admin@gmail.com' and the password hash above")
    print("3. Then test login with email='admin@gmail.com' and password='Admin@123'")

if __name__ == "__main__":
    test_mysql_connection()
