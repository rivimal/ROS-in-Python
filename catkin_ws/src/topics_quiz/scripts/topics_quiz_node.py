#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class RobotController:
    def __init__(self):
        # Publisher to the /cmd_vel topic
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # Subscriber to the /kobuki/laser/scan topic
        self.laser_subscriber = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.laser_callback)
        self.rate = rospy.Rate(10)  # 10 Hz
        self.move_cmd = Twist()

    def laser_callback(self, data):
        front_distance = data.ranges[len(data.ranges) // 2]  # Front laser reading
        left_distance = data.ranges[0]  # Left laser reading
        right_distance = data.ranges[-1]  # Right laser reading

        # Logic for moving the robot
        if front_distance > 1.0:  # No obstacle in front
            self.move_cmd.linear.x = 0.5  # Move forward
            self.move_cmd.angular.z = 0.0
        elif right_distance < 1.0:  # Obstacle on the right
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = 0.5  # Turn left
        elif left_distance < 1.0:  # Obstacle on the left
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = -0.5  # Turn right
        else:
            self.move_cmd.linear.x = 0.0  # Stop
            self.move_cmd.angular.z = 0.0

        self.velocity_publisher.publish(self.move_cmd)

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('topics_quiz_node', anonymous=True)
    controller = RobotController()
    controller.run()
