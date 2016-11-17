import unittest
from _.main import map_

class sut(unittest.TestCase):

    def setUp(self):
        self.map_ = map_

    def test_map_from_one_domain_to_another(self):
        expected = [2, 5, 8, 11]
        actual = self.map_([1, 2, 3, 4], lambda e, i: e * 2 + i)
        self.assertEqual(expected, actual)

    def test_map_iteratee_has_one_arg(self):
        expected = [2, 4, 6, 8]
        actual = self.map_([1, 2, 3, 4], lambda e: e * 2)
        self.assertEqual(expected, actual)