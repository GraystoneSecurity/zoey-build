#!/bin/bash
# Base Installation Scripts
cd /
sudo mkdir /opt/zoey
sudo mkdir /opt/zoey/modules
sudo yum clean all
sudo yum update -y

echo Assumes python 2.7.6 already installed. Checking python version
if which python > /dev/null 2>&1;
then
    #Python is installed
    python_version=`python --version 2>&1 | awk '{print $2}'`
    echo "Python version $python_version is installed."

else
    #Python is not installed
    echo "No Python executable is found. Installing now"
    sudo yum groupinstall -y 'development tools'
    sudo yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs
    wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
    xz -d Python-2.7.6.tar.xz
    cd Python-2.7.6
    ./configure --prefix=/usr/local
    sudo make && make installall
    sudo export PATH="/usr/local/bin:$PATH"
    cd /
fi
sudo yum install python-pip

## GitPython (https://github.com/gitpython-developers/GitPython)
sudo mkdir /opt/zoey/modules/GitPython
git clone git@github.com:gitpython-developers/GitPython.git
git submodule update --init --recursive
cd /opt/zoey/modules/GitPython
sudo python setup.py install

## NLTK 
# Natural Language Toolkit (https://github.com/nltk/nltk)
sudo mkdir /opt/zoey/modules/NLTK
git clone git@github.com:nltk/nltk.git
git submodule update --init --recursive
cd /opt/zoey/modules/NLTK
sudo python setup.py install

