class PlayerCharacter:
    # This is the constructor method, which automatically called when object is instantiated
    def __init__(self, name, age):
        self.name = name  # Attributes or Properties
        self.age = age  # Attributes or Properties

    def run(self):
        print(f"{self.name} is Running.....")
        return f"{self.name} is done"


player1 = PlayerCharacter("Maheen", 6)
print(player1.name, player1.age)
print(player1.run())

player2 = PlayerCharacter("Minahil", 6)
print(player2.name, player2.age)
print(player2.run())
