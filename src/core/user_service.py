from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class UserService():
    def __init__(self):
        self.client=MongoClient(os.getenv("MONGO_URI"))
        self.db=self.client[os.getenv("DB_NAME")]
        self.collection=self.db[os.getenv("COLLECTION_NAME")]

        try:
            self.client.admin.command('ping')
            print("Connect success")
        except Exception as e:
            print(e)

    def login(self, username, password):
        try:
            user=self.collection.find_one({"username": username})
            if user:
                if user["password"] == password:
                    return {"status": 200, "message": "Bạn đã đăng nhập thành công!"}
                else:
                    return {"status": 401, "message": "Bạn đang nhập sai mật khẩu!"}
            else:
                return {"status": 401, "message": "Không tìm thấy tên đăng nhập của bạn"}
        except Exception as e:
            return {"status": 500, "message": "Lỗi từ hệ thống"}