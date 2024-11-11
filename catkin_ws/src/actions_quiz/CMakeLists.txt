cmake_minimum_required(VERSION 3.0.2)
project(actions_quiz)

# Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  roscpp
  std_msgs
  message_generation  # Add this line for message generation
)

# Generate actions
add_action_files(
  DIRECTORY action
  FILES CustomActionMsg.action
)

# Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES actionlib_msgs std_msgs)

# Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)