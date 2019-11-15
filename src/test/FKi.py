#! /usr/bin/python
from std_msgs.msg import Float64
import re
from std_srvs.srv import Trigger, TriggerRequest, TriggerResponse
import rospy
import math
import numpy as np
import time

Length = 0.4
Width = 0.2
Hight = 0.1
angle = 0.7
X = -0.15
Y = 0.2
Z = 0.2
x = -0.13
y = 0.055
z = 0.1
length = 0.2
width = 0.03
hight = 0.03
n = 0
t = 0
A = np.sin(t)  # angle of big leg
a = np.cos(t)  # angle of small leg

def world_to_zero(X, Y, Z):
    try:
        X = float(X)
        Y = float(Y)
        Z = float(Z)
        Rotw0 = [0, 1, 0,
                0, 0, 1,
                1, 0, 0]
        Rotw0 = np.reshape(Rotw0, (3, 3))
        Tw0 = [Rotw0[0, 0], Rotw0[0, 1], Rotw0[0, 2], X,
               Rotw0[1, 0], Rotw0[1, 1], Rotw0[1, 2], Y,
               Rotw0[2, 0], Rotw0[2, 1], Rotw0[2, 2], Z,
                 0, 0, 0, 1]
        Tw0 = np.reshape(Tw0, (4, 4)) 
        outputWZ = Tw0  
    except:
        outputWZ = 'Check you input before finding translation from world frame to zero joint'
    print(outputWZ)
    return(outputWZ)   

def zero_to_one(A,length,width):
    try:
        err = np.sqrt(length)
        err = np.sqrt(width)
        A = float(A)
        Rt01 = [np.cos(0.7 + A), -np.sin(0.7 + A), 0,
                np.sin(0.7 + A), np.cos(0.7 + A), 0,
                0, 0, 1]
        Rt01 = np.reshape(Rt01, (3, 3))
        R01 = [1, 0, 0,
               0, 1, 0,
               0, 0, 1]
        R01 = np.reshape(R01, (3, 3))
        Rot01 = Rt01 * R01
        Rot01 = np.reshape(Rot01, (3, 3))
        T01 = [Rot01[0, 0], Rot01[0, 1], Rot01[0, 2], length * np.cos(0.7 + A),
               Rot01[1, 0], Rot01[1, 1], Rot01[1, 2], width,
               Rot01[2, 0], Rot01[2, 1], Rot01[2, 2], length * np.sin(0.7 + A),
                0, 0, 0, 1]
        T01 = np.reshape(T01, (4, 4))
        outputZO = T01
    except:
        outputZO = "Check sizes and angle of big leg"
    print(outputZO)
    return(outputZO)
    
def one_to_end_effector(a,length,width):
    try:
        err = np.sqrt(length)
        err = np.sqrt(width)
        a = float(a)
        Rt1ef = [np.cos(-0.7 + a), -np.sin(-0.7 + a), 0,
                 np.sin(-0.7 + a), np.cos(-0.7 + a), 0,
                    0, 0, 1]
        Rt1ef = np.reshape(Rt1ef, (3, 3))
        R1ef = [1, 0, 0,
                0, 1, 0,
                0, 0, 1]
        R1ef = np.reshape(R1ef, (3, 3))
        Rot1ef = Rt1ef * R1ef
        Rot1ef = np.reshape(Rot1ef, (3, 3))
        T1ef = [Rot1ef[0, 0], Rot1ef[0, 1], Rot1ef[0, 2], length * np.cos(0.7 + a),
                Rot1ef[1, 0], Rot1ef[1, 1], Rot1ef[1, 2], 1 / 2 * width,
                Rot1ef[2, 0], Rot1ef[2, 1], Rot1ef[2, 2], length * np.sin(0.7 + a),
                0, 0, 0, 1]
        T1ef = np.reshape(T1ef, (4, 4))
        outputOE = T1ef
    except:
        outputOE = "Check sizes and angle of small leg"
    print(outputOE)
    return(outputOE)

def ForKin(X,Y,Z,A,a,length,width):
    try:
        Tw0 = world_to_zero(X,Y,Z)
        T01 = zero_to_one(A,length,width)
        T1ef = one_to_end_effector(a,length,width)
        Twef = Tw0 * T01 * T1ef
        Xef = Twef[0, 3]
        Yef = Twef[1, 3]
        Zef = Twef[2, 3]
        outputForKin = [Xef, Yef, Zef]
    except:
        outputForKin = 'Your data is awful :3'
    print(outputForKin)
    return(outputForKin)

try:
    Xef, Yef, Zef = ForKin(X,Y,Z,A,a,length,width)
    print(Xef, Yef, Zef)
    output = Xef, Yef, Zef
except: 
    output = "I don't like your input"
print(output)

def trigger_response(request):
    return TriggerResponse(
    success=True,
    message =  str(output)      
    )
rospy.init_node('Say') 
my_service = rospy.Service('Say', Trigger, trigger_response)
time.sleep(1)
