cmake_minimum_required(VERSION 3.25)

project(dungeons_and_damage VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(
    dungeons_and_damage
    main.cpp
    include/commands.cpp
    include/Player.cpp
)