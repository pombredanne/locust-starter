FROM centos

RUN yum -y install epel-release &&\
    yum -y install python-pip gcc python-devel &&\
    yum clean all &&\
    pip install locustio &&\
    yum -y remove gcc epel-relase python2-pip cpp glibc-devel\
           glibc-headers kernel-headers\
           python-devel

COPY locustfiles /opt/locustfiles

ENV TEST=obsidian-backend

CMD locust -f /opt/locustfiles/$TEST.py