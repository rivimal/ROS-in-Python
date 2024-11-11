#!/usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

def move_in_square(side, repetitions):
    # Example movement logic (replace with actual movement commands)
    for _ in range(repetitions):
        for _ in range(4):  # Move in 4 sides to complete a square
            # Move forward
            rospy.loginfo(f"Moving forward for {side} units")
            rospy.sleep(side)  # Simulate moving forward
            
            # Turn 90 degrees (replace with actual turn command)
            rospy.loginfo("Turning 90 degrees")
            rospy.sleep(1)  # Simulate turning

def handle_move_bb8_in_square(req):
    rospy.loginfo("Received request: side=%f, repetitions=%d", req.side, req.repetitions)
    move_in_square(req.side, req.repetitions)
    return BB8CustomServiceMessageResponse(success=True)

def bb8_move_custom_service_server():
    rospy.init_node('bb8_move_custom_service_server')
    s = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, handle_move_bb8_in_square)
    rospy.loginfo("Ready to move BB-8 in a square.")
    rospy.spin()

if __name__ == "__main__":
    bb8_move_custom_service_server()
