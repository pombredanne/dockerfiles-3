# Dockerfile for aroma test installation under neurodebian/ubuntu  
FROM neurodebian:xenial  
MAINTAINER Ron Hartley-Davies (rtrhd@bristol.ac.uk)  
LABEL version="aroma-0.4.0"  
  
# Rewrite sources list as contrib and non-free not included  
RUN echo 'deb http://neuro.debian.net/debian xenial main contrib non-free' >
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN echo 'deb http://neuro.debian.net/debian data main contrib non-free' >>
/etc/apt/sources.list.d/neurodebian.sources.list  
  
# Dependencies: python packages, fsl, and testing tools  
RUN apt-get update && apt-get install -y \  
bzip2 \  
curl \  
fsl-core \  
fsl-mni152-templates \  
make \  
python-nibabel \  
python-nose \  
python-numpy \  
python-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copy src tree into place and run package install  
RUN useradd --create-home aroma  
COPY . /home/aroma/icaaroma  
WORKDIR /home/aroma/icaaroma  
RUN python setup.py install  
  
# do this explicitly as COPY doesn't respect USER command  
RUN chown -R aroma /home/aroma/icaaroma  
  
# User and environment to run with  
USER aroma  
ENV FSLDIR /usr/share/fsl/5.0  
ENV LD_LIBRARY_PATH /usr/lib/fsl/5.0  
ENV FSLOUTPUTTYPE NIFTI_GZ  
  
# Default command for "docker run" (nb aroma is on the path)  
# Other commands such as 'make tests' can be run explicitly  
CMD ["aroma", "--help"]  
  

