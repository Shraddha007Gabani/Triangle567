# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testxRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), "Right")

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4), 'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral')

    def testEquilateralTriangles1(self): 
        self.assertEqual(classifyTriangle(2,2,2), 'Equilateral')

    def testIsocelesTriangles2(self): 
        self.assertEqual(classifyTriangle(1,1,2), 'NotATriangle')

    def testIsocelesTriangles3(self): 
        self.assertEqual(classifyTriangle(3,4,3), 'Isoceles')

    def testIsocelesTriangles4(self): 
        self.assertEqual(classifyTriangle(4,10,10), 'Isoceles')

    def testScaleneTriangles5(self): 
        self.assertEqual(classifyTriangle(10,11,12),'Scalene')

    def testNotATriangleTriangles6(self): 
        self.assertEqual(classifyTriangle(0,1,1), 'InvalidInput')

    def testInvalidInputTriangles7(self): 
        self.assertEqual(classifyTriangle(300,1,1), 'InvalidInput')

    def testInvalidInputTriangles8(self): 
        self.assertEqual(classifyTriangle(300.05,1,1), 'InvalidInput')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

