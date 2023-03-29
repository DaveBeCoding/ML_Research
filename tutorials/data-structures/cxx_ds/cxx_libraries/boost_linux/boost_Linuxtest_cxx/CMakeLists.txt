cmake_minimum_required(VERSION 3.0)

project(BoostTest)

# Find the Boost libraries
find_package(Boost REQUIRED COMPONENTS system)

# Add the BoostTest executable
add_executable(BoostTest main.cxx)

# Link against the Boost libraries
target_link_libraries(BoostTest Boost::system)

