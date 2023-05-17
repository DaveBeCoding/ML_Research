cmake_minimum_required(VERSION 3.5)
project(boost-linear-algebra)

set(BOOST_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../boost)

find_package(Boost REQUIRED COMPONENTS serialization system)

include_directories(${Boost_INCLUDE_DIRS} ${BOOST_DIR})

add_executable(${PROJECT_NAME} main.cxx)

target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES} ${BOOST_DIR}/stage/lib/libboost_serialization.a)

set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 11)
