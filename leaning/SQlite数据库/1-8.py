import pymysql

# 连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='testdb')

# 拿到游标
cursor = conn.cursor()

# 执行sql语句
sql = "insert into user (id,name) values ('2', '失效饭')"
cursor.execute(sql)
sql = "insert into user (id,name) values ('3', '秒的好')"
cursor.execute(sql)
sql = "insert into user (id,name) values ('4', '果开远')"
cursor.execute(sql)
sql = "insert into user (id,name) values ('5', '梨好甜')"
cursor.execute(sql)

# 关闭游标和数据库
cursor.close()

conn.commit()
conn.close()
