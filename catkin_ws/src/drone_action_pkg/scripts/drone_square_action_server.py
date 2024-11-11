#!/usr/bin/env python

import rospy
import actionlib
from actionlib_tutorials.msg import FibonacciAction, FibonacciFeedback, FibonacciResult

class FibonacciActionServer:
    def __init__(self):
        self._feedback = FibonacciFeedback()
        self._result = FibonacciResult()

        # Create an action server
        self._action_server = actionlib.SimpleActionServer('fibonacci', FibonacciAction, self.execute_callback, False)
        self._action_server.start()

    def execute_callback(self, goal):
        # Start with the initial Fibonacci sequence
        self._feedback.sequence = [0, 1]
        
        rospy.loginfo("Executing Fibonacci sequence up to order: %d" % goal.order)

        # Perform the Fibonacci sequence calculation
        for i in range(1, goal.order):
            if self._action_server.is_preempt_requested():
                rospy.loginfo("Preempted Fibonacci calculation")
                self._action_server.set_preempted()
                return

            next_number = self._feedback.sequence[i] + self._feedback.sequence[i - 1]
            self._feedback.sequence.append(next_number)

            # Publish feedback
            self._action_server.publish_feedback(self._feedback)
            rospy.sleep(1.0)  # Simulate computation time

        # Set the result to the final Fibonacci sequence
        self._result.sequence = self._feedback.sequence
        rospy.loginfo("Completed Fibonacci sequence: %s" % self._result.sequence)
        self._action_server.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('fibonacci_action_server')
    server = FibonacciActionServer()
    rospy.spin()
