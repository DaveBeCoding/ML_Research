cmake_minimum_required(VERSION 3.0)
project(my_project)

# Find OpenCV installed via Homebrew
find_package(OpenCV REQUIRED PATHS /opt/homebrew/lib/cmake/opencv4)

# Add the executable target
add_executable(my_executable main.cxx)

# Link against OpenCV
target_link_libraries(my_executable ${OpenCV_LIBS})

