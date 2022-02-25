is_friend = False
is_user = False

if is_friend and is_user:
    print("You are user and friend")
else:
    print("Either you are not a user, or not a friend, or maybe both")


if is_friend or is_user:
    print("You are user or friend")
else:
    print("You are neither friend nor user")

# Logical Operators
# > < >= <= and or ==

print("b" > "a")
print("a" > "A")

# "not"
is_employable = False
if not is_employable:
    print("You cannot be hired, better luck next time")
