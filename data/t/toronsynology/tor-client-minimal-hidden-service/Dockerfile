FROM alpine:latest  
RUN apk update  
RUN apk upgrade  
RUN apk add bash nano  
# RUN apk add build-base  
# RUN apk add openssl  
# RUN apk add zlib  
# Tor 2.9.10 requires libevent-2.1  
RUN apk add libevent --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/main/ --allow-untrusted  
  
# Alpine Linux package testing :
http://dl-4.alpinelinux.org/alpine/edge/testing/x86_64/  
RUN apk add tor --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/community/ --allow-untrusted  
  
EXPOSE 9150  
RUN rm /var/cache/apk/*  
  
ADD ./torrc /etc/tor/torrc  
  
USER tor  
CMD /usr/bin/tor -f /etc/tor/torrc  

