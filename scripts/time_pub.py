#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
#from datetime import datetime

if __name__ == '__main__':
    rospy.init_node('time_pub')
    pub = rospy.Publisher('time', Point, queue_size=100)
    rate = rospy.Rate(1)
    time = Point()
    while not rospy.is_shutdown():
        time.x = rospy.Time.now().to_sec()
        time.y += 1
        pub.publish(time)
        rate.sleep()
