FROM node:9.5-alpine  
  
RUN apk update && \  
apk add --update --repository http://dl-3.alpinelinux.org/alpine/edge/testing
vips-tools vips-dev fftw-dev gcc g++ make libc6-compat && \  
apk add git && \  
apk add python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
rm -r /root/.cache && \  
rm -rf /var/cache/apk/*  
  
RUN npm install --global gatsby --no-optional gatsby@1.9  
RUN pip install awscli  
  
RUN mkdir -p /site  
WORKDIR /site  
VOLUME /site  
  

