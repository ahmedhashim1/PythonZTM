class PlayerCharacter:
    # Class object Attribute, not dynamic
    membership = True

    # This is the constructor method, which automatically called when object is instantiated
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name  # Attributes or Properties, dynamic
            self.age = age  # Attributes or Properties, dynamic

    def run(self):
        print(f"{self.name} is Running.....")
        return f"{self.name} is done"

    def shout(self):
        print(f"i am {self.name}")


player1 = PlayerCharacter("Maheen", 6)
print(player1.name, player1.age)
print(player1.run())
print(player1.membership)
print(player1.shout())

player2 = PlayerCharacter("Minahil", 6)
print(player2.name, player2.age)
print(player2.run())
print(player2.membership)
print(player2.shout())
