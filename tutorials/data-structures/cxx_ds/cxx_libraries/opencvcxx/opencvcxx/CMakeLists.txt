cmake_minimum_required(VERSION 3.0)
project(opencv_builder)

#set(OpenCV_DIR /Users/<user-name>/<Path-to-Dir>/ML_RESEARCH/tutorials/data-structures/cxx_ds/cxx_libraries/opencvcxx/opencv/build) 

set(OpenCV_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../opencv/build)

# Set the OpenCV source directory
set(OPENCV_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../opencv)

# Set the OpenCV build directory
set(OPENCV_BINARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../opencv/build)

# Set the build type to Release by default
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Find OpenCV
find_package(OpenCV REQUIRED)

# Add the OpenCV source directory to the include paths
include_directories(${OPENCV_SOURCE_DIR}/include)

# Create a shared library target
add_library(opencv SHARED IMPORTED)

# Set the library properties
set_target_properties(opencv PROPERTIES
    IMPORTED_LOCATION ${OPENCV_BINARY_DIR}/lib/libopencv_world.so
    INTERFACE_INCLUDE_DIRECTORIES ${OPENCV_SOURCE_DIR}/include
)

# Add the main executable target
add_executable(sharpen_image main.cxx)

# Link against OpenCV
target_link_libraries(sharpen_image opencv ${OpenCV_LIBS})

