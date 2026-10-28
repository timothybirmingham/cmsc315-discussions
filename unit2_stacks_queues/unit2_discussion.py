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

        self.items.append(value)

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
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        self.items.append(value)

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
        return self.items[0]

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

    print("\n=== STACK DEMO ===")
    # print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    # print("      test popping from an empty stack,")
    # print("      test peeking at an empty stack,")
    # print("      and verify a single-item stack becomes empty after removal.")

    stack = Stack()

    stack.push("Password reset")
    stack.push("Printer setup")
    stack.push("Software update")
    stack.push("Account unlocked")

    print("Top", stack.peek())

    while not stack.is_empty():
        print(stack.pop())

    print("Empty pip:", stack.pop())
    print("Empty peek:", stack.peek())

    single_stack = Stack()
    single_stack.push("Restart Computer")
    single_stack.pop()
    print(single_stack.is_empty())

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

    print("\n=== QUEUE DEMO ===")
    # print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    # print("      test dequeuing from an empty queue,")
    # print("      test viewing the front of an empty queue,")
    # print("      and verify a single-item queue becomes empty after removal.")

    queue = Queue()

    queue.enqueue("Password reset")
    queue.enqueue("Printer setup")
    queue.enqueue("Software update")
    queue.enqueue("Account unlocked")

    print("Front", queue.front())

    while not queue.is_empty():
        print(queue.dequeue())

    print("Empty dequeue:", queue.dequeue())
    print("Empty front:", queue.front())

    single_queue = Queue()
    single_queue.enqueue("Restart computer")
    single_queue.dequeue()
    print(single_queue.is_empty())


if __name__ == "__main__":
    main()