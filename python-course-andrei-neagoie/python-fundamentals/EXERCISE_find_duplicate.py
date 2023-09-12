str_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []

for str in str_list:
    if str_list.count(str) > 1:
        if str not in duplicates:
            duplicates.append(str)

print(duplicates)
