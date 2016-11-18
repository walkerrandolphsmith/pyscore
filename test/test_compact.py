import unittest
from _.main import compact


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = compact

    def test_compact_filters_out_falsy_values(self):
        expected = [True, 3]
        actual = self.sut([False, None, True, 3])
        self.assertEqual(expected, actual)
