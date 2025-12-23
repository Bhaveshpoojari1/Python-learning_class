
#its create a add update and delete via case statement using list

user = int(input("Enter Value : 1. add 2. delete 3. show 4. exit"))
l1 = []
while user != 4:
    match user:
        case 1:
            userinput ="";
            l1.append(userinput)
        case 2:
            pass
        case 3:
            print(l1)
        case 4:
            exit()
        case _:
            print("invalid")
            exit()