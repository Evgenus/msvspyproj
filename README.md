msvspyproj
==========

MS VisualStudio Python Project Helper

About
-----

Helps you to add and remove files from VisualStudio project automatically accordingly to list of rules.

License
-------

See `LICENSE` file.

> Copyright (c) 2011 Eugene Chernyshov

Getting started
---------------

**1. Make project.** Usually it is empty project. 

**2. Create a config.** It is better to call it `proj.conf`. Each line of config file could be:

 - empty line;
 - include rule; [plus][one or more spaces][wildcart]
 - exclude rule; [minus][one or more spaces][wildcart]
 - comment. [sharp][anything]