cmake_minimum_required(VERSION 3.10.0)
project(dungeons_and_damage VERSION 0.1.0)

add_executable(dungeons_and_damage src/main.cpp)

target_link_libraries(dungeons_and_damage glfw)