num = 0
while num <= 20:
    print(num)
    num += 1
# when this loop will end this else block will run, and if there is a BREAK in while loop this else block will not run (it will only run when while condition become false)
else:
    print("Done all the work")

while True:
    response = input("Say something: ")
    if response == "bye":
        break
