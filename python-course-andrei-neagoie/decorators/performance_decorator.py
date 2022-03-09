from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        # time before running func
        time1 = time()
        result = func(*args, **kwargs)
        # time after running func
        time2 = time()
        print(f"It took {time2 - time1} seconds")
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000000):
        i * 5


long_time()
