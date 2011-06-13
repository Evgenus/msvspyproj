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

Why?
----

It is usefull when:

 - you are using MSVS of course;
 - you are using some version control system and files could be added/removed from your project externally;
 - you making MSVS project for existing bunch of files and there are A LOT of them;
 - it is easy for you to manage files not by VS but some file-manager;
 - you can't put project file directly into repository.

Getting started
---------------

**1. Make project.** Usually it is empty project. 

**2. Create a config.** It is better to call it `proj.conf`. Each line of config file could be:

 - empty line;
 - include rule; [plus][one or more spaces][wildcart]
 - exclude rule; [minus][one or more spaces][wildcart]
 - comment. [sharp][anything]

The example could be found right here in this project. Last time I saw it, it looks like that:

    # compiled files
    - *.pyc

    # build files used by setup.py
    - .\build\*

    # source files
    + *.py

    # this config
    + .\proj.conf

    # github readme files
    + .\README.*

    # license files
    + .\LICENSE.txt
    + .\COPYING.LESSER

**3. Running.** If you installed `msvspyproj` then you have a script with same name. Run it and follow instructions.
Or you can do as I like to do. I'm using Visual Studio Run Button to run tests and playground.
And production entry point for me is something to be run in separate console or to be constantly running. 
Like web site with auto reloading. So main file of my project countains of some tests running procedure,
some trials and other stuff. I put something like that to that stuff.

    import msvspyproj
    #...
    if __name__ == '__main__':
        #...
        msvspyproj.magick() 

After every launch of tests my project is about to be checked and updated.

Dependencies
------------

 - [lxml](http://lxml.de/) for processing VS project files