FROM python

RUN export DOCKER_BUILDKIT=0
RUN export COMPOSE_DOCKER_CLI_BUILD=0


WORKDIR /app


COPY requeriments.txt requeriments.txt


RUN pip3 install -r  requeriments.txt

COPY . .
CMD gunicorn --bind 0.0.0.0:5050 wsgi:app

