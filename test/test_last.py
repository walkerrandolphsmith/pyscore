import unittest
from _.main import last


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = last

    def test_last_returns_the_last_element_in_collection(self):
        expected = 1
        actual = self.sut([5, 4, 3, 2, 1])
        self.assertEqual(expected, actual)

    def test_last_returns_the_last_n_elements_in_collection(self):
        expected = [3, 2, 1]
        actual = self.sut([5, 4, 3, 2, 1], 3)
        self.assertEqual(expected, actual)

    def test_last_returns_all_elements_in_collection_when_given_len_of_list(self):
        expected = [5, 4, 3, 2, 1]
        actual = self.sut([5, 4, 3, 2, 1], 5)
        self.assertEqual(expected, actual)
