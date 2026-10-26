######################### 
# Course: COMP 2113 FA01, 2026 
# Assignment 2, Question 1 
# Author: <your name here> 
# Student ID: <your student ID here> 
# email address: <your email address here> 
# Date: <the date you wrote / submitted the code, in 2026-09-23 format> 
# I certify that this code is my own. 
# I have not broken any rules concerning Academic Dishonesty. 
#########################

import numpy as np
from priority_queue import PriorityQueue


def test_initial_state():
    q = PriorityQueue()
    assert q.is_empty()
    assert len(q) == 0
    assert q.capacity == 5
    assert isinstance(q.data, np.ndarray)


def test_add_anywhere_by_priority():
    q = PriorityQueue()
    q.add("A", 10)
    q.add("C", 30)
    q.add("B", 20)
    assert q.items() == [(10, "A"), (20, "B"), (30, "C")]


def test_add_front_and_end():
    q = PriorityQueue()
    q.add("B", 20)
    q.add("A", 10)
    q.add("C", 30)
    assert q.items() == [(10, "A"), (20, "B"), (30, "C")]


def test_equal_priorities():
    q = PriorityQueue()
    q.add("first", 5)
    q.add("second", 5)
    q.add("third", 5)
    assert q.items() == [(5, "first"), (5, "second"), (5, "third")]


def test_remove_front_middle_end():
    q = PriorityQueue()
    for name, priority in [("A", 1), ("B", 2), ("C", 3), ("D", 4)]:
        q.add(name, priority)
        
    assert q.remove(0) == (1, "A")
    assert q.remove(1) == (3, "C")
    assert q.remove(1) == (4, "D")
    assert q.items() == [(2, "B")]


def test_remove_by_item():
    q = PriorityQueue()
    q.add("A", 1)
    q.add("B", 2)
    assert q.remove_item("B") == (2, "B")
    assert q.items() == [(1, "A")]


def test_push_pop_stack():
    q = PriorityQueue()
    q.push("one")
    q.push("two")
    q.push("three")
    assert q.pop() == "three"
    assert q.pop() == "two"
    assert q.pop() == "one"
    assert q.is_empty()


def test_resize_at_sixth_item():
    q = PriorityQueue()
    for i in range(6):
        q.add(f"item{i}", i)
    assert q.capacity == 10
    assert len(q) == 6
    assert q.peek() == "item0"


def test_multiple_resizes():
    q = PriorityQueue()
    for i in range(21):
        q.add(i, i)
    assert q.capacity == 40
    assert len(q) == 21
    
def test_empty_pop_and_peek():
    q = PriorityQueue()
    try:
        q.pop()
        assert False, 
    except IndexError:
        pass

    try:
        q.peek()
        assert False, 
    except IndexError:
        pass


def test_bad_index():
    q = PriorityQueue()
    q.add("A", 1)
    for bad in [-1, 1]:
        try:
            q.remove(bad)
            assert False, 
        except IndexError:
            pass


def test_bad_index_type():
    q = PriorityQueue()
    q.add("A", 1)
    try:
        q.remove("zero")
        assert False, 
    except TypeError:
        pass


def test_missing_item():
    q = PriorityQueue()
    q.add("A", 1)
    try:
        q.remove_item("missing")
        assert False, 
    except ValueError:
        pass

def test_bad_priority():
    q = PriorityQueue()
    try:
        q.add("A", "high")
        assert False, 
    except TypeError:
        pass


def run_tests():
    tests = [
        test_initial_state,
        test_add_anywhere_by_priority,
        test_add_front_and_end,
        test_equal_priorities,
        test_remove_front_middle_end,
        test_remove_by_item,
        test_push_pop_stack,
        test_resize_at_sixth_item,
        test_multiple_resizes,
        test_empty_pop_and_peek,
        test_bad_index,
        test_bad_index_type,
        test_missing_item,
        test_bad_priority,
    ]

    for test in tests:
        test()
        print(f"PASS: {test.__name__}")

    print(f"\n{len(tests)}/{len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests()