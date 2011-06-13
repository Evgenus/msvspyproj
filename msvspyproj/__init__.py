# msvspyproj - MS Visual Studio Python Project Helper
# Copyright (c) 2011, Eugene Chernyshov
# Licensed under the LGPL.

#standart
import os
import os.path
import glob
#internal
from .config import Config
from .project import PyProject

try:
    raw_input
except:
    raw_input = input

__all__ = ['Config', 'PyProject', 'magick']

def resolve_names(proj_file=None, conf_file=None):
    if proj_file is None:
        projects = glob.glob('*.pyproj')
        if len(projects) == 1:
            proj_file = projects[0]
            project_dir = os.path.dirname(proj_file)
        else:
            project_dir = os.getcwd()

    if conf_file is None:
        conf_file = os.path.join(project_dir, 'proj.conf')
        if not os.path.exists(conf_file):
            raise RuntimeError("Can't find `proj.conf` file in %s"%project_dir)

    return proj_file, conf_file

def find_files(proj_file=None, conf_file=None):
    proj_file, conf_file = resolve_names(conf_file=conf_file)
    print('Automatic MSVS project [%s] nanny found files:' % proj_file)
    config = Config(conf_file)
    project = PyProject(proj_file)
    for root, dirs, files in os.walk(project.projecthome):
        for file in files:
            filename = os.path.join(root, file)
            if config(filename):
                print('\t%s' % filename)    

def magick(proj_file=None, conf_file=None, verbose=True, ask=True):
    proj_file, conf_file = resolve_names(conf_file=conf_file)
    config = Config(conf_file)
    project = PyProject(proj_file)
    project.filter(config)
    for root, dirs, files in os.walk(project.projecthome):
        for file in files:
            filename = os.path.join(root, file)
            if config(filename):
                project.add(filename)

    if project:
        if verbose:
            print('Automatic MSVS project [%s] nanny reporting.' % proj_file)
            if project.toadd:
                print('I want to add:\n\t%s'%'\n\t'.join(project.toadd))

            if project.toremove:
                print('I want to remove:\n\t%s'%'\n\t'.join(project.toremove))

            if ask:
                while True:
                    result = raw_input('Apply chages to %s (y/n)? '%proj_file)
                    result = result.strip()
                    if result in ('yes', 'y'):
                        project.apply()
                        break
                    elif result in ('no', 'n'):
                        break
            else:
                project.apply()
        else:
            project.apply()

def make_parser():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', type=str, default=None, dest='proj',
        help='Path to MSVS python project file (*.pyproj). ')
    parser.add_argument('--input', '-i', type=str, default=None, dest='conf',
        help='Path to input config file (proj.conf). ')
    parser.add_argument('--quiet', '-q', default=False, 
        dest='quiet', action='store_true',
        help='Quite mode.')
    parser.add_argument('--apply', '-a', default=False, 
        dest='apply', action='store_true',
        help='Apply changes immediately without confirmation.')
    parser.add_argument('--show', '-s', default=False, 
        dest='show', action='store_true',
        help='Show found files')
    return parser

def main():
    options = make_parser().parse_args()
    if options.show:
        find_files(options.proj, options.conf)
    else:
        magick(options.proj,options.conf,not options.quiet,not options.apply)
