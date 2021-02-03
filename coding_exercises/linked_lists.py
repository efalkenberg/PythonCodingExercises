#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def append_end(self, value):
        end = self
        while end.get_next() is not None:
            end = end.get_next()
        end.set_next(Node(value))
    
    def length(self):
        length = 1
        end = self
        while end.get_next() is not None:
            length += 1
            end = end.get_next()
        return length

    def __repr__(self):
        if self.get_next() is not None:
            return str(self.data) + "->" + str(self.get_next())
        else:
            return str(self.data) + "->[END OF LIST]"


class LinkedListsUtils:

    @staticmethod
    def linked_list_from_array(input):
        head = None
        end = None
        for element in input:
            if head is None:
                head = Node(element)
                end = head
            else:
                end.setNext(Node(element))
                end = end.next_element()
        return head

    @staticmethod
    def remove_duplicate_from_linked_list(input):
        if input.length() < 2:
            return input
        head = input
        data = {}
        previous = None
        while head is not None:
            if head.get_data() in data.keys():
                previous.set_next(head.get_next())
            else:
                data[head.get_data()] = "x"
                previous = head
            head = head.get_next()
        return input

    @staticmethod
    def kth_to_last(input, k):
        # we are using a recursive attempt here which returns either
        # an integer (to count the distance from the end on our way back)
        # or a LinkedList to bubble the result back up. We could (should) also have
        # used a tuple or a class here ...
        if input.get_next() is None:
            # end of recursion
            if k == 0 :
                return input
            return 0
        else:
            prev = LinkedListsUtils.kth_to_last(input.get_next(), k)
            if type(prev) is int:
                # we are coming up from the recursion but haven't found it yet
                # increment the index and check if this is the one
                prev += 1
                if prev == k:
                    return input
                return prev
            else:
                # we  already found the index, just pass forward the result
                return prev
                