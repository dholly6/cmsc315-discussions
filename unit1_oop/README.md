# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

# My Implementation

I decided to create a video game character system using object oriented programming for discussion 1. I created a parent class called "gameCharacter" that stored the characters name and healh. Then I created a child class called "Player" that inherited from "gameCharacter" and added a level, inventory, and attack method to the player.

I demonstrated class and instance namespaces by creating two player objects and adding a special ability to only one of them. I also demonstrated shallow and deep copying using a players inventory. When the original inventory was changed, the shallow copy reflected the change because the nested list was shared, while the deep copy remained unchanged.

For my student created extension, I added a "take_damage" method. This method reduced a characters health while preventing health from dropping below zero. I also handeled negative damage as an invalid input.

## Case Testing

I tested the "take_damage" method with normal damage, damage greater than the character remaining health, and negative damage. Damage greater than the remaining health stopped the characters health at zero instead of allowing a negative value. Negative damage returned a error message and did not increase the characters health.