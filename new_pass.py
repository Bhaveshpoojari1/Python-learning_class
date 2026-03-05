#password code
# This code going to be used for the removing the for loop not want to print like attemp second wait like to print statement continuously 

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
        time.sleep(5)
        print("maximum attept reached you device temporary locked.")
       # for i in range(5):
            #time.sleep(1)
            #print(5-i,"second until next attempt")
        attempt = 0
    print(f"only {5-attempt} attempsts remaining")
    password = input("Enter your password again:")
#print("wait bhavesh")
print(f"welcome ,{name}")