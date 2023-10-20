import unittest
from cornflakes import equalstrings


class MyTestCase(unittest.TestCase):
    def test_true(self):
        first = "love"
        second = "evol"
        self.assertTrue(equalstrings.equal_strings(first, second))
