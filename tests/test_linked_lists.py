#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import coding_exercises.linked_lists as ll


class TestLinkedLists(unittest.TestCase):

    def test_class_node(self):
        head = ll.LinkedListNode(5)
        self.assertEqual(head.value, 5)
        head.append(ll.LinkedListNode(42))
        self.assertEqual(head.next.value, 42)
        head.append(ll.LinkedListNode(43))
        self.assertEqual(head.next.value, 43)

        linked_list = ll.LinkedListNode(5)
        linked_list.append_end(17)
        linked_list.append_end(19)
        linked_list.append_end(25)
        self.assertEqual(linked_list.length(), 4)

    def test_remove_duplicate_from_linked_list(self):
        linked_list = ll.LinkedListNode(5)
        linked_list.append_end(17)
        linked_list.append_end(19)
        linked_list.append_end(25)
        linked_list.append_end(25)
        self.assertEqual(linked_list.length(), 5)
        linked_list = ll.LinkedListsUtils.remove_duplicate_from_linked_list(linked_list)
        self.assertEqual(linked_list.length(), 4)

    def test_remove_duplicate_from_linked_list_2(self):
        linked_list = ll.LinkedListNode(5)
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
        linked_list = ll.LinkedListNode(8)
        linked_list.append_end(7)
        linked_list.append_end(6)
        linked_list.append_end(5)
        linked_list.append_end(4)
        linked_list.append_end(3)
        linked_list.append_end(2)
        linked_list.append_end(1)
        self.assertEqual(ll.LinkedListsUtils.kth_to_last(linked_list, 0).value, 1)
        self.assertEqual(ll.LinkedListsUtils.kth_to_last(linked_list, 1).value, 2)
        self.assertEqual(ll.LinkedListsUtils.kth_to_last(linked_list, 7).value, 8)

    def test_reverse_list(self):
        linked_list = ll.LinkedListNode(8)
        linked_list.append_end(7)
        linked_list.append_end(6)
        linked_list.append_end(5)
        linked_list.append_end(4)
        linked_list.append_end(3)
        linked_list.append_end(2)
        linked_list.append_end(1)
        self.assertEqual(ll.LinkedListsUtils.reverse_list(linked_list).value, 1)
        self.assertEqual(ll.LinkedListsUtils.reverse_list(linked_list).length(), linked_list.length())

    def test_remove_single_node(self):
        linked_list = ll.LinkedListNode(8)
        node2 = ll.LinkedListNode(5)
        linked_list.next = node2
        linked_list.append_end(7)
        linked_list.append_end(6)
        linked_list.append_end(5)
        linked_list.append_end(4)
        linked_list.append_end(3)
        linked_list.append_end(2)
        linked_list.append_end(1)

        self.assertEqual(linked_list.length(), 9)
        self.assertEqual(linked_list.next.value, 5)
        ll.LinkedListsUtils.remove_single_node(node2)
        self.assertEqual(linked_list.length(), 8)
        self.assertEqual(linked_list.next.value, 7)

    def test_find_loop_in_linked_list(self):
        linked_list = ll.LinkedListNode(8)
        linked_list.append_end(5)
        linked_list.append_end(7)
        linked_list.append_end(8)
        self.assertEqual(ll.LinkedListsUtils.find_loop_in_linked_list(linked_list), None)
        loop = ll.LinkedListNode(1000)
        loop.next = linked_list
        linked_list.append_end(loop)
        self.assertEqual(ll.LinkedListsUtils.find_loop_in_linked_list(linked_list).value, 8)

    def test_linked_list_contains_loop(self):
        linked_list = ll.LinkedListNode(8)
        loop = ll.LinkedListNode(5)
        linked_list.append_end(loop)
        linked_list.append_end(7)
        linked_list.append_end(8)
        linked_list.append_end(9)
        # no loop
        self.assertFalse(ll.LinkedListsUtils.linked_list_contains_loop(linked_list))
        linked_list.append_end(loop)
        # loop
        self.assertTrue(ll.LinkedListsUtils.linked_list_contains_loop(linked_list))

    def test_linked_list_contains_loop_2_runner(self):
        linked_list = ll.LinkedListNode(8)
        loop = ll.LinkedListNode(5)
        linked_list.append_end(loop)
        linked_list.append_end(7)
        linked_list.append_end(8)
        linked_list.append_end(9)
        # no loop
        self.assertFalse(ll.LinkedListsUtils.test_linked_list_contains_loop_2_runner(linked_list))
        linked_list.append_end(loop)
        # loop
        self.assertTrue(ll.LinkedListsUtils.test_linked_list_contains_loop_2_runner(linked_list))


if __name__ == '__main__':
    unittest.main()
