cmake_minimum_required(VERSION 3.5)

project(SharkTest)

set(SHARK_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../Shark/build)
set(SHARK_HEADERS "/home/cpud/Documents/src/MACHINE_LEARNING/ML_Research/tutorials/data-structures/cxx_ds/cxx_libraries/shark_linux/Shark/include/shark")

message(STATUS 'SHARK PATH ---  ' ${SHARK_DIR})
message(STATUS 'SHARK HEADER PATH ---  ' ${SHARK_HEADERS})

# Find the Shark libraries
find_package(Shark REQUIRED PATHS ${SHARK_DIR})
find_package(Boost REQUIRED COMPONENTS serialization system filesystem)
#include_directories(${SHARK_HEADERS})
#find_package(Shark REQUIRED PATHS ${SHARK_HEADERS} COMPONENTS Dataset)
include_directories(../Shark/include/)

#include_directories(/home/cpud/Documents/src/MACHINE_LEARNING/ML_Research/tutorials/data-structures/cxx_ds/cxx_libraries/shark_linux/Shark/include/shark)

# Add the SharkTest executable
add_executable(SharkTest main.cxx)

# Link against the Shark libraries
target_link_libraries(SharkTest ${SHARK_LIBRARIES})

