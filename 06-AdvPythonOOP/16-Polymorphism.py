class User():
    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # this will call parent class's method
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left {self.num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)


def player_attack(char):
    char.attack()


# player_attack(wizard1)
# player_attack(archer1)

# OR

for char in [wizard1, archer1]:
    player_attack(char)  # will produce same out as above
