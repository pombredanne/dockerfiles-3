FROM ubuntu  
MAINTAINER John Sanabria - john.sanabria@correounivalle.edu.co  
RUN apt-get update  
RUN apt-get -y install build-essential git python-dev python-pip python-
virtualenv  
RUN pip install --upgrade pip  
RUN mkdir /source  
WORKDIR /source  
RUN git clone https://github.com/josanabr/autotune.git  
WORKDIR /source/autotune  
RUN make install  

