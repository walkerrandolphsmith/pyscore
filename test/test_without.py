import unittest
from _.main import without


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = without

    def test_without_returns_an_instance_of_the_list_with_the_values_removed(self):
        first = {"id": 1, "size": "L"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "M"}
        expected = [second, third]
        actual = self.sut([first, second, third], first)
        self.assertEqual(expected, actual)