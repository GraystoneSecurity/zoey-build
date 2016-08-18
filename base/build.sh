#!/bin/bash
# Base Installation Scripts ensure OS is ready for python and application working directories. Install is then turned over to setup.py
cd /
sudo mkdir /opt/zoey
sudo mkdir /opt/zoey/modules
sudo mkdir /opt/zoey/module_installer
sudo yum clean all
sudo yum update -y

echo Assumes python 2.7.5 or greater already installed. Checking python version
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
python setup.py

