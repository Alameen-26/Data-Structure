# Assignment 2: Priority Queue (COMP 2113, Fall 2026)

A priority queue built on a manually managed NumPy array, plus a test file for it.

## Files

| File | What it is |
|------|------------|
| `Adedeji0310392a_DataStructures2b.py` | Question 2: the `PriorityQueue` class |
| `Adedeji0310392a_DataStructures2a.py` | Question 1: tests for the priority queue |

## How the priority queue works

- Items are stored in a NumPy array (`dtype=object`) that starts with a capacity of 5.
- When the array is full, `_resize()` doubles the capacity and copies the active items into the new array.
- `add(item, priority)` inserts an item in priority order. A lower number means a higher priority, and items with equal priority keep the order they were added in.
- `remove(index)` removes the item at any position, and `remove_item(item)` removes the first match by value.
- `push(item)` and `pop()` let it behave like a stack; `peek()` returns the next item without removing it.
- `is_empty()`, `len()`, `items()` and `str()` report the current state.

## Running it

Requires Python 3 and NumPy:

```bash
pip install numpy pytest
```

The test file imports the class with `from priority_queue import PriorityQueue`, so save a copy of the class file as `priority_queue.py` in the same folder, then run:

```bash
pytest Adedeji0310392a_DataStructures2a.py
```

The tests cover the starting state, adding at the front, middle and end, equal priorities, removing by index and by value, stack push/pop, resizing at the sixth item and beyond, and error handling for empty queues, bad indexes and bad priorities.
