# generators are iterable, but not every iterable is generator, like range() is generator, it create the range between 2 numbers, 1 by 1


# by using the yield keyword it becomes the generator
def generator_function(num):
    for i in range(num):
        # yield pauses the function, and next item iteration is run when next() is called
        yield i


# iteration also call the next in the generator
for item in generator_function(10):
    print(item)

g = generator_function(10)
print(next(g))
print(next(g))
print(next(g))
