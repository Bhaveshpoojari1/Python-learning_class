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



#continuos table code design without stop a code run 
code:

print("wlc Bhavesh Poojari")
print("Welcome to the world of table")
print("")
print("")

pass_word = "Bhavesh@123"

while True:
    pass_input = str(input("Pls enter the password:"))
    
    if pass_input == pass_word:
        print("Access Granted")
        break #exit the password
    else:
        print("Access Denied Wrong Password")
        
while True:
    print("-" * 30) #visual separator for new request 
    print("Wlc to the world of the table")
    try:
        table = int(input("pls enter the the table you want to display(Or type exit to quit:"))
        
        
        print(f"the table of {table}--")
        
        for i in range (0,11):
            print(table,"*",i,"=",i*table)
    except ValueError:
        print("Invalid Input pls enter the valid integer of the table number.")
