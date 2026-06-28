import sqlite3

# 连接
conn = sqlite3.connect("test.db")

# 创建游标
cursor = conn.cursor()

# 执行sql语句
# 建表
sql = "create table user (id int(11) primary key, name varchar(50))"
cursor.execute(sql)

# 关闭游标和数据库
cursor.close()
conn.close()
