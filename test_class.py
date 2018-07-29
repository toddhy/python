import unittest
from oop1_class import Point


class TestCase(unittest.TestCase):

    def test_slope(self):
        """Does 4, 10 return 2.5?"""
#        a = Point(4,10)
        self.assertEqual(Point(4,10).slope_from_origin(), 2.5)
        
    def test_getline(self):
        self.assertEqual((Point(4, 11).get_line_to(Point(6, 15))), (2, 3))

if __name__ == '__main__':
    unittest.main()