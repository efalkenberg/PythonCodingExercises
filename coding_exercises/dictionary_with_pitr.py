"""
Implement a dictionary that supports point-in-time lookups.

Expected API:

  get(key, timestamp=None)
  put(key, value)

The semantics should be chosen so that, if a timestamp is provided,
the dictionary behaves exactly like it would have at that point in time.

Don't worry about performance, but do write this as if it were
production code you'd be happy to check in.

Example:

put('AI', 'A')                # timestamp = 10
put('AI', 'B')                # timestamp = 12
put('AI', 'C')                # timestamp = 14

# timestamp = 15
get('AI')                   # Returns 'C'
get('AI', timestamp=13)     # Returns 'B'
get('AI', timestamp=10)     # Returns 'A'
get('AI', timestamp=5)      # Exception; key does not exist at t=5
"""

from collections import defaultdict
import unittest
import time


class DictionaryWithPoitLookups:
    """
    TODO: provide class description
    """

    _data = defaultdict(list)

    def __init__(self) -> None:
        pass

    def get(self, key: str, timestamp=None):

        if key not in self._data:
            raise Exception

        if timestamp is None:
            return self._data[key][0][0]

        for value_entry in self._data[key]:
            if value_entry[1] <= timestamp:
                return value_entry[0]

        raise Exception

    def put(self, key: str, value, timestamp=time.time()):
        self._data[key].insert(0, ((value, timestamp)))


class TestDictionaryWithLookups(unittest.TestCase):

    def test_dictionary(self):
        test_object = DictionaryWithPoitLookups()
        test_object.put('AI', 'A', 10)
        test_object.put('AI', 'B', 12)
        test_object.put('AI', 'C', 14)
        self.assertEqual(test_object.get('AI'), 'C')
        self.assertEqual(test_object.get('AI', 13), 'B')
        self.assertEqual(test_object.get('AI', 10), 'A')
        self.assertEqual(test_object.get('AI', 12), 'B')
        with self.assertRaises(Exception):
            test_object.get('AI', 5)
        with self.assertRaises(Exception):
            test_object.get('AF', 9)
        with self.assertRaises(Exception):
            test_object.get('AF')


if __name__ == '__main__':
    unittest.main()