import unittest
from _.main import every


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = every

    def test_every_returns_true_if_all_elements_pass_predicate(self):
        first = {"id": 1, "size": "L"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "M"}
        expected = False
        actual = self.sut([first, second, third], lambda e: e['size'] == 'M')
        self.assertEqual(expected, actual)

        first['size'] = 'M'
        expected = True
        actual = self.sut([first, second, third], lambda e: e['size'] == 'M')
        self.assertEqual(expected, actual)
