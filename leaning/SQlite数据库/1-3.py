import sqlite3

# 连接
conn = sqlite3.connect("test.db")

# 拿到游标
cursor = conn.cursor()

# 执行sql语句
# 查询
sql = "select * from user"
cursor.execute(sql)

results = cursor.fetchall()
print(results)

for r in results:
    print("我是%d号，我叫%s" %r)

# 关闭游标和数据库
cursor.close()

# conn.commit()
conn.close()
