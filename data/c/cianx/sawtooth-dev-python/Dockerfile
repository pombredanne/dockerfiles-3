# Copyright 2017 Intel Corporation  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#
------------------------------------------------------------------------------  
# Description:  
# Builds an image to be used when developing in Python. The default CMD is to  
# run build_python.  
#  
# The image is also used by unit and integration tests. Docker is used to  
# interact with and orchestrate the creation of other docker containers.  
#  
# Build:  
# $ cd sawtooth-core/docker  
# $ docker build . -f sawtooth-dev-python -t sawtooth-dev-python  
#  
# Run:  
# $ cd sawtooth-core  
# $ docker run -v $(pwd):/project/sawtooth-core \  
# -v /var/run/docker.sock:/var/run/docker.sock sawtooth-dev-python  
  
FROM ubuntu:xenial  
  
LABEL "install-type"="mounted"  
  
RUN echo "deb http://repo.sawtooth.me/ubuntu/ci xenial universe" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8AA7AF1F1091A5FD \  
&& apt-get update \  
&& apt-get install -y -q \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
inetutils-ping \  
libffi-dev \  
libssl-dev \  
pep8 \  
python3-aiodns=1.1.1-1 \  
python3-aiohttp=1.3.5-1 \  
python3-aiopg \  
python3-async-timeout=1.2.0-1 \  
python3-bitcoin=1.1.42-1 \  
python3-cbor \  
python3-cchardet=2.0a3-1 \  
python3-chardet=2.3.0-1 \  
python3-colorlog \  
python3-cov-core \  
python3-cryptography-vectors=1.7.2-1 \  
python3-cryptography=1.7.2-1 \  
python3-dev \  
python3-grpcio-tools=1.1.3-1 \  
python3-grpcio=1.1.3-1 \  
python3-lmdb=0.92-1 \  
python3-multidict=2.1.4-1 \  
python3-netifaces=0.10.4-0.1build2 \  
python3-nose2 \  
python3-pip \  
python3-protobuf \  
python3-psycopg2 \  
python3-pycares=2.1.1-1 \  
python3-pyformance \  
python3-pytest-runner=2.6.2-1 \  
python3-pytest=2.9.0-1 \  
python3-pytz=2016.10-1 \  
python3-requests \  
python3-secp256k1=0.13.2-1 \  
python3-setuptools-scm=1.15.0-1 \  
python3-six=1.10.0-1 \  
python3-toml \  
python3-yaml \  
python3-yarl=0.10.0-1 \  
python3-zmq \  
software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip3 install \  
pylint \  
bandit \  
coverage --upgrade  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update && apt-get install -y -q \  
docker-ce \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4004/tcp  
EXPOSE 8080  
  
RUN mkdir -p /project/sawtooth-core/ \  
&& mkdir -p /var/log/sawtooth \  
&& mkdir -p /var/lib/sawtooth \  
&& mkdir -p /etc/sawtooth \  
&& mkdir -p /etc/sawtooth/keys  
  
ENV PATH=$PATH:/project/sawtooth-core/bin  
  
WORKDIR /project/sawtooth-core  
CMD build_python  

