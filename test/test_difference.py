import unittest
from _.main import difference

class sut(unittest.TestCase):

    def setUp(self):
        self.difference = difference

    def test_difference_returns_all_elements_in_a_not_in_b(self):
        a = [1, 2, 3]
        b = [1, 3]
        expected = [2]
        actual = self.difference(a, b)
        self.assertEqual(expected, actual)
