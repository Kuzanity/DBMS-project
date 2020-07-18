import pymysql
name=input()
conn = pymysql.connect(host="localhost",port=3306,db="db_oragon",user="DBMS",password="12345")
cursor = conn.cursor()
cursor.callproc('getQuantity',[name])
result=cursor.fetchone()
print(result)