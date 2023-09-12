# if we add decorators to a function, that will supercharge that function


# this is the syntax of writing decorator, it gets a function as argument, then it wraps that function in another function, after that it returns the wrapper function, "simple_func" will become wrapped function
def my_decorator(func):
    # this func will be called when we call the function after decorating it, so this func will receive arguments
    def wrap_func(*arg, **kwargs):
        # unpack the arguments
        func(*arg, **kwargs)

    return wrap_func


@my_decorator
def simple_func(arg, arg2):
    print("simple function")
    print(arg, arg2)


# it is like calling the my_decorator passing the simple function, then call the returned function
simple_func("called from my_decorator", "umer")
