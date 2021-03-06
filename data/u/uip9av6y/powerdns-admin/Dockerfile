FROM alpine:3.7  
ARG FLAVOUR  
  
ENV APP_VERSION=2018.03.28.1  
ENV APP_HOME=/app  
WORKDIR ${APP_HOME}  
RUN set -xe; \  
addgroup -S www-data \  
&& adduser -S -D -H -h ${APP_HOME} -s /sbin/nologin -G www-data www-data \  
&& case "${FLAVOUR}" in \  
odbc) build_deps='unixodbc-dev'; run_deps='unixodbc'; pip_deps='pyodbc' ;; \  
mssql) build_deps='freetds-dev'; run_deps='freetds'; pip_deps='pymssql' ;; \  
mysql) build_deps='mariadb-dev'; run_deps='mariadb-client-libs';
pip_deps='MySQL-python' ;; \  
pgsql) build_deps='postgresql-dev'; run_deps='libpq'; pip_deps='psycopg2' ;; \  
sqlite3) build_deps=''; run_deps=''; pip_deps='noop' ;; \  
*) echo "unsupported flavour ${FLAVOUR}"; exit 1 ;; \  
esac \  
&& apk add --no-cache \  
uwsgi-python \  
python2 \  
py2-pip \  
libressl \  
libldap \  
libxslt \  
xmlsec \  
uwsgi \  
curl \  
$run_deps \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
python2-dev \  
libxml2-dev \  
xmlsec-dev \  
libffi-dev \  
openldap-dev \  
$build_deps \  
&& mkdir -p \  
"${APP_HOME}/migrations" \  
"${APP_HOME}/uploads" \  
"${APP_HOME}/saml" \  
&& curl -sSL "https://github.com/thomasDOTde/PowerDNS-
Admin/archive/${APP_VERSION}.tar.gz" \  
| tar -xzf - --strip-components 1 \  
&& find . -type f -iname '*.psd' -delete \  
&& find . -type d -name examples -exec rm -rf {} + \  
&& pip2 install \  
-r requirements.txt \  
&& pip2 install \  
# missing in requirements.txt; fix not released yet  
pytz \  
pyOpenSSL \  
$pip_deps \  
&& chown -R www-data:www-data \  
"${APP_HOME}" \  
&& apk del .build-deps  
  
EXPOSE 9191 9393  
COPY create_db_user.py \  
${APP_HOME}/  
COPY bin/ \  
/usr/local/bin/  
  
VOLUME [ \  
"${APP_HOME}/migrations", \  
"${APP_HOME}/uploads", \  
"${APP_HOME}/saml" \  
]  
HEALTHCHECK \--interval=1m --timeout=3s --start-period=10s \  
CMD curl -sf http://127.0.0.1:9393 || exit 1  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [ "uwsgi", "--master", "--processes=4", "--threads=2" ]  
  
ARG BUILD_DATE="1970-01-01T00:00:00Z"  
ARG VERSION="1.0.0"  
ARG VCS_URL="http://localhost/"  
ARG VCS_REF="master"  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="PowerDNS Admin" \  
org.label-schema.description="PowerDNS Web-GUI" \  
org.label-schema.url="https://github.com/thomasDOTde/PowerDNS-Admin" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vendor="Khanh Ngo" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/powerdns-admin/Dockerfile" \  
com.microscaling.license="MIT"

