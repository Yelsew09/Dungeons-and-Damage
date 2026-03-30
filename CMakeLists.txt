cmake_minimum_required(VERSION 3.16)

project(
    vulkanLearning
    VERSION 1.0
    DESCRIPTION "A place for me to learn how to use vulkan"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 17)

find_package(Vulkan REQUIRED)
find_package(glfw3 3.3 REQUIRED)

add_subdirectory(external/glm)

add_executable(
    vulkanLearning
    src/main.cpp
    src/everything_else.cpp
)

target_link_libraries(
    vulkanLearning
    PRIVATE glfw
    PRIVATE Vulkan::Vulkan
    PRIVATE glm::glm-header-only
)