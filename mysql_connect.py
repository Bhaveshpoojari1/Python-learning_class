import mysql.connector as connector

conn = connector.connect(host='localhost',port=3306,username = 'root',password='',database='login')
cursor = conn.cursor()

name = input("username :")
password = input("password :")

cursor.execute(f"select * from user_login where user_name = '{name}' and pass_word = '{password}' ")

data = cursor.fetchall()
print(data)