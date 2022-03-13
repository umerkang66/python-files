def fib(number):
    prev_num = 0
    next_num = 1
    for _ in range(number):
        # by adding yield this will become generator
        yield prev_num
        temp = prev_num
        # previous number will become next number where loop in ended
        prev_num = next_num
        # next num will sum of two numbers (one own its own) and will become the next one
        next_num = temp + next_num


# by using generators, we are not keeping anything in the memory
fib_list = []
for x in fib(10):
    fib_list.append(x)
print(fib_list)


# without generators
def fib2(number):
    prev_num = 0
    next_num = 1
    fib_list = []
    for _ in range(number):
        fib_list.append(prev_num)
        temp = prev_num
        # previous number will become next number where loop in ended
        prev_num = next_num
        # next num will sum of two numbers (one own its own) and will become the next one
        next_num = temp + next_num
    return fib_list


print(fib2(10))
