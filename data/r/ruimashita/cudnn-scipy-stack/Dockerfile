FROM ruimashita/cudnn  
  
MAINTAINER takuya.wakisaka@moldweorp.com  
  
# intall python  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python \  
python-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
# install pip  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
  
# Fix: InsecurePlatformWarning  
#
http://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libffi-dev \  
libssl-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& pip install --no-cache-dir ndg-httpsclient  
  
  
# install numpy  
RUN pip install --no-cache-dir numpy  
  
  
# install scipy  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libatlas-base-dev \  
gfortran \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& pip install --no-cache-dir scipy  
  
  
# install matplotlib  
RUN pip install --no-cache-dir matplotlib  
  
  
# install ipython  
RUN pip install --no-cache-dir ipython  
  
  
# install pandas  
RUN pip install --no-cache-dir pandas  
  
  
# install sympy  
RUN pip install --no-cache-dir sympy  
  
  
# install nose  
RUN pip install --no-cache-dir nose  

