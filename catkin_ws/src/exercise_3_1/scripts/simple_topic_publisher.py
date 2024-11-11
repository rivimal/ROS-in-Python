#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node('simple_topic_publisher', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 0.5  # Set forward speed
        msg.angular.z = 0.0  # No rotation
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

