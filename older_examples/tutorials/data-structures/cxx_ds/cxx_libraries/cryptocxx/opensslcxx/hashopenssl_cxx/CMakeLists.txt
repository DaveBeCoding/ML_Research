cmake_minimum_required(VERSION 3.0)

project(OPENSSL_CXX)

set(OPENSSL_ROOT_DIR "/opt/homebrew/opt/openssl@3")

message(STATUS "PATH LOCATION --- " ${OPENSSL_ROOT_DIR})

find_package(OpenSSL REQUIRED)

add_executable(${PROJECT_NAME}.exe main.cxx)

target_link_libraries(${PROJECT_NAME}.exe OpenSSL::SSL OpenSSL::Crypto)

