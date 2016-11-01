import unittest
from _ import union

class sut(unittest.TestCase):

    def setUp(self):

        self.union = union.union

    def test_union_returns_all_elements_of_a_and_b(self):
        expected = [1, 2, 3, 4, 5]
        actual = self.union([1, 2, 3], [1, 4, 5])
        self.assertEqual(expected, actual)