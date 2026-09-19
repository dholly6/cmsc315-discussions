# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:
## Discussion Board Reflection

While completing this assignment, I learned how Python dictionaries can work like hash tables by storing information as key-value pairs. For my program, I created a video game inventory where the item name was the key and the amount owned was the value. I practiced adding items, looking them up, updating quantities, and removing items.

One challenge was handling an item that was not in the inventory. Instead of letting the program cause an error, I used get() to return a message when an item could not be found. I also checked if an item existed before trying to delete it.

Hash tables make searching for information more efficient because a hash function helps determine where a key's value is stored instead of searching through every item one at a time. A collision can happen when two different keys are assigned to the same location. When collisions happen, the system has to use a method to handle them, which can slow down searches if there are too many.
