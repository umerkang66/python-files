cart = ["notebook", "sunglasses", "toys", "grapes", "second_index"]

# The last option is to skip the elements between the list, by slicing original list does not change, it returns the copy of original string
print(cart[0:len(cart):2])

# Lists are immutable
cart[0] = "umer"

cart.append("umer")
cart.insert(2, "second_index")
cart.extend(["chairs", "tables"])
cart.remove("toys")
cart.pop(3)
print(cart.index("chairs"))
cart.sort()

# cart.count() will tell us how many times a certain element has occur in list
print(cart.count("second_index"))

print("second_index" in cart)

print(cart)

# Creating the list from range
list_100 = list(range(1, 100 + 1))
for num in list_100:
    list_100[num - 1] = str(num)

# Joining the string with list
number_strings = ' '.join(list_100)
print(number_strings)

# List unpacking (just like js destructuring)
first, second, third, *others = [1, 2, 3, 4, 5, 6, 7, 8]

print(first, second, third)
print(others)
