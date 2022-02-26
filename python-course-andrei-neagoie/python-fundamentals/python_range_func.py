for num in range(5, 10 + 1):
    print(num)

# the 3rd parameter is how much take it as a step in each iteration (default is 1, meaning every number is printed)
for num in range(0, 10 + 1, 2):
    print(num)

# reverse range
for num in range(10, 0, -1):
    print(num)

# it can also goes toward negative numbers
for num in range(10, -10 - 1, -1):
    print(num)

# convert range into list
print(list(range(1, 10 + 1)))
