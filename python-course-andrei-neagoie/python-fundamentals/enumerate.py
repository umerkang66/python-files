# enumerate will give you a tuple with first element as index, and the second is element itself
for index, char in enumerate("umerkang"):
    print(f"At index: {index} char is --> {char}")

# this also works on lists and tuples
nums = [34, 35, 36, 37, 38, 39, 40]
for index, element in enumerate(nums):
    print(f"At index: {index} element is --> {element}")

nums_tuple = (34, 35, 36, 37, 38, 39, 40)
for index, element in enumerate(nums_tuple):
    print(f"At index: {index} tuple element is --> {element}")
