import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
import unittest
from isogram import is_isogram


class TestIsIsogram(unittest.TestCase):
    def test_empty_string(self):
        # An empty string should be considered an isogram
        self.assertTrue(is_isogram(""))

    def test_single_character(self):
        # A single character is always an isogram
        self.assertTrue(is_isogram("a"))
        self.assertTrue(is_isogram("z"))

    def test_all_lowercase_isogram(self):
        # A word with all lowercase letters and no repetition is an isogram
        self.assertTrue(is_isogram("isogram"))

    def test_mixed_case_isogram(self):
        # The function should be case-insensitive and still recognize the word as an isogram
        self.assertTrue(is_isogram("IsOgRaM"))

    def test_non_alphabetic_characters(self):
        # Non-alphabetic characters should be ignored in the isogram check
        self.assertTrue(is_isogram("is-o_gram!"))

    def test_repeated_letter(self):
        # A word with a repeated letter is not an isogram
        self.assertFalse(is_isogram("ambidextrously"))

    def test_repeated_letter_case_insensitive(self):
        # The function should be case-insensitive, so even if a letter is repeated with different cases, it should return False
        self.assertFalse(is_isogram("IsOgram"))

    def test_repeated_non_alphabetic_characters(self):
        # Repeated non-alphabetic characters should be ignored in the isogram check
        self.assertTrue(is_isogram("abc-def!"))
        self.assertTrue(is_isogram("abc_def!"))


if __name__ == '__main__':
    unittest.main()
