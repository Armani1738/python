import unittest

from classtask.task11 import value


class MyTestCase(unittest.TestCase):
    def test_value(self):
        number = [3, 4, 5, 6, 7, 9]
        answer = [6]
        result = value(number)
        self.assertEqual(result, answer)
