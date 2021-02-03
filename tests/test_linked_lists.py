#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import coding_exercises.linked_lists as ll

class TestLinkedLists(unittest.TestCase):

    def test_class_node(self):
        head = ll.Node(5)
        self.assertEqual(head.get_data(), 5)
        head.set_next(ll.Node(42))
        self.assertEqual(head.get_next().get_data(), 42)

        linked_list = ll.Node(5)
        linked_list.append_end(17)
        linked_list.append_end(19)
        linked_list.append_end(25)
        self.assertEqual(linked_list.length(), 4)
    
    def test_remove_duplicate_from_linked_list(self):
        linked_list = ll.Node(5)
        linked_list.append_end(17)
        linked_list.append_end(19)
        linked_list.append_end(25)
        linked_list.append_end(25)
        self.assertEqual(linked_list.length(), 5)
        linked_list = ll.LinkedListsUtils.remove_duplicate_from_linked_list(linked_list)
        self.assertEqual(linked_list.length(), 4)
        
    def test_remove_duplicate_from_linked_list_2(self):
        linked_list = ll.Node(5)
        linked_list.append_end(5)
        linked_list.append_end(3)
        linked_list.append_end(7)
        linked_list.append_end(7)
        linked_list.append_end(7)
        linked_list.append_end(4)
        linked_list.append_end(4)
        self.assertEqual(linked_list.length(), 8)
        linked_list = ll.LinkedListsUtils.remove_duplicate_from_linked_list(linked_list)
        self.assertEqual(linked_list.length(), 4)

    def test_kth_to_last(self):
        linked_list = ll.Node(8)
        linked_list.append_end(7)
        linked_list.append_end(6)
        linked_list.append_end(5)
        linked_list.append_end(4)
        linked_list.append_end(3)
        linked_list.append_end(2)
        linked_list.append_end(1)
        self.assertEqual(ll.LinkedListsUtils.kth_to_last(linked_list, 0).get_data(), 1)
        self.assertEqual(ll.LinkedListsUtils.kth_to_last(linked_list, 1).get_data(), 2)
        self.assertEqual(ll.LinkedListsUtils.kth_to_last(linked_list, 7).get_data(), 8)
    
if __name__ == '__main__':
    unittest.main()
