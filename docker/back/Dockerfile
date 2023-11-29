FROM python:3.10

WORKDIR /app/back

ADD ./back /app/back
ADD ./docker/back/wsgi-entrypoint.sh /app

RUN pip install --no-cache-dir -r /app/back/requirements.txt