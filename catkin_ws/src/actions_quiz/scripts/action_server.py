#!/usr/bin/env python

import rospy
import actionlib
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback

class DroneActionServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('/action_custom_msg_as', CustomActionMsgAction, execute_cb=self.execute, auto_start=False)
        self.server.start()

    def execute(self, goal):
        feedback = CustomActionMsgFeedback()
        if goal.goal == "TAKEOFF":
            # Simulate taking off
            rospy.loginfo("Taking off...")
            feedback.feedback = "Taking off"
            self.server.publish_feedback(feedback)
            rospy.sleep(5)  # Simulate some action duration
            self.server.set_succeeded()
        elif goal.goal == "LAND":
            # Simulate landing
            rospy.loginfo("Landing...")
            feedback.feedback = "Landing"
            self.server.publish_feedback(feedback)
            rospy.sleep(5)  # Simulate some action duration
            self.server.set_succeeded()
        else:
            self.server.set_aborted()

if __name__ == "__main__":
    rospy.init_node('drone_action_server')
    server = DroneActionServer()
    rospy.spin()
