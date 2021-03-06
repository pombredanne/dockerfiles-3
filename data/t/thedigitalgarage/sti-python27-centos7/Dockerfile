# This image provides a Python 2.7 environment you can use to run your Python  
# applications.  
FROM centos/s2i-base-centos7  
  
EXPOSE 8080  
  
ENV PYTHON_VERSION=2.7 \  
PATH=$HOME/.local/bin/:$PATH \  
PYTHONUNBUFFERED=1 \  
PYTHONIOENCODING=UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
PIP_NO_CACHE_DIR=off  
  
ENV SUMMARY="Platform for building and running Python $PYTHON_VERSION
applications" \  
DESCRIPTION="Python $PYTHON_VERSION available as docker container is a base
platform for \  
building and running various Python $PYTHON_VERSION applications and
frameworks. \  
Python is an easy to learn, powerful programming language. It has efficient
high-level \  
data structures and a simple but effective approach to object-oriented
programming. \  
Python's elegant syntax and dynamic typing, together with its interpreted
nature, \  
make it an ideal language for scripting and rapid application development in
many areas \  
on most platforms."  
  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$SUMMARY" \  
io.k8s.display-name="Python 2.7" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,python,python27,rh-python27" \  
com.redhat.component="python27-docker" \  
name="centos/python-27-centos7" \  
version="2.7" \  
release="1" \  
maintainer="SoftwareCollections.org <sclorg@redhat.com>"  
  
USER root  
  
RUN yum -y update  
  
RUN yum install -y centos-release-scl && \  
INSTALL_PKGS="libjpeg-turbo libjpeg-turbo-devel python27 python27-python-devel
python27-python-setuptools \  
python27-python-pip nss_wrapper httpd24 httpd24-httpd-devel httpd24-mod_ssl
httpd24-mod_auth_kerb \  
httpd24-mod_ldap httpd24-mod_session atlas-devel gcc-gfortran libffi-devel
libtool-ltdl" && \  
yum install -y \--setopt=tsflags=nodocs \--enablerepo=centosplus $INSTALL_PKGS
&& \  
rpm -V $INSTALL_PKGS && \  
# Remove centos-logos (httpd dependency, ~20MB of graphics) to keep image  
# size smaller.  
rpm -e --nodeps centos-logos && \  
yum clean all -y  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH.  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
# Copy extra files to the image.  
COPY ./root/ /  
  
# Create a Python virtual environment for use by any application to avoid  
# potential conflicts with Python packages preinstalled in the main Python  
# installation.  
RUN source scl_source enable python27 && \  
virtualenv /opt/app-root  
  
# In order to drop the root user, we have to make some directories world  
# writable as OpenShift default security model is to run the container under  
# random UID.  
RUN chown -R 1001:0 /opt/app-root && chmod -R ug+rwx /opt/app-root  
  
USER 1001  
  
# Set the default CMD to print the usage of the language image.  
CMD $STI_SCRIPTS_PATH/usage  

