import os
from glob import glob

from setuptools import setup

package_name = "motive_ros2_sandbox"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share/", package_name), glob("config/*.yaml")),
        (os.path.join("share/", package_name), glob("launch/*.launch.py")),
        (os.path.join("share/", package_name), glob("rviz/*.rviz")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Toshiyuki Oshima",
    maintainer_email="toshiyuki67026@gmail.com",
    description="Test package for using vrpn_client_ros with ros2",
    license="Apache License 2.0",
    entry_points={
        "console_scripts": [],
    },
)
