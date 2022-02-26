class PlayerCharacter:
    membership = True

    def __init__(self, name, birthYear):
        if self.membership:
            self.name = name
            self.birthYear = birthYear

    def get_age(self, currentYear):
        return currentYear - self.birthYear
