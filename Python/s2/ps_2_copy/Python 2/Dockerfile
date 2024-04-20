FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_DONT_LOAD_ENV=1
ENV COMPOSE_DOCKER_CLI_BUILD=1
ENV DOCKER_BUILDKIT=1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

RUN apt-get update && apt-get install -y gnupg wget curl vim --no-install-recommends

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && apt-get install -qq libpq-dev python3-dev postgresql-client-13  make screen sqlite3
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*

RUN pip install feedparser
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./

# https://wsvincent.com/beginners-guide-to-docker/ - use of pipenv w/ Django
# Note that we added the --system tag so that software packages are available throughout the entire container,
# not within a virtual environment which is Pipenv’s default but doesn’t make sense here since the entire Docker container is a virtual environment.
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD pipenv run daphne -u /tmp/daphne.sock -p 8000 pd.asgi:application -b 0.0.0.0 -t 4000 --access-log /dev/stdout
