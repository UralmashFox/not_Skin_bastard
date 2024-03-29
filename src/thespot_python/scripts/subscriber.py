#! /usr/bin/python
# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import time
# Instantiate CvBridge
bridge = CvBridge()

start_time = int(time.time())

def image_callback(msg):
    print('Received an image!')
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a png
        #time = str(msg.header.stamp)

        t = str(int(time.time()) - start_time + 1)
        print(t)
   
        cv2.imwrite("/home/marina/spot/pic"+t+".png", cv2_img)

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/thespot/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
