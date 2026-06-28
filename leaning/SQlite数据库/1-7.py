
import pymysql

# 连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='testdb')

# 创建游标
cursor = conn.cursor()

# 执行sql语句
sql = "create table user (id int(11) primary key, name varchar(50))"
cursor.execute(sql)

# 关闭游标和数据库
cursor.close()
conn.close()
