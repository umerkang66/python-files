str_list = ["a",  "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in str_list:
    if str_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
