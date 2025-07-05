class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # this will call parent class's method
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)  # Alternate method of User__init__(self, email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left {self.num_arrows}")


wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("Robin", 100, "robin@gmail.com")


def player_attack(char):
    char.attack()


# player_attack(wizard1)
# player_attack(archer1)

# OR

for char in [wizard1, archer1]:
    player_attack(char)  # will produce same out as above

print(wizard1.email)
print(archer1.email)
