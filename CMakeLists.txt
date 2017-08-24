cmake_minimum_required(VERSION 2.8.3)
project(tf_pose_estimator)
find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    message_generation
)

add_service_files(
    FILES
    EstimatorRequest.srv
)

generate_messages(
    DEPENDENCIES
    std_msgs
)
catkin_package()
