FROM node:alpine  
LABEL Name=docktor Authors="@gwleclerc,@matcornic,@Thiht"  
  
WORKDIR /opt/docktor  
  
ENV GOPATH="/opt/go/"  
ENV DOCKTOR_PATH="${GOPATH}/src/github.com/soprasteria/docktor"  
ENV PATH "$PATH:$GOPATH/bin"  
COPY . "${DOCKTOR_PATH}"  
  
# 1. Install dependencies  
# 2. Build docktor  
# 3. Delete dependencies and temp files  
# Note : Just one layer for this steps to avoid dependencies being commited to
different layers,  
# resulting in a larger image.  
# Gopkg.in error : https://github.com/niemeyer/gopkg/issues/50  
RUN set -ex \  
&& apk add --no-cache curl \  
&& apk add --no-cache --virtual .build-deps \  
bash \  
go \  
git \  
python \  
make \  
g++ \  
&& go get -v github.com/kardianos/govendor \  
&& echo '{ "allow_root": true }' > /root/.bowerrc \  
&& git config --global http.https://gopkg.in.followRedirects true \  
\  
&& cd "${DOCKTOR_PATH}" \  
&& govendor sync -v \  
&& npm install \  
&& npm run build \  
&& mkdir -p /opt/docktor/client/dist \  
&& mv client/dist/* /opt/docktor/client/dist \  
&& mv docktor /opt/docktor/docktor \  
&& chmod +x /opt/docktor/docktor \  
\  
&& npm cache clean --force \  
&& apk del .build-deps \  
&& rm -rf "$GOPATH" \  
&& rm -rf /root && mkdir /root \  
&& rm -rf /usr/bin/node  
  
EXPOSE 8080  
ENTRYPOINT ["./docktor"]  
CMD ["serve"]  

