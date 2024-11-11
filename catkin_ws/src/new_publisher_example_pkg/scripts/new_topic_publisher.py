#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 

def main():
    rospy.init_node('new_topic_publisher', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    cmdvel_msg = Twist()
    cmdvel_msg.linear.x = 0.2
    cmdvel_msg.linear.z = 0.5


    while not rospy.is_shutdown(): 
        pub.publish(cmdvel_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass