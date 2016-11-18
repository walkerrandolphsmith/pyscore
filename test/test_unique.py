import unittest
from _.main import unique


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = unique

    def test_unique_returns_all_elements_of_a_and_b(self):
        expected = [1, 2]
        actual = self.sut([1, 1, 2])
        self.assertEqual(expected, actual)
