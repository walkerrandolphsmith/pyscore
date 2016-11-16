import unittest
from _.main import reverse

class sut(unittest.TestCase):

    def setUp(self):
        self.reverse = reverse

    def test_reverse_reverses_a_list(self):
        expected = [3, 2, 1]
        actual = self.reverse([1, 2, 3])
        self.assertEqual(expected, actual)
