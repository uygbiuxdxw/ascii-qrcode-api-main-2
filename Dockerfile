FROM debian:11
LABEL maintainer="s@mck.la"
ARG MY_APP_PATH=/opt/qr2ascii-api

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ntp python3 pip curl \
    && mkdir -p ${MY_APP_PATH}/data

ADD main.py convert.py requirements.txt run.py ${MY_APP_PATH}
RUN pip install -r ${MY_APP_PATH}/requirements.txt
WORKDIR ${MY_APP_PATH}


VOLUME [${MY_APP_PATH}]

ENTRYPOINT /usr/bin/python3 -u run.py

EXPOSE 8000/tcp
