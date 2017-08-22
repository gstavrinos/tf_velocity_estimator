#!/usr/bin/env python
import tf
import rospy
from tf import TransformListener
from tf2_msgs.msg import TFMessage

tf_broadcaster = None
sliding_window = []
tf_ = None

def init():
    global tf_broadcaster, targeted_tf, tf_
    rospy.init_node('tf_pose_estimator')
    targeted_tf = rospy.get_param("~targeted_tf", "helipad")
    tf_broadcaster = tf.TransformBroadcaster()
    tf_ = TransformListener()
    rospy.Subscriber("tf", TFMessage, tf_callback)
    while not rospy.is_shutdown():
        rospy.spin()

def tf_callback(tf2):
    global tf_broadcaster, targeted_tf, tf_
    #if tf_.frameExists("odom") :#and tf_.frameExists(targeted_tf):
    try:
        t = tf_.getLatestCommonTime("/odom", targeted_tf)
        position, quaternion = tf_.lookupTransform("/odom", targeted_tf, t)
        print position
        if position not in sliding_window:
            # TODO create an object that includes position and time
            #sliding_window.push_back(position)
            pass
    except:
        pass
    '''
    for tf in tf2.transforms:
    if tf.child_frame_id == targeted_tf:
        tf_broadcaster.sendTransform(
            (width / 2 + top_left_x, -height / 2 + top_left_y, 0),
            (0, 0, 0, 1.0),
            rospy.Time.now(),
            'helipad',
            'ar_marker_' + master_marker)

        marker = Marker()
        marker.header.frame_id = 'ar_marker_' + master_marker
        marker.header.stamp = rospy.Time.now()
        marker.ns = 'ar_helipad'
        marker.id = 0
        # Based on http://docs.ros.org/api/visualization_msgs/html/msg/Marker.html
        # The shape code for the cube (rectangle) is 1
        # The add/modify action is 0
        marker.type = 1
        marker.action = 0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0
        marker.scale.x = width
        marker.scale.y = height
        marker.scale.z = 0.001
        marker.pose.position.x = width / 2 + top_left_x
        marker.pose.position.y = -height / 2 + top_left_y
        marker.pose.position.z = 0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 1.0
        marker.lifetime = rospy.Duration(1);
        marker_publisher.publish(marker)
    '''

if __name__ == '__main__':
    init() 