cmake_minimum_required(VERSION 3.0)
project(image_enhancer_OpenCV)

# Find OpenCV installed via Homebrew
find_package(OpenCV REQUIRED PATHS /opt/homebrew/lib/cmake/opencv4)

# Add the executable target
add_executable(${PROJECT_NAME}.exe main.cxx)

# Link against OpenCV
target_link_libraries(${PROJECT_NAME}.exe ${OpenCV_LIBS})

