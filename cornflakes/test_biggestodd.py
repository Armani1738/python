from unittest import TestCase

from cornflakes import biggestodd


class Test(TestCase):
    def test_largest_number(self):
        numbers = '23569'
        expected = '9'
        self.assertEqual(biggestodd.bigger_odds(numbers), expected)


