#!/usr/bin/env python
tests = 'test_roslaunch'
from FK import world_to_zero
from FK import zero_to_one
from FK import one_to_end_effector
from FK import ForKin
import rospy
import unittest
import numpy as np

class FK(unittest.TestCase):

    def test_world_to_zero(self):
        x = -100
        while x<100.5:
            X = x
            Y = x
            Z = x
            outputWZ = world_to_zero(X, Y, Z)
            self.assertNotEqual(outputWZ, 'none')
            x = x+0.5
        print("done test for 'world - 0' frames")
        
    def test_zero_to_one(self):
        x = -100
        while x<100.5:
            A = 'blow'
            length = 'blow'
            width = 'blow'
            outputZO = zero_to_one(A, length, width)
            self.assertNotEqual(outputZO, 'none')
            x = x+0.5
        print("done test for '0 - 1' frames")
        
    def test_one_to_end_effector(self):
        x = -100
        while x<100.5:
            a = 'blow'
            length = 'blow'
            width = 'blow'
            outputOE = one_to_end_effector(a,length,width)
            self.assertNotEqual(outputOE, 'none')
            x = x+0.5
        print("done test for '1 - EF' frames")    

    def test_ForKin(self):
        X = 'blow'
        Y = 'blow'
        Z = 'blow'
        A = 'blow'
        a = 'blow'
        length = 'blow'
        width = 'blow'
        x = -100
        while x<100.5:
            outputFK = ForKin(X,Y,Z,A,a,length,width)
            self.assertNotEqual(outputFK, 'none')
            x = x+0.5
        print("done test for 'world - EF' frames")   

if __name__ == '__main__':
    import rostest
    #from test_FK import FK
    rostest.unitrun('/home', 'FK-report_WZ', 'test_FK.FK.test_world_to_zero', sysargs=None)
    rostest.unitrun('/home', 'FK-report_ZO', 'test_FK.FK.test_zero_to_one', sysargs=None)
    rostest.unitrun('/home', 'FK-report_OE', 'test_FK.FK.test_one_to_end_effector', sysargs=None)
    rostest.unitrun('/home', 'FK-report_FK', 'test_FK.FK.test_ForKin', sysargs=None)
    rostest.rosrun('/home', 'FK-report_FULL', 'test_FK', sysargs=None)


    #unittest.main()