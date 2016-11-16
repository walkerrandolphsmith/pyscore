import unittest
from _.main import interleave

class sut(unittest.TestCase):

    def setUp(self):
        self.interleave = interleave

    def test_interleave_returns_all_elements_from_the_collections_interleaved(self):
        expected = [1, 2, 3, 4, 5, 6]
        actual = self.interleave([1, 4], [2, 5], [3, 6])
        self.assertEqual(expected, actual)
