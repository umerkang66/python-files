list_with_duplicates = ['a', 'b', 'c', 'b', 'd', 'n', 'm', 'n']


# get only duplicates separate in only_duplicates list
only_duplicates = list(set([
    char for char in list_with_duplicates if list_with_duplicates.count(char) > 1]))


print(only_duplicates)
