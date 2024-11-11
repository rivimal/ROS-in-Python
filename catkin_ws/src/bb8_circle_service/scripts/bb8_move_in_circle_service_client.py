#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty

rospy.init_node('bb8_move_in_circle_service_client')
rospy.wait_for_service('/move_bb8_in_circle')

try:
    move_circle = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
    resp = move_circle()
    rospy.loginfo("Service call successful, BB8 is moving in a circle!")
except rospy.ServiceException as e:
    rospy.logerr("Service call failed: %s", e)
