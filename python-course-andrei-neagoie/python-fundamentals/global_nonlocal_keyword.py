total = 0


def count():
    total = 10

    def count2():
        # nonlocal will see the total outside of this scope
        nonlocal total
        # but global will go straight to the global and there try to find the total
        # global total
        total += 1
        return total

    return count2()


print(count())
