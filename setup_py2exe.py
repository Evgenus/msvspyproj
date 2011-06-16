import sys
import py2exe
from setup import params

params.update(
    console=[
        dict(
            script="exe.py",
            icon_resources=[],
            bitmap_resources=[],
            other_resources=[],
            dest_base=params['name'],
            version=params['version'],
            company_name=params['author'],
            copyright=params['author'],
            name=params['name'],
            ),
        ],
    options = {
        "py2exe": {
            "includes": ['lxml._elementpath', 'gzip'], 
            } 
        }
    )
        
if __name__ == "__main__":
    from distutils.core import setup
    setup(**params)

