cmake_minimum_required(VERSION 3.25)

set(CMAKE_CXX_COMPILER /usr/bin/x86_64-linux-gnu-g++-14)
set(CMAKE_C_COMPILER /usr/bin/x86_64-linux-gnu-gcc-14)

project(dungeons_and_damage VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(
    dungeons_and_damage
    src/main2.cpp 
    src/glad.c
)

target_link_libraries(dungeons_and_damage glfw)