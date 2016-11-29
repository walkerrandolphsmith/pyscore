import unittest
from _.main import initial


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = initial

    def test_initial_returns_all_except_last_element(self):
        expected = [5, 4, 3, 2]
        actual = self.sut([5, 4, 3, 2, 1])
        self.assertEqual(expected, actual)

    def test_initial_returns_all_except_last_n_elements(self):
        expected = [5, 4]
        actual = self.sut([5, 4, 3, 2, 1], 3)
        self.assertEqual(expected, actual)
