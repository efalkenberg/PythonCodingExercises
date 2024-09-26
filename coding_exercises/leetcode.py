import unittest


def isPalindrome(x: int) -> bool:
    x_str = str(x)
    i1 = 0
    i2 = len(x_str) -1

    while i2 >= 0:
        if x_str[i1] != x_str[i2]:
            return False
        i1 = i1 +1
        i2 = i2 -1
        return True


def is_palindrome_recursive(s: str) -> bool:
    if len(s) < 2:
        return True

    if s[0] != s[-1:]:
        return False

    return is_palindrome_recursive(s[1:-1])


def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def search(s: str, left: int, right: int) -> str:
        if len(s) < 2:
            return ''
        if len(s) == 2:
            return s if s[0] == s[1] else ''

        while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
            left -= 1
            right += 1

        palindrome = s[left:right+1] if right-left > 1 else ''
        return palindrome

    longest_palindrome = ''

    for idx, value in enumerate(s):
        odd = search(s, idx, idx)
        even = search(s, idx, idx + 1)
        longest_palindrome = max((longest_palindrome, even, odd), key=len)

    return longest_palindrome


def romanToInt(s: str) -> int:
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000

    int_value = 0
    carryover = 0
    for idx, value in enumerate(s):
        if value == 'M':
            int_value += 1000 + carryover
            carryover = 0
        elif value == 'D':
            int_value += 500 + carryover
            carryover = 0
        elif value == 'C':
            # C can be placed before D (500) and M (1000) to make 400 and 900.
            if idx < len(s) - 1 and s[idx+1] in ('D', 'M'):
                carryover = -100
                continue
            int_value += 100 + carryover
            carryover = 0
        elif value == 'L':
            int_value += 50 + carryover
            carryover = 0
        elif value == 'X':
            # X can be placed before L (50) and C (100) to make 40 and 90.
            if idx < len(s) - 1 and s[idx+1] in ('L', 'C'):
                carryover = -10
                continue
            int_value += 10 + carryover
            carryover = 0
        elif value == 'V':
            int_value += 5 + carryover
            carryover = 0
        elif value == 'I':
            # I can be placed before V (5) and X (10) to make 4 and 9.
            if idx < len(s) - 1 and s[idx+1] in ('V', 'X'):
                carryover = -1
                continue
            int_value += 1
    return int_value


def bracket_checker(s: str) -> bool:
    # implemented like a classic stack based parser that pushes
    # and consumes tokens from a stack for syntax checking
    buffer = []
    for bracket in s: # for simplicity we assume this is safe
        if bracket in ['(', '[', '{']:
            buffer.append(bracket)
        elif bracket == ')':
            if len(buffer) < 1 or buffer[-1] != '(':
                return False
            del buffer[-1]
        elif bracket == '}':
            if len(buffer) < 1 or buffer[-1] != '{':
                return False
            del buffer[-1]
        elif bracket == ']':
            if len(buffer) < 1 or buffer[-1] != '[':
                return False
            del buffer[-1]
        else:
            # error state
            pass
    return len(buffer) < 1


class TestLeetCode(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(isPalindrome(1234567654321))
        self.assertFalse(isPalindrome(123456789))

    def test_palindrome_recursive(self):
        self.assertTrue(is_palindrome_recursive("aa"))
        self.assertTrue(is_palindrome_recursive("aba"))
        self.assertFalse(is_palindrome_recursive("abc"))
        self.assertTrue(is_palindrome_recursive("abcdedcba"))
        self.assertTrue(is_palindrome_recursive("abcdeffedcba"))

    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("xabay"), "aba")
        self.assertEqual(longest_palindrome("aa"), "aa")
        self.assertEqual(longest_palindrome("aba"), "aba")
        self.assertEqual(longest_palindrome("abcdef"), "")
        self.assertEqual(longest_palindrome("xgsg3u3fedcbabcdefdy"), "fedcbabcdef")
        self.assertEqual(longest_palindrome("my racecar has a radar"), " racecar ")

    def test_roman_to_int(self):
        self.assertTrue(romanToInt("IX"), 9)
        self.assertTrue(romanToInt("III"), 3)
        self.assertTrue(romanToInt("LVIII"), 58)
        self.assertTrue(romanToInt("MCMXCIV"), 1994)

    def test_bracket_checker(self):
        self.assertTrue(bracket_checker("[[][]{}()]"))
        self.assertFalse(bracket_checker("[[][]{}()]}"))
        self.assertFalse(bracket_checker("([)]"))

