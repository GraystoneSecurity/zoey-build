#!/usr/bin/python
import os
import shutil
import stat
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Zoey Graystone",
    version = "0.0.1",
    author = "Daniel Graystone",
    author_email = "dgraystone@graystonesec.net",
    description = ("An interactive A.I."
                                   ),
    license = "M.I.T.",
    keywords = "Zoey Graystone A.I.",
    url = "http://graystonesec.com/project_zoey",
    packages=['Zoey Graystone', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7"
    ],
)


## GitPython (https://github.com/gitpython-developers/GitPython)
sudo mkdir /opt/zoey/modules/GitPython
# install process needs work after this, can't authenticate to GitHub to pull. Pubkey error
#git clone git@github.com:gitpython-developers/GitPython.git
#git submodule update --init --recursive
#cd /opt/zoey/modules/GitPython
#sudo python setup.py install

## NLTK 
# Natural Language Toolkit (https://github.com/nltk/nltk)
sudo mkdir /opt/zoey/modules/NLTK
# install process needs work after this, can't authenticate to GitHub to pull. Pubkey error
#git clone git@github.com:nltk/nltk.git
#git submodule update --init --recursivecd 
#cd /opt/zoey/modules/NLTK
#sudo python setup.py install

## python-ts3
# Python TS3 Module (https://github.com/nikdoof/python-ts3)
sudo mkdir /opt/zoey/modules/python-ts3
# install process needs work after this, can't authenticate to GitHub to pull. Pubkey error
#git git@github.com:nikdoof/python-ts3.git
#git submodule update --init --recursive
#cd /opt/zoey/modules/python-ts3
#sudo python setup.py install