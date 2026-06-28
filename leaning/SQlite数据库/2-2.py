import sqlite3

conn = sqlite3.connect('test_1.db')

cursor = conn.cursor()
try:
    sql = "insert into student (id,name,email) values ('3','失效饭','123456qq.com')"
    cursor.execute(sql)
except:
    conn.rollback()
finally:
    cursor.close()
    conn.commit()
    conn.close()