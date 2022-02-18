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

# cart.count() will tell us how many times a certain element has occur in list
print(cart.count("second_index"))

print("second_index" in cart)

print(cart)
