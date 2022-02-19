# tuples are just like list, but immutable, and also iterable, and they are slightly more performant than list
my_tuple = (1, 2, 3, 4, 5, 1, 1)
print(my_tuple)

print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(5))

# tuple unpacking, here other will become a list (!tuple)
first, second, third, *other = (1, 2, 3, 4, 5, 6, 7)
print(first, second, third)
print(other)
