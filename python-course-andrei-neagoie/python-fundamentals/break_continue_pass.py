my_list = [23, 24, 25, 26, 27, 28]

i = 0
while i < len(my_list):
    if my_list[i] == 25:
        i += 1
        # break will break out of the loop, but continue will break out of the current iteration, and directly goes to the next iteration
        continue
    print(my_list[i])
    i += 1

# pass can be used as placeholder, it actually does nothing, it just pass it to the next line
for item in my_list:
    # still thinking about it what to do
    pass
