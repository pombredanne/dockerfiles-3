FROM ubuntu:14.04  
MAINTAINER Shigemasa Watanabe <shigemasa.watanabe@gu3.co.jp>  
  
RUN locale-gen ja_JP.UTF-8 \  
&& update-locale LC_ALL=ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV OTP_VERSION 20.0  
ENV ELIXIR_VERSION 1.5.0  
ENV GITLFS_VERSION 1.5.2  
ENV DOCKER_COMPOSE_VERSION 1.15.0  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
git \  
curl \  
libssl-dev \  
ncurses-dev \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN curl -sSL "http://www.erlang.org/download/otp_src_${OTP_VERSION}.tar.gz"
-o /usr/local/src/otp_src_${OTP_VERSION}.tar.gz \  
&& cd /usr/local/src \  
&& echo '4f0bad82024bb99210d8960f60b0e14821dcf939 *otp_src_20.0.tar.gz' |
sha1sum -c \  
&& tar xf otp_src_${OTP_VERSION}.tar.gz \  
&& cd otp_src_${OTP_VERSION} \  
&& ./configure --prefix=/opt/erlang-${OTP_VERSION} \  
\--enable-kernel-poll \  
\--enable-hipe \  
\--enable-dirty-schedulers \  
\--enable-smp-support \  
\--enable-m64-build \  
\--enable-sharing-preserving \  
\--without-javac \  
\--disable-native-libs \  
\--disable-vm-probes \  
\--disable-megaco-flex-scanner-lineno \  
\--disable-megaco-reentrant-flex-scanner \  
\--disable-sctp \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf otp_src_${OTP_VERSION} \  
&& rm otp_src_${OTP_VERSION}.tar.gz  
  
ENV PATH /opt/erlang-${OTP_VERSION}/bin:$PATH  
  
  
ENV PREFIX /opt/elixir-$ELIXIR_VERSION  
  
RUN curl -sSL https://github.com/elixir-
lang/elixir/archive/v$ELIXIR_VERSION.tar.gz -o
/usr/local/src/elixir-$ELIXIR_VERSION.tar.gz \  
&& cd /usr/local/src \  
&& echo '258f3ddf367706747e055977ddad117372019124 *elixir-1.5.0.tar.gz' |
sha1sum -c \  
&& tar xf elixir-$ELIXIR_VERSION.tar.gz \  
&& cd elixir-$ELIXIR_VERSION \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf elixir-$ELIXIR_VERSION \  
&& rm -rf elixir-$ELIXIR_VERSION.tar.gz  
  
ENV PATH /opt/elixir-${ELIXIR_VERSION}/bin:$PATH  
  
  
ENV PREFIX /opt/git-lfs-$GITLFS_VERSION  
  
RUN curl -sSL https://github.com/git-lfs/git-
lfs/releases/download/v$GITLFS_VERSION/git-lfs-linux-
amd64-$GITLFS_VERSION.tar.gz -o /usr/local/src/git-lfs-linux-
amd64-$GITLFS_VERSION.tar.gz \  
&& cd /usr/local/src \  
&& echo '022a14ecafe4da0f637551c9971bdaabc1358395ede3611571cbe863e02a78c7
*git-lfs-linux-amd64-1.5.2.tar.gz' | sha256sum -c \  
&& tar xf git-lfs-linux-amd64-$GITLFS_VERSION.tar.gz \  
&& cd git-lfs-$GITLFS_VERSION \  
&& ./install.sh \  
&& cd .. \  
&& rm -rf git-lfs-$GITLFS_VERSION \  
&& rm -rf git-lfs-linux-amd64-$GITLFS_VERSION.tar.gz  
  
ENV PATH /opt/git-lfs-${GITLFS_VERSION}/bin:$PATH  
  
  
RUN apt-get update \  
&& apt-get install -y \  
libpython-dev \  
libyaml-dev \  
python-pip \  
&& pip install --upgrade pip \  
&& pip install awscli \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN curl -L
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
WORKDIR /  

