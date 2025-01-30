import pymysql

connection = pymysql.connect(host='localhost',user='root',password='')

cursor=connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS viraj")
connection.close()