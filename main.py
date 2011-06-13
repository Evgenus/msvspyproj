# This file is my playground

import msvspyproj
import winreg

# HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\10.0\PythonTools\Options\Interpreters.DefaultInterpreter
# HKEY_CURRENT_USER\Software\Microsoft\PythonTools

VisualStudio = r'Software\Microsoft\VisualStudio'
Interpreters = r'PythonTools\Options\Interpreters'

Studios = {
    '4.0': 'Visual Studio',
    '5.0': 'Visual Studio 97',
    '6.0': 'Visual Studio 6.0',
    '7.0': 'Visual Studio .NET (2002)',
    '7.1': 'Visual Studio .NET 2003',
    '8.0': 'Visual Studio 2005',
    '9.0': 'Visual Studio 2008',
    '10.0': 'Visual Studio 2010',
    }

if __name__ == '__main__':
    msvspyproj.magick()

    valid_versions = {}
    with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, VisualStudio) as studios:
        number = 0
        while True:
            try:
                key = winreg.EnumKey(studios, number)
                if key in Studios:
                    valid_versions[key] = Studios[key]
            except EnvironmentError:
                break
            number +=1
        print(valid_versions)
