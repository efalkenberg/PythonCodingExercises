#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class TestLeetCode(unittest.TestCase):

    def test_the_slice(self):
        s = "today is a good day"
        self.assertEqual(s[0:5], 'today')
        self.assertEqual(s[2:4], 'da')
        self.assertEqual(s[:-4], 'today is a good')  # start at 0 without the last 4
        self.assertEqual(s[11:-4], 'good')
        self.assertEqual(s[-3:], 'day')
        self.assertEqual(s[6::], 'is a good day')
        self.assertEqual(s[6:], 'is a good day') # TODO: what's the difference?
        self.assertEqual(s[::-1], 'yad doog a si yadot')  # revere string
        self.assertEqual(s[::-2], 'yddo  iydt')  # one of the most Python things I've ever seen

