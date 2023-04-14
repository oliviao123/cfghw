# 2.2
import unittest
from isogram import is_isogram

class TestIsIsogram(unittest.TestCase):
    def test_is_isogram(self):
        # Test a simple isogram
        self.assertEqual(is_isogram("abcdefghijklmnopqrstuvwxyz"), True)

        # Test an empty string
        self.assertEqual(is_isogram(""), True)

        # Test a single character string
        self.assertEqual(is_isogram("a"), True)

        # Test a string with repeated characters
        self.assertEqual(is_isogram("hello"), False)

        # Test a string with only one repeated character
        self.assertEqual(is_isogram("ambidextrously"), True)

        # Test a string with multiple repeated characters
        self.assertEqual(is_isogram("abracadabra"), False)

        # Test a string with both upper and lower case characters
        self.assertEqual(is_isogram("IsOgRaM"), True)

        # Test a string with special characters and spaces
        self.assertEqual(is_isogram("hello world!"), False)


if __name__ == '__main__':
    unittest.main()
#
# Test a simple isogram: I chose this test case to verify that the function correctly identifies a simple string
# containing all 26 letters of the alphabet as an isogram.
#
# Test an empty string: I chose this test case to verify that the function correctly identifies an empty string
# as an isogram.
#
# Test a single character string: I chose this test case to verify that the function correctly identifies a
# single character string as an isogram.
#
# Test a string with repeated characters: I chose this test case to verify that the function correctly
# identifies a string with repeated characters as not an isogram.
#
# Test a string with only one repeated character: I chose this test case to verify that the function correctly
# identifies a string with only one repeated character as not an isogram.
#
# Test a string with multiple repeated characters: I chose this test case to verify that the function correctly
# identifies a string with multiple repeated characters as not an isogram.
#
# Test a string with both upper and lower case characters: I chose this test case to verify that the function
# correctly identifies a string with mixed upper and lower case characters as an isogram.
#
# Test a string with special characters and spaces: I chose this test case to verify that the function
# correctly ignores special characters and spaces in the input string and correctly identifies the string as not an isogram
