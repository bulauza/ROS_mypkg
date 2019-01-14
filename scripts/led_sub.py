#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
import os
import time

n = 0
status = None

def cb(message):
    global n
    global status

    n = message.y
    if n % 5 == 3:
        os.system("gpio -g write 25 0")
        status = "led : off"

    if n % 5 == 0: # /1sec
        os.system("gpio -g write 25 1")
        status = "led : on"

    rospy.loginfo(status)

if __name__ == '__main__': 
    os.system('gpio -g mode 25 out')
    rospy.init_node('led')
    sub = rospy.Subscriber('time', Point, cb) 
    pub = rospy.Publisher('status_led', String, queue_size=100) 
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(status)
        rate.sleep()
    os.system("gpio -g write 25 0")
    pub.publish("led : off")
