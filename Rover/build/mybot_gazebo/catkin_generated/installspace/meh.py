#!/usr/bin/env python3
# Copyright (c) 2016 The UUV Simulator Authors.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function
import rospy
import sys
from gazebo_msgs.srv import ApplyBodyWrench
from geometry_msgs.msg import Point, Wrench, Vector3

if __name__ == '__main__':
    print('Apply programmed perturbation to vehicle', rospy.get_namespace())
    rospy.init_node('Control')

    duration = 2.0

    force = [0, 0, 0]

    print('Force [N]=', force)

    torque = [0, 1, 0]

    print('Torque [N]=', torque)

    try:
        rospy.wait_for_service('/gazebo/apply_body_wrench', timeout=10)
    except rospy.ROSException:
        print('Service not available! Closing node...')
        sys.exit(-1)

    try:
        apply_wrench = rospy.ServiceProxy('/gazebo/apply_body_wrench', ApplyBodyWrench)
    except rospy.ServiceException as e:
        print('Service call failed, error=', e)
        sys.exit(-1)

    wrench = Wrench()
    wrench.force = Vector3(*force)
    wrench.torque = Vector3(*torque)
    success = apply_wrench(
        'my_robot::left_front_wheel',
        'world',
        Point(0, 0, 0),
        wrench,
        rospy.Time().now(),
        rospy.Duration(duration))
    success = apply_wrench(
        'my_robot::left_back_wheel',
        'world',
        Point(0, 0, 0),
        wrench,
        rospy.Time().now(),
        rospy.Duration(duration))

    # torque = [0, -1, 0]
    wrench.torque = Vector3(*torque)
    success = apply_wrench(
        'my_robot::right_front_wheel',
        'world',
        Point(0, 0, 0),
        wrench,
        rospy.Time().now(),
        rospy.Duration(duration))  
    success = apply_wrench(
        'my_robot::right_back_wheel',
        'world',
        Point(0, 0, 0),
        wrench,
        rospy.Time().now(),
        rospy.Duration(duration))

    if success:
        print('Body wrench perturbation applied!')
        print('\tDuration [s]: ', duration)
        print('\tForce [N]: ', force)
        print('\tTorque [Nm]: ', torque)
    else:
        print('Failed!')
