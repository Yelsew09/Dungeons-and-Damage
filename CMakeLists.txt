cmake_minimum_required(VERSION 3.16)
project(vulkanLearning)

set(CMAKE_CXX_STANDARD 17)

find_package(Vulkan REQUIRED)
find_package(glfw3 3.3 REQUIRED)

add_subdirectory(glm)

add_executable(vulkanLearning main.cpp)

target_link_libraries(
    vulkanLearning
    PRIVATE glfw
    PRIVATE Vulkan::Vulkan
)