FROM node:stretch  
MAINTAINER Lawrence Stubbs <technoexpressnet@gmail.com>  
  
COPY startmeshcentral.sh /  
RUN adduser --quiet meshserver \  
&& mkdir -p /home/meshserver/meshcentral-data \  
&& chmod +x /startmeshcentral.sh  
  
#RUN apt-get install -y mongodb  
COPY package.json /home/meshserver/  
COPY config.json /home/meshserver/meshcentral-data/  
RUN su - meshserver \  
&& cd /home/meshserver \  
&& npm install github:techno-express/MeshCentral  
  
ENV PORT 443  
ENV REDIRPORT 80  
ENV MPSPORT 4443  
ENV EMAIL mail@  
ENV HOST host.ltd  
ENV SMTP smtp.host.ltd  
ENV DB netdb  
ENV MONGODB "mongodb://127.0.0.1:27017/meshcentral"  
ENV MONGODBCOL "meshcentral"  
EXPOSE 25 80 443 4443 27017 27018  
ENTRYPOINT ["/startmeshcentral.sh"]  

