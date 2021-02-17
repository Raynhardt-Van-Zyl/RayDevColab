#! /usr/bin/env python

from gazebo_msgs.srv import GetModelState
import rospy
from gazebo_msgs.srv import ApplyBodyWrench
from geometry_msgs.msg import Point, Wrench, Vector3

class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name

class Tutorial:


    def show_gazebo_models(self):
        try:
            # model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            # resp_coordinates = model_coordinates('my_robot','left_front_wheel')
            # print(resp_coordinates)

            apply_wrench = rospy.ServiceProxy('/gazebo/apply_body_wrench', ApplyBodyWrench)

            wrench = Wrench()
            wrench.force = Vector3(50,50,50)
            wrench.torque = Vector3(50,50,50)
            
            rate = rospy.Rate(100)

            success = apply_wrench(
                'my_robot',
                'world',
                Point(0, 0, 0),
                wrench,
                rospy.Time().now(),
                rospy.Duration(5))

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))


if __name__ == '__main__':
    rospy.init_node('Control')
    tuto = Tutorial()
    tuto.show_gazebo_models()