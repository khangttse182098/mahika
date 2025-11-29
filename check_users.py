import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    
    cursor = conn.cursor(dictionary=True)
    
    # Show all tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("=== Available Tables ===")
    for table in tables:
        print(table)
    
    # Show users table structure
    cursor.execute("DESCRIBE users")
    columns = cursor.fetchall()
    print("\n=== Users Table Structure ===")
    for col in columns:
        print(col)
    
    # Show all users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(f"\n=== All Users ({len(users)} records) ===")
    for user in users:
        print(user)
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
