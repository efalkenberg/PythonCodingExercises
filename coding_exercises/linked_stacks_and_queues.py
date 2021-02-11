#!/usr/bin/python
# -*- coding: utf-8 -*-


class Stack(object):

    def __init__(self, data=None, next_node=None):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) > 0:
            return_value = self.data[len(self.data)-1]
            self.data.pop(len(self.data)-1)
            return return_value
        return None
    
    def length(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)


class MultiStack(object):

    def __init__(self, stacks=3, data=None):
        self.data = [None] * (stacks * 5)
        self.indices = []
        for i in range(0, stacks, 1):
            self.indices.append(int(len(self.data)/stacks)*i)        

    def push(self, stack, data):
        # this implementation completely lacks boundary
        # checks and growth
        self.data[self.indices[stack-1]] = data
        self.indices[stack-1] += 1

    def pop(self, stack):
        self.indices[stack-1] -= 1
        data = self.data[self.indices[stack-1]]
        self.data[self.indices[stack-1]] = None
        return data
    
    def length(self, stack):
        # laaaaaazy 🦥
        return int(len(self.data)/3)

    def __repr__(self):
        return str(self.data)


class MinStack(object):
        
    def __init__(self):
        self.data = []
        self.min = None

    def push(self, value):
        self.data.append((value, self.min))
        if self.min is None or self.min > value:
            self.min = value
    
    def pop(self):
        value = self.data.pop(len(self.data)-1)
        # restore stack if needed
        if value[0] == self.min:
            self.min = value[1]
        return value[0]
    
    def get_min(self):
        return self.min

    def __repr__(self):
        return str(self.data) + " min:" + str(self.min)


class StackOfPlates(object):
    
    def __init__(self, stack_max_height):
        self.stack_max_height = stack_max_height
        self.data = [[]]
    
    def push(self, value):
        idx = len(self.data)-1
        if len(self.data[idx]) >= self.stack_max_height:
            self.data.append([value])
        else:
            self.data[idx].append(value)
    
    def pop(self):
        idx = len(self.data)-1
        if len(self.data[idx]) < 1:
            self.data.pop(idx)
            idx -= 1
        idx2 = len(self.data[idx])-1
        value = self.data[idx].pop(idx2)
        return value

    def __repr__(self):
        return str(self.data) 



                