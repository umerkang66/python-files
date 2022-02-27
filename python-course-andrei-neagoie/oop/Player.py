class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def get_age(self, currentYear):
        return currentYear - self.age

    # we can use class state when we want to use class state
    @classmethod
    def adding_things(cls, num1, num2):
        # cls is the current class
        return cls("Umer", num1 + num2)

    # we can use class state when we don't want to use class state
    @staticmethod
    # static method doesn't have access to the cls (current class)
    def adding_things2(*nums):
        sum = 0
        for num in nums:
            sum += num
        return sum


umer = PlayerCharacter.adding_things(12, 9)
print(umer.age)

print(PlayerCharacter.adding_things2(23, 12, 12, 32, 23))
