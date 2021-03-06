FROM pcic/geospatial-python  
MAINTAINER Mike McCann <mccann@mbari.org>  
  
# Modeled after http://michal.karzynski.pl/blog/2015/04/19/packaging-django-
applications-as-docker-container-images/  
# Additional requirements for stoqs not in pcic/geospatial-python  
RUN apt-get update && \  
apt-get -qq -y install \  
freetds-dev \  
git \  
gmt \  
libncurses-dev \  
postgresql-9.6 \  
time \  
wget  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
# Make sure python and python-config refer to corresponding Python 3 versions  
RUN cd /usr/bin/ &&\  
ln -fs python3 python &&\  
ln -fs python3-config python-config  
  
WORKDIR /srv  
  
# Symlink to requirements from docker directory used to minimize context  
COPY docker/requirements /requirements  
RUN /bin/bash -c 'pip install -r /requirements/production.txt'  
  
# NCAR's natgrid needed for contour plotting - several warnings/errors on
compiling that can be ignored  
RUN wget http://sourceforge.net/projects/matplotlib/files/matplotlib-
toolkits/natgrid-0.2/natgrid-0.2.1.tar.gz  
RUN tar -xzf natgrid-0.2.1.tar.gz  
RUN cd natgrid-0.2.1 && python setup.py install && cd ..  
  
# Connection to uwsgi/nginx  
COPY docker/docker-stoqs-uwsgi.ini /etc/uwsgi/django-uwsgi.ini  
  
CMD ["docker/stoqs-start.sh"]  
  

