FROM composer:latest AS composer  
  
COPY typo3 /app  
  
RUN composer install --no-ansi --no-interaction --no-dev --no-progress
--classmap-authoritative --ignore-platform-reqs  
  
RUN composer exec typo3cms install:generatepackagestates \  
&& mkdir -p configuration \  
&& ln -s ../../configuration/LocalConfiguration.php
web/typo3conf/LocalConfiguration.php \  
&& ln -s ../../configuration/AdditionalConfiguration.php
web/typo3conf/AdditionalConfiguration.php \  
&& ln -s ../../configuration/AdditionalFactoryConfiguration.php
web/typo3conf/AdditionalFactoryConfiguration.php \  
&& ln -s ../../configuration/realurl_conf.php web/typo3conf/realurl_conf.php  
  
FROM t3easy/php:7.2  
  
ENV TYPO3_CONTEXT Development  
  
COPY \--chown=82 \--from=composer /app .  
  
ENV PATH "/app/vendor/bin:$PATH"  

