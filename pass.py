#password code 
#This code going to be used like a for loop to print a continuos wait for the some time to input a password to be print like a print defination 
import time
print("welcome bhavesh")

name = input("Enter your name:")
while name !="Bhavesh":
    name=input("Enter your name:")
password = input("Pls enter your password:")
attempt = 0
while password !="Bhavesh@123":
    attempt +=1
    if attempt >=5:
        time.sleep(1)
        print("maximum attept reached you device temporary locked.")
        for i in range(5):
            time.sleep(1)
            print(5-i,"second until next attempt")
        attempt = 0
    print(f"only {5-attempt} attempsts remaining")
    password = input("Enter your password again:")
#print("wait bhavesh")
print(f"welcome ,{name}")