import unittest
from _.main import reverse


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = reverse

    def test_reverse_reverses_a_list(self):
        expected = [3, 2, 1]
        actual = self.sut([1, 2, 3])
        self.assertEqual(expected, actual)
