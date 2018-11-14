FROM ubuntu:16.04  
MAINTAINER Wallies cam.parry@gmail.com  
  
LABEL Vendor="Wallies" \  
Name=openssl \  
Version=0.0.1  
  
ARG OPENSSL_VERSION=1.1.0b  
  
# default variables  
ENV SIZE 4096  
ENV KEY_NAME ecc  
ENV COUNTRY "UK"  
ENV STATE "Greater London"  
ENV LOCATION "London"  
ENV ORGANISATION "Redfog"  
ENV DAYS "365"  
ENV SUBJ "/C=$COUNTRY/ST=$STATE/L=$LOCATION/O=$ORGANISATION"  
ENV ALT_NAME "DNS:example.com,DNS:www.example.com"  
WORKDIR /tmp  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
ca-certificates checkinstall build-essential perl wget apt-utils \  
&& DEBIAN_FRONTEND=noninteractive apt-get --yes --force-yes build-dep openssl
\  
&& echo "Downloading openssl v${OPENSSL_VERSION} from
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz ..." \  
&& wget https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \  
&& tar -zxf openssl-${OPENSSL_VERSION}.tar.gz \  
&& cd /tmp/openssl-${OPENSSL_VERSION} \  
&& ./config --prefix=/usr/local \--openssldir=/usr/local/ssl\  
&& make \  
&& checkinstall \  
&& ln -s /usr/local/bin/openssl /usr/bin/openssl \  
&& rm -rf /tmp/openssl-${OPENSSL_VERSION} \  
&& apt-get purge -yqq build-essential checkinstall wget apt-utils \  
&& apt-get clean \  
&& apt-get autoremove -yqq \  
&& rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
RUN mkdir -p /certs /app/bin  
  
COPY init.sh /app/bin  
  
RUN chmod 750 /app/bin/init.sh  
  
# certificate directories  
WORKDIR /certs  
  
VOLUME ["/certs"]  
  
ENTRYPOINT ["/app/bin/init.sh"]  

