#! /usr/bin/python
import rospy
import math
import numpy as np
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
        Rotw0 = [0, 1, 0,
                0, 0, 1,
                1, 0, 0]
        Rotw0 = np.reshape(Rotw0, (3, 3))
        Tw0 = [Rotw0[0, 0], Rotw0[0, 1], Rotw0[0, 2], X,
               Rotw0[1, 0], Rotw0[1, 1], Rotw0[1, 2], Y,
               Rotw0[2, 0], Rotw0[2, 1], Rotw0[2, 2], Z,
                 0, 0, 0, 1]
        Tw0 = np.reshape(Tw0, (4, 4))
        return(Tw0)
    except: print("what the hell are you trying to do with such values?", X)
def zero_to_one(A, length, width):
    try:
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
        return(T01)
    except: print("Good values I need!")
def one_to_end_effector(a,length,width):
    try:
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
        return(T1ef)
    except: print("Come around and paste adequate values")
def ForKin(X,Y,Z,A,a,length,width):
    try:
        Tw0 = world_to_zero()
        T01 = zero_to_one()
        T1ef = one_to_end_effector()
        Twef = Tw0 * T01 * T1ef
        Xef = Twef[0, 3]
        Yef = Twef[1, 3]
        Zef = Twef[2, 3]
        return(Xef, Yef, Zef)
    except: print("Your data is awful :3")
try:
    Xef, Yef, Zef = FK()
    print(Xef, Yef, Zef)
except: print("I don't like your input")
