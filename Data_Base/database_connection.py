import pymysql

connection = pymysql.connect(host='localhost',user='root',password='',database='viraj')

if connection.open:
    print("connection establised !")
connection.close