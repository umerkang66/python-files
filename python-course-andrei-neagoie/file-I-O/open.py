my_file = open('test.txt')

# after first time reading the cursor comes at last, so reading second and third time, will return nothing
# print(my_file.read())
# we have to move the cursor to the first position
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

print(my_file.readline())
# this one returns the array of strings
print(my_file.readlines())

my_file.close()
