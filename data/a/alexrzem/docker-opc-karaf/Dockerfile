FROM java:openjdk-8  
MAINTAINER alexrzem  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV KARAF_VERSION=4.0.4  
RUN wget http://apache.openmirror.de/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz; \  
mkdir /opt/karaf; \  
tar --strip-components=1 -C /opt/karaf -xzf apache-
karaf-${KARAF_VERSION}.tar.gz; \  
rm apache-karaf-${KARAF_VERSION}.tar.gz; \  
mkdir /deploy; \  
sed -i 's/^\\(felix\\.fileinstall\\.dir\s*=\s*\\).*$/\1\/deploy/'
/opt/karaf/etc/org.apache.felix.fileinstall-deploy.cfg \  
/opt/karaf/bin/karaf  
  
VOLUME ["/deploy"]  
EXPOSE 1099 8101 44444  
ENTRYPOINT ["/opt/karaf/bin/karaf"]

