import os
from setuptools import setup, find_packages

version = '0.2.0.0'

description = "Just alittle tinkering with Python, all code is released on GPLv3 licencing terms."
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.md')).read()
except:
    long_description = description

setup(
    name = "My-New-Python-Project",
    version = version,
    url = 'http://github.com/maxm11/My-New-Python-Project/',
    license = 'BSD',
    description = description,
    long_description = long_description,
    author = 'Max Murphy',
    author_email = 'maxmrphy@gmail.com',
    packages = find_packages(''),
    package_dir = {''},
    install_requires = [''],
    entry_points=""
    [console_scripts]
    ghi = github.issues:main
    "",
    classifiers=[
        'Development Status :: 1 - Prototype',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Sexy People',
        'Intended Audience :: Really Sexy People',
        'License :: GPLv3 License',
        'Operating System MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    test_suite = 'nose.collector',
)