from unittest import TestCase

from tupleassignment import TupleAssignment

class Test(TestCase):
    def test_reverse(self):
        new_tuple = (10, 20, 30, 40, 50)
        result = TupleAssignment.reverse(new_tuple)
        number1 = (50, 40, 30, 20, 10)
        self.assertEqual(result, number1)

    def test_nested_tuple(self):
        numbers = ("Orange", [10, 20, 30], (5, 15, 25))
        result = TupleAssignment.nested_tuple(numbers)
        expected = ((0, 20), (1, 25))
        self.assertEqual(result, expected)

    def test_lastnfirst_number(self):
        numbers = (15, 25, 60, 50, 30, 40, 45, 55)
        result = TupleAssignment.last_and_first_number(numbers)
        expected = (55, 15)
        self.assertEqual(result, expected)

    def test_sort_items(self):
        numbers = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
        result = TupleAssignment.sorted_numbers
        expected =  (('c', 11), ('a', 23), ('d', 29), ('b', 37))
        self.assertEqual(('c', 11), expected[0])
        self.assertEqual(('a', 23), expected[1])
        self.assertEqual(('d', 29), expected[2])
        self.assertEqual(('b', 37), expected[3])


    def test_appeared_numbers(self):
        numbers = [20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5]
        result = TupleAssignment.appeared_numbers(numbers)
        expected = [20, 10, 5]
        self.assertEqual(result, expected)

