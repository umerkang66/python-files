class User:
    def __init__(self, firstname, age):
        self.firstname = firstname
        self.age = age

    def sign_in(self):
        print(f"\"{self.firstname}\", with age \"{self.age}\", is singed in")


class Wizard(User):
    def __init__(self, firstname, age, power):
        super().__init__(firstname, age)
        self.power = power

    def attack(self):
        print(f"{self.firstname} is attacking with the power of {self.power}")


class Archer(User):
    def __init__(self, firstname, age, arrows):
        super().__init__(firstname, age)
        self.arrows = arrows

    def attack_arrows(self):
        print(f"{self.firstname} is attacking with the arrows of {self.arrows}")


class HybridBorg(Wizard, Archer):
    def __init__(self, firstname, age, power, arrows):
        Archer.__init__(self, firstname, age, arrows)
        self.power = power


hybrid_borg = HybridBorg("umer", 20, 150, 300)
hybrid_borg.attack_arrows()
hybrid_borg.attack()
