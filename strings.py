name = "Bhavesh Poojari     "

print(name)

print(name.upper())
print(name.lower())
print(name.capitalize()) # it will create a starting letter of string capitalize

name1 = name.strip()
print(name1.strip())
print(name1.center(50,"-"))
print(name1.find('esh'))
print(name1.index("esh"))
print(name1.isdigit())
print('22s'.isdigit())
print('Bhavesh'.isalpha())
print('Bhavesh23'.isalnum())
print('bhavesh'.isupper())
print("bhavesh".islower())

print(" - ".join(name1))


