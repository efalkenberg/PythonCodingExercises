#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import coding_exercises.trees_and_graphs as tg
import coding_exercises.linked_lists as ll

class TestTrees(unittest.TestCase):

    def test_random_tree_generation(self):
        root = tg.NodeUtil.create_full_balanced_tree(5)
        self.assertEqual(tg.NodeUtil.depth(root), 5) 

        bst_root = tg.NodeUtil.create_bst(10)
        # print(bst_root)
        bst_root.append(667)
        self.assertTrue(tg.NodeUtil.depth_first_search(bst_root, 667, True))

    def test_conversion_to_linked_list(self):
        NODE_COUNT = 100
        bst_root = tg.NodeUtil.create_bst(NODE_COUNT)
        # print(bst_root)
        linked_list = ll.LinkedListNode("[START]")
        linked_list = tg.NodeUtil.bst_to_linked_list(bst_root, linked_list)
        last_node = linked_list.last_node()
        # print(linked_list)
        # print("------------------------------------------")
        # print(last_node)
        # print("------------------------------------------")

        self.assertTrue(linked_list.length(), NODE_COUNT)
        self.assertTrue(last_node.length(), 1)

    def test_conversion_to_double_linked_list(self):
        NODE_COUNT = 100
        bst_root = tg.NodeUtil.create_bst(NODE_COUNT)
        # print(bst_root)
        linked_list = ll.DoubleLinkedListNode("[START]")
        linked_list = tg.NodeUtil.bst_to_linked_list(bst_root, linked_list)
        last_node = linked_list.last_node()
        # print(linked_list)
        # print("------------------------------------------")
        # print(last_node)
        # print("------------------------------------------")
        # print(last_node.previous_node.previous_node.previous_node.previous_node)
        # print("------------------------------------------")

        self.assertTrue(linked_list.length(), NODE_COUNT)
        self.assertTrue(last_node.length(), 1)
        self.assertTrue(last_node.previous_node.previous_node.previous_node.previous_node.length(), 5)



    


if __name__ == '__main__':
    unittest.main()
