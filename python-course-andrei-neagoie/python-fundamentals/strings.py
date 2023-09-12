name = "umer is my name"

# by doing all of the operations, original string is not changed
# get access from certain index to certain index, the last index will not be included
print(name[2:8])

# [start:stop:stepover]
# "stepover" is how many items to stepover, the default is 1, because we are going one by one, but can change it
print(name[0:8:2])

# In python the negative index means start at the end of list or string

# reverse a string
# it means start from zero, end from the last element, stepover from the last element means reverse it
print(name[::-1])

# IMMUTABILITY
# strings in python are immutable, means they cannot be changed
immutable_str = "my name is umer"
# immutable_str[0] = "y"

# CALCULATING THE LENGTH OF THE STRING
length_of_str = len(immutable_str)
print(length_of_str)

# STRING METHODS
# upper() method doesn't change the original string
print(name.upper())
# capitalize the first element of the string
print(name.capitalize())

# returns the starting from where it starts
print(name.find("is"))

# this replaces all the occurrences of "is", and returns the new string, don't mutate the original string
print(name.replace("is", "are"))

name = "umer is my name"
print(name[::-1])
