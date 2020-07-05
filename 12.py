"""
Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""
import unittest

def is_palindrome(ip_string):
    check_str=''.join(list(reversed(ip_string)))
    if ip_string==check_str:
        return f'Palindrome'
    else:
        return f'Non Palindrome'
class TestPalindrome(unittest.TestCase):
    def test_str(self):
        self.assertEquals(is_palindrome('aba'), "Palindrome")
        self.assertEquals(is_palindrome('abaa'), "Non Palindrome")
    def test_num(self):
        self.assertEquals(is_palindrome('121'), "Palindrome")
        self.assertEquals(is_palindrome('123'), "Non Palindrome")
if __name__ == "__main__":
    print(is_palindrome(input('Enter string or number')))
    unittest.main()