#!/usr/bin/python
# -*- coding: utf-8 -*-

class LinkedListNode(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def append_end(self, value):
        end = self.last_node()
        if type(value) is int: 
            end.set_next(LinkedListNode(value))
        else:
            end.set_next(value)

    def length(self):
        length = 1
        end = self
        while end.get_next() is not None:
            length += 1
            end = end.get_next()
        return length

    def last_node(self):
        end = self
        while end.get_next() is not None:
            end = end.get_next()
        return end

    def __repr__(self):
        if self.get_next() is not None:
            return str(self.data) + "->" + str(self.get_next())
        else:
            return str(self.data) + "->[END OF LIST]"

class DoubleLinkedListNode(LinkedListNode):

    def __init__(self, data=None):
        self.data = data
        self.previous_node = None
        self.next_node = None

    def set_next(self, new_next):
        self.next_node = new_next

    def insert(self, value):
        old_next = self.next_node
        if type(value) is int: 
            self.set_next(DoubleLinkedListNode(value))
        else:
            self.set_next(value)
        
        # set the `previous_node` pointer
        self.next_node.previous_node = self
        self.next_node.next_node = old_next
        if old_next is not None:
            self.next_node.next_node.previous_node = self.next_node
        
    def append_end(self, value):
        end = self
        while end.get_next() is not None:
            end = end.get_next()
        end.insert(value)

    def __repr__(self):
        if self.get_next() is not None:
            return str(self.data) + "<->" + str(self.get_next())
        else:
            return str(self.data) + "->[END OF LIST]"

class LinkedListsUtils:

    @staticmethod
    def linked_list_from_array(input):
        head = None
        end = None
        for element in input:
            if head is None:
                head = LinkedListNode(element)
                end = head
            else:
                end.setNext(LinkedListNode(element))
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
    
    @staticmethod
    def reverse_list(input, prev=None):
        if input.get_next() is not None:
            head = LinkedListsUtils.reverse_list(input.get_next(), input)
            input.set_next(prev)
            return head
        else:
            input.set_next(prev)
            return input

    @staticmethod
    def remove_single_node(node):
        while node.get_next().get_next() is not None:
            node.set_data(node.get_next().get_data())
            node = node.get_next()
        
        node.set_data(node.get_next().get_data())
        node.set_next(None)
    
    @staticmethod
    def find_loop_in_linked_list(node):
        seen = set()
        while node.get_next() is not None:
            if node in seen:
                return node
            seen.add(node)
            node = node.get_next()
        return None
    
    @staticmethod 
    def linked_list_contains_loop(node, depth=1):
        if node is None:
            # end of list, no loop
            return False

        # a loop can not be longer than the entire list, so looking forward
        # as many steps as we are into the list is enough
        check_node = node.get_next()
        for n in range(0, depth, 1):
            if check_node is None:
                # end of list, no loop
                return False
            else:
                if node is check_node:
                    # loop detected
                    return True 
            check_node = check_node.get_next()
        
        # no loop detected, move on with the next element
        return LinkedListsUtils.linked_list_contains_loop(node.get_next(), depth + 1)

    @staticmethod
    def test_linked_list_contains_loop_2_runner(node):
        runnerSlow = node
        runnerFast = node
        while runnerSlow is not None and runnerFast is not None and runnerFast.get_next() is not None:
            runnerSlow = runnerSlow.get_next()
            runnerFast = runnerFast.get_next().get_next()
            if runnerSlow is runnerFast:
                return True
        return False

                