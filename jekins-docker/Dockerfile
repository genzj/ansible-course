FROM jenkins/jenkins:lts

USER root
COPY sources.list /etc/apt/sources.list
RUN apt-get update && \
      apt-get install -y python3 python3-pip

RUN pip3 install --index-url=https://mirrors.aliyun.com/pypi/simple/ ansible
USER jenkins

COPY plugins.txt /tmp/plugins.txt

RUN /usr/local/bin/install-plugins.sh < /tmp/plugins.txt

