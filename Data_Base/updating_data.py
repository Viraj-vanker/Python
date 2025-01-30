import pymysql

connection = pymysql.connect(host='localhost',user='root',password='',database='viraj')

cursor=connection.cursor()

sql="UPDATE students SET grade = %s WHERE name = %s"
values = ("B","viraj")
cursor.execute(sql,values)
connection.commit()
connection.close()