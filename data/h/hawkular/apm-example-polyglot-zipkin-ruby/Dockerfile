#  
# Copyright 2015-2016 Red Hat, Inc. and/or its affiliates  
# and other contributors as indicated by the @author tags.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
FROM ruby:2.3.1  
MAINTAINER Pavol Loffay <ploffay@redhat.com>  
  
ENV APP_HOME /app/  
  
COPY Gemfile* $APP_HOME  
ADD *.ru $APP_HOME  
ADD *.rb $APP_HOME  
  
WORKDIR $APP_HOME  
RUN bundle install  
  
EXPOSE 3002  
CMD ["bundle", "exec" ,"rackup", "-p", "3002", "--host", "0.0.0.0", "-s",
"puma"]  

