"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class GameCharacter:
    character_count = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health
        GameCharacter.character_count += 1

    def display_info(self):
        return f"name: {self.name}, Health: {self.health}"

    #TODO 6 Additional feature: Damage system
    def take_damage(self, damage):
        if damage < 0:
            return "Damage cannot be negative."

        self.health = max(0, self.health - damage)
        return f"{self.name} now has {self.health} health."


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Player(GameCharacter):
    player_type = "Playable"

    def __init__(self, name, health, level, inventory):
        super().__init__(name, health)
        self.level = level
        self.inventory = inventory

    def display_info(self):
        return f"Name: {self.name}, Health: {self.health}, Level: {self.level}"

    def attack(self):
        return f"{self.name} attacks the enemy!"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    player1 = Player("Knight", 100, 5, ["Sword", "Potion"])
    player2 = Player("Wizard", 80, 7, ["Staff", "Spell Book"])

    #Access class variable through the class
    print("Player type through class:", Player.player_type)

    #Access class variable through an object
    print("Player type through object:", player1.player_type)

    #Add an attribute to only player1
    player1.special_ability = "Power Strike"

    #Display each object's namespace
    print("Player 1 namespace:", player1.__dict__)
    print("Player 2 mamespace:", player2.__dict__)

    #Display information about the class namespace
    print("Player class namespace:", Player.__dict__)



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original_player = Player(
        "Warrior",
        100,
        10,
        ["Sword", "Shield"]
    )

    #Create a shallow copy and a deep copy
    shallow_player = copy(original_player)
    deep_player = deepcopy(original_player)

    #Modify the nested inventory list of the original player
    original_player.inventory.append("Health Potion")

    #A shallow copy shares the nested inventory list with the original.
    #A deep copy creates its own separate copy of the inventory list.
    print("Original inventory:", original_player.inventory)
    print("Shallow copy inventory:", shallow_player.inventory)
    print("Deep copy inventory:", deep_player.inventory)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    character = GameCharacter("Goblin", 50)
    print(character.display_info())
    print(character.take_damage(20))
    print(character.take_damage(100))
    print(character.take_damage(-10))


    print("\n=== Child Object ===")
    player = Player("Knight", 100, 5, ["Sword", "Potion"])
    print(player.display_info())
    print(player.attack())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()