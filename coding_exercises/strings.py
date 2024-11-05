#!/usr/bin/python
# -*- coding: utf-8 -*-

class StringUtils:

    @staticmethod
    def all_unique_chars(input):
        if len(input) < 2:
            return True

        i = 0
        for char in input:
            for j in range(i+1, len(input)):
                if input[i] == input[j]:
                    return False
            i += 1
        return True

    @staticmethod
    def urlify(input):
        '''
        even though python has a lot of fancy string operations,
        we will do it c-style here and only use basic operations
        where possible
        '''
        chars = list(input)
        blanks = 0
        for char in chars:
            if char == ' ':
                blanks += 1

        '''
        add extra space so that there is enough room to replace
        ' ' with '%20' 
        '''
        original_length = len(chars)
        chars.extend(list(' ' * 2 * blanks))
        '''
        Walk backwards through the input list and 
        append it to the end, while adding %20 where
        needed
        '''
        insertIdx = len(chars) - 1
        for i in range(original_length-1, 0, -1):
            if chars[i] == ' ':
                chars[insertIdx] = '0'
                chars[insertIdx-1] = '2'
                chars[insertIdx-2] = '%'
                insertIdx -= 3
            else:
                chars[insertIdx] = chars[i]
                insertIdx -= 1

        return "".join(chars)
    
    @staticmethod
    def is_permutation_of_palindrome(input):
        if len(input) < 2:
            return True

        char_counter = {}
        for char in input:
            if char in char_counter:
                char_counter[char] += 1
            else:
                char_counter[char] = 1

        max_singles_left = 0
        if len(input) % 2 != 0:
            max_singles_left = 1
        
        for char, count in char_counter.items():
            if count == 1:
                if max_singles_left == 0:
                    return False
                max_singles_left = 0
            else:
                if count % 2 != 0:
                    return False
        return True


        
        


        
