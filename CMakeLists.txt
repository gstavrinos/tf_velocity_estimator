cmake_minimum_required(VERSION 2.8.3)
project(tf_velocity_estimator)
find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    geometry_msgs
    message_generation
)

add_message_files(
    FILES
    PosesAndVelocities.msg
    Velocity.msg
)

generate_messages(
    DEPENDENCIES
    std_msgs
    geometry_msgs
)
catkin_package()
