import unittest
from _.main import sample


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = sample

    def test_sample_returns_a_list_with_a_single_element(self):
        expected = 1
        actual = len(self.sut([1, 2, 3, 4]))
        self.assertEqual(expected, actual)

    def test_sample_returns_new_list_with_sample_size_elements(self):
        expected = 2
        actual = len(self.sut([1, 2, 3, 4], 2))
        self.assertEqual(expected, actual)
