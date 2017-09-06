import unittest
from _.main import take_while as sut


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = sut

    def test_take_while_returns_elements_until_predicate_no_longer_satisfied(self):
        expected = [2, 4]
        actual = self.sut([2, 4, 3, 6], lambda e: e % 2 is 0)
        self.assertEqual(expected, actual)