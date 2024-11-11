#!/usr/bin/env python
import rospy
from bb8_circle_service.srv import BB8MoveCircleCustom

def call_bb8_circle_service(duration):
    rospy.wait_for_service('/move_bb8_in_circle_custom')
    try:
        move_circle = rospy.ServiceProxy('/move_bb8_in_circle_custom', BB8MoveCircleCustom)
        resp = move_circle(duration)
        rospy.loginfo("Success: %s", resp.success)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == "__main__":
    rospy.init_node('bb8_move_custom_service_client')
    duration = 5  # Set duration for how long BB8 moves in circles
    call_bb8_circle_service(duration)
