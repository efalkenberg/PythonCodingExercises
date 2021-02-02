#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import coding_exercises.strings as str

class TestStringUtils(unittest.TestCase):

    def test_all_unique_chars(self):
        self.assertTrue(str.StringUtils.all_unique_chars(""))
        self.assertTrue(str.StringUtils.all_unique_chars(" "))
        self.assertTrue(str.StringUtils.all_unique_chars("a"))
        self.assertTrue(str.StringUtils.all_unique_chars("ab"))
        self.assertTrue(str.StringUtils.all_unique_chars("abc"))
        self.assertTrue(str.StringUtils.all_unique_chars("àáâ"))
        self.assertTrue(str.StringUtils.all_unique_chars("💥"))
        self.assertTrue(str.StringUtils.all_unique_chars("🏊️a"))

        self.assertFalse(str.StringUtils.all_unique_chars("  "))
        self.assertFalse(str.StringUtils.all_unique_chars("aa"))
        self.assertFalse(str.StringUtils.all_unique_chars("aab"))
        self.assertFalse(str.StringUtils.all_unique_chars("baa"))
        self.assertFalse(str.StringUtils.all_unique_chars("abba"))
        self.assertFalse(str.StringUtils.all_unique_chars("🎲🎲"))
        self.assertFalse(str.StringUtils.all_unique_chars("🎲a🎲"))
        self.assertFalse(str.StringUtils.all_unique_chars("abcdefg🎲a🎲"))
    
    def test_urlify(self):
        self.assertEqual(str.StringUtils.urlify(""), "")
        self.assertEqual(str.StringUtils.urlify("http://"), "http://")
        self.assertEqual(str.StringUtils.urlify("http://www.google.com"), "http://www.google.com")
        self.assertEqual(str.StringUtils.urlify("http://www.google.com/a b"), "http://www.google.com/a%20b")
        self.assertEqual(str.StringUtils.urlify("http://www.google.com/a b c"), "http://www.google.com/a%20b%20c")
        self.assertEqual(str.StringUtils.urlify("http://www.google.com/a b c "), "http://www.google.com/a%20b%20c%20")
        self.assertEqual(str.StringUtils.urlify("http://www.google.com/a b c  "), "http://www.google.com/a%20b%20c%20%20")

    def test_is_permutation_of_palindrome(self):
        self.assertTrue(str.StringUtils.is_permutation_of_palindrome("radar"))
        self.assertTrue(str.StringUtils.is_permutation_of_palindrome("raadd"))
        self.assertTrue(str.StringUtils.is_permutation_of_palindrome(""))
        self.assertTrue(str.StringUtils.is_permutation_of_palindrome("a"))
        self.assertFalse(str.StringUtils.is_permutation_of_palindrome("Wood"))
        self.assertFalse(str.StringUtils.is_permutation_of_palindrome("House"))

    

if __name__ == '__main__':
    unittest.main()
