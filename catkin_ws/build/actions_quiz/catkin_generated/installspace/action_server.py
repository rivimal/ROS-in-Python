#!/usr/bin/env python3

import rospy
import actionlib
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback

class DroneActionServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('/action_custom_msg_as', CustomActionMsgAction, execute=self.execute, auto_start=False)
        self.server.start()
        rospy.loginfo("Action Server started")

    def execute(self, goal):
        feedback = CustomActionMsgFeedback()
        if goal.goal == "TAKEOFF":
            rospy.loginfo("Taking off...")
            feedback.feedback = "Taking off"
            self.server.publish_feedback(feedback)
            rospy.sleep(1)  # Simulate the drone taking off
            rospy.loginfo("Drone is airborne.")
        elif goal.goal == "LAND":
            rospy.loginfo("Landing...")
            feedback.feedback = "Landing"
            self.server.publish_feedback(feedback)
            rospy.sleep(1)  # Simulate the drone landing
            rospy.loginfo("Drone has landed.")
        self.server.set_succeeded()

if __name__ == '__main__':
    rospy.init_node('drone_action_server')
    server = DroneActionServer()
    rospy.spin()
