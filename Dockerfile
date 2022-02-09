FROM python:3.10-alpine3.15

LABEL mantainer="Eduardo Segura Richart <edusr@correo.ugr.es>"

WORKDIR /app

COPY poetry.lock pyproject.toml tasks.py /app/

RUN adduser -S tester && chown tester . && \
    apk update && \
    apk add curl

USER tester

ENV PATH="$PATH:/home/tester/.local/bin:/home/tester/.poetry/bin"

RUN pip3 install invoke && \
    invoke installpoetry && \
    poetry config virtualenvs.create false && \
    invoke installdeps

WORKDIR /app/test

ENTRYPOINT ["invoke", "test"]
