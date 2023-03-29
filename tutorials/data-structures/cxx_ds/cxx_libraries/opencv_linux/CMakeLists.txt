cmake_minimum_required(VERSION 3.0)

project(OpenCVTest)

set(CMAKE_CXX_STANDARD 17)

# Find the OpenCV libraries
find_package(OpenCV REQUIRED)

# Add the OpenCVTest executable
add_executable(OpenCVTest main.cxx)

# Link against the OpenCV libraries
target_link_libraries(OpenCVTest ${OpenCV_LIBS})

