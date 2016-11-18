import unittest
from _.main import some


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = some

    def test_some_returns_true_if_any_element_satisfies_predicate(self):
        first = {"id": 1, "size": "M"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "L"}
        expected = True
        actual = self.sut([first, second, third], lambda e: e['size'] == 'L')
        self.assertEqual(expected, actual)

        expected = False
        actual = self.sut([first, second, third], lambda e: e['size'] == 'S')
        self.assertEqual(expected, actual)
