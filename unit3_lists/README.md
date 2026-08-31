# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## My Implementation

The player inventory system was implemented using a Python list to demonstrate insertion, deletion, and search operations. I inserted items in the beginning, the middle, and the end of the inventory and then removed the items from each of those positions.

I also searched the inventory for items that existed and items that were did not exist. I also the tested edge cases by attempting to delete an item using an invalid index and by attempting to delete an item from an empty inventory. Both cases were handled and did not crashing the program.

## Reflection

I learned more about how Python lists can be used to insert, delete, and search for data throughout this assignment. Using a player inventory helped me understand these operations because items can be added or removed from different positions in the inventory. I also learned how indexes are used to control where an operation occurs in a list.

One challenge I encountered was making sure the deletion operations removed the correct items as the size of the inventory changed. After each deletion I displayed the updated inventory so I could verify that the correct item was removed every time. I also tested invalid operations like deleting from an invalid index and an empty list to make sure the program handled them without crashing.

List operations can affect performance in real world applications because inserting or deleting items may require other elements to be shifted. This becomes more important as a list grows larger. Choosing the appropriate list structure and operation can help an application manage data more efficiently.