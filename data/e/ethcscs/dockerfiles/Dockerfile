FROM ubuntu:14.04  
MAINTAINER Alberto Madonna <madonna@cscs.ch>  
  
LABEL com.pyfr.version="1.5.0"  
  
# Install system dependencies  
RUN apt-get update && apt-get install -y \  
unzip \  
wget \  
build-essential \  
gfortran-4.8 \  
libopenblas-dev \  
liblapack-dev \  
python3-dev \  
python3-pip \  
libhdf5-dev \  
libmpich-dev \  
libmetis-dev \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# Install gcc/g++ 4.9 (required for OpenMP 4.0)  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test && \  
apt-get update && apt-get install -y --no-install-recommends \  
gcc-4.9 \  
g++-4.9 && \  
rm -rf /var/lib/apt/lists/* && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 50 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 50  
  
# Install CUDA Toolkit 8.0  
ENV CUDA_VERSION 8.0  
LABEL com.nvidia.cuda.version="8.0"  
  
RUN wget -q -O -
http://developer.download.nvidia.com/compute/cuda/repos/GPGKEY | apt-key add -
&& \  
echo "deb
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64 /" >
/etc/apt/sources.list.d/cuda.list && \  
apt-get update --fix-missing  
  
ENV CUDA_PKG_VERSION 8-0=8.0.44-1  
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes \  
cuda-core-$CUDA_PKG_VERSION \  
cuda-misc-headers-$CUDA_PKG_VERSION \  
cuda-command-line-tools-$CUDA_PKG_VERSION \  
cuda-license-$CUDA_PKG_VERSION \  
cuda-cublas-dev-$CUDA_PKG_VERSION \  
cuda-curand-dev-$CUDA_PKG_VERSION \  
cuda-cudart-dev-$CUDA_PKG_VERSION \  
cuda-driver-dev-$CUDA_PKG_VERSION && \  
ln -s cuda-$CUDA_VERSION /usr/local/cuda && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "/usr/local/cuda/lib" >> /etc/ld.so.conf.d/cuda.conf && \  
echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# Create new user  
RUN useradd docker  
WORKDIR /home/docker  
  
# Install Python dependencies  
RUN pip3 install numpy>=1.8 \  
pytools>=2016.2.1 \  
mako>=1.0.0 \  
mpi4py>=2.0 && \  
pip3 install pycuda>=2015.1 \  
h5py>=2.6.0 && \  
wget -q -O GiMMiK-2.1.tar.gz
https://github.com/vincentlab/GiMMiK/archive/v2.1.tar.gz && \  
tar -xvzf GiMMiK-2.1.tar.gz && \  
cd GiMMiK-2.1 && \  
python3 setup.py install && \  
cd .. && \  
rm -rf GiMMiK-2.1.tar.gz GiMMiK-2.1  
  
# Set base directory for pyCUDA cache  
ENV XDG_CACHE_HOME /tmp  
  
# Install PyFR  
RUN wget -q -O PyFR-1.5.0.zip http://www.pyfr.org/download/PyFR-1.5.0.zip && \  
unzip -qq PyFR-1.5.0.zip && \  
cd PyFR-1.5.0 && \  
python3 setup.py install && \  
cd .. && \  
rm -rf PyFR-1.5.0.zip PyFR-1.5.0  
  
RUN apt-get update && apt-get install -y --no-install-recommends mpich && \  
rm -rf /var/lib/apt/lists/*  
  
#ENTRYPOINT ["pyfr"]  
CMD ["pyfr --help"]  

