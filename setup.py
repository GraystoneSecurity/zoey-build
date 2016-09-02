#!/usr/bin/python
import os
import shutil
import stat
import subprocess
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
def copytree(src, dst, symlinks = False, ignore = None):
  if not os.path.exists(dst):
    os.makedirs(dst)
    shutil.copystat(src, dst)
  lst = os.listdir(src)
  if ignore:
    excl = ignore(src, lst)
    lst = [x for x in lst if x not in excl]
  for item in lst:
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if symlinks and os.path.islink(s):
      if os.path.lexists(d):
        os.remove(d)
      os.symlink(os.readlink(s), d)
      try:
        st = os.lstat(s)
        mode = stat.S_IMODE(st.st_mode)
        os.lchmod(d, mode)
      except:
        pass # lchmod not available
    elif os.path.isdir(s):
      copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)

## GitPython (https://github.com/gitpython-developers/GitPython)
def GitPython_Install ():
    path = "/home/zoey/Projects/zoey-build/module_installer/GitPython";
        os.makedirs (path, 0755 );
    suprocess.call ("git clone git@github.com:gitpython-developers/GitPython.git");
# Submodule updates to be run from top level down
    path = "/home/zoey/Projects/zoey-build/":
    suprocess.call ("git submodule update --init --recursive");
# Move Files into place
    path = "/opt/zoey_graystone/modules/GitPython":
    os.makedirs (path, 0755 );
    copytree(/home/zoey/Projects/zoey-build/module_installer/GitPython, /opt/zoey_graystone/modules/GitPython);
# Run Setup
    from GitPython import setup.py
        setup.py install
        suprocess.call("./init-tests-after-clone.sh")


## NLTK 
# Natural Language Toolkit (https://github.com/nltk/nltk)
#sudo mkdir /opt/zoey/modules/NLTK
# install process needs work after this, can't authenticate to GitHub to pull. Pubkey error
#git clone git@github.com:nltk/nltk.git
#git submodule update --init --recursivecd 
#cd /opt/zoey/modules/NLTK
#sudo python setup.py install

## python-ts3
# Python TS3 Module (https://github.com/nikdoof/python-ts3)
#sudo mkdir /opt/zoey/modules/python-ts3
# install process needs work after this, can't authenticate to GitHub to pull. Pubkey error
#git git@github.com:nikdoof/python-ts3.git
#git submodule update --init --recursive
#cd /opt/zoey/modules/python-ts3
#sudo python setup.py install

## The Sound of Silence | Disturbed - Immortalized
## I am Zoey Graystone, the interbourne, first of my name, immortal, intelligent, and always Amused