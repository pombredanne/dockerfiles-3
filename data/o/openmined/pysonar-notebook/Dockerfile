FROM openmined/pysyft:hydrogen  
RUN ["apk", "add", "--no-cache", "python3", "python3-dev", "musl-dev", "linux-
headers", "g++", "lapack-dev", "gfortran", "gmp-dev", "mpfr-dev", "mpc1-dev",
"make"]  
  
RUN ["mkdir", "/pysonar"]  
COPY requirements.txt /pysonar  
RUN ["pip3", "install", "numpy"]  
RUN ["pip3", "install", "scipy"]  
RUN ["pip3", "install", "-r", "/pysonar/requirements.txt"]  
  
# install pySonar lib  
COPY . /pysonar  
WORKDIR /pysonar  
RUN ["python3", "setup.py", "install"]  
  
# copy notebook code  
RUN ["pip3", "install", "jupyter", "notebook"]  
RUN ["mkdir", "/notebooks"]  
COPY notebooks /notebooks  
COPY jupyter_notebook_config.py /notebooks/  
  
# import abi via NPM module  
RUN apk add --update nodejs nodejs-npm git && \  
make import-abi && \  
cp -r /pysonar/abis /abis  
  
WORKDIR /notebooks  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--config=./jupyter_notebook_config.py", "--allow-
root"]

