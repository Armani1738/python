import unittest

from javapythonassignment.functionsclass import largest_element


class MyTestCase(unittest.TestCase):
    def test_largest(self):
        number = [45,76,23,87,23,56]
        largest = 87
        result = largest_element(number)
        self.assertEqual(result, largest)