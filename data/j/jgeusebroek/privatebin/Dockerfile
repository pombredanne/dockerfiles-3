FROM alpine:latest  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
ARG VERSION=1.1.1  
ENV GID=991 UID=991  
RUN apk -U add \  
curl \  
nginx \  
php7-fpm \  
php7-gd \  
php7-mcrypt \  
php7-json \  
php7-zlib \  
php7-pdo \  
php7-pdo_mysql \  
supervisor \  
tini \  
ca-certificates \  
tar \  
&& mkdir privatebin && cd privatebin \  
&& curl -L -o privatebin.tar.gz
https://github.com/PrivateBin/PrivateBin/archive/$VERSION.tar.gz \  
&& tar xvzf privatebin.tar.gz --strip 1 \  
&& rm privatebin.tar.gz \  
&& mv cfg/conf.sample.php /privatebin \  
&& apk del tar ca-certificates curl libcurl \  
&& rm -f /var/cache/apk/*  
  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/php-fpm.conf /etc/php7/php-fpm.conf  
COPY files/supervisord.conf /usr/local/etc/supervisord.conf  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
VOLUME [ "/privatebin/data", "/privatebin/cfg" ]  
  
EXPOSE 80  
LABEL description "PrivateBin is a minimalist, open source online pastebin
where the server has zero knowledge of pasted data."  
CMD ["/sbin/tini","--","/entrypoint.sh"]  

