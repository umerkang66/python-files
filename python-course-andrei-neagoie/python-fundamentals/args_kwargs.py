# arguments and keyword_arguments
# *args will collect all the non-named arguments, in the tuple, and **kwargs will collect all the name arguments in a dictionary
def super_func(*args, **kwargs):
    print(args)
    print(kwargs)


super_func(1, 2, 3, 4, 5, name="umer", age=20, course="computer science")

# RULE: params, *args, default params, **kwargs
# according to this rule


def super_func2(firstname, *args, default_param="hi", **kwargs):
    print(firstname)
    print(default_param)
    print(args)
    print(kwargs)


super_func2(
    "umer", 1, 2, 3, 4, 5, name="umer", age=20, course="computer science"
)


def highest_even(*args):
    highest = 0
    for num in args:
        if num % 2 == 0 and num > highest:
            highest = num
    return highest


print(highest_even(10, 19, 2, 3, 4, 8, 11))
