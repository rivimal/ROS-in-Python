#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from bb8_circle_service.srv import BB8MoveCircleCustom, BB8MoveCircleCustomResponse

def handle_move_bb8_in_circle_custom(req):
    rospy.loginfo("Service called: Moving BB8 in a circle for %s seconds", req.duration)
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    # Create twist message for circular movement
    vel_msg = Twist()
    vel_msg.linear.x = 0.2  # Forward speed
    vel_msg.angular.z = 0.2  # Angular speed for circular movement

    # Move for the specified duration
    for _ in range(req.duration * 10):  # 10 Hz
        vel_pub.publish(vel_msg)
        rate.sleep()

    # Stop the robot after moving
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

    rospy.loginfo("BB8 stopped after %s seconds", req.duration)
    return BB8MoveCircleCustomResponse(True)

rospy.init_node('bb8_move_custom_service_server')
rospy.Service('/move_bb8_in_circle_custom', BB8MoveCircleCustom, handle_move_bb8_in_circle_custom)
rospy.loginfo("Service /move_bb8_in_circle_custom is ready.")
rospy.spin()
