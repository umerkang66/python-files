num = range(5, 10 + 1)
print(list(num))

# the 3rd parameter is how much take it as a step in each iteration (default is 1, meaning every number is add in range)
num = range(0, 10 + 1, 2)
print(list(num))

# reverse range
num = range(10, 0, -1)
print(list(num))

# it can also goes toward negative numbers
num = range(10, -10 - 1, -1)
print(list(num))

# convert range into list
print(list(range(1, 10 + 1)))
