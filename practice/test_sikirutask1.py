from unittest import TestCase
from sikirutask1 import list_of_numbers, odd, double_item, change_element_index, empty_list, concatenate_list, excercise


class Test(TestCase):
    def test_list_of_numbers(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(expected, list_of_numbers(1, 21))

    def test_for_the_odd_number_of_a_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.assertEqual(expected, odd(numbers))

    def test_for_the_double_number(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
        self.assertEqual(expected, double_item(odd(numbers)))

    def test_change_index(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 9, 25, 49, 0, 0, 0, 0, 289, 361]
        self.assertEqual(expected, change_element_index(double_item(odd(numbers))))

    def test_empty_lists(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = []
        self.assertEqual(expected, empty_list(change_element_index(double_item(odd(numbers)))))

    def test_concatenate_list(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        lists = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(lists, concatenate_list(list1, list2))

    def test_excercise(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        lists = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(lists, excercise(list1, list2))
