FROM php:5.6-apache  
  
RUN touch /usr/local/etc/php/conf.d/upload-limit.ini \ && echo
"upload_max_filesize = 32M" >> /usr/local/etc/php/conf.d/upload-limit.ini \ &&
echo "post_max_size = 32M" >> /usr/local/etc/php/conf.d/upload-limit.ini  
  
RUN a2enmod rewrite expires headers  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y apt-utils libpng12-dev libjpeg-dev &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache  
  
RUN apt-get update && apt-get install -y unzip rsync && rm -r
/var/lib/apt/lists/*  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.6  
ENV WORDPRESS_SHA1 830962689f350e43cd1a069f3a4f68a44c0339c8  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

