cmake_minimum_required(VERSION 3.10.0)
project(dungeons_and_damage VERSION 0.1.0)

add_executable(
    dungeons_and_damage
    main.cpp
    include/classes.hpp
    include/Player.cpp
    include/Knight.cpp
    include/Peashooter.cpp
    include/Rouge.cpp
    include/Mage.cpp
    include/Skele.cpp
    include/Bard.cpp
    include/Barbarian.cpp
    include/Narrator.cpp
)