import unittest
from _ import some

class sut(unittest.TestCase):

    def setUp(self):
        self.some = some.some

    def test_some_returns_true_if_any_element_satisfies_predicate(self):
        first = {"id": 1, "size": "M"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "L"}
        expected = True
        actual = self.some([first, second, third], lambda e: e['size'] == 'L')
        self.assertEqual(expected, actual)

        expected = False
        actual = self.some([first, second, third], lambda e: e['size'] == 'S')
        self.assertEqual(expected, actual)
