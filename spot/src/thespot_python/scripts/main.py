#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import Float64
import rospy
from std_msgs.msg import String

def talker():
    pubLBB = rospy.Publisher('/thespot_robot/left_back_big/command', Float64, queue_size=10)
    pubRFB = rospy.Publisher('/thespot_robot/right_forward_big/command', Float64, queue_size=10)
    pubLFB = rospy.Publisher('/thespot_robot/left_forward_big/command', Float64, queue_size=10)
    pubRBB = rospy.Publisher('/thespot_robot/right_back_big/command', Float64, queue_size=10)

    pubLBS = rospy.Publisher('/thespot_robot/left_back_small/command', Float64, queue_size=10)
    pubRFS = rospy.Publisher('/thespot_robot/right_forward_small/command', Float64, queue_size=10)
    pubLFS = rospy.Publisher('/thespot_robot/left_forward_small/command', Float64, queue_size=10)
    pubRBS = rospy.Publisher('/thespot_robot/right_back_small/command', Float64, queue_size=10)
    print("HELLO")

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
        angle += 0.5

""" def callback(data):
    rospy.loginfo("I heard %s",data.data)
    print m._connection_header
    {'callerid': '/talker_38321_1284999593611',
    'latching': '0',
    'md5sum': '992ce8a1687cec8c8bd883ec73ca41d1',
    'message_definition': 'string data\n\n',
    'topic': '/chatter',
    'type': 'std_msgs/String'}
    
def listener():
    rospy.init_node('thespot_talker')
    rospy.Subscriber("chatter", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin() """

if __name__ == '__main__':
    try:
        talker()
        #listener()
    except rospy.ROSInterruptException:
        pass



