FROM jenkins/jenkins:2.113-alpine  
MAINTAINER juergen.seliger@gmail.com  
  
# if we want to install via apt  
USER root  
  
## jenkins plugins  
RUN /usr/local/bin/install-plugins.sh pipeline-stage-view handlebars workflow-
durable-task-step pipeline-milestone-step momentjs pipeline-stage-tags-
metadata docker-workflow plain-credentials pipeline-stage-step matrix-project
ace-editor workflow-job junit workflow-multibranch mailer pipeline-model-
definition cloudbees-folder pipeline-graph-analysis structs pipeline-github-
lib pipeline-rest-api ldap docker-slaves git-client script-security display-
url-api pam-auth ws-cleanup workflow-basic-steps github-branch-source
workflow-cps-global-lib pipeline-build-step workflow-aggregator git-server
github workflow-api windows-slaves email-ext token-macro authentication-tokens
branch-api git pipeline-input-step bouncycastle-api github-api pipeline-model-
declarative-agent durable-task ssh-slaves scm-api icon-shim gradle workflow-
support matrix-auth timestamper workflow-step-api workflow-cps antisamy-
markup-formatter jquery-detached resource-disposer credentials-binding docker-
commons workflow-scm-step pipeline-model-extensions credentials jackson2-api
ssh-credentials pipeline-model-api external-monitor-job ant build-timeout  
  
  
## jenkins-job-builder  
ENV VERSION 2.0.3  
  
RUN apk add \--no-cache python  
RUN apk add \--no-cache py-pip  
RUN pip install --upgrade pip  
RUN pip install jenkins-job-builder==${VERSION}  
  
  
#CMD ["gradle"]  
  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 4.6  
  
ARG
GRADLE_DOWNLOAD_SHA256=98bd5fd2b30e070517e03c51cbb32beee3e2ee1a84003a5a5d748996d4b1b915  
RUN set -o errexit -o nounset \  
&& echo "Installing build dependencies" \  
&& apk add \--no-cache --virtual .build-deps \  
ca-certificates \  
openssl \  
unzip \  
\  
&& echo "Downloading Gradle" \  
&& wget -O gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \  
\  
&& echo "Checking download hash" \  
&& echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum -c - \  
\  
&& echo "Installing Gradle" \  
&& unzip gradle.zip \  
&& rm gradle.zip \  
&& mkdir /opt \  
&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \  
&& ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle \  
\  
&& apk del .build-deps \  
\  
&& echo "Adding gradle user and group" \  
&& addgroup -S -g 1001 gradle \  
&& adduser -D -S -G gradle -u 1001 -s /bin/ash gradle \  
&& mkdir /home/gradle/.gradle \  
&& chown -R gradle:gradle /home/gradle \  
\  
&& echo "Symlinking root Gradle cache to gradle Gradle cache" \  
&& ln -s /home/gradle/.gradle /root/.gradle  
  
# Create Gradle volume  
USER gradle  
VOLUME "/home/gradle/.gradle"  
WORKDIR /home/gradle  
  
#RUN set -o errexit -o nounset \  
# && echo "Testing Gradle installation" \  
# && gradle --version  
#RUN apt-get update && apt-get install -y ruby  
##make more-thing-here  
# drop back to the regular jenkins user - good practice  
  
USER jenkins  

