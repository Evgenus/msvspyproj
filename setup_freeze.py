import sys
from cx_Freeze import Executable
from setup import params

params.update(
    executables=[
        Executable(script="exe.py", targetName=params['name']+'.exe',)
        ],
    )

options = params.setdefault("options", {})

options["build_exe"] = dict(
    includes=[
        'lxml._elementpath',
        'inspect',
        'gzip',
        ], 
    )

if __name__ == "__main__":
    from cx_Freeze import setup
    setup(**params)
