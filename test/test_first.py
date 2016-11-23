import unittest
from _.main import first


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = first

    def test_first_returns_the_first_element_in_collection(self):
        expected = 5
        actual = self.sut([5, 4, 3, 2, 1])
        self.assertEqual(expected, actual)

    def test_first_returns_the_first_n_elements_in_collection(self):
        expected = [5, 4, 3]
        actual = self.sut([5, 4, 3, 2, 1], 3)
        self.assertEqual(expected, actual)
