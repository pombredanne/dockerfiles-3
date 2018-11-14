FROM debian:8.6  
MAINTAINER deathsea coder.deathsea@gmail.com  
RUN apt-get update && \  
apt-get install -y curl python-pip python-m2crypto libnet1 libnet1-dev
libpcap0.8 libpcap0.8-dev  
RUN export COW_INSTALLDIR=/usr/sbin && curl -L git.io/cow |bash  
COPY rc /root/.cow/  
RUN pip install shadowsocks==2.8.2  
COPY start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
CMD ["/usr/local/bin/start.sh"]  

