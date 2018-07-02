FROM resin/rpi-raspbian:stretch

MAINTAINER Ericmas001

ENV ON=18
ENV OFF=16
ENV URL=PROVIDE_ME
ENV KEY=PROVIDE_ME

VOLUME /logs /config/ /pics

RUN apt-get update
RUN apt-get install \
	python \
	python-dev \
	python-setuptools \
	python-pip \
    python-rpi.gpio \
	-y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel
RUN pip install pip-upgrade-outdated
RUN pip_upgrade_outdated

RUN echo "Test1"
ADD entrypoint.sh /entrypoint.sh
COPY exec/*.py /exec/

CMD ["/bin/bash", "/entrypoint.sh"]