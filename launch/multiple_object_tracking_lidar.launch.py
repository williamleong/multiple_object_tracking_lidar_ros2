import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch

################### user configure parameters for ros2 start ###################
frame_id        = 'map'
# filtered_cloud  = '/point_cloud/full'
filtered_cloud  = '/point_cloud/downsample'
stateDim        = 4 # [x,y,v_x,v_y]//,w,h]
measDim         = 2 # [z_x,z_y,z_w,z_h]
ctrlDim         = 0
################### user configure parameters for ros2 end #####################

multiple_object_tracking_lidar_params = [
    {"frame_id": frame_id},
    {"filtered_cloud": filtered_cloud},
    {"stateDim": stateDim},
    {"measDim": measDim},
    {"ctrlDim": ctrlDim},
]

def generate_launch_description():
    multiple_object_tracking_lidar = Node(
        package='multiple_object_tracking_lidar',
        executable='multiple_object_tracking_lidar_node',
        name='multiple_object_tracking_lidar',
        parameters=multiple_object_tracking_lidar_params,
        output={
            'stdout': 'screen',
            'stderr': 'screen',
        },

        # https://gist.github.com/JADC362/a4425c2d05cdaadaaa71b697b674425f
        # https://juraph.com/miscellaneous/ros2_and_gdb/
        # prefix="gdbserver localhost:3000"
    )

    return LaunchDescription(
        [
            multiple_object_tracking_lidar
        ]
    )
