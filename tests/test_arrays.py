#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import coding_exercises.arrays as a 

class TestArrayUtils(unittest.TestCase):

    def test_rotate_matrix(self):
        input_3x3 = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

        expected_output_3x3 = [
            ['7', '4', '1'],
            ['8', '5', '2'],
            ['9', '6', '3']
        ]
        self.assertEqual(a.ArrayUtils.rotate_matrix(input_3x3), expected_output_3x3)

        input_4x4 = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ]

        expected_output_4x4 = [
            ['M', 'I', 'E', 'A'],
            ['N', 'J', 'F', 'B'],
            ['O', 'K', 'G', 'C'],
            ['P', 'L', 'H', 'D']
        ]
        self.assertEqual(a.ArrayUtils.rotate_matrix(input_4x4), expected_output_4x4)

if __name__ == '__main__':
    unittest.main()
