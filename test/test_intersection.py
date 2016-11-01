import unittest
from _ import intersection

class sut(unittest.TestCase):

    def setUp(self):

        self.intersection = intersection.intersection

    def test_intersection_returns_elements_that_are_members_of_a_and_b(self):
        expected = [1]
        actual = self.intersection([1, 2, 3], [1, 4, 5])
        self.assertEqual(expected, actual)