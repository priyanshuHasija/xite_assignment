FROM confluentinc/cp-kafka:6.0.0
USER root

COPY action_data.json /tmp/

RUN yum -y -qq update && \
	yum install -y -qq curl
    
#
# install jq to parse json within bash scripts
RUN curl -o /usr/local/bin/jq http://stedolan.github.io/jq/download/linux64/jq && \
  chmod +x /usr/local/bin/jq
