# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

While completing this assignment, I learned how Bubble Sort and Merge Sort organize data in different ways. I used video game scores to test both algorithms and compared their results using two datasets. I also tested empty and already sorted lists to make sure both algorithms handled those cases correctly.

The biggest challenge was understanding how Merge Sort uses recursion. Bubble Sort was easier for me to follow because it compares neighboring values and swaps them when they are out of order. Merge Sort was more complicated because it divides the list into smaller parts and then combines them in sorted order. Breaking the process into separate functions helped me understand it.

Bubble Sort is useful for small lists or lists that are already nearly sorted, especially when it can stop early if no swaps are needed. However, it can become slow with larger datasets because it may need many comparisons. Merge Sort is more efficient for large datasets because its time complexity is O(n log n), compared with Bubble Sort's O(n²) worst case. The tradeoff is that Merge Sort needs extra memory when merging the lists.
