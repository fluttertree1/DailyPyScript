import sqlite3

conn = sqlite3.connect('test_1.db')

cursor = conn.cursor()
try:
    sql = "select * from student"
    cursor.execute(sql)

    result = cursor.fetchall()
    print(result)
except:
    conn.rollback()
finally:
    cursor.close()
    # conn.commit()
    conn.close()