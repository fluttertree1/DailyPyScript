import sqlite3

conn = sqlite3.connect('test_1.db')

cursor = conn.cursor()

sql = "create table student (id int(11) primary key, name varchar(50), email varchar(20)) "
cursor.execute(sql)

cursor.close()
# conn.commit()
conn.close()