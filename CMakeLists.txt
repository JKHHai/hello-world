cmake_minimum_required(VERSION 3.5)
project (Hello)

set(sources test1.c)
add_executable(hello main.c ${sources})

get_cmake_property( P VARIABLES )
	foreach( VAR in ${P} )
		message( STATUS " ${VAR} = ${${VAR}} " )
	endforeach()

