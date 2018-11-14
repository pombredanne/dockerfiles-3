FROM centos:7  
ENV PATH /opt/go/bin:${PATH}  
ENV GOROOT /opt/go  
ENV GOPATH /opt/gopath  
  
RUN yum install -y make \  
gcc \  
g++ \  
wget \  
git \  
nano \  
which \  
docker \  
libtool-ltdl \  
libtool-ltdl-devel  
  
RUN cd /tmp/ && curl -LO https://storage.googleapis.com/golang/go1.8.1.linux-
amd64.tar.gz \  
&& tar xf go1.8.1.linux-amd64.tar.gz -C /opt \  
&& rm /tmp/go1.8.1.linux-amd64.tar.gz  
  
RUN mkdir -p /opt/gopath/src/github.com/hyperledger  
RUN cd /opt/gopath/src/github.com/hyperledger \  
&& git clone https://github.com/hyperledger/fabric.git \  
&& cd fabric \  
&& git checkout v1.0.3  
RUN cd /opt/gopath/src/github.com/hyperledger/fabric \  
&& make configtxgen configtxlator cryptogen \  
&& cp build/bin/* /usr/local/bin/ \  
&& rm -rf build  

