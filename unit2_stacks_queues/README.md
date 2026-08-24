# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## My Implementation

I implemented a stack via python list and a queue using  deque. I used a video game scenario to demonstrate implementing stack. The stack represented a game action history queue where the most recent action was removed first using LIFO behavior. The queue represented players waiting to enter a game and where the first player added was removed first using FIFO behavior.

I also tested edge cases for both structures. I tested popping and peeking from an empty stack and verified that a single item stack became empty after removal. I tested dequeuing and checking the front of an empty queue and verified that a single item queue became empty after removal.

## Reflection

While completing this assignment I learned more about how stacks and queues organize and remove data differently. I learned that a stack follows LIFO or "last in first out'". I demonstrated this using a video game action history. For example "use potion" was the last action added to the stack so it was the first action removed when undoing actions. A queue follows FIFO I demonstrated this with players waiting to enter a game. Player 1 entered the queue first so player 1 was also the first player removed from the queue.

One challenge I encountered was correctly setting up the queue. My program originally produced an error because the queues internal items structure was not initialized correctly, I fixed this by initializing it with deque.

This assignment helped me understand why choosing the correct data structure matters and why stacks are useful when the newest item needs to be processed first while queues are useful when items should be processed in the order they arrive.