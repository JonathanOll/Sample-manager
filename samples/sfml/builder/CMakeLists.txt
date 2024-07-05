cmake_minimum_required( VERSION 3.23 )
set(CMAKE_BUILD_TYPE Release)
project(Project_Name)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/../)

file(GLOB SRCS
    ".././sources/*.cpp"
    ".././headers/*.hpp"
    )

find_package(SFML COMPONENTS system window graphics REQUIRED)

include_directories(${SFML_INCLUDE_DIR})

add_executable(main ${SRCS})

target_include_directories(main PRIVATE ${CMAKE_SOURCE_DIR}/../headers)

target_link_libraries(main PRIVATE 
                      "sfml-system"
                      "sfml-main"
                      "sfml-window"
                      "sfml-graphics"
                      )
