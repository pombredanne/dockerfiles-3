FROM debian  
  
# Make sure the package repository is up to date.  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
ADD https://deb.nodesource.com/setup /tmp/node-setup.sh  
# Install JDK 7 (latest edition)  
RUN sh /tmp/node-setup.sh && apt-get install -y openjdk-7-jdk nodejs  
  
# Add user jenkins to the image  
RUN adduser --quiet jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

