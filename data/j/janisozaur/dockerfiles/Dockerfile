FROM ubuntu:16.04  
RUN dpkg --add-architecture i386  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN apt-get update  
RUN apt-get install -y libcurl4-openssl-dev:i386 libcrypto++-dev:i386
libfontconfig1-dev:i386 libfreetype6-dev:i386 bundler git curl build-essential
vim zlib1g-dev wget libjansson-dev:i386 libspeex-dev:i386 libspeexdsp-dev:i386
cmake libsdl2-dev:i386 libsdl2-ttf-dev:i386 pkg-config:i386 g++-6-multilib
gcc-6-multilib lib32gcc-6-dev libpng12-dev:i386  

