def special_for(iterable):
    # this "iter" function is going to allow us to use the next function
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        # StopIteration will automatically be caught by for loop's next function
        except StopIteration:
            break


special_for([1, 2, 3])

print('--------')

# create our own generator, this is range() work under the hood
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # we are able to use the for loop because this is now an iterable, and next dunder method is also defined, which is by default is not defined in normal class (that is only defined in iterables like list)
    def __iter__(self):
        return self

    # this is how "next" work under the hood, when we iterate over something like range, this use "next" dunder method, we are defining our own dunder method here
    def __next__(self):
        if self.current <= self.last:
            num = self.current
            self.current += 1
            return num
        # for loop will automatically catches that loop will stop looping
        raise StopIteration


gen = MyGen(0, 10)
for i in gen:
    print(i)
