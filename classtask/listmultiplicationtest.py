import unittest
import listmultiplication
class MyTestCase(unittest.TestCase):
  def test_list_multiplication(self):
    number = [3, 7, 2, 6, 5]
    expected = [27, 343, 8, 216, 125]
    result = listmultiplication.multiplication(number)
    self.assertEqual(result, expected)
