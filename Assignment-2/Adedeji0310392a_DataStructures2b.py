######################### 
# Course: COMP 2113 FA01, 2026 
# Assignment 2, Question 2 
# Author: <your name here> 
# Student ID: 0310392a 
# email address: <your email address here> 
# Date: <the date you wrote / submitted the code, in 2026-10-01 format> 
# I certify that this code is my own. 
# I have not broken any rules concerning Academic Dishonesty. 
#########################
import numpy as np


class PriorityQueue:
    """A priority queue using a manually managed NumPy array."""

    INITIAL_CAPACITY = 5

    def __init__(self):
        self.data = np.empty(self.INITIAL_CAPACITY, dtype=object)
        self.size = 0
        self.capacity = self.INITIAL_CAPACITY

    def _resize(self):
        """Double the backing array and copy the active elements."""
        old_capacity = self.capacity
        self.capacity *= 2
        new_data = np.empty(self.capacity, dtype=object)

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        print(
            f"Backing array full: increasing capacity "
            f"from {old_capacity} to {self.capacity}."
        )

    def add(self, item, priority):
        """Add item according to priority; lower number = higher priority."""
        if not isinstance(priority, (int, float, np.integer, np.floating)):
            raise TypeError("Priority must be numeric.")

        if self.size == self.capacity:
            self._resize()

        # Find the insertion point. Equal priorities remain in arrival order.
        position = self.size
        while position > 0 and self.data[position - 1][0] > priority:
            self.data[position] = self.data[position - 1]
            position -= 1

        self.data[position] = (priority, item)
        self.size += 1

    def remove(self, index):
        """Remove and return the item at any active queue index."""
        if not isinstance(index, (int, np.integer)):
            raise TypeError("Queue position must be an integer.")
        if index < 0 or index >= self.size:
            raise IndexError("Queue position is out of range.")

        removed = self.data[index]
        
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1
        return removed

    def remove_item(self, item):
        """Remove the first occurrence of an item by value."""
        for i in range(self.size):
            if self.data[i][1] == item:
                return self.remove(i)
        raise ValueError("Item was not found in the queue.")

    def push(self, item):
        """Push an item so it behaves like the top of a stack."""
        # Give the new item a priority higher than every existing item.
        if self.size == 0:
            priority = 0
        else:
            priority = self.data[0][0] - 1
        self.add(item, priority)

    def pop(self):
        """Pop and return the most recently pushed item."""
        if self.size == 0:
            raise IndexError("Cannot pop from an empty queue.")
        return self.remove(0)[1]

    def peek(self):
        """Return the next item without removing it."""
        if self.size == 0:
            raise IndexError("Cannot peek at an empty queue.")
        return self.data[0][1]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def items(self):
        """Return active entries for testing/display."""
        return [self.data[i] for i in range(self.size)]

    def __str__(self):
        return str(self.items())
   
    def main():
        """Simple command-line demonstration."""
        queue = PriorityQueue()
        print("Priority Queue demonstration")
        print("Commands:")
        print("  add <priority> <item>")
        print("  remove <index>")
        print("  remove_item <item>")
        print("  push <item>")
        print("  pop")
        print("  peek")
        print("  show")
        print("  quit")

        while True:
            try:
                parts = input("> ").strip().split(maxsplit=2)
                if not parts:
                    continue

                command = parts[0].lower()

                if command == "add":
                    if len(parts) != 3:
                        print("Usage: add <priority> <item>")
                        continue
                    priority = float(parts[1])
                    if priority.is_integer():
                        priority = int(priority)
                    queue.add(parts[2], priority)
                    print(queue)

                elif command == "remove":
                    if len(parts) != 2:
                        print("Usage: remove <index>")
                        continue
                    print("Removed:", queue.remove(int(parts[1])))
                    print(queue)

                elif command == "remove_item":
                    if len(parts) != 2:
                        print("Usage: remove_item <item>")
                        continue
                    print("Removed:", queue.remove_item(parts[1]))
                    print(queue)

                elif command == "push":
                    if len(parts) != 2:
                        print("Usage: push <item>")
                        continue
                    queue.push(parts[1])
                    print(queue)
                   
                    elif command == "pop":
                        print("Popped:", queue.pop())
                        print(queue)

                    elif command == "peek":
                        print("Next:", queue.peek())

                    elif command == "show":
                        print(queue)

                    elif command == "quit":
                        break
                    else:
                        print("Unknown command.")

                except (TypeError, ValueError, IndexError) as error:
                    print("Error:", error)


        if __name__ == "__main__":
            main()