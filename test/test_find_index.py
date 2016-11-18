import unittest
from _.main import find_index


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = find_index

    def test_find_index_returns_index_of_first_element_that_satisfies_predicate(self):
        first = {"id": 1, "size": "L"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "M"}
        expected = 1
        actual = self.sut([first, second, third], lambda e: e["size"] == "M")
        self.assertEqual(expected, actual)
