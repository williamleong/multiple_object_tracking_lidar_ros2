cmake_minimum_required(VERSION 3.5)
project(multiple_object_tracking_lidar)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(pcl_ros REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(
  include
  include/multiple_object_tracking_lidar
  ${cv_bridge_INCLUDE_DIRS}
  ${visualization_msgs_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_library(multiple_object_tracking_lidar SHARED
  src/multiple_object_tracking_lidar.cpp)
target_compile_definitions(multiple_object_tracking_lidar
  PRIVATE "COMPOSITION_BUILDING_DLL")

ament_target_dependencies(multiple_object_tracking_lidar
    "pcl_ros"
    "rclcpp"
    "sensor_msgs"
    "cv_bridge"
    "visualization_msgs"
    "OpenCV"
)

rclcpp_components_register_nodes(multiple_object_tracking_lidar "multiple_object_tracking_lidar::MultipleObjectTrackingLidar")
set(node_plugins "${node_plugins}multiple_object_tracking_lidar::MultipleObjectTrackingLidar;$<TARGET_FILE:multiple_object_tracking_lidar>\n")

add_executable(multiple_object_tracking_lidar_node
    src/multiple_object_tracking_lidar_node.cpp)
target_link_libraries(multiple_object_tracking_lidar_node
    multiple_object_tracking_lidar
    ${OpenCV_LIBS}
)

install(
  DIRECTORY include/
  DESTINATION include
)

install(TARGETS
    multiple_object_tracking_lidar
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION lib/${PACKAGE_NAME}
)

install(TARGETS
    multiple_object_tracking_lidar_node
    DESTINATION lib/${PROJECT_NAME}
)

# Install launch files.
install(DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()