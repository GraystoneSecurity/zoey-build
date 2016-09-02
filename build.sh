#!/bin/bash
# Base Installation Scripts ensure OS is ready for python and application working directories. Install is then turned over to setup.py
cd /
sudo mkdir /opt/zoey_graystone
touch /opt/zoey_graystone/__init__.py
sudo mkdir /opt/zoey_graystone/modules
touch /opt/zoey_graystone/modules/__init__.py

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
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
echo "Python Setup is complete. Starting main Zoey install"

echo "Moving base code in place into /opt/zoey_graystone"
sudo mv setup.py /opt/zoey_graystone

echo "WARNING: CONTINUING WILL INSTALL THE ZOEY GRAYSTONE A.I.
AND OVERWRITE ANY EXISTING FILES IN THE MAIN DIRECTORY"

read -r -p "Install Zoey Graystone A.I.? [y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
    sudo python /opt/zoey_graystone/setup.py
else
    echo "Install Aborted"
fi


