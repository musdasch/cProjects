# cProjects
Sublime Text 3 plugin to manage your c/c++ Projects.

## Important
This plugin is only tested on a linux platform yet. I would by happy to know if it runs on an other platform.

## Synopsis
This plugin expands the sublime text by a simple  C and C++ Integrated Development Environment.
Features include: support for project creation, customizable compiler command, include autocomplete, easy include and libry management.
More features are planned.

## Installation
Clone the repository in to the Sublime Text Packages folder.
```bash
cd [Packages folder]
git clone https://github.com/musdasch/cProjects.git
```

## Usage

### Crat Project
To create a project you can use either the short menu with the shortcut `ctrl + alt + m`  or the menu item `Project` > `CProject` > `New CProject`

After that you have to enter a project name and the project directory.

### Set Source File
To compile you have to set the source file which holds the main function. In order to set the source file you can either use the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set Source File`

After that you can choose which opened file should be used.

### Alter Object Files
In order to add, alter or remove Object Fildes from the compiler command you can use the short menu with the shortcut `ctrl + alt + m` or use the menu item `Project` > `CProject` > `Alter Object Files`

After that you can choose between the options `Add object file` or `Add from opened files`, if you have already set a object file you have the additional options `Alter object file` which allows you to allter the path to the object file and `Delete object file`

### Alter Includes
In order to have an easy access to your header files you can include a folder by default the headers folder is added. To add, alter or remove folders you can use the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Alter Includes`.

After that you can choose between `Add include`, `Alter include` or `Delete include`.

### Alter Libraries
If you want to include libraries in your project, you can use can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Alter Libraries`.

After that you can choose between `Add library`, `Alter library` or `Delete library`.

### Alter Library Paths
in order to have a easy access to foreign libraries you can set a path to the library folder. to add, alter or delete library path you can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Alter Library Paths`.

After that you can chosse between `Add library path`, `Alter library path` or `Delete library path`.

### Set Build Path
By default the build path is `[project path]/bin/builds` in order to change the path you can use the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set build path` and set an new directory to build in.

### Set Single Build Path
There is also the option to separately change the build path for the single build command. To change the build path for single source files you can use either the short menu with the shortcut `ctrl + alt + m` or  the menu item `Project` > `CProject` > `Set Single Build Path`.

### Set Compiler
By default the compiler is `g++` in order to set e new default compiler you can either use the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set compiler` and set a new one.

### Set Options
In order to specify compiler options such as `-Wall` you can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set options`.

### Set Single Options
You have also the the opportunity to change the options for the single file build command. In order to set new options you can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set Single Options`.

### Set Run Command
The default run command is set in such a way that the program is started in the `gnome-terminal`. If you doesn't use gnome you can change the run command by either using the short menu with the shortcat `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set run command`.

Default run command: `gnome-terminal  -- bash -c "${build_path}; read -n1"`

### Set Single Run Command
The run command for the build system witch builds the single source files is stored differently. In order to alter the run command for single builds you can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set Single Run Command`.

Default single run command: `gnome-terminal  -- bash -c "${single_build_path}; read -n1"`

### Build Variables
There are a few variables to make your build command dynamic. The Variables are:

CProject specefic:
  * ${compiler} - The compiler as set in the project setings, e. g., g++
  * ${build_path} - Output file, e. g., ./bin/builds/binary.
  * ${single_build_path} - Output file for single build.
  * ${run} - The run command as specified in the project setings.
  * ${single_run} - The run command for single builds. 
  * ${options} - The compiler options as specified in the project setings.
  * ${single_options} - The compiler options for single builds.
  * ${source_file} - The source file as specified in the project setings.
  * ${source_base_name} - The name only portion of the source_file as specified in the project setings.

Sublime Text standard:
  * ${file} - The full path to the current file, e. g., C:\Files\Chapter1.txt.
  * ${file_path} - The directory of the current file, e. g., C:\Files.
  * ${file_name} - The name portion of the current file, e. g., Chapter1.txt.
  * ${file_extension} - The extension portion of the current file, e. g., txt.
  * ${file_base_name} - The name only portion of the current file, e. g., Document.
  * ${packages} - The full path to the Packages folder.
  * ${project} - The full path to the current project file.
  * ${project_path} - The directory of the current project file.
  * ${project_name} - The name portion of the current project file.
  * ${project_extension} - The extension portion of the current project file.
  * ${project_base_name} - The name only portion of the current project file.


### Build
You have several options to build if you press the shortcut `ctrl + shift + b`. The options are:

  * `CProject` builds first and runs the chosen source file.
  * `CProject - Build` only builds the chosen source file.
  * `CProject - Run` only starts the previous build from the chosen source file.
  * `CProject - Single File` builds first and runs the opened source file.
  * `CProject - Single File - Build` only builds the opened source file.
  * `CProject - Single File - Run` only runs the opened source file.

If you press `ctrl + b` the previous comand will by repettet

## Features
The CProject is a minimal Development Enviroment. It provides :

### Creat Project
  * Creats a project folder for you.
  * Sets up the project.

### Compiler Command
  * Allows you to change the compiler command by alter the settings.
  * Custom build system testet with g++ compiler.

### Libry Management
  * Comfortable tool to add, alter or remove of includes libraries or paths in your project.

### Include Autocomplete
  * Autocomplete file names for #include "" directives.
  * List of standart directives.
  * Searches in your includes.
  * Searches in same directory as the file.

### Snippets
  * isn't fully implemented yet.

## Planned
  * Suport Clang auto complete

## Contact
You can leave bug reports, feature requests, or comments using the issues section.

## Thanks!
Thank you for your interest in this package!

## License
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE Version 2, December 2004

Copyright (C) 2017 Tim Vögtli musdasch@gmail.com

Everyone is permitted to copy and distribute verbatim or modified copies of this license document, and changing it is allowed as long as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
