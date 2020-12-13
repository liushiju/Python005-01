#!/venv1/bin/python
import pymysql

# 配置项正常会写到一个配置文件中
db = pymysql.connect("192.168.0.168", "testuser", "testpass", "testdb")

try:
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()
except Exception as e:
    print(f"fetch error {e}")
finally:
    db.close()

print(f"Database version : {result} ")
