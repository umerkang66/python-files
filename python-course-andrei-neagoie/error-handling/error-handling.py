while True:
    try:
        birth_year = int(input("What is your birth_year?\n"))
        age = 2022 - birth_year
        10 / birth_year
        print(f"Your age is {age}")
    except ValueError:
        print("Please enter a number")
        break
    except ZeroDivisionError:
        print("Please enter age higher than 0")
        break
    else:
        # if there is no error this will run
        print("Thank you")
        break
    finally:
        print("ok, iam finally done")


def sum(num1, num2):
    try:
        num1 / num2
        return num1 + num2
    # We can accept multiple errors
    except (TypeError, ZeroDivisionError) as err:
        print(f"Error: {err}")


print(sum(1, 0))
