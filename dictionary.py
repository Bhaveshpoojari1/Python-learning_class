# changable ordered duplicates not allowed

person = {
    "name" : "prasad",
    "age" : 21,
    "gender" : "male",
    "hobby" : ["dancing","singing"]
}

print(person.get("name"))

# add
person['color'] = "red"
print(person)

# remove
del person['color']
del person['hobby'][1]
print(person)

# update 
person['age'] = 36
print(person)

# This code is going to be used for a arrange a value in the form of a horixzontal to vertical value.

# for loop going to bre used 
for i,val in person.items():
    print(i,":",val)

