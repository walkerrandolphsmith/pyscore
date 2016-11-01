import unittest
from _ import compact

class sut(unittest.TestCase):

    def setUp(self):

        self.compact = compact.compact

    def test_compact_filters_out_falsy_values(self):
        expected = [True, 3]
        actual = self.compact([False, None, True, 3])
        self.assertEqual(expected, actual)