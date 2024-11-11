#!/usr/bin/env python

import rospy
from iri_wam_reproduce_trajectory.srv import ExecuteTrajectory  # Use the correct service name
import rospkg

def main():
    rospy.init_node('exercise_5_1')

    # Get the trajectory file path
    rospack = rospkg.RosPack()
    traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

    # Wait for the execute_trajectory service
    rospy.wait_for_service('/execute_trajectory')
    try:
        execute_trajectory = rospy.ServiceProxy('/execute_trajectory', ExecuteTrajectory)
        
        # Prepare the data to send (adjust based on your service definition)
        with open(traj, 'r') as file:
            trajectory_data = file.read()  # Ensure this matches the service's expected input

        # Call the service
        response = execute_trajectory(trajectory_data)  # Adjust parameters as needed
        rospy.loginfo(response)

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == '__main__':
    main()
