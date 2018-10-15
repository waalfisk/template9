FROM python:3-slim-stretch

#Requirements
RUN apt-get update \
 && apt-get install -y --no-install-recommends apt-utils \
 && apt-get install -y --no-install-recommends cron \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# with ugly fix from 
RUN apt-get update \
 && mkdir -p /usr/share/man/man1 \
 && mkdir -p /usr/share/man/man7 \
 && apt-get install -y --no-install-recommends postgresql-client \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

#install pypi packages
RUN pip install --upgrade pip \
 && pip install --no-cache-dir psycopg2-binary \
 && pip install --no-cache-dir python-dateutil \
 && rm -rf ~/.cache/pip

#mount point
RUN mkdir -p /data

#copy the script to docker
COPY script.sh /root/script.sh

#copy crontab file to cron folder, and access rights
COPY crontab /etc/cron.d/mycron
RUN chmod 0644 /etc/cron.d/mycron

#run SQL code on a remote PSQL server container 172.64.0.5
COPY install.sql /root/install.sql
#not reliable. Better run it manually: docker exec -it mytempl9 bash
#RUN /usr/bin/psql -h 172.64.0.5 -p 5432 -U postgres -w -f /root/install.sql

#copy python program
COPY script.py /root/script.py

#initialize log file, and run run cron at boot
RUN touch /var/log/cron.log
ENTRYPOINT cron && tail -f /var/log/cron.log
