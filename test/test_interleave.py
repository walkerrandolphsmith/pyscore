import unittest
from _.main import interleave


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = interleave

    def test_interleave_returns_all_elements_from_the_collections_interleaved(self):
        expected = [1, 2, 3, 4, 5, 6]
        actual = self.sut([1, 4], [2, 5], [3, 6])
        self.assertEqual(expected, actual)
