matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for index, row in enumerate(matrix):
    for col in row:
        print(col, end=" ")
    if index != len(matrix) - 1:
        print("\n")
