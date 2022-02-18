name = "umer is my name"

# get access from certain index to certain index, the last index will not be included
print(name[2:8])

# [start:stop:stepover]
# "stepover" is how many items to stepover, the default is 1, because we are going one by one, but can change it
print(name[0:8:2])

# In python the negative index means start at the end of array or string

# reverse a string
# it means start from zero, end from the last element, stepover from the last element means reverse it
print(name[::-1])
