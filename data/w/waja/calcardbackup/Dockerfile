FROM alpine:3.7  
# Dockerfile Maintainer  
MAINTAINER Jan Wagner "waja@cyconet.org"  
ARG "BUILD_DATE=unknown"  
ARG "BUILD_VERSION=unknown"  
ARG "VCS_URL=unknown"  
ARG "VCS_REF=unknown"  
ARG "VCS_BRANCH=unknown"  
ENV GIT_PROJECT=BernieO/calcardbackup  
  
# See http://label-schema.org/rc1/ and https://microbadger.com/labels  
LABEL org.label-schema.name="calcardbackup - ownCloud/Nextcloud backup tool" \  
org.label-schema.description="backup calendars and addressbooks from a local
ownCloud/Nextcloud installation on Alpine Linux based container" \  
org.label-schema.vendor="Cyconet" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$BUILD_VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-branch=$VCS_BRANCH  
  
COPY ["run.sh", "/"]  
  
RUN apk --no-cache update && apk --no-cache upgrade && \  
# Install dependencies  
apk --no-cache add \--virtual build-dependencies ca-certificates tar curl jq
&& \  
# Create directory  
mkdir -p /opt/calcardbackup && cd /opt/calcardbackup && \  
# Download latest release  
curl -L $(curl -s https://api.github.com/repos/$GIT_PROJECT/releases/latest |
jq -r ".tarball_url") | tar xz --strip=1 && \  
# Remove build deps  
apk del build-dependencies && \  
# Install needed packages  
apk add \--update bash curl findutils mysql-client postgresql-client sqlite
gzip && rm -rf /var/cache/apk/* && \  
# Create backup dir and make our start script executable  
mkdir /backup  
  
VOLUME ["/backup"]  
  
CMD ["/run.sh"]  

