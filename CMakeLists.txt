cmake_minimum_required(VERSION 3.16)
project(vulkanLearning)

set(CMAKE_CXX_STANDARD 17)
find_package(Vulkan REQUIRED)
include_directories(${Vulkan_INCLUDE_DIRS})

add_subdirectory(glm)
SET(GLM_TEST_ENABLE OFF CACHE BOOL "GLM Build unit tests")

add_executable(vulkanLearning main.cpp)

target_link_libraries(vulkanLearning PRIVATE Vulkan::Vulkan)