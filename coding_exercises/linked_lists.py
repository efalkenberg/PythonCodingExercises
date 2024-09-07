#!/usr/bin/python
# -*- coding: utf-8 -*-

class LinkedListNode(object):

    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next = next_node

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        if new_value is None or not isinstance(new_value, int):
            raise TypeError("Input must be set and of type `int`")
        self._value = new_value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, LinkedListNode):
            raise TypeError("Input must be `None` or `LinkedListNode`")
        self._next = new_next

    def append(self, value):
        if value is None:
            self._next = None

        if isinstance(value, int):
            if self._next is None:
                self._next = LinkedListNode(value)
            else:
                new_next = LinkedListNode(value)
                new_next.next = self._next.next
                self._next = new_next
        elif isinstance(value, LinkedListNode):
            if self._next is None:
                self._next = value
            else:
                value.next = self._next
                self._next = value
        else:
            raise TypeError("Input must be set and of type `int` or `LinkedListNode`")

    def append_end(self, value):
        if value is None:
            raise TypeError("Input must be set")
        self.last_node().append(value)

    def length(self):
        length = 1
        end = self
        while end.next is not None:
            length += 1
            end = end.next
        return length

    def last_node(self):
        end = self
        while end.next is not None:
            end = end.next
        return end

    # def __repr__(self):
    #     if self._next is not None:
    #         return str(self._value) + "->" + str(self._next)
    #     else:
    #         return str(self._data) + "->[END OF LIST]"

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
        while end.next is not None:
            end = end.next
        end.insert(value)

    def __repr__(self):
        if self.next is not None:
            return str(self.data) + "<->" + str(self.next)
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
            if head.value in data.keys():
                previous.next = head.next
            else:
                data[head.value] = "x"
                previous = head
            head = head.next
        return input

    @staticmethod
    def kth_to_last(input, k):
        # we are using a recursive attempt here which returns either
        # an integer (to count the distance from the end on our way back)
        # or a LinkedList to bubble the result back up. We could (should) also have
        # used a tuple or a class here ...
        if input.next is None:
            # end of recursion
            if k == 0 :
                return input
            return 0
        else:
            prev = LinkedListsUtils.kth_to_last(input.next, k)
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
        if input.next is not None:
            head = LinkedListsUtils.reverse_list(input.next, input)
            input.next = prev
            return head
        else:
            input.next = prev
            return input

    @staticmethod
    def remove_single_node(node):
        while node.next.next is not None:
            node.value = node.next.value
            node = node.next
        
        node.value = node.next.value
        node.next = None
    
    @staticmethod
    def find_loop_in_linked_list(node):
        seen = set()
        while node.next is not None:
            if node in seen:
                return node
            seen.add(node)
            node = node.next
        return None
    
    @staticmethod 
    def linked_list_contains_loop(node, depth=1):
        if node is None:
            # end of list, no loop
            return False

        # a loop can not be longer than the entire list, so looking forward
        # as many steps as we are into the list is enough
        check_node = node.next
        for n in range(0, depth, 1):
            if check_node is None:
                # end of list, no loop
                return False
            else:
                if node is check_node:
                    # loop detected
                    return True 
            check_node = check_node.next
        
        # no loop detected, move on with the next element
        return LinkedListsUtils.linked_list_contains_loop(node.next, depth + 1)

    @staticmethod
    def test_linked_list_contains_loop_2_runner(node):
        runnerSlow = node
        runnerFast = node
        while runnerSlow is not None and runnerFast is not None and runnerFast.next is not None:
            runnerSlow = runnerSlow.next
            runnerFast = runnerFast.next.next
            if runnerSlow is runnerFast:
                return True
        return False

                