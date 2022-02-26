# := This operator can assign the value to a variable in an expression

name = "umerkang"

if (length := len(name)) > 5:
    print(f"Too long {length} elements")
