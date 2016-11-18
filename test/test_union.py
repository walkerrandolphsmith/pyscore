import unittest
from _.main import union


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = union

    def test_union_returns_all_elements_of_a_and_b(self):
        expected = [1, 2, 3, 4, 5]
        actual = self.sut([1, 2, 3], [1, 4, 5])
        self.assertEqual(expected, actual)
