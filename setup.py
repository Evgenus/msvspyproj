from setuptools import setup

params = dict(
    name='msvspyproj',
    version='0.1.0',
    description="Tools for MS Visual Studio project files manipulation",
    long_description="Observes files in current directory subtree accordingly to config files and tries to keep project file up to date",    
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
        ],
    keywords='msvs',
    author='Eugene Chernyshov',
    author_email='Chernyshov.Eugene@gmail.com',
    url='http://evgenus.github.com/msvspyproj/',
    license='LGPL',
    packages=['msvspyproj'],
    entry_points = {
        'console_scripts': ['msvspyproj = msvspyproj:main'],
        },
    )

try:
    import py2exe
except ImportError:
    pass
else:
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

setup(**params)

