import unittest

from javapythonassignment.functionsclass import largest_element, reverse_list, element, odd_number, even_numbers

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
        result = element(number)
        self.assertEqual(result, answer)

    def test_odd_number(self):
        number = [1,2,3,4,5,6,7,8,9,10]
        answer = [1,3,5,7,9]
        result = odd_number(number)
        self.assertEqual(result, answer)

    def test_even_numbers(self):
        number = [1,2,3,4,5,6,7,8,9,10]
        answer = [2,4,6,8,10]
        result = even_numbers(number)
        self.assertEqual(result, answer)