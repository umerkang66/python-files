# list comprehensions
# my_list = [param for param in iterable]

my_list = [char.upper() for char in 'umerkang' if char > "k"]
print(my_list)

nums_list = [num * 2 for num in range(0, 10)]
print(nums_list)

nums_list_even = [num for num in range(0, 10) if num % 2 == 0]
print(nums_list_even)


# dict comprehensions
# my_dict = {item: item for item in iterable}
person_list = [("name", "umer"), ("age", 20), ("course", "computer science")]
my_dict = {key: value for key, value in person_list}
print(my_dict)


person = {
    'name': 'umer',
    'age': 20,
    'course': 'computer science'
}

person_dict = {key: value for key, value in person.items()}

print(person_dict)

nums_dict = {num: num ** 2 for num in [101, 102, 103, 104]}
print(nums_dict)

# set comprehensions
# my_set = {set_item for set_item in iterable}
my_set = {item for item in [1, 2, 3, 4, 4, 4] if item > 1}
print(my_set)
