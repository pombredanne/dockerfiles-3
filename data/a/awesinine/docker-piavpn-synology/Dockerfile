FROM ubuntu:14.04  
MAINTAINER "Ryan Morten <ryan.camus.morten@gmail.com>"  
ENV DEBIAN_FRONTEND noninteractive  
  
VOLUME ["/app/deluge","/torrents","/tv","/completed","test"]  
EXPOSE 8112 1080  
CMD ["/app/start.sh"]  
  
RUN echo "APT::Install-Recommends 0;" >> /etc/apt/apt.conf.d/01norecommends
&&\  
echo "APT::Install-Suggests 0;" >> /etc/apt/apt.conf.d/01norecommends &&\  
apt-get update &&\  
apt-get install -qy openvpn dante-server deluged deluge-web deluge-console
runit curl ca-certificates &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\  
mkdir -p /torrents &&\  
mkdir -p /tv &&\  
mkdir -p /completed &&\  
mkdir -p /incomplete  
  
ADD config/sockd/sockd.conf /etc/  
ADD config/openvpn/ /etc/openvpn/  
ADD service/ /etc/service/  
ADD app/ /app/  

