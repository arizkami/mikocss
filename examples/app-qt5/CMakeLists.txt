# MikoCSS C++ Project
cmake_minimum_required(VERSION 3.10)
project(MikoCSSProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include MikoCSS headers
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# Find required packages based on framework
find_package(Qt5 REQUIRED COMPONENTS Core Widgets Gui)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Example executable
add_executable(example main.cpp)
target_link_libraries(example Qt5::Core Qt5::Widgets Qt5::Gui)
