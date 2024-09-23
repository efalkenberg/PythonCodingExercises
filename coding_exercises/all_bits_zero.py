#!/usr/bin/python
# -*- coding: utf-8 -*-

# Tak a grid of 0s and 1s and check whether it can
# be transformed to all 1s
# Your only allowed operation is to flip an entire row
# or column of bits which will "XOR 1" the entire row
#
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 1 1 1 1 0 1
# 0 0 0 0 0 0
# (true, flip row[3], flip column[3])
#
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 1
# 0 0 0 0 0 0
# (false)
#
# Write a function that can take such a grid as numpy
# array and return a boolean indicating whether the
# grid can be transformed to all zeros.
#

import numpy as np
import unittest


def grid_checker(grid):
    if not isinstance(grid, np.ndarray):
        raise TypeError(f"grid_checker can only check numpy arrays but is of type {type(grid)}")

    # single dimension always works
    if grid.ndim < 2:
        return True

    # if the sum is 0 or the same as the amount of values, it's all
    # 0s or all 1s, which makes it a grid that can be transformed
    if np.sum(grid) == 0 or grid.size == np.sum(grid):
        return True

    # the logic below looks for cases that can not be resolved and
    # will return false whenever such a case is found.
    width = grid.shape[0]
    height = grid.shape[1]

    # TODO: there are a lot of caching opportunities here
    for idx, value in np.ndenumerate(grid):
        if value == 0:
            continue

        # (1) if a row has a all 0s or all 1s, it can be flipped
        # sample:
        # 1 1 1
        # 0 0 0
        # 0 0 0
        row_sum = np.sum(grid[idx[0]])
        if row_sum == 0:
            continue
        if row_sum == width:
            grid[idx[0]] = 0

        # (2.1) we determined that the value is 1 in a mixed row
        # when all values in this colum are also 1, this one is safe
        # to flip
        # sample:
        # 1 0 0
        # 1 0 0
        # 1 0 0
        if np.sum(grid, axis=0)[idx[1]] == height:
            continue
        # TODO: do we actually have to update the grid here?

        # (2.2 the colum is also mixed, find the column values that are 0
        # to see if the rest of their row is all 1s because that would allow
        # us to flip the column and then their row afterwards
        # sample:
        # 1 0 0
        # 0 1 1
        # 1 0 0

        # sample 2
        # 0 0 1 0 0
        # 0 0 1 0 0
        # 1 1 0 1 1
        # 0 0 1 0 0
        # 0 0 1 0 0
        # This could be solved by first flipping column 2 and then row 2 afterwards
        for j in range(height):
            # skip the current row and the cells that are 1
            if j == idx[1] or grid[j, idx[1]] == 1:
                continue

            # j is now pointing at a row with a 0, this can only be flipped
            # if all other values are 1s
            if np.sum(grid[j]) != (width-1):
                return False

    return True


class TestGridChecker(unittest.TestCase):
    def test_single_dimension(self):
        self.assertTrue(grid_checker(np.array([])))
        self.assertTrue(grid_checker(np.array([1])))

    def test_all_same(self):
        self.assertTrue(grid_checker(np.array([[0, 0], [0, 0]])))
        self.assertTrue(grid_checker(np.array([[1, 1], [1, 1]])))
        self.assertTrue(grid_checker(np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])))

    def test_all_2d_flippable(self):
        self.assertTrue(grid_checker(np.array([[1, 1], [0, 0]])))
        self.assertTrue(grid_checker(np.array([[0, 1], [0, 1]])))
        self.assertFalse(grid_checker(np.array([[0, 1], [1, 1]])))
