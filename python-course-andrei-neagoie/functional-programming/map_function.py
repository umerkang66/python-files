from functools import reduce


nums_list = [1, 2, 3, 4]


# map
def multiply_by_2(num):
    return num * 2


double_nums = list(map(multiply_by_2, nums_list))
print(double_nums)


# filter
def filter_even(num):
    return num % 2 == 0


even_nums = list(filter(filter_even, nums_list))
print(even_nums)


# zip
your_list = [10, 20, 30, 40]

# this will zip items at the same index together, if the one of the list of tuple doesn't have anything at the current_index of first tuple or list, then that simply will not be added
print(list(zip(nums_list, your_list)))

# reduce
nums2 = [1, 2, 3]


def accumulator(previousValue, currentValue):
    return previousValue + currentValue


# if we didn't provide the initial value, the initial value will automatically becomes zero
total = reduce(accumulator, nums2, 0)
print(total)
