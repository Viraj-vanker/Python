import pymysql

connection = pymysql.connect(host='localhost',user='root',password='',database='viraj')

cursor=connection.cursor()

sql="INSERT INTO students(name, age, grade) VALUES (%s, %s, %s)"
values = ("Viraj",20,"A")
cursor.execute(sql,values)
connection.commit()
connection.close()