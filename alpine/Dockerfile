ARG  CODE_VERSION=3.7
FROM alpine:${CODE_VERSION}
LABEL maintainer="walmins@gmail.com"
# WORKDIR /app
ADD app/ /app

RUN apk add --no-cache --update python3 py-curl py-requests && \
	python3 -m ensurepip && \
	rm -r /usr/lib/python*/ensurepip && \
	pip3 install --upgrade pip setuptools && \
	if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
	if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
	rm -r /root/.cache
ENTRYPOINT ["/app/autoswitch-hiveOS.py"]
