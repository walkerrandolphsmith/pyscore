import unittest
from _ import find_all

class sut(unittest.TestCase):

    def setUp(self):

        self.find_all = find_all.find_all

    def test_find_all_filters_out_elements_that_dont_satisfy_predicate(self):
        first = {"id": 1, "size": "M"}
        second = {"id": 2, "size": "S"}
        third = {"id": 3, "size": "L"}
        expected = [first]
        actual = self.find_all([first, second, third], lambda e: e["size"] == "M")
        self.assertEqual(expected, actual)