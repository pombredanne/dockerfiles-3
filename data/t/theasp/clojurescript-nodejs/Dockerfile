FROM node:latest  
MAINTAINER Andrew Phillips <theasp@gmail.com>  
  
WORKDIR /tmp  
ENV CLOJURE_VERSION=1.9.0.375  
# Download the whole repo as an archive  
RUN echo deb http://deb.debian.org/debian jessie-backports main >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -t jessie-backports -q -y install openjdk-8-jdk curl \  
&& npm install -g shadow-cljs \  
&& curl -s https://download.clojure.org/install/linux-
install-$CLOJURE_VERSION.sh | bash  

