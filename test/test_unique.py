import unittest
from _.main import unique

class sut(unittest.TestCase):

    def setUp(self):
        self.unique = unique

    def test_unique_returns_all_elements_of_a_and_b(self):
        expected = [1, 2]
        actual = self.unique([1, 1, 2])
        self.assertEqual(expected, actual)
