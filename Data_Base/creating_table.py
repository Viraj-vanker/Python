import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='viraj')

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               age INT,
               grade VARCHAR(10))

        """)

connection.close()