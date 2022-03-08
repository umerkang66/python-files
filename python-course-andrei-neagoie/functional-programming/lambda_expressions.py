from functools import reduce


nums = [4, 6, 8, 9]

new_list = list(map(lambda num: num * 2, nums))
print(new_list)

new_filtered_list = list(filter(lambda num: num % 2 == 0, nums))
print(new_filtered_list)


reduced_num = reduce(lambda prev, num: prev + num, nums)
print(reduced_num)

list4 = [5, 4, 3]

square_list4 = list(map(lambda num: num ** 2, list4))
print(square_list4)


unsorted_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
# by default it will sort using first key
unsorted_list.sort(key=lambda nums_tuple: nums_tuple[1])

print(unsorted_list)
