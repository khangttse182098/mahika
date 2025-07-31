"""
SQL Commands to set up the users table for Mahika app

Run these commands in your Railway MySQL database:
"""

# SQL to create the users table
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""

# SQL to insert the admin test user
# Password hash for: Admin@123
PASSWORD_HASH = "scrypt:32768:8:1$5FY0OttWc6RMD8mk$64de45d95a169cf1477618113b54a62b12fc9c8d09517eab9e95df1926d718fece19e8a97f4135ea869e92eea5dc0f8b304a35c64a13acbc4bfc95a846a6ac0c9e"

INSERT_USER_SQL = f"""
INSERT INTO users (email, password) VALUES ('admin@gmail.com', '{PASSWORD_HASH}')
ON DUPLICATE KEY UPDATE password = VALUES(password);
"""

print("=== MySQL Setup Commands for Mahika App ===")
print("\n1. Create the users table:")
print(CREATE_TABLE_SQL)
print("\n2. Insert the admin test user:")
print(INSERT_USER_SQL)
print("\n=== After running these commands ===")
print("You can test login with:")
print("Email: admin@gmail.com")
print("Password: Admin@123")
