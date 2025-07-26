# MikoCSS C++ Project
cmake_minimum_required(VERSION 3.10)
project(MikoCSSProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include MikoCSS headers
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# Find required packages based on framework
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

include_directories(${GTK3_INCLUDE_DIRS})
link_directories(${GTK3_LIBRARY_DIRS})
add_definitions(${GTK3_CFLAGS_OTHER})

# Example executable
add_executable(example main.cpp)
target_link_libraries(example ${GTK3_LIBRARIES})
