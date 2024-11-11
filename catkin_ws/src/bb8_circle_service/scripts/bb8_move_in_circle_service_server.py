#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

def move_in_circle(req):
    rospy.loginfo("Moving BB8 in a circle...")
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    # Define circular motion
    vel_msg = Twist()
    vel_msg.linear.x = 0.2  # Move forward
    vel_msg.angular.z = 0.2  # Rotate to create a circle

    # Move for a certain amount of time
    for _ in range(50):  # Adjust for desired duration
        vel_pub.publish(vel_msg)
        rate.sleep()

    # Stop the robot after moving
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

    return EmptyResponse()

rospy.init_node('bb8_move_in_circle_service_server')
rospy.Service('/move_bb8_in_circle', Empty, move_in_circle)
rospy.loginfo("Service /move_bb8_in_circle ready.")
rospy.spin()
