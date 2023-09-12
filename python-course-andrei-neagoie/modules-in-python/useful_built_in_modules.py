from collections import Counter, defaultdict, OrderedDict

my_list = [1, 2, 3, 3, 4, 5, 6, 6, 6]
print(Counter(my_list))

dictionary = defaultdict(lambda: 0, {"a": 1, "b": 2})
print(dictionary["c"])

dictionary2 = {"a": 1, "b": 2}
# dictionary2["a"] = 1
# dictionary2["b"] = 2

dictionary3 = {"b": 2, "a": 2}
# dictionary3["a"] = 1
# dictionary3["b"] = 2

# If order of insertion is not same, this will give us False,
# if it would be regular dictionary, then the order doesn't matter,
# it will always return true, IMPORTANT! in newer versions of python,
# the order of values in dictionaries is maintained
print(dictionary2 == dictionary3)
