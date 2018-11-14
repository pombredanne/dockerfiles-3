FROM alpine:3.7  
MAINTAINER Gaganpreet <gaganpreet.arora@gmail.com>  
  
RUN \  
echo "Installing packages" && \  
apk add --no-cache \  
ca-certificates \  
mediainfo \  
fcgi \  
rtorrent \  
screen \  
nodejs \  
python \  
nodejs-npm \  
make \  
g++ \  
gcc \  
git \  
nginx  
  
WORKDIR /usr/src/flood  
  
RUN git clone https://github.com/jfurrow/flood.git /usr/src/flood  
  
COPY flood.config.js /usr/src/flood/config.js  
  
RUN npm install && npm cache clean --force  
  
RUN npm run build  
  
RUN rm /etc/nginx/conf.d/*  
  
COPY flood.nginx.conf /etc/nginx/conf.d/  
  
RUN mkdir -p /run/nginx  
  
EXPOSE 80  
VOLUME ["/flood"]  
  
CMD ["sh", "-c", "nginx && npm start"]  

