#!/usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage

def move_bb8():
    rospy.wait_for_service('/move_bb8_in_square_custom')
    try:
        move_bb8_square = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
        
        # Call the service for a small square
        response1 = move_bb8_square(1.0, 2)  # 1 sqm, 2 repetitions
        if response1.success:
            rospy.loginfo("Small square completed successfully.")
        else:
            rospy.logwarn("Small square did not complete.")

        # Call the service for a big square
        response2 = move_bb8_square(2.0, 1)  # 2 sqm, 1 repetition
        if response2.success:
            rospy.loginfo("Big square completed successfully.")
        else:
            rospy.logwarn("Big square did not complete.")

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == "__main__":
    rospy.init_node('bb8_move_custom_service_client')
    move_bb8()
