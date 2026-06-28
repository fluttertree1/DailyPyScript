import sqlite3
import logging
# 配置日志
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fileHandle = logging.FileHandler(filename="loggingDemo.log", mode='a', encoding='utf-8')
fileHandle.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(message)-45s | %(filename)10s | %(lineno)s | %(levelname)s')
fileHandle.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

logger.addHandler(fileHandle)
logger.addHandler(consoleHandler)

# 连接数据库
conn = sqlite3.connect('test_1.db')
cursor = conn.cursor()
# 创建表
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company(
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            age INT(3),
            email TEXT UNIQUE
        )
    ''')
    logger.info("创建成功")
except sqlite3.Error as e:
    logger.info(f"创建列表失败：{e}")
# 插入数据
try:
    cursor.execute("INSERT INTO company (id,name,age) values(?,?,?)", (1, 'mdh', 20))
    conn.commit()
    logger.info("插入成功")
except sqlite3.Error as e:
    logger.info(f"插入失败：{e}")
