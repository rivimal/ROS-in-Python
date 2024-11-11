#! /usr/bin/env python

import rospy
from new_publisher_example_package.msg import Age  # Import the custom Age message

def main():
    rospy.init_node('age_publisher', anonymous=True)
    age_publisher = rospy.Publisher('/robot_age', Age, queue_size=10)

    rate = rospy.Rate(1)  # Publish at 1 Hz
    age_value = 32  # Example age value

    while not rospy.is_shutdown():
        age_msg = Age()
        age_msg.age = age_value  # Set the age value

        rospy.loginfo("Publishing age: %d", age_value)
        age_publisher.publish(age_msg)

        rate.sleep()

if __name__ == '__main__':
    main()




'''
from nav_msgs.msg import Odometry 

def callback(data): 
    position_x = data.pose.pose.position.x
    position_y = data.pose.pose.position.y
    orientation_z = data.pose.pose.orientation.z

    print(f"Position: [x: {position_x}, y: {position_y}], Orientation: [z: {orientation_z}]")


def main():
    rospy.init_node('new_topic_subscriber', anonymous=True)
    rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
    '''