############################################################  
# Dockerfile to build HTSeq container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:12.04  
  
# File Author / Maintainer  
MAINTAINER Kathrin Klee  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install Latex  
RUN apt-get install --yes build-essential python2.7-dev python-numpy python-
matplotlib python-pip  
  
# Download and uncompress HTSeq archive  
ADD HTSeq-0.6.1p1.tar.gz /tmp/  
  
# Install HTSeq  
RUN cd /tmp/* && python setup.py build && python setup.py install  
  
# Install pysam  
RUN pip install 'pysam'  
  
# Cleanup  
RUN apt-get clean  
RUN rm -rf /tmp/*  

