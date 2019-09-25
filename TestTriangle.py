import unittest
from Triangle import classify_triangle, right_triangle


class Test(unittest.TestCase):

    # def testTriangleClassification(self):

    def testTriangleClassification(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene Triangle')
        self.assertEqual(classify_triangle(4, 4, 5), 'Scalene Triangle', 'should fail')
        self.assertEqual(classify_triangle(3, 4, 7), 'Isosceles Triangle', 'should fail')
        self.assertEqual(classify_triangle(3, 3, 5), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(3, 8, 3), 'Equilateral Triangle', 'should fail')
        self.assertEqual(classify_triangle(7, 7, 7), 'Equilateral Triangle')

    def testRightTriangle(self):
        self.assertEqual(right_triangle(1, 3, 9), 'Not a right triangle')
        self.assertEqual(right_triangle(3, 4, 5), 'Not a right triangle', 'should fail')
        self.assertEqual(right_triangle(5, 12, 13), 'Right Triangle')
        self.assertEqual(right_triangle(5, 14, 12), 'Right Triangle', 'should fail')
        self.assertNotEqual(right_triangle(5, 14, 12), 'Right Triangle')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
