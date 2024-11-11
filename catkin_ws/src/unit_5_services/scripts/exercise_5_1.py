#!/usr/bin/env python

import rospy
from iri_wam_reproduce_trajectory.srv import ExecuteTrajectory, ExecuteTrajectoryRequest
import rospkg

# Initialize a ROS node
rospy.init_node('execute_trajectory_client')

# Wait for the service to be available
rospy.wait_for_service('/execute_trajectory')

# Create a service proxy
execute_trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecuteTrajectory)

# Get the path to the trajectory file
rospack = rospkg.RosPack()
traj_file = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

# Create a request object and set the trajectory file
traj_request = ExecuteTrajectoryRequest()
traj_request.trajectory = traj_file  # Assuming the service expects a string path to the trajectory

# Call the service
result = execute_trajectory_service(traj_request)

# Print the result
print(result)
