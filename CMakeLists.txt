cmake_minimum_required(VERSION 3.10.0)
project(dungeons_and_damage VERSION 0.1.0)

add_executable(
    dungeons_and_damage
    src/main.cpp
    src/glad.h
    src/glad.c
)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

target_link_libraries(dungeons_and_damage glfw)