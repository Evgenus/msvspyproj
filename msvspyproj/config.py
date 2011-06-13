# msvspyproj - MS Visual Studio Python Project Helper
# Copyright (c) 2011, Eugene Chernyshov
# Licensed under the LGPL.

#standart
import re
from fnmatch import translate

class Config(object):
    rule = re.compile('^\s*([\+\-\#])\s+(.*)$')
    def __init__(self, filename):
        self.rules = []
        with open(filename) as stream:
            for lineno, line in enumerate(stream, start=1):
                if not line.strip():
                    continue
                mo = self.rule.match(line)
                if mo is not None:
                    kind, wildcard = mo.groups()
                    pattern = translate(wildcard)
                    rule = re.compile(pattern)
                    if kind == '+':
                        self.rules.append((True, rule, pattern))
                        continue
                    elif kind == '-':
                        self.rules.append((False, rule, pattern))
                        continue
                    elif kind == '#':
                        continue
                error = SyntaxError('Bad rule')
                error.filename = filename
                error.lineno = lineno
                error.offset = 1
                error.text = line
                raise error

    def __call__(self, path):
        for result, rule, pattern in self.rules:
            mo = rule.match(path)
            if mo is not None:
                return result
        return False

