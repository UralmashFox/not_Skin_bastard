#!/usr/bin/env python
tests = 'test_roslaunch'
from FK import world_to_zero
from FK import zero_to_one
from FK import one_to_end_effector
#import roslib; #roslib.load_manifest(tests)  # This line is not needed with Catkin.
import rospy
import unittest
import numpy as np
a = 5
A = 1
x = -100

class FK(unittest.TestCase):

    def test_world_to_zero(self):
        x = -100
        while x<100.5:
            X = 'blow'
            Y = 'blow'
            Z = 'blow'
            #print (Tw0)
            outputWZ = world_to_zero(X, Y, Z)
            self.assertNotEqual(outputWZ, 'none')
            x = x+0.5
        print("done test for world - zero frames")
        
    def test_zero_to_one(self):
        x = -100
        while x<100.5:
            A = 'blow'
            length = 'blow'
            width = 'blow'
            outputZO = zero_to_one(A, length, width)
            self.assertNotEqual(outputZO, 'none')
            x = x+0.5
        print("done test for world - zero frames")
        
# class zero_to_one(unittest.TestCase):

#     def test_FK()

#         A = 'pDjhSJj'

#         self.assertTrue(a)

# class one_to_end_effector(unittest.TestCase):

#     def runTest(self):
#         my_var = True

#         # do some things to my_var which might change its value...

#         self.assertTrue(my_var)

# class FK(unittest.TestCase):

#     def runTest(self):
#         my_var = False

#         # do some things to my_var which might change its value...

#         self.assertTrue(my_var)      

class MyTestSuite(unittest.TestSuite):

    def __init__(self):
        super(MyTestSuite, self).__init__()
        self.addTest(FK())
        # self.addTest(world_to_zero())
        # self.addTest(zero_to_one())
        # self.addTest(one_to_end_effector())
        # self.addTest(FK())

if __name__ == '__main__':
    import rostest
    from test_FK import FK
    rostest.rosrun('/home/marina/spot/src/tests', 'FK-report_WZ', 'test_FK', sysargs=None)

    unittest.main()