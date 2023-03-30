cmake_minimum_required(VERSION 3.5)

project(SharkTest)

set(SHARK_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../Shark/build)

# Find the Shark libraries
find_package(Shark REQUIRED PATHS ${SHARK_DIR})
find_package(Boost REQUIRED COMPONENTS serialization system filesystem)
include_directories(../Shark/build/include)

# Add the SharkTest executable
add_executable(SharkTest main.cxx)

# Link against the Shark libraries
target_link_libraries(SharkTest ${SHARK_LIBRARIES})

