import mysql.connector as connector
import time

print("Welcome,Bhavesh")

conn = connector.connect(host='localhost', port=3306, user='root', password='', database='login')
cursor = conn.cursor()

name = input("username : ")

password = input("password : ")

attempt = 0

while True:
    cursor.execute("select * from user_login where user_name=%s and pass_word=%s",(name,password))
    data = cursor.fetchall()

    if data:
        print(f"Welcome,{name}")
        print(data)
        break
    else:
        attempt += 1
        if attempt >= 5:
            time.sleep(2)
            print("Maximum attempt reached your account is temporary locked")
            break

        print(f"only {5-attempt} attempts remaining")
        password = input("Enter your password again:")

conn.close()