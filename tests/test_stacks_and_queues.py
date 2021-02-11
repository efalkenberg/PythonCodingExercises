#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import coding_exercises.linked_stacks_and_queues as sq

class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = sq.Stack()
        stack.push(100)
        stack.push(200)
        stack.push(300)
        stack.push(400)
        self.assertEqual(stack.length(), 4)
        self.assertEqual(stack.pop(), 400)
        self.assertEqual(stack.pop(), 300)
        self.assertEqual(stack.pop(), 200)
        self.assertEqual(stack.pop(), 100)
        self.assertEqual(stack.pop(), None)

    def test_triple_stack(self):
        stack = sq.MultiStack(3)
        stack.push(1, 100)
        stack.push(1, 200)
        stack.push(1, 300)
        stack.push(1, 400)

        stack.push(2, 7)
        stack.push(2, 8)
        stack.push(2, 9)

        stack.push(3, 1000)
        stack.push(3, 2000)
        stack.push(3, 3000)

        self.assertEqual(stack.pop(1), 400)
        self.assertEqual(stack.pop(1), 300)
        self.assertEqual(stack.pop(1), 200)
        self.assertEqual(stack.pop(1), 100)
        self.assertEqual(stack.pop(1), None)
        self.assertEqual(stack.pop(2), 9)
        self.assertEqual(stack.pop(2), 8)
        self.assertEqual(stack.pop(3), 3000)

    def test_min_stack(self):
        stack = sq.MinStack()
        stack.push(100)
        stack.push(200)
        stack.push(300)
        stack.push(400)
        self.assertEqual(stack.min, 100)
        stack.push(1)
        self.assertEqual(stack.min, 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.get_min(), 100)
        self.assertEqual(stack.pop(), 400)
        self.assertEqual(stack.get_min(), 100)

    def test_stack_of_plates(self):
        stack = sq.StackOfPlates(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        stack.pop()
        self.assertEqual(stack.pop(), 3)

if __name__ == '__main__':
    unittest.main()
