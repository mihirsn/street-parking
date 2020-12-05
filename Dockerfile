FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
		gcc \
		libc-dev \
	&& rm -rf /var/lib/apt/lists/*

ADD . /opt/
#RUN pip3 install -r requirements.txt
#RUN python3 seed_data.py

EXPOSE 5000
#ENTRYPOINT ["/sbin/init"]
