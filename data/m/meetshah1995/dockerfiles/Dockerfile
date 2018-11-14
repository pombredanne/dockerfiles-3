FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu14.04  
  
MAINTAINER Meet P Shah <meetshah1995@gmail.com>  
RUN rm -rf /var/lib/apt/lists/* \  
/etc/apt/sources.list.d/cuda.list \  
/etc/apt/sources.list.d/nvidia-ml.list  
  
RUN apt-get update  
  
RUN apt-get install -y \--no-install-recommends apt-utils build-essential sudo
git  
  
# tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
ca-certificates cmake libjpeg-dev wget git vim software-properties-common
libsm6 libxext6 libgtk2.0-dev  
  
# python  
RUN add-apt-repository ppa:fkrull/deadsnakes && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--force-yes \--no-install-
recommends \  
python2.7 \  
python2.7-dev  
  
# python packages  
RUN wget -O ~/get-pip.py \  
https://bootstrap.pypa.io/get-pip.py && \  
python2.7 ~/get-pip.py && \  
ln -s /usr/bin/python2.7 /usr/local/bin/python && \  
pip \--no-cache-dir install \--upgrade setuptools && \  
pip \--no-cache-dir install \--upgrade numpy scipy pandas scikit-learn
matplotlib Cython opencv-python cffi easydict pyyaml  
  
# pytorch  
RUN pip \--no-cache-dir install \--upgrade
http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp27-cp27mu-
manylinux1_x86_64.whl torchvision  
  
# config & cleanup  
RUN ldconfig && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* ~/*  
  
# Expose ports  
# 6006 for tensorbard,  
# 443 for visdom  
# 8888 for jupyter notebooks  
EXPOSE 443 6006 8888  
  
CMD ["/bin/bash"]  

