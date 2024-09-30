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
    if len(s) < 2:
        return s
    def search(s: str, left: int, right: int) -> str:
        if right == len(s):
            return ''
        if len(s) == 2:
            return s if s[0] == s[1] else ''

        while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
            left -= 1
            right += 1

        palindrome = s[left:right+1] if (right - left > 0 and s[left] == s[right]) else ''
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    if head.next is None:
        return None
    n = find_and_remove(head, n)
    # special case: the head item needs to be removed
    if n != -1:
        head = head.next
    return head


def find_and_remove(node: ListNode, index) -> int:
    if node is None:
        return 0
    else:
        n = find_and_remove(node.next, index)
        if n == -1:
            return n  # already found and removed
        if n == index:
            node.next = node.next.next
            return -1
        return n + 1


def letter_combinations(digits: str) -> [str]:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    output = []
    for num_val in digits:
        if len(output) == 0:
            output = mapping[num_val]
        else:
            tmp = []
            for char_val in mapping[num_val]:
                for output_item in output:
                    tmp.append(output_item + char_val)
            output = tmp
    return output


def is_valid_sudoku(board: [str]) -> bool:
    # check rows and columns
    for i in range(9):
        tmp_c = set()
        tmp_r = set()
        for j in range(9):
            # i'th row
            if board[i][j] != ".":
                if board[i][j] in tmp_r:
                    return False
                tmp_r.add(board[i][j])
            # j'th column
            if board[j][i] != ".":
                if board[j][i] in tmp_c:
                    return False
                tmp_c.add(board[j][i])

    # check 9x9 grids
    for offset_i in range(3):
        for offset_j in range(3):
            tmp_g = set()
            for i in range(3):
                for j in range(3):
                    i_with_offset = i + offset_i * 3
                    j_with_offset = j + offset_j * 3
                    if board[i_with_offset][j_with_offset] != ".":
                        if board[i_with_offset][j_with_offset] in tmp_g:
                            return False
                        tmp_g.add(board[i_with_offset][j_with_offset])
    return True
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
        self.assertEqual(longest_palindrome("a"), "a")
        self.assertEqual(longest_palindrome("ac"), "")
        self.assertEqual(longest_palindrome("xabay"), "aba")
        self.assertEqual(longest_palindrome("aa"), "aa")
        self.assertEqual(longest_palindrome("aba"), "aba")
        self.assertEqual(longest_palindrome("cbbd"), "bb")
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

    def test_remove_nth_from_end(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head = remove_nth_from_end(head, 2)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)
        self.assertEqual(head.next.next.next.val, 5)
        self.assertEqual(head.next.next.next.next, None)

    def test_letter_combinations(self):
        self.assertEqual(letter_combinations(""), [])
        self.assertEqual(set(letter_combinations("2")), set(["a", "b", "c"]))
        self.assertEqual(set(letter_combinations("23")), set(["ad","ae","af","bd","be","bf","cd","ce","cf"]))

    def test_is_valid_sudoku(self):
        self.assertTrue(is_valid_sudoku([["5","3",".",".","7",".",".",".","."]
                                        ,["6",".",".","1","9","5",".",".","."]
                                        ,[".","9","8",".",".",".",".","6","."]
                                        ,["8",".",".",".","6",".",".",".","3"]
                                        ,["4",".",".","8",".","3",".",".","1"]
                                        ,["7",".",".",".","2",".",".",".","6"]
                                        ,[".","6",".",".",".",".","2","8","."]
                                        ,[".",".",".","4","1","9",".",".","5"]
                                        ,[".",".",".",".","8",".",".","7","9"]]))
        self.assertFalse(is_valid_sudoku([["8","3",".",".","7",".",".",".","."]
                                        ,["6",".",".","1","9","5",".",".","."]
                                        ,[".","9","8",".",".",".",".","6","."]
                                        ,["8",".",".",".","6",".",".",".","3"]
                                        ,["4",".",".","8",".","3",".",".","1"]
                                        ,["7",".",".",".","2",".",".",".","6"]
                                        ,[".","6",".",".",".",".","2","8","."]
                                        ,[".",".",".","4","1","9",".",".","5"]
                                        ,[".",".",".",".","8",".",".","7","9"]]))


