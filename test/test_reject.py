import unittest
from _.main import reject


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = reject

    def test_reject_returns_list_without_elements_that_pass_predicate(self):
        first = {"id": 1, "size": "L"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "M"}
        expected = [second, third]
        actual = self.sut([first, second, third], lambda e: e['size'] == 'L')
        self.assertEqual(expected, actual)
