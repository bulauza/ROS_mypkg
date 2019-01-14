#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import String
from datetime import datetime

time = None
def cb(message):
    global time
#    global count

    # UNIX time conversion
    time = message.x
    time = datetime.fromtimestamp(time)
    time = '{0:%Y/%m/%d %H:%M:%S}'.format(time)
    rospy.loginfo(time)

if __name__ == '__main__':
    rospy.init_node('convert')
    rospy.Subscriber('time', Point, cb)
    pub = rospy.Publisher('time_str', String, queue_size=100)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(time)
        rate.sleep()
