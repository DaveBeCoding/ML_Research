cmake_minimum_required(VERSION 3.5)

project(SharkTest)

set(SHARK_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../Shark/build)
message(STATUS 'SHARK PATH ---  ' ${SHARK_DIR})

# Find the Shark libraries
find_package(Shark REQUIRED PATHS ${SHARK_DIR})
find_package(Boost REQUIRED COMPONENTS serialization system filesystem)
find_package(Shark REQUIRED COMPONENTS Dataset)
include_directories(${SHARK_DIR}/include)
#include_directories(../Shark/include/shark/Data/Dataset.h)

# Add the SharkTest executable
add_executable(SharkTest main.cxx)

# Link against the Shark libraries
target_link_libraries(SharkTest ${SHARK_LIBRARIES})

