# They are not stored in order in memory
person = {
    "firstname": "umer",
    "age": 20,
    "umer": 40
}

# the Key has to be unique, and immutable (!lists), if the two elements have same, the second value will override the first value

print(person["firstname"])

# what if we don't know the key of dictionaries
for key in person.keys():
    print(person[key])

for value in person.values():
    print(value)

# if we try to get access the key that doesn't exist in the dictionary, then by using normal getting method, it will throw an error, but by using "get" method, it will only return "None", we can also set the default value (if it doesn't not exist)
print(person.get("umer", 23))

# another way of creating an dictionary
person2 = dict(name="Umer Kang", age=20)
person2["firstname"] = "Kang Kang"

# This only checks for the keys, !values
if "firstname" in person2:
    print("Yay, firstname exists")

# if we want to check for values
if 20 in person2.values():
    print("20 exists")

print(person2)

# This syntax can only run for tuples, and dict.items also returns a tuple
for (key, value) in person2.items():
    print(f"{key}: {value}")

# doesn't return anything, but clear the dict
new_person = person
person.clear()

print(new_person)
print(person)

# create an new dict
new_person2 = person2.copy()
new_person2.clear()

print(new_person2)
print(person2)

# if key doesn't exist, it will add it
person2.update({"age": 55})
print(person2)
