import sqlite3

# 连接
conn = sqlite3.connect("test.db")

# 拿到游标
cursor = conn.cursor()

# 执行sql语句
# 更新语句
sql = "update user set name='糙职阶' where id=1"
cursor.execute(sql)

sql = "select * from user"
cursor.execute(sql)

results = cursor.fetchall()

for r in results:
    print("我是%d号，我叫%s" % r)

# 关闭游标和数据库
cursor.close()

conn.commit()
conn.close()
