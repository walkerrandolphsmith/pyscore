import unittest
from _.main import find_all


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = find_all

    def test_find_all_filters_out_elements_that_dont_satisfy_predicate(self):
        first = {"id": 1, "size": "M"}
        second = {"id": 2, "size": "S"}
        third = {"id": 3, "size": "L"}
        expected = [first]
        actual = self.sut([first, second, third], lambda e: e["size"] == "M")
        self.assertEqual(expected, actual)
