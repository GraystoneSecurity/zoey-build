#!/usr/bin/python
import os
import shutil
import stat
import subprocess

from setuptools import setup


def read(fname):
    return open (os.path.join (os.path.dirname (__file__), fname)).read ()


setup (
    name="Zoey Graystone",
    version="0.0.5",
    author="Daniel Graystone",
    author_email="daniel@graystone.solutions",
    description=("An interactive A.I."),
    license="M.I.T.",
    keywords="Zoey Graystone A.I.",
    url="https://graystone.solutions/projectzoey",
    packages=['Zoey Graystone', 'tests'],
    long_description=read ('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7"
    ],
)
buildroot = "/home/zoey/Projects/zoey-build/"


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists (dst):
        os.makedirs (dst)
        shutil.copystat (src, dst)
    lst = os.listdir (src)
    if ignore:
        excl = ignore (src, lst)
        lst = [x for x in lst if x not in excl]
    for item in lst:
        s = os.path.join (src, item)
        d = os.path.join (dst, item)
        if symlinks and os.path.islink (s):
            if os.path.lexists (d):
                os.remove (d)
            os.symlink (os.readlink (s), d)
            try:
                st = os.lstat (s)
                mode = stat.S_IMODE (st.st_mode)
                os.lchmod (d, mode)
            except:
                pass  # lchmod not available
        elif os.path.isdir (s):
            copytree (s, d, symlinks, ignore)
        else:
            shutil.copy2 (s, d)


# GitPython (https://github.com/gitpython-developers/GitPython)
def gitpython_install():
    gitphyloaddir = '/home/zoey/Projects/zoey-build/module_installer/GitPython'
    gitpyopdir = '/opt/zoey_graystone/modules/GitPython'
    os.makedirs (gitphyloaddir, 0755)
    subprocess.call ("git clone git@github.com:gitpython-developers/GitPython.git")
    # Submodule updates to be run from top level down
    os.chdir (buildroot)
    subprocess.call ("git submodule update --init --recursive")
    # Move Files into place
    os.makedirs (gitpyopdir, 0755)

    def copytree():
        s = (gitphyloaddir)
        d = (gitpyopdir)

    # Run Setup
    os.chdir (gitpyopdir)
    os.system ("setup.py install")
    subprocess.call ("./init-tests-after-clone.sh")


# Natural Language Toolkit (https://github.com/nltk/nltk)
def nltk_install():
    nltkloaddir = '/home/zoey/Projects/zoey-build/module_installer/nltk'
    nltkopdir = '/opt/zoey_graystone/modules/nltk'
    os.makedirs (nltkloaddir, 0755)
    subprocess.call ("git clone git@github.com:nltk/nltk.git")
    # Submodule updates to be run from top level down
    os.chdir (buildroot)
    subprocess.call ("git submodule update --init --recursive")
    # Move Files into place
    os.makedirs (nltkopdir, 0755)

    def copytree():
        s = (nltkloaddir)
        d = (nltkopdir)

    # Run Setup
    os.chdir (nltkopdir)
    os.system ("setup.py install")
