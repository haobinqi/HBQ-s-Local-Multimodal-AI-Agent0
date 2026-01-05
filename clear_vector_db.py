# clear_vector_db.py
import shutil
import os

DB_PATH = "vector_db/chroma"

if os.path.exists(DB_PATH):
    shutil.rmtree(DB_PATH)
    print(f"已删除数据库文件夹: {DB_PATH}")
else:
    print(f"数据库文件夹不存在: {DB_PATH}")
