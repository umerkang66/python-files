# by using this we don't have to close the file
# it has also the default parameter, mode=r, means read
with open("test.txt", mode='r') as my_file:
    text_list = my_file.readlines()


# write files, mode can be "w" for write, and "r+" for read and write, it can also be "a", for append mode
# if we have "write" mode, the new content will override the content, and delete the previous content
# if we have "read and write" mode, then contents will be changes (of the previous file) till the cursor of new content, rest of the content (of the previous file) will remain the same
with open("happy.txt", mode="r+") as my_file:
    # text is int, tells us how many chars we have write
    text = my_file.write(":)")
    print(text)


# if we want to write a file that doesn't exit, it will be created in the write mode "w", it will not be created in read mode "r", and read-write mode "r+"
