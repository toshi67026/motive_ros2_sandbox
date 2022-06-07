#!/usr/bin/env python3

import os

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration


def generate_launch_description() -> LaunchDescription:
    pkg_dir = get_package_share_directory("motive_ros_foxy_sandbox")

    sample_params_path = os.path.join(pkg_dir, "sample.params.yaml")
    rviz_config_path = os.path.join(pkg_dir, "sample.rviz")

    vrpn_client_node = Node(
        package="vrpn_client_ros",
        executable="vrpn_client_node",
        output="screen",
        parameters=[sample_params_path],
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_path],
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(vrpn_client_node)
    ld.add_action(rviz2_node)

    return ld
