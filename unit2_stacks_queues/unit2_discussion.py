"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)  # Adds the newest value to the top of the stack for LIFO

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return None
        return self.items[-1]  # Returns the newest item without removing it

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data sIs this tructure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)  # Adds the newest value to the back of the queue for FIFO

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None
        return self.items[0]  # Returns the oldest item without removing it

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0
    


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

print("\n=== STACK DEMO: GAME ACTION HISTORY ===")

game_actions = Stack()

game_actions.push("Move Forward")
game_actions.push("Pick Up Sword")
game_actions.push("Attack Enemy")
game_actions.push("Use Potion")

print("Top action:", game_actions.peek())

print("Undo:", game_actions.pop())
print("Undo:", game_actions.pop())
print("Undo:", game_actions.pop())
print("Undo:", game_actions.pop())

print("Pop from empty stack:", game_actions.pop())
print("Peek at empty stack:", game_actions.peek())


#Edge Cases
single_stack = Stack()
single_stack.push("Save Game")

print("Single item removed:", single_stack.pop())
print("Is stack empty after removal?", single_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO: GAME MATCHMAKING ===")

game_queue = Queue()
game_queue.enqueue("Player 1")
game_queue.enqueue("Player 2")
game_queue.enqueue("Player 3")
game_queue.enqueue("Player 4")
print("Next player:", game_queue.front())

print("Player entering game:", game_queue.dequeue())
print("Player entering game:", game_queue.dequeue())
print("Player entering game:", game_queue.dequeue())
print("Player entering game:", game_queue.dequeue())
print("Dequeue from empty queue:", game_queue.dequeue())
print("Front of empty queue:", game_queue.front())



# Edge Case
single_queue = Queue()
single_queue.enqueue("Player 5")

print("Single player removed:", single_queue.dequeue())
print("Is queue empty after removal?", single_queue.is_empty())

if __name__ == "__main__":
    main()
