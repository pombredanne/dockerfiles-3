FROM debian:stretch  
MAINTAINER Michel El Habr <michel-haber@hotmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /app  
ADD . /app  
  
# Add backports and testing  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >>
/etc/apt/sources.list  
RUN echo "deb http://ftp.debian.org/debian testing main" >>
/etc/apt/sources.list  
ADD testing.pref /etc/apt/preferences.d/  
  
# Install packages  
RUN apt-get -qq update  
RUN apt-get -y dist-upgrade  
RUN apt-get --no-install-recommends -y install \  
build-essential ca-certificates clang clang-format cmake curl git g++ python \  
gcc-arm-none-eabi binutils-arm-none-eabi gdb-arm-none-eabi \  
libstdc++-arm-none-eabi-newlib libgl1-mesa-glx libglib2.0-0 \  
libnewlib-arm-none-eabi ccache autoconf automake virtualenv \  
unzip libpq-dev python3-dev sudo \  
python3-pip  
  
RUN pip3 install -U pip setuptools  
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt  
  
# Build Criterion  
RUN (cd /tmp && git clone https://github.com/Snaipe/Criterion && \  
cd Criterion && git submodule update --init && mkdir build && cd build && \  
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && make && make install && \  
cd /tmp && rm -rf Criterion)  

