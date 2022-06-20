# motive_ros2_sandbox
ROS2 package for trying out vrpn_client_ros with ROS2(foxy).

## Installation
1. [Install vrpn](https://github.com/vrpn/vrpn/wiki/Installing-and-testing)

2. Install the dependent ROS2 package.
    ```sh
    cd ~/ros2_ws/src
    vcs import < motive_ros2_sandbox/.repos
    ```

## Usage
1. Properly connect windows for Motive and Linux for ROS2.

2. Select markers and generate a rigid body model in Motive with the name `test`.

3. launch
    ```sh
    ros2 launch motive_ros2_sandbox sample.launch.py
    ```

### rviz2
![](assets/sample_rviz.png)

### rqt_graph
![](assets/sample_rosgraph.png)

## References
- https://github.com/ros-drivers/vrpn_client_ros/issues/15
- https://github.com/ros-drivers/vrpn_client_ros/pull/16
- https://github.com/ros-drivers/vrpn_client_ros/pull/20
- https://github.com/toshi67026/vrpn_client_ros/tree/foxy_test \
Forked and modified for use with ros-foxy.
