FROM alpine:latest  
MAINTAINER "Tim Fall <tim@hashicorp.com>"  
ENV NOMAD_VERSION=0.4.1  
ENV
NOMAD_SHA256SUM=710ff3515bc449bc2a06652464f4af55f1b76f63c77a9048bc30d6fde284b441  
  
RUN apk add --update git bash wget  
  
ADD
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
./  
ADD
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_SHA256SUMS
./  
  
RUN sed -i '/nomad_${NOMAD_VERSION}_linux_amd64.zip/!d'
nomad_${NOMAD_VERSION}_SHA256SUMS  
RUN sha256sum -cs nomad_${NOMAD_VERSION}_SHA256SUMS  
RUN unzip nomad_${NOMAD_VERSION}_linux_amd64.zip -d /bin  
RUN rm -f nomad_${NOMAD_VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/bin/nomad"]  

