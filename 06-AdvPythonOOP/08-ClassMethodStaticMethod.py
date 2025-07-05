class PlayerCharacter:
    # Class object Attribute, not dynamic
    membership = True

    # This is the constructor method, which automatically called when object is instantiated
    def __init__(self, name, age):
        if (age > 18):
            self.name = name  # Attributes or Properties, dynamic
            self.age = age  # Attributes or Properties, dynamic

    def run(self):
        print(f"{self.name} is Running.....")
        return f"{self.name} is done"

    def shout(self):
        print(f"i am {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Maheen", 19)
print(player1.name, player1.age)
print(player1.run())
# print(player1.membership)
# print(player1.shout())
print(player1.adding_things(1, 2))

# player2 = PlayerCharacter("Minahil", 6)
# print(player2.name, player2.age)
# print(player2.run())
# print(player2.membership)
# print(player2.shout())
print(PlayerCharacter.adding_things(5, 6))  # <==== Class methods can call even if no object is instantiated
