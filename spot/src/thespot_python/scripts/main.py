#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import Float64

def talker():
    pubLBB = rospy.Publisher('/thespot_robot/left_back_big/command', Float64, queue_size=10)
    pubRFB = rospy.Publisher('/thespot_robot/right_forward_big/command', Float64, queue_size=10)
    pubLFB = rospy.Publisher('/thespot_robot/left_forward_big/command', Float64, queue_size=10)
    pubRBB = rospy.Publisher('/thespot_robot/right_back_big/command', Float64, queue_size=10)

    pubLBS = rospy.Publisher('/thespot_robot/left_back_small/command', Float64, queue_size=10)
    pubRFS = rospy.Publisher('/thespot_robot/right_forward_small/command', Float64, queue_size=10)
    pubLFS = rospy.Publisher('/thespot_robot/left_forward_small/command', Float64, queue_size=10)
    pubRBS = rospy.Publisher('/thespot_robot/right_back_small/command', Float64, queue_size=10)


    rospy.init_node('thespot_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    angle = 0
    while not rospy.is_shutdown():

        positionLBB = math.sin(angle)
        rospy.loginfo(positionLBB)
        pubLBB.publish(positionLBB)

        positionRFB = math.sin(angle)
        rospy.loginfo(positionRFB)
        pubRFB.publish(positionRFB)

        positionLFB = -math.sin(angle)
        rospy.loginfo(positionLFB)
        pubLFB.publish(positionLFB)

        positionRBB = -math.sin(angle)
        rospy.loginfo(positionRBB)
        pubRBB.publish(positionRBB)
#Small legz:

        positionLBS = math.cos(angle)
        rospy.loginfo(positionLBS)
        pubLBS.publish(positionLBS)

        positionRFS = math.cos(angle)
        rospy.loginfo(positionRFS)
        pubRFS.publish(positionRFS)

        positionLFS = -math.cos(angle)
        rospy.loginfo(positionLFS)
        pubLFS.publish(positionLFS)

        positionRBS = -math.cos(angle)
        rospy.loginfo(positionRBS)
        pubRBS.publish(positionRBS)



        rate.sleep()
        angle += 0.9

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass