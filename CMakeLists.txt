cmake_minimum_required(VERSION 3.16)

set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Release>:Release")

project(
    themain
    VERSION 1.0
    DESCRIPTION "A place for me to learn how to use vulkan"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 17)

find_package(Vulkan REQUIRED)
find_package(glfw3 3.3 REQUIRED)

add_subdirectory(external/glm)

file(GLOB_RECURSE MY_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")

add_executable(
    themain
    "${MY_SOURCES}"
)

#target_compile_definitions("${CMAKE_PROJECT_NAME}" PUBLIC RESOURCES_PATH="${CMAKE_CURRENT_SOURCE_DIR}/resources/") # Development Line
target_compile_definitions("${CMAKE_PROJECT_NAME}" PUBLIC RESOURCES_PATH="./resources/") # Release line

file(GLOB MY_INCLUDE_DIRS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/include/*/")

target_include_directories(
    themain
    PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}/src/include"
    ${MY_INCLUDE_DIRS}
)

target_link_libraries(
    themain
    PRIVATE glfw
    PRIVATE Vulkan::Vulkan
    PRIVATE glm::glm-header-only
)