FROM centos:centos7  
  
ENV PATH $PATH:/opt/couchbase-sync-gateway/bin  
  
# Install dependencies:  
# wget: for downloading Sync Gateway package installer  
RUN yum -y update && \  
yum install -y \  
wget && \  
yum clean all  
  
# Install Sync Gateway  
RUN wget http://packages.couchbase.com/releases/couchbase-sync-
gateway/1.4.1/couchbase-sync-gateway-community_1.4.1-3_x86_64.rpm && \  
rpm -i couchbase-sync-gateway-community_1.4.1-3_x86_64.rpm && \  
rm couchbase-sync-gateway-community_1.4.1-3_x86_64.rpm  
  
# Create directory where the default config stores memory snapshots to disk  
RUN mkdir /opt/couchbase-sync-gateway/data && \  
mkdir /etc/sync_gateway && touch /etc/sync_gateway/config.json  
  
# copy the default config into the container  
COPY scripts/entrypoint.sh /initSync  
  
RUN chmod +x /initSync  
  
# Invoke the sync_gateway executable by default  
ENTRYPOINT ["/initSync"]  
  
# Expose ports  
# port 4984: public port  
EXPOSE 4984 4985

