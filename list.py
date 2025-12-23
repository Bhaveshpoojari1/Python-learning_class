# lists
# ordered changable duplicates allowed
#its a process of creating a list & updating it
    
names = ["prasad","sahil","rahul","raj","rakesh"]

print(names)

# add 
names.append("sayali")
names.insert(2,"kajal")
names.extend(["jay","raj"])
print(names)

# remove
names.remove("kajal")
names.pop(5)
print(names)

# update 
names[2] = "priya"

print(names)

# loop
for i in names:
    print(i)