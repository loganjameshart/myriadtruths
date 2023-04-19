# Myriad Truths
## Creates a pseudo-shell on a host machine for viewing file directories and transferring files.

This project was created to explore ethical hacking through Python.

This program creates an open socket connection on port 6666 of the host machine and, once connected to, will provide the user with a menu of commands to execute
on the host machine. 

Currently, there is a "system" command which displays the host machine's system type. This is used to understand which directory conventions to use when looking into the
host machine's file system (C:\\ for Windows vs. /usr/bin for *nix machines). This requires knowledge of file directory conventions on part of the client connecting to the host machine,
but my intention is that future iterations of this project will handle this automatically.

There was initially a command line menu created through the argparse library, but I found it quicker to simply create my own commands executed
through a live session. Subsequent iterations will include command line arguments. 
