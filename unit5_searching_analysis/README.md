# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

While completing this assignment, I learned more about how linear search and binary search work and why the way data is organized matters. Linear search was easier for me to understand because it checks each item one at a time until it finds the target. Binary search was a little more difficult because I had to understand how the low, high, and middle positions changed during the search. Testing the code with small and large datasets helped me understand the difference between the two.

One challenge I had was understanding how binary search knows which half of the list to remove. After working through the code, it made more sense because the list is already sorted. If the target is higher or lower than the middle value, the program knows which half it can ignore.

I would use binary search for a large sorted list because it can find an item without checking every value. Linear search can still be useful when the list is small or not sorted. Binary search would not work correctly on an unsorted list unless the data was sorted first.
