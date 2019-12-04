#! /usr/bin/env python
import rospy
tests = 'test_roslaunch'
import unittest
from std_srvs.srv import Trigger, TriggerRequest, TriggerResponse
import numpy as np
import time

b = []
c = []

import tf
import geometry_msgs.msg
t = tf.Transformer(True, rospy.Duration(10.0))
t.getFrameStrings()
[]
m = geometry_msgs.msg.TransformStamped()
m.header.frame_id = 'world'
m.child_frame_id = 'camera_link'
xr = m.transform.translation.x
yr = m.transform.translation.y
zr = m.transform.translation.z
print (xr, yr, zr)

rospy.init_node('listen')
rospy.wait_for_service('Say')
sos_service = rospy.ServiceProxy('Say', Trigger)
sos = TriggerRequest()
result = sos_service(sos)

b = str(result)
b = b[25:]
b = b[:-2]
c = np.fromstring(b, dtype=np.float, sep=', ')
xc = round(c[0], 1)
yc = round(c[1], 1)
zc = round(c[2], 1)
print (xc, yc, zc)

class FK(unittest.TestCase):

    def test_FKi(self):
        self.assertAlmostEqual(xc, xr)
        print("done integ test")

if __name__ == '__main__':
    import rostest
    from test_FK import FK
    rostest.rosrun('/home, 'FK-report_FULL', 'test_FKi', sysargs=None)
    #unittest.main()

