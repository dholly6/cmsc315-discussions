"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary for a video game inventory.
    game_inventory = {}

    # A dictionary behaves like a hash table by storing data
    # as key-value pairs. The item name is the key and the
    # number owned is the value.
    game_inventory["Health Potion"] = 5
    game_inventory["Mana Potion"] = 3
    game_inventory["Iron Sword"] = 1
    game_inventory["Wood"] = 20
    game_inventory["Gold"] = 100

    print("Game inventory:", game_inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # The key is used to quickly find its matching value.
    print("Health Potions:", game_inventory["Health Potion"])
    print("Gold:", game_inventory["Gold"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", game_inventory)

    # Assigning a new value to an existing key replaces its old value.
    game_inventory["Gold"] = 150

    print("After update:", game_inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", game_inventory)

    # Removing a key also removes the value connected to that key.
    del game_inventory["Iron Sword"]

    print("After deletion:", game_inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: get() safely returns a message when a key is missing.
    missing_item = game_inventory.get("Diamond", "Item not found")
    print("Diamond lookup:", missing_item)

    # Edge case 2: Check for a key before trying to delete it.
    if "Magic Shield" in game_inventory:
        del game_inventory["Magic Shield"]
    else:
        print("Magic Shield cannot be deleted because it is not in the inventory.")


if __name__ == "__main__":
    main()
