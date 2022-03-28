with open('files/file-1.py', mode="r") as file_1:
    print(file_1.read())

with open('./files/file-1.py', mode="r") as file_1:
    print(file_1.read())
