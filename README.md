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
If you want to include libraries in your project, you can use can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project -> CProject -> Alter Libraries`.

After that you can choose between `Add library`, `Alter library` or `Delete library`.

### Alter Library Paths
in order to have a easy access to foreign libraries you can set a path to the library folder. to add, alter or delete library path you can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Alter Library Paths`.

After that you can chosse between `Add library path`, `Alter library path` or `Delete library path`.

### Set Build Path
By default the build path is `[project path]/bin/builds` in order to change the path you can use the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set build path` and set an new directory to build in.

### Set Compiler
By default the compiler is `g++` in order to set e new default compiler you can either use the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set compiler` and set a new one.

### Set Options
In order to specify compiler options such as `-Wall` you can use either the short menu with the shortcut `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set options`.

### Set Run Command
The default run command is set in such a way that the program is started in the `gnome-terminal`. If you doesn't use gnome you can change the run command by either using the short menu with the shortcat `ctrl + alt + m` or the menu item `Project` > `CProject` > `Set run command`.

Default run command: `gnome-terminal  -- bash -c "${build_path}; read -n1"`

### Build
You have several options to build if you press the shortcut `ctrl + shift + b`. The options are:

 * `CProject` only builds.
 * `CProject - Run` only starts the previous build.
 * `CProject - Build & Run` builds first and runs after that.

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
