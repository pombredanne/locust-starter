FROM centos
MAINTAINER Vašek Pavlín <vasek@redhat.com>

ENV TEST=obsidian-backend

ENTRYPOINT ["entrypoint"]

RUN yum -y install epel-release &&\
    yum -y install python-pip gcc python-devel &&\
    yum clean all &&\
    pip install locustio &&\
    yum -y remove gcc epel-relase python2-pip cpp glibc-devel\
           glibc-headers kernel-headers\
           python-devel

COPY entrypoint.sh /usr/bin/entrypoint
RUN chmod +x /usr/bin/entrypoint

COPY locustfiles /opt/locustfiles

