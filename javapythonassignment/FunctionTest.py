import unittest

from javapythonassignment.functionsclass import largest_element, reverse_list, check_element


class MyTestCase(unittest.TestCase):
    def test_largest(self):
        number = [45, 76, 23, 87, 23, 56]
        largest = 87
        result = largest_element(number)
        self.assertEqual(result, largest)

    def test_reverse(self):
        number = [7, 3, 8, 6, 1, 20]
        number1 = [20, 1, 6, 8, 3, 7]
        result = reverse_list(number)
        self.assertEqual(result, number1)

    def test_element(self):
        number = [3, 4, 5, 6, 7, 9]
        answer = [6]
        result = check_element(number)
        self.assertEqual(result, answer)
