import unittest
from _.main import rest


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = rest

    def test_rest_returns_all_elements_excluding_the_first(self):
        expected = [4, 3, 2, 1]
        actual = self.sut([5, 4, 3, 2, 1])
        self.assertEqual(expected, actual)

    def test_rest_returns_elements_from_index_onwards(self):
        expected = [3, 2, 1]
        actual = self.sut([5, 4, 3, 2, 1], 2)
        self.assertEqual(expected, actual)
