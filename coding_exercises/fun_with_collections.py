"""
Cheat sheet for Python collections
"""

from collections import defaultdict
from collections import deque
import unittest


class TestLeetCode(unittest.TestCase):

    def test_defaultdict(self):

        # typical use case for defaultdict is to return a list
        # to skip the check whether the key exists
        default_to_list = defaultdict(list)
        pizza_my_heart = list(['pizza', 'my', 'heart'])
        for word in pizza_my_heart:
            default_to_list['foo'].append(word)
        self.assertEqual(default_to_list['foo'], pizza_my_heart)

        # defaultdict is also great for counters
        default_to_int = defaultdict(int)
        for i in range(10):
            default_to_int['foo'] += 1
        self.assertEqual(default_to_int['foo'], 10)
        for word in "what shall we do with the drunken sailor?".split():
            default_to_int[word] += 1
        self.assertEqual(default_to_int['shall'], 1)
        self.assertEqual(default_to_int['morning'], 0)

        # any callable can be used for the defaultdict's
        # so called `default factory`
        def eike():
            return "eike"

        default_to_eike = defaultdict(eike)
        self.assertEqual(default_to_eike['foo'], 'eike')

    def test_dequeue(self):
        dequeue = deque('what shall we do with the drunken sailor?'.split())
        self.assertEqual(dequeue.pop(), 'sailor?')
        self.assertEqual(dequeue.popleft(), 'what')
        self.assertEqual(list(dequeue),
                         list('shall we do with the drunken'.split()))
        dequeue.appendleft('what')
        dequeue.append('sailor?')
        self.assertEqual(list(dequeue),
                         list('what shall we do with the drunken sailor?'.split()))


