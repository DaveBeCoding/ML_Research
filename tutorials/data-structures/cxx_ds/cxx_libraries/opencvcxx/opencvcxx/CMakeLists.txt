cmake_minimum_required(VERSION 3.5)

project(sharpen_image)

find_package(OpenCV REQUIRED)

set(CMAKE_CXX_STANDARD 11)

add_executable(${PROJECT_NAME} main.cxx)

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

set(EXECUTABLE_OUTPUT_PATH "${PROJECT_SOURCE_DIR}/..")

