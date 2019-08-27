
import unittest
from triangle import classifyTriangle, rightTriangle


class Test(unittest.TestCase):

   # def testTriangleClassification(self):
        
    def testTriangleClassification(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene Triangle')
        self.assertEqual(classifyTriangle(4, 4, 5), 'Scalene Triangle', 'should fail') 
        self.assertEqual(classifyTriangle(3, 4, 7), 'Isosceles Triangle', 'should fail') 
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles Triangle')
        self.assertEqual(classifyTriangle(3, 8, 3), 'Equilateral Triangle', 'should fail') 
        self.assertEqual(classifyTriangle(7, 7, 7), 'Equilateral Triangle')
        
    def testRightTriangle(self):
        self.assertEqual(rightTriangle(1, 3, 9), 'Not a right triangle')
        self.assertEqual(rightTriangle(3, 4, 5), 'Not a right triangle', 'should fail')
        self.assertEqual(rightTriangle(5, 12, 13), 'Right Triangle')
        self.assertEqual(rightTriangle(5, 14, 12), 'Right Triangle', 'should fail')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()