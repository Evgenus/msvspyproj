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

if __name__ == "__main__":
    from setuptools import setup
    setup(**params)