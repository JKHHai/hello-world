# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/justinhai/Desktop/SummerResearch2018/Testing

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/justinhai/Desktop/SummerResearch2018/Testing/build

# Include any dependencies generated for this target.
include CMakeFiles/hello.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/hello.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/hello.dir/flags.make

CMakeFiles/hello.dir/main.c.o: CMakeFiles/hello.dir/flags.make
CMakeFiles/hello.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/justinhai/Desktop/SummerResearch2018/Testing/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/hello.dir/main.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/hello.dir/main.c.o   -c /home/justinhai/Desktop/SummerResearch2018/Testing/main.c

CMakeFiles/hello.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/hello.dir/main.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/justinhai/Desktop/SummerResearch2018/Testing/main.c > CMakeFiles/hello.dir/main.c.i

CMakeFiles/hello.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/hello.dir/main.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/justinhai/Desktop/SummerResearch2018/Testing/main.c -o CMakeFiles/hello.dir/main.c.s

CMakeFiles/hello.dir/main.c.o.requires:

.PHONY : CMakeFiles/hello.dir/main.c.o.requires

CMakeFiles/hello.dir/main.c.o.provides: CMakeFiles/hello.dir/main.c.o.requires
	$(MAKE) -f CMakeFiles/hello.dir/build.make CMakeFiles/hello.dir/main.c.o.provides.build
.PHONY : CMakeFiles/hello.dir/main.c.o.provides

CMakeFiles/hello.dir/main.c.o.provides.build: CMakeFiles/hello.dir/main.c.o


CMakeFiles/hello.dir/test1.c.o: CMakeFiles/hello.dir/flags.make
CMakeFiles/hello.dir/test1.c.o: ../test1.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/justinhai/Desktop/SummerResearch2018/Testing/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/hello.dir/test1.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/hello.dir/test1.c.o   -c /home/justinhai/Desktop/SummerResearch2018/Testing/test1.c

CMakeFiles/hello.dir/test1.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/hello.dir/test1.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/justinhai/Desktop/SummerResearch2018/Testing/test1.c > CMakeFiles/hello.dir/test1.c.i

CMakeFiles/hello.dir/test1.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/hello.dir/test1.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/justinhai/Desktop/SummerResearch2018/Testing/test1.c -o CMakeFiles/hello.dir/test1.c.s

CMakeFiles/hello.dir/test1.c.o.requires:

.PHONY : CMakeFiles/hello.dir/test1.c.o.requires

CMakeFiles/hello.dir/test1.c.o.provides: CMakeFiles/hello.dir/test1.c.o.requires
	$(MAKE) -f CMakeFiles/hello.dir/build.make CMakeFiles/hello.dir/test1.c.o.provides.build
.PHONY : CMakeFiles/hello.dir/test1.c.o.provides

CMakeFiles/hello.dir/test1.c.o.provides.build: CMakeFiles/hello.dir/test1.c.o


# Object files for target hello
hello_OBJECTS = \
"CMakeFiles/hello.dir/main.c.o" \
"CMakeFiles/hello.dir/test1.c.o"

# External object files for target hello
hello_EXTERNAL_OBJECTS =

hello: CMakeFiles/hello.dir/main.c.o
hello: CMakeFiles/hello.dir/test1.c.o
hello: CMakeFiles/hello.dir/build.make
hello: CMakeFiles/hello.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/justinhai/Desktop/SummerResearch2018/Testing/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable hello"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/hello.dir/build: hello

.PHONY : CMakeFiles/hello.dir/build

CMakeFiles/hello.dir/requires: CMakeFiles/hello.dir/main.c.o.requires
CMakeFiles/hello.dir/requires: CMakeFiles/hello.dir/test1.c.o.requires

.PHONY : CMakeFiles/hello.dir/requires

CMakeFiles/hello.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/hello.dir/cmake_clean.cmake
.PHONY : CMakeFiles/hello.dir/clean

CMakeFiles/hello.dir/depend:
	cd /home/justinhai/Desktop/SummerResearch2018/Testing/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/justinhai/Desktop/SummerResearch2018/Testing /home/justinhai/Desktop/SummerResearch2018/Testing /home/justinhai/Desktop/SummerResearch2018/Testing/build /home/justinhai/Desktop/SummerResearch2018/Testing/build /home/justinhai/Desktop/SummerResearch2018/Testing/build/CMakeFiles/hello.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/hello.dir/depend
