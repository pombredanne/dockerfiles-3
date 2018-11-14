# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Hoat Le "hoatle@teracy.com"  
RUN apt-get update && apt-get install -y nginx  
RUN echo 'Hi, I am in your container' \  
>/usr/share/nginx/html/index.html  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-h"]  

