# sets are just unordered collections of unique objects, there cannot be multiple items
# in memory where sets are stored, there is not order (just like dictionaries), that's why they don't have indexes

my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set)

unique_list = []
for num in my_set:
    unique_list.append(num)

print(unique_list)

another_list = [1, 2, 3, 1, 2, 3]
print(list(set(another_list)))

print(5 in my_set)

# new_set = my_set
new_set = my_set.copy()
my_set.clear()

print(my_set)
print(new_set)

# set methods
set_1 = {1, 1, 1, 2, 3, 4}
set_2 = {3, 3, 4, 4, 5, 6}
set_3 = {7, 7, 8, 9, 9, 9}
set_4 = {1, 2, 3, 4, 5, 6}

# difference is between
# difference = set_1.difference(set_2)
# set_1.discard(5)
# set_1.difference_update(set_2)
# intersection = set_1.intersection(set_2)
# isdisjoint = set_1.isdisjoint(set_3)
# If all elements of a set is present in another set, then that is a SUBSET of another set, and another set is SUPERSET
# issubset = set_1.issubset(set_4)
# issuperset = set_4.issuperset(set_1)
# union_set = set_1.union(set_2)
# ShortHand Syntax
# union_set2 = set_1 | set_2
