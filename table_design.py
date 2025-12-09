print("Welcome to the world of the table ")

print("available table is 8")
print("want to aceess pls enter the pass word")
i=1
enter_password= str(input("pls enter the password :"))
pass_word = "Bhavesh@123"

#enter_password= input(int("pls enter the password"))
while enter_password !=pass_word:
    print("wrong password")
print("Access grant!")


number = int(input("enter which table you wanted : "))
for i in range(0,10):
    print(i*number)
print("the table of",number,"IS:")