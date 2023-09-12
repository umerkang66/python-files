def is_even(num):
    return num % 2 == 0


print(is_even(50))


# parameters (that can also be default)
def say_hello(name="any name", emoji="🤣🤣🤣"):
    """
    This prints the name, and emoji that you will provide
    """
    print(f"Hello {name} {emoji}")


# positional arguments
say_hello("Umer", "💥💥💥")

# keyword arguments
say_hello(emoji="😀😀😀", name="kang")

# Find out about the function itself
print(say_hello.__doc__)
help(say_hello)
