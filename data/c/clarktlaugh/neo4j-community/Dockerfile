FROM java:8  
MAINTAINER Clark Laughlin, clark.laughlin@linaro.org  
  
RUN wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add - &&
\  
echo 'deb http://debian.neo4j.org/repo stable/' >
/etc/apt/sources.list.d/neo4j.list && \  
apt-get update ; apt-get install neo4j -y  
  
ADD launch.sh /  
RUN chmod +x /launch.sh && \  
apt-get clean && \  
echo "remote_shell_host=0.0.0.0" >> /var/lib/neo4j/conf/neo4j.properties  
  
RUN sed -i.bak
"s|dbms.security.auth_enabled=true|dbms.security.auth_enabled=false|"
/var/lib/neo4j/conf/neo4j-server.properties  
  
VOLUME /var/lib/neo4j/data  
  
EXPOSE 7474  
EXPOSE 1337  
WORKDIR /  
  
CMD ["/bin/bash", "-c", "/launch.sh"]  

