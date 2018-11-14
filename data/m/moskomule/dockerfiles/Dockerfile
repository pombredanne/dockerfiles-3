FROM ubuntu:latest  
RUN apt-get update && apt-get install -y wget bzip2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /opt  
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O miniconda.sh \  
&& bash miniconda.sh -b -p /opt/.miniconda \  
&& rm miniconda.sh  
ENV PATH="/opt/.miniconda/bin:$PATH"  
RUN conda install -y -q pytorch torchvision -c pytorch \  
&& pip install tqdm ipython \  
&& conda clean --all -y -q  

