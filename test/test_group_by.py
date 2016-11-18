import unittest
from _.main import group_by


class Sut(unittest.TestCase):
    def setUp(self):
        self.sut = group_by

    def test_group_by_groups_values_by_key(self):
        expected = {
            "s": [1, 3],
            "m": [1],
            "l": [2]
        }
        actual = self.sut([(1, "s"), (1, "m"), (2, "l"), (3, "s")])
        self.assertEqual(expected, actual)
