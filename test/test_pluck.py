import unittest
from _.main import pluck

class sut(unittest.TestCase):

    def setUp(self):
        self.pluck = pluck

    def test_some_returns_true_if_any_element_satisfies_predicate(self):
        first = {"id": 1, "size": "M"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "L"}
        expected = [1, 2, 3]
        actual = self.pluck([first, second, third], 'id')
        self.assertEqual(expected, actual)
