#!/usr/bin/env python

import rospy
import actionlib
from actionlib_tutorials.msg import FibonacciAction, FibonacciGoal

def fibonacci_client():
    # Create the action client
    client = actionlib.SimpleActionClient('fibonacci', FibonacciAction)

    # Wait for the action server to be available
    rospy.loginfo("Waiting for action server to start...")
    client.wait_for_server()

    # Create and send the goal
    goal = FibonacciGoal(order=5)  # Set the order of Fibonacci sequence
    rospy.loginfo("Sending Fibonacci goal: %d" % goal.order)
    client.send_goal(goal)

    # Wait for the result
    client.wait_for_result()

    # Get and display the result
    result = client.get_result()
    rospy.loginfo("Fibonacci result: %s" % result.sequence)

if __name__ == '__main__':
    try:
        rospy.init_node('fibonacci_action_client')
        fibonacci_client()
    except rospy.ROSInterruptException:
        pass
