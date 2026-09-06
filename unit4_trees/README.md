# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Reflection

Discussion post 4 tought me how a Binary Search Tree organizes data using nodes with left and right child references. I also learned how recursion can be used to insert values, search values, and how to perform an in-order traversal. The in-order traversal waas a great vissual to show how a BST keeps smaller values on the left and larger values on the right.

The biggest challenge I encountered was making sure the recursive methods returned the correct node references. An indentation issue caused some nodes to become disconnected thus causing some search results to return incorrect values. After reviewing the recursive logic I could see that the return statements were places incorrectly so making sure the return statements were placed outside the conditional blocks when necessary fixed the issue.

BSTs can help improve performance because each comparison can reduce the search to either the left or right subtree instead of checking every item. Though if values are inserted in sorted order the tree can become unbalanced and behave more like a linked list which reduces its efficiency.