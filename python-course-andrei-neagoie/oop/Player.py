class PlayerCharacter:
    membership = True

    def __init__(self, name, birthYear):
        if self.membership:
            self._name = name
            self._birthYear = birthYear

    def _get_age(self, currentYear):
        return currentYear - self._birthYear

    def speak(self):
        print(f"My name is {self._name}, and I am {self._get_age(2022)} years old")

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


umer = PlayerCharacter.adding_things(2000, 1)
umer.speak()

print(PlayerCharacter.adding_things2(23, 12, 12, 32, 23))

# Multiple methods are added into class, this is called encapsulation

# By adding methods we can abstract away the implementation details
