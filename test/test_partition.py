import unittest
from _.main import partition


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = partition

    def test_some_returns_true_if_any_element_satisfies_predicate(self):
        first = {"id": 1, "size": "M"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "L"}
        forth = {"id": 4, "size": "XL"}
        expected = [[first, second],[third, forth]]
        actual = self.sut([first, second, third, forth], lambda e: e['size'] == 'M')
        self.assertEqual(expected, actual)
