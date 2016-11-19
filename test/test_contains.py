import unittest
from _.main import contains


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = contains

    def test_contains_returns_true_if_element_is_in_list(self):
        expected = True
        actual = self.sut([1, 2, 3], 3)
        self.assertEqual(expected, actual)

    def test_contains_returns_false_if_element_is_not_in_list(self):
        expected = False
        actual = self.sut([1, 2, 3], 5)
        self.assertEqual(expected, actual)