# msvspyproj - MS Visual Studio Python Project Helper
# Copyright (c) 2011, Eugene Chernyshov
# Licensed under the LGPL.

#standart
import os.path
#external
from lxml import etree

class PyProject(object):
    namespaces = {'ns': 'http://schemas.microsoft.com/developer/msbuild/2003'}
    rule_projecthome = etree.XPath(
        '/ns:Project/ns:PropertyGroup/ns:ProjectHome', namespaces=namespaces)
    rule_sources = etree.XPath(
        '/ns:Project/ns:ItemGroup/ns:Compile', namespaces=namespaces)
    rule_content = etree.XPath(
        '/ns:Project/ns:ItemGroup/ns:Content', namespaces=namespaces)
    rule_folders = etree.XPath(
        '/ns:Project/ns:ItemGroup', namespaces=namespaces)
    source_ext = {'.py'}
    def __init__(self, filename):
        self.filename = filename
        self.parser = etree.XMLParser(
            remove_blank_text=True,
            ns_clean=True,
            )
        self.tree = etree.parse(filename, self.parser)
        project_dir = os.path.dirname(filename)
        project_home = self.rule_projecthome(self.tree)[0].text
        self.projecthome = os.path.join(project_dir, project_home)
        self.sources = set()
        for file in self.rule_sources(self.tree):
            path = os.path.join(self.projecthome, file.get('Include'))
            self.sources.add(path)
        for file in self.rule_content(self.tree):
            path = os.path.join(self.projecthome, file.get('Include'))
            self.sources.add(path)
        self.toadd = set()
        self.toremove = set()
    def filter(self, matcher):
        for file in self.sources:
            if not matcher(file) or not os.path.exists(file):
                self.toremove.add(file)
                self.toadd.discard(file)
    def add(self, file):
        if file not in self.sources:
            self.toremove.discard(file)
            self.toadd.add(file)
    def apply(self):
        self.sources |= self.toadd
        self.sources -= self.toremove
        for container in self.rule_folders(self.tree):
            container.getparent().remove(container)
        compile = etree.SubElement(self.tree.getroot(), 'ItemGroup')
        for file in sorted(self.sources):
            name, ext = os.path.splitext(file)
            if ext in self.source_ext:
                path = os.path.relpath(file, self.projecthome)
                etree.SubElement(compile, 'Compile', Include=path)
        content = etree.SubElement(self.tree.getroot(), 'ItemGroup')
        for file in sorted(self.sources):
            name, ext = os.path.splitext(file)
            if ext not in self.source_ext:
                path = os.path.relpath(file, self.projecthome)
                etree.SubElement(content, 'Content', Include=path)
        folders = etree.SubElement(self.tree.getroot(), 'ItemGroup')
        paths = set()
        for file in sorted(self.sources):
            path = os.path.relpath(file, self.projecthome)
            path = os.path.dirname(path)
            while path and path not in paths:
                paths.add(path)
                etree.SubElement(folders, 'Folder', Include=path)
                path = os.path.dirname(path)
        self.tree.write(self.filename, 
            encoding='UTF-8', 
            xml_declaration=True, 
            pretty_print=True)
    def __bool__(self):
        return True
        return bool(self.toremove) or bool(self.toadd)
    __nonzero__ = __bool__
